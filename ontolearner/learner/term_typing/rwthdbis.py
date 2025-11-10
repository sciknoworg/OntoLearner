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

        self.device = device
        self.model: Optional[AutoModelForSequenceClassification] = None
        self.tokenizer: Optional[AutoTokenizer] = None
        self.id2label: Dict[int, str] = {}
        self.label2id: Dict[str, int] = {}

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
            self._train_from_term_typings(train_data=data)
            return None

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

    def _train_from_term_typings(self, train_data: Any) -> None:
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
        if term_typings is None:
            raise ValueError("train_data must provide .term_typings for term-typing.")

        texts, label_ids, self.id2label, self.label2id = (
            self._expand_multilabel_training_rows(term_typings)
        )

        dataset = DatasetDict(
            {"train": Dataset.from_dict({"labels": label_ids, "text": texts})}
        )

        backbone = self.trained_model_path or self.model_name
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(backbone, use_fast=True)
        except Exception:
            # fallback if fast tokenizer isn't available
            self.tokenizer = AutoTokenizer.from_pretrained(backbone, use_fast=False)

        def tokenize_batch(batch: Dict[str, List[str]]):
            """Tokenize a batch of texts with truncation and max length."""
            return self.tokenizer(
                batch["text"], truncation=True, max_length=self.max_length
            )

        tokenized = dataset.map(tokenize_batch, batched=True, remove_columns=["text"])
        data_collator = DataCollatorWithPadding(self.tokenizer)

        self.model = AutoModelForSequenceClassification.from_pretrained(
            backbone,
            num_labels=len(self.id2label),
            id2label=self.id2label,
            label2id=self.label2id,
        )

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
            inputs = {name: tensor.to(self.device) for name, tensor in inputs.items()}
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
