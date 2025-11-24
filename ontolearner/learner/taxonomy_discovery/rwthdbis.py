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

import json
import os
import random
import re
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Callable
from functools import partial
from tqdm.auto import tqdm
import g4f
from g4f.client import Client as _G4FClient
import torch
from datasets import Dataset, DatasetDict
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
    set_seed,
)

from ...base import AutoLearner


class RWTHDBISSFTLearner(AutoLearner):
    """
    Supervised classifier for (parent, child) taxonomy edges.

    Model input format:
        "<relation template> ## <optional context>"

    Context building:
        If no `context_json_path` is provided, the learner precomputes a fixed-name
        context file `rwthdbis_onto_processed.json` under `output_dir/context/`
        from the ontology terms and stores the path in `self.context_json_path`.

    Attributes:
        model_name: Hugging Face model identifier.
        output_dir: Directory where checkpoints and tokenizer are saved/loaded.
        min_predictions: If no candidate is predicted positive, return the top-k
            by positive probability (k = min_predictions).
        max_length: Maximum tokenized length for inputs.
        per_device_train_batch_size: Micro-batch size per device.
        gradient_accumulation_steps: Gradient accumulation steps.
        num_train_epochs: Number of training epochs.
        learning_rate: Optimizer LR.
        weight_decay: Weight decay for AdamW.
        logging_steps: Logging interval for Trainer.
        save_strategy: HF saving strategy (e.g., 'epoch').
        save_total_limit: Max checkpoints to keep.
        fp16: Enable FP16 mixed precision.
        bf16: Enable BF16 mixed precision (on supported hardware).
        seed: Random seed for reproducibility.
        negative_ratio: Number of negatives per positive during training.
        bidirectional_templates: If True, also add reversed template examples.
        context_json_path: Path to the preprocessed term-context JSON. If None,
            the file is generated with the fixed prefix `rwthdbis_onto_*`.
        ontology_name: Logical dataset/domain label used in prompts and filtering
            (filenames still use the fixed `rwthdbis_onto_*` prefix).
        device: user-defined argument as 'cuda' or 'cpu'.
        model: Loaded/initialized `AutoModelForSequenceClassification`.
        tokenizer: Loaded/initialized `AutoTokenizer`.
    """

    # Sentences containing any of these phrases are pruned from term_info.
    _CONTEXT_REMOVALS = [
        "couldn't find any",
        "does not require",
        "assist you further",
        "feel free to",
        "I'm currently unable",
        "the search results",
        "I'm unable to",
        "recommend referring directly",
        "bear with me",
        "searching for the most relevant information",
        "I'm currently checking the most relevant",
        "already in English",
        "require further",
        "any additional information",
        "already an English",
        "don't have information",
        "I'm sorry,",
        "For further exploration",
        "For more detailed information",
    ]

    def __init__(
        self,
        min_predictions: int = 1,
        model_name: str = "distilroberta-base",
        output_dir: str = "./results/taxonomy-discovery",
        device: str = "cpu",
        max_length: int = 256,
        per_device_train_batch_size: int = 8,
        gradient_accumulation_steps: int = 4,
        num_train_epochs: int = 1,
        learning_rate: float = 2e-5,
        weight_decay: float = 0.01,
        logging_steps: int = 25,
        save_strategy: str = "epoch",
        save_total_limit: int = 1,
        fp16: bool = True,
        bf16: bool = False,
        seed: int = 42,
        negative_ratio: int = 5,
        bidirectional_templates: bool = True,
        context_json_path: Optional[str] = None,
        ontology_name: str = "Geonames",
    ) -> None:
        """
        Initialize the taxonomy-edge learner and set training/inference knobs.

        Notes:
            - Output artifacts are written under `output_dir`, including
              the model weights and tokenizer (for later `from_pretrained` loads).
            - If `context_json_path` is not provided, a new context file named
              `rwthdbis_onto_processed.json` is generated under `output_dir/context/`.
        """
        super().__init__()

        self.model_name = model_name
        safe_model_name = model_name.replace("/", "__")

        resolved_output = output_dir.format(model_name=safe_model_name)
        self.output_dir = str(Path(resolved_output))
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

        # Store provided argument values as-is (types are enforced by callers).
        self.min_predictions = min_predictions
        self.max_length = max_length
        self.per_device_train_batch_size = per_device_train_batch_size
        self.gradient_accumulation_steps = gradient_accumulation_steps
        self.num_train_epochs = num_train_epochs
        self.learning_rate = learning_rate
        self.weight_decay = weight_decay
        self.logging_steps = logging_steps
        self.save_strategy = save_strategy
        self.save_total_limit = save_total_limit
        self.fp16 = fp16
        self.bf16 = bf16
        self.seed = seed

        self.negative_ratio = negative_ratio
        self.bidirectional_templates = bidirectional_templates
        self.context_json_path = context_json_path

        self.ontology_name = ontology_name
        self.device = device
        self.model: Optional[AutoModelForSequenceClassification] = None
        self.tokenizer: Optional[AutoTokenizer] = None

        # Context caches built from the context JSON.
        self._context_exact: Dict[str, str] = {}  # lower(term) -> info
        self._context_rows: List[
            Dict[str, str]
        ] = []  # [{'term': str, 'term_info': str}, ...]

    def _is_windows(self) -> bool:
        """Return True if the current OS is Windows (NT)."""
        return (os.name == "nt") or (platform.system().lower() == "windows")

    def _normalize_text(self, raw_text: str, *, drop_questions: bool = False) -> str:
        """
        Normalize plain text consistently across the pipeline.

        Operations:
            - Remove markdown-like link patterns (e.g., '[[1]](http://...)').
            - Replace newlines with spaces; collapse repeated spaces.
            - Optionally drop sentences containing '?' (useful for model generations).

        Args:
            raw_text: Input text to normalize.
            drop_questions: If True, filter out sentences with '?'.

        Returns:
            str: Cleaned single-line string.
        """
        if raw_text is None:
            return ""
        text = str(raw_text)

        # Remove simple markdown link artifacts like [[1]](http://...)
        text = re.sub(r"\[\[\d+\]\]\(https?://[^\)]+\)", "", text)

        # Replace newlines with spaces and collapse multiple spaces
        text = text.replace("\n", " ")
        text = re.sub(r"\s{2,}", " ", text)

        if drop_questions:
            sentences = [s.strip() for s in text.split(".")]
            sentences = [s for s in sentences if s and "?" not in s]
            text = ". ".join(sentences)

        return text.strip()

    def _default_gpt_inference_with_dataset(self, term: str, dataset_name: str) -> str:
        """
        Generate a plain-text description for `term`, conditioned on `dataset_name`,
        via g4f (best-effort). Falls back to an empty string on failure.

        The raw output is then normalized with `_normalize_text(drop_questions=True)`.

        Args:
            term: Term to describe.
            dataset_name: Ontology/domain name used in the prompt.

        Returns:
            str: Cleaned paragraph describing the term, or "" on failure.
        """
        prompt = (
            f"Here is a: {term}, which is of domain name :{dataset_name}, translate it into english, "
            "Provide as detailed a definition of this term as possible in plain text.without any markdown format."
            "No reference link in result. "
            "- Focus on intrinsic properties; do not name other entities or explicit relationships.\n"
            "- Include classification/type, defining features, scope/scale, roles/functions, and measurable attributes when applicable.\n"
            "Output: Plain text paragraphs only, neutral and factual."
            f"Make sure all provided information can be used for discovering implicit relation of other {dataset_name} term, but don't mention the relation in result."
        )

        try:
            client = _G4FClient()
            response = client.chat.completions.create(
                model=g4f.models.default,
                messages=[{"role": "user", "content": prompt}],
            )
            raw_text = (
                response.choices[0].message.content
                if response and response.choices
                else ""
            )
        except Exception:
            raw_text = ""  # best-effort fallback

        return self._normalize_text(raw_text, drop_questions=True)

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        AutoLearner hook: route to training or prediction.

        Args:
            data: Ontology-like object (has `.taxonomies` or `.type_taxonomies.taxonomies`).
            test: If True, run inference; otherwise, train a model.

        Returns:
            If test=True, a list of accepted edges as dicts with keys `parent` and `child`;
            otherwise None.
        """
        return self._predict_pairs(data) if test else self._train_from_pairs(data)

    def _train_from_pairs(self, train_data: Any) -> None:
        """
        Train a binary classifier from ontology pairs.

        Steps:
            1) (Re)build the term-context JSON unless `context_json_path` is set.
            2) Extract positive (parent, child) edges from `train_data`.
            3) Sample negatives at `negative_ratio`.
            4) Tokenize, instantiate HF Trainer, train, and save.

        Args:
            train_data: Ontology-like object with `.type_taxonomies.taxonomies`
                (preferred) or `.taxonomies`, each item providing `parent` and `child`.

        Raises:
            ValueError: If no positive pairs are found.

        Side Effects:
            - Writes a trained model to `self.output_dir` (via `trainer.save_model`).
            - Writes the tokenizer to `self.output_dir` (via `save_pretrained`).
            - Sets `self.context_json_path` if it was previously unset.
              The generated context file is named `rwthdbis_onto_processed.json`.
        """
        # Always (re)build context from ontology unless an explicit file is provided
        if not self.context_json_path:
            context_dir = Path(self.output_dir) / "context"
            context_dir.mkdir(parents=True, exist_ok=True)
            processed_context_file = context_dir / "rwthdbis_onto_processed.json"

            # Remove stale file then regenerate
            if processed_context_file.exists():
                try:
                    processed_context_file.unlink()
                except Exception:
                    pass

            self.preprocess_context_from_ontology(
                ontology=train_data,
                processed_dir=context_dir,
                dataset_name=self.ontology_name,
                num_workers=max(1, min(os.cpu_count() or 2, 4)),
                provider=partial(
                    self._default_gpt_inference_with_dataset,
                    dataset_name=self.ontology_name,
                ),
                max_retries=5,
            )
            self.context_json_path = str(processed_context_file)

        # Reproducibility
        set_seed(self.seed)
        random.seed(self.seed)
        torch.manual_seed(self.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.seed)

        # Build labeled pairs from ontology; context comes from preprocessed map
        positive_pairs = self._extract_positive_pairs(train_data)
        if not positive_pairs:
            raise ValueError("No positive (parent, child) pairs found in train_data.")

        entity_names = sorted(
            {parent for parent, _ in positive_pairs}
            | {child for _, child in positive_pairs}
        )
        negative_pairs = self._generate_negatives(
            positives=positive_pairs,
            entities=entity_names,
            ratio=self.negative_ratio,
        )

        labels, input_texts = self._build_text_dataset(positive_pairs, negative_pairs)
        dataset_dict = DatasetDict(
            {"train": Dataset.from_dict({"label": labels, "text": input_texts})}
        )

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        # Ensure a pad token exists for robust padding across models.
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = (
                getattr(self.tokenizer, "eos_token", None)
                or getattr(self.tokenizer, "sep_token", None)
                or getattr(self.tokenizer, "cls_token", None)
            )

        def tokenize_batch(batch: Dict[str, List[str]]):
            """Tokenize a batch of input texts for HF Datasets mapping."""
            return self.tokenizer(
                batch["text"], truncation=True, max_length=self.max_length
            )

        tokenized_dataset = dataset_dict.map(
            tokenize_batch, batched=True, remove_columns=["text"]
        )
        data_collator = DataCollatorWithPadding(self.tokenizer)

        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.model_name,
            num_labels=2,
            id2label={0: "incorrect", 1: "correct"},
            label2id={"incorrect": 0, "correct": 1},
        )
        # Ensure model has a pad_token_id if tokenizer provides one.
        if (
            getattr(self.model.config, "pad_token_id", None) is None
            and self.tokenizer.pad_token_id is not None
        ):
            self.model.config.pad_token_id = self.tokenizer.pad_token_id

        training_args = TrainingArguments(
            output_dir=self.output_dir,
            learning_rate=self.learning_rate,
            per_device_train_batch_size=self.per_device_train_batch_size,
            gradient_accumulation_steps=self.gradient_accumulation_steps,
            num_train_epochs=self.num_train_epochs,
            weight_decay=self.weight_decay,
            save_strategy=self.save_strategy,
            save_total_limit=self.save_total_limit,
            logging_steps=self.logging_steps,
            dataloader_pin_memory=bool(torch.cuda.is_available()),
            fp16=self.fp16,
            bf16=self.bf16,
            report_to="none",
            save_safetensors=True,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=tokenized_dataset["train"],
            tokenizer=self.tokenizer,
            data_collator=data_collator,
        )
        trainer.train()
        trainer.save_model()
        # Persist tokenizer alongside the model for from_pretrained() loads.
        self.tokenizer.save_pretrained(self.output_dir)

    def _predict_pairs(self, eval_data: Any) -> List[Dict[str, str]]:
        """
        Score candidate pairs and return those predicted as positive.

        If no pair is predicted positive but `min_predictions` > 0, the top-k
        pairs by positive probability are returned.

        Args:
            eval_data: Ontology-like object with either `.pairs` (preferred) or
                `.type_taxonomies.taxonomies` / `.taxonomies`.

        Returns:
            list[dict]: Each dict has keys `parent` and `child`.
        """
        import torch.nn.functional as F

        self._ensure_loaded_for_inference()

        candidate_pairs = self._extract_pairs_for_eval(eval_data)
        if not candidate_pairs:
            return []

        accepted_pairs: List[Dict[str, str]] = []
        scored_candidates: List[Tuple[float, str, str, int]] = []

        self.model.eval()
        with torch.no_grad():
            for parent_term, child_term in candidate_pairs:
                input_text = self._format_input(parent_term, child_term)
                inputs = self.tokenizer(
                    input_text,
                    return_tensors="pt",
                    truncation=True,
                    max_length=self.max_length,
                )
                inputs = {key: tensor.to(self.device) for key, tensor in inputs.items()}
                logits = self.model(**inputs).logits
                probabilities = F.softmax(logits, dim=-1).squeeze(0)
                p_positive = float(probabilities[1].item())
                predicted_label = int(torch.argmax(logits, dim=-1).item())
                scored_candidates.append(
                    (p_positive, parent_term, child_term, predicted_label)
                )
                if predicted_label == 1:
                    accepted_pairs.append({"parent": parent_term, "child": child_term})

        if accepted_pairs:
            return accepted_pairs

        top_k = max(0, int(self.min_predictions))
        if top_k == 0:
            return []
        scored_candidates.sort(key=lambda item: item[0], reverse=True)
        return [
            {"parent": parent_term, "child": child_term}
            for (_prob, parent_term, child_term, _pred) in scored_candidates[:top_k]
        ]

    def _ensure_loaded_for_inference(self) -> None:
        """
        Load model and tokenizer from `self.output_dir` if not already loaded.

        Side Effects:
            - Sets `self.model` and `self.tokenizer`.
            - Moves the model to `self.device`.
            - Ensures `tokenizer.pad_token_id` is set if model config provides one.
        """
        if self.model is not None and self.tokenizer is not None:
            return
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.output_dir
        ).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(self.output_dir)
        if (
            self.tokenizer.pad_token_id is None
            and getattr(self.model.config, "pad_token_id", None) is not None
        ):
            self.tokenizer.pad_token_id = self.model.config.pad_token_id

    def _load_context_map(self) -> None:
        """
        Populate in-memory maps from the context JSON (`self.context_json_path`).

        Builds:
            - `_context_exact`: dict mapping lowercased term → term_info.
            - `_context_rows`: list of dict rows with 'term' and 'term_info'.

        If `context_json_path` is falsy or loading fails, both structures become empty.
        """
        if not self.context_json_path:
            self._context_exact = {}
            self._context_rows = []
            return
        try:
            rows = json.load(open(self.context_json_path, "r", encoding="utf-8"))
            self._context_exact = {
                str(row.get("term", "")).strip().lower(): str(
                    row.get("term_info", "")
                ).strip()
                for row in rows
            }
            self._context_rows = [
                {
                    "term": str(row.get("term", "")),
                    "term_info": str(row.get("term_info", "")),
                }
                for row in rows
            ]
        except Exception:
            self._context_exact = {}
            self._context_rows = []

    def _lookup_context_info(self, raw_term: str) -> str:
        """
        Retrieve textual context for a term using exact and simple fuzzy matching.

        - Exact: lowercased term lookup in `_context_exact`.
        - Fuzzy: split `raw_term` by commas, strip whitespace; treat each piece
                 as a case-insensitive substring against row['term'].

        Args:
            raw_term: Original term string (possibly comma-separated).

        Returns:
            str: Concatenated matches' term_info ('.' joined). Empty string if none.
        """
        if not raw_term:
            return ""
        term_key = raw_term.strip().lower()
        if term_key in self._context_exact:
            return self._context_exact[term_key]

        subterms = [re.sub(r"\s+", "", piece) for piece in raw_term.split(",")]
        matched_infos: List[str] = []
        for subterm in subterms:
            if not subterm:
                continue
            lower_subterm = subterm.lower()
            for row in self._context_rows:
                if lower_subterm in row["term"].lower():
                    info = row.get("term_info", "")
                    if info:
                        matched_infos.append(info)
                        break  # one hit per subterm
        return ".".join(matched_infos)

    def _extract_positive_pairs(self, ontology_obj: Any) -> List[Tuple[str, str]]:
        """
        Extract positive (parent, child) edges from an ontology-like object.

        Reads from `ontology_obj.type_taxonomies.taxonomies` (preferred) or
        falls back to `ontology_obj.taxonomies`. Each item must expose `parent`
        and `child` as attributes or dict keys.

        Returns:
            list[tuple[str, str]]: (parent, child) pairs (may be empty).
        """
        type_taxonomies = getattr(ontology_obj, "type_taxonomies", None)
        items = (
            getattr(type_taxonomies, "taxonomies", None)
            if type_taxonomies is not None
            else getattr(ontology_obj, "taxonomies", None)
        )
        pairs: List[Tuple[str, str]] = []
        if items:
            for item in items:
                parent_term = (
                    getattr(item, "parent", None)
                    if not isinstance(item, dict)
                    else item.get("parent")
                )
                child_term = (
                    getattr(item, "child", None)
                    if not isinstance(item, dict)
                    else item.get("child")
                )
                if parent_term and child_term:
                    pairs.append((str(parent_term), str(child_term)))
        return pairs

    def _extract_pairs_for_eval(self, ontology_obj: Any) -> List[Tuple[str, str]]:
        """
        Extract candidate pairs for evaluation.

        Prefers `ontology_obj.pairs` if present; otherwise falls back to the
        positive pairs from the ontology (see `_extract_positive_pairs`).

        Returns:
            list[tuple[str, str]]: Candidate (parent, child) pairs.
        """
        candidate_pairs = getattr(ontology_obj, "pairs", None)
        if candidate_pairs:
            pairs: List[Tuple[str, str]] = []
            for item in candidate_pairs:
                parent_term = (
                    getattr(item, "parent", None)
                    if not isinstance(item, dict)
                    else item.get("parent")
                )
                child_term = (
                    getattr(item, "child", None)
                    if not isinstance(item, dict)
                    else item.get("child")
                )
                if parent_term and child_term:
                    pairs.append((str(parent_term), str(child_term)))
            return pairs
        return self._extract_positive_pairs(ontology_obj)

    def _generate_negatives(
        self,
        positives: List[Tuple[str, str]],
        entities: List[str],
        ratio: int,
    ) -> List[Tuple[str, str]]:
        """
        Sample negative edges by excluding known positives and self-pairs.

        Constructs the cartesian product of entities (excluding (x, x)),
        removes all known positives, and samples up to `ratio * len(positives)`
        negatives uniformly at random.

        Args:
            positives: Known positive edges.
            entities: Unique set/list of entity terms.
            ratio: Target negatives per positive (lower-bounded by 1×).

        Returns:
            list[tuple[str, str]]: Sampled negative pairs (may be smaller).
        """
        positive_set = set(positives)
        all_possible = {
            (parent, child)
            for parent in entities
            for child in entities
            if parent != child
        }
        negative_candidates = list(all_possible - positive_set)

        target_count = max(len(positive_set) * max(1, ratio), len(positive_set))
        sample_count = min(target_count, len(negative_candidates))
        return (
            random.sample(negative_candidates, k=sample_count)
            if sample_count > 0
            else []
        )

    def _build_text_dataset(
        self,
        positives: List[Tuple[str, str]],
        negatives: List[Tuple[str, str]],
    ) -> Tuple[List[int], List[str]]:
        """
        Create parallel lists of labels and input texts for HF Datasets.

        Builds formatted inputs using `_format_input`, and duplicates examples in
        the reverse direction if `bidirectional_templates` is True.

        Returns:
            tuple[list[int], list[str]]: (labels, input_texts) where labels are
            1 for positive and 0 for negative.
        """
        self._load_context_map()

        labels: List[int] = []
        input_texts: List[str] = []

        def add_example(parent_term: str, child_term: str, label_value: int) -> None:
            """Append one (and optionally reversed) example to the dataset."""
            input_texts.append(self._format_input(parent_term, child_term))
            labels.append(label_value)
            if self.bidirectional_templates:
                input_texts.append(
                    self._format_input(child_term, parent_term, reverse=True)
                )
                labels.append(label_value)

        for parent_term, child_term in positives:
            add_example(parent_term, child_term, 1)
        for parent_term, child_term in negatives:
            add_example(parent_term, child_term, 0)

        return labels, input_texts

    def _format_input(
        self, parent_term: str, child_term: str, reverse: bool = False
    ) -> str:
        """
        Format a (parent, child) pair into relation text + optional context.

        Returns:
            str: "<relation template> [## Context. 'parent': ... 'child': ...]"
        """
        relation_text = (
            f"{child_term} is a subclass / child / subtype / descendant class of {parent_term}"
            if reverse
            else f"{parent_term} is the superclass / parent / supertype / ancestor class of {child_term}"
        )

        parent_info = self._lookup_context_info(parent_term)
        child_info = self._lookup_context_info(child_term)
        if not parent_info and not child_info:
            return relation_text

        context_text = (
            f"## Context. '{parent_term}': {parent_info} '{child_term}': {child_info}"
        )
        return f"{relation_text} {context_text}"

    def _fill_bucket_threaded(
        self, bucket_rows: List[dict], output_path: Path, provider: Callable[[str], str]
    ) -> None:
        """
        Populate a shard with provider-generated `term_info` using threads.

        Resumes from `output_path` if it already exists, periodically writes
        progress (every ~10 items), and finally dumps the full bucket to disk.
        """
        start_index = 0
        try:
            if output_path.is_file():
                existing_rows = json.load(open(output_path, "r", encoding="utf-8"))
                if isinstance(existing_rows, list) and existing_rows:
                    bucket_rows[: len(existing_rows)] = existing_rows
                    start_index = len(existing_rows)
        except Exception:
            pass

        for row_index in range(start_index, len(bucket_rows)):
            try:
                bucket_rows[row_index]["term_info"] = provider(
                    bucket_rows[row_index]["term"]
                )
            except Exception:
                bucket_rows[row_index]["term_info"] = ""
            if row_index % 10 == 1:
                json.dump(
                    bucket_rows[: row_index + 1],
                    open(output_path, "w", encoding="utf-8"),
                    ensure_ascii=False,
                    indent=2,
                )

        json.dump(
            bucket_rows,
            open(output_path, "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=2,
        )

    def _merge_part_files(
        self, dataset_name: str, merged_path: Path, shard_paths: List[Path]
    ) -> None:
        """
        Merge shard files into one JSON and filter boilerplate sentences.

        - Reads shard lists/dicts from `shard_paths`.
        - Drops sentences that contain markers in `_CONTEXT_REMOVALS` or the
          `dataset_name` string.
        - Normalizes the remaining text via `_normalize_text`.
        - Writes merged JSON to `merged_path`, then best-effort deletes shards.
        """
        merged_rows: List[dict] = []
        for shard_path in shard_paths:
            try:
                if not shard_path.is_file():
                    continue
                part_content = json.load(open(shard_path, "r", encoding="utf-8"))
                if isinstance(part_content, list):
                    merged_rows.extend(part_content)
                elif isinstance(part_content, dict):
                    merged_rows.append(part_content)
            except Exception:
                continue

        removal_markers = list(self._CONTEXT_REMOVALS) + [dataset_name]
        for row in merged_rows:
            term_info_raw = str(row.get("term_info", ""))
            kept_sentences: List[str] = []
            for sentence in term_info_raw.split("."):
                sentence_no_links = re.sub(
                    r"\[\[\d+\]\]\(https?://[^\)]+\)", "", sentence
                )
                if any(marker in sentence_no_links for marker in removal_markers):
                    continue
                kept_sentences.append(sentence_no_links)
            row["term_info"] = self._normalize_text(
                ".".join(kept_sentences), drop_questions=False
            )

        merged_path.parent.mkdir(parents=True, exist_ok=True)
        json.dump(
            merged_rows,
            open(merged_path, "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=4,
        )

        # best-effort cleanup
        for shard_path in shard_paths:
            try:
                os.remove(shard_path)
            except Exception:
                pass

    def _execute_for_terms(
        self,
        terms: List[str],
        merged_path: Path,
        shard_paths: List[Path],
        provider: Callable[[str], str],
        dataset_name: str,
        num_workers: int = 2,
    ) -> None:
        """
        Generate context for `terms`, writing shards to `shard_paths`, then merge.

        Always uses threads (pickling-safe for instance methods).
        Shows a tqdm progress bar and merges shards at the end.
        """
        worker_count = max(1, min(num_workers, os.cpu_count() or 2, 4))
        all_rows = [
            {"id": index, "term": term, "term_info": ""}
            for index, term in enumerate(terms)
        ]

        buckets: List[List[dict]] = [[] for _ in range(worker_count)]
        for reversed_index, row in enumerate(reversed(all_rows)):
            buckets[reversed_index % worker_count].append(row)

        total_rows = len(terms)
        progress_bar = tqdm(
            total=total_rows, desc=f"{dataset_name} generation (threads)"
        )

        def run_bucket(bucket_rows: List[dict], out_path: Path) -> int:
            self._fill_bucket_threaded(bucket_rows, out_path, provider)
            return len(bucket_rows)

        with ThreadPoolExecutor(max_workers=worker_count) as pool:
            futures = [
                pool.submit(
                    run_bucket, buckets[bucket_index], shard_paths[bucket_index]
                )
                for bucket_index in range(worker_count)
            ]
            for future in as_completed(futures):
                completed_count = future.result()
                if progress_bar:
                    progress_bar.update(completed_count)
        if progress_bar:
            progress_bar.close()

        self._merge_part_files(dataset_name, merged_path, shard_paths)

    def _re_infer_short_entries(
        self,
        merged_path: Path,
        re_shard_paths: List[Path],
        re_merged_path: Path,
        provider: Callable[[str], str],
        dataset_name: str,
        num_workers: int,
    ) -> int:
        """
        Re-query terms whose `term_info` is too short (< 50 chars).

        Process:
            - Read `merged_path`.
            - Filter boilerplate using `_CONTEXT_REMOVALS` and `dataset_name`.
            - Split into short/long groups by length 50.
            - Regenerate short group with `provider` in parallel (threads).
            - Merge regenerated + long back into `merged_path`.

        Returns:
            int: Count of rows still < 50 chars after re-inference.
        """
        merged_rows = json.load(open(merged_path, "r", encoding="utf-8"))

        removal_markers = list(self._CONTEXT_REMOVALS) + [dataset_name]
        short_rows: List[dict] = []
        long_rows: List[dict] = []

        for row in merged_rows:
            term_info_raw = str(row.get("term_info", ""))
            sentences = term_info_raw.split(".")
            for marker in removal_markers:
                sentences = [
                    sentence if marker not in sentence else "" for sentence in sentences
                ]
            filtered_info = self._normalize_text(
                ".".join(sentences), drop_questions=False
            )
            row["term_info"] = filtered_info

            (short_rows if len(filtered_info) < 50 else long_rows).append(row)

        worker_count = max(1, min(num_workers, os.cpu_count() or 2, 4))
        buckets: List[List[dict]] = [[] for _ in range(worker_count)]
        for row_index, row in enumerate(short_rows):
            buckets[row_index % worker_count].append(row)

        # Clean old re-inference shards
        for path in re_shard_paths:
            try:
                os.remove(path)
            except Exception:
                pass

        total_candidates = len(short_rows)
        progress_bar = tqdm(
            total=total_candidates, desc=f"{dataset_name} re-inference (threads)"
        )

        def run_bucket(bucket_rows: List[dict], out_path: Path) -> int:
            self._fill_bucket_threaded(bucket_rows, out_path, provider)
            return len(bucket_rows)

        with ThreadPoolExecutor(max_workers=worker_count) as pool:
            futures = [
                pool.submit(
                    run_bucket, buckets[bucket_index], re_shard_paths[bucket_index]
                )
                for bucket_index in range(worker_count)
            ]
            for future in as_completed(futures):
                completed_count = future.result()
                if progress_bar:
                    progress_bar.update(completed_count)
        if progress_bar:
            progress_bar.close()

        # Merge and write back
        self._merge_part_files(dataset_name, re_merged_path, re_shard_paths)
        new_rows = (
            json.load(open(re_merged_path, "r", encoding="utf-8"))
            if re_merged_path.is_file()
            else []
        )
        final_rows = long_rows + new_rows
        json.dump(
            final_rows,
            open(merged_path, "w", encoding="utf-8"),
            ensure_ascii=False,
            indent=4,
        )

        remaining_short = sum(
            1 for row in final_rows if len(str(row.get("term_info", ""))) < 50
        )
        return remaining_short

    def _extract_terms_from_ontology(self, ontology: Any) -> List[str]:
        """
        Collect unique term names from `ontology.type_taxonomies.taxonomies`,
        falling back to `ontology.taxonomies` if needed.

        Returns:
            list[str]: Sorted unique term list.
        """
        type_taxonomies = getattr(ontology, "type_taxonomies", None)
        taxonomies = (
            getattr(type_taxonomies, "taxonomies", None)
            if type_taxonomies is not None
            else getattr(ontology, "taxonomies", None)
        )
        unique_terms: set[str] = set()
        if taxonomies:
            for row in taxonomies:
                parent_term = (
                    getattr(row, "parent", None)
                    if not isinstance(row, dict)
                    else row.get("parent")
                )
                child_term = (
                    getattr(row, "child", None)
                    if not isinstance(row, dict)
                    else row.get("child")
                )
                if parent_term:
                    unique_terms.add(str(parent_term))
                if child_term:
                    unique_terms.add(str(child_term))
        return sorted(unique_terms)

    def preprocess_context_from_ontology(
        self,
        ontology: Any,
        processed_dir: str | Path,
        dataset_name: str = "GeoNames",
        num_workers: int = 2,
        provider: Optional[Callable[[str], str]] = None,
        max_retries: int = 5,
    ) -> Path:
        """
        Build `{id, term, term_info}` rows from an ontology object.

        Always regenerates the fixed-name file `rwthdbis_onto_processed.json`,
        performing:
            - Parallel generation of term_info in shards (`_execute_for_terms`),
            - Re-inference rounds for short entries (`_re_infer_short_entries`),
            - Final merge and cleanup,
            - Updates `self.context_json_path`.

        Filenames under `processed_dir`:
            - merged: `rwthdbis_onto_processed.json`
            - shards: `rwthdbis_onto_type_part{idx}.json`
            - re-infer shards: `rwthdbis_onto_re_inference{idx}.json`
            - re-infer merged: `rwthdbis_onto_Types_re_inference.json`

        Returns:
            Path: The merged context JSON path (`rwthdbis_onto_processed.json`).
        """
        provider = provider or partial(
            self._default_gpt_inference_with_dataset, dataset_name=dataset_name
        )

        processed_dir = Path(processed_dir)
        processed_dir.mkdir(parents=True, exist_ok=True)

        merged_path = processed_dir / "rwthdbis_onto_processed.json"
        if merged_path.exists():
            try:
                merged_path.unlink()
            except Exception:
                pass

        worker_count = max(1, min(num_workers, os.cpu_count() or 2, 4))
        shard_paths = [
            processed_dir / f"rwthdbis_onto_type_part{index}.json"
            for index in range(worker_count)
        ]
        re_shard_paths = [
            processed_dir / f"rwthdbis_onto_re_inference{index}.json"
            for index in range(worker_count)
        ]
        re_merged_path = processed_dir / "rwthdbis_onto_Types_re_inference.json"

        # Remove any leftover shards
        for path in shard_paths + re_shard_paths + [re_merged_path]:
            try:
                if path.exists():
                    path.unlink()
            except Exception:
                pass

        unique_terms = self._extract_terms_from_ontology(ontology)
        print(f"[Preprocess] Unique terms from ontology: {len(unique_terms)}")

        self._execute_for_terms(
            terms=unique_terms,
            merged_path=merged_path,
            shard_paths=shard_paths,
            provider=provider,
            dataset_name=dataset_name,
            num_workers=worker_count,
        )

        retry_round = 0
        while retry_round < max_retries:
            remaining_count = self._re_infer_short_entries(
                merged_path=merged_path,
                re_shard_paths=re_shard_paths,
                re_merged_path=re_merged_path,
                provider=provider,
                dataset_name=dataset_name,
                num_workers=worker_count,
            )
            print(
                f"[Preprocess] Re-infer round {retry_round + 1} done. Remaining short entries: {remaining_count}"
            )
            retry_round += 1
            if remaining_count == 0:
                break

        print(f"[Preprocess] Done. Merged context at: {merged_path}")
        self.context_json_path = str(merged_path)
        return merged_path
