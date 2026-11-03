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

"""
ProTeam learner for primitive ontology construction and expansion.

This implementation integrates the original ProTeam submission to the
LLMs4OL 2026 competition into the OntoLearner framework.

The submitted retrieval-augmented generation, few-shot prompting,
ontology extraction, pattern-based term typing, and vocabulary-constrained
filtering methodologies are preserved while adapting the implementation
to OntoLearner's PrimitiveOntologyLearner interface.
"""

import json
import re
from typing import Any, Dict, List, Optional
import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForCausalLM, AutoTokenizer

from ...base import PrimitiveOntologyLearner


class ProTeamLearner(PrimitiveOntologyLearner):
    """
    Retrieval-augmented learner for primitive ontology construction and expansion.

    This implementation follows the ProTeam submission with Qwen2.5-14B-Instruct
    and sentence-based retrieval of labeled ontology examples. For ontology
    expansion, it combines generated triples with pattern-based term typing
    and vocabulary-constrained filtering.
    """

    _SYSTEM_PROMPT_A = """You are an expert ontology engineer. Extract ALL ontology triples from the passage.

A triple is [subject, relation, object].

HOW TO EXTRACT:
1. Read the passage. It explicitly states relationships between concepts.
2. Extract EVERY relationship the text states — do not skip any, do not invent any
   that the text does not state.
3. Copy each subject and object EXACTLY as it appears in the text: preserve spelling,
   spacing, hyphens, parentheses, numbers, and codes. Do NOT merge words, do NOT
   drop spaces, do NOT paraphrase. If the text says "provolone cheese", output
   "provolone cheese" — never "provolonecheese".

RELATION MAPPING (map the text's wording to these exact relation strings):
  "subclass of" / "type of" / "kind of" / "category of"  -> "is-a"
  "instance of" / "example of" / "is a valid instance"    -> "instance-of"
  "disjoint" / "mutually exclusive"                        -> "disjoint with"
  "equivalent" / "same as" / "equal to"                    -> "equivalent class"
  "part of" / "component of"                               -> "part_of"
  "has part" / "contains"                                  -> "has part"
Use "is-a" as the default for hierarchy/subtype relations (it is by far the most common).

OUTPUT:
  Output ONLY a JSON array of [subject, relation, object]. No explanation, no markdown.
  Format: [["exact term", "is-a", "exact parent term"], ...]"""

    _SYSTEM_PROMPT_B = """You are an expert ontology engineer performing ONTOLOGY EXTENSION.

You will receive:
1. A text passage (context)
2. An existing ontology (initial triples)
3. New terms that need to be typed (terms) — SHORT noun phrases
4. Available types for typing (types) — SHORT noun phrases

Your task: Generate the EXTENDED triples that ADD new knowledge.

CRITICAL RULES:
1. Only use terms/types from the provided lists — do NOT invent new ones.
2. Use "is-a" for subclass relationships (most common).
3. Do NOT repeat triples already in the initial ontology.
4. Output ONLY a JSON array of [subject, relation, object]. No explanation.

Valid relations: "is-a", "instance-of", "disjoint with", "equivalent class", "has part", "part_of"

Format: [["subj", "rel", "obj"], ...]"""

    def __init__(
        self,
        model_id: str = "Qwen/Qwen2.5-14B-Instruct",
        retriever_model_id: str = "sentence-transformers/all-MiniLM-L6-v2",
        device: str = "cuda",
        batch_size: int = 10,
        max_input_length: int = 3072,
    ) -> None:
        """
        Initialize the learner with the model and retrieval configuration.

        Args:
            model_id: Hugging Face model identifier or local model path.
            retriever_model_id: Sentence embedding model for example retrieval.
            device: Device used for model inference.
            batch_size: Number of documents processed per generation batch.
            max_input_length: Maximum number of input tokens.
        """
        super().__init__()

        self.model_id = model_id
        self.retriever_model_id = retriever_model_id
        self.device = device
        self.batch_size = batch_size
        self.max_input_length = max_input_length

        self.tokenizer = None
        self.model = None
        self.retriever = None
        self.train_data: Dict[str, List[Dict[str, Any]]] = {}
        self.train_embeddings: Dict[str, np.ndarray] = {}

    def load(self, model_id: Optional[str] = None, retriever_id: Optional[str] = None, **kwargs: Any) -> None:
        """
        Load the language model and sentence embedding model.

        Args:
            model_id: Optional language model identifier or local path.
            retriever_id: Optional embedding model identifier or local path.
        """
        if model_id is not None:
            self.model_id = model_id
        if retriever_id is not None:
            self.retriever_model_id = retriever_id

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_id, trust_remote_code=True, padding_side="left"
        )
        self.tokenizer.truncation_side = "left"
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.model = None
        for attention in ("flash_attention_2", "sdpa", "eager"):
            try:
                self.model = AutoModelForCausalLM.from_pretrained(
                    self.model_id,
                    torch_dtype=torch.float32 if self.device == "cpu" else torch.float16,
                    device_map="auto",
                    trust_remote_code=True,
                    attn_implementation=attention,
                )
                break
            except Exception:
                continue
        if self.model is None:
            raise RuntimeError("Could not load the language model.")

        self.model.eval()
        self.retriever = SentenceTransformer(self.retriever_model_id, device=self.device)

    def _ontology_construction(self, data: Any, test: bool = False) -> Optional[Any]:
        """Build the retrieval index or predict primitive ontology triples."""
        if test:
            return self._predict_triples(data, task="ontology_construction")
        self._fit_retriever(data, task="ontology_construction")
        return None

    def _ontology_expansion(self, data: Any, test: bool = False) -> Optional[Any]:
        """Build the retrieval index or predict ontology extension triples."""
        if test:
            return self._predict_triples(data, task="ontology_expansion")
        self._fit_retriever(data, task="ontology_expansion")
        return None

    def _get_context(self, sample: Dict[str, Any]) -> str:
        """Combine the text of a sample's documents into one passage."""
        return "\n\n".join(document["text"] for document in sample["documents"])

    def _fit_retriever(self, data: List[Dict[str, Any]], task: str) -> None:
        """Encode the labeled training documents for few-shot retrieval."""
        if self.retriever is None:
            raise RuntimeError("Call load() before fit().")

        target = (
            "primitive-ontology-triples"
            if task == "ontology_construction"
            else "extended-primitive-ontology-triples"
        )
        for sample in data:
            if target not in sample:
                raise KeyError(f"Missing '{target}' in {task} training sample.")
        if not data:
            raise ValueError("Training data must contain at least one labeled sample.")

        self.train_data[task] = data
        self.train_embeddings[task] = self.retriever.encode(
            [self._get_context(sample) for sample in data],
            batch_size=512,
            show_progress_bar=True,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

    def _retrieve_examples(self, data: List[Dict[str, Any]], task: str) -> List[List[Dict[str, Any]]]:
        """Retrieve the most similar labeled documents for each input."""
        if self.retriever is None or task not in self.train_embeddings:
            raise RuntimeError("Call load() and fit() for this task before predict().")
        if not data:
            return []

        query_embeddings = self.retriever.encode(
            [self._get_context(sample) for sample in data],
            batch_size=256,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )
        scores = query_embeddings @ self.train_embeddings[task].T
        top_k = min(5 if task == "ontology_construction" else 2, len(self.train_data[task]))

        examples = []
        for row in scores:
            indices = np.argpartition(row, -top_k)[-top_k:]
            indices = indices[np.argsort(row[indices])[::-1]]
            examples.append([self.train_data[task][index] for index in indices])
        return examples

    def _build_prompt_a(self, sample: Dict[str, Any], examples: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """Prepare the Flagship few-shot prompt using the retrieved documents."""
        messages = [{"role": "system", "content": self._SYSTEM_PROMPT_A}]
        for example in examples:
            context = self._get_context(example)[:900]
            triples = example["primitive-ontology-triples"][:16]
            messages.append({"role": "user", "content": f"TEXT:\n{context}"})
            messages.append({"role": "assistant", "content": json.dumps(triples)})
        messages.append({"role": "user", "content": f"TEXT:\n{self._get_context(sample)}"})
        return messages

    def _format_user_b(self, sample: Dict[str, Any]) -> str:
        """Format the document and existing ontology for the Reuse task."""
        initial = json.dumps(sample.get("initial-primitive-ontology-triples", []))
        terms = json.dumps(sample.get("terms", []))
        types = json.dumps(sample.get("types", []))
        return (
            f"CONTEXT:\n{self._get_context(sample)}\n\n"
            f"EXISTING ONTOLOGY TRIPLES:\n{initial}\n\n"
            f"NEW TERMS TO TYPE: {terms}\n"
            f"AVAILABLE TYPES: {types}"
        )

    def _build_prompt_b(self, sample: Dict[str, Any], examples: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """Prepare the Reuse prompt with examples from the initial ontologies."""
        messages = [{"role": "system", "content": self._SYSTEM_PROMPT_B}]
        for example in examples:
            messages.append({"role": "user", "content": self._format_user_b(example)})
            messages.append({
                "role": "assistant",
                "content": json.dumps(example["extended-primitive-ontology-triples"]),
            })
        messages.append({"role": "user", "content": self._format_user_b(sample)})
        return messages

    def _generate_batch(self, messages_list: List[List[Dict[str, str]]], max_new_tokens: int) -> List[str]:
        """Generate ontology triples using the instruction-tuned model."""
        import torch

        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Call load() before predict().")

        results = []
        for start in range(0, len(messages_list), self.batch_size):
            messages = messages_list[start:start + self.batch_size]
            texts = [
                self.tokenizer.apply_chat_template(
                    message, tokenize=False, add_generation_prompt=True
                )
                for message in messages
            ]
            inputs = self.tokenizer(
                texts,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=self.max_input_length,
            ).to(self.device)
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    do_sample=False,
                    temperature=None,
                    top_p=None,
                    pad_token_id=self.tokenizer.eos_token_id,
                )
            prompt_length = inputs["input_ids"].shape[1]
            for output in outputs:
                results.append(
                    self.tokenizer.decode(output[prompt_length:], skip_special_tokens=True).strip()
                )
        return results

    def _parse_triples(self, raw: str) -> List[List[str]]:
        """Parse generated triples from JSON or quoted text."""
        raw = raw.strip()
        try:
            result = json.loads(raw)
            if isinstance(result, list):
                return self._clean_triples(result)
        except Exception:
            pass

        match = re.search(r'\[[\s\S]*\]', raw)
        if match:
            try:
                result = json.loads(match.group())
                if isinstance(result, list):
                    return self._clean_triples(result)
            except Exception:
                pass

        triples = []
        patterns = [
            r'"([^"]+)"\s*,\s*"([^"]+)"\s*,\s*"([^"]+)"',
            r"'([^']+)'\s*,\s*'([^']+)'\s*,\s*'([^']+)'",
        ]
        for pattern in patterns:
            for line in raw.split('\n'):
                for subject, relation, obj in re.findall(pattern, line):
                    triples.append([subject.strip(), relation.strip(), obj.strip()])
        return self._clean_triples(triples)

    def _clean_triples(self, triples: List[Any]) -> List[List[str]]:
        """Normalize extracted triples and discard invalid relations."""
        cleaned = []
        for triple in triples:
            if not isinstance(triple, (list, tuple)) or len(triple) != 3:
                continue
            subject, relation, obj = [str(value).strip().lower() for value in triple]
            if not subject or not relation or not obj:
                continue
            if subject == obj and relation in {"is-a", "instance-of"}:
                continue
            cleaned.append([subject, relation, obj])
        return cleaned

    def _pattern_type_terms(self, sample: Dict[str, Any]) -> List[List[str]]:
        """Extract nearby term-type pairs from Reuse documents."""
        triples = []
        context = self._get_context(sample).lower()
        terms = [term.lower() for term in sample.get("terms", [])]
        types = [typ.lower() for typ in sample.get("types", [])]

        for term in terms:
            best_type, best_score = None, 0
            for typ in types:
                for sentence in re.split(r'[.;]\s*', context):
                    if term in sentence and typ in sentence:
                        distance = abs(sentence.find(term) - sentence.find(typ))
                        score = 1 + max(0, 50 - distance) / 50
                        if score > best_score:
                            best_score, best_type = score, typ
            if best_type:
                triples.append([term, "instance-of", best_type])
        return triples

    def _constrain_b(self, triples: List[List[str]], sample: Dict[str, Any]) -> List[List[str]]:
        """Filter Reuse predictions against the supplied ontology vocabulary."""
        terms = {term.lower().strip() for term in sample.get("terms", [])}
        types = {typ.lower().strip() for typ in sample.get("types", [])}
        for triple in sample.get("initial-primitive-ontology-triples", []):
            if len(triple) == 3:
                terms.add(str(triple[0]).lower().strip())
                types.add(str(triple[2]).lower().strip())
        known = terms | types

        initial = {
            tuple(str(value).lower().strip() for value in triple)
            for triple in sample.get("initial-primitive-ontology-triples", [])
            if len(triple) == 3
        }
        seen = set(initial)
        filtered = []
        for triple in triples:
            current = tuple(triple)
            if current in seen:
                continue
            subject, relation, obj = triple
            if not known or subject in known or obj in known:
                filtered.append(triple)
                seen.add(current)
        return filtered

    def _predict_triples(self, data: List[Dict[str, Any]], task: str) -> List[Dict[str, Any]]:
        """Generate triples and return the task-specific ontology predictions."""
        examples = self._retrieve_examples(data, task)
        if task == "ontology_construction":
            messages = [self._build_prompt_a(sample, retrieved) for sample, retrieved in zip(data, examples)]
            target = "primitive-ontology-triples"
            max_new_tokens = 900
        else:
            messages = [self._build_prompt_b(sample, retrieved) for sample, retrieved in zip(data, examples)]
            target = "extended-primitive-ontology-triples"
            max_new_tokens = 200

        results = []
        for start in range(0, len(messages), self.batch_size):
            batch_messages = messages[start:start + self.batch_size]
            batch_samples = data[start:start + self.batch_size]
            responses = self._generate_batch(batch_messages, max_new_tokens)
            for sample, response in zip(batch_samples, responses):
                triples = self._parse_triples(response)
                if task == "ontology_construction":
                    seen = set()
                    unique = []
                    for triple in triples:
                        current = tuple(triple)
                        if current not in seen:
                            seen.add(current)
                            unique.append(triple)
                    triples = unique
                else:
                    patterns = self._pattern_type_terms(sample)
                    merged = {tuple(triple) for triple in triples} | {tuple(triple) for triple in patterns}
                    triples = self._constrain_b([list(triple) for triple in merged], sample)
                results.append({"id": sample["id"], target: triples})
        return results
