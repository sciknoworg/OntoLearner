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

"""
BigDipperAI learner for primitive ontology construction.

This implementation integrates the original BigDipperAI submission to the
LLMs4OL 2026 competition into the OntoLearner framework.

The submitted data processing, relation-weighted QLoRA training, ontology
generation, graph completion, and candidate fusion methodologies are
preserved while adapting the implementation to OntoLearner's
PrimitiveOntologyLearner interface.
"""

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


# BigDipperAI prompting, parsing, candidate selection, and validation.
Triple = Tuple[str, str, str]
PROMPT_VERSION = "task-a-sft-graph-v1"

ALLOWED_RELATIONS = [
    "is-a",
    "instance-of",
    "is defined by",
    "equivalent class",
    "disjoint with",
    "type",
    "exact match",
    "tree view",
    "part_of",
    "has part",
    "database_cross_reference",
    "see also",
    "same as",
    "range",
    "is_conjugate_base_of",
    "is_conjugate_acid_of",
    "derives from",
    "develops_from",
    "broader",
    "domain",
    "located in",
    "has role",
    "term replaced by",
    "positively regulates",
    "regulates",
    "overlaps",
    "ro_0002473",
    "ro_0002220",
]

BAD_ENTITY_KEYS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "be",
    "by",
    "for",
    "from",
    "group",
    "groups",
    "he",
    "her",
    "his",
    "in",
    "including",
    "is",
    "it",
    "its",
    "la",
    "of",
    "or",
    "she",
    "that",
    "the",
    "their",
    "them",
    "these",
    "they",
    "this",
    "those",
    "type",
    "value",
    "category",
    "categories",
    "class",
    "classes",
    "system",
    "systems",
    "taxonomy",
    "taxonomies",
    "domain",
    "domains",
    "field",
    "fields",
    "method",
    "methods",
    "was",
    "were",
    "which",
    "who",
    "whose",
    "with",
    "within",
}

FUSION_BAD_ENTITIES = {
    "a",
    "an",
    "the",
    "this",
    "that",
    "these",
    "those",
    "which",
    "which itself",
    "it",
    "its",
    "they",
    "them",
    "one",
    "role",
    "order",
    "realm",
    "key",
    "structural",
    "composition",
    "category",
    "categories",
    "class",
    "classes",
    "group",
    "groups",
    "system",
    "systems",
}

BOUNDARY_WORDS = (
    "the",
    "a",
    "an",
    "this",
    "that",
    "these",
    "those",
    "where",
    "when",
    "while",
    "as",
    "in",
    "within",
    "across",
    "among",
    "for",
    "to",
    "of",
    "by",
    "with",
    "including",
    "include",
    "includes",
    "contains",
    "contain",
    "encompasses",
    "encompass",
)

SOURCE_WEIGHTS = {"sft": 1.0, "graph_completion": 0.92}
SOURCE_MIN_SCORES = {"sft": 0.5, "graph_completion": 0.86}
RELATION_MIN_SCORES = {
    "default": 0.95,
    "disjoint with": 0.9,
    "equivalent class": 0.9,
    "instance-of": 0.7,
    "is defined by": 0.84,
    "is-a": 0.5,
    "type": 0.9,
}
RELATION_CAPS = {
    "default": 4,
    "disjoint with": 2,
    "equivalent class": 2,
    "has part": 4,
    "instance-of": 32,
    "is defined by": 4,
    "is-a": 32,
    "part_of": 4,
    "see also": 4,
    "type": 2,
}
MAX_TRIPLES_PER_ITEM = 48



# BigDipperAI Task A and optional Task B training supervision.
DEV_RATIO = 0.2
DEV_SALT = "llms4ol-task-a-baseline-v1"
FOLD_COUNT = 5
FOLD_SALT = "llms4ol-task-a-sft-fold-v1"

# Submitted weighted QLoRA and adapter inference using in-memory records.
DEFAULT_BASE_MODEL = "Qwen/Qwen3-8B"
MAX_INPUT_TOKENS = 3072
MAX_OUTPUT_TOKENS = 1536
RETRY_OUTPUT_TOKENS = 3072
LORA_R = 32
LORA_ALPHA = 64
LORA_DROPOUT = 0.05
LEARNING_RATE = 0.0002
NUM_TRAIN_EPOCHS = 3.0
RELATION_WEIGHTS = {"instance-of": 3.0, "type": 3.0, "default": 1.0}
RELATION_WEIGHT_MAX = 3.0
TARGET_MODULES = [
    "q_proj",
    "k_proj",
    "v_proj",
    "o_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
]


