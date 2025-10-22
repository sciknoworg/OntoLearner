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
from typing import Any, Dict, List, Optional, Tuple

import torch
from datasets import Dataset, DatasetDict
from tqdm.auto import tqdm
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
    set_seed,
)
from transformers import DebertaV2Tokenizer

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
        seed: int = 42
    ) -> None:
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

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model: Optional[AutoModelForSequenceClassification] = None
        self.tokenizer: Optional[AutoTokenizer] = None
        self.id2label: Dict[int, str] = {}
        self.label2id: Dict[str, int] = {}

    def _term_typing(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        train: expects ontology-like object with .term_typings
        test:  returns List[{"term": str, "types": [str]}] (for evaluator)
        """
        if not test:
            return self._train_from_term_typings(train_data=data)

        terms = self._collect_eval_terms(data)
        return self._predict_structured_output(terms)

    def _load_robust_tokenizer(self, backbone: str) -> AutoTokenizer:
        try:
            return AutoTokenizer.from_pretrained(backbone, use_fast=True)
        except Exception as fast_err:
            print(f"[tokenizer] Fast tokenizer failed: {fast_err}. Trying DebertaV2Tokenizer (slow)...")

        try:
            return DebertaV2Tokenizer.from_pretrained(backbone)
        except Exception as slow_err:
            print(f"[tokenizer] DebertaV2Tokenizer failed: {slow_err}. Trying AutoTokenizer(use_fast=False)...")

        try:
            return AutoTokenizer.from_pretrained(backbone, use_fast=False)
        except Exception as final_err:
            raise RuntimeError(
                "Failed to load a tokenizer for this DeBERTa model.\n"
                "Try:\n"
                "  - pip install --upgrade sentencepiece\n"
                "  - ensure network access for model files\n"
                "  - clear your HF cache and retry\n"
                "  - pin versions: transformers==4.43.*, tokenizers<0.20\n"
                f"Original error: {final_err}"
            )

    def _expand_multilabel_training_rows(
        self, term_typings: List[Any]
    ) -> Tuple[List[str], List[int], Dict[int, str], Dict[str, int]]:
        """
        From multi-label instances -> (texts, label_ids), and label maps.
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
        Accepts List[str] OR object with .term_typings; returns list of term texts.
        """
        if isinstance(eval_data, list) and all(isinstance(x, str) for x in eval_data):
            terms = eval_data
        else:
            term_typings = getattr(eval_data, "term_typings", None)
            if term_typings is None:
                raise ValueError("Provide a List[str] OR an object with .term_typings for test=True.")
            terms = [str(instance.term) for instance in term_typings]
        return terms

    def _train_from_term_typings(self, train_data: Any) -> None:
        set_seed(self.seed)
        random.seed(self.seed)
        torch.manual_seed(self.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.seed)

        term_typings: List[Any] = getattr(train_data, "term_typings", None)
        if term_typings is None:
            raise ValueError("train_data must provide .term_typings for term-typing.")

        texts, label_ids, self.id2label, self.label2id = self._expand_multilabel_training_rows(term_typings)

        dataset = DatasetDict({"train": Dataset.from_dict({"labels": label_ids, "text": texts})})

        backbone = self.trained_model_path or self.model_name
        self.tokenizer = self._load_robust_tokenizer(backbone)

        def tokenize_batch(batch: Dict[str, List[str]]):
            return self.tokenizer(batch["text"], truncation=True, max_length=self.max_length)

        tokenized = dataset.map(tokenize_batch, batched=True, remove_columns=["text"])
        data_collator = DataCollatorWithPadding(self.tokenizer)

        self.model = AutoModelForSequenceClassification.from_pretrained(
            backbone,
            num_labels=len(self.id2label),
            id2label=self.id2label,
            label2id=self.label2id,
        )

        if getattr(self.model.config, "pad_token_id", None) is None and self.tokenizer.pad_token_id is not None:
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
        if self.model is not None and self.tokenizer is not None:
            return
        model_path = self.trained_model_path or self.output_dir
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = self._load_robust_tokenizer(model_path)

        cfg = self.model.config
        if hasattr(cfg, "id2label") and hasattr(cfg, "label2id"):
            self.id2label = dict(cfg.id2label)
            self.label2id = dict(cfg.label2id)

        self.model.to(self.device).eval()

    def _predict_label_ids(self, terms: List[str]) -> List[int]:
        self._ensure_loaded_for_inference()
        predictions: List[int] = []
        for term_text in tqdm(terms, desc="Inference", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}"):
            inputs = self.tokenizer(term_text, return_tensors="pt", truncation=True, max_length=self.max_length)
            inputs = {name: tensor.to(self.device) for name, tensor in inputs.items()}
            with torch.no_grad():
                logits = self.model(**inputs).logits
                predictions.append(int(torch.argmax(logits, dim=-1).item()))
        return predictions

    def _predict_structured_output(self, terms: List[str]) -> List[Dict[str, List[str]]]:
        """
        Convert predicted IDs into evaluator format:
        [{"term": "<text>", "types": ["<label_str>"]}, ...]
        """
        label_ids = self._predict_label_ids(terms)
        id2label_map = self.id2label or {}  # fallback handled below

        results: List[Dict[str, List[str]]] = []
        for term_text, label_id in zip(terms, label_ids):
            label_str = id2label_map.get(int(label_id), str(int(label_id)))
            results.append({"term": term_text, "types": [label_str]})
        return results
