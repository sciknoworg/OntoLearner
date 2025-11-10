# Copyright (c) 2025 SciKnowOrg
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import random
import re
import ast
import gc
from typing import Any, Dict, List, Optional, Set, Tuple
from collections import defaultdict

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

from ...base import AutoLearner, AutoLLM


# -----------------------------------------------------------------------------
# Concrete AutoLLM: local HF wrapper that follows the AutoLLM interface
# -----------------------------------------------------------------------------
class LocalAutoLLM(AutoLLM):
    """
    Handles loading and generation for a Hugging Face Causal Language Model (Qwen/TinyLlama).
    Uses 4-bit quantization for efficiency and greedy decoding by default.
    """

    def __init__(
        self, label_mapper: Any = None, device: str = "cpu", token: str = ""
    ) -> None:
        super().__init__(label_mapper=label_mapper, device=device, token=token)
        self.model = None
        self.tokenizer = None

    def load(
        self,
        model_id: str,
        load_in_4bit: bool = False,
        dtype: str = "auto",
        trust_remote_code: bool = True,
    ):
        """Load tokenizer + model, applying 4-bit quantization if specified and possible."""

        # Determine the target data type (default to float32 for CPU, float16 for GPU)
        torch_dtype_val = torch.float16 if torch.cuda.is_available() else torch.float32

        # Load the tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_id, trust_remote_code=trust_remote_code
        )
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        quant_config = None
        if load_in_4bit:
            # Configure BitsAndBytes for 4-bit loading
            quant_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
            )
            if torch_dtype_val is None:
                torch_dtype_val = torch.float16

        # Set device mapping (auto for multi-GPU or single GPU, explicit CPU otherwise)
        device_map = "auto" if (self.device != "cpu") else {"": "cpu"}

        # Load the Causal Language Model
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map=device_map,
            torch_dtype=torch_dtype_val,
            quantization_config=quant_config,
            trust_remote_code=trust_remote_code,
        )

        # Ensure model is on the correct device (redundant if device_map="auto" but safe)
        if self.device == "cpu":
            self.model.to("cpu")

    def generate(
        self,
        inputs: List[str],
        max_new_tokens: int = 64,
        temperature: float = 0.0,
        top_p: float = 1.0,
    ) -> List[str]:
        """Generate continuations for a list of prompts, returning only the generated part."""
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Model/tokenizer not loaded. Call .load() first.")

        # --- Generation Setup ---
        # Tokenize batch (padding is essential for batch inference)
        enc = self.tokenizer(inputs, return_tensors="pt", padding=True, truncation=True)
        input_ids = enc["input_ids"]
        attention_mask = enc["attention_mask"]

        # Move tensors to the model's device (e.g., cuda:0)
        model_device = next(self.model.parameters()).device
        input_ids = input_ids.to(model_device)
        attention_mask = attention_mask.to(model_device)

        # --- Generate ---
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_new_tokens=max_new_tokens,
                do_sample=(
                    temperature > 0.0
                ),  # Use greedy decoding if temperature is 0.0
                temperature=temperature,
                top_p=top_p,
                pad_token_id=self.tokenizer.eos_token_id,
            )

        # --- Post-processing: Extract only the generated tail ---
        decoded_outputs: List[str] = []
        for i, output_ids in enumerate(outputs):
            full_decoded_text = self.tokenizer.decode(
                output_ids, skip_special_tokens=True
            )
            prompt_text = self.tokenizer.decode(input_ids[i], skip_special_tokens=True)

            # Safely strip the prompt text from the full output
            if full_decoded_text.startswith(prompt_text):
                generated_tail = full_decoded_text[len(prompt_text) :].strip()
            else:
                # Fallback extraction (less robust if padding affects token indices)
                prompt_len = input_ids.shape[1]
                generated_tail = self.tokenizer.decode(
                    output_ids[prompt_len:], skip_special_tokens=True
                ).strip()
            decoded_outputs.append(generated_tail)

        return decoded_outputs


