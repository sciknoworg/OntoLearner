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

import ast
import gc
import random
import re
from collections import defaultdict
from typing import Any, DefaultDict, Dict, List, Optional, Set

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from ...base import AutoLearner

class SBUNLPFewShotLearner(AutoLearner):
    """
    Public API expected by the pipeline:
      - `load(model_id=...)`
      - `fit(train_data, task=..., ontologizer=...)`
      - `predict(test_data, task=..., ontologizer=...)`

    Expected input bundle format (train/test):
      - "documents": list of dicts, each with keys: {"id", "title", "text"}
      - "terms2docs": dict mapping term -> list of doc_ids
      - "terms2types": optional dict mapping term -> list of types

    Prediction output payload (pipeline wraps this):
      - {"terms": [{"doc_id": str, "term": str}, ...],
         "types": [{"doc_id": str, "type": str}, ...]}
    """

    def __init__(
        self,
        llm_model_id: Optional[str] = None,
        device: str = "cpu",
        load_in_4bit: bool = False,
        max_new_tokens: int = 256,
        trust_remote_code: bool = True,
    ) -> None:
        """
        Initialize the few-shot learner.

        Args:
            llm_model_id: Default HF model id to load if `load()` is called without one.
            device: "cpu" or a CUDA device identifier (e.g. "cuda").
            load_in_4bit: Whether to attempt 4-bit quantized loading (bitsandbytes).
            max_new_tokens: Maximum tokens to generate per prompt.
            retriever_model_id: Unused (kept for compatibility).
            top_k: Unused (kept for compatibility).
            trust_remote_code: Forwarded to HF loaders (use with caution).
        """
        super().__init__()
        self.device = device
        self.max_new_tokens = int(max_new_tokens)

        self._default_model_id = llm_model_id
        self._load_in_4bit_default = bool(load_in_4bit)
        self._trust_remote_code_default = bool(trust_remote_code)

        # HF objects
        self.model: Optional[AutoModelForCausalLM] = None
        self.tokenizer: Optional[AutoTokenizer] = None

        self._is_loaded = False
        self._loaded_model_id: Optional[str] = None

        # Cached few-shot example blocks built during `fit()`
        self.few_shot_terms_block: str = ""
        self.few_shot_types_block: str = ""

    def load(self, model_id: Optional[str] = None, **kwargs: Any) -> None:
        """
        Load the underlying HF causal LM and tokenizer.

        LearnerPipeline typically calls: `learner.load(model_id=llm_id)`.

        Args:
            model_id: HF model id. If None, uses `llm_model_id` from __init__.
            **kwargs:
                load_in_4bit: override default 4-bit loading.
                trust_remote_code: override default trust_remote_code.
        """
        resolved_model_id = model_id or self._default_model_id
        if not resolved_model_id:
            raise ValueError(
                f"No model_id provided to {self.__class__.__name__}.load() and no llm_model_id in __init__."
            )

        load_in_4bit = bool(kwargs.get("load_in_4bit", self._load_in_4bit_default))
        trust_remote_code = bool(kwargs.get("trust_remote_code", self._trust_remote_code_default))

        # Avoid re-loading same model
        if self._is_loaded and self._loaded_model_id == resolved_model_id:
            return

        torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        tokenizer = AutoTokenizer.from_pretrained(resolved_model_id, trust_remote_code=trust_remote_code)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        self.tokenizer = tokenizer

        quantization_config = None
        if load_in_4bit:
            quantization_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
            )
            torch_dtype = torch.float16

        device_map = "auto" if (self.device != "cpu") else {"": "cpu"}

        model = AutoModelForCausalLM.from_pretrained(
            resolved_model_id,
            device_map=device_map,
            torch_dtype=torch_dtype,
            quantization_config=quantization_config,
            trust_remote_code=trust_remote_code,
        )

        if self.device == "cpu":
            model.to("cpu")

        self.model = model
        self._is_loaded = True
        self._loaded_model_id = resolved_model_id

    def _invert_terms_to_docs_mapping(self, terms_to_documents: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """
        Convert term->docs mapping to doc->terms mapping.

        Args:
            terms_to_documents: Mapping from term to list of document IDs.

        Returns:
            Mapping from document ID to list of terms associated with it.
        """
        document_to_terms: DefaultDict[str, List[str]] = defaultdict(list)
        for term, document_ids in (terms_to_documents or {}).items():
            for document_id in document_ids or []:
                document_to_terms[str(document_id)].append(str(term))
        return dict(document_to_terms)

    def _derive_document_to_types(
        self,
        terms_to_documents: Dict[str, List[str]],
        terms_to_types: Optional[Dict[str, List[str]]],
    ) -> Dict[str, List[str]]:
        """
        Derive doc->types mapping using (terms->docs) and (terms->types).

        Args:
            terms_to_documents: term -> [doc_id...]
            terms_to_types: term -> [type...]

        Returns:
            doc_id -> sorted list of unique types.
        """
        if not terms_to_types:
            return {}

        document_to_types: DefaultDict[str, Set[str]] = defaultdict(set)

        for term, document_ids in (terms_to_documents or {}).items():
            candidate_types = terms_to_types.get(term, []) or []
            for document_id in document_ids or []:
                for candidate_type in candidate_types:
                    if isinstance(candidate_type, str) and candidate_type.strip():
                        document_to_types[str(document_id)].add(candidate_type.strip())

        return {doc_id: sorted(list(type_set)) for doc_id, type_set in document_to_types.items()}

    def _truncate_text(self, text: str, max_chars: int) -> str:
        """
        Truncate text to a maximum number of characters (adds an ellipsis when truncated).

        Args:
            text: Input text.
            max_chars: Maximum characters to keep. If <= 0, returns the original text.

        Returns:
            Truncated or original text.
        """
        if not max_chars or max_chars <= 0 or not text:
            return text or ""
        return (text[:max_chars] + "…") if len(text) > max_chars else text

    def build_few_shot_terms_block(
        self,
        documents: List[Dict[str, Any]],
        terms_to_documents: Dict[str, List[str]],
        sample_size: int = 28,
        seed: int = 123,
        max_chars_per_text: int = 1200,
    ) -> str:
        """
        Build and cache the few-shot block for term extraction.

        Strategy:
            - Create strata by associated terms (doc -> associated term list).
            - Sample proportionally across strata.
            - Deduplicate by document id and top up from remaining docs if needed.

        Args:
            documents: Documents with keys: {"id","title","text"}.
            terms_to_documents: Mapping term -> list of doc IDs.
            sample_size: Desired number of examples in the block.
            seed: RNG seed (local to this call).
            max_chars_per_text: Text truncation limit per example.

        Returns:
            The formatted few-shot example block string.
        """
        rng = random.Random(seed)

        document_to_terms = self._invert_terms_to_docs_mapping(terms_to_documents)
        total_documents = len(documents)
        target_sample_count = min(int(sample_size), total_documents)

        strata: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)
        for document in documents:
            document_id = str(document.get("id", ""))
            associated_terms = document_to_terms.get(document_id, ["no_term"])
            for term in associated_terms:
                strata[str(term)].append(document)

        sampled_documents: List[Dict[str, Any]] = []
        for docs_in_stratum in strata.values():
            if not docs_in_stratum:
                continue
            proportion = len(docs_in_stratum) / max(1, total_documents)
            stratum_quota = int(target_sample_count * proportion)
            if stratum_quota > 0:
                sampled_documents.extend(rng.sample(docs_in_stratum, min(stratum_quota, len(docs_in_stratum))))

        sampled_by_id = {str(d.get("id", "")): d for d in sampled_documents if d.get("id", "")}
        final_documents = list(sampled_by_id.values())

        if len(final_documents) > target_sample_count:
            final_documents = rng.sample(final_documents, target_sample_count)
        elif len(final_documents) < target_sample_count:
            remaining_documents = [d for d in documents if str(d.get("id", "")) not in sampled_by_id]
            additional_needed = min(target_sample_count - len(final_documents), len(remaining_documents))
            if additional_needed > 0:
                final_documents.extend(rng.sample(remaining_documents, additional_needed))

        lines: List[str] = []
        for document in final_documents:
            document_id = str(document.get("id", ""))
            title = str(document.get("title", ""))
            text = self._truncate_text(str(document.get("text", "")), max_chars_per_text)
            associated_terms = document_to_terms.get(document_id, [])

            lines.append(
                "Document ID: {doc_id}\n"
                "Title: {title}\n"
                "Text: {text}\n"
                "Associated Terms: {terms}\n"
                "----------------------------------------".format(
                    doc_id=document_id,
                    title=title,
                    text=text,
                    terms=associated_terms,
                )
            )

        self.few_shot_terms_block = "\n".join(lines)
        return self.few_shot_terms_block

    def build_few_shot_types_block(
        self,
        documents: List[Dict[str, Any]],
        terms_to_documents: Dict[str, List[str]],
        terms_to_types: Optional[Dict[str, List[str]]] = None,
        sample_size: int = 28,
        seed: int = 123,
        max_chars_per_text: int = 800,
    ) -> str:
        """
        Build and cache the few-shot block for type (class) extraction.

        Prefers doc->types derived from `terms_to_types`; if absent, falls back to treating
        associated terms as "types" for stratification (behavior-preserving fallback).

        Args:
            documents: Documents with keys: {"id","title","text"}.
            terms_to_documents: Mapping term -> list of doc IDs.
            terms_to_types: Optional mapping term -> list of types.
            sample_size: Desired number of examples in the block.
            seed: RNG seed (local to this call).
            max_chars_per_text: Text truncation limit per example.

        Returns:
            The formatted few-shot example block string.
        """
        rng = random.Random(seed)

        documents_by_id = {str(d.get("id", "")): d for d in documents if d.get("id", "")}

        document_to_types = self._derive_document_to_types(terms_to_documents, terms_to_types)
        if not document_to_types:
            document_to_types = self._invert_terms_to_docs_mapping(terms_to_documents)

        type_to_documents: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)
        for document_id, candidate_types in document_to_types.items():
            document = documents_by_id.get(document_id)
            if not document:
                continue
            for candidate_type in candidate_types:
                type_to_documents[str(candidate_type)].append(document)

        total_documents = len(documents)
        target_sample_count = min(int(sample_size), total_documents)

        sampled_documents: List[Dict[str, Any]] = []
        for docs_in_stratum in type_to_documents.values():
            if not docs_in_stratum:
                continue
            proportion = len(docs_in_stratum) / max(1, total_documents)
            stratum_quota = int(target_sample_count * proportion)
            if stratum_quota > 0:
                sampled_documents.extend(rng.sample(docs_in_stratum, min(stratum_quota, len(docs_in_stratum))))

        sampled_by_id = {str(d.get("id", "")): d for d in sampled_documents if d.get("id", "")}
        final_documents = list(sampled_by_id.values())

        if len(final_documents) > target_sample_count:
            final_documents = rng.sample(final_documents, target_sample_count)
        elif len(final_documents) < target_sample_count:
            remaining_documents = [d for d in documents if str(d.get("id", "")) not in sampled_by_id]
            additional_needed = min(target_sample_count - len(final_documents), len(remaining_documents))
            if additional_needed > 0:
                final_documents.extend(rng.sample(remaining_documents, additional_needed))

        lines: List[str] = []
        for document in final_documents:
            document_id = str(document.get("id", ""))
            title = str(document.get("title", ""))
            text = self._truncate_text(str(document.get("text", "")), max_chars_per_text)

            associated_types = document_to_types.get(document_id, [])
            associated_types_escaped = [t.replace("'", "\\'") for t in associated_types]

            lines.append(
                "Document ID: {doc_id}\n"
                "Title: {title}\n"
                "Text: {text}\n"
                "Associated Types: {types}\n"
                "----------------------------------------".format(
                    doc_id=document_id,
                    title=title,
                    text=text,
                    types=associated_types_escaped,
                )
            )

        self.few_shot_types_block = "\n".join(lines)
        return self.few_shot_types_block

    def _format_term_prompt(self, example_block: str, title: str, text: str) -> str:
        """
        Format a prompt for term extraction.

        Args:
            example_block: Few-shot examples block.
            title: Document title.
            text: Document text.

        Returns:
            Prompt string.
        """
        return (
            f"{example_block}\n"
            "[var]\n"
            f"Title: {title}\n"
            f"Text: {text}\n"
            "[var]\n"
            "Extract all relevant terms that could form the basis of an ontology from the above document.\n"
            "Return ONLY a Python list like ['term1', 'term2', ...] and nothing else.\n"
            "If no terms are found, return [].\n"
        )

    def _format_type_prompt(self, example_block: str, title: str, text: str) -> str:
        """
        Format a prompt for type (class) extraction.

        Args:
            example_block: Few-shot examples block.
            title: Document title.
            text: Document text.

        Returns:
            Prompt string.
        """
        return (
            f"{example_block}\n"
            "[var]\n"
            f"Title: {title}\n"
            f"Text: {text}\n"
            "[var]\n"
            "Extract all relevant TYPES mentioned in the above document that could serve as ontology classes.\n"
            "Only consider content inside the [var] ... [var] block.\n"
            "Return ONLY a valid Python list like ['type1', 'type2'] and nothing else. If none, return [].\n"
        )

    def _parse_python_list_of_strings(self, raw_text: str) -> List[str]:
        """
        Parse an LLM response intended to be a Python list of strings.

        This parser is intentionally tolerant:
          1) Try literal_eval on the full string
          2) Else extract the first [...] block and literal_eval it
          3) Else fallback to extracting quoted strings

        Args:
            raw_text: Model output.

        Returns:
            List of strings (possibly empty).
        """
        stripped = (raw_text or "").strip()
        if stripped in ("", "[]"):
            return []

        try:
            parsed = ast.literal_eval(stripped)
            if isinstance(parsed, list):
                return [item for item in parsed if isinstance(item, str)]
        except Exception:
            pass

        match = re.search(r"\[[\s\S]*?\]", stripped)
        if match:
            try:
                parsed = ast.literal_eval(match.group(0))
                if isinstance(parsed, list):
                    return [item for item in parsed if isinstance(item, str)]
            except Exception:
                pass

        quoted = re.findall(r"'([^']+)'|\"([^\"]+)\"", stripped)
        return [a or b for a, b in quoted]

    def _generate_completion(self, prompt_text: str) -> str:
        """
        Generate a completion for a single prompt (deterministic decoding).

        Args:
            prompt_text: Full prompt to send to the model.

        Returns:
            The generated completion text (prompt stripped where possible).
        """
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Model/tokenizer not loaded. Call .load() first.")

        encoded = self.tokenizer([prompt_text], return_tensors="pt", padding=True, truncation=True)
        input_ids = encoded["input_ids"]
        attention_mask = encoded["attention_mask"]

        model_device = next(self.model.parameters()).device
        input_ids = input_ids.to(model_device)
        attention_mask = attention_mask.to(model_device)

        with torch.no_grad():
            output_ids = self.model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_new_tokens=self.max_new_tokens,
                do_sample=False,
                temperature=0.0,
                top_p=1.0,
                pad_token_id=self.tokenizer.eos_token_id,
            )[0]

        decoded_full = self.tokenizer.decode(output_ids, skip_special_tokens=True)
        decoded_prompt = self.tokenizer.decode(input_ids[0], skip_special_tokens=True)

        if decoded_full.startswith(decoded_prompt):
            return decoded_full[len(decoded_prompt) :].strip()

        prompt_token_count = int(attention_mask[0].sum().item())
        return self.tokenizer.decode(output_ids[prompt_token_count:], skip_special_tokens=True).strip()

    def fit(
        self,
        train_data: Any,
        task: str = "text2onto",
        ontologizer: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        Build and cache few-shot blocks from the training split.

        Args:
            train_data: A split bundle dict. Must contain "documents" and "terms2docs".
            task: Must be "text2onto".
            ontologizer: Unused here (kept for signature compatibility).
            **kwargs:
                sample_size: Few-shot sample size per block (default 28).
                seed: RNG seed (default 123).
        """
        if task != "text2onto":
            raise ValueError(f"{self.__class__.__name__} only supports task='text2onto' (got {task!r}).")

        if not self._is_loaded:
            self.load(model_id=self._default_model_id)

        documents: List[Dict[str, Any]] = train_data.get("documents", []) or []
        terms_to_documents: Dict[str, List[str]] = train_data.get("terms2docs", {}) or {}
        terms_to_types: Optional[Dict[str, List[str]]] = train_data.get("terms2types", None)

        sample_size = int(kwargs.get("sample_size", 28))
        seed = int(kwargs.get("seed", 123))

        self.build_few_shot_terms_block(
            documents=documents,
            terms_to_documents=terms_to_documents,
            sample_size=sample_size,
            seed=seed,
        )
        self.build_few_shot_types_block(
            documents=documents,
            terms_to_documents=terms_to_documents,
            terms_to_types=terms_to_types,
            sample_size=sample_size,
            seed=seed,
        )

    def predict(
        self,
        test_data: Any,
        task: str = "text2onto",
        ontologizer: bool = False,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        """
        Run term/type extraction over test documents.

        Args:
            test_data: A split bundle dict. Must contain "documents".
            task: Must be "text2onto".
            ontologizer: Unused here (kept for signature compatibility).
            **kwargs:
                max_docs: If > 0, limit number of docs processed.

        Returns:
            Prediction payload dict: {"terms": [...], "types": [...]}.
        """
        if task != "text2onto":
            raise ValueError(f"{self.__class__.__name__} only supports task='text2onto' (got {task!r}).")

        if not self.few_shot_terms_block or not self.few_shot_types_block:
            raise RuntimeError("Few-shot blocks are empty. Pipeline should call fit() before predict().")

        max_docs = int(kwargs.get("max_docs", -1))
        documents: List[Dict[str, Any]] = test_data.get("documents", []) or []
        if max_docs > 0:
            documents = documents[:max_docs]

        term_predictions: List[Dict[str, str]] = []
        type_predictions: List[Dict[str, str]] = []

        for doc_index, document in enumerate(documents, start=1):
            document_id = str(document.get("id", "unknown"))
            title = str(document.get("title", ""))
            text = str(document.get("text", ""))

            term_prompt = self._format_term_prompt(self.few_shot_terms_block, title, text)
            extracted_terms = self._parse_python_list_of_strings(self._generate_completion(term_prompt))
            for term in extracted_terms:
                normalized_term = (term or "").strip()
                if normalized_term:
                    term_predictions.append({"doc_id": document_id, "term": normalized_term})

            type_prompt = self._format_type_prompt(self.few_shot_types_block, title, text)
            extracted_types = self._parse_python_list_of_strings(self._generate_completion(type_prompt))
            for extracted_type in extracted_types:
                normalized_type = (extracted_type or "").strip()
                if normalized_type:
                    type_predictions.append({"doc_id": document_id, "type": normalized_type})

            if doc_index % 50 == 0:
                gc.collect()
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()

        # IMPORTANT: return only the prediction payload; LearnerPipeline wraps it.
        return {"terms": term_predictions, "types": type_predictions}
