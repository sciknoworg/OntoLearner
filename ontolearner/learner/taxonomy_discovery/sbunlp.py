# Copyright (c) 2025 SciKnowOrg
# License: MIT

import os
import re
import json
from typing import Any, Dict, List, Optional

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from ...base import AutoLearner


class SBUNLPFewShotLearner(AutoLearner):
    """
    Few-shot taxonomy discovery via N×M batch prompting.

    This learner:
      - Caches & cleans gold parent–child pairs during `fit`.
      - Splits (train pairs × test terms) into a grid of chunks.
      - Builds an instruction prompt per grid cell with few-shot JSON examples.
      - Generates and parses model outputs as JSON relations.
      - Merges & deduplicates all predicted edges.
    """

    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-0.5B-Instruct",
        try_4bit: bool = True,
        device: str = "cpu",
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
        """
        Initialize the learner and core generation / batching settings.

        Args:
            model_name: HF id/path of the causal LLM (e.g., Qwen Instruct).
            try_4bit: If True and on CUDA, load with 4-bit NF4 quantization.
            device: "cpu" or "cuda" for model execution.
            num_train_chunks: Number of chunks for the gold (parent, child) bank.
            num_test_chunks: Number of chunks for the test term list.
            max_new_tokens: Max new tokens to generate per prompt call.
            max_input_tokens: Clip the *input* prompt to this many tokens (tail kept).
            temperature: Sampling temperature; 0.0 uses greedy decoding.
            top_p: Nucleus sampling parameter (used when temperature > 0).
            limit_num_prompts: Optional hard cap on prompts issued (debug/cost).
            output_dir: Optional directory to save per-batch JSON predictions.
            **kwargs: Forwarded to the base class.
        """
        super().__init__(**kwargs)
        self.model_name = model_name
        self.try_4bit = try_4bit
        self.device = device

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
        self.train_pairs_clean: List[Dict[str, str]] = []

    def _clean_pairs(self, pair_rows: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Normalize, filter, and deduplicate relation pairs.

        Operations:
          - Cast 'parent'/'child' to strings and strip whitespace.
          - Drop rows with empty values.
          - Drop self-relations (case-insensitive parent == child).
          - Deduplicate by lowercase (parent, child).

        Args:
            pair_rows: Raw list of dicts with at least 'parent' and 'child'.

        Returns:
            Cleaned list of {'parent','child'} dicts.
        """
        cleaned, seen = [], set()
        for rec in pair_rows or []:
            if not isinstance(rec, dict):
                continue
            p = str(rec.get("parent", "")).strip()
            c = str(rec.get("child", "")).strip()
            if not p or not c:
                continue
            key = (p.lower(), c.lower())
            if key[0] == key[1] or key in seen:
                continue
            seen.add(key)
            cleaned.append({"parent": p, "child": c})
        return cleaned

    def _chunk_list(self, items: List[Any], num_chunks: int) -> List[List[Any]]:
        """
        Split a list into `num_chunks` near-equal contiguous parts.

        Args:
            items: Sequence to split.
            num_chunks: Number of chunks to produce; if <= 0, returns [items].

        Returns:
            List of chunks (some may be empty if len(items) < num_chunks).
        """
        if num_chunks <= 0:
            return [items]
        n = len(items)
        base, rem = divmod(n, num_chunks)
        out, start = [], 0
        for i in range(num_chunks):
            size = base + (1 if i < rem else 0)
            out.append(items[start : start + size])
            start += size
        return out

    def _ensure_dir(self, path: Optional[str]) -> None:
        """
        Create a directory if `path` is a non-empty string.

        Args:
            path: Directory to create (recursively). Ignored if falsy.
        """
        if path:
            os.makedirs(path, exist_ok=True)

    def load(self, **_: Any) -> None:
        """
        Load tokenizer and model; optionally enable 4-bit quantization.

        Assumes bitsandbytes is available if `try_4bit=True` on CUDA.
        Sets tokenizer pad token if missing. Places model on GPU (device_map='auto')
        when `device='cuda'`, otherwise on CPU.

        Args:
            **_: Unused kwargs for interface compatibility.
        """
        quant_config = None
        if self.try_4bit and self.device == "cuda":
            quant_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
            )

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        if getattr(self.tokenizer, "pad_token_id", None) is None:
            if getattr(self.tokenizer, "eos_token", None) is not None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            elif getattr(self.tokenizer, "unk_token", None) is not None:
                self.tokenizer.pad_token = self.tokenizer.unk_token

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            device_map=("auto" if self.device == "cuda" else None),
            torch_dtype=(torch.float16 if self.device == "cuda" else torch.float32),
            quantization_config=quant_config,
        )
        if self.device == "cpu":
            self.model.to("cpu")

    def _format_chat(self, user_text: str) -> str:
        """
        Wrap plain text with the model's chat template, if provided.

        Many instruction-tuned models expose `tokenizer.chat_template`.
        If available, use it to construct a proper chat prompt; otherwise,
        return the text unchanged.

        Args:
            user_text: Content of the user message.

        Returns:
            A generation-ready prompt string.
        """
        if hasattr(self.tokenizer, "apply_chat_template") and getattr(
            self.tokenizer, "chat_template", None
        ):
            return self.tokenizer.apply_chat_template(
                [{"role": "user", "content": user_text}],
                tokenize=False,
                add_generation_prompt=True,
            )
        return user_text

    @torch.no_grad()
    def _generate(self, prompt_text: str) -> str:
        """
        Generate text for a single prompt, guarding input length.

        Steps:
          1) Format prompt via chat template (if present).
          2) Tokenize and clip the *input* to `max_input_tokens` (tail kept).
          3) Call `model.generate` with configured decoding params.
          4) Strip the echoed prompt from the decoded output (if present).

        Args:
            prompt_text: Textual prompt to feed the model.

        Returns:
            Model continuation string (prompt-echo stripped when applicable).
        """
        formatted = self._format_chat(prompt_text)
        ids = self.tokenizer(formatted, add_special_tokens=False, return_tensors=None)[
            "input_ids"
        ]
        if len(ids) > self.max_input_tokens:
            ids = ids[-self.max_input_tokens :]
        device = next(self.model.parameters()).device
        input_ids = torch.tensor([ids], device=device)

        out = self.model.generate(
            input_ids=input_ids,
            max_new_tokens=self.max_new_tokens,
            do_sample=(self.temperature > 0.0),
            temperature=self.temperature,
            top_p=self.top_p,
            pad_token_id=self.tokenizer.pad_token_id,
            eos_token_id=getattr(self.tokenizer, "eos_token_id", None),
            use_cache=True,
        )

        decoded_full = self.tokenizer.decode(out[0], skip_special_tokens=True)
        decoded_prompt = self.tokenizer.decode(input_ids[0], skip_special_tokens=True)
        return (
            decoded_full[len(decoded_prompt) :].strip()
            if decoded_full.startswith(decoded_prompt)
            else decoded_full.strip()
        )

    def _build_prompt(
        self,
        train_pairs_chunk: List[Dict[str, str]],
        test_terms_chunk: List[str],
    ) -> str:
        """
        Construct a few-shot prompt with JSON examples and test terms.

        The prompt:
          - Shows several gold (parent, child) examples in JSON.
          - Lists the test terms (one per line) between [PAIR] tags.
          - Instructs to return ONLY a JSON array of {'parent','child'}.

        Args:
            train_pairs_chunk: Cleaned training relations for examples.
            test_terms_chunk: The current chunk of test terms.

        Returns:
            The fully formatted prompt string.
        """
        examples_json = json.dumps(train_pairs_chunk, ensure_ascii=False, indent=2)
        test_block = "\n".join(test_terms_chunk)
        prompt = (
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
            f"{test_block}\n"
            "[PAIR]\n"
            "Return only JSON."
        )
        return prompt

    def _parse_pairs(self, text: str) -> List[Dict[str, str]]:
        """
        Parse a generation string into a list of relation dicts.

        Parsing strategy:
          1) Try to parse the entire string as JSON; expect a list.
          2) Else, regex-extract the outermost JSON-like array and parse that.
          3) On failure, return an empty list.

        Args:
            text: Raw model output.

        Returns:
            Cleaned list of {'parent','child'} dicts (possibly empty).
        """
        text = text.strip()
        try:
            obj = json.loads(text)
            if isinstance(obj, list):
                return self._clean_pairs(obj)
        except Exception:
            pass
        m = re.search(r"\[\s*(?:\{[\s\S]*?\}\s*,?\s*)*\]", text)
        if m:
            try:
                obj = json.loads(m.group(0))
                if isinstance(obj, list):
                    return self._clean_pairs(obj)
            except Exception:
                pass
        return []

    def fit(self, train_data: Any, task: str, ontologizer: bool = True):
        """
        Cache and clean gold relations for few-shot prompting.

        For `task == "taxonomy-discovery"`:
          - If `ontologizer=True`, convert ontology-like input into
            a list of {'parent','child'} via the base helper.
          - Otherwise, accept a user-provided list directly.
          - Store a cleaned, deduplicated bank in `self.train_pairs_clean`.

        Args:
            train_data: Ontology-like object or list of relation dicts.
            task: Task selector (expects "taxonomy-discovery").
            ontologizer: Whether to transform ontology inputs.

        Returns:
            None. (State is stored on the instance.)
        """
        if task != "taxonomy-discovery":
            return super().fit(train_data, task, ontologizer)
        if ontologizer:
            gold = self.tasks_ground_truth_former(train_data, task="taxonomy-discovery")
            self.train_pairs_clean = self._clean_pairs(gold)
        else:
            self.train_pairs_clean = self._clean_pairs(train_data)

    def _taxonomy_discovery(
        self, data: Any, test: bool = False
    ) -> Optional[List[Dict[str, str]]]:
        """
        Run few-shot inference (test=True) or no-op during training.

        Inference steps:
          - Ensure tokenizer/model are loaded.
          - Normalize `data` to a list of test terms (via base helper if needed).
          - Create the N×M grid across (train_pairs_chunk × test_terms_chunk).
          - For each cell: build prompt → generate → parse → (optionally) save.
          - Merge and deduplicate all predicted pairs before returning.

        Args:
            data: Test input (ontology-like, list of strings, or mixed).
            test: If True, perform prediction; otherwise return None.

        Returns:
            On `test=True`: deduplicated list of {'parent','child'}.
            On `test=False`: None.
        """
        if not test:
            return None
        if self.model is None or self.tokenizer is None:
            self.load()

        if isinstance(data, list) and (len(data) == 0 or isinstance(data[0], str)):
            test_terms: List[str] = data
        else:
            test_terms = super().tasks_data_former(
                data=data, task="taxonomy-discovery", test=True
            )

        train_chunks = self._chunk_list(self.train_pairs_clean, self.num_train_chunks)
        test_chunks = self._chunk_list(test_terms, self.num_test_chunks)

        self._ensure_dir(self.output_dir)

        merged: List[Dict[str, str]] = []
        issued = 0

        for ti, tr in enumerate(train_chunks, 1):
            for si, ts in enumerate(test_chunks, 1):
                issued += 1
                if self.limit_num_prompts and issued > self.limit_num_prompts:
                    break
                prompt = self._build_prompt(tr, ts)
                resp = self._generate(prompt)
                pairs = self._parse_pairs(resp)

                if self.output_dir:
                    path = os.path.join(self.output_dir, f"pairs_T{ti}_S{si}.json")
                    with open(path, "w", encoding="utf-8") as f:
                        json.dump(pairs, f, ensure_ascii=False, indent=2)

                merged.extend(pairs)

            if self.limit_num_prompts and issued >= (self.limit_num_prompts or 0):
                break

        return self._clean_pairs(merged)