class BigDipperAILearner(PrimitiveOntologyLearner):
    """Generate primitive ontology triples with the BigDipperAI method.

    The original training uses Task A labels and optional aligned Task B
    labels for relation-weighted 4-bit QLoRA. With ``train_adapter=False``, fit
    prepares the same training supervision and Task A graph index without
    training. This development path is not an equivalent trained checkpoint.

    """
    def __init__(
        self,
        model_id: str = DEFAULT_BASE_MODEL,
        auxiliary_data: Optional[Sequence[Dict[str, Any]]] = None,
        device: str = "cuda",
        train_adapter: bool = True,
        adapter_path: Optional[str] = None,
        output_dir: str = "./results/bigdipperai",
        local_files_only: bool = False,
        max_input_tokens: int = MAX_INPUT_TOKENS,
        max_output_tokens: int = MAX_OUTPUT_TOKENS,
        retry_output_tokens: int = RETRY_OUTPUT_TOKENS,
        max_train_samples: Optional[int] = None,
        max_eval_samples: Optional[int] = None,
        max_steps: Optional[int] = None,
    ) -> None:
        """
        Configure the learner and initialize training and inference state.

        Args:
            model_id: Hugging Face base model ID or local path.
            auxiliary_data: Optional labeled Task B Reuse records.
            device: Model device for base-model inference.
            train_adapter: Whether to train the original weighted QLoRA adapter.
            adapter_path: Optional existing trained adapter directory; skips training.
            output_dir: Directory for adapter and optional training artifacts.
            local_files_only: Only use locally cached model files.
            max_input_tokens: Maximum input tokens; 3072 in the submission.
            max_output_tokens: Initial generation budget; 1536 in the submission.
            retry_output_tokens: Retry generation budget; 3072 in the submission.
            max_train_samples: Optional training subset for smoke tests.
            max_eval_samples: Optional evaluation subset for training diagnostics.
            max_steps: Optional training steps limit for tests.

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

        self.generator = None
        self.graph_index: Dict[str, Any] = {}
        self.train_rows: List[Dict[str, Any]] = []
        self.training_summary: Dict[str, Any] = {}
        self.inference_log: Dict[str, Any] = {}

    def load(self, model_id: Optional[str] = None, adapter_path: Optional[str] = None) -> None:
        """Load a trained adapter or a smaller base model for development."""
        if model_id is not None:
            self.model_id = model_id
        if adapter_path is not None:
            self.adapter_path = Path(adapter_path)
            self._existing_adapter = True

        if self.adapter_path is not None:
            self.generator = self.AdapterGenerator(
                self, self.model_id, self.adapter_path, self.local_files_only
            )
        elif not self.train_adapter:
            self.generator = self.BaseGenerator(
                self, self.model_id,
                device=self.device,
                local_files_only=self.local_files_only,
                max_input_tokens=self.max_input_tokens,
                max_output_tokens=self.max_output_tokens,
            )

    @staticmethod
    def _normalize_record(sample: Dict[str, Any]) -> Dict[str, Any]:
        """Adapt OntoLearner's document records to the submitted context schema."""
        result = dict(sample)
        if "context" not in result:
            documents = sample.get("documents", [])
            result["context"] = "\n\n".join(document["text"] for document in documents)
        if not isinstance(result.get("id"), str) or not isinstance(result.get("context"), str):
            raise ValueError("Each record must have string 'id' and document text.")
        return result

    def _ontology_construction(self, data: Any, test: bool = False) -> Optional[Any]:
        """Fit on labeled records or infer ontology triples from documents."""
        if test:
            return self._construct_ontologies(data)
        self._prepare_training_data(data)
        return None

    def _prepare_training_data(self, data: Any) -> None:
        """Prepare original Task A and optional schema-aligned Task B supervision."""
        samples = data if isinstance(data, (list, tuple)) else [data]
        task_a = [self._normalize_record(sample) for sample in samples]
        if not task_a:
            raise ValueError("Training requires at least one labeled Task A record.")
        for sample in task_a:
            if "primitive-ontology-triples" not in sample:
                raise ValueError("Task A training records require 'primitive-ontology-triples'.")

        task_b = [self._normalize_record(sample) for sample in self.auxiliary_data or []]
        task_a_rows = [self._task_a_record(sample) for sample in task_a]
        task_b_rows, task_b_metadata = self._convert_task_b_items(task_b)
        # Keep auxiliary samples in the training rows, not in graph completion.
        mixed_rows = task_a_rows + task_b_rows
        ids = [row["id"] for row in mixed_rows]
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate ID in combined training records.")

        self.train_rows = mixed_rows
        self.graph_index = self._build_graph_index(task_a)
        self.training_summary = {
            "task_a_rows": len(task_a_rows),
            "task_a_dev_rows": sum(row["split"] == "dev" for row in task_a_rows),
            "mixed_train_rows": len(mixed_rows),
            "allowed_relations": ALLOWED_RELATIONS,
            **task_b_metadata,
        }

        # Full QLoRA training is optional; the CPU path prepares data only.
        if self.train_adapter and not self._existing_adapter:
            if not self.device.startswith("cuda"):
                raise RuntimeError("Original weighted 4-bit QLoRA training requires a CUDA device.")
            eval_rows = [row for row in task_a_rows if row["split"] == "dev"]
            if not eval_rows:
                raise ValueError(
                    "No Task A development records selected by the submitted fold algorithm. "
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
        """Generate and validate ontology triples with the submitted pipeline."""
        if self.generator is None:
            raise RuntimeError("Call load() before predict(), or fit() with train_adapter=True.")
        if not self.graph_index:
            raise RuntimeError("Call fit() with Task A training annotations before predict().")
        samples = data if isinstance(data, (list, tuple)) else [data]
        items = [self._normalize_record(sample) for sample in samples]
        predictions, self.inference_log = self._predict_items(
            items, self.graph_index, self.generator,
            retry_output_tokens=self.retry_output_tokens,
        )
        errors = self._validate_prediction_payload(
            predictions,
            expected_ids=[item["id"] for item in items],
            require_order=True,
        )
        if errors:
            raise RuntimeError("Prediction validation failed: " + "; ".join(errors[:10]))
        return predictions

    @dataclass
    class ParseResult:
        """Store parsed ontology triples and model-output diagnostics."""
        rows: List["ScoredTriple"]
        hard_error: str = ""
        soft_errors: Tuple[str, ...] = ()
        raw_length: int = 0
        salvaged_count: int = 0


    @dataclass
    class ScoredTriple:
        """Represent a candidate ontology edge with its provenance and score."""
        triple: Triple
        source: str
        score: float
        evidence: str = ""
        entity_presence: str = "ontology_prior"


    def _build_prompt(self, item: Dict[str, Any]) -> str:
        """Build the constrained JSON extraction prompt for a Task A item.

        Args:
            item: Task A record with an ID and text context.

        Returns:
            JSON-encoded prompt with permitted relations and output schema.
        """
        schema = {"primitive-ontology-triples": [["subject", "relation", "object"]]}
        instructions = [
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
        # Keep the extraction instructions and output schema in the prompt payload.
        payload = {
            "prompt_version": PROMPT_VERSION,
            "instructions": instructions,
            "allowed_relations": ALLOWED_RELATIONS,
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
        """Format messages using the model chat template.

        Args:
            tokenizer: Model tokenizer used to format messages.
            messages: System and user chat messages.
            enable_thinking: Whether to enable the Qwen thinking format.

        Returns:
            Formatted prompt text.
        """
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


    def _norm_key(self, text: str) -> str:
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
        normalized = self._norm_key(entity)
        compact = self._compact_key(entity)
        if normalized and normalized in self._norm_key(context):
            return 0.7
        if compact and compact in self._compact_key(context):
            return 0.58
        return 0.0


    def _triples_from_item(self, item: Dict[str, Any]) -> List[Triple]:
        """Extract well-formed Task A ground-truth triples from a record."""
        rows: List[Triple] = []
        for triple in item.get("primitive-ontology-triples", []):
            if isinstance(triple, list) and len(triple) == 3:
                values = tuple(str(value).strip() for value in triple)
                if all(values):
                    rows.append(values)  # type: ignore[arg-type]
        return rows


    def _serialize_triples(self, triples: Iterable[Triple]) -> List[List[str]]:
        """Convert triple tuples to JSON-compatible triple lists."""
        return [[subject, relation, obj] for subject, relation, obj in triples]


    def _relation_counts(self, triples: Sequence[Triple]) -> Dict[str, int]:
        """Count the relation types in a sequence of triples."""
        return dict(Counter(relation for _, relation, _ in triples).most_common())


    def _clean_entity(self, text: str) -> str:
        """Remove generic boundary text and punctuation from an entity."""
        text = re.sub(r"\s+", " ", text).strip()
        text = text.strip(" .,:;[]{}\"'")
        text = re.sub(r"^(?:" + "|".join(BOUNDARY_WORDS) + r")\s+", "", text, flags=re.I)
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
        """Convert common relation aliases to submitted relation names."""
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
        if self._norm_key(raw) in BAD_ENTITY_KEYS:
            return False
        noise = {"in", "of", "to", "as", "by", "on", "or", "is", "be", "we", "he", "me", "my", "no", "so", "up"}
        if key in noise:
            return False
        if relation not in {"is-a", "instance-of", "type"}:
            return False
        if relation == "is-a" and self._norm_key(other) in {"atom", "element"}:
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
        key = self._norm_key(entity)
        if key and key in BAD_ENTITY_KEYS:
            return False
        if len(re.findall(r"\S+", entity)) > 20:
            return False
        return True


    def _clean_candidate_triple(self, triple: Triple) -> Optional[Triple]:
        """Normalize a triple and reject unsupported relations or entities."""
        subject = self._clean_entity(str(triple[0]))
        relation = self._repair_relation(str(triple[1]))
        obj = self._clean_entity(str(triple[2]))
        if relation not in set(ALLOWED_RELATIONS):
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


    def _coerce_triple(self, row: Any) -> Optional[Triple]:
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


    def _dedupe_scored(self, rows: Iterable[ScoredTriple]) -> List[ScoredTriple]:
        """Keep the highest-scoring row for each distinct triple."""
        best: Dict[Triple, ScoredTriple] = {}
        for row in rows:
            if row.triple not in best or row.score > best[row.triple].score:
                best[row.triple] = row
        return list(best.values())


    def _salvage_model_triples(self, text: str) -> List[ScoredTriple]:
        """Recover valid triple arrays when the full JSON cannot be parsed."""
        decoder = json.JSONDecoder()
        rows: List[ScoredTriple] = []
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


    def _parse_model_output(self, text: str) -> ParseResult:
        """Parse and validate model-generated ontology triples.

        Args:
            text: Raw model generation, possibly with malformed JSON.

        Returns:
            Validated scored triples together with parsing diagnostics.
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
        rows: List[ScoredTriple] = []
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


    def _classify_entity_presence(self, triple: Triple, context: str) -> str:
        """Classify whether a candidate entity occurs in the source text."""
        subject, _, obj = triple
        subject_presence = self._entity_presence(subject, context)
        object_presence = self._entity_presence(obj, context)
        if subject_presence >= 0.86 and object_presence >= 0.86:
            return "text_span"
        if subject_presence >= 0.58 or object_presence >= 0.58:
            return "normalized_text_span"
        return "ontology_prior"


    def _build_graph_completion_candidates(
        self,
        item: Dict[str, Any],
        graph_index: Dict[str, Any],
        seed_rows: Sequence[ScoredTriple],
    ) -> List[ScoredTriple]:
        """Recover supported self-edges from the Task A training graph.

        Args:
            item: Inference record containing its source context.
            graph_index: Entity and triple-frequency index from Task A training labels.
            seed_rows: Parsed triples used to identify relevant entities.

        Returns:
            Deduplicated graph-completion candidates with scores.
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
        # Only recover self-edges observed in the Task A training graph.
        for record in graph_index.get("triple_counts", []):
            triple = (record["subject"], record["relation"], record["object"])
            count = int(record["count"])
            subject, relation, obj = triple
            if subject != obj or relation not in set(ALLOWED_RELATIONS) or count < 1:
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


    def _presence_bonus(self, triple: Triple, context: str) -> float:
        """Assign a small score bonus for entities found in the text."""
        subject, _, obj = triple
        return 0.04 * self._entity_presence(subject, context) + 0.04 * self._entity_presence(obj, context)


    def _relation_rank_key(self, row: ScoredTriple) -> Tuple[float, float]:
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


    def _fuse_candidates(
        self,
        item: Dict[str, Any],
        rows: Sequence[ScoredTriple],
    ) -> Tuple[List[Triple], List[Dict[str, Any]]]:
        """Filter, score, and cap candidates from model and graph sources.

        Args:
            item: Inference record containing its source context.
            rows: Candidate triples with source labels and initial scores.

        Returns:
            Accepted triples and per-candidate diagnostic records.
        """
        # Apply source-specific thresholds before selecting the strongest triple.
        best: Dict[Triple, ScoredTriple] = {}
        rejected: Counter[str] = Counter()
        for row in rows:
            cleaned = self._clean_candidate_triple(row.triple)
            if cleaned is None:
                rejected["invalid"] += 1
                continue
            if self._norm_key(cleaned[0]) in FUSION_BAD_ENTITIES or self._norm_key(cleaned[2]) in FUSION_BAD_ENTITIES:
                rejected["bad_entity"] += 1
                continue
            weighted = row.score * SOURCE_WEIGHTS.get(row.source, 1.0)
            required = max(
                SOURCE_MIN_SCORES.get(row.source, 0.0),
                RELATION_MIN_SCORES.get(cleaned[1], RELATION_MIN_SCORES["default"]),
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
            cap = RELATION_CAPS.get(relation, RELATION_CAPS["default"])
            if caps[relation] >= cap:
                rejected["relation_cap"] += 1
                continue
            accepted.append(row)
            caps[relation] += 1
            if len(accepted) >= MAX_TRIPLES_PER_ITEM:
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
        triples_by_id: Dict[str, List[Triple]],
    ) -> List[Dict[str, Any]]:
        """Produce OntoLearner prediction dictionaries in input order."""
        return [
            {
                "id": item["id"],
                "primitive-ontology-triples": self._serialize_triples(triples_by_id.get(item["id"], [])),
            }
            for item in items
        ]


    def _validate_prediction_payload(
        self,
        payload: Any,
        expected_ids: Optional[Sequence[str]] = None,
        require_order: bool = True,
    ) -> List[str]:
        """Validate output IDs, triple shape, and permitted relations.

        Args:
            payload: Generated prediction dictionaries.
            expected_ids: Optional expected document IDs.
            require_order: Whether predicted IDs must preserve input order.

        Returns:
            Validation error messages, or an empty list for valid output.
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
                if triple[1] not in set(ALLOWED_RELATIONS):
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
        """Assign the original hash-based development split to a Task A item."""
        digest = hashlib.md5(f"{DEV_SALT}:{item_id}".encode("utf-8")).hexdigest()
        bucket = int(digest[:8], 16) / 0xFFFFFFFF
        return "dev" if bucket < DEV_RATIO else "train"

    def _fold_for_id(self, item_id: str) -> int:
        """Assign a deterministic data fold from the item ID."""
        digest = hashlib.md5(f"{FOLD_SALT}:{item_id}".encode("utf-8")).hexdigest()
        return int(digest[:8], 16) % FOLD_COUNT

    def _task_a_record(self, item: Dict[str, Any]) -> Dict[str, Any]:
        """Convert a labeled Task A sample into supervised JSON training data."""
        triples = self._triples_from_item(item)
        return {
            "id": item["id"],
            "split": self._stable_dev_split(item["id"]),
            "fold": self._fold_for_id(item["id"]),
            "prompt": self._build_prompt(item),
            "target_json": json.dumps(
                {"primitive-ontology-triples": self._serialize_triples(triples)},
                ensure_ascii=False,
                separators=(",", ":"),
            ),
            "relation_counts": self._relation_counts(triples),
            "gold_triple_count": len(triples),
        }

    def _coerce_task_b_triple(self, row: Any) -> Triple | None:
        """Convert one Task B triple to a validated string tuple."""
        if not isinstance(row, list) or len(row) != 3:
            return None
        values = tuple(str(value).strip() for value in row)
        if not all(values):
            return None
        return values  # type: ignore[return-value]

    def _clean_task_b_triples(self, groups: Sequence[Iterable[Any]]) -> Tuple[List[Triple], Dict[str, int], int]:
        """Merge and deduplicate permitted initial and extended Task B triples."""
        allowed = set(ALLOWED_RELATIONS)
        dropped: Counter[str] = Counter()
        seen = set()
        triples = []
        duplicate_count = 0
        for group in groups:
            for row in group:
                triple = self._coerce_task_b_triple(row)
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

    def _convert_task_b_items(self, items: Sequence[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """Adapt Task B labels as auxiliary Task A training examples.

        Args:
            items: Normalized Reuse records with initial and extended ontology triples.

        Returns:
            Auxiliary supervised rows and relation-filtering metadata.
        """
        rows = []
        dropped_relations: Counter[str] = Counter()
        kept_relations: Counter[str] = Counter()
        duplicate_triples = 0
        empty_targets = 0
        # Reuse both initial and extended Task B triples as auxiliary supervision.
        for item in items:
            triples, dropped, duplicate_count = self._clean_task_b_triples(
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
            item_id = f"task_b_reuse:{item['id']}"
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
                    "source_task": "task_b_reuse_as_task_a_aux",
                    "prompt": self._build_prompt(prompt_item),
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
            "task_b_items": len(items),
            "task_b_aux_rows": len(rows),
            "task_b_kept_triples": sum(row["gold_triple_count"] for row in rows),
            "task_b_duplicate_triples_removed": duplicate_triples,
            "task_b_empty_targets": empty_targets,
            "task_b_kept_relation_counts": dict(sorted(kept_relations.items())),
            "task_b_dropped_relation_counts": dict(sorted(dropped_relations.items())),
        }
        return rows, metadata


    def _build_graph_index(self, items: Sequence[Dict[str, Any]]) -> Dict[str, Any]:
        """Build the original graph index using Task A training annotations only."""
        triple_counts: Counter[Triple] = Counter()
        entity_forms: Dict[str, Counter[str]] = defaultdict(Counter)
        # Index only the labeled Task A records, not auxiliary Task B examples.
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
        """Weight training samples by the frequency of rare relation types."""
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
            count * RELATION_WEIGHTS.get(relation, RELATION_WEIGHTS["default"])
            for relation, count in clean_counts.items()
        )
        return min(RELATION_WEIGHT_MAX, max(1.0, weighted / total))


    class CausalJsonCollator:
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
        base_model: str = DEFAULT_BASE_MODEL,
        local_files_only: bool = False,
        max_train_samples: Optional[int] = None,
        max_eval_samples: Optional[int] = None,
        max_steps: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Fine-tune the submitted relation-weighted 4-bit QLoRA adapter.

        Args:
            train_rows: Prepared Task A and optional auxiliary Task B examples.
            eval_rows: Held-out development examples for evaluation.
            adapter_dir: Directory used for checkpoints and the trained adapter.
            base_model: Pretrained Qwen model ID.
            local_files_only: Whether loading requires already-cached files.
            max_train_samples: Optional training-row limit for development.
            max_eval_samples: Optional evaluation-row limit for development.
            max_steps: Optional override for the training step count.

        Returns:
            Training summary and saved adapter location.
        """
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
            raise RuntimeError("Original 4-bit NF4 QLoRA training requires a CUDA-enabled GPU.")
        set_seed(42)
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
                r=LORA_R,
                lora_alpha=LORA_ALPHA,
                lora_dropout=LORA_DROPOUT,
                bias="none",
                task_type="CAUSAL_LM",
                target_modules=TARGET_MODULES,
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
                {"role": "system", "content": "Return only valid JSON for the ontology extraction task."},
                {"role": "user", "content": row["prompt"]},
            ]
            prompt_text = self._apply_chat_template_json(tokenizer, messages, enable_thinking=False)
            prompt_ids = tokenizer(
                prompt_text,
                truncation=True,
                max_length=MAX_INPUT_TOKENS,
                add_special_tokens=False,
            )["input_ids"]
            target_ids = tokenizer(
                row["target_json"] + tokenizer.eos_token,
                truncation=True,
                max_length=MAX_OUTPUT_TOKENS,
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
            num_train_epochs=NUM_TRAIN_EPOCHS,
            learning_rate=LEARNING_RATE,
            per_device_train_batch_size=1,
            per_device_eval_batch_size=1,
            gradient_accumulation_steps=8,
            logging_steps=10,
            save_steps=200,
            eval_steps=200,
            save_total_limit=3,
            max_grad_norm=0.3,
            warmup_steps=0.03,
            max_steps=max_steps if max_steps is not None else -1,
            seed=42,
            data_seed=42,
            fp16=torch.cuda.is_available() and not torch.cuda.is_bf16_supported(),
            bf16=torch.cuda.is_available() and torch.cuda.is_bf16_supported(),
            gradient_checkpointing=True,
            report_to=[],
            eval_strategy="steps",
            remove_unused_columns=False,
        )

        # Scale per-example causal losses using the submitted relation weights.
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
            data_collator=self.CausalJsonCollator(tokenizer.pad_token_id),
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


    class AdapterGenerator:
        """Load a fine-tuned 4-bit QLoRA adapter for ontology inference."""
        def __init__(self, learner: "BigDipperAILearner", base_model: str, adapter_dir: Path, local_files_only: bool = False) -> None:
            """Load the pretrained model, tokenizer, and trained LoRA adapter."""
            self.learner = learner
            import torch
            from peft import PeftModel
            from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

            if not torch.cuda.is_available():
                raise RuntimeError("Original 4-bit adapter inference requires CUDA. Use a base model on CPU for smoke tests.")
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

        def generate(self, item: Dict[str, Any], max_new_tokens: int = MAX_OUTPUT_TOKENS) -> str:
            """Generate ontology JSON using greedy adapter decoding."""
            import torch

            messages = [
                {"role": "system", "content": "Return only valid JSON for the ontology extraction task."},
                {"role": "user", "content": self.learner._build_prompt(item)},
            ]
            text = self.learner._apply_chat_template_json(self.tokenizer, messages, enable_thinking=False)
            inputs = self.tokenizer(
                [text],
                return_tensors="pt",
                truncation=True,
                max_length=MAX_INPUT_TOKENS,
            ).to(next(self.model.parameters()).device)
            with torch.inference_mode():
                output_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
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
    ) -> Tuple[List[ScoredTriple], List[Tuple[str, str, str]], List[Dict[str, Any]]]:
        """Combine parsed model triples with graph completion and filtering."""
        rows = list(parse_result.rows)
        rows.extend(self._build_graph_completion_candidates(item, graph_index, parse_result.rows))
        triples, accepted_log = self._fuse_candidates(item, rows)
        return rows, triples, accepted_log


    def _predict_items(
        self,
        items: Sequence[Dict[str, Any]],
        graph_index: Dict[str, Any],
        generator: Any,
        retry_output_tokens: int = RETRY_OUTPUT_TOKENS,
    ) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
        """Generate and validate Task A triples with the submitted inference flow.

        Args:
            items: Normalized inference records with text contexts.
            graph_index: Task A graph-completion index.
            generator: Initialized base-model or adapter generator.
            retry_output_tokens: Token budget for a failed generation retry.

        Returns:
            Prediction dictionaries and detailed inference diagnostics.
        """
        triples_by_id = {}
        logs = []
        for item_index, item in enumerate(items):
            started = time.time()
            raw_text = generator.generate(item)
            result = self._parse_model_output(raw_text)
            attempts = [self._attempt_record(1, result)]
            retry_reason = ""
            # Retry malformed JSON once with the larger generation budget.
            if result.hard_error:
                retry_reason = "parse_error"
                retry_text = generator.generate(item, retry_output_tokens)
                retry_result = self._parse_model_output(retry_text)
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
                retry_result = self._parse_model_output(retry_text)
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


    # CPU development inference retains the submitted prompt and greedy decoder.
    class BaseGenerator:
        """Run the original prompting and decoding algorithm without an adapter."""

        def __init__(
            self,
            learner: "BigDipperAILearner",
            base_model: str,
            device: str = "cpu",
            local_files_only: bool = False,
            max_input_tokens: int = MAX_INPUT_TOKENS,
            max_output_tokens: int = MAX_OUTPUT_TOKENS,
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
                {"role": "system", "content": "Return only valid JSON for the ontology extraction task."},
                {"role": "user", "content": self.learner._build_prompt(item)},
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