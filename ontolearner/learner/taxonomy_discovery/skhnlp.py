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
import random

import pandas as pd
import torch
import Levenshtein
from datasets import Dataset
from typing import Any, Optional, List, Tuple, Dict
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    AutoModelForCausalLM,
    BertTokenizer,
    BertForSequenceClassification,
    pipeline,
    Trainer,
    TrainingArguments,
)

from ...base import AutoLearner, AutoPrompt
from ...utils import taxonomy_split, train_test_split as ontology_split
from ...data_structure import OntologyData, TaxonomicRelation


class SKHNLPTaxonomyPrompts(AutoPrompt):
    """Builds the 7 taxonomy prompts used during fine-tuning / inference.

    The class stores a small inventory of prompt templates that verbalize the
    (parent, child) relationship using different phrasings. Each template ends
    with a masked token slot intended for True/False classification.
    """

    def __init__(self) -> None:
        """Initialize prompt templates and the default prompt in the base class."""
        super().__init__(
            prompt_template="{parent} is the superclass of {child}. This statement is [MASK]."
        )
        self.templates: List[str] = [
            "{parent} is the superclass of {child}. This statement is [MASK].",
            "{child} is a subclass of {parent}. This statement is [MASK].",
            "{parent} is the parent class of {child}. This statement is [MASK].",
            "{child} is a child class of {parent}. This statement is [MASK].",
            "{parent} is a supertype of {child}. This statement is [MASK].",
            "{child} is a subtype of {parent}. This statement is [MASK].",
            "{parent} is an ancestor class of {child}. This statement is [MASK].",
        ]

    def format(self, parent: str, child: str, template_idx: int) -> str:
        """Render a prompt for a (parent, child) pair using a specific template.

        Args:
            parent: The parent/superclass label.
            child: The child/subclass label.
            template_idx: Index into the internal `templates` list.

        Returns:
            The fully formatted prompt string.
        """
        return self.templates[template_idx].format(parent=parent, child=child)


