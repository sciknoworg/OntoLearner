# Copyright (c) 2025 SciKnowOrg
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABC
from collections import defaultdict
import json
import re
from typing import Any, Dict, List, Optional

import torch
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer

from ..data_structure import Document, PseudoSentence, SyntheticText2OntoData
from .batchifier import TaxonomyBatchifier


class SyntheticDocumentResponse(ABC):
    """Small validation helper for generated synthetic documents."""

    def __init__(self, title: str, fluent_passage_text: str):
        self.title = title.strip()
        self.fluent_passage_text = fluent_passage_text.strip()


class SyntheticGenerator(ABC):
    """Generate synthetic Text2Onto documents using a direct transformers backend."""

    def __init__(
            self,
            batch_size: int = 50,
            worker_count: int = 3,
            verbalizer: Any = None,
            model_id: str = "Qwen/Qwen2.5-0.5B-Instruct",
            token: str = "",
            device: str = "auto",
            max_new_tokens: int = 256,
            temperature: float = 0.2,
            top_p: float = 0.9,
            repetition_penalty: float = 1.05,
            generation_batch_size: Optional[int] = None,
            max_input_length: int = 2048,
            load_model: bool = True,
            extraction_method: str = "rule-based",
            openai_api_key: Optional[str] = None,
            openai_model: str = "gpt-4o-mini",
            is_chat_model: bool = True,
            min_pseudo_sentences: int = 5,
    ):
        if verbalizer is not None:
            import warnings

            warnings.warn(
                "SyntheticGenerator no longer uses DSPy verbalizers; the argument is ignored and kept only for compatibility.",
                DeprecationWarning,
                stacklevel=2,
            )

        self.batch_size = batch_size
        self.worker_count = worker_count
        self.model_id = model_id
        self.token = token
        self.device = device
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.repetition_penalty = repetition_penalty
        # Default to batch_size when not provided to avoid None in range() calls
        self.generation_batch_size = generation_batch_size or batch_size
        # self.max_context_items = max_context_items
        self.max_input_length = max_input_length
        self.extraction_method = extraction_method
        self.openai_api_key = openai_api_key
        self.openai_model = openai_model
        self.is_chat_model = is_chat_model
        self.min_pseudo_sentences = min_pseudo_sentences

        self.tokenizer = None
        self.model = None
        if load_model:
            self.load(model_id=model_id)

    def load(self, model_id: Optional[str] = None) -> None:
        resolved_model_id = model_id if model_id is not None else self.model_id
        if resolved_model_id is None:
            raise ValueError("A model_id must be provided to load the Text2Onto generator.")
        self.model_id = resolved_model_id

        tokenizer_kwargs = {"padding_side": "left", "trust_remote_code": True}
        if self.token:
            tokenizer_kwargs["token"] = self.token
        self.tokenizer = AutoTokenizer.from_pretrained(resolved_model_id, **tokenizer_kwargs)
        if getattr(self.tokenizer, "pad_token", None) is None:
            if getattr(self.tokenizer, "eos_token", None):
                self.tokenizer.pad_token = self.tokenizer.eos_token
            elif getattr(self.tokenizer, "unk_token", None):
                self.tokenizer.pad_token = self.tokenizer.unk_token
            else:
                raise ValueError(
                    "Tokenizer must define either an eos_token or unk_token so a pad token can be assigned.")

        model_kwargs: Dict[str, Any] = {"trust_remote_code": True}
        if self.token:
            model_kwargs["token"] = self.token

        use_cuda = self.device != "cpu" and torch.cuda.is_available()
        model_kwargs["dtype"] = torch.float16 if use_cuda else torch.float32
        model_kwargs["device_map"] = "auto" if use_cuda and torch.cuda.is_available() else "cpu"
        self.model = AutoModelForCausalLM.from_pretrained(resolved_model_id, **model_kwargs)
        self.model.eval()

    def generate_pseudo_sentences(self, parent_to_child: Dict[str, List]) -> List[PseudoSentence]:
        taxonomy_batcher = TaxonomyBatchifier(parent_to_child=parent_to_child, batch_size=self.batch_size)
        return taxonomy_batcher.batchify()

    @staticmethod
    def _looks_like_placeholder(label: str) -> bool:
        if not isinstance(label, str):
            return True
        stripped = label.strip()
        return bool(re.match(r"^N(?:[_-]|\d)", stripped))

    def _build_relational_context(self, batch_row: Dict[str, Any], child_to_parent: Dict[str, List[str]],
                                  relation_context: Dict[str, List[str]]) -> List[str]:
        context_lines: List[str] = []
        seen = set()

        def add_line(line: str) -> None:
            if line not in seen:  # and len(context_lines) < self.max_context_items:
                context_lines.append(line)
                seen.add(line)

        for term in batch_row.get("terms", []) or []:
            parents = child_to_parent.get(term, []) or []
            if parents:
                add_line(f"- term {term}: types/parents -> {', '.join(parents)}")
            for rel in relation_context.get(term, []) or []:
                add_line(f"- term {term}: related fact -> {rel}")

        for ont_type in batch_row.get("types", []) or []:
            parents = child_to_parent.get(ont_type, []) or []
            if parents:
                add_line(f"- type {ont_type}: parents -> {', '.join(parents)}")

        return context_lines

    def _build_prompt(self, row: Dict[str, Any], topic: str, child_to_parent: Dict[str, List[str]], relation_context: Dict[str, List[str]]) -> str:
        pseudo_sentences = row.get("pseudo_sentences", []) or []
        context_lines = self._build_relational_context(row, child_to_parent, relation_context)

        prompt_lines = [
            f"You are writing a short synthetic document for the {topic} topic.",
            "Use the pseudo sentences below as underlying factual constraints that must be true in your text.",
            "CRITICAL: Write a highly natural, informative passage that sounds like a real article, textbook, or domain text.",
            "DO NOT just list facts or use robotic phrasing like 'X is a subclass of' or 'X is an instance of Y'. Interweave the concepts naturally.",
            "You MUST explicitly include the exact names of every subject and object mentioned in the pseudo sentences.",
            "Return valid JSON only with keys: title, fluent_passage_text.",
            "Keep the title concise and descriptive.",
            "",
            "Pseudo sentences / Facts to convey:",
        ]

        prompt_lines.extend(f"- {sentence}" for sentence in pseudo_sentences)

        if context_lines:
            prompt_lines.extend(["", "Additional Ontology context (use for background):"])
            prompt_lines.extend(context_lines)

        prompt_lines.extend(
            [
                "",
                "Output format:",
                '{"title": "...", "fluent_passage_text": "..."}',
            ]
        )
        return "\n".join(prompt_lines)

    def _extract_json(self, text: str) -> Optional[Dict[str, Any]]:
        if self.extraction_method == "openai":
            try:
                import openai
                client = openai.OpenAI(api_key=self.openai_api_key)

                tools = [
                    {
                        "type": "function",
                        "function": {
                            "name": "extract_fields",
                            "description": "Extract structured data from text",
                            "parameters": {
                                "type": "object",
                                "properties": {
                                    "title": {
                                        "type": "string",
                                        "description": "The title of the passage"
                                    },
                                    "fluent_passage_text": {
                                        "type": "string",
                                        "description": "The cleaned and fluent version of the passage text"
                                    }
                                },
                                "required": ["title", "fluent_passage_text"]
                            }
                        }
                    }
                ]
                response = client.chat.completions.create(
                    model=self.openai_model,
                    messages=[
                        {"role": "system",
                         "content": "Extract the JSON object from the following text. Return valid JSON only, without any markdown formatting."},
                        {"role": "user", "content": text}
                    ],
                    tools=tools,
                    tool_choice={"type": "function", "function": {"name": "extract_fields"}}
                )
                tool_call = response.choices[0].message.tool_calls[0]
                arguments = json.loads(tool_call.function.arguments)
                return arguments
                # if response.choices[0].message.content:
                #     return json.loads(response.choices[0].message.content)
            except ImportError:
                print("[WARNING] openai package is not installed. Falling back to rule-based extraction.")
            except Exception as e:
                print(f"[ERROR] OpenAI JSON extraction failed: {e}. Falling back to rule-based extraction.")

        text = text.strip()
        if not text:
            return None

        candidate = text
        if candidate.startswith("```"):
            candidate = re.sub(r"^```(?:json)?\s*", "", candidate, flags=re.IGNORECASE)
            candidate = re.sub(r"\s*```$", "", candidate)

        start = candidate.find("{")
        end = candidate.rfind("}")
        if start == -1 or end == -1 or end <= start:
            return None

        try:
            return json.loads(candidate[start: end + 1])
        except Exception:
            return None

    def _validate_document(self, data: Dict[str, Any], row: Dict[str, Any], topic: str) -> SyntheticDocumentResponse:
        title = str(data.get("title", "")).strip()
        passage = str(data.get("fluent_passage_text", "")).strip()
        #         if not title or not passage:
        #             raise ValueError("Generated payload is missing title or passage text.")

        #         passage_lower = passage.lower()
        #         missing_required = [label for label in (row.get("terms", []) or []) + (row.get("types", []) or []) if label and label.lower() not in passage_lower]
        #         if missing_required:
        #             raise ValueError(f"Generated passage is missing required labels: {', '.join(missing_required[:6])}")

        #         if topic and topic.lower() not in passage_lower and topic.lower() not in title.lower():
        #             # The topic is soft guidance, so do not fail hard here; it is only used for repair.
        #             pass

        return SyntheticDocumentResponse(title=title, fluent_passage_text=passage)

    def _repair_generation(self, original_text: str, row: Dict[str, Any], topic: str, prompt: str) -> str:
        repair_prompt = "\n".join(
            [
                "The previous answer was invalid or incomplete.",
                "Rewrite it as valid JSON only with keys: title, fluent_passage_text.",
                "The new passage must explicitly include every required term and type, but it MUST be written naturally.",
                "DO NOT use robotic phrasing like 'is a subclass of' or 'is instance of'. Interweave them like a real educational text.",
                "",
                f"Topic: {topic}",
                "Pseudo sentences (facts to convey):",
                *(f"- {sentence}" for sentence in (row.get('pseudo_sentences', []) or [])),
                "",
                "Required exact words/labels:",
                ", ".join((row.get("terms", []) or []) + (row.get("types", []) or [])),
                "",
                "Original answer to repair:",
                original_text.strip(),
                "",
                "Base prompt:",
                prompt,
            ]
        )
        return repair_prompt

    def _generate_texts(self, prompts: List[str]) -> List[str]:
        # Route to the correct backend and return its outputs
        if self.is_chat_model:
            return self._generate_texts_chat_llm(prompts=prompts)
        return self._generate_texts_causal_llm(prompts=prompts)

    def _generate_texts_causal_llm(self, prompts: List[str]) -> List[str]:
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("SyntheticGenerator model must be loaded before generation.")

        encoded = self.tokenizer(
            prompts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=self.max_input_length,
        )
        encoded = {k: v.to(self.model.device) for k, v in encoded.items()}

        generation_kwargs: Dict[str, Any] = {
            "max_new_tokens": self.max_new_tokens,
            "pad_token_id": self.tokenizer.pad_token_id,
            "eos_token_id": self.tokenizer.eos_token_id,
            # "repetition_penalty": self.repetition_penalty,
        }
        # if self.temperature and self.temperature > 0:
        # generation_kwargs.update({"do_sample": True, "temperature": self.temperature, "top_p": self.top_p})
        # else:
        # generation_kwargs["do_sample"] = False

        outputs = self.model.generate(**encoded, **generation_kwargs)

        input_length = encoded["input_ids"].shape[1]
        generated_tokens = outputs[:, input_length:]
        return self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    def _generate_texts_chat_llm(self, prompts: List[str]) -> List[str]:
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("SyntheticGenerator model must be loaded before generation.")
        formatted_prompts = [
            self.tokenizer.apply_chat_template(
                [{"role": "user", "content": p}],
                tokenize=False,
                add_generation_prompt=True
            )
            for p in prompts
        ]
        encoded = self.tokenizer(
            formatted_prompts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=self.max_input_length,
        )
        encoded = {k: v.to(self.model.device) for k, v in encoded.items()}
        generation_kwargs: Dict[str, Any] = {
            "max_new_tokens": self.max_new_tokens,
            "pad_token_id": self.tokenizer.pad_token_id,
            "eos_token_id": self.tokenizer.eos_token_id,

            # sampling ON
            "do_sample": True,
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 20,

            "repetition_penalty": 1.0,

            # important for speed
            "use_cache": True,
        }
        outputs = self.model.generate(**encoded, **generation_kwargs)
        decoded = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
        responses = []
        for prompt, full_output in zip(formatted_prompts, decoded):
            responses.append(full_output[len(prompt):].strip())

        return responses

    def _generate_document_from_row(
            self,
            row: Dict[str, Any],
            topic: str,
            child_to_parent: Dict[str, List[str]],
            relation_context: Dict[str, List[str]],
    ) -> Document:
        prompt = self._build_prompt(row=row, topic=topic, child_to_parent=child_to_parent,
                                    relation_context=relation_context)
        last_error: Optional[Exception] = None

        for attempt in range(2):
            response_text = self._generate_texts([prompt])[0]
            response_payload = self._extract_json(response_text)

            try:
                if response_payload is None:
                    raise ValueError("Generated response is not valid JSON.")
                validated = self._validate_document(response_payload, row=row, topic=topic)
                return Document(id=row["id"], title=validated.title, text=validated.fluent_passage_text, row=row)
            except Exception as exc:
                last_error = exc
                if attempt == 0:
                    prompt = self._repair_generation(response_text, row, topic, prompt)

        raise RuntimeError(f"Unable to generate a valid synthetic document for {row.get('id')}: {last_error}")

    def worker(self, row: Dict[str, Any], topic: str, child_to_parent: Dict[str, List[str]],
               relation_context: Dict[str, List[str]]):
        try:
            return True, self._generate_document_from_row(row, topic, child_to_parent, relation_context)
        except Exception as exc:
            print(f"[ERROR] Processing failed for {row.get('id')}: {exc}")
            return False, None

    def generate_documents(self, pseudo_sentences: List[PseudoSentence], topic: str,
                           child_to_parent: Dict[str, List[str]], relation_context: Dict[str, List[str]]):
        generated_docs: List[Document] = []
        rows = [ps.model_dump() for ps in pseudo_sentences]

        for batch_start in tqdm(range(0, len(rows), self.generation_batch_size), desc="Processing batches"):
            batch_rows = rows[batch_start: batch_start + self.generation_batch_size]
            prompts = [self._build_prompt(row=row, topic=topic, child_to_parent=child_to_parent,
                                          relation_context=relation_context) for row in batch_rows]
            responses = self._generate_texts(prompts)

            for row, response_text, prompt in zip(batch_rows, responses, prompts):
                # try:
                response_payload = self._extract_json(response_text)
                if response_payload is None:
                    raise ValueError("Generated response is not valid JSON.")
                validated = self._validate_document(response_payload, row=row, topic=topic)
                generated_docs.append(
                    Document(id=row["id"], title=validated.title, text=validated.fluent_passage_text))
                print(">>> Generation was sucessful for doc: ", row["id"])
                # except Exception:
                #     try:
                #         repaired = self._generate_texts([self._repair_generation(response_text, row, topic, prompt)])[0]
                #         response_payload = self._extract_json(repaired) or {}
                #         validated = self._validate_document(response_payload, row=row, topic=topic)
                #         generated_docs.append(Document(id=row["id"], title=validated.title, text=validated.fluent_passage_text, row=row))
                #     except Exception as exc:
                #         print(f"[ERROR] Document generation failed for {row.get('id')}: {exc}")

        return generated_docs

    def _merge_small_pseudo_sentences(self, pseudo_sentences: List[PseudoSentence], min_pseudo_sentences: int = 5) -> List[PseudoSentence]:
        merged_batches = []
        current_sentences = []
        current_terms = set()
        current_types = set()

        for batch in pseudo_sentences:
            current_sentences.extend(batch.pseudo_sentences)
            current_terms.update(batch.terms)
            current_types.update(batch.types)

            if len(current_sentences) >= min_pseudo_sentences:
                merged_batches.append(
                    PseudoSentence(
                        id=f"merged_{len(merged_batches)}",
                        pseudo_sentences=current_sentences,
                        terms=list(current_terms),
                        types=list(current_types)
                    )
                )
                current_sentences = []
                current_terms = set()
                current_types = set()

        if current_sentences:
            if merged_batches:
                merged_batches[-1].pseudo_sentences.extend(current_sentences)
                merged_batches[-1].terms.extend(list(current_terms))
                merged_batches[-1].types.extend(list(current_types))
                merged_batches[-1].terms = list(set(merged_batches[-1].terms))
                merged_batches[-1].types = list(set(merged_batches[-1].types))
            else:
                merged_batches.append(
                     PseudoSentence(
                        id="merged_0",
                        pseudo_sentences=current_sentences,
                        terms=list(current_terms),
                        types=list(current_types)
                    )
                )

        return merged_batches

    def generate(self, ontological_data: Any, topic: str) -> SyntheticText2OntoData:
        term_types = ontological_data.term_typings
        taxonomic_relations = ontological_data.type_taxonomies
        non_taxonomic_relations = getattr(ontological_data, "type_non_taxonomic_relations", None)

        parent_to_child = defaultdict(list)
        child_to_parent = defaultdict(set)
        relation_context = defaultdict(list)

        for tt in term_types:
            for a_type in tt.types:
                if self._looks_like_placeholder(a_type) or self._looks_like_placeholder(tt.term):
                    continue
                parent_to_child[a_type].append([tt.ID, tt.term, "is instance of"])
                child_to_parent[tt.term].add(a_type)

        for tr in taxonomic_relations.taxonomies:
            if self._looks_like_placeholder(tr.parent) or self._looks_like_placeholder(tr.child):
                continue
            parent_to_child[tr.parent].append([tr.ID, tr.child, "is subclass of"])
            child_to_parent[tr.child].add(tr.parent)

        if non_taxonomic_relations is not None:
            for rel in non_taxonomic_relations.non_taxonomies:
                if self._looks_like_placeholder(rel.head) or self._looks_like_placeholder(
                        rel.tail) or self._looks_like_placeholder(rel.relation):
                    continue
                relation_context[rel.head].append(f"{rel.relation} {rel.tail}")
                relation_context[rel.tail].append(f"{rel.head} {rel.relation} {rel.tail}")

        child_to_parent = {k: sorted(v) for k, v in child_to_parent.items()}
        relation_context = {k: sorted(set(v)) for k, v in relation_context.items()}

        pseudo_sentences = self.generate_pseudo_sentences(parent_to_child=parent_to_child)
        pseudo_sentences = self._merge_small_pseudo_sentences(pseudo_sentences, min_pseudo_sentences=self.min_pseudo_sentences)

        generated_docs = self.generate_documents(
            pseudo_sentences=pseudo_sentences,
            topic=topic,
            child_to_parent=child_to_parent,
            relation_context=relation_context,
        )

        return SyntheticText2OntoData(
            child_to_parent=child_to_parent,
            pseudo_sentences=pseudo_sentences,
            generated_docs=generated_docs,
        )
