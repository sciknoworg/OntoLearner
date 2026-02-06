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
import random
from typing import Any, Callable, Dict, List, Optional, Tuple

import torch
from datasets import Dataset, DatasetDict
from functools import partial
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm.auto import tqdm
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
    set_seed,
)
from pathlib import Path
import g4f
from g4f.client import Client as _G4FClient

from ...base import AutoLearner



class RWTHDBISSFTLearner(AutoLearner):
    """
    Supervised term-typing

    Training expands multi-label examples into multiple single-label rows.
    Inference returns: [{"term": "<text>", "types": ["<label_str>"]}, ...]
    """

    def __init__(
        self,
        model_name: str = "microsoft/deberta-v3-small",
        trained_model_path: Optional[str] = None,
        output_dir: Optional[str] = None,
        device: str = "cpu",
        max_length: int = 64,
        per_device_train_batch_size: int = 16,
        gradient_accumulation_steps: int = 2,
        num_train_epochs: int = 3,
        learning_rate: float = 2e-5,
        weight_decay: float = 0.01,
        logging_steps: int = 50,
        save_strategy: str = "epoch",
        save_total_limit: int = 1,
        fp16: bool = False,
        bf16: bool = False,
        seed: int = 42,
        train_method: int = 2,
        context_json_path: Optional[str] = None,
        ontology_name: str = "Geonames",
    ) -> None:
        """Initialize the term-typing learner and configure training defaults.

        Args:
            model_name: Backbone HF model identifier (used if `trained_model_path` is None).
            trained_model_path: Optional path to a fine-tuned checkpoint for loading.
            output_dir: Directory to write checkpoints and tokenizer; defaults to './term_typing'.
            device: user-defined argument as 'cuda' or 'cpu'.
            max_length: Maximum tokenized sequence length.
            per_device_train_batch_size: Per-device batch size during training.
            gradient_accumulation_steps: Number of update accumulation steps.
            num_train_epochs: Training epochs.
            learning_rate: Optimizer learning rate.
            weight_decay: Weight decay coefficient.
            logging_steps: Logging interval (steps) for the Trainer.
            save_strategy: Checkpoint save strategy (e.g., 'epoch', 'steps', 'no').
            save_total_limit: Maximum number of checkpoints to keep.
            fp16: Enable mixed precision (FP16) if supported.
            bf16: Enable mixed precision (BF16) if supported.
            seed: Random seed for reproducibility.
            train_method: Training method selector (see _train_from_term_typings).

        Side Effects:
            Creates `output_dir` if it does not exist.

        Notes:
            The learner predicts exactly one label per term at inference time
            (argmax over logits).
        """
        super().__init__()
        self.model_name = model_name
        self.trained_model_path = trained_model_path
        self.output_dir = output_dir or "./term_typing"
        os.makedirs(self.output_dir, exist_ok=True)

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
        self.train_method = train_method

        self.context_json_path = context_json_path
        self.ontology_name = ontology_name

        self.device = device
        self.model: Optional[AutoModelForSequenceClassification] = None
        self.tokenizer: Optional[AutoTokenizer] = None
        self.id2label: Dict[int, str] = {}
        self.label2id: Dict[str, int] = {}

        # Context caches built from the context JSON.
        self._context_exact: Dict[str, str] = {}  # lower(term) -> info
        self._context_rows: List[
            Dict[str, str]
        ] = []  # [{'term': str, 'term_info': str}, ...]

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

    def _term_typing(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        Train or run inference for term typing, depending on `test`.

        When `test=False`, trains on `data.term_typings`.
        When `test=True`, predicts labels for provided terms.

        Args:
            data: If training, an object with `.term_typings` where each item has
                `term` and `types` (list[str]). If testing, either a `List[str]`
                of raw term texts or an object with `.term_typings`.
            test: If True, runs inference; otherwise trains.

        Returns:
            If `test=True`: a list of dicts like
            `[{"term": "<text>", "types": ["<label_str>"]}, ...]`.
            If `test=False`: None.

        Raises:
            ValueError: If required fields are missing from `data`.
        """
        if test:
            terms = self._collect_eval_terms(data)
            return self._predict_structured_output(terms)
        else:
            self._train_from_term_typings(
                train_data=data,
                train_method=self.train_method,
            )
            return None

################################################################################
#  Data Preprocessing ##########################################################
################################################################################

### Generate Context Information by GPT(via g4f.Client) ##########################################################

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

### Extract Context Information from Ontology ##########################################################

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

### Process Training / Inference Data - Augmented with Context Information (from Ontology or GPT) ##########################################################

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

### Process Training Data - for Fine-tuning for Text Classification(FT-TC) ##########################################################

    def _expand_multilabel_training_rows(
        self, term_typings: List[Any]
    ) -> Tuple[List[str], List[int], Dict[int, str], Dict[str, int]]:
        """
        Expand multi-label instances into single-label rows and derive label maps.

        Each training instance with fields:
            - `term`: str-like
            - `types`: list of label strings
        is expanded into len(types) rows with the same `term` and individual labels.

        Args:
            term_typings: Sequence of objects (e.g., dataclasses) exposing
                `.term` and `.types`.

        Returns:
            A tuple `(texts, label_ids, id2label, label2id)`:
                - texts: Flattened list of term strings (one per label).
                - label_ids: Parallel list of integer label ids.
                - id2label: Mapping from id -> label string.
                - label2id: Mapping from label string -> id.
        """
        label_strings: List[str] = []
        for instance in term_typings:
            label_strings.extend([str(label) for label in instance.types])

        unique_labels = sorted(set(label_strings))
        id2label = {i: label for i, label in enumerate(unique_labels)}
        label2id = {label: i for i, label in enumerate(unique_labels)}

        texts: List[str] = []
        label_ids: List[int] = []
        for instance in term_typings:
            term_text = str(instance.term)
            for label in instance.types:
                texts.append(term_text)
                label_ids.append(label2id[str(label)])

        return texts, label_ids, id2label, label2id

    def _collect_eval_terms(self, eval_data: Any) -> List[str]:
        """
        Collect the list of term texts to predict for evaluation.

        Accepts either:
            - A `List[str]` of raw term texts, or
            - An object with `.term_typings`, from which `.term` is extracted.

        Args:
            eval_data: Input carrier for terms.

        Returns:
            List of term strings.

        Raises:
            ValueError: If `eval_data` lacks the expected structure.
        """
        if isinstance(eval_data, list) and all(isinstance(x, str) for x in eval_data):
            terms = eval_data
        else:
            term_typings = getattr(eval_data, "term_typings", None)
            if term_typings is None:
                raise ValueError(
                    "Provide a List[str] OR an object with .term_typings for test=True."
                )
            terms = [str(instance.term) for instance in term_typings]
        return terms


################################################################################
#  Model Training ##########################################################
################################################################################

    def _train_from_term_typings(self, train_data: Any, train_method: int = 2) -> None:
        """Train the term-typing classifier from `.term_typings`.

        Steps:
            1) Seed RNGs for reproducibility.
            2) Expand multi-label examples into single-label rows.
            3) Build HF `DatasetDict`, tokenizer, and data collator.
            4) Initialize `AutoModelForSequenceClassification`.
            5) Train with `Trainer` and save model/tokenizer to `output_dir`.

        Args:
            train_data: Object with `.term_typings`; each item exposes
                `.term` (text) and `.types` (list[str]).

        Raises:
            ValueError: If `train_data` does not provide `.term_typings`.

        Side Effects:
            Writes a trained model to `self.output_dir` and updates
            `self.id2label` / `self.label2id`.
        """

        set_seed(self.seed)
        random.seed(self.seed)
        torch.manual_seed(self.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.seed)

        term_typings: List[Any] = getattr(train_data, "term_typings", None)
        ## term_typings: [TermTyping(ID='TT_65ab367d', term='degree Fahrenheit', types=['temperature unit']), TermTyping(ID='TT_7140a11f', term='week', types=['time unit'])]

        if term_typings is None:
            raise ValueError("train_data must provide .term_typings for term-typing.")

        ## train_method: 1: DS-CL, 2: FT-TC, 3: SKPT
        train_method_dict = {
            1: "DS-CL: Domain-specific Continual Learning",
            2: "FT-TC: Fine-tuning for Text Classification",
            3: "SKPT: Structured Knowledge Prompt Tuning"
        }

        backbone = self.trained_model_path or self.model_name
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(backbone, use_fast=True)
        except Exception:
            # fallback if fast tokenizer isn't available
            self.tokenizer = AutoTokenizer.from_pretrained(backbone, use_fast=False)

################################################################################
        ### Best Performance Method: 1. DS-CL + FT-TC / 2. DS-CL + SKPT -> Choose depends on the dataset.
        # If the dataset is small and the number of types is samll, use FT-TC.
        # If the dataset is large and the number of types is small, use DS-CL + FT-TC.
        # If the dataset is small and the number of types is large, use SKPT.
        # If the dataset is large and the number of types is large, use DS-CL + SKPT.
################################################################################

        if train_method == 1:
            ### DS-CL: Domain-specific Continual Learning ###
            print(f"Train method: {train_method_dict[train_method]}")
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

            self._load_context_map()
            unique_items = sorted({
                str(tt.term) for tt in term_typings
            } | {
                str(t) for tt in term_typings for t in tt.types
            })
            pretrain_texts_list = [
                self._lookup_context_info(item) for item in unique_items
            ]
            dataset = DatasetDict({'train': Dataset.from_dict({'text': pretrain_texts_list})})
            self.model = AutoModelForCausalLM.from_pretrained(
                self.model_name, device_map="auto"
            )
            self.num_train_epochs = 3
            self.per_device_train_batch_size = 4

        if train_method == 2:
            ### FT-TC: Fine-tuning for Text Classification ###
            print(f"Train method: {train_method_dict[train_method]}")

            texts, label_ids, self.id2label, self.label2id = (
                self._expand_multilabel_training_rows(term_typings)
            )

            # Get context information from the context JSON.
            #self._load_context_map()
            #demo_texts = [_format_term_with_context(text) for text in texts[:10]]
            #print(demo_texts)

            ## texts: ['degree Fahrenheit', 'week']
            ## label_ids: [0, 1]
            ## self.id2label: {'0': 'temperature unit', '1': 'time unit'}
            ## self.label2id: {'temperature unit': 0, 'time unit': 1}

            dataset = DatasetDict(
                {"train": Dataset.from_dict({"labels": label_ids, "text": texts})}
            )

            self.model = AutoModelForSequenceClassification.from_pretrained(
                backbone,
                num_labels=len(self.id2label),
                id2label=self.id2label,
                label2id=self.label2id,
            )

        if train_method == 3:
            ### SKPT: Structured Knowledge Prompt Tuning ###
            print(f"Train method: {train_method_dict[train_method]}")
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

            texts, label_ids, self.id2label, self.label2id = (
                self._expand_multilabel_training_rows(term_typings)
            )
            # Get context information from the context JSON and build prompt-style inputs.
            self._load_context_map()

            ################################################################################
            # Build prompt-style inputs.
            # References:
            # WordNet: ”Given the term {term} from the WordNet dataset, classify it intoone of the following types: [’adj’, ’adverb’, ’noun’, ’verb’]. Result:”
            # GeoNames: ”{term} geographically is a ?”
            # UMLS: ”{term} in medicine / biomedicine is a ?”
            # GO: ”{term} in biological is a ?”
            ################################################################################
            def _format_term_with_context(term: str) -> str:
                term_info = self._lookup_context_info(term)
                if term_info:
                    return f'''[ Knowledge ]
                            Biological term in Gene Ontology : { term }
                            Describe : { term_info }
                            [ Prediction ]
                            Text : "{ term } in biological is a ?"
                            Ans:
                    '''
                return f'''[ Knowledge ]
                            Biological term in Gene Ontology : { term }
                            Describe : { term_info }
                            [ Prediction ]
                            Text : "{ term } in biological is a ?"
                            Ans:
                    '''

            texts = [_format_term_with_context(text) for text in texts]

            ## label_ids: [0, 1]
            ## self.id2label: {'0': 'temperature unit', '1': 'time unit'}
            ## self.label2id: {'temperature unit': 0, 'time unit': 1}

            dataset = DatasetDict(
                {"train": Dataset.from_dict({"labels": label_ids, "text": texts})}
            )

            #  Also can train the model as CausalLM for the prompt-style inputs.
            self.model = AutoModelForSequenceClassification.from_pretrained(
                backbone,
                num_labels=len(self.id2label),
                id2label=self.id2label,
                label2id=self.label2id,
            )

################################################################################
        # Common Settings for Training
################################################################################

        def tokenize_batch(batch: Dict[str, List[str]]):
            """Tokenize a batch of texts with truncation and max length."""
            return self.tokenizer(
                batch["text"], truncation=True, max_length=self.max_length
            )
        tokenized = dataset.map(
            tokenize_batch,
            batched=True,
            remove_columns=["text"],
        )
        data_collator = DataCollatorWithPadding(self.tokenizer)

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
            fp16=self.fp16,
            bf16=self.bf16,
            report_to=[],
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=tokenized["train"],
            tokenizer=self.tokenizer,
            data_collator=data_collator,
        )

        trainer.train()
        trainer.save_model(self.output_dir)
        self.tokenizer.save_pretrained(self.output_dir)



    def _ensure_loaded_for_inference(self) -> None:
        """Load model/tokenizer for inference if not already loaded.

        Loads from `trained_model_path` if set, otherwise from `output_dir`.
        Also restores `id2label`/`label2id` from the model config when present,
        moves the model to the configured device, and sets eval mode.
        """
        if self.model is not None and self.tokenizer is not None:
            return
        model_path = self.trained_model_path or self.output_dir
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
        except Exception:
            self.tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False)

        cfg = self.model.config
        if hasattr(cfg, "id2label") and hasattr(cfg, "label2id"):
            self.id2label = dict(cfg.id2label)
            self.label2id = dict(cfg.label2id)

        self.model.to(self.device).eval()

################################################################################
#  Model Inference ##########################################################
################################################################################

    def _predict_label_ids(self, terms: List[str]) -> List[int]:
        """Predict label ids (argmax) for a list of term strings.

        Ensures model/tokenizer are loaded, then performs forward passes
        term-by-term and collects the argmax label id.

        Args:
            terms: List of raw term texts.

        Returns:
            List of integer label ids corresponding to `terms`.
        """
        self._ensure_loaded_for_inference()
        model_device = next(self.model.parameters()).device
        predictions: List[int] = []
        for term_text in tqdm(
            terms, desc="Inference", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"
        ):
            inputs = self.tokenizer(
                term_text,
                return_tensors="pt",
                truncation=True,
                max_length=self.max_length,
            )
            inputs = {name: tensor.to(model_device) for name, tensor in inputs.items()}
            with torch.no_grad():
                logits = self.model(**inputs).logits
                predictions.append(int(torch.argmax(logits, dim=-1).item()))
        return predictions

    def _predict_structured_output(
        self, terms: List[str]
    ) -> List[Dict[str, List[str]]]:
        """
        Convert predicted label IDs into evaluator-friendly structured outputs.

        The output format is:
            [{"term": "<text>", "types": ["<label_str>"]}, ...]

        Args:
            terms: Raw term texts to classify.

        Returns:
            List of dicts mapping each input term to a list with its predicted
            label string. Falls back to stringified id if label mapping is absent.
        """
        label_ids = self._predict_label_ids(terms)
        id2label_map = self.id2label or {}  # fallback handled below

        results: List[Dict[str, List[str]]] = []
        for term_text, label_id in zip(terms, label_ids):
            label_str = id2label_map.get(int(label_id), str(int(label_id)))
            results.append({"term": term_text, "types": [label_str]})
        return results
