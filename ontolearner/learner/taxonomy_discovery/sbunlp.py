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

import os
import re
import json
import importlib.util
from typing import Any, Dict, List, Optional, Tuple

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from ...base import AutoLearner

class SBUNLPFewShotLearner(AutoLearner):
    """
    Taxonomy-discovery via N×M batch prompting with a small Qwen model.

    Lifecycle
    ---------
    fit():
        Cache + clean training parent–child pairs.
    predict():
        Chunk (train pairs × test terms), prompt per chunk pair, parse, merge,
        and deduplicate predicted relations.
    """

    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-0.5B-Instruct",
        try_4bit: bool = True,
        num_train_chunks: int = 7,
        num_test_chunks: int = 7,
        max_new_tokens: int = 140,
        max_input_tokens: int = 1500,
        temperature: float = 0.0,
        top_p: float = 1.0,
        limit_num_prompts: Optional[int] = None,
        output_dir: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.model_name = model_name
        self.try_4bit = try_4bit

        self.num_train_chunks = num_train_chunks
        self.num_test_chunks = num_test_chunks

        self.max_new_tokens = max_new_tokens
        self.max_input_tokens = max_input_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.limit_num_prompts = limit_num_prompts

        self.output_dir = output_dir

        self.tokenizer: Optional[AutoTokenizer] = None
        self.model: Optional[AutoModelForCausalLM] = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.train_pairs_clean: List[Dict[str, str]] = []

    # ----------------------- small helpers ----------------------
    def _clean_pairs(pair_rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Normalize, drop empty or self-relations, and deduplicate by (parent, child).
        """
        cleaned_pairs: List[Dict[str, str]] = []
        seen_parent_child: set[Tuple[str, str]] = set()

        for pair_record in pair_rows or []:
            if not isinstance(pair_record, dict):
                continue

            parent_label = str(pair_record.get("parent", "")).strip()
            child_label = str(pair_record.get("child", "")).strip()
            if not parent_label or not child_label:
                continue

            normalized_key = (parent_label.lower(), child_label.lower())
            if normalized_key[0] == normalized_key[1]:  # parent==child
                continue
            if normalized_key in seen_parent_child:
                continue

            seen_parent_child.add(normalized_key)
            cleaned_pairs.append({"parent": parent_label, "child": child_label})

        return cleaned_pairs

    def _chunk_list(items: List[Any], num_chunks: int) -> List[List[Any]]:
        """
        Split `items` into `num_chunks` near-equal parts. Some chunks may be empty.
        """
        if num_chunks <= 0:
            return [items]
        total_items = len(items)
        base_size, remainder = divmod(total_items, num_chunks)

        chunks: List[List[Any]] = []
        start_index = 0
        for chunk_index in range(num_chunks):
            current_size = base_size + (1 if chunk_index < remainder else 0)
            end_index = start_index + current_size
            chunks.append(items[start_index:end_index])
            start_index = end_index
        return chunks

    def _ensure_dir(self, maybe_path: Optional[str]) -> None:
        if maybe_path:
            os.makedirs(maybe_path, exist_ok=True)

    # ---------------------- model load/gen ----------------------
    def load(self, **_: Any) -> None:
        """
        Load tokenizer/model; use 4-bit nf4 on CUDA if available + requested.
        """
        bnb_available = importlib.util.find_spec("bitsandbytes") is not None
        use_4bit_quant = bool(self.try_4bit and bnb_available and self.device == "cuda")

        quant_config = None
        if use_4bit_quant:
            from transformers import BitsAndBytesConfig
            quant_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
            )

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map=("auto" if self.device == "cuda" else None),
            torch_dtype=(torch.float16 if self.device == "cuda" else torch.float32),
            quantization_config=quant_config,
        )

    def _format_chat(self, user_text: str) -> str:
        """
        Wrap user text with the model's chat template (if present).
        """
        if hasattr(self.tokenizer, "apply_chat_template") and getattr(self.tokenizer, "chat_template", None):
            return self.tokenizer.apply_chat_template(
                [{"role": "user", "content": user_text}],
                tokenize=False,
                add_generation_prompt=True,
            )
        return user_text

    @torch.no_grad()
    def _generate(self, prompt_text: str) -> str:
        """
        Single prompt → model text. Clips *input* tokens to avoid overflow.
        """
        formatted_prompt = self._format_chat(prompt_text)
        prompt_token_ids = self.tokenizer(formatted_prompt, add_special_tokens=False, return_tensors=None)["input_ids"]
        if len(prompt_token_ids) > self.max_input_tokens:
            prompt_token_ids = prompt_token_ids[-self.max_input_tokens:]

        prompt_tensor = torch.tensor([prompt_token_ids]).to(self.model.device)

        generation = self.model.generate(
            input_ids=prompt_tensor,
            max_new_tokens=self.max_new_tokens,
            do_sample=(self.temperature > 0.0),
            temperature=self.temperature,
            top_p=self.top_p,
            pad_token_id=self.tokenizer.pad_token_id,
            eos_token_id=getattr(self.tokenizer, "eos_token_id", None),
            use_cache=True,
        )

        decoded_full = self.tokenizer.decode(generation[0], skip_special_tokens=True)
        decoded_prompt = self.tokenizer.decode(prompt_tensor[0], skip_special_tokens=True)
        return decoded_full[len(decoded_prompt):].strip() if decoded_full.startswith(decoded_prompt) else decoded_full.strip()

    # ------------------ prompt build & parsing ------------------
    def _build_prompt(train_pairs_chunk: List[Dict[str, str]],
                      test_terms_chunk: List[str]) -> str:
        """
        Few-shot with JSON examples + a block of test terms.
        The model must return ONLY a JSON array of {parent, child}.
        """
        examples_json = json.dumps(train_pairs_chunk, ensure_ascii=False, indent=2)
        test_types_block = "\n".join(test_terms_chunk)
        return (
            "From this file, extract all parent–child relations like in the examples.\n"
            "Return ONLY a JSON array of objects with keys 'parent' and 'child'.\n"
            "Output format:\n"
            "[\n"
            '  {"parent": "parent1", "child": "child1"},\n'
            '  {"parent": "parent2", "child": "child2"}\n'
            "]\n\n"
            "EXAMPLES (JSON):\n"
            f"{examples_json}\n\n"
            "TEST TYPES (between [PAIR] tags):\n"
            "[PAIR]\n"
            f"{test_types_block}\n"
            "[PAIR]\n"
            "Return only JSON."
        )

    def _parse_pairs(model_text: str) -> List[Dict[str, str]]:
        """
        Parse a model response into a list of {'parent','child'} dicts.
        """
        def deduplicate_and_normalize(dict_list: List[Dict[str, str]]) -> List[Dict[str, str]]:
            return SBUNLPFewShotLearner._clean_pairs(dict_list)

        response_text = model_text.strip()

        # 1) Direct JSON list
        try:
            maybe_json = json.loads(response_text)
            if isinstance(maybe_json, list):
                return deduplicate_and_normalize(maybe_json)
        except Exception:
            pass

        # 2) Find outermost [ ... ] and parse that
        outer_list_match = re.search(r"\[\s*(?:\{[\s\S]*?\}\s*,?\s*)*\]", response_text)
        if outer_list_match:
            try:
                array_json = json.loads(outer_list_match.group(0))
                if isinstance(array_json, list):
                    return deduplicate_and_normalize(array_json)
            except Exception:
                pass

        # 3) Nothing parsable
        return []

    # --------------------- AutoLearner hooks --------------------
    def fit(self, train_data: Any, task: str, ontologizer: bool = True):
        """
        Build the training example bank (parent–child pairs).
        """
        if task != "taxonomy-discovery":
            return super().fit(train_data, task, ontologizer)

        if ontologizer:
            # Convert ontology object → list of {"parent","child"} gold pairs
            gold_pairs_from_ontology = self.tasks_ground_truth_former(
                train_data, task="taxonomy-discovery"
            )
            self.train_pairs_clean = self._clean_pairs(gold_pairs_from_ontology)
        else:
            # Already a Python list of dicts
            self.train_pairs_clean = self._clean_pairs(train_data)

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        Main prediction path. Returns a deduplicated list of relations.
        """
        if not test:
            return None

        if self.model is None or self.tokenizer is None:
            self.load()

        # Build test vocabulary of types/terms
        if isinstance(data, list) and (len(data) == 0 or isinstance(data[0], str)):
            test_type_list: List[str] = data
        else:
            test_type_list = super().tasks_data_former(
                data=data, task="taxonomy-discovery", test=True
            )

        # Create N×M grid
        train_chunks = self._chunk_list(self.train_pairs_clean, self.num_train_chunks)
        test_chunks = self._chunk_list(test_type_list, self.num_test_chunks)

        self._ensure_dir(self.output_dir)

        merged_predicted_pairs: List[Dict[str, str]] = []
        issued_prompt_count = 0

        for train_chunk_index, train_pairs_chunk in enumerate(train_chunks, start=1):
            for test_chunk_index, test_terms_chunk in enumerate(test_chunks, start=1):
                issued_prompt_count += 1
                if self.limit_num_prompts and issued_prompt_count > self.limit_num_prompts:
                    break

                prompt_text = self._build_prompt(train_pairs_chunk, test_terms_chunk)
                model_response = self._generate(prompt_text)
                parsed_relation_pairs = self._parse_pairs(model_response)

                # Optional per-batch dump for debugging
                if self.output_dir:
                    batch_json_path = os.path.join(
                        self.output_dir, f"pairs_T{train_chunk_index}_S{test_chunk_index}.json"
                    )
                    with open(batch_json_path, "w", encoding="utf-8") as fp:
                        json.dump(parsed_relation_pairs, fp, ensure_ascii=False, indent=2)

                merged_predicted_pairs.extend(parsed_relation_pairs)

            if self.limit_num_prompts and issued_prompt_count >= (self.limit_num_prompts or 0):
                break

        # Deduplicate final list
        return self._clean_pairs(merged_predicted_pairs)
