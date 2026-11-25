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

from __future__ import annotations

import hashlib
import json
import math
import re
import statistics
import time
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

from ...base import PrimitiveOntologyLearner


class BigDipperAIPrimitiveLearner(PrimitiveOntologyLearner):
    """
    Relation-weighted learner for primitive ontology construction.

    This learner uses supervised QLoRA fine-tuning, structured JSON generation,
    graph completion, and candidate fusion to extract ontology triples from text.
    Labeled expansion records can provide auxiliary training supervision.
    Setting train_adapter=False enables base-model inference for development
    without reproducing the fine-tuned model.
    """
    _system_prompt = 'Return only valid JSON for the ontology extraction task.'

    _construction_prompt = [
        "You are constructing a primitive ontology from raw text.",
        "Return only one valid JSON object and no commentary.",
        "Use exactly this key: primitive-ontology-triples.",
        "Each triple must be a 3-item array: [subject, relation, object].",
        "Use only the allowed relations.",
        "Preserve ontology entity spelling and punctuation when it is meaningful.",
        "Do not lowercase all entities.",
        "Create one triple per ontology edge; lists should be expanded into separate triples.",
        "Include taxonomy, instance typing, definition, equivalence, disjointness, and other primitive relations when supported.",
    ]

    _allowed_relations = [
        'is-a', 'instance-of', 'is defined by', 'equivalent class', 'disjoint with', 'type', 'exact match', 'tree view', 'part_of', 'has part', 'database_cross_reference', 'see also', 'same as', 'range', 'is_conjugate_base_of',
        'is_conjugate_acid_of', 'derives from', 'develops_from', 'broader', 'domain','located in', 'has role', 'term replaced by', 'positively regulates', 'regulates', 'overlaps', 'ro_0002473', 'ro_0002220',
    ]

    _bad_entity_keys = {
        'a', 'an', 'and', 'are', 'as', 'be', 'by', 'for', 'from', 'group', 'groups', 'he', 'her', 'his', 'in', 'including', 'is', 'it', 'its', 'la', 'of', 'or', 'she', 'that', 'the', 'their', 'them', 'these', 'they',
        'this', 'those', 'type', 'value', 'category', 'categories', 'class', 'classes', 'system', 'systems', 'taxonomy', 'taxonomies', 'domain', 'domains', 'field', 'fields', 'method', 'methods','was', 'were', 'which',
        'who', 'whose', 'with', 'within',
    }

    _fusion_bad_entities = {
        'a', 'an', 'the', 'this', 'that', 'these', 'those', 'which', 'which itself', 'it', 'its', 'they', 'them', 'one', 'role', 'order', 'realm', 'key', 'structural', 'composition', 'category', 'categories',
        'class', 'classes', 'group', 'groups', 'system', 'systems',
    }

    _boundary_words = (
        'the', 'a', 'an', 'this', 'that', 'these', 'those', 'where', 'when', 'while', 'as', 'in', 'within', 'across', 'among', 'for', 'to', 'of', 'by', 'with', 'including', 'include', 'includes', 'contains',
        'contain', 'encompasses', 'encompass',
    )

    _source_weights = {'sft': 1.0, 'graph_completion': 0.92}

    _source_min_scores = {'sft': 0.5, 'graph_completion': 0.86}

    _relation_min_scores = {'default': 0.95, 'disjoint with': 0.9, 'equivalent class': 0.9, 'instance-of': 0.7, 'is defined by': 0.84, 'is-a': 0.5, 'type': 0.9}

    _relation_caps = {'default': 4, 'disjoint with': 2, 'equivalent class': 2, 'has part': 4, 'instance-of': 32, 'is defined by': 4, 'is-a': 32, 'part_of': 4, 'see also': 4, 'type': 2}

    _relation_weights = {'instance-of': 3.0, 'type': 3.0, 'default': 1.0}

    _target_modules = ['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj']

    Triple = Tuple[str, str, str]

    def __init__(
        self,
        model_id: str = "Qwen/Qwen3-8B",
        auxiliary_data: Optional[Sequence[Dict[str, Any]]] = None,
        device: str = "cuda",
        train_adapter: bool = True,
        adapter_path: Optional[str] = None,
        output_dir: str = "./results/bigdipperai",
        local_files_only: bool = False,
        max_input_tokens: int = 3072,
        max_output_tokens: int = 1536,
        retry_output_tokens: int = 3072,
        max_train_samples: Optional[int] = None,
        max_eval_samples: Optional[int] = None,
        max_steps: Optional[int] = None,
        *,
        system_prompt: Optional[str] = None,
        construction_prompt: Optional[Sequence[str]] = None,
        allowed_relations: Optional[Sequence[str]] = None,
        bad_entity_keys: Optional[Iterable[str]] = None,
        fusion_bad_entities: Optional[Iterable[str]] = None,
        boundary_words: Optional[Sequence[str]] = None,
        source_weights: Optional[Dict[str, float]] = None,
        source_min_scores: Optional[Dict[str, float]] = None,
        relation_min_scores: Optional[Dict[str, float]] = None,
        relation_caps: Optional[Dict[str, int]] = None,
        max_triples_per_item: int = 48,
        dev_ratio: float = 0.2,
        fold_count: int = 5,
        lora_r: int = 32,
        lora_alpha: int = 64,
        lora_dropout: float = 0.05,
        learning_rate: float = 0.0002,
        num_train_epochs: float = 3.0,
        relation_weights: Optional[Dict[str, float]] = None,
        target_modules: Optional[Sequence[str]] = None,
        relation_weight_max: float = 3.0,
        train_batch_size: int = 1,
        eval_batch_size: int = 1,
        gradient_accumulation_steps: int = 8,
        warmup_ratio: float = 0.03,
        random_state: int = 42,
    ) -> None:
        """
        Configure the learner and initialize training and inference state.

        Args:
            model_id: Hugging Face base model ID or local path.
            auxiliary_data: Optional labeled ontology expansion records.
            device: Model device for base-model inference.
            train_adapter: Whether to train the relation-weighted QLoRA adapter.
            adapter_path: Optional existing trained adapter directory; skips training.
            output_dir: Directory for adapter and optional training artifacts.
            local_files_only: Only use locally cached model files.
            max_input_tokens: Maximum input tokens.
            max_output_tokens: Initial generation budget.
            retry_output_tokens: Retry generation budget.
            max_train_samples: Optional training subset for smoke tests.
            max_eval_samples: Optional evaluation subset for training diagnostics.
            max_steps: Optional training steps limit for tests.
            system_prompt: Custom system instructions. If None, use the default system prompt.
            construction_prompt: Sequence of construction instruction strings. If None, use the default instructions.
            allowed_relations: Permitted relation labels. If None, use the default vocabulary.
            bad_entity_keys: Normalized entity keys rejected during candidate cleaning. If None, use the default keys.
            fusion_bad_entities: Additional normalized entity keys rejected during fusion. If None, use the default keys.
            boundary_words: Literal leading words removed during entity cleaning. If None, use the default words.
            source_weights: Overrides for the default candidate source weights.
            source_min_scores: Overrides for the default source acceptance thresholds.
            relation_min_scores: Overrides for the default relation acceptance thresholds.
            relation_caps: Overrides for the default per-relation output limits.
            max_triples_per_item: Maximum number of accepted triples per sample.
            dev_ratio: Fraction used for deterministic development assignment, not a held-out split.
            fold_count: Number of deterministic fold labels in prepared training records. Does not enable cross-validation.
            lora_r: LoRA adapter rank.
            lora_alpha: LoRA adapter scaling parameter.
            lora_dropout: LoRA dropout probability.
            learning_rate: Learning rate for adapter training.
            num_train_epochs: Number of adapter training epochs.
            relation_weights: Overrides for the default relation-specific sample weights.
            target_modules: Modules targeted by LoRA adaptation. If None, use the default modules.
            relation_weight_max: Maximum training sample weight.
            train_batch_size: Per-device training batch size. With a batch size of one, normalized sample weighting cancels out.
            eval_batch_size: Per-device evaluation batch size.
            gradient_accumulation_steps: Number of steps accumulated before an optimizer update.
            warmup_ratio: Fraction of training steps used for learning-rate warmup.
            random_state: Random seed for model training and data sampling.

        """
        super().__init__()
        self.model_id = model_id
        self.auxiliary_data = list(auxiliary_data) if auxiliary_data is not None else None
        self.device = device
        self.train_adapter = train_adapter
        self.adapter_path = Path(adapter_path) if adapter_path is not None else None
        self._existing_adapter = adapter_path is not None
        self.output_dir = Path(output_dir)
        self.local_files_only = local_files_only
        self.max_input_tokens = max_input_tokens
        self.max_output_tokens = max_output_tokens
        self.retry_output_tokens = retry_output_tokens
        self.max_train_samples = max_train_samples
        self.max_eval_samples = max_eval_samples
        self.max_steps = max_steps
        self.system_prompt = self._system_prompt if system_prompt is None else system_prompt
        self.construction_prompt = list(self._construction_prompt if construction_prompt is None else construction_prompt)
        self.allowed_relations = list(self._allowed_relations if allowed_relations is None else allowed_relations)
        self.bad_entity_keys = set(self._bad_entity_keys if bad_entity_keys is None else bad_entity_keys)
        self.fusion_bad_entities = set(self._fusion_bad_entities if fusion_bad_entities is None else fusion_bad_entities)
        self.boundary_words = tuple(self._boundary_words if boundary_words is None else boundary_words)
        self.source_weights = {**self._source_weights, **(source_weights or {})}
        self.source_min_scores = {**self._source_min_scores, **(source_min_scores or {})}
        self.relation_min_scores = {**self._relation_min_scores, **(relation_min_scores or {})}
        self.relation_caps = {**self._relation_caps, **(relation_caps or {})}
        self.max_triples_per_item = max_triples_per_item
        self.dev_ratio = dev_ratio
        self.fold_count = fold_count
        self.lora_r = lora_r
        self.lora_alpha = lora_alpha
        self.lora_dropout = lora_dropout
        self.learning_rate = learning_rate
        self.num_train_epochs = num_train_epochs
        self.relation_weights = {**self._relation_weights, **(relation_weights or {})}
        self.target_modules = list(self._target_modules if target_modules is None else target_modules)
        self.relation_weight_max = relation_weight_max
        self.train_batch_size = train_batch_size
        self.eval_batch_size = eval_batch_size
        self.gradient_accumulation_steps = gradient_accumulation_steps
        self.warmup_ratio = warmup_ratio
        self.random_state = random_state

        self.generator = None
        self.graph_index: Dict[str, Any] = {}
        self.train_rows: List[Dict[str, Any]] = []
        self.training_summary: Dict[str, Any] = {}
        self.inference_log: Dict[str, Any] = {}

    def load(self, model_id: Optional[str] = None, adapter_path: Optional[str] = None) -> None:
        """
        Load a trained adapter or a pretrained model for inference.

        When adapter training is enabled and no adapter is supplied, model
        initialization is deferred to fit().

        Args:
            model_id: Optional Hugging Face model identifier or local path.
            adapter_path: Optional path to a trained LoRA adapter.

        Raises:
            RuntimeError: If adapter inference is requested without CUDA.
            FileNotFoundError: If the adapter directory does not exist.
        """
        if model_id is not None:
            self.model_id = model_id
        if adapter_path is not None:
            self.adapter_path = Path(adapter_path)
            self._existing_adapter = True

        if self.adapter_path is not None:
            self.generator = self._AdapterGenerator(
                self, self.model_id, self.adapter_path, self.local_files_only
            )
        elif not self.train_adapter:
            self.generator = self._BaseGenerator(
                self, self.model_id,
                device=self.device,
                local_files_only=self.local_files_only,
                max_input_tokens=self.max_input_tokens,
                max_output_tokens=self.max_output_tokens,
            )

    @staticmethod
    def _validate_record(sample: Dict[str, Any]) -> Dict[str, Any]:
        """Validate the identifier and context of a primitive ontology record."""
        if not isinstance(sample.get("id"), str) or not isinstance(sample.get("context"), str):
            raise ValueError("Each record must have string 'id' and 'context' fields.")
        return dict(sample)

    def _ontology_construction(self, data: Any, test: bool = False) -> Optional[Any]:
        """Fit on labeled records or infer ontology triples from documents."""
        if test:
            return self._construct_ontologies(data)
        self._prepare_training_data(data)
        return None

    def _prepare_training_data(self, data: Any) -> None:
        """Prepare construction training data and optional auxiliary expansion supervision."""
        samples = data if isinstance(data, (list, tuple)) else [data]
        ontology_construction = [self._validate_record(sample) for sample in samples]
        if not ontology_construction:
            raise ValueError("Training requires at least one labeled ontology construction record.")
        for sample in ontology_construction:
            if "primitive-ontology-triples" not in sample:
                raise ValueError("ontology construction training records require 'primitive-ontology-triples'.")

        ontology_expansion = [self._validate_record(sample) for sample in self.auxiliary_data or []]
        ontology_construction_rows = [self._prepare_construction_record(sample) for sample in ontology_construction]
        ontology_expansion_rows, ontology_expansion_metadata = self.prepare_expansion_supervision(ontology_expansion)
        # Keep auxiliary samples in the training rows, not in graph completion.
        mixed_rows = ontology_construction_rows + ontology_expansion_rows
        ids = [row["id"] for row in mixed_rows]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate ID in combined training records.")

        self.train_rows = mixed_rows
        self.graph_index = self.build_graph_index(ontology_construction)
        self.training_summary = {
            "ontology_construction_rows": len(ontology_construction_rows),
            "ontology_construction_dev_rows": sum(row["split"] == "dev" for row in ontology_construction_rows),
            "mixed_train_rows": len(mixed_rows),
            "allowed_relations": self.allowed_relations,
            **ontology_expansion_metadata,
        }

        # Full QLoRA training is optional; the CPU path prepares data only.
        if self.train_adapter and not self._existing_adapter:
            if not self.device.startswith("cuda"):
                raise RuntimeError("Relation-weighted 4-bit QLoRA training requires a CUDA device.")
            eval_rows = [row for row in ontology_construction_rows if row["split"] == "dev"]
            if not eval_rows:
                raise ValueError(
                    "No ontology construction development records selected by the deterministic split algorithm. "
                    "Use more training records when train_adapter=True."
                )
            self.output_dir.mkdir(parents=True, exist_ok=True)
            self.adapter_path = self.output_dir / "adapter"
            self.training_summary["adapter_training"] = self._train_adapter(
                mixed_rows,
                eval_rows,
                self.adapter_path,
                base_model=self.model_id,
                local_files_only=self.local_files_only,
                max_train_samples=self.max_train_samples,
                max_eval_samples=self.max_eval_samples,
                max_steps=self.max_steps,
            )
            self.load(adapter_path=str(self.adapter_path))

    def _construct_ontologies(self, data: Any) -> List[Dict[str, Any]]:
        """Generate and validate ontology triples with the construction pipeline."""
        if self.generator is None:
            raise RuntimeError("Call load() before predict(), or fit() with train_adapter=True.")
        if not self.graph_index:
            raise RuntimeError("Call fit() with ontology construction training annotations before predict().")
        samples = data if isinstance(data, (list, tuple)) else [data]
        items = [self._validate_record(sample) for sample in samples]
        predictions, self.inference_log = self._predict_items(
            items, self.graph_index, self.generator,
            retry_output_tokens=self.retry_output_tokens,
        )
        errors = self.validate_predictions(
            predictions,
            expected_ids=[item["id"] for item in items],
            require_order=True,
        )
        if errors:
            raise RuntimeError("Prediction validation failed: " + "; ".join(errors[:10]))
        return predictions

    @dataclass
    class ParseResult:
        """
        Store parsed ontology triples and model-output diagnostics.
        """
        rows: List["BigDipperAIPrimitiveLearner.ScoredTriple"]
        hard_error: str = ""
        soft_errors: Tuple[str, ...] = ()
        raw_length: int = 0
        salvaged_count: int = 0


    @dataclass
    class ScoredTriple:
        """
        Represent a candidate ontology edge with its provenance and score.
        """
        triple: BigDipperAIPrimitiveLearner.Triple
        source: str
        score: float
        evidence: str = ""
        entity_presence: str = "ontology_prior"


    def build_construction_prompt(self, item: Dict[str, Any]) -> str:
        """
        Build the constrained JSON extraction prompt for an ontology construction sample.

        Args:
            item: Ontology construction record with an ID and text context.

        Returns:
            JSON-encoded prompt with permitted relations and output schema.
        """
        schema = {"primitive-ontology-triples": [["subject", "relation", "object"]]}
        instructions = self.construction_prompt
        # Keep the extraction instructions and output schema in the prompt payload.
        payload = {
            "prompt_version": "ontology-construction",
            "instructions": instructions,
            "allowed_relations": self.allowed_relations,
            "output_schema": schema,
            "id": item.get("id", ""),
            "context": item["context"],
        }
        return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


    def _apply_chat_template_json(
        self,
        tokenizer: Any,
        messages: Sequence[Dict[str, str]],
        enable_thinking: Optional[bool] = False,
    ) -> str:
        """Format messages using the model chat template."""
        if not hasattr(tokenizer, "apply_chat_template"):
            return messages[-1]["content"] + "\nJSON:"
        kwargs = {"tokenize": False, "add_generation_prompt": True}
        if enable_thinking is not None:
            try:
                return tokenizer.apply_chat_template(messages, enable_thinking=enable_thinking, **kwargs)
            except TypeError:
                pass
        return tokenizer.apply_chat_template(messages, **kwargs)


    def _normalize_space(self, text: str) -> str:
        """Collapse repeated whitespace in text."""
        return re.sub(r"\s+", " ", text).strip()


    def _normalize_key(self, text: str) -> str:
        """Normalize a string to a lowercase comparison key."""
        text = text.lower()
        text = re.sub(r"[\u2010-\u2015]", "-", text)
        text = re.sub(r"[^a-z0-9]+", " ", text)
        return self._normalize_space(text)


    def _compact_key(self, text: str) -> str:
        """Build a compact ASCII comparison key for an entity."""
        return re.sub(r"[^a-z0-9]+", "", text.lower())


    def _unicode_compact_key(self, text: str) -> str:
        """Build a Unicode-aware alphanumeric comparison key."""
        text = unicodedata.normalize("NFKC", text).casefold()
        return "".join(ch for ch in text if unicodedata.category(ch)[0] in {"L", "N"})


    def _entity_presence(self, entity: str, context: str) -> float:
        """Score how directly an entity is mentioned in the source context."""
        if not entity:
            return 0.0
        if entity in context:
            return 1.0
        if entity.lower() in context.lower():
            return 0.86
        normalized = self._normalize_key(entity)
        compact = self._compact_key(entity)
        if normalized and normalized in self._normalize_key(context):
            return 0.7
        if compact and compact in self._compact_key(context):
            return 0.58
        return 0.0


    def _triples_from_item(self, item: Dict[str, Any]) -> List[BigDipperAIPrimitiveLearner.Triple]:
        """Extract well-formed ontology construction ground-truth triples from a record."""
        rows: List[BigDipperAIPrimitiveLearner.Triple] = []
        for triple in item.get("primitive-ontology-triples", []):
            if isinstance(triple, list) and len(triple) == 3:
                values = tuple(str(value).strip() for value in triple)
                if all(values):
                    rows.append(values)  # type: ignore[arg-type]
        return rows


    def _serialize_triples(self, triples: Iterable[BigDipperAIPrimitiveLearner.Triple]) -> List[List[str]]:
        """Convert triple tuples to JSON-compatible triple lists."""
        return [[subject, relation, obj] for subject, relation, obj in triples]


    def _relation_counts(self, triples: Sequence[BigDipperAIPrimitiveLearner.Triple]) -> Dict[str, int]:
        """Count the relation types in a sequence of triples."""
        return dict(Counter(relation for _, relation, _ in triples).most_common())


    def _clean_entity(self, text: str) -> str:
        """Remove generic boundary text and punctuation from an entity."""
        text = re.sub(r"\s+", " ", text).strip()
        text = text.strip(" .,:;[]{}\"'")
        if self.boundary_words:
            text = re.sub(r"^(?:" + "|".join(re.escape(word) for word in self.boundary_words) + r")\s+", "", text, flags=re.I)
        text = re.sub(
            r"^.*\b(?:including|such as|include|includes|contains|contain|encompasses|encompass)\s+",
            "",
            text,
            flags=re.I,
        )
        text = re.sub(
            r"^.*\b(?:order|class|category|group)\s+([A-Za-z0-9][A-Za-z0-9_\-/() :]{1,120})$",
            r"\1",
            text,
            flags=re.I,
        )
        text = re.sub(r"\s+(?:which|that|where|while|when)\b.*$", "", text, flags=re.I)
        text = re.sub(
            r"\b(?:within|in|for|during|across)\s+(?:the|this|these)?\s*(?:broader|general|wider)?\s*(?:group|category|class|taxonomy|system|database|context|field)\b.*$",
            "",
            text,
            flags=re.I,
        )
        return re.sub(r"\s+", " ", text).strip(" .,:;[]{}\"'")


    def _repair_relation(self, relation: str) -> str:
        """Convert common relation aliases to supported relation names."""
        relation = relation.strip()
        aliases = {
            "is_a": "is-a",
            "isa": "is-a",
            "subclass_of": "is-a",
            "subclass of": "is-a",
            "subclass": "is-a",
            "subtype": "is-a",
            "type of": "is-a",
            "instance_of": "instance-of",
            "instance of": "instance-of",
            "part of": "part_of",
            "same_as": "same as",
            "equivalent_class": "equivalent class",
            "exact_match": "exact match",
        }
        return aliases.get(relation.lower(), relation)


    def _is_short_symbol_entity(self, entity: str, relation: str, other: str) -> bool:
        """Allow short ontology symbols only in supported contexts."""
        raw = entity.strip()
        key = self._unicode_compact_key(raw)
        if len(key) < 1 or len(key) > 2:
            return False
        if not re.fullmatch(r"[A-Za-z]{1,2}", raw):
            return False
        if self._normalize_key(raw) in self.bad_entity_keys:
            return False
        noise = {"in", "of", "to", "as", "by", "on", "or", "is", "be", "we", "he", "me", "my", "no", "so", "up"}
        if key in noise:
            return False
        if relation not in {"is-a", "instance-of", "type"}:
            return False
        if relation == "is-a" and self._normalize_key(other) in {"atom", "element"}:
            return True
        if relation == "instance-of":
            if self._unicode_compact_key(raw) == self._unicode_compact_key(other):
                return True
            if re.fullmatch(r"[A-Z][a-z]?", other.strip()):
                return True
        return False


    def _valid_ontology_entity(self, entity: str, allow_short: bool = False) -> bool:
        """Reject empty, generic, or excessively long ontology entities."""
        entity = unicodedata.normalize("NFKC", entity.strip())
        if len(entity) > 180:
            return False
        if len(entity) < 2 and not allow_short:
            return False
        if not self._unicode_compact_key(entity):
            return False
        key = self._normalize_key(entity)
        if key and key in self.bad_entity_keys:
            return False
        if len(re.findall(r"\S+", entity)) > 20:
            return False
        return True


    def _clean_candidate_triple(self, triple: BigDipperAIPrimitiveLearner.Triple) -> Optional[BigDipperAIPrimitiveLearner.Triple]:
        """Normalize a triple and reject unsupported relations or entities."""
        subject = self._clean_entity(str(triple[0]))
        relation = self._repair_relation(str(triple[1]))
        obj = self._clean_entity(str(triple[2]))
        if relation not in set(self.allowed_relations):
            return None
        subject_short = self._is_short_symbol_entity(subject, relation, obj)
        object_short = self._is_short_symbol_entity(obj, relation, subject)
        if not self._valid_ontology_entity(subject, subject_short) or not self._valid_ontology_entity(obj, object_short):
            return None
        if not subject_short and not self._entity_meets_compact_min(subject, 3):
            return None
        if not object_short and not self._entity_meets_compact_min(obj, 3):
            return None
        return subject, relation, obj


    def _entity_meets_compact_min(self, entity: str, minimum: int) -> bool:
        """Check the minimum entity length using Unicode-aware symbols."""
        key = self._unicode_compact_key(entity)
        required = min(minimum, 2) if any(ord(ch) > 127 for ch in key) else minimum
        return len(key) >= required


    def _coerce_triple(self, row: Any) -> Optional[BigDipperAIPrimitiveLearner.Triple]:
        """Read a candidate triple from list or dictionary output."""
        if isinstance(row, list) and len(row) >= 3:
            return str(row[0]), str(row[1]), str(row[2])
        if isinstance(row, dict):
            subject = row.get("subject", row.get("s"))
            relation = row.get("relation", row.get("predicate", row.get("r")))
            obj = row.get("object", row.get("o"))
            if subject is not None and relation is not None and obj is not None:
                if isinstance(obj, list):
                    obj = "; ".join(str(value).strip() for value in obj if str(value).strip())
                return str(subject), str(relation), str(obj)
        return None


    def _repair_truncated_json(self, candidate: str) -> str:
        """Recover a potentially complete JSON prefix from truncated output."""
        candidate = candidate.strip()
        repairs = []
        for marker in ["]}", "]]", "]"]:
            index = candidate.rfind(marker)
            if index < 0:
                continue
            repaired = candidate[: index + len(marker)]
            if marker == "]]" and not repaired.rstrip().endswith("}"):
                repaired = '{"primitive-ontology-triples":' + repaired + "}"
            elif marker == "]" and candidate.lstrip().startswith("{") and not repaired.rstrip().endswith("}"):
                repaired += "}"
            repairs.append(repaired)
        return repairs[0] if repairs else ""


    def _extract_json_payload(self, text: str) -> Tuple[Any, str]:
        """Locate and parse a JSON object or array in generated text."""
        candidates: List[str] = re.findall(r"```(?:json)?\s*(.*?)\s*```", text, flags=re.S)
        for left, right in [("{", "}"), ("[", "]")]:
            start = text.find(left)
            end = text.rfind(right)
            if start >= 0 and end > start:
                candidates.append(text[start : end + 1])
        last_error = "no_json"
        # First parse the complete JSON span; attempt a truncated-prefix repair on failure.
        for candidate in candidates:
            try:
                return json.loads(candidate), ""
            except Exception as exc:
                last_error = str(exc)
                repaired = self._repair_truncated_json(candidate)
                if repaired and repaired != candidate:
                    try:
                        return json.loads(repaired), ""
                    except Exception as repaired_exc:
                        last_error = str(repaired_exc)
        return None, last_error


    def _dedupe_scored(self, rows: Iterable[BigDipperAIPrimitiveLearner.ScoredTriple]) -> List[BigDipperAIPrimitiveLearner.ScoredTriple]:
        """Keep the highest-scoring row for each distinct triple."""
        best: Dict[BigDipperAIPrimitiveLearner.Triple, BigDipperAIPrimitiveLearner.ScoredTriple] = {}
        for row in rows:
            if row.triple not in best or row.score > best[row.triple].score:
                best[row.triple] = row
        return list(best.values())


    def _salvage_model_triples(self, text: str) -> List[BigDipperAIPrimitiveLearner.ScoredTriple]:
        """Recover valid triple arrays when the full JSON cannot be parsed."""
        decoder = json.JSONDecoder()
        rows: List[BigDipperAIPrimitiveLearner.ScoredTriple] = []
        for index, char in enumerate(text):
            if char != "[":
                continue
            try:
                payload, _ = decoder.raw_decode(text, index)
            except Exception:
                continue
            triple = self._coerce_triple(payload)
            cleaned = self._clean_candidate_triple(triple) if triple else None
            if cleaned:
                rows.append(self.ScoredTriple(cleaned, "sft", 1.0, "model_json_salvage"))
        return self._dedupe_scored(rows)


    def parse_model_output(self, text: str) -> BigDipperAIPrimitiveLearner.ParseResult:
        """
        Parse and validate model-generated ontology triples.

        This method supports JSON objects and arrays, recovers valid triples
        from truncated JSON responses, and removes invalid and duplicate triples.

        Args:
            text: Raw text generated by the language model.

        Returns:
            A ParseResult containing scored triples and parsing diagnostics.
        """
        payload, error = self._extract_json_payload(text)
        # Recover individual triple arrays when generation ends mid-object.
        if payload is None:
            salvaged = self._salvage_model_triples(text)
            if salvaged:
                return self.ParseResult(
                    salvaged,
                    hard_error=error,
                    soft_errors=("salvaged_truncated_json",),
                    raw_length=len(text),
                    salvaged_count=len(salvaged),
                )
            return self.ParseResult([], hard_error=error, raw_length=len(text))
        if isinstance(payload, list):
            triples_payload = payload
        elif isinstance(payload, dict):
            triples_payload = payload.get("primitive-ontology-triples", payload.get("triples", []))
        else:
            return self.ParseResult([], hard_error="json_not_object_or_list", raw_length=len(text))
        if not isinstance(triples_payload, list):
            return self.ParseResult([], hard_error="triples_not_list", raw_length=len(text))
        rows: List[BigDipperAIPrimitiveLearner.ScoredTriple] = []
        diagnostics = []
        for row in triples_payload:
            triple = self._coerce_triple(row)
            if triple is None:
                diagnostics.append("bad_shape")
                continue
            cleaned = self._clean_candidate_triple(triple)
            if cleaned is None:
                diagnostics.append("invalid_triple")
                continue
            rows.append(self.ScoredTriple(cleaned, "sft", 1.0, "model_json"))
        return self.ParseResult(
            self._dedupe_scored(rows),
            soft_errors=tuple(sorted(set(diagnostics))),
            raw_length=len(text),
        )


    def _classify_entity_presence(self, triple: BigDipperAIPrimitiveLearner.Triple, context: str) -> str:
        """Classify whether a candidate entity occurs in the source text."""
        subject, _, obj = triple
        subject_presence = self._entity_presence(subject, context)
        object_presence = self._entity_presence(obj, context)
        if subject_presence >= 0.86 and object_presence >= 0.86:
            return "text_span"
        if subject_presence >= 0.58 or object_presence >= 0.58:
            return "normalized_text_span"
        return "ontology_prior"


    def build_graph_completion_candidates(self, item: Dict[str, Any], graph_index: Dict[str, Any], seed_rows: Sequence[BigDipperAIPrimitiveLearner.ScoredTriple]) -> List[BigDipperAIPrimitiveLearner.ScoredTriple]:
        """
        Recover supported self-edges from the ontology construction training graph.

        This method identifies relevant entities from the source context and
        seed triples, recovers self-edges observed in the training graph, and
        assigns heuristic scores based on their training frequency.

        Args:
            item: Input sample containing the source context.
            graph_index: Training-derived index containing entity surface forms
                         and triple frequencies.
            seed_rows: Scored triples used to identify relevant entities. May be empty.

        Returns:
            List of deduplicated scored graph-completion candidates.
        """
        context = item["context"]
        entities = set()
        for row in seed_rows:
            entities.add(row.triple[0])
            entities.add(row.triple[2])
        lowered = context.lower()
        present = []
        for forms in graph_index.get("entity_forms", {}).values():
            for form in forms.keys():
                form = str(form)
                if len(form) >= 3 and form.lower() in lowered:
                    present.append(form)
        present = sorted(set(present), key=lambda value: (-len(value), value.lower()))[:16]
        entities.update(present)
        entity_keys = {self._compact_key(entity) for entity in entities}
        rows = []
        # Only recover self-edges observed in the ontology construction training graph.
        for record in graph_index.get("triple_counts", []):
            triple = (record["subject"], record["relation"], record["object"])
            count = int(record["count"])
            subject, relation, obj = triple
            if subject != obj or relation not in set(self.allowed_relations) or count < 1:
                continue
            if self._compact_key(subject) not in entity_keys and self._entity_presence(subject, context) < 0.58:
                continue
            score = 0.82 + min(0.16, math.log1p(count) * 0.04)
            cleaned = self._clean_candidate_triple(triple)
            if cleaned:
                rows.append(
                    self.ScoredTriple(
                        cleaned,
                        "graph_completion",
                        score,
                        f"self_edge_count={count}",
                        self._classify_entity_presence(cleaned, context),
                    )
                )
        return self._dedupe_scored(rows)


    def _presence_bonus(self, triple: BigDipperAIPrimitiveLearner.Triple, context: str) -> float:
        """Assign a small score bonus for entities found in the text."""
        subject, _, obj = triple
        return 0.04 * self._entity_presence(subject, context) + 0.04 * self._entity_presence(obj, context)


    def _relation_rank_key(self, row: BigDipperAIPrimitiveLearner.ScoredTriple) -> Tuple[float, float]:
        """Rank candidates using relation and entity-presence priorities."""
        priority = {
            "is-a": 0.08,
            "instance-of": 0.06,
            "is defined by": 0.04,
            "equivalent class": 0.03,
            "disjoint with": 0.03,
        }.get(row.triple[1], 0.0)
        presence = {
            "text_span": 0.04,
            "normalized_text_span": 0.02,
            "ontology_prior": 0.0,
        }.get(row.entity_presence, 0.0)
        return row.score + priority + presence, row.score


    def fuse_candidates(self, item: Dict[str, Any], rows: Sequence[BigDipperAIPrimitiveLearner.ScoredTriple]) -> Tuple[List[BigDipperAIPrimitiveLearner.Triple], List[Dict[str, Any]]]:
        """
        Fuse candidate triples from model predictions and graph completion.

        This method applies source-specific weights, relation-specific thresholds,
        and entity presence scores to rank candidate triples. It retains the
        highest-scoring candidate for each unique triple and applies relation-specific
        and global output limits.

        Args:
            item: Input sample containing the source context.
            rows: Candidate triples with source labels, scores, and supporting evidence.

        Returns:
            A tuple containing accepted ontology triples and diagnostic records
            with candidate scores, evidence, and rejection counts.
        """
        # Apply source-specific thresholds before selecting the strongest triple.
        best: Dict[BigDipperAIPrimitiveLearner.Triple, BigDipperAIPrimitiveLearner.ScoredTriple] = {}
        rejected: Counter[str] = Counter()
        for row in rows:
            cleaned = self._clean_candidate_triple(row.triple)
            if cleaned is None:
                rejected["invalid"] += 1
                continue
            if self._normalize_key(cleaned[0]) in self.fusion_bad_entities or self._normalize_key(cleaned[2]) in self.fusion_bad_entities:
                rejected["bad_entity"] += 1
                continue
            weighted = row.score * self.source_weights.get(row.source, 1.0)
            required = max(
                self.source_min_scores.get(row.source, 0.0),
                self.relation_min_scores.get(cleaned[1], self.relation_min_scores["default"]),
            )
            if weighted < required:
                rejected["below_threshold"] += 1
                continue
            scored = self.ScoredTriple(
                cleaned,
                row.source,
                weighted + self._presence_bonus(cleaned, item["context"]),
                row.evidence,
                self._classify_entity_presence(cleaned, item["context"]),
            )
            if cleaned not in best or scored.score > best[cleaned].score:
                best[cleaned] = scored

        # Rank valid triples and apply per-relation and global output limits.
        ranked = sorted(best.values(), key=self._relation_rank_key, reverse=True)
        accepted = []
        caps: Counter[str] = Counter()
        for row in ranked:
            relation = row.triple[1]
            cap = self.relation_caps.get(relation, self.relation_caps["default"])
            if caps[relation] >= cap:
                rejected["relation_cap"] += 1
                continue
            accepted.append(row)
            caps[relation] += 1
            if len(accepted) >= self.max_triples_per_item:
                break
        log_rows = [
            {
                "triple": list(row.triple),
                "source": row.source,
                "score": row.score,
                "evidence": row.evidence,
                "entity_presence": row.entity_presence,
            }
            for row in accepted
        ]
        log_rows.append({"diagnostics": {"rejected": dict(rejected), "candidate_count": len(rows)}})
        return [row.triple for row in accepted], log_rows


    def _prediction_payload(
        self,
        items: Sequence[Dict[str, Any]],
        triples_by_id: Dict[str, List[BigDipperAIPrimitiveLearner.Triple]],
    ) -> List[Dict[str, Any]]:
        """Produce OntoLearner prediction dictionaries in input order."""
        return [
            {
                "id": item["id"],
                "primitive-ontology-triples": self._serialize_triples(triples_by_id.get(item["id"], [])),
            }
            for item in items
        ]


    def validate_predictions(self, payload: Any, expected_ids: Optional[Sequence[str]] = None, require_order: bool = True) -> List[str]:
        """
        Validate prediction structure, output IDs, and permitted relations.

        Args:
            payload: Generated prediction dictionaries.
            expected_ids: Optional expected sample IDs.
            require_order: Whether predicted IDs must preserve input order.

        Returns:
            Structural validation errors, or an empty list if none are found.
        """
        if not isinstance(payload, list):
            return ["payload is not a list"]
        errors = []
        seen_ids = set()
        item_ids = []
        for index, item in enumerate(payload):
            if not isinstance(item, dict):
                errors.append(f"item {index} is not an object")
                continue
            extra = sorted(set(item) - {"id", "primitive-ontology-triples"})
            if extra:
                errors.append(f"item {index} has unexpected keys: {extra}")
            item_id = item.get("id")
            if not isinstance(item_id, str) or not item_id:
                errors.append(f"item {index} has no id")
            elif item_id in seen_ids:
                errors.append(f"duplicate id: {item_id}")
            else:
                seen_ids.add(item_id)
                item_ids.append(item_id)
            triples = item.get("primitive-ontology-triples")
            if not isinstance(triples, list):
                errors.append(f"{item_id}: triples is not a list")
                continue
            for triple_index, triple in enumerate(triples):
                if not isinstance(triple, list) or len(triple) != 3:
                    errors.append(f"{item_id}: triple {triple_index} is not a length-3 list")
                    continue
                if not all(isinstance(value, str) and value for value in triple):
                    errors.append(f"{item_id}: triple {triple_index} has an empty or non-string value")
                    continue
                if triple[1] not in set(self.allowed_relations):
                    errors.append(f"{item_id}: triple {triple_index} uses an unsupported relation")
        if expected_ids is not None:
            expected = list(expected_ids)
            missing = [item_id for item_id in expected if item_id not in set(item_ids)]
            extra_ids = [item_id for item_id in item_ids if item_id not in set(expected)]
            if missing:
                errors.append(f"missing {len(missing)} expected ids; first missing id={missing[0]}")
            if extra_ids:
                errors.append(f"found {len(extra_ids)} unexpected ids; first unexpected id={extra_ids[0]}")
            if require_order and item_ids != expected:
                errors.append("prediction ids are not in expected order")
        return errors

    def _stable_dev_split(self, item_id: str) -> str:
        """Assign the deterministic hash-based development split to an ontology construction sample."""
        digest = hashlib.md5(f"development:{item_id}".encode("utf-8")).hexdigest()
        bucket = int(digest[:8], 16) / 0xFFFFFFFF
        return "dev" if bucket < self.dev_ratio else "train"

    def _fold_for_id(self, item_id: str) -> int:
        """Assign a deterministic data fold from the item ID."""
        digest = hashlib.md5(f"fold:{item_id}".encode("utf-8")).hexdigest()
        return int(digest[:8], 16) % self.fold_count

    def _prepare_construction_record(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Convert a labeled ontology construction sample into supervised JSON training data."""
        triples = self._triples_from_item(item)
        return {
            "id": item["id"],
            "split": self._stable_dev_split(item["id"]),
            "fold": self._fold_for_id(item["id"]),
            "prompt": self.build_construction_prompt(item),
            "target_json": json.dumps(
                {"primitive-ontology-triples": self._serialize_triples(triples)},
                ensure_ascii=False,
                separators=(",", ":"),
            ),
            "relation_counts": self._relation_counts(triples),
            "gold_triple_count": len(triples),
        }

    def _coerce_expansion_triple(self, row: Any) -> BigDipperAIPrimitiveLearner.Triple | None:
        """Convert one ontology expansion triple to a validated string tuple."""
        if not isinstance(row, list) or len(row) != 3:
            return None
        values = tuple(str(value).strip() for value in row)
        if not all(values):
            return None
        return values  # type: ignore[return-value]

    def _clean_expansion_triples(self, groups: Sequence[Iterable[Any]]) -> Tuple[List[BigDipperAIPrimitiveLearner.Triple], Dict[str, int], int]:
        """Merge and deduplicate permitted initial and extended ontology expansion triples."""
        allowed = set(self.allowed_relations)
        dropped: Counter[str] = Counter()
        seen = set()
        triples = []
        duplicate_count = 0
        for group in groups:
            for row in group:
                triple = self._coerce_expansion_triple(row)
                if triple is None:
                    dropped["<bad-shape>"] += 1
                    continue
                if triple[1] not in allowed:
                    dropped[triple[1]] += 1
                    continue
                if triple in seen:
                    duplicate_count += 1
                    continue
                seen.add(triple)
                triples.append(triple)
        return triples, dict(sorted(dropped.items())), duplicate_count

    def prepare_expansion_supervision(self, items: Sequence[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """
        Prepare auxiliary ontology construction training examples from labeled
        ontology expansion records.

        This method merges initial and extended ontology triples, removes
        duplicates, and filters unsupported relations before converting the
        records into supervised training examples.

        Args:
            items: Labeled expansion records containing an ID, textual context,
                   initial ontology triples, and extended ontology triples.

        Returns:
            A tuple containing auxiliary training records and metadata describing
            retained relations, discarded relations, duplicate triples, and
            empty training targets.
        """
        rows = []
        dropped_relations: Counter[str] = Counter()
        kept_relations: Counter[str] = Counter()
        duplicate_triples = 0
        empty_targets = 0
        # Include both initial and extended expansion triples as auxiliary supervision.
        for item in items:
            triples, dropped, duplicate_count = self._clean_expansion_triples(
                [
                    item.get("initial-primitive-ontology-triples") or [],
                    item.get("extended-primitive-ontology-triples") or [],
                ]
            )
            dropped_relations.update(dropped)
            kept_relations.update(relation for _, relation, _ in triples)
            duplicate_triples += duplicate_count
            if not triples:
                empty_targets += 1
            item_id = f"ontology_expansion:{item['id']}"
            prompt_item = {
                "id": item_id,
                "context": item["context"],
                "primitive-ontology-triples": self._serialize_triples(triples),
            }
            rows.append(
                {
                    "id": item_id,
                    "split": "train",
                    "fold": self._fold_for_id(item_id),
                    "source_task": "ontology_expansion_auxiliary",
                    "prompt": self.build_construction_prompt(prompt_item),
                    "target_json": json.dumps(
                        {"primitive-ontology-triples": self._serialize_triples(triples)},
                        ensure_ascii=False,
                        separators=(",", ":"),
                    ),
                    "relation_counts": self._relation_counts(triples),
                    "gold_triple_count": len(triples),
                }
            )
        metadata = {
            "ontology_expansion_items": len(items),
            "ontology_expansion_aux_rows": len(rows),
            "ontology_expansion_kept_triples": sum(row["gold_triple_count"] for row in rows),
            "ontology_expansion_duplicate_triples_removed": duplicate_triples,
            "ontology_expansion_empty_targets": empty_targets,
            "ontology_expansion_kept_relation_counts": dict(sorted(kept_relations.items())),
            "ontology_expansion_dropped_relation_counts": dict(sorted(dropped_relations.items())),
        }
        return rows, metadata


    def build_graph_index(self, items: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Build a graph index from labeled ontology construction records.

        This method counts triple occurrences and groups entity surface forms
        by their normalized keys. The resulting index provides training-derived
        evidence for graph completion.

        Args:
            items: Labeled construction records containing reference ontology triples.

        Returns:
            Dictionary containing the number of indexed records, triple
            frequencies, and entity surface forms with their occurrence counts.
        """
        triple_counts: Counter[BigDipperAIPrimitiveLearner.Triple] = Counter()
        entity_forms: Dict[str, Counter[str]] = defaultdict(Counter)
        for item in items:
            for subject, relation, obj in self._triples_from_item(item):
                triple_counts[(subject, relation, obj)] += 1
                entity_forms[self._compact_key(subject)][subject] += 1
                entity_forms[self._compact_key(obj)][obj] += 1
        return {
            "indexed_items": len(items),
            "triple_counts": [
                {"subject": subject, "relation": relation, "object": obj, "count": count}
                for (subject, relation, obj), count in triple_counts.most_common()
            ],
            "entity_forms": {
                key: dict(forms.most_common())
                for key, forms in entity_forms.items()
            },
        }


    def _relation_counts_from_target(self, target_json: str) -> Dict[str, int]:
        """Count relation labels from the serialized training target."""
        counts: Dict[str, int] = {}
        try:
            payload = json.loads(target_json)
        except Exception:
            return counts
        for row in payload.get("primitive-ontology-triples", []):
            if isinstance(row, list) and len(row) == 3:
                relation = str(row[1])
                counts[relation] = counts.get(relation, 0) + 1
        return counts

    def _sample_weight_for_row(self, row: Dict[str, Any]) -> float:
        """Weight training samples using the configured relation weights."""
        counts = row.get("relation_counts") or self._relation_counts_from_target(row.get("target_json", ""))
        clean_counts = {
            str(relation): int(count)
            for relation, count in counts.items()
            if count is not None and int(count) > 0
        }
        total = sum(clean_counts.values())
        if total <= 0:
            return 1.0
        weighted = sum(
            count * self.relation_weights.get(relation, self.relation_weights["default"])
            for relation, count in clean_counts.items()
        )
        return min(self.relation_weight_max, max(1.0, weighted / total))


    class _CausalJsonCollator:
        """Pad causal-language-model examples and their sample weights."""
        def __init__(self, pad_token_id: int) -> None:
            """Store the token ID used for batch padding."""
            self.pad_token_id = pad_token_id

        def __call__(self, features: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
            """Pad token and label sequences while masking padded loss tokens."""
            import torch

            max_length = max(len(row["input_ids"]) for row in features)
            input_ids = []
            labels = []
            attention_mask = []
            sample_weight = []
            for row in features:
                padding = max_length - len(row["input_ids"])
                input_ids.append(row["input_ids"] + [self.pad_token_id] * padding)
                labels.append(row["labels"] + [-100] * padding)
                attention_mask.append(row["attention_mask"] + [0] * padding)
                sample_weight.append(float(row.get("sample_weight", 1.0)))
            return {
                "input_ids": torch.tensor(input_ids, dtype=torch.long),
                "labels": torch.tensor(labels, dtype=torch.long),
                "attention_mask": torch.tensor(attention_mask, dtype=torch.long),
                "sample_weight": torch.tensor(sample_weight, dtype=torch.float),
            }

    def _resolve_resume_checkpoint(self, output_dir: Path) -> Optional[str]:
        """Find the latest saved Trainer checkpoint in the output directory."""
        checkpoints = []
        if output_dir.exists():
            for path in output_dir.glob("checkpoint-*"):
                if not path.is_dir():
                    continue
                try:
                    step = int(path.name.rsplit("-", 1)[1])
                except ValueError:
                    continue
                checkpoints.append((step, path))
        return str(max(checkpoints, key=lambda item: item[0])[1]) if checkpoints else None

    def _train_adapter(
        self,
        train_rows: Sequence[Dict[str, Any]],
        eval_rows: Sequence[Dict[str, Any]],
        adapter_dir: Path,
        base_model: str = "Qwen/Qwen3-8B",
        local_files_only: bool = False,
        max_train_samples: Optional[int] = None,
        max_eval_samples: Optional[int] = None,
        max_steps: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Fine-tune the relation-weighted 4-bit QLoRA adapter."""
        import torch
        import torch.nn.functional as functional
        from datasets import Dataset
        from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
        from transformers import (
            AutoModelForCausalLM,
            AutoTokenizer,
            BitsAndBytesConfig,
            Trainer,
            TrainingArguments,
            set_seed,
        )

        if not torch.cuda.is_available():
            raise RuntimeError("4-bit NF4 QLoRA training requires a CUDA-enabled GPU.")
        set_seed(self.random_state)
        tokenizer = AutoTokenizer.from_pretrained(
            base_model,
            trust_remote_code=True,
            local_files_only=local_files_only,
        )
        if tokenizer.pad_token_id is None:
            tokenizer.pad_token = tokenizer.eos_token
        compute_dtype = torch.bfloat16 if torch.cuda.is_available() and torch.cuda.is_bf16_supported() else torch.float16
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=compute_dtype,
            bnb_4bit_use_double_quant=True,
        )
        model = AutoModelForCausalLM.from_pretrained(
            base_model,
            trust_remote_code=True,
            local_files_only=local_files_only,
            device_map="auto",
            torch_dtype="auto",
            quantization_config=quantization_config,
        )
        model = prepare_model_for_kbit_training(model)
        model.config.use_cache = False
        model = get_peft_model(
            model,
            LoraConfig(
                r=self.lora_r,
                lora_alpha=self.lora_alpha,
                lora_dropout=self.lora_dropout,
                bias="none",
                task_type="CAUSAL_LM",
                target_modules=self.target_modules,
            ),
        )

        train_rows = list(train_rows)
        eval_rows = list(eval_rows)
        if max_train_samples is not None:
            train_rows = train_rows[:max_train_samples]
        if max_eval_samples is not None:
            eval_rows = eval_rows[:max_eval_samples]
        if not train_rows or not eval_rows:
            raise ValueError("Training and evaluation data must both contain at least one row")

        def tokenize(row: Dict[str, Any], is_eval: bool) -> Dict[str, Any]:
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": row["prompt"]},
            ]
            prompt_text = self._apply_chat_template_json(tokenizer, messages, enable_thinking=False)
            prompt_ids = tokenizer(
                prompt_text,
                truncation=True,
                max_length=self.max_input_tokens,
                add_special_tokens=False,
            )["input_ids"]
            target_ids = tokenizer(
                row["target_json"] + tokenizer.eos_token,
                truncation=True,
                max_length=self.max_output_tokens,
                add_special_tokens=False,
            )["input_ids"]
            return {
                "input_ids": prompt_ids + target_ids,
                "labels": [-100] * len(prompt_ids) + target_ids,
                "attention_mask": [1] * (len(prompt_ids) + len(target_ids)),
                "sample_weight": 1.0 if is_eval else self._sample_weight_for_row(row),
            }

        # Tokenize the prompt and target, masking prompt tokens in the loss.
        train_dataset = Dataset.from_list(train_rows)
        eval_dataset = Dataset.from_list(eval_rows)
        train_dataset = train_dataset.map(
            lambda row: tokenize(row, False),
            remove_columns=train_dataset.column_names,
        )
        eval_dataset = eval_dataset.map(
            lambda row: tokenize(row, True),
            remove_columns=eval_dataset.column_names,
        )

        training_args = TrainingArguments(
            output_dir=str(adapter_dir),
            num_train_epochs=self.num_train_epochs,
            learning_rate=self.learning_rate,
            per_device_train_batch_size=self.train_batch_size,
            per_device_eval_batch_size=self.eval_batch_size,
            gradient_accumulation_steps=self.gradient_accumulation_steps,
            logging_steps=10,
            save_steps=200,
            eval_steps=200,
            save_total_limit=3,
            max_grad_norm=0.3,
            warmup_ratio=self.warmup_ratio,
            max_steps=max_steps if max_steps is not None else -1,
            seed=self.random_state,
            data_seed=self.random_state,
            fp16=torch.cuda.is_available() and not torch.cuda.is_bf16_supported(),
            bf16=torch.cuda.is_available() and torch.cuda.is_bf16_supported(),
            gradient_checkpointing=True,
            report_to=[],
            eval_strategy="steps",
            remove_unused_columns=False,
        )

        # Scale per-example causal losses using the configured relation weights.
        class WeightedCausalTrainer(Trainer):
            def compute_loss(self, model: Any, inputs: Dict[str, Any], return_outputs: bool = False, **kwargs: Any) -> Any:
                sample_weight = inputs.pop("sample_weight", None)
                labels = inputs.pop("labels")
                outputs = model(**inputs)
                logits = outputs.logits
                shift_logits = logits[..., :-1, :].contiguous()
                shift_labels = labels[..., 1:].contiguous()
                token_loss = functional.cross_entropy(
                    shift_logits.view(-1, shift_logits.size(-1)),
                    shift_labels.view(-1),
                    ignore_index=-100,
                    reduction="none",
                ).view(shift_labels.shape)
                mask = shift_labels.ne(-100)
                per_sample_loss = (token_loss * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)
                if sample_weight is None:
                    sample_weight = torch.ones_like(per_sample_loss)
                else:
                    sample_weight = sample_weight.to(per_sample_loss.device, dtype=per_sample_loss.dtype)
                loss = (per_sample_loss * sample_weight).sum() / sample_weight.sum().clamp(min=1e-6)
                return (loss, outputs) if return_outputs else loss

        trainer = WeightedCausalTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            data_collator=self._CausalJsonCollator(tokenizer.pad_token_id),
        )
        adapter_dir.mkdir(parents=True, exist_ok=True)
        resume = self._resolve_resume_checkpoint(adapter_dir)
        train_result = trainer.train(resume_from_checkpoint=resume)
        trainer.save_model(str(adapter_dir))
        tokenizer.save_pretrained(str(adapter_dir))
        return {
            "base_model": base_model,
            "adapter_dir": str(adapter_dir.resolve()),
            "train_rows": len(train_rows),
            "eval_rows": len(eval_rows),
            "global_step": int(train_result.global_step),
            "training_loss": float(train_result.training_loss),
        }


    class _AdapterGenerator:
        """Load a fine-tuned 4-bit QLoRA adapter for ontology inference."""
        def __init__(self, learner: "BigDipperAIPrimitiveLearner", base_model: str, adapter_dir: Path, local_files_only: bool = False) -> None:
            """Load the pretrained model, tokenizer, and trained LoRA adapter."""
            self.learner = learner
            import torch
            from peft import PeftModel
            from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

            if not torch.cuda.is_available():
                raise RuntimeError("4-bit adapter inference requires CUDA. Use a base model on CPU for smoke tests.")
            if not adapter_dir.is_dir():
                raise FileNotFoundError(f"Adapter directory does not exist: {adapter_dir}")
            self.tokenizer = AutoTokenizer.from_pretrained(
                base_model,
                trust_remote_code=True,
                local_files_only=local_files_only,
            )
            if self.tokenizer.pad_token_id is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            compute_dtype = torch.bfloat16 if torch.cuda.is_available() and torch.cuda.is_bf16_supported() else torch.float16
            model = AutoModelForCausalLM.from_pretrained(
                base_model,
                trust_remote_code=True,
                local_files_only=local_files_only,
                device_map="auto",
                torch_dtype="auto",
                quantization_config=BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_compute_dtype=compute_dtype,
                    bnb_4bit_use_double_quant=True,
                ),
            )
            self.model = PeftModel.from_pretrained(model, str(adapter_dir), local_files_only=True)
            self.model.eval()
            if torch.cuda.is_available():
                torch.cuda.empty_cache()

        def generate(self, item: Dict[str, Any], max_new_tokens: Optional[int] = None) -> str:
            """Generate ontology JSON using greedy adapter decoding."""
            import torch

            messages = [
                {"role": "system", "content": self.learner.system_prompt},
                {"role": "user", "content": self.learner.build_construction_prompt(item)},
            ]
            text = self.learner._apply_chat_template_json(self.tokenizer, messages, enable_thinking=False)
            inputs = self.tokenizer(
                [text],
                return_tensors="pt",
                truncation=True,
                max_length=self.learner.max_input_tokens,
            ).to(next(self.model.parameters()).device)
            with torch.inference_mode():
                output_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens if max_new_tokens is not None else self.learner.max_output_tokens,
                    do_sample=False,
                    num_beams=1,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                )
            generated = output_ids[0][inputs.input_ids.shape[1] :]
            return self.tokenizer.decode(generated, skip_special_tokens=True).strip()


    def _attempt_record(self, attempt: int, result: Any) -> Dict[str, Any]:
        """Summarize one JSON parsing attempt for inference logs."""
        return {
            "attempt": attempt,
            "parse_error": result.hard_error,
            "parse_soft_errors": list(result.soft_errors),
            "raw_length": result.raw_length,
            "salvaged_count": result.salvaged_count,
            "sft_rows": len(result.rows),
        }

    def _rows_and_fusion(
        self,
        item: Dict[str, Any],
        parse_result: Any,
        graph_index: Dict[str, Any],
    ) -> Tuple[List[BigDipperAIPrimitiveLearner.ScoredTriple], List[Tuple[str, str, str]], List[Dict[str, Any]]]:
        """Combine parsed model triples with graph completion and filtering."""
        rows = list(parse_result.rows)
        rows.extend(self.build_graph_completion_candidates(item, graph_index, parse_result.rows))
        triples, accepted_log = self.fuse_candidates(item, rows)
        return rows, triples, accepted_log


    def _predict_items(
        self,
        items: Sequence[Dict[str, Any]],
        graph_index: Dict[str, Any],
        generator: Any,
        retry_output_tokens: int = 3072,
    ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """Generate construction triples with retry and candidate fusion."""
        triples_by_id = {}
        logs = []
        for item_index, item in enumerate(items):
            started = time.time()
            raw_text = generator.generate(item)
            result = self.parse_model_output(raw_text)
            attempts = [self._attempt_record(1, result)]
            retry_reason = ""
            # Retry malformed JSON once with the larger generation budget.
            if result.hard_error:
                retry_reason = "parse_error"
                retry_text = generator.generate(item, retry_output_tokens)
                retry_result = self.parse_model_output(retry_text)
                attempts.append(self._attempt_record(2, retry_result))
                if retry_result.rows or not retry_result.hard_error:
                    raw_text = retry_text
                    result = retry_result

            rows, triples, accepted_log = self._rows_and_fusion(item, result, graph_index)
            attempts[-1]["final_count"] = len(triples)
            # Also retry valid JSON when all candidates are rejected by fusion.
            if not triples and not retry_reason:
                retry_reason = "empty_output"
                retry_text = generator.generate(item, retry_output_tokens)
                retry_result = self.parse_model_output(retry_text)
                retry_rows, retry_triples, retry_log = self._rows_and_fusion(item, retry_result, graph_index)
                attempt = self._attempt_record(2, retry_result)
                attempt["final_count"] = len(retry_triples)
                attempts.append(attempt)
                if retry_triples or (result.hard_error and not retry_result.hard_error):
                    raw_text = retry_text
                    result = retry_result
                    rows = retry_rows
                    triples = retry_triples
                    accepted_log = retry_log

            triples_by_id[item["id"]] = triples
            source_counts = Counter(
                row.get("source", "diagnostics")
                for row in accepted_log
                if "triple" in row
            )
            logs.append(
                {
                    "id": item["id"],
                    "item_index": item_index,
                    "final_count": len(triples),
                    "candidate_count": len(rows),
                    "source_counts": dict(source_counts),
                    "parse_error": result.hard_error,
                    "parse_soft_errors": list(result.soft_errors),
                    "raw_length": result.raw_length,
                    "salvaged_count": result.salvaged_count,
                    "attempt_count": len(attempts),
                    "retry_reason": retry_reason,
                    "attempts": attempts,
                    "seconds": time.time() - started,
                    "triples": accepted_log,
                    "raw_text": raw_text,
                }
            )
        return self._prediction_payload(items, triples_by_id), {
            "items": logs,
            "summary": self._summarize_logs(logs),
        }


    def _summarize_logs(self, logs: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
        """Aggregate generation, parsing, and triple-count diagnostics."""
        if not logs:
            return {"items": 0}
        counts = [int(row["final_count"]) for row in logs]
        seconds = [float(row["seconds"]) for row in logs]
        sources: Counter[str] = Counter()
        for row in logs:
            sources.update(row["source_counts"])
        return {
            "items": len(logs),
            "parse_failures": sum(1 for row in logs if row["parse_error"]),
            "parse_soft_failures": sum(1 for row in logs if row["parse_soft_errors"]),
            "retried_items": sum(1 for row in logs if int(row["attempt_count"]) > 1),
            "salvaged_triples": sum(int(row["salvaged_count"]) for row in logs),
            "empty_outputs": sum(1 for count in counts if count == 0),
            "avg_seconds": statistics.mean(seconds),
            "median_seconds": statistics.median(seconds),
            "avg_final_triples": statistics.mean(counts),
            "median_final_triples": statistics.median(counts),
            "final_triples_min": min(counts),
            "final_triples_max": max(counts),
            "final_triples_distribution": dict(sorted(Counter(counts).items())),
            "source_counts": dict(sources.most_common()),
        }


    # Use the same prompt and greedy decoding for base-model inference.
    class _BaseGenerator:
        """Generate ontology triples with a pretrained model without an adapter."""

        def __init__(
            self,
            learner: "BigDipperAIPrimitiveLearner",
            base_model: str,
            device: str = "cpu",
            local_files_only: bool = False,
            max_input_tokens: int = 3072,
            max_output_tokens: int = 1536,
        ) -> None:
            """Load a pretrained model without an adapter for development."""
            self.learner = learner
            import torch
            from transformers import AutoModelForCausalLM, AutoTokenizer

            self.tokenizer = AutoTokenizer.from_pretrained(
                base_model, trust_remote_code=True, local_files_only=local_files_only
            )
            if self.tokenizer.pad_token_id is None:
                self.tokenizer.pad_token = self.tokenizer.eos_token

            dtype = torch.float32 if device == "cpu" else (
                torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                base_model,
                trust_remote_code=True,
                local_files_only=local_files_only,
                torch_dtype=dtype,
            ).to(device)
            self.model.eval()
            self.device = device
            self.max_input_tokens = max_input_tokens
            self.max_output_tokens = max_output_tokens

        def generate(self, item: Dict[str, Any], max_new_tokens: Optional[int] = None) -> str:
            """Generate ontology JSON with greedy base-model decoding."""
            import torch

            messages = [
                {"role": "system", "content": self.learner.system_prompt},
                {"role": "user", "content": self.learner.build_construction_prompt(item)},
            ]
            text = self.learner._apply_chat_template_json(self.tokenizer, messages, enable_thinking=False)
            inputs = self.tokenizer(
                [text], return_tensors="pt", truncation=True,
                max_length=self.max_input_tokens,
            ).to(self.device)
            with torch.inference_mode():
                output_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens if max_new_tokens is not None else self.max_output_tokens,
                    do_sample=False,
                    num_beams=1,
                    pad_token_id=self.tokenizer.pad_token_id,
                    eos_token_id=self.tokenizer.eos_token_id,
                )
            generated = output_ids[0][inputs.input_ids.shape[1]:]
            return self.tokenizer.decode(generated, skip_special_tokens=True).strip()