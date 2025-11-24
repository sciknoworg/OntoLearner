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

from typing import Any, Dict, List, Optional, Tuple, Iterable
import json
from json.decoder import JSONDecodeError
import os
import random
import re

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from ...base import AutoLearner, AutoLLM

try:
    from outlines.models import Transformers as OutlinesTFModel
    from outlines.generate import json as outlines_generate_json
    from pydantic import BaseModel

    class _PredictedTypesSchema(BaseModel):
        """Schema used when generating structured JSON { "types": [...] }."""

        types: List[str]

    OUTLINES_AVAILABLE: bool = True
except Exception:
    # If outlines is unavailable, we will fall back to greedy decoding + regex parsing.
    OUTLINES_AVAILABLE = False
    _PredictedTypesSchema = None
    OutlinesTFModel = None
    outlines_generate_json = None


class LocalAutoLLM(AutoLLM):
    """
    Minimal local LLM helper.

    - Inherits AutoLLM but overrides load/generate to avoid label_mapper.
    - Optional 4-bit loading with `load_in_4bit=True` in .load().
    - Greedy decoding by default (deterministic).
    """

    def __init__(self, device: str = "cpu", token: str = "") -> None:
        """
        Initialize the local LLM holder.

        Parameters
        ----------
        device : str
            Execution device: "cpu" or "cuda".
        token : str
            Optional auth token for private model hubs.
        """
        super().__init__(label_mapper=None, device=device, token=token)
        self.model: Optional[AutoModelForCausalLM] = None
        self.tokenizer: Optional[AutoTokenizer] = None

    def load(self, model_id: str, *, load_in_4bit: bool = False) -> None:
        """
        Load a Hugging Face causal model + tokenizer and set deterministic
        generation defaults.

        Parameters
        ----------
        model_id : str
            Model identifier resolvable by HF `from_pretrained`.
        load_in_4bit : bool
            If True and bitsandbytes is available, load using 4-bit quantization.
        """
        # Tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_id, padding_side="left", token=self.token
        )
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        # Model (optionally quantized)
        if load_in_4bit:
            from transformers import BitsAndBytesConfig

            quantization_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_use_double_quant=True,
                bnb_4bit_compute_dtype=torch.bfloat16,
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                model_id,
                device_map="auto",
                quantization_config=quantization_config,
                token=self.token,
            )
        else:
            device_map = (
                "auto" if (self.device != "cpu" and torch.cuda.is_available()) else None
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                model_id,
                device_map=device_map,
                torch_dtype=torch.bfloat16
                if torch.cuda.is_available()
                else torch.float32,
                token=self.token,
            )

        # Deterministic generation defaults
        generation_cfg = self.model.generation_config
        generation_cfg.do_sample = False
        generation_cfg.temperature = None
        generation_cfg.top_k = None
        generation_cfg.top_p = None
        generation_cfg.num_beams = 1

    def generate(self, prompts: List[str], max_new_tokens: int = 128) -> List[str]:
        """
        Greedy-generate continuations for a list of prompts.

        Parameters
        ----------
        prompts : List[str]
            Prompts to generate for (batched).
        max_new_tokens : int
            Maximum number of new tokens per continuation.

        Returns
        -------
        List[str]
            Decoded new-token texts (no special tokens, stripped).
        """
        if self.model is None or self.tokenizer is None:
            raise RuntimeError(
                "Call .load(model_id) on LocalAutoLLM before generate()."
            )

        tokenized_batch = self.tokenizer(
            prompts, return_tensors="pt", padding=True, truncation=True
        )
        input_seq_len = tokenized_batch["input_ids"].shape[1]
        tokenized_batch = {
            k: v.to(self.model.device) for k, v in tokenized_batch.items()
        }

        with torch.no_grad():
            outputs = self.model.generate(
                **tokenized_batch,
                max_new_tokens=max_new_tokens,
                pad_token_id=self.tokenizer.eos_token_id,
                do_sample=False,
                num_beams=1,
            )

        # Only return the newly generated part for each row in the batch
        continuation_token_ids = outputs[:, input_seq_len:]
        return [
            self.tokenizer.decode(row, skip_special_tokens=True).strip()
            for row in continuation_token_ids
        ]