# -----------------------------------------------------------------------------
# Main Learner: SBUNLPFewShotLearner (Task A Text2Onto)
# -----------------------------------------------------------------------------
class SBUNLPFewShotLearner(AutoLearner):
    """
    Concrete learner implementing the Task A Text2Onto pipeline (Term and Type Extraction).
    It uses Few-Shot prompts generated from training data for inference.
    """

    def __init__(self, model: Optional[AutoLLM] = None, device: str = "cpu"):
        super().__init__()
        # self.model is an instance of LocalAutoLLM
        self.model = model or LocalAutoLLM(device=device)
        self.device = device
        # Cached in-memory prompt blocks built during the fit phase
        self.fewshot_terms_block: str = ""
        self.fewshot_types_block: str = ""

    # --- Few-shot construction (terms) ---
    def build_stratified_fewshot_prompt(
        self,
        documents_path: str,
        terms_path: str,
        sample_size: int = 28,
        seed: int = 123,
        max_chars_per_text: int = 1200,
    ) -> str:
        """
        Builds the few-shot exemplar block for Term Extraction using stratified sampling.
        """
        random.seed(seed)

        # Read documents (JSONL) into a list
        corpus_documents: List[Dict[str, Any]] = []
        with open(documents_path, "r", encoding="utf-8") as file_handle:
            for line in file_handle:
                if line.strip():
                    corpus_documents.append(json.loads(line))

        num_total_docs = len(corpus_documents)
        num_sample_docs = min(sample_size, num_total_docs)

        # Load the map of term -> [list of document IDs]
        with open(terms_path, "r", encoding="utf-8") as file_handle:
            term_to_doc_map = json.load(file_handle)

        # Invert map: document ID -> [list of terms]
        doc_id_to_terms_map = defaultdict(list)
        for term, doc_ids in term_to_doc_map.items():
            for doc_id in doc_ids:
                doc_id_to_terms_map[doc_id].append(term)

        # Define strata (groups of documents associated with specific terms)
        strata_map = defaultdict(list)
        for doc in corpus_documents:
            doc_id = doc.get("id", "")
            associated_terms = doc_id_to_terms_map.get(doc_id, ["no_term"])
            for term in associated_terms:
                strata_map[term].append(doc)

        # Perform proportional sampling across strata
        sampled_documents: List[Dict[str, Any]] = []
        for term_str, stratum_docs in strata_map.items():
            num_stratum_docs = len(stratum_docs)
            if num_stratum_docs == 0:
                continue

            # Calculate proportional sample size
            proportion = num_stratum_docs / num_total_docs
            num_to_sample_from_stratum = int(num_sample_docs * proportion)

            if num_to_sample_from_stratum > 0:
                sampled_documents.extend(
                    random.sample(
                        stratum_docs, min(num_to_sample_from_stratum, num_stratum_docs)
                    )
                )

        # Deduplicate sampled documents by ID and adjust count to exactly 'sample_size'
        unique_docs_by_id = {}
        for doc in sampled_documents:
            unique_docs_by_id[doc.get("id", "")] = doc

        final_sample_docs = list(unique_docs_by_id.values())

        if len(final_sample_docs) > num_sample_docs:
            final_sample_docs = random.sample(final_sample_docs, num_sample_docs)
        elif len(final_sample_docs) < num_sample_docs:
            remaining_docs = [
                d for d in corpus_documents if d.get("id", "") not in unique_docs_by_id
            ]
            needed_count = min(
                num_sample_docs - len(final_sample_docs), len(remaining_docs)
            )
            final_sample_docs.extend(random.sample(remaining_docs, needed_count))

        # Format the few-shot exemplar text block
        prompt_lines: List[str] = []
        for doc in final_sample_docs:
            doc_id = doc.get("id", "")
            title = doc.get("title", "")
            text = doc.get("text", "")

            # Truncate text if it exceeds the maximum character limit
            if max_chars_per_text and len(text) > max_chars_per_text:
                text = text[:max_chars_per_text] + "…"

            associated_terms = doc_id_to_terms_map.get(doc_id, [])
            prompt_lines.append(
                f"Document ID: {doc_id}\nTitle: {title}\nText: {text}\nAssociated Terms: {associated_terms}\n----------------------------------------"
            )

        prompt_block = "\n".join(prompt_lines)
        self.fewshot_terms_block = prompt_block
        return prompt_block

    # --- Few-shot construction (types) ---
    def build_types_fewshot_block(
        self,
        docs_jsonl: str,
        terms2doc_json: str,
        sample_per_term: int = 1,
        full_word: bool = True,
        case_sensitive: bool = True,
        max_chars_per_text: int = 800,
    ) -> str:
        """
        Builds the few-shot block for Type Extraction.
        This method samples documents based on finding an associated term/type within the text.
        """
        # Load documents into dict by ID
        docs_by_id = {}
        with open(docs_jsonl, "r", encoding="utf-8") as file_handle:
            for line in file_handle:
                line_stripped = line.strip()
                if line_stripped:
                    try:
                        doc = json.loads(line_stripped)
                        doc_id = doc.get("id", "")
                        if doc_id:
                            docs_by_id[doc_id] = doc
                    except json.JSONDecodeError:
                        continue

        # Load term -> [doc_id,...] map
        with open(terms2doc_json, "r", encoding="utf-8") as file_handle:
            term_to_doc_map = json.load(file_handle)

        flags = 0 if case_sensitive else re.IGNORECASE
        prompt_lines: List[str] = []

        # Iterate over terms (which act as types in this context)
        for term, doc_ids in term_to_doc_map.items():
            escaped_term = re.escape(term)
            # Create regex pattern for matching the term in the text
            pattern = rf"\b{escaped_term}\b" if full_word else escaped_term
            term_regex = re.compile(pattern, flags=flags)

            picked_count = 0
            for doc_id in doc_ids:
                doc = docs_by_id.get(doc_id)
                if not doc:
                    continue

                title = doc.get("title", "")
                text = doc.get("text", "")

                # Check if the term/type is actually present in the document text/title
                if term_regex.search(f"{title} {text}"):
                    text_content = text

                    # Truncate text if necessary
                    if max_chars_per_text and len(text_content) > max_chars_per_text:
                        text_content = text_content[:max_chars_per_text] + "…"

                    # Escape single quotes in the term for Python list formatting in the prompt
                    term_for_prompt = term.replace("'", "\\'")

                    prompt_lines.append(
                        f"Document ID: {doc_id}\nTitle: {title}\nText: {text_content}\nAssociated Types: ['{term_for_prompt}']\n----------------------------------------"
                    )
                    picked_count += 1

                    if picked_count >= sample_per_term:
                        break  # Move to the next term

        prompt_block = "\n".join(prompt_lines)
        self.fewshot_types_block = prompt_block
        return prompt_block

    def fit(
        self,
        train_docs_jsonl: str,
        terms2doc_json: str,
        sample_size: int = 28,
        seed: int = 123,
    ) -> None:
        """
        Fit phase: Builds and caches the few-shot prompt blocks from the training files.
        No model training occurs (Few-Shot/In-Context Learning).
        """
        # Build prompt block for Term extraction
        _ = self.build_stratified_fewshot_prompt(
            train_docs_jsonl, terms2doc_json, sample_size=sample_size, seed=seed
        )
        # Build prompt block for Type extraction
        _ = self.build_types_fewshot_block(
            train_docs_jsonl, terms2doc_json, sample_per_term=1
        )

    # -------------------------
    # Inference helpers (prompt construction and output parsing)
    # -------------------------
    def _build_term_prompt(self, example_block: str, title: str, text: str) -> str:
        """Constructs the full prompt for Term Extraction."""
        return f"""{example_block}
            [var]
            Title: {title}
            Text: {text}
            [var]
            Extract all relevant terms that could form the basis of an ontology from the above document.
            Return ONLY a Python list like ['term1', 'term2', ...] and nothing else.
            If no terms are found, return [].
            """

    def _build_type_prompt(self, example_block: str, title: str, text: str) -> str:
        """Constructs the full prompt for Type Extraction."""
        return f"""{example_block}
            [var]
            Title: {title}
            Text: {text}
            [var]
            Extract all relevant TYPES mentioned in the above document that could serve as ontology classes.
            Only consider content inside the [var] ... [var] block.
            Return ONLY a valid Python list like ['type1', 'type2'] and nothing else. If none, return [].
            """

    def _parse_list_like(self, raw_string: str) -> List[str]:
        """Try to extract a Python list of strings from model output robustly."""
        processed_string = raw_string.strip()
        if processed_string in ("[]", ""):
            return []

        # 1. Try direct evaluation
        try:
            parsed_value = ast.literal_eval(processed_string)
            if isinstance(parsed_value, list):
                # Filter to ensure only strings are returned
                return [item for item in parsed_value if isinstance(item, str)]
        except Exception:
            pass

        # 2. Try finding and evaluating text within outermost brackets [ ... ]
        bracket_match = re.search(r"\[[\s\S]*?\]", processed_string)
        if bracket_match:
            try:
                parsed_value = ast.literal_eval(bracket_match.group(0))
                if isinstance(parsed_value, list):
                    return [item for item in parsed_value if isinstance(item, str)]
            except Exception:
                pass

        # 3. Fallback: Find comma-separated quoted substrings (less robust, but catches errors)
        # Finds content inside either single quotes ('...') or double quotes ("...")
        quoted_matches = re.findall(r"'([^']+)'|\"([^\"]+)\"", processed_string)
        flattened_list = [a_match or b_match for a_match, b_match in quoted_matches]
        return flattened_list

    def _call_model_one(self, prompt: str, max_new_tokens: int = 120) -> str:
        """Calls the underlying LocalAutoLLM for a single prompt. Returns the raw tail output."""
        # self.model is an instance of LocalAutoLLM
        model_output = self.model.generate(
            [prompt], max_new_tokens=max_new_tokens, temperature=0.0, top_p=1.0
        )
        return model_output[0] if model_output else ""

    def predict_terms(
        self,
        docs_test_jsonl: str,
        out_jsonl: str,
        max_lines: int = -1,
        max_new_tokens: int = 120,
    ) -> int:
        """
        Runs Term Extraction on the test documents and saves results to a JSONL file.
        Returns: The count of individual terms written.
        """
        if not self.fewshot_terms_block:
            raise RuntimeError("Few-shot block for terms is empty. Call fit() first.")

        num_written_terms = 0
        with (
            open(docs_test_jsonl, "r", encoding="utf-8") as file_in,
            open(out_jsonl, "w", encoding="utf-8") as file_out,
        ):
            for line_index, line in enumerate(file_in, start=1):
                if 0 < max_lines < line_index:
                    break

                try:
                    document = json.loads(line.strip())
                except Exception:
                    continue  # Skip malformed JSON lines

                doc_id = document.get("id", "unknown")
                title = document.get("title", "")
                text = document.get("text", "")

                # Construct and call model
                prompt = self._build_term_prompt(self.fewshot_terms_block, title, text)
                raw_output = self._call_model_one(prompt, max_new_tokens=max_new_tokens)
                predicted_terms = self._parse_list_like(raw_output)

                # Write extracted terms
                for term_or_type in predicted_terms:
                    if isinstance(term_or_type, str) and term_or_type.strip():
                        file_out.write(
                            json.dumps({"doc_id": doc_id, "term": term_or_type.strip()})
                            + "\n"
                        )
                        num_written_terms += 1

                # Lightweight memory management for long runs
                if line_index % 50 == 0:
                    gc.collect()
                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()

        return num_written_terms

    def predict_types(
        self,
        docs_test_jsonl: str,
        out_jsonl: str,
        max_lines: int = -1,
        max_new_tokens: int = 120,
    ) -> int:
        """
        Runs Type Extraction on the test documents and saves results to a JSONL file.
        Returns: The count of individual types written.
        """
        if not self.fewshot_types_block:
            raise RuntimeError("Few-shot block for types is empty. Call fit() first.")

        num_written_types = 0
        with (
            open(docs_test_jsonl, "r", encoding="utf-8") as file_in,
            open(out_jsonl, "w", encoding="utf-8") as file_out,
        ):
            for line_index, line in enumerate(file_in, start=1):
                if 0 < max_lines < line_index:
                    break

                try:
                    document = json.loads(line.strip())
                except Exception:
                    continue  # Skip malformed JSON lines

                doc_id = document.get("id", "unknown")
                title = document.get("title", "")
                text = document.get("text", "")

                # Construct and call model using the dedicated type prompt block
                prompt = self._build_type_prompt(self.fewshot_types_block, title, text)
                raw_output = self._call_model_one(prompt, max_new_tokens=max_new_tokens)
                predicted_types = self._parse_list_like(raw_output)

                # Write extracted types
                for term_or_type in predicted_types:
                    if isinstance(term_or_type, str) and term_or_type.strip():
                        file_out.write(
                            json.dumps({"doc_id": doc_id, "type": term_or_type.strip()})
                            + "\n"
                        )
                        num_written_types += 1

                if line_index % 50 == 0:
                    gc.collect()
                    if torch.cuda.is_available():
                        torch.cuda.empty_cache()

        return num_written_types

    # --- Evaluation utilities (unchanged from prior definition, added docstrings) ---
    def load_gold_pairs(self, terms2doc_path: str) -> Set[Tuple[str, str]]:
        """Convert terms2docs JSON into a set of unique (doc_id, term) pairs, lowercased."""
        gold_pairs = set()
        with open(terms2doc_path, "r", encoding="utf-8") as file_handle:
            term_to_doc_map = json.load(file_handle)

        for term, doc_ids in term_to_doc_map.items():
            clean_term = term.strip().lower()
            for doc_id in doc_ids:
                gold_pairs.add((doc_id, clean_term))
        return gold_pairs

    def load_predicted_pairs(
        self, predicted_jsonl_path: str, key: str = "term"
    ) -> Set[Tuple[str, str]]:
        """Load predicted (doc_id, term/type) pairs from a JSONL file, lowercased."""
        predicted_pairs = set()
        with open(predicted_jsonl_path, "r", encoding="utf-8") as file_handle:
            for line in file_handle:
                try:
                    entry = json.loads(line.strip())
                except Exception:
                    continue
                doc_id = entry.get("doc_id")
                value = entry.get(key)
                if doc_id and value:
                    predicted_pairs.add((doc_id, value.strip().lower()))
        return predicted_pairs

    def evaluate_extraction_f1(
        self, terms2doc_path: str, predicted_jsonl: str, key: str = "term"
    ) -> float:
        """
        Computes set-based binary Precision, Recall, and F1 score against the gold pairs.
        """
        # Load the ground truth and predictions
        gold_set = self.load_gold_pairs(terms2doc_path)
        predicted_set = self.load_predicted_pairs(predicted_jsonl, key=key)

        # Build combined universe of all pairs for score calculation
        all_pairs = sorted(gold_set | predicted_set)

        # Create binary labels (1=present, 0=absent)
        y_true = [1 if pair in gold_set else 0 for pair in all_pairs]
        y_pred = [1 if pair in predicted_set else 0 for pair in all_pairs]

        # Use scikit-learn for metric calculation
        from sklearn.metrics import precision_recall_fscore_support

        precision, recall, f1, _ = precision_recall_fscore_support(
            y_true, y_pred, average="binary", zero_division=0
        )

        # Display results
        num_true_positives = len(gold_set & predicted_set)

        print("\n📊 Evaluation Results:")
        print(f"   ✅ Precision: {precision:.4f}")
        print(f"   ✅ Recall:    {recall:.4f}")
        print(f"   ✅ F1 Score:  {f1:.4f}")
        print(f"   📌 Gold pairs:      {len(gold_set)}")
        print(f"   📌 Predicted pairs:{len(predicted_set)}")
        print(f"   🎯 True Positives: {num_true_positives}")

        return float(f1)