class SKHNLPSequentialFTLearner(AutoLearner):
    """
    BERT-based classifier for taxonomy discovery.

    With OntologyData:
      * TRAIN: ontology-aware split; create balanced train/eval with negatives.
      * PREDICT/TEST: notebook-style parent selection -> list[{'parent', 'child'}].

    With DataFrame/list:
      * TRAIN: taxonomy_split + negatives; build prompts and fine-tune.
      * PREDICT/TEST: pairwise binary classification (returns label + score).
    """

    def __init__(
        self,
        # core
        model_name: str = "bert-large-uncased",
        n_prompts: int = 7,
        random_state: int = 1403,
        num_labels: int = 2,
        device: str = "cpu",  # "cuda" | "cpu" | None (auto)
        # data split & negative sampling (now configurable)
        eval_fraction: float = 0.16,
        neg_ratio_reversed: float = 1 / 3,
        neg_ratio_manipulated: float = 2 / 3,
        # ---- expose TrainingArguments as individual user-defined args ----
        output_dir: str = "./results/",
        num_train_epochs: int = 1,
        per_device_train_batch_size: int = 4,
        per_device_eval_batch_size: int = 4,
        warmup_steps: int = 500,
        weight_decay: float = 0.01,
        logging_dir: str = "./logs/",
        logging_steps: int = 50,
        eval_strategy: str = "epoch",
        save_strategy: str = "epoch",
        load_best_model_at_end: bool = True,
        use_fast_tokenizer: Optional[bool] = None,
        trust_remote_code: bool = False,
    ) -> None:
        """Configure the sequential fine-tuning learner.

        Args:
            model_name: HF model id or local path for the BERT backbone.
            n_prompts: Number of prompt variants to iterate over sequentially.
            random_state: RNG seed for shuffling/sampling steps.
            num_labels: Number of classes for the classifier head.
            device: Force device ('cuda' or 'cpu'). If None, auto-detects CUDA.
            eval_fraction: Fraction of positives to hold out for evaluation.
            neg_ratio_reversed: Proportion of reversed-parent negatives vs positives.
            neg_ratio_manipulated: Proportion of random-parent negatives vs positives.
            output_dir: Directory where HF Trainer writes checkpoints/outputs.
            num_train_epochs: Number of epochs per prompt.
            per_device_train_batch_size: Training batch size per device.
            per_device_eval_batch_size: Evaluation batch size per device.
            warmup_steps: Linear warmup steps for LR scheduler.
            weight_decay: Weight decay coefficient.
            logging_dir: Directory for Trainer logs.
            logging_steps: Interval for log events (in steps).
            eval_strategy: Evaluation schedule ('no', 'steps', 'epoch').
            save_strategy: Checkpoint save schedule ('no', 'steps', 'epoch').
            load_best_model_at_end: Whether to restore the best checkpoint.
            use_fast_tokenizer: Force fast/slow tokenizer. If None, try fast then fallback to slow.
        Notes:
            The model is fine-tuned *sequentially* across prompt columns.
            You can control the eval split and negative sampling mix via
            `eval_fraction`, `neg_ratio_reversed`, and `neg_ratio_manipulated`.
        """
        super().__init__()
        self.model_name = model_name
        self.n_prompts = n_prompts
        self.random_state = random_state
        self.num_labels = num_labels
        self.device = device

        # user-tunable ratios / split
        self._eval_fraction = float(eval_fraction)
        self._neg_ratio_reversed = float(neg_ratio_reversed)
        self._neg_ratio_manipulated = float(neg_ratio_manipulated)
        if not (0.0 < self._eval_fraction < 1.0):
            raise ValueError("eval_fraction must be in (0, 1).")
        if self._neg_ratio_reversed < 0 or self._neg_ratio_manipulated < 0:
            raise ValueError("neg_ratio_* must be >= 0.")

        self.tokenizer: Optional[BertTokenizer] = None
        self.model: Optional[BertForSequenceClassification] = None
        self.prompter = SKHNLPTaxonomyPrompts()

        # Candidate parents (unique parent list) for multi-class parent selection.
        self._candidate_parents: Optional[List[str]] = None

        # Keep last train/eval tables for inspection
        self._last_train: Optional[pd.DataFrame] = None
        self._last_eval: Optional[pd.DataFrame] = None
        self.trust_remote_code = bool(trust_remote_code)
        self.use_fast_tokenizer = use_fast_tokenizer

        random.seed(self.random_state)

        # Build TrainingArguments from the individual user-defined values
        self.training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=num_train_epochs,
            per_device_train_batch_size=per_device_train_batch_size,
            per_device_eval_batch_size=per_device_eval_batch_size,
            warmup_steps=warmup_steps,
            weight_decay=weight_decay,
            logging_dir=logging_dir,
            logging_steps=logging_steps,
            eval_strategy=eval_strategy,
            save_strategy=save_strategy,
            load_best_model_at_end=load_best_model_at_end,
        )

    def load(self, model_id: Optional[str] = None, **_: Any) -> None:
        """Load tokenizer & model in a backbone-agnostic way; move model to self.device."""
        model_id = model_id or self.model_name

        # ---- Tokenizer (robust fast→slow fallback unless explicitly set) ----
        if self.use_fast_tokenizer is None:
            try:
                self.tokenizer = AutoTokenizer.from_pretrained(
                    model_id, use_fast=True, trust_remote_code=self.trust_remote_code
                )
            except Exception as fast_err:
                print(
                    f"[tokenizer] Fast tokenizer failed: {fast_err}. Falling back to slow tokenizer..."
                )
                self.tokenizer = AutoTokenizer.from_pretrained(
                    model_id, use_fast=False, trust_remote_code=self.trust_remote_code
                )
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_id,
                use_fast=self.use_fast_tokenizer,
                trust_remote_code=self.trust_remote_code,
            )

        # Ensure pad token exists (some models lack it)
        if getattr(self.tokenizer, "pad_token", None) is None:
            # Try sensible fallbacks
            fallback = (
                getattr(self.tokenizer, "eos_token", None)
                or getattr(self.tokenizer, "sep_token", None)
                or getattr(self.tokenizer, "cls_token", None)
            )
            if fallback is not None:
                self.tokenizer.pad_token = fallback

        # ---- Model (classifier head sized to self.num_labels) ----
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_id,
            num_labels=self.num_labels,
            trust_remote_code=self.trust_remote_code,
            # Allows swapping in a new head size even if the checkpoint differs
            ignore_mismatched_sizes=True,
        )

        # Make sure padding ids line up
        if (
            getattr(self.model.config, "pad_token_id", None) is None
            and getattr(self.tokenizer, "pad_token_id", None) is not None
        ):
            self.model.config.pad_token_id = self.tokenizer.pad_token_id

        # Set problem type (single-label classification by default)
        # If you plan multi-label, you'd switch to "multi_label_classification"
        self.model.config.problem_type = "single_label_classification"

        # Move to target device
        self.model.to(self.device)

    def tasks_ground_truth_former(self, data: Any, task: str) -> Any:
        """Normalize ground-truth inputs for 'taxonomy-discovery'.

        Supports DataFrame with columns ['parent','child',('label')],
        list of dicts, or falls back to the base class behavior.

        Args:
            data: Input object to normalize.
            task: Task name, passed from the outer pipeline.

        Returns:
            A list of dictionaries with keys 'parent', 'child', and optionally
            'label' when present in the input.
        """
        if task != "taxonomy-discovery":
            return super().tasks_ground_truth_former(data, task)

        if isinstance(data, pd.DataFrame):
            if "label" in data.columns:
                return [
                    {"parent": p, "child": c, "label": bool(lbl)}
                    for p, c, lbl in zip(data["parent"], data["child"], data["label"])
                ]
            return [
                {"parent": p, "child": c} for p, c in zip(data["parent"], data["child"])
            ]

        if isinstance(data, list):
            return data

        return super().tasks_ground_truth_former(data, task)

    def _make_negatives(
        self, positives_df: pd.DataFrame
    ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Create two types of negatives from a positives table.

        Returns:
            A tuple `(reversed_df, manipulated_df)` where:
                - `reversed_df`: pairs with parent/child columns swapped, label=False.
                - `manipulated_df`: pairs with the parent replaced by a random
                  *different* parent from the same pool, label=False.

        Notes:
            The input DataFrame must contain columns ['parent', 'child'].
        """
        unique_parents = positives_df["parent"].unique().tolist()

        def as_reversed(df: pd.DataFrame) -> pd.DataFrame:
            out = df.copy()
            out[["parent", "child"]] = out[["child", "parent"]].values
            out["label"] = False
            return out

        def with_random_parent(df: pd.DataFrame) -> pd.DataFrame:
            def pick_other_parent(p: str) -> str:
                pool = [x for x in unique_parents if x != p]
                return random.choice(pool) if pool else p

            out = df.copy()
            out["parent"] = out["parent"].apply(pick_other_parent)
            out["label"] = False
            return out

        return as_reversed(positives_df), with_random_parent(positives_df)

    def _balance_with_negatives(
        self,
        positives_df: pd.DataFrame,
        reversed_df: pd.DataFrame,
        manipulated_df: pd.DataFrame,
    ) -> pd.DataFrame:
        """Combine positives with negatives using configured ratios.

        Sampling ratios are defined by the instance settings
        `self._neg_ratio_reversed` and `self._neg_ratio_manipulated`,
        keeping the positives count unchanged.

        Args:
            positives_df: Positive pairs with `label=True`.
            reversed_df: Negative pairs produced by flipping parent/child.
            manipulated_df: Negative pairs with randomly reassigned parents.

        Returns:
            A deduplicated, shuffled DataFrame with a class-balanced mix.
        """
        n_pos = len(positives_df)
        n_rev = int(n_pos * self._neg_ratio_reversed)
        n_man = int(n_pos * self._neg_ratio_manipulated)

        combined = pd.concat(
            [
                positives_df.sample(n_pos, random_state=self.random_state),
                reversed_df.sample(n_rev, random_state=self.random_state),
                manipulated_df.sample(n_man, random_state=self.random_state),
            ],
            ignore_index=True,
        )
        combined = combined.drop_duplicates(
            subset=["parent", "child", "label"]
        ).reset_index(drop=True)
        return combined

    def _add_prompt_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Append one column per prompt variant to the given pairs table.

        For each row `(parent, child)`, creates columns `prompt_1 ... prompt_n`.

        Args:
            df: Input DataFrame with columns ['parent', 'child', ...].

        Returns:
            A copy of `df` including the newly added prompt columns.
        """
        out = df.copy()
        for i in range(self.n_prompts):
            out[f"prompt_{i + 1}"] = out.apply(
                lambda r, k=i: self.prompter.format(r["parent"], r["child"], k), axis=1
            )
        return out

    def _df_from_relations(
        self, relations: List[TaxonomicRelation], label: bool = True
    ) -> pd.DataFrame:
        """Convert a list of `TaxonomicRelation` to a DataFrame.

        Args:
            relations: Iterable of `TaxonomicRelation(parent, child)`.
            label: Class label to assign to all resulting rows.

        Returns:
            DataFrame with columns ['parent', 'child', 'label'].
        """
        if not relations:
            return pd.DataFrame(columns=["parent", "child", "label"])
        return pd.DataFrame(
            [{"parent": r.parent, "child": r.child, "label": label} for r in relations]
        )

    def _relations_from_df(self, df: pd.DataFrame) -> List[TaxonomicRelation]:
        """Convert a DataFrame to a list of `TaxonomicRelation`.

        Args:
            df: DataFrame with columns ['parent', 'child'].

        Returns:
            List of `TaxonomicRelation` objects in row order.
        """
        return [
            TaxonomicRelation(parent=p, child=c)
            for p, c in zip(df["parent"], df["child"])
        ]

    def _build_masked_prompt(
        self, parent: str, child: str, index_1_based: int, mask_token: str = "[MASK]"
    ) -> str:
        """Construct one of several True/False prompts with a mask token.

        Args:
            parent: Parent label.
            child: Child label.
            index_1_based: 1-based index selecting a template.
            mask_token: The token used to denote the masked label.

        Returns:
            A formatted prompt string.
        """
        prompts_1based = [
            f"{parent} is the superclass of {child}. This statement is {mask_token}.",
            f"{child} is a subclass of {parent}. This statement is {mask_token}.",
            f"{parent} is the parent class of {child}. This statement is {mask_token}.",
            f"{child} is a child class of {parent}. This statement is {mask_token}.",
            f"{parent} is a supertype of {child}. This statement is {mask_token}.",
            f"{child} is a subtype of {parent}. This statement is {mask_token}.",
            f"{parent} is an ancestor class of {child}. This statement is {mask_token}.",
            f"{child} is a descendant classs of {child}. This statement is {mask_token}.",
            f'"{parent}" is the superclass of "{child}". This statement is {mask_token}.',
        ]
        return prompts_1based[index_1_based - 1]

    @torch.no_grad()
    def _predict_prompt_true_false(self, sentence: str) -> bool:
        """Run a single True/False prediction on a prompt.

        Args:
            sentence: Fully formatted prompt text.

        Returns:
            True iff the predicted class index is 1 (positive).
        """
        enc = self.tokenizer(sentence, return_tensors="pt").to(self.model.device)
        logits = self.model(**enc).logits
        predicted_label = torch.argmax(logits, dim=1).item()
        return predicted_label == 1

    def _select_parent_via_prompts(self, child: str) -> str:
        """Select the most likely parent for a given child via prompt voting.

        The procedure:
          1) Generate prompts for each candidate parent at increasing "levels".
          2) Accumulate votes from the True/False classifier.
          3) Resolve ties by recursing to the next level; after 4 levels, break ties randomly.

        Args:
            child: The child label whose parent should be predicted.

        Returns:
            The chosen parent string.

        Raises:
            AssertionError: If candidate parents were not initialized.
        """
        assert self._candidate_parents, "Candidate parents not initialized."
        scores: dict[str, int] = {p: 0 for p in self._candidate_parents}

        def prompt_indices_for_level(level: int) -> List[int]:
            if level == 0:
                return [1]
            return [2 * level, 2 * level + 1]

        def recurse(active_parents: List[str], level: int) -> str:
            idxs = [
                i for i in prompt_indices_for_level(level) if 1 <= i <= self.n_prompts
            ]
            if idxs:
                for parent in active_parents:
                    votes = sum(
                        1
                        for idx in idxs
                        if self._predict_prompt_true_false(
                            self._build_masked_prompt(
                                parent=parent, child=child, index_1_based=idx
                            )
                        )
                    )
                    scores[parent] += votes

            max_score = max(scores[p] for p in active_parents)
            tied = [p for p in active_parents if scores[p] == max_score]
            if len(tied) == 1:
                return tied[0]
            if level < 4:
                return recurse(tied, level + 1)
            return random.choice(tied)

        return recurse(list(scores.keys()), level=0)

    def _taxonomy_discovery(self, data: Any, test: bool = False):
        """
        TRAIN:
          - OntologyData -> ontology-aware split; negatives per split; balanced sets.
          - DataFrame/list -> taxonomy_split for positives; negatives proportional.
        TEST:
          - OntologyData -> parent selection: [{'parent': predicted, 'child': child}]
          - DataFrame/list -> binary pair classification with 'label' + 'score'

        Args:
            data: One of {OntologyData, pandas.DataFrame, list[dict], list[tuple]}.
            test: If True, run inference; otherwise perform training.

        Returns:
            - On training: None (model is fine-tuned in-place).
            - On inference with OntologyData: list of {'parent','child'} predictions.
            - On inference with pairs: list of dicts including 'label' and 'score'.
        """
        is_ontology_object = isinstance(data, OntologyData)

        # Normalize input
        if isinstance(data, pd.DataFrame):
            pairs_df = data.copy()
        elif isinstance(data, list):
            pairs_df = pd.DataFrame(data)
        else:
            gt_pairs = super().tasks_ground_truth_former(data, "taxonomy-discovery")
            pairs_df = pd.DataFrame(gt_pairs)
            if "label" not in pairs_df.columns:
                pairs_df["label"] = True

        # Maintain candidate parents across calls
        if "parent" in pairs_df.columns:
            parents_in_call = sorted(pd.unique(pairs_df["parent"]).tolist())
            if test:
                if self._candidate_parents is None:
                    self._candidate_parents = parents_in_call
                else:
                    self._candidate_parents = sorted(
                        set(self._candidate_parents).union(parents_in_call)
                    )
            else:
                if self._candidate_parents is None:
                    self._candidate_parents = parents_in_call

        if test:
            if is_ontology_object and self._candidate_parents:
                predictions: List[dict[str, str]] = []
                for _, row in pairs_df.iterrows():
                    child_term = row["child"]
                    chosen_parent = self._select_parent_via_prompts(child_term)
                    predictions.append({"parent": chosen_parent, "child": child_term})
                return predictions

            # pairwise binary classification
            prompts_df = self._add_prompt_columns(pairs_df.copy())
            true_probs_by_prompt: List[torch.Tensor] = []

            for i in range(self.n_prompts):
                col = f"prompt_{i + 1}"
                enc = self.tokenizer(
                    prompts_df[col].tolist(),
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                ).to(self.model.device)
                with torch.no_grad():
                    logits = self.model(**enc).logits
                    true_probs_by_prompt.append(torch.softmax(logits, dim=1)[:, 1])

            avg_true_prob = torch.stack(true_probs_by_prompt, dim=0).mean(0)
            predicted_bool = (avg_true_prob >= 0.5).cpu().tolist()

            results: List[dict[str, Any]] = []
            for p, c, s, yhat in zip(
                pairs_df["parent"],
                pairs_df["child"],
                avg_true_prob.tolist(),
                predicted_bool,
            ):
                results.append(
                    {
                        "parent": p,
                        "child": c,
                        "label": int(bool(yhat)),
                        "score": float(s),
                    }
                )
            return results

        if isinstance(data, OntologyData):
            train_onto, eval_onto = ontology_split(
                data,
                test_size=self._eval_fraction,
                random_state=self.random_state,
                verbose=False,
            )

            train_pos_rel: List[TaxonomicRelation] = (
                getattr(train_onto.type_taxonomies, "taxonomies", []) or []
            )
            eval_pos_rel: List[TaxonomicRelation] = (
                getattr(eval_onto.type_taxonomies, "taxonomies", []) or []
            )

            train_pos_df = self._df_from_relations(train_pos_rel, label=True)
            eval_pos_df = self._df_from_relations(eval_pos_rel, label=True)

            tr_rev_df, tr_man_df = self._make_negatives(train_pos_df)
            ev_rev_df, ev_man_df = self._make_negatives(eval_pos_df)

            train_df = self._balance_with_negatives(train_pos_df, tr_rev_df, tr_man_df)
            eval_df = self._balance_with_negatives(eval_pos_df, ev_rev_df, ev_man_df)

            train_df = self._add_prompt_columns(train_df)
            eval_df = self._add_prompt_columns(eval_df)

        else:
            if "label" not in pairs_df.columns or pairs_df["label"].nunique() == 1:
                positives_df = pairs_df[pairs_df.get("label", True)][
                    ["parent", "child"]
                ].copy()
                pos_rel = self._relations_from_df(positives_df)

                tr_rel, ev_rel = taxonomy_split(
                    pos_rel,
                    train_terms=None,
                    test_size=self._eval_fraction,
                    random_state=self.random_state,
                    verbose=False,
                )
                train_pos_df = self._df_from_relations(tr_rel, label=True)
                eval_pos_df = self._df_from_relations(ev_rel, label=True)

                tr_rev_df, tr_man_df = self._make_negatives(train_pos_df)
                ev_rev_df, ev_man_df = self._make_negatives(eval_pos_df)

                train_df = self._balance_with_negatives(
                    train_pos_df, tr_rev_df, tr_man_df
                )
                eval_df = self._balance_with_negatives(
                    eval_pos_df, ev_rev_df, ev_man_df
                )

                train_df = self._add_prompt_columns(train_df)
                eval_df = self._add_prompt_columns(eval_df)

            else:
                positives_df = pairs_df[pairs_df["label"]][["parent", "child"]].copy()
                pos_rel = self._relations_from_df(positives_df)

                tr_rel, ev_rel = taxonomy_split(
                    pos_rel,
                    train_terms=None,
                    test_size=self._eval_fraction,
                    random_state=self.random_state,
                    verbose=False,
                )
                train_pos_df = self._df_from_relations(tr_rel, label=True)
                eval_pos_df = self._df_from_relations(ev_rel, label=True)

                negatives_df = pairs_df[pairs_df["label"]][["parent", "child"]].copy()
                negatives_df = negatives_df.sample(
                    frac=1.0, random_state=self.random_state
                ).reset_index(drop=True)

                n_eval_neg = (
                    max(1, int(len(negatives_df) * self._eval_fraction))
                    if len(negatives_df) > 0
                    else 0
                )
                eval_neg_df = (
                    negatives_df.iloc[:n_eval_neg].copy()
                    if n_eval_neg > 0
                    else negatives_df.iloc[:0].copy()
                )
                train_neg_df = negatives_df.iloc[n_eval_neg:].copy()

                train_neg_df["label"] = False
                eval_neg_df["label"] = False

                train_df = pd.concat([train_pos_df, train_neg_df], ignore_index=True)
                eval_df = pd.concat([eval_pos_df, eval_neg_df], ignore_index=True)

                train_df = self._add_prompt_columns(train_df)
                eval_df = self._add_prompt_columns(eval_df)

        # Ensure labels are int64
        train_df["label"] = train_df["label"].astype("int64")
        eval_df["label"] = eval_df["label"].astype("int64")

        # Sequential fine-tuning across prompts
        for i in range(self.n_prompts):
            prompt_col = f"prompt_{i + 1}"
            train_ds = Dataset.from_pandas(
                train_df[[prompt_col, "label"]].reset_index(drop=True)
            )
            eval_ds = Dataset.from_pandas(
                eval_df[[prompt_col, "label"]].reset_index(drop=True)
            )

            train_ds = train_ds.rename_column("label", "labels")
            eval_ds = eval_ds.rename_column("label", "labels")

            def tokenize_batch(batch):
                """Tokenize a batch for the current prompt column with truncation/padding."""
                return self.tokenizer(
                    batch[prompt_col], padding="max_length", truncation=True
                )

            train_ds = train_ds.map(
                tokenize_batch, batched=True, remove_columns=[prompt_col]
            )
            eval_ds = eval_ds.map(
                tokenize_batch, batched=True, remove_columns=[prompt_col]
            )

            train_ds.set_format(
                type="torch", columns=["input_ids", "attention_mask", "labels"]
            )
            eval_ds.set_format(
                type="torch", columns=["input_ids", "attention_mask", "labels"]
            )

            trainer = Trainer(
                model=self.model,
                args=self.training_args,
                train_dataset=train_ds,
                eval_dataset=eval_ds,
            )
            trainer.train()

        self._last_train = train_df
        self._last_eval = eval_df
        return None


class SKHNLPZSLearner(AutoLearner):
    """
    Zero-shot taxonomy learner using an instruction-tuned causal LLM.

    Behavior
    --------
    - Builds a fixed classification prompt listing 9 GeoNames parent classes.
    - For each input row (child term), generates a short completion and parses
      the predicted class from a strict '#[ ... ]#' format.
    - Optionally normalizes the raw prediction to one of the valid 9 labels via:
        * "none"        : keep the parsed text as-is
        * "substring"   : snap to a label if either is a substring of the other
        * "levenshtein" : snap to the closest label by edit distance
        * "auto"        : substring, then Levenshtein if needed
    - Saves raw and normalized predictions to CSV if `save_path` is provided.

    Inputs the learner accepts (via `_to_dataframe`):
    - pandas.DataFrame with columns: ['child', 'parent'] or ['child', 'parent', 'label']
    - list[dict] with keys: 'child', 'parent' (and optionally 'label')
    - list of tuples/lists: (child, parent) or (child, parent, label)
    - OntoLearner-style object exposing .type_taxonomies.taxonomies iterable with (child, parent)
    """

    # Fixed class inventory (GeoNames parents)
    CLASS_LIST = [
        "city, village",
        "country, state, region",
        "forest, heath",
        "mountain, hill, rock",
        "parks, area",
        "road, railroad",
        "spot, building, farm",
        "stream, lake",
        "undersea",
    ]

    # Strict format: #[ ... ]#
    _PREDICTION_PATTERN = re.compile(r"#\[\s*([^\]]+?)\s*\]#")

    def __init__(
        self,
        model_name: str = "Qwen/Qwen2.5-0.5B-Instruct",
        device: Optional[str] = None,  # "cuda" | "cpu" | None (auto)
        max_new_tokens: int = 16,
        save_path: Optional[str] = None,  # directory or full path
        verbose: bool = True,
        normalize_mode: str = "none",  # "none" | "substring" | "levenshtein" | "auto"
        random_state: int = 1403,
    ) -> None:
        """Configure the zero-shot learner.

        Args:
            model_name: HF model id/path for the instruction-tuned causal LLM.
            device: Force device ('cuda' or 'cpu'), else auto-detect.
            max_new_tokens: Generation length budget for each completion.
            save_path: Optional CSV path or directory for saving predictions.
            verbose: If True, print progress messages.
            normalize_mode: Post-processing for class names
                ('none' | 'substring' | 'levenshtein' | 'auto').
            random_state: RNG seed for any sampling steps.
        """
        super().__init__()
        self.model_name = model_name
        self.verbose = verbose
        self.max_new_tokens = max_new_tokens
        self.save_path = save_path
        self.normalize_mode = (normalize_mode or "none").lower().strip()
        self.random_state = random_state

        random.seed(self.random_state)

        # Device: auto-detect CUDA if not specified
        if device is None:
            self._has_cuda = torch.cuda.is_available()
        else:
            self._has_cuda = device == "cuda"
        self._pipe_device = 0 if self._has_cuda else -1
        self._model_device_map = {"": "cuda"} if self._has_cuda else None

        self._tokenizer = None
        self._model = None
        self._pipeline = None

        # Prompt template used for every example
        self._classification_prompt = (
            "My task is classification. My classes are as follows: "
            "(city, village), (country, state, region), (forest, heath), "
            "(mountain, hill, rock), (parks, area), (road, railroad), "
            "(spot, building, farm), (stream, lake), (undersea). "
            'I will provide you with a phrase like "wadi mouth". '
            "The name of each class is placed within a pair of parentheses. "
            "I want you to choose the most appropriate class from those mentioned above "
            "based on the given phrase and present it in a format like #[parks, area]#. "
            "So, the general format for each response will be #[class name]#. "
            "Pay attention to the format of the response. Start with a '#' character, "
            "include the class name inside it, and end with another '#' character. "
            "Additionally, make sure to include a '#' character at the end to indicate "
            "that the answer is complete. I don't need any additional explanations."
        )

    def load(self, model_id: str = "") -> None:
        """
        Load tokenizer, model, and text-generation pipeline.

        Args:
            model_id: Optional HF id/path override; defaults to `self.model_name`.

        Side Effects:
            Initializes the tokenizer and model, configures the generation
            pipeline on CPU/GPU, and sets a pad token if absent.
        """
        model_id = model_id or self.model_name
        if self.verbose:
            print(f"[ZeroShotTaxonomyLearner] Loading {model_id}")

        self._tokenizer = AutoTokenizer.from_pretrained(model_id)

        # Ensure a pad token is set for generation
        if (
            self._tokenizer.pad_token_id is None
            and self._tokenizer.eos_token_id is not None
        ):
            self._tokenizer.pad_token = self._tokenizer.eos_token

        self._model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map=self._model_device_map,
            torch_dtype="auto",
        )

        self._pipeline = pipeline(
            task="text-generation",
            model=self._model,
            tokenizer=self._tokenizer,
            device=self._pipe_device,  # 0 for GPU, -1 for CPU
        )

        if self.verbose:
            print("Device set to use", "cuda" if self._has_cuda else "cpu")
            print("[ZeroShotTaxonomyLearner] Model loaded.")

    def _taxonomy_discovery(
        self, data: Any, test: bool = False
    ) -> Optional[List[Dict[str, str]]]:
        """
        Zero-shot prediction over all incoming rows (no filtering/augmentation).

        Args:
            data: One of {DataFrame, list[dict], list[tuple], Ontology-like}.
            test: If False, training is skipped (zero-shot learner), and None is returned.

        Returns:
            On `test=True`, a list of dicts [{'parent': predicted_label, 'child': child}, ...].
            On `test=False`, returns None.
        """
        if not test:
            if self.verbose:
                print("[ZeroShot] Training skipped (zero-shot).")
            return None

        df = self._to_dataframe(data)

        if self.verbose:
            print(f"[ZeroShot] Incoming rows: {len(df)}; columns: {list(df.columns)}")

        eval_df = pd.DataFrame(df).reset_index(drop=True)
        if eval_df.empty:
            return []

        # Prepare columns for inspection and saving
        eval_df["prediction_raw"] = ""
        eval_df["prediction_sub"] = ""
        eval_df["prediction_lvn"] = ""
        eval_df["prediction_auto"] = ""
        eval_df["prediction"] = ""  # final (per normalize_mode)

        # Generate predictions row by row
        for idx, row in eval_df.iterrows():
            child_term = str(row["child"])
            raw_text, parsed_raw = self._generate_and_parse(child_term)

            # Choose a string to normalize (parsed token if matched, otherwise whole output)
            basis = parsed_raw if parsed_raw != "unknown" else raw_text

            # Compute all normalization variants
            sub_norm = self._normalize_substring_only(basis)
            lvn_norm = self._normalize_levenshtein_only(basis)
            auto_norm = self._normalize_auto(basis)

            # Final selection by mode
            if self.normalize_mode == "none":
                final_label = parsed_raw
            elif self.normalize_mode == "substring":
                final_label = sub_norm
            elif self.normalize_mode == "levenshtein":
                final_label = lvn_norm
            elif self.normalize_mode == "auto":
                final_label = auto_norm
            else:
                final_label = parsed_raw  # fallback

            # Persist to DataFrame for inspection/export
            eval_df.at[idx, "prediction_raw"] = parsed_raw
            eval_df.at[idx, "prediction_sub"] = sub_norm
            eval_df.at[idx, "prediction_lvn"] = lvn_norm
            eval_df.at[idx, "prediction_auto"] = auto_norm
            eval_df.at[idx, "prediction"] = final_label

        # Return in the format expected by the pipeline
        return [
            {"parent": p, "child": c}
            for p, c in zip(eval_df["prediction"], eval_df["child"])
        ]

    def _generate_and_parse(self, child_term: str) -> (str, str):
        """
        Generate a completion for the given child term and extract the raw predicted class
        using the strict '#[ ... ]#' pattern.

        Args:
            child_term: The child label to classify into one of the fixed classes.

        Returns:
            Tuple `(raw_generation_text, parsed_prediction_or_unknown)`, where the second
            element is either the text inside '#[ ... ]#' or the string 'unknown'.
        """
        messages = [
            {"role": "system", "content": "You are a helpful classifier."},
            {"role": "user", "content": f"{self._classification_prompt} {child_term}"},
        ]

        prompt = self._tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
        )

        generation = self._pipeline(
            prompt,
            max_new_tokens=self.max_new_tokens,
            do_sample=False,
            temperature=0.0,
            top_p=1.0,
            eos_token_id=self._tokenizer.eos_token_id,
            pad_token_id=self._tokenizer.eos_token_id,
            return_full_text=False,
        )[0]["generated_text"]

        match = self._PREDICTION_PATTERN.search(generation)
        parsed = match.group(1).strip() if match else "unknown"
        return generation, parsed

    def _normalize_substring_only(self, text: str) -> str:
        """
        Snap to a label if the string is equal to / contained in / contains a valid label (case-insensitive).

        Args:
            text: Raw class text to normalize.

        Returns:
            One of `CLASS_LIST` on a match; otherwise 'unknown'.
        """
        if not isinstance(text, str):
            return "unknown"
        lowered = text.strip().lower()
        if not lowered:
            return "unknown"

        for label in self.CLASS_LIST:
            label_lower = label.lower()
            if (
                lowered == label_lower
                or lowered in label_lower
                or label_lower in lowered
            ):
                return label
        return "unknown"

    def _normalize_levenshtein_only(self, text: str) -> str:
        """
        Snap to the nearest label by Levenshtein (edit) distance.

        Args:
            text: Raw class text to normalize.

        Returns:
            The nearest label in `CLASS_LIST`, or 'unknown' if input is empty/invalid.
        """
        if not isinstance(text, str):
            return "unknown"
        lowered = text.strip().lower()
        if not lowered:
            return "unknown"

        best_label = None
        best_distance = 10**9
        for label in self.CLASS_LIST:
            label_lower = label.lower()
            distance = Levenshtein.distance(lowered, label_lower)
            if distance < best_distance:
                best_distance = distance
                best_label = label
        return best_label or "unknown"

    def _normalize_auto(self, text: str) -> str:
        """
        Cascade: try substring-first; if no match, fall back to Levenshtein snapping.

        Args:
            text: Raw class text to normalize.

        Returns:
            Normalized label string or 'unknown'.
        """
        snapped = self._normalize_substring_only(text)
        return (
            snapped if snapped != "unknown" else self._normalize_levenshtein_only(text)
        )

    def _to_dataframe(self, data: Any) -> pd.DataFrame:
        """
        Normalize various input formats into a DataFrame.

        Supported inputs:
            * pandas.DataFrame with columns ['child','parent',('label')]
            * list[dict] with keys 'child','parent',('label')
            * list of tuples/lists: (child, parent) or (child, parent, label)
            * Ontology-like object with `.type_taxonomies.taxonomies`

        Args:
            data: The source object to normalize.

        Returns:
            A pandas DataFrame with standardized columns.

        Raises:
            ValueError: If the input type/shape is not recognized.
        """
        if isinstance(data, pd.DataFrame):
            df = data.copy()
            df.columns = [str(c).lower() for c in df.columns]
            return df.reset_index(drop=True)

        if isinstance(data, list) and data and isinstance(data[0], dict):
            rows = [{str(k).lower(): v for k, v in d.items()} for d in data]
            return pd.DataFrame(rows).reset_index(drop=True)

        if isinstance(data, (list, tuple)) and data:
            first = data[0]
            if isinstance(first, (list, tuple)) and not isinstance(first, dict):
                n = len(first)
                if n >= 3:
                    return pd.DataFrame(
                        data, columns=["child", "parent", "label"]
                    ).reset_index(drop=True)
                if n == 2:
                    return pd.DataFrame(data, columns=["child", "parent"]).reset_index(
                        drop=True
                    )

        try:
            type_taxonomies = getattr(data, "type_taxonomies", None)
            if type_taxonomies is not None:
                taxonomies = getattr(type_taxonomies, "taxonomies", None)
                if taxonomies is not None:
                    rows = []
                    for rel in taxonomies:
                        parent = getattr(rel, "parent", None)
                        child = getattr(rel, "child", None)
                        label = (
                            getattr(rel, "label", None)
                            if hasattr(rel, "label")
                            else None
                        )
                        if parent is not None and child is not None:
                            rows.append(
                                {"child": child, "parent": parent, "label": label}
                            )
                    if rows:
                        return pd.DataFrame(rows).reset_index(drop=True)
        except Exception:
            pass

        raise ValueError(
            "Unsupported data format. Provide a DataFrame, a list of dicts, "
            "a list of (child, parent[, label]) tuples/lists, or an object with "
            ".type_taxonomies.taxonomies."
        )

    def _resolve_save_path(self, save_path: str, default_filename: str) -> str:
        """
        Resolve a target file path from a directory or path-like input.

        If `save_path` points to a directory, joins it with `default_filename`.
        If it already looks like a file path (has an extension), returns as-is.

        Args:
            save_path: Directory or file path supplied by the caller.
            default_filename: Basename to use when `save_path` is a directory.

        Returns:
            A concrete file path where outputs can be written.
        """
        base = os.path.basename(save_path)
        has_ext = os.path.splitext(base)[1] != ""
        return save_path if has_ext else os.path.join(save_path, default_filename)
