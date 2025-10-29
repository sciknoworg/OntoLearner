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

    This class reproduces the notebook logic:
      - Fit phase learns the *allowed type inventory* from training data.
      - Predict phase performs blind prompting per term using the learned type list.
      - Outputs are restricted to the allowed types and returned as [{"id", "types"}].

    Expected I/O (recommended):
      - fit(train_data, task="term-typing", ontologizer=True):
          The framework's AutoLearner.tasks_data_former() provides a unique list of
          type labels; we store it to `self.allowed_types`.
      - predict(eval_data, task="term-typing", ontologizer=False):
          Pass a list of dicts with keys {"id": str, "term": str} so IDs are preserved.
          Returns a list of dicts [{"id": ..., "types": [...] }].
    """

    def __init__(
        self,
        model_id: str = "Qwen/Qwen2.5-0.5B-Instruct",
        device: Optional[str] = None,
        max_new_tokens: int = 64,
        temperature: float = 0.0,
        token: Optional[str] = None,
    ) -> None:
        """
        Args:
            model_id: HF model id for Qwen.
            device: "cuda", "mps", or "cpu". Auto-detected if None.
            max_new_tokens: Generation cap per prompt.
            temperature: Not used for greedy decoding (kept for future).
            token: HF token if the model is gated.
        """
        super().__init__()

        # Basic configuration
        self.model_id = model_id
        # default device detection: prefer CUDA if available
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.token = token

        # Model/tokenizer placeholders (populated by load())
        self.tokenizer: Optional[AutoTokenizer] = None
        self.model: Optional[AutoModelForCausalLM] = None

        # Learned inventory of allowed type labels (populated by fit())
        self.allowed_types: List[str] = []

        # Regex used to extract quoted strings from model output (e.g. "type")
        self._quoted_re = re.compile(r'"([^"]+)"')

    def load(self, **kwargs: Any):
        """
        Load Qwen model and tokenizer.

        NOTE:
          - The HF arguments used here mirror your original code (`token=...`).
            You may see a deprecation warning for `torch_dtype` (older transformers);
            switching to `dtype=` is recommended but I did not change behavior here.
        """
        # Respect overrides from kwargs if provided
        model_id = kwargs.get("model_id", self.model_id)
        token = kwargs.get("token", self.token)

        # Load tokenizer. If the model is gated, pass token (original code uses `token`).
        # If your environment requires `use_auth_token=` replace here.
        self.tokenizer = AutoTokenizer.from_pretrained(model_id, token=token)

        # Ensure tokenizer has a pad token (some models omit it)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        # Device mapping for from_pretrained -> keep same behavior as original code
        device_map = "auto" if self.device != "cpu" else "cpu"
        # original code used torch_dtype; left as-is to avoid behavioral change
        torch_dtype = torch.float16 if self.device != "cpu" else torch.float32

        # Load the model weights. This can be heavy; keep same params as original.
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map=device_map,
            torch_dtype=torch_dtype,
            token=token,
        )
        return self

    # -------------------------------------------------------------------------
    # Fit / Predict interface
    # -------------------------------------------------------------------------
    def fit(self, train_data: Any, task: str, ontologizer: bool = True):
        """
        Learn the allowed type inventory from the training data.

        Expected behavior:
          - If `tasks_data_former(..., test=False)` returns a list of strings,
            set allowed_types to that list (deduped & sorted).
          - If it returns a list of dicts (relationships), extract unique 'parent'
            fields and use those as the allowed type inventory.

        This method contains a tolerant branch for the framework's custom container:
          If the returned `train_fmt` is not a list but has a `.term_typings` attribute
          (e.g., OntologyData object used by the framework), iterate that attribute
          and collect any `types` values found.
        """
        train_fmt = self.tasks_data_former(data=train_data, task=task, test=False) if ontologizer else train_data
        if task != "term-typing":
            raise ValueError("SBUNLPZSLearner only implements 'term-typing'.")

        # If framework passed a container with `.term_typings`, extract types from there
        if not isinstance(train_fmt, list):
            # handle OntologyData-like object with attribute 'term_typings'
            if hasattr(train_fmt, "term_typings"):
                try:
                    # term_typings is expected to be an iterable of objects with attribute `types`
                    collected = set()
                    for tt in getattr(train_fmt, "term_typings") or []:
                        # tt.types could be list[str] or a single str
                        if hasattr(tt, "types"):
                            tvals = tt.types
                        elif isinstance(tt, dict) and "types" in tt:
                            tvals = tt["types"]
                        else:
                            tvals = None

                        # Normalize both list and single-string cases
                        if isinstance(tvals, (list, tuple, set)):
                            for x in tvals:
                                if isinstance(x, str):
                                    collected.add(x)
                        elif isinstance(tvals, str):
                            collected.add(tvals)

                    # If we successfully collected types, set allowed_types and return
                    if collected:
                        self.allowed_types = sorted(collected)
                        return self
                    # else fall through to error below (no types found)
                except Exception:
                    # If anything unexpected occurs while iterating term_typings,
                    # gracefully fall through and raise the original TypeError below.
                    pass

            # not a supported non-list type -> keep original behavior (raise)
            raise TypeError("For term-typing, expected a list of type labels at fit().")

        # At this point train_fmt is a list (original logic preserved)
        if train_fmt and isinstance(train_fmt[0], dict) and "parent" in train_fmt[0]:
            # Case A: Received raw relationships/pairs (e.g., from train_test_split).
            # Extract unique parent types from the relationship records.
            unique_types = set(r.get("parent") for r in train_fmt if r.get("parent"))
            self.allowed_types = sorted(unique_types)
        elif all(isinstance(x, str) for x in train_fmt):
            # Case B: Received a clean list of type labels (List[str]).
            self.allowed_types = sorted(set(train_fmt))
        else:
            # The input is a list but not in either expected format -> raise
            raise TypeError("For term-typing, input data format for fit() is invalid. Expected list of strings (types) or list of relationships (dicts).")

        return self

    def predict(self, eval_data: Any, task: str, ontologizer: bool = True) -> Any:
        """
        Predict types for each term.

        Expected inputs:
          - With ontologizer=True: a list[str] of term strings (IDs are autogenerated).
          - With ontologizer=False: a list[dict] where each dict has keys {'id','term'}.

        This method tolerantly converts common framework containers (e.g., an
        OntologyData object exposing `.term_typings`) into the expected list[dict]
        shape so that the internal _term_typing() can run unchanged.
        """
        if task != "term-typing":
            # Delegate to base for other tasks (not implemented here)
            return super().predict(eval_data, task, ontologizer=ontologizer)

        def _extract_list_of_dicts_from_term_typings(obj) -> Optional[List[Dict[str, str]]]:
            """
            Helper: try to produce a list of {"id","term"} dicts from objects
            exposing a `term_typings` iterable. Supports either object-like
            TermTyping (attributes) or dict-style entries.
            """
            tts = getattr(obj, "term_typings", None)
            if tts is None:
                return None
            out = []
            for tt in tts:
                # support object-style TermTyping (attributes) and dict-style
                if isinstance(tt, dict):
                    # try several common key names for ID
                    tid = tt.get("ID") or tt.get("id") or tt.get("Id") or tt.get("ID_")
                    tterm = tt.get("term") or tt.get("label") or tt.get("name")
                else:
                    # object-style access
                    tid = getattr(tt, "ID", None) or getattr(tt, "id", None) or getattr(tt, "Id", None)
                    tterm = getattr(tt, "term", None) or getattr(tt, "label", None) or getattr(tt, "name", None)
                if tid is None or tterm is None:
                    # skip malformed entry - this is defensive so downstream code has valid inputs
                    continue
                out.append({"id": str(tid), "term": str(tterm)})
            return out if out else None

        # Case A: ontologizer=True -> framework often provides list[str]
        if ontologizer:
            if isinstance(eval_data, list) and all(isinstance(x, str) for x in eval_data):
                # Simple case: convert list of terms to list of dicts with generated IDs
                eval_pack = [{"id": f"TT_{i:06d}", "term": t} for i, t in enumerate(eval_data)]
            else:
                # Try to extract from a framework container (e.g., OntologyData)
                maybe = _extract_list_of_dicts_from_term_typings(eval_data)
                if maybe is not None:
                    eval_pack = maybe
                else:
                    # Last resort: if eval_data is some iterable of strings, convert it
                    try:
                        if hasattr(eval_data, "__iter__") and not isinstance(eval_data, (str, bytes)):
                            lst = list(eval_data)
                            if all(isinstance(x, str) for x in lst):
                                eval_pack = [{"id": f"TT_{i:06d}", "term": t} for i, t in enumerate(lst)]
                            else:
                                raise TypeError("With ontologizer=True, eval_data must be list[str] of terms.")
                        else:
                            raise TypeError("With ontologizer=True, eval_data must be list[str] of terms.")
                    except TypeError:
                        # re-raise to preserve original error semantics
                        raise
            # Delegate to internal inference routine
            return self._term_typing(eval_pack, test=True)

        # Case B: ontologizer=False -> we expect list[dict], but tolerate common containers
        else:
            if isinstance(eval_data, list) and all(isinstance(x, dict) for x in eval_data):
                eval_pack = eval_data
            else:
                # Try to extract from framework container (term_typings)
                maybe = _extract_list_of_dicts_from_term_typings(eval_data)
                if maybe is not None:
                    eval_pack = maybe
                else:
                    # As a final attempt, allow eval_data to be a dict with a list under some known keys
                    if isinstance(eval_data, dict):
                        for key in ("term_typings", "terms", "items"):
                            if key in eval_data and isinstance(eval_data[key], (list, tuple)):
                                converted = []
                                for x in eval_data[key]:
                                    # Accept dict-style entries that include id and term/name
                                    if isinstance(x, dict) and ("id" in x or "ID" in x) and ("term" in x or "name" in x):
                                        tid = x.get("ID") or x.get("id")
                                        tterm = x.get("term") or x.get("name")
                                        converted.append({"id": str(tid), "term": str(tterm)})
                                if converted:
                                    eval_pack = converted
                                    break
                        else:
                            # Could not convert; raise same TypeError as before
                            raise TypeError("With ontologizer=False, eval_data must be a list of dicts with keys {'id','term'}.")
                    else:
                        # Not a supported container -> raise
                        raise TypeError("With ontologizer=False, eval_data must be a list of dicts with keys {'id','term'}.")
            # Delegate to internal inference routine
            return self._term_typing(eval_pack, test=True)


    # -------------------------------------------------------------------------
    # Internal task implementations (AutoLearner hooks)
    # -------------------------------------------------------------------------
    def _term_typing(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        Core implementation:
         - training mode (test=False): `data` is a list of allowed type labels -> store them.
         - inference mode (test=True): `data` is a list of {"id","term"} -> produce [{"id","types"}].
        """
        if not test:
            # training: expect a list of strings (type labels)
            if not isinstance(data, list):
                raise TypeError("Expected a list of type labels at training time.")
            self.allowed_types = sorted(set(data))
            return None

        # Inference path
        if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
            raise TypeError("At prediction time, expected a list of {'id','term'} dicts.")

        # Ensure model and tokenizer are loaded
        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Model/tokenizer not loaded. Call .load() before predict().")

        results = []
        for item in data:
            # preserve incoming IDs and terms
            term_id = item["id"]
            term_text = item["term"]

            # build the blind JSON-prompt that instructs the model to output types
            prompt = self._build_blind_prompt(term_id, term_text, self.allowed_types)

            # generate and parse model output into allowed types
            types = self._generate_and_parse_types(prompt)

            # append result for this term (keep original id)
            # include the original term so downstream evaluation (and any consumers) can match by term
            results.append({"id": term_id, "term": term_text, "types": types})

        return results

    # -------------------------------------------------------------------------
    # Prompting + parsing
    # -------------------------------------------------------------------------

    def _format_types_inline(allowed: List[str]) -> str:
        """
        Format allowed types as comma-separated quoted strings for insertion into the prompt.
        Example: '"type1", "type2", "type3"'
        """
        return ", ".join(f'"{t}"' for t in allowed)

    def _build_blind_prompt(self, term_id: str, term: str, allowed_types: List[str]) -> str:
        """
        Construct the prompt given a single term. The prompt:
          - Instructs the model to produce a JSON array of {id, types} objects.
          - Provides the allowed types list (so the model should only use those).
          - Includes the single input item for which the model must decide types.

        Note: This is the same blind-prompting approach used in the original notebook.
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
        Greedy generate, then extract quoted strings and filter by allowed types.

        Important details:
          - We assert model/tokenizer presence before calling.
          - Tokenized inputs are moved to the model device (original code uses .to(self.model.device)).
          - The decoded text is scanned for quoted substrings using self._quoted_re.
          - Only quoted strings that are present in self.allowed_types are kept.
          - Returned list is unique & sorted for deterministic ordering.
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

        # Filter candidates to the allowed inventory
        filtered = [c for c in candidates if c in self.allowed_types]

        # Return unique & sorted for stability across runs
        return sorted(set(filtered))
