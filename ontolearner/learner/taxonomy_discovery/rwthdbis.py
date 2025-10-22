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
import time
import platform
import multiprocessing
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

    If no `context_json_path` is provided, the class precomputes a
    context file ({ontology_name}_processed.json) directly from the ontology
    object.
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
        output_dir: str = "./results/{model_name}",
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
        ontology_name: str = "Geonames"
    ) -> None:
        super().__init__()

        self.model_name = model_name
        self.safe_model_name = model_name.replace("/", "__")

        resolved_output = output_dir.format(model_name=self.safe_model_name)
        self.output_dir = str(Path(resolved_output))
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

        self.min_predictions = int(min_predictions)
        self.max_length = int(max_length)
        self.per_device_train_batch_size = int(per_device_train_batch_size)
        self.gradient_accumulation_steps = int(gradient_accumulation_steps)
        self.num_train_epochs = float(num_train_epochs)
        self.learning_rate = float(learning_rate)
        self.weight_decay = float(weight_decay)
        self.logging_steps = int(logging_steps)
        self.save_strategy = str(save_strategy)
        self.save_total_limit = int(save_total_limit)
        self.fp16 = bool(fp16)
        self.bf16 = bool(bf16)
        self.seed = int(seed)

        self.negative_ratio = int(negative_ratio)
        self.bidirectional_templates = bool(bidirectional_templates)
        self.context_json_path = context_json_path

        self.ontology_name = ontology_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model: Optional[AutoModelForSequenceClassification] = None
        self.tokenizer: Optional[AutoTokenizer] = None

        os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
        os.environ.setdefault("WANDB_DISABLED", "true")
        os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")

        self._context_exact: Dict[str, str] = {}       # lower(term) -> info
        self._context_rows: List[Dict[str, str]] = []  # [{'term': str, 'term_info': str}, ...]

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Optional[Any]:
        return self._predict_pairs(data) if test else self._train_from_pairs(data)

    def _train_from_pairs(self, train_data: Any) -> None:
        # Always (re)build context from ontology unless an explicit file is provided
        if not self.context_json_path:
            context_dir = Path(self.output_dir) / "context"
            context_dir.mkdir(parents=True, exist_ok=True)
            processed_context_file = context_dir / f"{self.ontology_name}_processed.json"

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
                provider=partial(self._default_gpt_inference_with_dataset, dataset_name=self.ontology_name),
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

        entity_names = sorted({parent for parent, _ in positive_pairs} | {child for _, child in positive_pairs})
        negative_pairs = self._generate_negatives(
            positives=positive_pairs,
            entities=entity_names,
            ratio=self.negative_ratio,
        )

        labels, texts = self._build_text_dataset(positive_pairs, negative_pairs)


        datasets = DatasetDict({"train": Dataset.from_dict({"label": labels, "text": texts})})

        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = (
                getattr(self.tokenizer, "eos_token", None)
                or getattr(self.tokenizer, "sep_token", None)
                or getattr(self.tokenizer, "cls_token", None)
            )

        def tokenize_batch(batch: Dict[str, List[str]]):
            return self.tokenizer(batch["text"], truncation=True, max_length=self.max_length)

        tokenized = datasets.map(tokenize_batch, batched=True, remove_columns=["text"])
        collator = DataCollatorWithPadding(self.tokenizer)

        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.model_name,
            num_labels=2,
            id2label={0: "incorrect", 1: "correct"},
            label2id={"incorrect": 0, "correct": 1},
        )
        if getattr(self.model.config, "pad_token_id", None) is None and self.tokenizer.pad_token_id is not None:
            self.model.config.pad_token_id = self.tokenizer.pad_token_id

        train_args = TrainingArguments(
            output_dir=self.output_dir,
            learning_rate=self.learning_rate,
            per_device_train_batch_size=self.per_device_train_batch_size,
            gradient_accumulation_steps=self.gradient_accumulation_steps,
            num_train_epochs=self.num_train_epochs,
            weight_decay=self.weight_decay,
            save_strategy=self.save_strategy,
            save_total_limit=self.save_total_limit,
            logging_steps=self.logging_steps,
            dataloader_pin_memory = bool(torch.cuda.is_available()),
            fp16=self.fp16,
            bf16=self.bf16,
            report_to="none",
            save_safetensors=True,
        )

        trainer = Trainer(
            model=self.model,
            args=train_args,
            train_dataset=tokenized["train"],
            tokenizer=self.tokenizer,
            data_collator=collator,
        )
        trainer.train()
        trainer.save_model(self.output_dir)
        self.tokenizer.save_pretrained(self.output_dir)

    def _predict_pairs(self, eval_data: Any) -> List[Dict[str, str]]:
        import torch.nn.functional as F

        self._ensure_loaded_for_inference()

        candidate_pairs = self._extract_pairs_for_eval(eval_data)
        if not candidate_pairs:
            return []

        accepted: List[Dict[str, str]] = []
        scored_candidates: List[Tuple[float, str, str, int]] = []

        self.model.eval()
        with torch.no_grad():
            for parent_term, child_term in candidate_pairs:
                input_text = self._format_input(parent_term, child_term)
                inputs = self.tokenizer(input_text, return_tensors="pt", truncation=True, max_length=self.max_length)
                inputs = {k: v.to(self.device) for k, v in inputs.items()}
                logits = self.model(**inputs).logits
                probs = F.softmax(logits, dim=-1).squeeze(0)
                p_positive = float(probs[1].item())
                predicted_label = int(torch.argmax(logits, dim=-1).item())
                scored_candidates.append((p_positive, parent_term, child_term, predicted_label))
                if predicted_label == 1:
                    accepted.append({"parent": parent_term, "child": child_term})

        if accepted:
            return accepted

        top_k = max(0, int(self.min_predictions))
        if top_k == 0:
            return []
        scored_candidates.sort(key=lambda item: item[0], reverse=True)
        return [{"parent": parent_term, "child": child_term}
                for (_prob, parent_term, child_term, _pred) in scored_candidates[:top_k]]

    def _ensure_loaded_for_inference(self) -> None:
        if self.model is not None and self.tokenizer is not None:
            return
        self.model = AutoModelForSequenceClassification.from_pretrained(self.output_dir).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(self.output_dir)
        if self.tokenizer.pad_token_id is None and getattr(self.model.config, "pad_token_id", None) is not None:
            self.tokenizer.pad_token_id = self.model.config.pad_token_id

    def _load_context_map(self) -> None:
        """Build exact and fuzzy maps from {ontology_name}_processed.json."""
        if not (self.context_json_path):
            self._context_exact = {}
            self._context_rows = []
            return
        try:
            rows = json.load(open(self.context_json_path, "r", encoding="utf-8"))
            self._context_exact = {
                str(row.get("term", "")).strip().lower(): str(row.get("term_info", "")).strip()
                for row in rows
            }
            self._context_rows = [
                {"term": str(row.get("term", "")), "term_info": str(row.get("term_info", ""))}
                for row in rows
            ]
        except Exception:
            self._context_exact = {}
            self._context_rows = []

    def _lookup_context_info(self, raw_term: str) -> str:
        """
        Loose context lookup: split by commas, strip whitespace, case-insensitive
        substring match against any row['term']. Join hits with '.'.
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
        Read pairs from ontology_obj.type_taxonomies.taxonomies (or fallback to .taxonomies).
        Each item must provide 'parent' and 'child' attributes/keys.
        """
        type_taxonomies = getattr(ontology_obj, "type_taxonomies", None)
        items = getattr(type_taxonomies, "taxonomies", None) if type_taxonomies is not None else getattr(ontology_obj, "taxonomies", None)
        pairs: List[Tuple[str, str]] = []
        if items:
            for item in items:
                parent_term = getattr(item, "parent", None) if not isinstance(item, dict) else item.get("parent")
                child_term = getattr(item, "child", None) if not isinstance(item, dict) else item.get("child")
                if parent_term and child_term:
                    pairs.append((str(parent_term), str(child_term)))
        return pairs

    def _extract_pairs_for_eval(self, ontology_obj: Any) -> List[Tuple[str, str]]:
        candidate_pairs = getattr(ontology_obj, "pairs", None)
        if candidate_pairs:
            pairs: List[Tuple[str, str]] = []
            for item in candidate_pairs:
                parent_term = getattr(item, "parent", None) if not isinstance(item, dict) else item.get("parent")
                child_term = getattr(item, "child", None) if not isinstance(item, dict) else item.get("child")
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
        positive_set = set(positives)
        all_possible = {(parent_term, child_term) for parent_term in entities for child_term in entities if parent_term != child_term}
        negative_candidates = list(all_possible - positive_set)

        target_count = max(len(positive_set) * max(1, ratio), len(positive_set))
        sample_count = min(target_count, len(negative_candidates))
        return random.sample(negative_candidates, k=sample_count) if sample_count > 0 else []

    def _build_text_dataset(
        self,
        positives: List[Tuple[str, str]],
        negatives: List[Tuple[str, str]],
    ) -> Tuple[List[int], List[str]]:
        self._load_context_map()

        labels: List[int] = []
        input_texts: List[str] = []

        def add_example(parent_term: str, child_term: str, label_value: int) -> None:
            input_texts.append(self._format_input(parent_term, child_term))
            labels.append(label_value)
            if self.bidirectional_templates:
                input_texts.append(self._format_input(child_term, parent_term, reverse=True))
                labels.append(label_value)

        for parent_term, child_term in positives:
            add_example(parent_term, child_term, 1)
        for parent_term, child_term in negatives:
            add_example(parent_term, child_term, 0)

        return labels, input_texts

    def _format_input(self, parent_term: str, child_term: str, reverse: bool = False) -> str:
        relation_text = (
            f"{child_term} is a subclass / child / subtype / descendant class of {parent_term}"
            if reverse
            else f"{parent_term} is the superclass / parent / supertype / ancestor class of {child_term}"
        )

        parent_info = self._lookup_context_info(parent_term)
        child_info = self._lookup_context_info(child_term)
        if not parent_info and not child_info:
            return relation_text

        context_text = f"## Context. '{parent_term}': {parent_info} '{child_term}': {child_info}"
        return f"{relation_text} {context_text}"

    @staticmethod
    def _is_windows() -> bool:
        return (os.name == "nt") or (platform.system().lower() == "windows")

    @staticmethod
    def _default_gpt_inference_with_dataset(term: str, dataset_name: str) -> str:
        """
        Generate a plain-text description for `term`, tailored by `dataset_name`.
        Uses g4f if available; otherwise returns an empty string.
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
            raw_text = response.choices[0].message.content if response and response.choices else ""
        except Exception:
            raw_text = ""  # or some deterministic fallback

        # Clean up
        cleaned = re.sub(r"[\*\-\#]", "", raw_text)
        cleaned = re.sub(r"\n\s*\n", " ", cleaned)
        cleaned = cleaned.replace("\n", " ")
        cleaned = re.sub(r"\s{2,}", " ", cleaned)
        cleaned = re.sub(r"\[\[\d+\]\]\(https?://[^\)]+\)", "", cleaned)
        sentences = [sentence for sentence in cleaned.split(".") if "?" not in sentence]
        return ".".join(sentences).strip()

    @staticmethod
    def _clean_term_info(raw_text: str) -> str:
        """Normalize whitespace and remove link artifacts."""
        cleaned = re.sub(r"\[\[\d+\]\]\(https?://[^\)]+\)", "", str(raw_text))
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        return cleaned

    @classmethod
    def _merge_part_files(cls, dataset_name: str, merged_path: Path, part_paths: List[Path]) -> None:
        merged_rows: List[dict] = []
        for part_path in part_paths:
            try:
                if not part_path.is_file():
                    continue
                part_content = json.load(open(part_path, "r", encoding="utf-8"))
                if isinstance(part_content, list):
                    merged_rows.extend(part_content)
                elif isinstance(part_content, dict):
                    merged_rows.append(part_content)
            except Exception:
                continue

        removal_markers = list(cls._CONTEXT_REMOVALS) + [dataset_name]
        for row in merged_rows:
            term_info_raw = str(row.get("term_info", ""))
            kept_sentences: List[str] = []
            for sentence in term_info_raw.split("."):
                sentence_no_links = re.sub(r"\[\[\d+\]\]\(https?://[^\)]+\)", "", sentence)
                if any(marker in sentence_no_links for marker in removal_markers):
                    continue
                kept_sentences.append(sentence_no_links)
            row["term_info"] = cls._clean_term_info(".".join(kept_sentences))

        merged_path.parent.mkdir(parents=True, exist_ok=True)
        json.dump(merged_rows, open(merged_path, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

        # best-effort cleanup
        for part_path in part_paths:
            try:
                os.remove(part_path)
            except Exception:
                pass

    @staticmethod
    def _fill_bucket_threaded(bucket_rows: List[dict], output_path: Path, provider: Callable[[str], str]) -> None:
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
                bucket_rows[row_index]["term_info"] = provider(bucket_rows[row_index]["term"])
            except Exception:
                bucket_rows[row_index]["term_info"] = ""
            if row_index % 10 == 1:
                json.dump(bucket_rows[: row_index + 1], open(output_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

        json.dump(bucket_rows, open(output_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    @staticmethod
    def _fill_bucket_process(
        worker_id: int,
        bucket_rows: List[dict],
        output_path: Path,
        provider: Callable[[str], str],
        progress_map: "multiprocessing.managers.DictProxy",
    ) -> None:
        current_index = 0
        try:
            if output_path.is_file():
                existing_rows = json.load(open(output_path, "r", encoding="utf-8"))
                if isinstance(existing_rows, list) and existing_rows:
                    bucket_rows[: len(existing_rows)] = existing_rows
                    current_index = len(existing_rows)
        except Exception:
            pass

        progress_map[worker_id] = current_index

        for row_index in range(current_index, len(bucket_rows)):
            try:
                bucket_rows[row_index]["term_info"] = provider(bucket_rows[row_index]["term"])
            except Exception:
                bucket_rows[row_index]["term_info"] = ""
            progress_map[worker_id] = row_index + 1
            if row_index % 10 == 1:
                json.dump(bucket_rows[: row_index + 1], open(output_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

        json.dump(bucket_rows, open(output_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        progress_map[worker_id] = len(bucket_rows)

    @classmethod
    def _execute_for_terms(
        cls,
        terms: List[str],
        merged_path: Path,
        part_paths: List[Path],
        provider: Callable[[str], str],
        dataset_name: str,
        num_workers: int = 2,
    ) -> None:
        """
        Generate context for `terms`, writing shards to `part_paths`, then merge.
        Threads on Windows; processes on POSIX.
        """
        worker_count = max(1, min(num_workers, os.cpu_count() or 2, 4))
        all_rows = [{"id": row_index, "term": term, "term_info": ""} for row_index, term in enumerate(terms)]

        buckets: List[List[dict]] = [[] for _ in range(worker_count)]
        for reversed_index, row in enumerate(reversed(all_rows)):
            buckets[reversed_index % worker_count].append(row)

        if cls._is_windows():
            total_rows = len(terms)
            progress_bar = tqdm(total=total_rows, desc=f"{dataset_name} generation (threads)")

            def run_bucket(bucket_rows: List[dict], out_path: Path) -> int:
                cls._fill_bucket_threaded(bucket_rows, out_path, provider)
                return len(bucket_rows)

            with ThreadPoolExecutor(max_workers=worker_count) as pool:
                futures = [pool.submit(run_bucket, buckets[bucket_index], part_paths[bucket_index])
                           for bucket_index in range(worker_count)]
                for future in as_completed(futures):
                    completed_count = future.result()
                    if progress_bar:
                        progress_bar.update(completed_count)
            if progress_bar:
                progress_bar.close()
        else:
            manager = multiprocessing.Manager()
            progress_map = manager.dict({worker_index: 0 for worker_index in range(worker_count)})

            processes: List[multiprocessing.Process] = []
            for worker_index, bucket_rows in enumerate(buckets):
                process = multiprocessing.Process(
                    target=cls._fill_bucket_process,
                    args=(worker_index, bucket_rows, part_paths[worker_index], provider, progress_map),
                )
                processes.append(process)
                process.start()

            total_rows = len(terms)
            with tqdm(total=total_rows, desc=f"{dataset_name} generation") as progress_bar:
                previous_total = 0
                while any(process.is_alive() for process in processes):
                    current_total = int(sum(progress_map.values()))
                    progress_bar.update(current_total - previous_total)
                    previous_total = current_total
                    time.sleep(0.5)
                current_total = int(sum(progress_map.values()))
                if current_total > previous_total:
                    progress_bar.update(current_total - previous_total)

            for process in processes:
                process.join()

        cls._merge_part_files(dataset_name, merged_path, part_paths)

    @classmethod
    def _re_infer_short_entries(
        cls,
        merged_path: Path,
        re_part_paths: List[Path],
        re_merged_path: Path,
        provider: Callable[[str], str],
        dataset_name: str,
        num_workers: int,
    ) -> int:
        """
        Re-query terms with too-short term_info (< 50 chars). Returns remaining count.
        """
        merged_rows = json.load(open(merged_path, "r", encoding="utf-8"))

        removal_markers = list(cls._CONTEXT_REMOVALS) + [dataset_name]
        short_rows: List[dict] = []
        long_rows: List[dict] = []

        for row in merged_rows:
            term_info_raw = str(row.get("term_info", ""))
            sentences = term_info_raw.split(".")
            for marker in removal_markers:
                sentences = [sentence if marker not in sentence else "" for sentence in sentences]
            filtered_info = re.sub(r"\[\[\d+\]\]\(https?://[^\)]+\)", "", ".".join(sentences))
            row["term_info"] = filtered_info
            (short_rows if len(filtered_info) < 50 else long_rows).append(row)

        worker_count = max(1, min(num_workers, os.cpu_count() or 2, 4))
        buckets: List[List[dict]] = [[] for _ in range(worker_count)]
        for row_index, row in enumerate(short_rows):
            buckets[row_index % worker_count].append(row)

        # clean old re-inference shards
        for path in re_part_paths:
            try:
                os.remove(path)
            except Exception:
                pass

        total_candidates = len(short_rows)
        if cls._is_windows():
            progress_bar = tqdm(total=total_candidates, desc=f"{dataset_name} re-inference (threads)")

            def run_bucket(bucket_rows: List[dict], out_path: Path) -> int:
                cls._fill_bucket_threaded(bucket_rows, out_path, provider)
                return len(bucket_rows)

            with ThreadPoolExecutor(max_workers=worker_count) as pool:
                futures = [pool.submit(run_bucket, buckets[bucket_index], re_part_paths[bucket_index])
                           for bucket_index in range(worker_count)]
                for future in as_completed(futures):
                    completed_count = future.result()
                    if progress_bar:
                        progress_bar.update(completed_count)
            if progress_bar:
                progress_bar.close()
        else:
            manager = multiprocessing.Manager()
            progress_map = manager.dict({worker_index: 0 for worker_index in range(worker_count)})

            processes: List[multiprocessing.Process] = []
            for worker_index, bucket_rows in enumerate(buckets):
                process = multiprocessing.Process(
                    target=cls._fill_bucket_process,
                    args=(worker_index, bucket_rows, re_part_paths[worker_index], provider, progress_map),
                )
                processes.append(process)
                process.start()

            with tqdm(total=total_candidates, desc=f"{dataset_name} re-inference") as progress_bar:
                previous_total = 0
                while any(process.is_alive() for process in processes):
                    current_total = int(sum(progress_map.values()))
                    progress_bar.update(current_total - previous_total)
                    previous_total = current_total
                    time.sleep(1)
                if progress_bar.n < total_candidates:
                    progress_bar.update(total_candidates - progress_bar.n)

            for process in processes:
                process.join()

        # merge and write back
        cls._merge_part_files(dataset_name, re_merged_path, re_part_paths)
        new_rows = json.load(open(re_merged_path, "r", encoding="utf-8")) if re_merged_path.is_file() else []
        final_rows = long_rows + new_rows
        json.dump(final_rows, open(merged_path, "w", encoding="utf-8"), ensure_ascii=False, indent=4)

        remaining_short = sum(1 for row in final_rows if len(str(row.get("term_info", ""))) < 50)
        return remaining_short

    @staticmethod
    def _extract_terms_from_ontology(ontology: Any) -> List[str]:
        """
        Collect unique term names from ontology.type_taxonomies.taxonomies.
        """
        type_taxonomies = getattr(ontology, "type_taxonomies", None)
        taxonomies = getattr(type_taxonomies, "taxonomies", None) if type_taxonomies is not None else getattr(ontology, "taxonomies", None)
        unique_terms: set[str] = set()
        if taxonomies:
            for row in taxonomies:
                parent_term = getattr(row, "parent", None) if not isinstance(row, dict) else row.get("parent")
                child_term = getattr(row, "child", None) if not isinstance(row, dict) else row.get("child")
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
        Build {id, term, term_info} from an ontology object.
        Always regenerates {dataset_name}_processed.json.
        """
        provider = provider or provider or partial(self._default_gpt_inference_with_dataset, dataset_name=dataset_name)

        processed_dir = Path(processed_dir)
        processed_dir.mkdir(parents=True, exist_ok=True)

        merged_path = processed_dir / f"{dataset_name}_processed.json"
        if merged_path.exists():
            try:
                merged_path.unlink()
            except Exception:
                pass

        worker_count = max(1, min(num_workers, os.cpu_count() or 2, 4))
        shard_paths = [processed_dir / f"{dataset_name}_type_part{shard_index}.json" for shard_index in range(worker_count)]
        reinf_paths = [processed_dir / f"{dataset_name}_re_inference{shard_index}.json" for shard_index in range(worker_count)]
        reinf_merged_path = processed_dir / f"{dataset_name}_Types_re_inference.json"

        # remove any leftover shards
        for path in shard_paths + reinf_paths + [reinf_merged_path]:
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
            part_paths=shard_paths,
            provider=provider,
            dataset_name=dataset_name,
            num_workers=worker_count,
        )

        retry_round = 0
        while retry_round < max_retries:
            remaining_count = self._re_infer_short_entries(
                merged_path=merged_path,
                re_part_paths=reinf_paths,
                re_merged_path=reinf_merged_path,
                provider=provider,
                dataset_name=dataset_name,
                num_workers=worker_count,
            )
            print(f"[Preprocess] Re-infer round {retry_round + 1} done. Remaining short entries: {remaining_count}")
            retry_round += 1
            if remaining_count == 0:
                break

        print(f"[Preprocess] Done. Merged context at: {merged_path}")
        self.context_json_path = str(merged_path)
        return merged_path
