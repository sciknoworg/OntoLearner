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

from typing import Any, Dict, List, Optional
import re

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from ...base import AutoLearner


class SBUNLPZSLearner(AutoLearner):
    """
    Qwen-based blind term typing learner (Task B), implemented as an AutoLearner.

    Lifecycle:
      • `fit(...)` learns/records the allowed type inventory from the training payload.
      • `load(...)` explicitly loads the tokenizer/model (pass `model_id`/`token` here).
      • `predict(...)` prompts the model per term and returns normalized types limited
        to the learned inventory.
    """

    def __init__(
        self,
        device: str = "cpu",
        max_new_tokens: int = 64,
        temperature: float = 0.0,
        model_id: str = "Qwen/Qwen2.5-0.5B-Instruct",
        token: Optional[str] = None,
    ) -> None:
        """
        Configure runtime knobs. Model identity and auth are provided to `load(...)`.

        Args:
            device: Torch device policy ("cuda", "mps", or "cpu").
            max_new_tokens: Max tokens to generate per prompt (greedy decoding).
            temperature: Reserved for future sampling; generation is greedy here.
            model_id: Fallback model id/path used if `load()` is called without args.
            token: Fallback HF token used if `load()` is called without args.

        Side Effects:
            Initializes runtime configuration, instance defaults for `load()`,
            and placeholders for `tokenizer`, `model`, and `allowed_types`.
        """
        super().__init__()
        self.device = device
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature

        # Defaults that load() may use when its args are None
        self.model_id = model_id
        self.token = token

        # Placeholders populated by load()
        self.tokenizer: Optional[AutoTokenizer] = None
        self.model: Optional[AutoModelForCausalLM] = None

        # Learned inventory
        self.allowed_types: List[str] = []

        # Regex used to extract quoted strings from model output (e.g., "type")
        self._quoted_re = re.compile(r'"([^"]+)"')

    def load(
        self,
        model_id: Optional[str] = None,
        token: Optional[str] = None,
        dtype: Optional[torch.dtype] = None,
    ):
        """
        Load tokenizer and model weights explicitly.

        Argument precedence:
          1) Use `model_id` / `token` passed to this method (if provided).
          2) Else fall back to `self.model_id` / `self.token`.

        Device & dtype:
          • If `dtype` is None, the default is float16 on CUDA/MPS and float32 on CPU.
          • `device_map` is `"auto"` for non-CPU devices, `"cpu"` otherwise.

        Args:
            model_id: HF model id/path to load. If None, uses `self.model_id`.
            token: HF token if the model is gated. If None, uses `self.token`.
            dtype: Optional torch dtype override (e.g., `torch.float16`).

        Returns:
            self
        """
        resolved_model_id = model_id or self.model_id
        resolved_token = token if token is not None else self.token

        # Tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            resolved_model_id, token=resolved_token
        )
        if self.tokenizer.pad_token is None:
            # Prefer EOS as pad if available
            self.tokenizer.pad_token = self.tokenizer.eos_token

        # Device & dtype
        if dtype is None:
            if self.device == "cpu":
                resolved_dtype = torch.float32
            else:
                # Works for CUDA and Apple MPS
                resolved_dtype = torch.float16
        else:
            resolved_dtype = dtype

        device_map = "auto" if self.device != "cpu" else "cpu"

        self.model = AutoModelForCausalLM.from_pretrained(
            resolved_model_id,
            device_map=device_map,
            torch_dtype=resolved_dtype,  # keep torch_dtype for broad Transformers compatibility
            token=resolved_token,
        )
        return self

    def fit(self, train_data: Any, task: str, ontologizer: bool = True):
        """
        Learn the allowed type inventory from the training data.

        Normalization rules:
          • If `ontologizer=True`, the framework's `tasks_data_former(..., test=False)`
            is used to normalize `train_data`.
          • If a container exposes `.term_typings`, types are collected from there.
          • If the normalized data is a list of dicts with `"parent"`, unique parents
            become the allowed types.
          • If it's a list of strings, that unique set becomes the allowed types.

        Args:
            train_data: Training payload provided by the pipeline.
            task: Must be `"term-typing"`.
            ontologizer: If True, normalize via `tasks_data_former()` first.

        Returns:
            self

        Raises:
            ValueError: If `task` is not `"term-typing"`.
            TypeError: If the training data cannot be normalized to a list of
                strings or relationship dicts.
        """
        train_fmt = (
            self.tasks_data_former(data=train_data, task=task, test=False)
            if ontologizer
            else train_data
        )
        if task != "term-typing":
            raise ValueError("SBUNLPZSLearner only implements 'term-typing'.")

        # If framework passed a container with `.term_typings`, extract types from there
        if not isinstance(train_fmt, list):
            if hasattr(train_fmt, "term_typings"):
                try:
                    collected = set()
                    for tt in getattr(train_fmt, "term_typings") or []:
                        # tt.types could be list[str] or a single str
                        if hasattr(tt, "types"):
                            tvals = tt.types
                        elif isinstance(tt, dict) and "types" in tt:
                            tvals = tt["types"]
                        else:
                            tvals = None

                        if isinstance(tvals, (list, tuple, set)):
                            for x in tvals:
                                if isinstance(x, str):
                                    collected.add(x)
                        elif isinstance(tvals, str):
                            collected.add(tvals)

                    if collected:
                        self.allowed_types = sorted(collected)
                        return self
                except Exception:
                    # Fall through to error below if unexpected issues occur.
                    pass

            raise TypeError("For term-typing, expected a list of type labels at fit().")

        # At this point train_fmt is a list (original logic preserved)
        if train_fmt and isinstance(train_fmt[0], dict) and "parent" in train_fmt[0]:
            # Case A: Received raw relationships/pairs (e.g., from train_test_split).
            unique_types = set(r.get("parent") for r in train_fmt if r.get("parent"))
            self.allowed_types = sorted(unique_types)
        elif all(isinstance(x, str) for x in train_fmt):
            # Case B: Received a clean list of type labels (List[str]).
            self.allowed_types = sorted(set(train_fmt))
        else:
            raise TypeError(
                "For term-typing, input data format for fit() is invalid. "
                "Expected list of strings (types) or list of relationships (dicts)."
            )

        return self

    def predict(self, eval_data: Any, task: str, ontologizer: bool = True) -> Any:
        """
        Predict types for each term and return standardized rows.

        Expected inputs:
          • With `ontologizer=True`: a `list[str]` of terms (IDs are auto-generated),
            or a container exposing `.term_typings` from which `{'id','term'}` pairs
            can be extracted.
          • With `ontologizer=False`: a `list[dict]` of `{'id','term'}` to preserve IDs.

        Args:
            eval_data: Evaluation payload as described above.
            task: Must be `"term-typing"`.
            ontologizer: If True, normalize through the pipeline’s data former.

        Returns:
            A list of dictionaries:
                `{"id": str, "term": str, "types": List[str]}`.
        """
        if task != "term-typing":
            # Delegate to base for other tasks (not implemented here)
            return super().predict(eval_data, task, ontologizer=ontologizer)

        def _extract_list_of_dicts_from_term_typings(
            obj,
        ) -> Optional[List[Dict[str, str]]]:
            """Try to derive `[{id, term}, ...]` from an object with `.term_typings`."""
            tts = getattr(obj, "term_typings", None)
            if tts is None:
                return None
            out = []
            for tt in tts:
                if isinstance(tt, dict):
                    tid = tt.get("ID") or tt.get("id") or tt.get("Id") or tt.get("ID_")
                    tterm = tt.get("term") or tt.get("label") or tt.get("name")
                else:
                    tid = (
                        getattr(tt, "ID", None)
                        or getattr(tt, "id", None)
                        or getattr(tt, "Id", None)
                    )
                    tterm = (
                        getattr(tt, "term", None)
                        or getattr(tt, "label", None)
                        or getattr(tt, "name", None)
                    )
                if tid is None or tterm is None:
                    continue
                out.append({"id": str(tid), "term": str(tterm)})
            return out if out else None

        # Case A: ontologizer=True -> framework often provides list[str]
        if ontologizer:
            if isinstance(eval_data, list) and all(
                isinstance(x, str) for x in eval_data
            ):
                eval_pack = [
                    {"id": f"TT_{i:06d}", "term": t} for i, t in enumerate(eval_data)
                ]
            else:
                maybe = _extract_list_of_dicts_from_term_typings(eval_data)
                if maybe is not None:
                    eval_pack = maybe
                else:
                    # Last resort: attempt to coerce iterables of str
                    if hasattr(eval_data, "__iter__") and not isinstance(
                        eval_data, (str, bytes)
                    ):
                        lst = list(eval_data)
                        if all(isinstance(x, str) for x in lst):
                            eval_pack = [
                                {"id": f"TT_{i:06d}", "term": t}
                                for i, t in enumerate(lst)
                            ]
                        else:
                            raise TypeError(
                                "With ontologizer=True, eval_data must be list[str] of terms."
                            )
                    else:
                        raise TypeError(
                            "With ontologizer=True, eval_data must be list[str] of terms."
                        )
            return self._term_typing(eval_pack, test=True)

        # Case B: ontologizer=False -> expect list[dict], but tolerate containers
        else:
            if isinstance(eval_data, list) and all(
                isinstance(x, dict) for x in eval_data
            ):
                eval_pack = eval_data
            else:
                maybe = _extract_list_of_dicts_from_term_typings(eval_data)
                if maybe is not None:
                    eval_pack = maybe
                else:
                    if isinstance(eval_data, dict):
                        for key in ("term_typings", "terms", "items"):
                            if key in eval_data and isinstance(
                                eval_data[key], (list, tuple)
                            ):
                                converted = []
                                for x in eval_data[key]:
                                    if (
                                        isinstance(x, dict)
                                        and ("id" in x or "ID" in x)
                                        and ("term" in x or "name" in x)
                                    ):
                                        tid = x.get("ID") or x.get("id")
                                        tterm = x.get("term") or x.get("name")
                                        converted.append(
                                            {"id": str(tid), "term": str(tterm)}
                                        )
                                if converted:
                                    eval_pack = converted
                                    break
                        else:
                            raise TypeError(
                                "With ontologizer=False, eval_data must be a list of dicts with keys {'id','term'}."
                            )
                    else:
                        raise TypeError(
                            "With ontologizer=False, eval_data must be a list of dicts with keys {'id','term'}."
                        )
            return self._term_typing(eval_pack, test=True)

    def _term_typing(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        Internal implementation of the *term-typing* task.

        Training mode (`test=False`):
          • Expects a `list[str]` of allowed types. Stores a sorted unique copy.

        Inference mode (`test=True`):
          • Expects a `list[dict]` of `{"id","term"}` items.
          • Requires `load()` to have been called (model/tokenizer available).
          • Builds a blind prompt per item, generates text, parses quoted
            candidates, and filters them to `self.allowed_types`.

        Args:
            data: See the mode-specific expectations above.
            test: Set `True` to run inference; `False` to store the type inventory.

        Returns:
            • `None` in training mode.
            • `list[dict]` with `{"id","term","types":[...]}` in inference mode.

        Raises:
            TypeError: If `data` is not in the expected shape for the mode.
            RuntimeError: If model/tokenizer are not loaded at inference time.
        """
        if not test:
            # training: expect a list of strings (type labels)
            if not isinstance(data, list):
                raise TypeError("Expected a list of type labels at training time.")
            self.allowed_types = sorted(set(data))
            return None

        # Inference path
        if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
            raise TypeError(
                "At prediction time, expected a list of {'id','term'} dicts."
            )

        if self.model is None or self.tokenizer is None:
            raise RuntimeError(
                "Model/tokenizer not loaded. Call .load() before predict()."
            )

        results = []
        for item in data:
            term_id = item["id"]
            term_text = item["term"]
            prompt = self._build_blind_prompt(term_id, term_text, self.allowed_types)
            types = self._generate_and_parse_types(prompt)
            results.append({"id": term_id, "term": term_text, "types": types})

        return results

    def _format_types_inline(self, allowed: List[str]) -> str:
        """
        Format the allowed types for inline inclusion in prompts.

        Args:
            allowed: List of allowed type labels.

        Returns:
            A comma-separated string of quoted types, e.g.:
            `"type1", "type2", "type3"`. Returns an empty string for an empty list.
        """
        if not allowed:
            return ""
        return ", ".join(f'"{t}"' for t in allowed if isinstance(t, str) and t.strip())

    def _build_blind_prompt(
        self, term_id: str, term: str, allowed_types: List[str]
    ) -> str:
        """
        Construct the blind JSON prompt for a single term.

        The prompt:
          • Instructs the model to produce ONLY a JSON array of `{id, types}` objects.
          • Provides the allowed types list so the model should only use those.
          • Includes the single input item for which the model must decide types.

        Args:
            term_id: Identifier to carry through to the output JSON.
            term: The input term string to classify.
            allowed_types: Inventory used to constrain outputs.

        Returns:
            The full prompt string to feed to the LLM.
        """
        allowed_str = self._format_types_inline(allowed_types)
        return (
            "Identify the type(s) of the term in a second JSON file.\n"
            "A term can have more than one type.\n"
            "Output file must be in this format:\n"
            "[\n"
            '{ "id": "TT_465e8904", "types": [ "type1" ] },\n'
            '{ "id": "TT_01c7707e", "types": [ "type2", "type3" ] },\n'
            '{ "id": "TT_b20cb478", "types": [ "type4" ] }\n'
            "]\n"
            "The id must be taken from the input JSON file.\n"
            "You must find the type(s) for each term in the JSON file.\n"
            "Types must be selected only from the types list.\n\n"
            f"Types list: {allowed_str}\n\n"
            f'{{ "id": "{term_id}", "term": "{term}" }}'
        )

    def _generate_and_parse_types(self, prompt: str) -> List[str]:
        """
        Greedy-generate text, extract candidate types, and filter to the inventory.

        Workflow:
          1) Tokenize the prompt and generate deterministically (greedy).
          2) Decode and extract quoted substrings via regex (e.g., `"type"`).
          3) Keep only those candidates that exist in `self.allowed_types`.
          4) Return a unique, sorted list (stable across runs).

        Args:
            prompt: Fully formatted prompt string.

        Returns:
            List of predicted type labels (possibly empty if none found).

        Raises:
            AssertionError: If `model` or `tokenizer` are unexpectedly `None`.
        """
        assert self.model is not None and self.tokenizer is not None

        # Tokenize prompt and move tensors to model device to avoid device mismatch
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                do_sample=False,  # deterministic (greedy) decoding
                pad_token_id=self.tokenizer.eos_token_id,
            )

        # Decode full generated sequence (prompt + generation). Then extract quoted strings.
        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        candidates = self._quoted_re.findall(text)

        # Filter candidates to the allowed inventory and stabilize order.
        filtered = [c for c in candidates if c in self.allowed_types]
        return sorted(set(filtered))