class AlexbekFewShotLearner(AutoLearner):
    """
    Text2Onto learner for LLMS4OL Task A (term & type extraction).

    Public API (A1 + convenience):
      - fit(train_docs_jsonl, terms2doc_json, sample_size=24, seed=42)
      - predict_terms(docs_test_jsonl, out_jsonl, max_new_tokens=128, few_shot_k=6) -> int
      - predict_types(docs_test_jsonl, out_jsonl, max_new_tokens=128, few_shot_k=6) -> int
      - evaluate_extraction_f1(gold_item2docs_json, preds_jsonl, key="term"|"type") -> float

    Option A (A2, term→types) bridge:
      - predict_types_from_terms_option_a(...)
        Reads your A1 results (docs→terms), predicts types for each term, and
        writes two files: terms2types_pred.json + types2docs_pred.json
    """

    def __init__(self, model: LocalAutoLLM, device: str = "cpu", **_: Any) -> None:
        """
        Initialize learner state and canned prompts.

        Parameters
        ----------
        model : LocalAutoLLM
            Loaded local LLM helper instance.
        device : str
            Device name ("cpu" or "cuda").
        """
        super().__init__(**_)
        self.model = model
        self.device = device

        # Few-shot exemplars for A1 (Docs→Terms) and for Docs→Types:
        # Each exemplar is a tuple: (title, text, gold_list)
        self._fewshot_terms_docs: List[Tuple[str, str, List[str]]] = []
        self._fewshot_types_docs: List[Tuple[str, str, List[str]]] = []

        # System prompts
        self._system_prompt_terms = (
            "You are an expert in ontology term extraction.\n"
            "Extract only terms that explicitly appear in the document.\n"
            'Answer strictly as JSON: {"terms": ["..."]}\n'
        )
        self._system_prompt_types = (
            "You are an expert in ontology type classification.\n"
            "List ontology *types* that characterize the document’s terminology.\n"
            'Answer strictly as JSON: {"types": ["..."]}\n'
        )

        # Compiled regex for robust JSON extraction from LLM outputs
        self._json_object_regex = re.compile(r"\{[^{}]*\}", re.S)
        self._json_array_regex = re.compile(r"\[[^\]]*\]", re.S)

        # Term→Types (Option A) specific prompt
        self._system_prompt_term_to_types = (
            "You are an expert in ontology and semantic type classification.\n"
            "Given a term, predict its semantic types from the domain-specific ontology.\n"
            'Answer strictly as JSON:\n{"types": ["type1", "type2", "..."]}'
        )

    def fit(
        self,
        *,
        train_docs_jsonl: str,
        terms2doc_json: str,
        sample_size: int = 24,
        seed: int = 42,
    ) -> None:
        """
        Build internal few-shot exemplars from a labeled training split.

        Parameters
        ----------
        train_docs_jsonl : str
            Path to JSONL (or tolerant JSON/JSONL) with train documents.
        terms2doc_json : str
            JSON mapping item -> [doc_id,...]; "item" can be a term or type.
        sample_size : int
            Number of exemplar documents to keep for few-shot prompting.
        seed : int
            RNG seed for reproducible sampling.
        """
        rng = random.Random(seed)

        # Load documents and map doc_id -> row
        document_map = self._load_documents_jsonl(train_docs_jsonl)
        if not document_map:
            raise FileNotFoundError(f"No documents found in: {train_docs_jsonl}")

        # Load item -> [doc_ids]
        item_to_docs_map = self._load_json(terms2doc_json)
        if not isinstance(item_to_docs_map, dict):
            raise ValueError(
                f"{terms2doc_json} must be a JSON dict mapping item -> [doc_ids]"
            )

        # Reverse mapping: doc_id -> [items]
        doc_id_to_items_map: Dict[str, List[str]] = {}
        for item_label, doc_id_list in item_to_docs_map.items():
            for doc_id in doc_id_list:
                doc_id_to_items_map.setdefault(doc_id, []).append(item_label)

        # Build candidate exemplars (title, text, gold_list)
        exemplar_candidates: List[Tuple[str, str, List[str]]] = []
        for doc_id, labeled_items in doc_id_to_items_map.items():
            doc_row = document_map.get(doc_id)
            if not doc_row:
                continue
            doc_title = str(doc_row.get("title", ""))  # be defensive (may be None)
            doc_text = self._to_text(
                doc_row.get("text", "")
            )  # string-ify list if needed
            if not doc_text:
                continue
            gold_items = self._unique_preserve(
                [s for s in labeled_items if isinstance(s, str)]
            )
            if gold_items:
                exemplar_candidates.append((doc_title, doc_text, gold_items))

        if not exemplar_candidates:
            raise RuntimeError(
                "No candidate docs with items found to build few-shot exemplars."
            )

        chosen_exemplars = rng.sample(
            exemplar_candidates, k=min(sample_size, len(exemplar_candidates))
        )
        # Reuse exemplars for both docs→terms and docs→types prompting
        self._fewshot_terms_docs = chosen_exemplars
        self._fewshot_types_docs = chosen_exemplars

    def predict_terms(
        self,
        *,
        docs_test_jsonl: str,
        out_jsonl: str,
        max_new_tokens: int = 128,
        few_shot_k: int = 6,
    ) -> int:
        """
        Extract terms that explicitly appear in each document.

        Writes one JSON object per line:
          {"id": "<doc_id>", "terms": ["...", "...", ...]}

        Parameters
        ----------
        docs_test_jsonl : str
            Path to test/dev documents in JSONL or tolerant JSON/JSONL.
        out_jsonl : str
            Output JSONL path where predictions are written (one line per doc).
        max_new_tokens : int
            Max generation length.
        few_shot_k : int
            Number of few-shot exemplars to prepend per prompt.

        Returns
        -------
        int
            Number of lines written (i.e., number of processed documents).
        """
        if self.model is None or self.model.model is None:
            raise RuntimeError("Load a model first: learner.model.load(MODEL_ID, ...)")

        test_documents = self._load_documents_jsonl(docs_test_jsonl)
        prompts: List[str] = []
        document_order: List[str] = []

        for document_id, document_row in test_documents.items():
            title = str(document_row.get("title", ""))
            text = self._to_text(document_row.get("text", ""))

            fewshot_block = self._format_fewshot_block(
                self._system_prompt_terms,
                self._fewshot_terms_docs,
                key="terms",
                k=few_shot_k,
            )
            user_block = self._format_user_block(title, text)

            prompts.append(f"{fewshot_block}\n{user_block}\nAssistant:")
            document_order.append(document_id)

        generations = self.model.generate(prompts, max_new_tokens=max_new_tokens)
        parsed_term_lists = [
            self._parse_json_list(generated, key="terms") for generated in generations
        ]

        os.makedirs(os.path.dirname(out_jsonl) or ".", exist_ok=True)
        lines_written = 0
        with open(out_jsonl, "w", encoding="utf-8") as fp_out:
            for document_id, term_list in zip(document_order, parsed_term_lists):
                payload = {"id": document_id, "terms": self._unique_preserve(term_list)}
                fp_out.write(json.dumps(payload, ensure_ascii=False) + "\n")
                lines_written += 1
        return lines_written

    def predict_types(
        self,
        *,
        docs_test_jsonl: str,
        out_jsonl: str,
        max_new_tokens: int = 128,
        few_shot_k: int = 6,
    ) -> int:
        """
        Predict ontology types that characterize each document’s terminology.

        Writes one JSON object per line:
          {"id": "<doc_id>", "types": ["...", "...", ...]}

        Parameters
        ----------
        docs_test_jsonl : str
            Path to test/dev documents in JSONL or tolerant JSON/JSONL.
        out_jsonl : str
            Output JSONL path where predictions are written (one line per doc).
        max_new_tokens : int
            Max generation length.
        few_shot_k : int
            Number of few-shot exemplars to prepend per prompt.

        Returns
        -------
        int
            Number of lines written (i.e., number of processed documents).
        """
        if self.model is None or self.model.model is None:
            raise RuntimeError("Load a model first: learner.model.load(MODEL_ID, ...)")

        test_documents = self._load_documents_jsonl(docs_test_jsonl)
        prompts: List[str] = []
        document_order: List[str] = []

        for document_id, document_row in test_documents.items():
            title = str(document_row.get("title", ""))
            text = self._to_text(document_row.get("text", ""))

            fewshot_block = self._format_fewshot_block(
                self._system_prompt_types,
                self._fewshot_types_docs,
                key="types",
                k=few_shot_k,
            )
            user_block = self._format_user_block(title, text)

            prompts.append(f"{fewshot_block}\n{user_block}\nAssistant:")
            document_order.append(document_id)

        generations = self.model.generate(prompts, max_new_tokens=max_new_tokens)
        parsed_type_lists = [
            self._parse_json_list(generated, key="types") for generated in generations
        ]

        os.makedirs(os.path.dirname(out_jsonl) or ".", exist_ok=True)
        lines_written = 0
        with open(out_jsonl, "w", encoding="utf-8") as fp_out:
            for document_id, type_list in zip(document_order, parsed_type_lists):
                payload = {"id": document_id, "types": self._unique_preserve(type_list)}
                fp_out.write(json.dumps(payload, ensure_ascii=False) + "\n")
                lines_written += 1
        return lines_written

    def evaluate_extraction_f1(
        self,
        gold_item2docs_json: str,
        preds_jsonl: str,
        *,
        key: str = "term",
    ) -> float:
        """
        Compute micro-F1 over (doc_id, item) pairs.

        Parameters
        ----------
        gold_item2docs_json : str
            JSON mapping item -> [doc_ids].
        preds_jsonl : str
            JSONL lines like {"id": "...", "terms":[...]} or {"id":"...","types":[...]}.
        key : str
            "term" or "type" depending on what you are evaluating.

        Returns
        -------
        float
            Micro-averaged F1 score.
        """
        item_to_doc_ids: Dict[str, List[str]] = self._load_json(gold_item2docs_json)

        # Build gold: doc_id -> set(items)
        gold_doc_to_items: Dict[str, set] = {}
        for item_label, doc_id_list in item_to_doc_ids.items():
            for document_id in doc_id_list:
                gold_doc_to_items.setdefault(document_id, set()).add(
                    self._norm(item_label)
                )

        # Build predictions: doc_id -> set(items)
        pred_doc_to_items: Dict[str, set] = {}
        with open(preds_jsonl, "r", encoding="utf-8") as fp_in:
            for line in fp_in:
                row = json.loads(line.strip())
                document_id = str(row.get("id", ""))
                items_list = row.get("terms" if key == "term" else "types", [])
                pred_doc_to_items[document_id] = {
                    self._norm(x) for x in items_list if isinstance(x, str)
                }

        # Micro counts
        true_positive = false_positive = false_negative = 0
        all_document_ids = set(gold_doc_to_items.keys()) | set(pred_doc_to_items.keys())
        for document_id in all_document_ids:
            gold_set = gold_doc_to_items.get(document_id, set())
            pred_set = pred_doc_to_items.get(document_id, set())
            true_positive += len(gold_set & pred_set)
            false_positive += len(pred_set - gold_set)
            false_negative += len(gold_set - pred_set)

        precision = (
            true_positive / (true_positive + false_positive)
            if (true_positive + false_positive)
            else 0.0
        )
        recall = (
            true_positive / (true_positive + false_negative)
            if (true_positive + false_negative)
            else 0.0
        )
        f1 = (
            2 * precision * recall / (precision + recall)
            if (precision + recall)
            else 0.0
        )
        return f1

    def predict_types_from_terms(
        self,
        *,
        doc_terms_jsonl: Optional[str] = None,  # formerly a1_results_jsonl
        doc_terms_list: Optional[List[Dict]] = None,  # formerly a1_results_list
        few_shot_jsonl: Optional[
            str
        ] = None,  # JSONL lines: {"term":"...", "types":[...]}
        rag_terms_json: Optional[
            str
        ] = None,  # JSON list; items may contain "term" and "RAG":[...]
        random_few_shot: Optional[int] = 3,
        model_id: str = "Qwen/Qwen2.5-1.5B-Instruct",
        use_structured_output: bool = True,
        seed: int = 42,
        out_terms2types: str = "terms2types_pred.json",
        out_types2docs: str = "types2docs_pred.json",
    ) -> Dict[str, Any]:
        """
        Predict types for each unique term extracted per document and derive a types→docs map.

        Parameters
        ----------
        doc_terms_jsonl : Optional[str]
            Path to JSONL with lines like {"id": "...", "terms": [...]} or a JSON with {"results":[...]}.
        doc_terms_list : Optional[List[Dict]]
            In-memory results like [{"id":"...","extracted_terms":[...]}] or {"id":"...","terms":[...]}.
        few_shot_jsonl : Optional[str]
            Global few-shot exemplars: one JSON object per line with {"term": "...", "types":[...]}.
        rag_terms_json : Optional[str]
            Optional per-term RAG exemplars: a JSON list of {"term": "...", "RAG":[{"term": "...", "types":[...]}]}.
        random_few_shot : Optional[int]
            If provided, randomly select up to this many few-shot examples for each prediction.
        model_id : str
            HF model id used specifically for term→types predictions.
        use_structured_output : bool
            If True and outlines is available, enforce structured {"types":[...]} output.
        seed : int
            Random seed for reproducibility.
        out_terms2types : str
            Output JSON path for list of {"term": "...", "predicted_types":[...]}.
        out_types2docs : str
            Output JSON path for dict {"TYPE":[doc_ids,...], ...}.

        Returns
        -------
        Dict[str, Any]
            Summary with predictions and counts.
        """
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed(seed)

        # Load normalized document→terms results
        doc_term_extractions = self._load_doc_term_extractions(
            results_json_path=doc_terms_jsonl,
            in_memory_results=doc_terms_list,
        )
        if not doc_term_extractions:
            raise ValueError(
                "No document→terms results provided (doc_terms_jsonl/doc_terms_list)."
            )

        # Prepare unique term list and term→doc occurrences
        unique_terms = self._collect_unique_terms_from_extractions(doc_term_extractions)
        term_to_doc_ids_map = self._build_term_to_doc_ids(doc_term_extractions)

        # Load optional global few-shot examples
        global_few_shot_examples: List[Dict] = []
        if few_shot_jsonl and os.path.exists(few_shot_jsonl):
            with open(few_shot_jsonl, "r", encoding="utf-8") as few_shot_file:
                for raw_line in few_shot_file:
                    raw_line = raw_line.strip()
                    if not raw_line:
                        continue
                    try:
                        json_obj = json.loads(raw_line)
                    except Exception:
                        continue
                    if (
                        isinstance(json_obj, dict)
                        and "term" in json_obj
                        and "types" in json_obj
                    ):
                        global_few_shot_examples.append(json_obj)

        # Optional per-term RAG examples: {normalized_term -> [examples]}
        rag_examples_lookup: Dict[str, List[Dict]] = {}
        if rag_terms_json and os.path.exists(rag_terms_json):
            try:
                rag_payload = self._load_json(rag_terms_json)
                if isinstance(rag_payload, list):
                    for rag_item in rag_payload:
                        if isinstance(rag_item, dict):
                            normalized_term = self._normalize_term(
                                rag_item.get("term", "")
                            )
                            rag_examples_lookup[normalized_term] = rag_item.get(
                                "RAG", []
                            )
            except Exception:
                pass

        # Load a small chat LLM dedicated to Term→Types
        typing_model, typing_tokenizer = self._load_llm_for_types(model_id)

        # Predict types per term
        term_to_predicted_types_list: List[Dict] = []
        for term_text in unique_terms:
            normalized_term = self._normalize_term(term_text)

            # Prefer per-term RAG for this term, else use global few-shot
            few_shot_examples_for_term = (
                rag_examples_lookup.get(normalized_term, None)
                or global_few_shot_examples
            )

            # Build conversation and prompt
            conversation_messages = self._build_conv_for_type_infer(
                term=term_text,
                few_shot_examples=few_shot_examples_for_term,
                random_k=random_few_shot,
            )
            typing_prompt_string = self._apply_chat_template_safe_types(
                typing_tokenizer, conversation_messages
            )

            predicted_types: List[str] = []
            raw_generation_text: str = ""

            # Structured JSON path (if requested and available)
            if (
                use_structured_output
                and OUTLINES_AVAILABLE
                and _PredictedTypesSchema is not None
            ):
                try:
                    outlines_model = OutlinesTFModel(typing_model, typing_tokenizer)  # type: ignore
                    generator = outlines_generate_json(
                        outlines_model, _PredictedTypesSchema
                    )  # type: ignore
                    structured = generator(typing_prompt_string, max_tokens=512)
                    predicted_types = [
                        label for label in structured.types if isinstance(label, str)
                    ]
                    raw_generation_text = json.dumps(
                        {"types": predicted_types}, ensure_ascii=False
                    )
                except Exception:
                    # Fall back to greedy decoding
                    use_structured_output = False

            # Greedy decode fallback
            if (
                not use_structured_output
                or not OUTLINES_AVAILABLE
                or _PredictedTypesSchema is None
            ):
                tokenized_prompt = typing_tokenizer(
                    typing_prompt_string,
                    return_tensors="pt",
                    truncation=True,
                    max_length=2048,
                )
                if torch.cuda.is_available():
                    tokenized_prompt = {
                        name: tensor.cuda() for name, tensor in tokenized_prompt.items()
                    }
                with torch.no_grad():
                    output_ids = typing_model.generate(
                        **tokenized_prompt,
                        max_new_tokens=256,
                        do_sample=False,
                        num_beams=1,
                        pad_token_id=typing_tokenizer.eos_token_id,
                    )
                new_token_span = output_ids[0][tokenized_prompt["input_ids"].shape[1] :]
                raw_generation_text = typing_tokenizer.decode(
                    new_token_span, skip_special_tokens=True
                )
                predicted_types = self._extract_types_from_text(raw_generation_text)

            term_to_predicted_types_list.append(
                {
                    "term": term_text,
                    "predicted_types": sorted(set(predicted_types)),
                }
            )

        # 7) Build types→docs from (term→types) and (term→docs)
        types_to_doc_id_set: Dict[str, set] = {}
        for term_prediction in term_to_predicted_types_list:
            normalized_term = self._normalize_term(term_prediction["term"])
            doc_ids_for_term = term_to_doc_ids_map.get(normalized_term, [])
            for type_label in term_prediction.get("predicted_types", []):
                types_to_doc_id_set.setdefault(type_label, set()).update(
                    doc_ids_for_term
                )

        types_to_doc_ids: Dict[str, List[str]] = {
            type_label: sorted(doc_id_set)
            for type_label, doc_id_set in types_to_doc_id_set.items()
        }

        # 8) Save outputs
        os.makedirs(os.path.dirname(out_terms2types) or ".", exist_ok=True)
        with open(out_terms2types, "w", encoding="utf-8") as fp_terms2types:
            json.dump(
                term_to_predicted_types_list,
                fp_terms2types,
                ensure_ascii=False,
                indent=2,
            )

        os.makedirs(os.path.dirname(out_types2docs) or ".", exist_ok=True)
        with open(out_types2docs, "w", encoding="utf-8") as fp_types2docs:
            json.dump(types_to_doc_ids, fp_types2docs, ensure_ascii=False, indent=2)

        # Cleanup VRAM if any
        del typing_model, typing_tokenizer
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

        return {
            "terms2types_pred": term_to_predicted_types_list,
            "types2docs_pred": types_to_doc_ids,
            "unique_terms": len(unique_terms),
            "types_count": len(types_to_doc_ids),
        }

    def _load_json(self, path: str) -> Dict[str, Any]:
        """Load a JSON file from disk and return its parsed object."""
        with open(path, "r", encoding="utf-8") as file_obj:
            return json.load(file_obj)

    def _iter_json_objects(self, blob: str) -> Iterable[Dict[str, Any]]:
        """
        Iterate over *all* JSON objects found inside a string.

        Supports cases where multiple JSON objects are concatenated back-to-back
        in a single line. It skips stray commas/whitespace between objects.

        Parameters
        ----------
        blob : str
            A string that may contain one or more JSON objects.

        Yields
        ------
        Dict[str, Any]
            Each parsed JSON object.
        """
        json_decoder = json.JSONDecoder()
        cursor_index, text_length = 0, len(blob)
        while cursor_index < text_length:
            # Skip whitespace/commas between objects
            while cursor_index < text_length and blob[cursor_index] in " \t\r\n,":
                cursor_index += 1
            if cursor_index >= text_length:
                break
            try:
                json_obj, end_index = json_decoder.raw_decode(blob, idx=cursor_index)
            except JSONDecodeError:
                # Can't decode from this position; stop scanning this chunk
                break
            yield json_obj
            cursor_index = end_index

    def _load_documents_jsonl(self, path: str) -> Dict[str, Dict[str, Any]]:
        """
        Robust reader that supports:
        • True JSONL (one object per line)
        • Lines with multiple concatenated JSON objects
        • Whole file as a JSON array

        Returns
        -------
        Dict[str, Dict[str, Any]]
            Mapping doc_id -> full document row.
        """
        documents_by_id: Dict[str, Dict[str, Any]] = {}

        with open(path, "r", encoding="utf-8") as file_obj:
            content = file_obj.read().strip()

        # Case A: whole-file JSON array
        if content.startswith("["):
            try:
                json_array = json.loads(content)
                if isinstance(json_array, list):
                    for record in json_array:
                        if not isinstance(record, dict):
                            continue
                        document_id = str(
                            record.get("id")
                            or record.get("doc_id")
                            or (record.get("doc") or {}).get("id")
                            or ""
                        )
                        if document_id:
                            documents_by_id[document_id] = record
                    return documents_by_id
            except Exception:
                # Fall back to line-wise handling if array parsing fails
                pass

        # Case B: treat as JSONL-ish; parse *all* objects per line
        for raw_line in content.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            for record in self._iter_json_objects(line):
                if not isinstance(record, dict):
                    continue
                document_id = str(
                    record.get("id")
                    or record.get("doc_id")
                    or (record.get("doc") or {}).get("id")
                    or ""
                )
                if document_id:
                    documents_by_id[document_id] = record

        return documents_by_id

    def _to_text(self, text_field: Any) -> str:
        """
        Convert a 'text' field into a single string (handles list-of-strings).

        Parameters
        ----------
        text_field : Any
            The value found under "text" in the dataset row.

        Returns
        -------
        str
            A single-string representation of the text.
        """
        if isinstance(text_field, str):
            return text_field
        if isinstance(text_field, list):
            return " ".join(str(part) for part in text_field)
        return str(text_field) if text_field is not None else ""

    def _unique_preserve(self, values: List[str]) -> List[str]:
        """
        Deduplicate values while preserving the original order.

        Parameters
        ----------
        values : List[str]
            Sequence possibly containing duplicates.

        Returns
        -------
        List[str]
            Sequence without duplicates, order preserved.
        """
        seen_values: set = set()
        ordered_values: List[str] = []
        for candidate in values:
            if candidate not in seen_values:
                seen_values.add(candidate)
                ordered_values.append(candidate)
        return ordered_values

    def _norm(self, text: str) -> str:
        """
        Lowercased, single-spaced normalization (for comparisons).

        Parameters
        ----------
        text : str
            Input string.

        Returns
        -------
        str
            Normalized string.
        """
        return " ".join(text.lower().split())

    def _normalize_term(self, term: str) -> str:
        """
        Normalization tailored for term keys / lookups.

        Parameters
        ----------
        term : str
            Term to normalize.

        Returns
        -------
        str
            Lowercased, trimmed and single-spaced term.
        """
        return " ".join(str(term).strip().split()).lower()

    def _format_fewshot_block(
        self,
        system_prompt: str,
        fewshot_examples: List[Tuple[str, str, List[str]]],
        *,
        key: str,
        k: int = 6,
    ) -> str:
        """
        Render a few-shot block like:

        <SYSTEM PROMPT>

        ### Example
        User:
        Title: ...
        <text>
        Assistant:
        {"terms": [...]}   or   {"types": [...]}

        Parameters
        ----------
        system_prompt : str
            Instructional system text to prepend.
        fewshot_examples : List[Tuple[str, str, List[str]]]
            Examples as (title, text, labels_list).
        key : str
            Either "terms" or "types" depending on the task.
        k : int
            Number of examples to include.

        Returns
        -------
        str
            Formatted few-shot block text.
        """
        lines: List[str] = [system_prompt.strip(), ""]
        for example_title, example_text, gold_list in fewshot_examples[:k]:
            lines.append("### Example")
            lines.append(f"User:\nTitle: {example_title}\n{example_text}")
            lines.append(
                f'Assistant:\n{{"{key}": '
                + json.dumps(gold_list, ensure_ascii=False)
                + "}"
            )
        return "\n".join(lines)

    def _format_user_block(self, title: str, text: str) -> str:
        """
        Format the 'Task' block for the current document.

        Parameters
        ----------
        title : str
            Document title.
        text : str
            Document text (single string).

        Returns
        -------
        str
            Formatted user block.
        """
        return f"### Task\nUser:\nTitle: {title}\n{text}"

    def _parse_json_list(self, generated_text: str, *, key: str) -> List[str]:
        """
        Extract a list from model output, trying:
        1) JSON object with the key ({"terms":[...]} or {"types":[...]}).
        2) Any top-level JSON array.
        3) Fallback: comma-split.

        Parameters
        ----------
        generated_text : str
            Raw generation text to parse.
        key : str
            "terms" or "types".

        Returns
        -------
        List[str]
            Parsed strings (best-effort).
        """
        # 1) Try a JSON object and read key
        try:
            object_match = self._json_object_regex.search(generated_text)
            if object_match:
                json_obj = json.loads(object_match.group(0))
                json_array = json_obj.get(key)
                if isinstance(json_array, list):
                    return [value for value in json_array if isinstance(value, str)]
        except Exception:
            pass

        # 2) Any JSON array
        try:
            array_match = self._json_array_regex.search(generated_text)
            if array_match:
                json_array = json.loads(array_match.group(0))
                if isinstance(json_array, list):
                    return [value for value in json_array if isinstance(value, str)]
        except Exception:
            pass

        # 3) Fallback: comma-split (last resort)
        if "," in generated_text:
            return [
                part.strip().strip('"').strip("'")
                for part in generated_text.split(",")
                if part.strip()
            ]
        return []

    def _apply_chat_template_safe_types(
        self, tokenizer: AutoTokenizer, messages: List[Dict[str, str]]
    ) -> str:
        """
        Safely build a prompt string for chat models. Uses the model's chat template
        when available; otherwise falls back to a simple concatenation.
        """
        try:
            return tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )
        except Exception:
            system_text = next(
                (m["content"] for m in messages if m.get("role") == "system"), ""
            )
            last_user_text = next(
                (m["content"] for m in reversed(messages) if m.get("role") == "user"),
                "",
            )
            return f"{system_text}\n\nUser:\n{last_user_text}\n\nAssistant:"

    def _build_conv_for_type_infer(
        self,
        term: str,
        few_shot_examples: Optional[List[Dict]] = None,
        random_k: Optional[int] = None,
    ) -> List[Dict[str, str]]:
        """
        Create a chat-style conversation for a single term→types query,
        optionally prepending few-shot examples.
        """
        messages: List[Dict[str, str]] = [
            {"role": "system", "content": self._system_prompt_term_to_types}
        ]
        examples = list(few_shot_examples or [])
        if random_k and len(examples) > random_k:
            import random as _rnd

            examples = _rnd.sample(examples, random_k)
        for exemplar in examples:
            example_term = exemplar.get("term", "")
            example_types = exemplar.get("types", [])
            messages.append({"role": "user", "content": f"Term: {example_term}"})
            messages.append(
                {
                    "role": "assistant",
                    "content": json.dumps({"types": example_types}, ensure_ascii=False),
                }
            )
        messages.append({"role": "user", "content": f"Term: {term}"})
        return messages

    def _extract_types_from_text(self, generated_text: str) -> List[str]:
        """
        Parse {"types":[...]} from a free-form generation.
        """
        try:
            object_match = re.search(r'\{[^}]*"types"[^}]*\}', generated_text)
            if object_match:
                json_obj = json.loads(object_match.group(0))
                types_array = json_obj.get("types", [])
                return [
                    type_label
                    for type_label in types_array
                    if isinstance(type_label, str)
                ]
        except Exception:
            pass
        return []

    def _load_llm_for_types(
        self, model_id: str
    ) -> Tuple[AutoModelForCausalLM, AutoTokenizer]:
        """
        Load a *separate* small chat model for Term→Types (keeps LocalAutoLLM untouched).
        """
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
            device_map="auto" if torch.cuda.is_available() else None,
        )
        return model, tokenizer

    def _load_doc_term_extractions(
        self,
        *,
        results_json_path: Optional[str] = None,
        in_memory_results: Optional[List[Dict]] = None,
    ) -> List[Dict]:
        """
        Normalize document→terms outputs to a list of:
        {"id": "<doc_id>", "extracted_terms": ["...", ...]}

        Accepts either:
        - in_memory_results (list of dicts)
        - results_json_path pointing to:
            • a JSONL file with lines: {"id": "...", "terms": [...]}
            • OR a JSON file with {"results":[{"id":..., "extracted_terms": [...]}, ...]}
            • OR a JSON list of dicts
        """
        normalized_records: List[Dict] = []

        def _coerce_to_record(source_row: Dict) -> Optional[Dict]:
            document_id = str(source_row.get("id", "")) or str(
                source_row.get("doc_id", "")
            )
            if not document_id:
                return None
            terms = source_row.get("extracted_terms")
            if terms is None:
                terms = source_row.get("terms")
            if (
                terms is None
                and "payload" in source_row
                and isinstance(source_row["payload"], dict)
            ):
                terms = source_row["payload"].get("terms")
            if not isinstance(terms, list):
                terms = []
            return {
                "id": document_id,
                "extracted_terms": [t for t in terms if isinstance(t, str)],
            }

        if in_memory_results is not None:
            for source_row in in_memory_results:
                coerced_record = _coerce_to_record(source_row)
                if coerced_record:
                    normalized_records.append(coerced_record)
            return normalized_records

        if not results_json_path:
            raise ValueError("Provide results_json_path or in_memory_results")

        # Detect JSON vs JSONL by extension (best-effort)
        if results_json_path.endswith(".jsonl"):
            with open(results_json_path, "r", encoding="utf-8") as file_in:
                for raw_line in file_in:
                    raw_line = raw_line.strip()
                    if not raw_line:
                        continue
                    # Multiple concatenated objects per line? Iterate them all.
                    for json_obj in self._iter_json_objects(raw_line):
                        if isinstance(json_obj, dict):
                            coerced_record = _coerce_to_record(json_obj)
                            if coerced_record:
                                normalized_records.append(coerced_record)
        else:
            payload_obj = self._load_json(results_json_path)
            if isinstance(payload_obj, dict) and "results" in payload_obj:
                for source_row in payload_obj["results"]:
                    coerced_record = _coerce_to_record(source_row)
                    if coerced_record:
                        normalized_records.append(coerced_record)
            elif isinstance(payload_obj, list):
                for source_row in payload_obj:
                    if isinstance(source_row, dict):
                        coerced_record = _coerce_to_record(source_row)
                        if coerced_record:
                            normalized_records.append(coerced_record)

        return normalized_records

    def _collect_unique_terms_from_extractions(
        self, doc_term_extractions: List[Dict]
    ) -> List[str]:
        """
        Collect unique terms (original casing) from normalized document→terms results.
        """
        seen_normalized_terms: set = set()
        ordered_unique_terms: List[str] = []
        for record in doc_term_extractions:
            for term_text in record.get("extracted_terms", []):
                normalized = self._normalize_term(term_text)
                if normalized and normalized not in seen_normalized_terms:
                    seen_normalized_terms.add(normalized)
                    ordered_unique_terms.append(term_text.strip())
        return ordered_unique_terms

    def _build_term_to_doc_ids(
        self, doc_term_extractions: List[Dict]
    ) -> Dict[str, List[str]]:
        """
        Build lookup: normalized_term -> sorted unique list of doc_ids.
        """
        term_to_doc_set: Dict[str, set] = {}
        for record in doc_term_extractions:
            document_id = str(record.get("id", ""))
            for term_text in record.get("extracted_terms", []):
                normalized = self._normalize_term(term_text)
                if not normalized or not document_id:
                    continue
                term_to_doc_set.setdefault(normalized, set()).add(document_id)
        return {
            normalized_term: sorted(doc_ids)
            for normalized_term, doc_ids in term_to_doc_set.items()
        }
