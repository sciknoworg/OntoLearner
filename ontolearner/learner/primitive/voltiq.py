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
Volt-IQ learner for primitive ontology construction and expansion.

This implementation integrates the executable Volt-IQ submission to the
LLMs4OL 2026 competition into the OntoLearner framework.

The submitted constrained Ollama construction extractor and all seventeen
ontology expansion strategies, including lexical, contextual, memorized,
and OBO/FoodOn-based extensions, are preserved while adapting the
implementation to OntoLearner's PrimitiveOntologyLearner interface.
The final merged construction artifact is not reconstructed by the
published portable extractor.
"""

from __future__ import annotations
import json
import os
import re
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urlparse

from ...base import PrimitiveOntologyLearner

# Volt-IQ ontology_construction prompt, relation map, and conservative extraction constraints.
DEFAULT_OLLAMA_URL = "http://127.0.0.1:11434"
DEFAULT_OLLAMA_MODEL = "qwen3.6:27b"
OLLAMA_JSON_SCHEMA = {
    "type": "object",
    "properties": {
        "triples": {
            "type": "array",
            "items": {
                "type": "array",
                "items": {"type": "string"},
                "minItems": 3,
                "maxItems": 3,
            },
        }
    },
    "required": ["triples"],
}

EXTRACT_SYSTEM = """You are an ontology triple extractor. Extract triples from text as
[subject, predicate, object]. Perform one careful extraction: quality beats quantity.

For every triple, apply this checklist:
1. The subject is a concise noun phrase, not a sentence fragment.
2. The relation is explicitly supported by an exact sentence or clause.
3. The object is a concise noun phrase, not a sentence fragment.
4. Both entities and the relation have specific textual evidence.
5. The triple is not a duplicate.

Predicate rules:
- is-a is the default for class hierarchy: X is a type, kind, or subclass of Y.
  It also applies when the text enumerates several items as types of one category.
- instance-of is only for a unique individual or a numbered instance such as type VI.
- disjoint with requires explicit disjoint or mutually exclusive wording.
- equivalent class requires explicit equivalent-to or same-as wording.
- part_of and has_part require explicit part/component wording.

Entity rules:
- Copy entity names from the text and preserve meaningful punctuation.
- Keep parenthetical qualifiers and long compound names intact.
- Do not split a multi-word entity into unrelated pieces.
- Do not invent generic entities or relations merely because terms co-occur.
- Never emit a self-loop.
- When evidence is vague, omit the candidate.

Return only JSON in this form:
{"triples": [["subject", "predicate", "object"], ...]}"""

EXTRACT_USER = """Extract all ontology triples supported by the following text. Apply
the evidence checklist to every candidate and remain conservative.

Text:
{context}

Return only {{"triples": [["subject", "predicate", "object"], ...]}}."""

PREDICATE_MAP = {
    "is-a": "is-a",
    "is a": "is-a",
    "isa": "is-a",
    "is_a": "is-a",
    "subclass of": "is-a",
    "subclassof": "is-a",
    "type of": "is-a",
    "instance-of": "instance-of",
    "instance of": "instance-of",
    "instanceof": "instance-of",
    "member of": "instance-of",
    "example of": "instance-of",
    "part_of": "part_of",
    "part of": "part_of",
    "partof": "part_of",
    "is part of": "part_of",
    "component of": "part_of",
    "has_part": "has_part",
    "has part": "has_part",
    "haspart": "has_part",
    "contains": "has_part",
    "consists of": "has_part",
    "composed of": "has_part",
    "equivalent to": "equivalent class",
    "equivalent class": "equivalent class",
    "same as": "equivalent class",
    "disjoint": "disjoint with",
    "disjoint with": "disjoint with",
    "located in": "located in",
    "found in": "located in",
    "derives from": "derives from",
    "develops from": "develops_from",
    "develops_from": "develops_from",
    "has role": "has role",
}

GENERIC_ENTITIES = {
    "category",
    "class",
    "concept",
    "concepts",
    "data",
    "different",
    "entities",
    "entity",
    "group",
    "individuals",
    "item",
    "items",
    "kind",
    "object",
    "other",
    "particular",
    "process",
    "several",
    "specific",
    "thing",
    "things",
    "type",
    "types",
    "various",
}

EXPANSION_METHODS = (
    "constrained_lex",
    "context_rules",
    "type_link",
    "hybrid_reuse",
    "memorized_lexical",
    "memorized_lexical_strict",
    "obo_direct",
    "obo_memorized_hybrid",
    "obo_memorized_selective",
    "obo_foodon_hybrid",
    "obo_foodon_selective",
    "obo_foodon_to_direct",
    "obo_foodon_to_terms_only",
    "obo_foodon_to_hybrid",
    "obo_foodon_to_selective",
    "obo_foodon_to_selective_threshold_4",
    "obo_foodon_to_selective_threshold_8",
)

RELATION_CANONICAL = {
    "is a": "is-a",
    "isa": "is-a",
    "instance of": "instance-of",
    "part of": "part_of",
}
EXPANSION_CACHE_DIR = Path(os.environ.get("LLMS4OL_CACHE_DIR", Path.home() / ".cache" / "ontolearner" / "voltiq")) / "expansion"
EXPANSION_OBO_CACHE_DIR = EXPANSION_CACHE_DIR / "obo_probe"
EXPANSION_OWL_CACHE_DIR = EXPANSION_CACHE_DIR / "owl_probe"
EXPANSION_OBO_SOURCE_URLS = {
    "go": "http://current.geneontology.org/ontology/go-basic.obo",
    "cl": "http://purl.obolibrary.org/obo/cl.obo",
    "envo": "http://purl.obolibrary.org/obo/envo.obo",
    "pato": "http://purl.obolibrary.org/obo/pato.obo",
    "uo": "http://purl.obolibrary.org/obo/uo.obo",
    "bfo": "http://purl.obolibrary.org/obo/bfo.obo",
    "obi": "http://purl.obolibrary.org/obo/obi.obo",
    "ro": "http://purl.obolibrary.org/obo/ro.obo",
    "po": "http://purl.obolibrary.org/obo/po.obo",
    "uberon": "http://purl.obolibrary.org/obo/uberon.obo",
    "chebi": "http://purl.obolibrary.org/obo/chebi.obo",
    "mondo": "http://purl.obolibrary.org/obo/mondo.obo",
    "hp": "http://purl.obolibrary.org/obo/hp.obo",
    "doid": "http://purl.obolibrary.org/obo/doid.obo",
    "ncit": "http://purl.obolibrary.org/obo/ncit.obo",
}
EXPANSION_OBO_SOURCE_KEYS = tuple(EXPANSION_OBO_SOURCE_URLS)
EXPANSION_EXTRA_OBO_SOURCE_URLS = {
    "to": "http://purl.obolibrary.org/obo/to.obo",
}
EXPANSION_ALL_OBO_SOURCE_URLS = {
    **EXPANSION_OBO_SOURCE_URLS,
    **EXPANSION_EXTRA_OBO_SOURCE_URLS,
}
EXPANSION_FOODON_TO_SOURCE_KEYS = EXPANSION_OBO_SOURCE_KEYS + ("to",)
EXPANSION_FOODON_OWL_URL = "http://purl.obolibrary.org/obo/foodon.owl"
EXPANSION_FOODON_OWL_PATH = EXPANSION_OWL_CACHE_DIR / "foodon.owl"
OBO_IN_OWL_PREFIX = "http://www.geneontology.org/formats/oboInOwl#"


class VoltIQPrimitiveLearner(PrimitiveOntologyLearner):
    """
    Construct and expand primitive ontologies using Volt-IQ's executable methods.

    Construction applies the submitted conservative Ollama extractor.
    Expansion supports all seventeen submitted strategies; the primary
    F01 method is selected by default.
    """

    EXPANSION_METHODS = EXPANSION_METHODS

    def __init__(
        self,
        model_id: str = DEFAULT_OLLAMA_MODEL,
        base_url: str = DEFAULT_OLLAMA_URL,
        workers: int = 1,
        timeout: float = 600.0,
        expansion_method: str = "obo_foodon_to_terms_only",
        generator: Optional[Any] = None,
    ) -> None:
        """
        Initialize the Volt-IQ learner for primitive ontology construction and expansion.

        Args:
            model_id: Local Ollama model used for ontology construction.
            base_url: Local Ollama endpoint.
            workers: Number of parallel construction requests.
            timeout: Timeout for local inference requests, in seconds.
            expansion_method: Submitted method for ontology expansion.
            generator: Optional generation backend for testing construction.
        """
        super().__init__()
        if expansion_method not in self.EXPANSION_METHODS:
            raise ValueError(f"Unknown ontology expansion method: {expansion_method}")
        self.model_id = model_id
        self.base_url = base_url
        self.workers = workers
        self.timeout = timeout
        self.expansion_method = expansion_method
        self.generator = generator
        self.train_data: Optional[List[Dict[str, Any]]] = None
        self._ollama_opener = None
        self._ollama_checked = False

    def load(self, model_id: Optional[str] = None, generator: Optional[Any] = None, **kwargs: Any) -> None:
        """
        Configure the original local Ollama generator for construction.

        The connection is initialized lazily during construction prediction,
        so expansion can run without an Ollama server.

        Args:
            model_id: Optional installed Ollama model name.
            generator: Optional test generator implementing `generate`.
        """
        if model_id is not None:
            self.model_id = model_id
            self._ollama_checked = False
            self._ollama_opener = None
        if generator is not None:
            self.generator = generator

    def _ontology_construction(self, data: Any, test: bool = False) -> Optional[Any]:
        """Prepare construction records or extract their text-supported triples."""
        records = self.tasks_data_former(data, task="ontology_construction", test=test)
        if not test:
            # The submitted portable construction extractor requires no fine-tuning.
            return None

        if self.generator is None:
            self._initialize_ollama()

        # Original constrained extraction and validation are kept unchanged.
        return self._build_submission(records, workers=self.workers, generator=self.generator)

    def _ontology_expansion(self, data: Any, test: bool = False) -> Optional[Any]:
        """Store expansion supervision or run the selected submitted strategy."""
        records = self.tasks_data_former(data, task="ontology_expansion", test=test)
        if not test:
            for record in records:
                if "extended-primitive-ontology-triples" not in record:
                    raise KeyError("Training requires 'extended-primitive-ontology-triples'.")
            self.train_data = records
            return None
        if self.train_data is None:
            raise RuntimeError("Call fit() with ontology expansion samples before predict().")
        for record in records:
            for field in ("terms", "types", "initial-primitive-ontology-triples"):
                if field not in record:
                    raise KeyError(f"Expansion prediction requires '{field}'.")
        return self._build_extended_predictions_for_method(
            records,
            train_records=self.train_data,
            method=self.expansion_method,
        )

    # Ontology construction: preserve the original constrained extractor.

    def _initialize_ollama(self) -> None:
        """Initialize the local Ollama connection when construction is requested."""
        if self._ollama_checked:
            return
        parsed = urlparse(self.base_url)
        if parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "localhost", "::1"}:
            raise ValueError("ontology construction only permits an offline Ollama endpoint on loopback HTTP.")
        self._ollama_opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        self._require_installed_model()
        self._ollama_checked = True

    def _ollama_request(self, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        """Send an HTTP request to the local Ollama service."""
        data = None if payload is None else json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            f"{self.base_url.rstrip('/')}{path}",
            data=data,
            headers={"Content-Type": "application/json"},
            method="GET" if payload is None else "POST",
        )
        try:
            with self._ollama_opener.open(request, timeout=self.timeout) as response:
                result = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Local Ollama request failed ({exc.code}): {detail}") from exc
        except urllib.error.URLError as exc:
            raise RuntimeError(
                "Local Ollama is unavailable. Start the local Ollama service before ontology construction inference."
            ) from exc
        if not isinstance(result, dict):
            raise RuntimeError("Local Ollama returned an invalid response.")
        return result

    def _require_installed_model(self) -> None:
        """Check that the configured model is available in local Ollama."""
        tags = self._ollama_request("/api/tags").get("models", [])
        installed = {
            value
            for row in tags
            if isinstance(row, dict)
            for value in (row.get("name"), row.get("model"))
            if isinstance(value, str)
        }
        if self.model_id not in installed:
            raise RuntimeError(
                f"Offline model {self.model_id!r} is not installed in Ollama. "
                "Provision the model locally before running this submission."
            )

    def _ollama_generate(self, *, system: str, user: str) -> str:
        """Generate constrained JSON using the original local Ollama settings."""
        response = self._ollama_request(
            "/api/chat",
            {
                "model": self.model_id,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "stream": False,
                "format": OLLAMA_JSON_SCHEMA,
                "options": {"temperature": 0.0},
            },
        )
        message = response.get("message", {})
        content = message.get("content") if isinstance(message, dict) else None
        if not isinstance(content, str):
            raise RuntimeError("Local Ollama response did not contain text content.")
        return content

    def _extract_json_object(self, text: str) -> dict[str, Any]:
        """Parse a JSON object from a direct or fenced model response."""
        if not text:
            return {}
        value = text.strip()
        if value.startswith("```"):
            value = re.sub(r"^```(?:json)?\s*", "", value, flags=re.IGNORECASE)
            value = re.sub(r"\s*```$", "", value)
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, dict) else {}
        except json.JSONDecodeError:
            pass

        decoder = json.JSONDecoder()
        for index, character in enumerate(value):
            if character != "{":
                continue
            try:
                parsed, _ = decoder.raw_decode(value[index:])
            except json.JSONDecodeError:
                continue
            if isinstance(parsed, dict):
                return parsed
        return {}

    def _parse_triples(self, text: str) -> list[list[str]]:
        """Extract well-formed triples from a model response."""
        parsed = self._extract_json_object(text)
        triples = parsed.get("triples", [])
        if not isinstance(triples, list):
            return []

        result = []
        for triple in triples:
            if not isinstance(triple, (list, tuple)) or len(triple) != 3:
                continue
            values = [str(item).strip() for item in triple]
            if all(values):
                result.append(values)
        return result

    def _normalize_predicate(self, predicate: str) -> str:
        """Normalize a generated relation to the submitted predicate vocabulary."""
        value = re.sub(r"\s+", " ", predicate.strip().lower())
        if value in PREDICATE_MAP:
            return PREDICATE_MAP[value]
        if any(word in value for word in ("subclass", "type", "kind", "category")):
            return "is-a"
        if any(word in value for word in ("member", "example", "instance")):
            return "instance-of"
        return ""

    def _entity_is_supported(self, entity: str, context: str) -> bool:
        """Check whether an entity has textual support in the input document."""
        value = entity.strip().lower()
        if len(value) < 2 or len(value) > 200 or value in GENERIC_ENTITIES:
            return False
        if value.startswith(("abstract:", "content:", "title:")):
            return False

        context_lower = context.lower()
        if value in context_lower:
            return True
        content_words = [word for word in re.findall(r"[a-z0-9]+", value) if len(word) >= 4]
        if not content_words:
            return False
        supported = sum(word in context_lower for word in content_words)
        return supported >= max(1, (2 * len(content_words) + 2) // 3)

    def _fix_instance_relations(self, triples: list[list[str]]) -> list[list[str]]:
        """Correct taxonomy and instance relations using the submitted numeric heuristic."""
        result = []
        for subject, predicate, object_value in triples:
            if predicate == "instance-of" and not re.search(r"\d", subject):
                result.append([subject, "is-a", object_value])
                continue
            if predicate == "is-a" and re.search(r"\d", subject):
                stem = re.sub(r"\s+\d+[a-z]?$", "", subject.lower())
                if stem == object_value.lower() or object_value.lower() in stem:
                    result.append([subject, "instance-of", object_value])
                    continue
            result.append([subject, predicate, object_value])
        return result

    def _post_process(self, triples: list[list[str]], context: str) -> list[list[str]]:
        """Normalize predicates, reject unsupported entities, and deduplicate."""
        cleaned = []
        for triple in triples:
            if not isinstance(triple, list) or len(triple) != 3:
                continue
            subject, predicate, object_value = (str(item).strip() for item in triple)
            relation = self._normalize_predicate(predicate)
            if not relation or subject.casefold() == object_value.casefold():
                continue
            if (
                not self._entity_is_supported(subject, context)
                or not self._entity_is_supported(object_value, context)
            ):
                continue
            cleaned.append([subject, relation, object_value])

        seen = set()
        result = []
        for triple in self._fix_instance_relations(cleaned):
            key = (triple[0].casefold(), triple[1], triple[2].casefold())
            if key in seen:
                continue
            seen.add(key)
            result.append(triple)
        return result

    def _extract_triples(
        self,
        context: str,
        *,
        generator: Any | None = None,
        max_retries: int = 3,
    ) -> list[list[str]]:
        """Run one deterministic offline extraction and validate its triples."""
        active_generator = generator if generator is not None else self.generator
        if active_generator is None:
            self._initialize_ollama()
        prompt = EXTRACT_USER.format(context=context)
        last_error: Exception | None = None

        for attempt in range(max_retries):
            try:
                content = (
                    active_generator.generate(system=EXTRACT_SYSTEM, user=prompt)
                    if active_generator is not None
                    else self._ollama_generate(system=EXTRACT_SYSTEM, user=prompt)
                )
                return self._post_process(self._parse_triples(content), context)
            except Exception as exc:
                last_error = exc
                if attempt + 1 < max_retries:
                    time.sleep(2**attempt)

        raise RuntimeError(f"ontology construction extraction failed after {max_retries} attempts") from last_error

    def _build_submission(
        self,
        records: list[dict[str, Any]],
        *,
        workers: int = 1,
        generator: Any | None = None,
    ) -> list[dict[str, Any]]:
        """Predict ontology construction records while preserving the original order and IDs."""
        for index, record in enumerate(records):
            if not isinstance(record, dict) or "id" not in record or "context" not in record:
                raise ValueError(f"ontology construction record {index} must contain id and context")

        active_generator = generator if generator is not None else self.generator
        if active_generator is None:
            self._initialize_ollama()
        predictions: list[dict[str, Any] | None] = [None] * len(records)

        with ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
            futures = {
                executor.submit(
                    self._process_construction_record, index, record, active_generator
                ): index
                for index, record in enumerate(records)
            }
            for future in as_completed(futures):
                index, prediction = future.result()
                predictions[index] = prediction

        if any(prediction is None for prediction in predictions):
            raise RuntimeError("ontology construction did not produce a prediction for every input record")
        return [prediction for prediction in predictions if prediction is not None]

    def _process_construction_record(
        self, index: int, record: dict[str, Any], generator: Any | None
    ) -> tuple[int, dict[str, Any]]:
        """Extract triples for one construction record."""
        triples = self._extract_triples(str(record["context"]), generator=generator)
        return index, {
            "id": record["id"],
            "primitive-ontology-triples": triples,
        }

    # Ontology expansion: original submitted strategies.

    def _normalize_label(self, text: str) -> str:
        """Normalize ontology labels for relation lookup and filtering."""
        value = text.lower().strip()
        value = value.replace("_", " ")
        value = re.sub(r"[^\w\s]", " ", value)
        value = re.sub(r"\s+", " ", value)
        return value.strip()

    def _normalize_relation(self, text: str) -> str:
        """Normalize relation aliases using the submitted canonical map."""
        value = self._normalize_label(text)
        return RELATION_CANONICAL.get(value, value)

    def _token_set(self, text: str) -> set[str]:
        """Return normalized lexical tokens from an ontology label."""
        return {token for token in self._normalize_label(text).split() if token}

    def _clean_context_label(self, text: str) -> str:
        """Clean labels extracted from the document context."""
        value = self._normalize_label(text)
        value = re.sub(
            r"^(within this domain|in this domain|for instance|for example|specifically|similarly|likewise)\s+",
            "",
            value,
        )
        value = re.sub(r"^(the|a|an)\s+", "", value)
        return value.strip()

    def _sentence_split(self, text: str) -> list[str]:
        """Split a document into candidate evidence sentences."""
        value = re.sub(r"\s+", " ", text.replace("\n", " ")).strip()
        return [item.strip() for item in re.split(r"(?<=[.!?])\s+", value) if item.strip()]

    def _split_enumeration(self, text: str) -> list[str]:
        """Extract candidate labels from a coordinated phrase."""
        value = re.sub(r"\s+(?:and|or)\s+", ", ", text.strip(), flags=re.IGNORECASE)
        parts = [self._clean_context_label(part) for part in value.split(",")]
        return [part for part in parts if part]

    def _sanitize_extended_triples(self, triples: list[list[str]], initial_triples: list[list[str]]) -> list[list[str]]:
        """Remove self-loops, duplicates, and existing ontology edges."""
        initial_set = {
            (self._normalize_label(head), self._normalize_relation(relation), self._normalize_label(tail))
            for head, relation, tail in initial_triples
            if all(isinstance(item, str) for item in (head, relation, tail))
        }
        cleaned = []
        seen = set()
        for triple in triples:
            if not isinstance(triple, list) or len(triple) != 3:
                continue
            head, relation, tail = triple
            if not all(isinstance(item, str) for item in (head, relation, tail)):
                continue
            normalized = (self._normalize_label(head), self._normalize_relation(relation), self._normalize_label(tail))
            if not all(normalized) or normalized[0] == normalized[2]:
                continue
            if normalized in initial_set or normalized in seen:
                continue
            seen.add(normalized)
            cleaned.append(list(normalized))
        return sorted(cleaned, key=lambda triple: (triple[0], triple[1], triple[2]))

    def _lexical_parent_score(self, child: str, parent: str, parent_counts: Counter[str]) -> float:
        """Score a lexical type-parent candidate."""
        child_tokens = child.split()
        parent_tokens = parent.split()
        if not child_tokens or not parent_tokens or child == parent:
            return -1.0
        if len(parent_tokens) > len(child_tokens):
            return -1.0
        overlap = len(set(child_tokens) & set(parent_tokens))
        suffix_bonus = 2.0 if child_tokens[-1] == parent_tokens[-1] else 0.0
        substring_bonus = 3.0 if parent in child else 0.0
        length_bonus = 1.0 / max(1, len(child_tokens) - len(parent_tokens) + 1)
        prior_bonus = parent_counts[parent] / max(1, sum(parent_counts.values()))
        return overlap + suffix_bonus + substring_bonus + length_bonus + prior_bonus

    def _memorized_parent_score(self, child: str, parent: str, parent_counts: Counter[str]) -> float:
        """Score type parents with lexical and training-frequency evidence."""
        child_norm = self._normalize_label(child)
        parent_norm = self._normalize_label(parent)
        if not child_norm or not parent_norm or child_norm == parent_norm:
            return -1.0
        child_tokens = child_norm.split()
        parent_tokens = parent_norm.split()
        overlap = len(set(child_tokens) & set(parent_tokens))
        suffix_bonus = 2.0 if child_tokens and parent_tokens and child_tokens[-1] == parent_tokens[-1] else 0.0
        prefix_bonus = 1.0 if child_tokens and parent_tokens and child_tokens[0] == parent_tokens[0] else 0.0
        substring_bonus = 3.0 if parent_norm in child_norm else 0.0
        length_bonus = 1.0 / max(1, len(child_tokens) - len(parent_tokens) + 1)
        prior_bonus = parent_counts[parent_norm] / max(1, sum(parent_counts.values()))
        return overlap + suffix_bonus + prefix_bonus + substring_bonus + length_bonus + prior_bonus

    def _extract_context_is_a_pairs(self, context: str) -> list[tuple[str, str]]:
        """Recover explicit hierarchical pairs from the document context."""
        patterns = [
            re.compile(
                r"(?P<parent>[^.;:]+?)\s+category\s+serves\s+as\s+(?:a|the)\s+(?:broad|general)\s+classification",
                re.IGNORECASE,
            ),
            re.compile(
                r"(?P<child>[^.;:]+?)\s+(?:is|are|was|were)\s+(?:a|an)\s+(?:distinct\s+subclass|subclass|class|category)\s+of\s+(?P<parent>[^.;:]+)",
                re.IGNORECASE,
            ),
            re.compile(
                r"(?P<child>[^.;:]+?)\s+(?:is|are|was|were)\s+recognized\s+as\s+(?:a|an)\s+distinct\s+subclass",
                re.IGNORECASE,
            ),
            re.compile(
                r"(?P<child>[^.;:]+?)\s+(?:is|are|was|were)\s+(?:categorized|classified|recognized|identified)\s+as\s+(?P<parent>[^.;:]+)",
                re.IGNORECASE,
            ),
            re.compile(
                r"(?P<child>[^.;:]+?)\s+(?:falls?\s+under|belongs?\s+to)\s+(?P<parent>[^.;:]+)",
                re.IGNORECASE,
            ),
        ]
        include_patterns = [
            re.compile(
                r"(?:this group|this category|this class|this domain|the category|the class)\s+includes?\s+(?P<children>[^.;:]+)",
                re.IGNORECASE,
            ),
        ]
        pairs = []
        broad_parent = None
        for sentence in self._sentence_split(context):
            broad_match = patterns[0].search(sentence)
            if broad_match:
                broad_parent = self._clean_context_label(broad_match.group("parent"))
            for pattern in patterns[1:]:
                for match in pattern.finditer(sentence):
                    child = self._clean_context_label(match.group("child"))
                    parent = (
                        self._clean_context_label(match.group("parent"))
                        if "parent" in match.groupdict() and match.group("parent")
                        else broad_parent
                    )
                    if child and parent and child != parent:
                        pairs.append((child, parent))
            if broad_parent:
                for pattern in include_patterns:
                    for match in pattern.finditer(sentence):
                        for child in self._split_enumeration(match.group("children")):
                            if child and child != broad_parent:
                                pairs.append((child, broad_parent))
        return pairs

    def _extract_explicit_context_triples(
        self,
        context: str,
        *,
        terms: list[str],
        types: list[str],
        initial_triples: list[list[str]],
    ) -> list[list[str]]:
        """Extract direct "X is a Y" statements constrained to known ontology expansion labels."""
        known_children = sorted(
            {
                self._normalize_label(item)
                for item in [*terms, *types]
                if self._normalize_label(item)
            },
            key=lambda item: (-len(item.split()), item),
        )
        known_parents = sorted(
            {
                self._normalize_label(item)
                for item in types
                if self._normalize_label(item)
            }
            | {
                self._normalize_label(triple[0])
                for triple in initial_triples
                if isinstance(triple, list) and len(triple) == 3 and isinstance(triple[0], str)
            }
            | {
                self._normalize_label(triple[2])
                for triple in initial_triples
                if isinstance(triple, list) and len(triple) == 3 and isinstance(triple[2], str)
            },
            key=lambda item: (-len(item.split()), item),
        )
        parent_set = set(known_parents)
        child_set = set(known_children)
        triples: list[list[str]] = []

        for child, parent in self._extract_context_is_a_pairs(context):
            child_norm = self._normalize_label(child)
            parent_norm = self._normalize_label(parent)
            if child_norm in child_set and parent_norm in parent_set and child_norm != parent_norm:
                triples.append([child_norm, "is-a", parent_norm])

        for sentence in self._sentence_split(context):
            normalized_sentence = self._clean_context_label(sentence)
            if not normalized_sentence:
                continue
            for child in known_children:
                match = re.search(
                    rf"(?:^|\b){re.escape(child)}\s+(?:is|are|was|were)\s+"
                    r"(?P<parent>[^.;:,]+)",
                    normalized_sentence,
                )
                if not match:
                    continue
                parent_phrase = self._clean_context_label(match.group("parent"))
                parent_tokens = parent_phrase.split()
                parent_candidates = [
                    " ".join(parent_tokens[:width])
                    for width in range(min(len(parent_tokens), 6), 0, -1)
                ]
                for parent in parent_candidates:
                    if parent in parent_set and parent != child:
                        triples.append([child, "is-a", parent])
                        break
                break
        return triples

    def _build_parent_statistics(self, train_records: list[dict[str, Any]]) -> tuple[Counter[str], dict[str, str]]:
        """Count type-parent relations in the training extensions."""
        parent_counts: Counter[str] = Counter()
        child_to_parent: dict[str, str] = {}
        for row in train_records:
            for triple in row.get("extended-primitive-ontology-triples", []):
                if not isinstance(triple, list) or len(triple) != 3:
                    continue
                head, relation, tail = triple
                relation = self._normalize_relation(relation)
                head = self._normalize_label(head)
                tail = self._normalize_label(tail)
                if relation != "is-a" or not head or not tail or head == tail:
                    continue
                parent_counts[tail] += 1
                child_to_parent.setdefault(head, tail)
        return parent_counts, child_to_parent

    def _build_relation_memory(self, train_records: list[dict[str, Any]]) -> dict[tuple[str, str], Counter[str]]:
        """Index observed training extensions by head and relation."""
        memory: dict[tuple[str, str], Counter[str]] = defaultdict(Counter)
        for row in train_records:
            for triple in row.get("extended-primitive-ontology-triples", []):
                if not isinstance(triple, list) or len(triple) != 3:
                    continue
                head, relation, tail = triple
                if not all(isinstance(item, str) for item in (head, relation, tail)):
                    continue
                head_norm = self._normalize_label(head)
                relation_norm = self._normalize_relation(relation)
                tail_norm = self._normalize_label(tail)
                if not head_norm or not relation_norm or not tail_norm or head_norm == tail_norm:
                    continue
                memory[(head_norm, relation_norm)][tail_norm] += 1
        return memory

    def _predict_type_extensions(self, context: str, types: list[str], initial_triples: list[list[str]], parent_counts: Counter[str] | None = None) -> list[list[str]]:
        """Generate lexical and document-supported type extensions."""
        parent_counts = parent_counts or Counter()
        normalized_types = sorted({self._normalize_label(item) for item in types if self._normalize_label(item)})
        initial_heads = {
            self._normalize_label(triple[0])
            for triple in initial_triples
            if isinstance(triple, list) and len(triple) == 3 and isinstance(triple[0], str) and self._normalize_label(triple[0])
        }
        initial_tails = {
            self._normalize_label(triple[2])
            for triple in initial_triples
            if isinstance(triple, list) and len(triple) == 3 and isinstance(triple[2], str) and self._normalize_label(triple[2])
        }
        initial_nodes = sorted(initial_heads | initial_tails)
        parent_candidates = sorted(set(normalized_types) | set(initial_nodes))
        context_pairs = self._extract_context_is_a_pairs(context)
        pair_map = defaultdict(list)
        for child, parent in context_pairs:
            pair_map[child].append(parent)

        predicted = []
        for child in normalized_types:
            if child in pair_map:
                for parent in pair_map[child]:
                    if parent in parent_candidates and child != parent:
                        predicted.append([child, "is-a", parent])
                        break
                if predicted and predicted[-1][0] == child:
                    continue
            if child in initial_tails and child not in initial_heads:
                continue

            best_parent = None
            best_score = -1.0
            for parent in parent_candidates:
                if parent == child:
                    continue
                score = self._lexical_parent_score(child, parent, parent_counts)
                if score > best_score:
                    best_score = score
                    best_parent = parent
            if best_parent and best_score >= 2.0:
                predicted.append([child, "is-a", best_parent])
        return predicted

    def _predict_term_typings(self, terms: list[str], types: list[str], context: str) -> list[list[str]]:
        """Assign types to record terms using document and lexical evidence."""
        normalized_terms = sorted({self._normalize_label(item) for item in terms if self._normalize_label(item)})
        normalized_types = sorted({self._normalize_label(item) for item in types if self._normalize_label(item)})
        context_pairs = self._extract_context_is_a_pairs(context)
        pair_map = defaultdict(list)
        for child, parent in context_pairs:
            pair_map[child].append(parent)

        predicted = []
        for term in normalized_terms:
            parent = None
            if "user" in term and "person" in normalized_types:
                parent = "person"
            if term in pair_map:
                for candidate in pair_map[term]:
                    if candidate in normalized_types:
                        parent = candidate
                        break
            if parent is None:
                term_tokens = self._token_set(term)
                best_score = -1.0
                for candidate in normalized_types:
                    candidate_tokens = self._token_set(candidate)
                    overlap = len(term_tokens & candidate_tokens)
                    suffix_bonus = 1.0 if term.split() and candidate.split() and term.split()[-1] == candidate.split()[-1] else 0.0
                    score = overlap + suffix_bonus
                    if score > best_score:
                        best_score = score
                        parent = candidate
            if parent:
                predicted.append([term, "instance-of", parent])
        return predicted

    def _predict_memorized_type_extensions(
        self,
        *,
        types: list[str],
        relation_memory: dict[tuple[str, str], Counter[str]],
        parent_counts: Counter[str],
        score_threshold: float,
    ) -> list[list[str]]:
        """Recover type parents from memorized and lexical candidates."""
        normalized_types = sorted({self._normalize_label(item) for item in types if self._normalize_label(item)})
        type_set = set(normalized_types)
        predicted = []

        for child in normalized_types:
            parent = None
            memorized = relation_memory.get((child, "is-a"))
            if memorized:
                candidates = [
                    (candidate_parent, count)
                    for candidate_parent, count in memorized.items()
                    if candidate_parent in type_set and candidate_parent != child
                ]
                if candidates:
                    candidates.sort(
                        key=lambda item: (
                            -(item[1] + 0.15 * self._memorized_parent_score(child, item[0], parent_counts)),
                            item[0],
                        )
                    )
                    parent = candidates[0][0]
            if parent is None:
                best_parent = None
                best_score = -1.0
                for candidate_parent in normalized_types:
                    if candidate_parent == child:
                        continue
                    score = self._memorized_parent_score(child, candidate_parent, parent_counts)
                    if score > best_score:
                        best_score = score
                        best_parent = candidate_parent
                if best_parent and best_score >= score_threshold:
                    parent = best_parent
            if parent:
                predicted.append([child, "is-a", parent])
        return predicted

    def _predict_memorized_term_typings(
        self,
        *,
        terms: list[str],
        types: list[str],
        relation_memory: dict[tuple[str, str], Counter[str]],
    ) -> list[list[str]]:
        """Assign term types using training memory and lexical fallback."""
        normalized_terms = sorted({self._normalize_label(item) for item in terms if self._normalize_label(item)})
        normalized_types = sorted({self._normalize_label(item) for item in types if self._normalize_label(item)})
        type_set = set(normalized_types)
        predicted = []

        for term in normalized_terms:
            parent = None
            memorized = relation_memory.get((term, "instance-of"))
            if memorized:
                candidates = [
                    (candidate_parent, count)
                    for candidate_parent, count in memorized.items()
                    if candidate_parent in type_set
                ]
                if candidates:
                    candidates.sort(key=lambda item: (-item[1], item[0]))
                    parent = candidates[0][0]
            if parent is None and normalized_types:
                term_tokens = self._token_set(term)
                best_parent = None
                best_score = -1.0
                for candidate_parent in normalized_types:
                    candidate_tokens = self._token_set(candidate_parent)
                    overlap = len(term_tokens & candidate_tokens)
                    suffix_bonus = (
                        1.0
                        if term.split() and candidate_parent.split() and term.split()[-1] == candidate_parent.split()[-1]
                        else 0.0
                    )
                    score = overlap + suffix_bonus
                    if score > best_score:
                        best_score = score
                        best_parent = candidate_parent
                if best_parent:
                    parent = best_parent
            if parent:
                predicted.append([term, "instance-of", parent])
        return predicted

    def _ensure_expansion_obo_source_cached(self, source_key: str) -> Path:
        """Resolve cached OBO resources, downloading if necessary."""
        if source_key not in EXPANSION_ALL_OBO_SOURCE_URLS:
            raise ValueError(f"Unknown ontology expansion OBO source: {source_key}")
        EXPANSION_OBO_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        path = EXPANSION_OBO_CACHE_DIR / f"{source_key}.obo"
        if path.exists() and path.stat().st_size > 1000:
            return path
        request = urllib.request.Request(EXPANSION_ALL_OBO_SOURCE_URLS[source_key], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=180) as response:
            path.write_bytes(response.read())
        return path

    @lru_cache(maxsize=None)
    def _load_expansion_obo_source_terms(self, source_key: str) -> tuple[dict[str, Any], ...]:
        """Read labels, synonyms, and direct parents from an OBO resource."""
        path = self._ensure_expansion_obo_source_cached(source_key)
        terms: list[dict[str, Any]] = []
        current_id = None
        current_name = None
        current_parents: list[str] = []
        current_synonyms: list[str] = []
        is_obsolete = False
        in_term = False

        def flush_term() -> None:
            if not current_id or not current_name or is_obsolete:
                return
            terms.append(
                {
                    "id": current_id,
                    "name": self._normalize_label(current_name),
                    "parents": list(current_parents),
                    "synonyms": [self._normalize_label(item) for item in current_synonyms if self._normalize_label(item)],
                }
            )

        for raw_line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw_line.strip()
            if line == "[Term]":
                flush_term()
                current_id = None
                current_name = None
                current_parents = []
                current_synonyms = []
                is_obsolete = False
                in_term = True
                continue
            if line.startswith("["):
                flush_term()
                current_id = None
                current_name = None
                current_parents = []
                current_synonyms = []
                is_obsolete = False
                in_term = False
                continue
            if not in_term:
                continue
            if line.startswith("id: "):
                current_id = line[4:].strip()
            elif line.startswith("name: "):
                current_name = line[6:].strip()
            elif line.startswith("is_a: "):
                current_parents.append(line.split()[1])
            elif line.startswith("synonym: "):
                match = re.match(r'synonym: "(.+?)"\s', line)
                if match:
                    current_synonyms.append(match.group(1))
            elif line == "is_obsolete: true":
                is_obsolete = True
        flush_term()
        return tuple(terms)

    def _ensure_expansion_foodon_owl_cached(self) -> Path:
        """Resolve the cached FoodOn ontology."""
        EXPANSION_OWL_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        if EXPANSION_FOODON_OWL_PATH.exists() and EXPANSION_FOODON_OWL_PATH.stat().st_size > 1_000_000:
            return EXPANSION_FOODON_OWL_PATH
        request = urllib.request.Request(EXPANSION_FOODON_OWL_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=180) as response:
            EXPANSION_FOODON_OWL_PATH.write_bytes(response.read())
        return EXPANSION_FOODON_OWL_PATH

    @lru_cache(maxsize=1)
    def _load_expansion_foodon_owl_terms(self) -> tuple[dict[str, Any], ...]:
        """Read labels and direct subclass relations from FoodOn."""
        try:
            import rdflib
            from rdflib import URIRef
        except ImportError as exc:  # pragma: no cover - dependency is provided by OntoLearner
            raise RuntimeError("rdflib is required to parse FoodOn OWL.") from exc

        owl_path = self._ensure_expansion_foodon_owl_cached()
        graph = rdflib.Graph()
        graph.parse(str(owl_path), format="xml")
        label_predicates = {
            rdflib.namespace.RDFS.label,
            URIRef(f"{OBO_IN_OWL_PREFIX}hasExactSynonym"),
            URIRef(f"{OBO_IN_OWL_PREFIX}hasRelatedSynonym"),
            URIRef(f"{OBO_IN_OWL_PREFIX}hasBroadSynonym"),
        }
        labels_by_uri: dict[str, list[str]] = defaultdict(list)
        parent_uris: dict[str, list[str]] = defaultdict(list)

        for subject, predicate, object_value in graph.triples((None, None, None)):
            if predicate in label_predicates and isinstance(subject, URIRef):
                label = self._normalize_label(str(object_value))
                subject_id = str(subject)
                if label and label not in labels_by_uri[subject_id]:
                    labels_by_uri[subject_id].append(label)
        for subject, object_value in graph.subject_objects(rdflib.namespace.RDFS.subClassOf):
            if isinstance(subject, URIRef) and isinstance(object_value, URIRef):
                parent_uris[str(subject)].append(str(object_value))

        return tuple(
            {
                "id": term_id,
                "labels": tuple(labels),
                "parents": tuple(parent_uris.get(term_id, [])),
            }
            for term_id, labels in labels_by_uri.items()
        )

    def _collect_obo_candidate_labels(self, row: dict[str, Any]) -> set[str]:
        """Collect record-local labels for public-ontology matching."""
        return {
            self._normalize_label(item)
            for item in [*row.get("types", []), *row.get("terms", [])]
            if isinstance(item, str) and self._normalize_label(item)
        }

    def _build_expansion_obo_index(
        self,
        records: list[dict[str, Any]],
        *,
        source_keys: tuple[str, ...] = EXPANSION_OBO_SOURCE_KEYS,
        include_foodon_owl: bool = False,
    ) -> dict[str, Any]:
        """Build the record-restricted OBO and FoodOn parent index."""
        label_universe = set()
        for row in records:
            label_universe.update(self._collect_obo_candidate_labels(row))

        name_to_ids: dict[str, list[tuple[str, str]]] = defaultdict(list)
        id_to_labels: dict[tuple[str, str], list[str]] = defaultdict(list)
        id_to_parents: dict[tuple[str, str], list[tuple[str, str]]] = {}
        source_term_counts: dict[str, int] = {}

        for source_key in source_keys:
            terms = self._load_expansion_obo_source_terms(source_key)
            source_term_counts[source_key] = len(terms)
            for term in terms:
                term_key = (source_key, term["id"])
                id_to_parents[term_key] = [(source_key, parent_id) for parent_id in term["parents"]]
                labels = []
                if term["name"]:
                    labels.append(term["name"])
                labels.extend(synonym for synonym in term["synonyms"] if synonym and synonym not in labels)
                for label in labels:
                    if label not in label_universe:
                        continue
                    name_to_ids[label].append(term_key)
                    id_to_labels[term_key].append(label)

        if include_foodon_owl:
            source_key = "foodon_owl"
            foodon_terms = self._load_expansion_foodon_owl_terms()
            source_term_counts[source_key] = len(foodon_terms)
            for term in foodon_terms:
                term_key = (source_key, term["id"])
                id_to_parents[term_key] = [(source_key, parent_id) for parent_id in term["parents"]]
                for label in term["labels"]:
                    if label not in label_universe:
                        continue
                    name_to_ids[label].append(term_key)
                    id_to_labels[term_key].append(label)

        return {
            "name_to_ids": dict(name_to_ids),
            "id_to_labels": dict(id_to_labels),
            "id_to_parents": id_to_parents,
            "source_term_counts": source_term_counts,
            "matched_label_count": len(name_to_ids),
        }

    def _predict_expansion_obo_type_edges(self, row: dict[str, Any], obo_index: dict[str, Any]) -> list[list[str]]:
        """Recover direct public-ontology parents within record labels."""
        labels = self._collect_obo_candidate_labels(row)
        name_to_ids = obo_index["name_to_ids"]
        id_to_labels = obo_index["id_to_labels"]
        id_to_parents = obo_index["id_to_parents"]
        predicted = []

        for child in sorted(labels):
            for term_key in name_to_ids.get(child, []):
                for parent_key in id_to_parents.get(term_key, []):
                    for parent in id_to_labels.get(parent_key, []):
                        if parent in labels and parent != child:
                            predicted.append([child, "is-a", parent])
        return predicted

    def _build_extended_predictions(self, records: list[dict[str, Any]], train_records: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
        """Run the original lexical construction of ontology extensions."""
        return self._build_extended_predictions_for_method(records, train_records=train_records, method="constrained_lex")

    def _build_extended_predictions_for_method(
        self,
        records: list[dict[str, Any]],
        train_records: list[dict[str, Any]] | None = None,
        *,
        method: str,
    ) -> list[dict[str, Any]]:
        """Run one of the original ontology expansion strategies."""
        if method not in EXPANSION_METHODS:
            raise ValueError(f"Unknown ontology expansion method {method!r}. Expected one of: {', '.join(EXPANSION_METHODS)}")

        parent_counts, _ = self._build_parent_statistics(train_records or [])
        relation_memory = self._build_relation_memory(train_records or [])
        obo_index = (
            self._build_expansion_obo_index(
                records,
                source_keys=EXPANSION_FOODON_TO_SOURCE_KEYS
                if method
                in {
                    "obo_foodon_to_direct",
                    "obo_foodon_to_terms_only",
                    "obo_foodon_to_hybrid",
                    "obo_foodon_to_selective",
                    "obo_foodon_to_selective_threshold_4",
                    "obo_foodon_to_selective_threshold_8",
                }
                else EXPANSION_OBO_SOURCE_KEYS,
                include_foodon_owl=method
                in {
                    "obo_foodon_hybrid",
                    "obo_foodon_selective",
                    "obo_foodon_to_direct",
                    "obo_foodon_to_terms_only",
                    "obo_foodon_to_hybrid",
                    "obo_foodon_to_selective",
                    "obo_foodon_to_selective_threshold_4",
                    "obo_foodon_to_selective_threshold_8",
                },
            )
            if method
            in {
                "obo_direct",
                "obo_memorized_hybrid",
                "obo_memorized_selective",
                "obo_foodon_hybrid",
                "obo_foodon_selective",
                "obo_foodon_to_direct",
                "obo_foodon_to_terms_only",
                "obo_foodon_to_hybrid",
                "obo_foodon_to_selective",
                "obo_foodon_to_selective_threshold_4",
                "obo_foodon_to_selective_threshold_8",
            }
            else None
        )
        predictions = []
        for row in records:
            initial_triples = row.get("initial-primitive-ontology-triples", [])
            context_extensions = []
            type_extensions = []
            term_extensions = []
            memorized_extensions = []
            obo_extensions = []
            if method in {"context_rules", "hybrid_reuse"}:
                context_extensions = self._extract_explicit_context_triples(
                    row["context"],
                    terms=row.get("terms", []),
                    types=row.get("types", []),
                    initial_triples=initial_triples,
                )
            if method in {"constrained_lex", "hybrid_reuse"}:
                type_extensions = self._predict_type_extensions(
                    context=row["context"],
                    types=row.get("types", []),
                    initial_triples=initial_triples,
                    parent_counts=parent_counts,
                )
            if method in {"constrained_lex", "type_link", "hybrid_reuse"}:
                term_extensions = self._predict_term_typings(
                    terms=row.get("terms", []),
                    types=row.get("types", []),
                    context=row["context"],
                )
            if method in {"memorized_lexical", "memorized_lexical_strict"}:
                memorized_extensions = self._predict_memorized_type_extensions(
                    types=row.get("types", []),
                    relation_memory=relation_memory,
                    parent_counts=parent_counts,
                    score_threshold=1.0 if method == "memorized_lexical" else 1.2,
                )
                memorized_extensions.extend(
                    self._predict_memorized_term_typings(
                        terms=row.get("terms", []),
                        types=row.get("types", []),
                        relation_memory=relation_memory,
                    )
                )
            if method in {
                "obo_direct",
                "obo_memorized_hybrid",
                "obo_memorized_selective",
                "obo_foodon_hybrid",
                "obo_foodon_selective",
                "obo_foodon_to_direct",
                "obo_foodon_to_terms_only",
                "obo_foodon_to_hybrid",
                "obo_foodon_to_selective",
                "obo_foodon_to_selective_threshold_4",
                "obo_foodon_to_selective_threshold_8",
            }:
                obo_extensions = self._predict_expansion_obo_type_edges(row, obo_index or {})
            if method in {
                "obo_memorized_hybrid",
                "obo_memorized_selective",
                "obo_foodon_hybrid",
                "obo_foodon_selective",
                "obo_foodon_to_hybrid",
                "obo_foodon_to_selective",
                "obo_foodon_to_selective_threshold_4",
                "obo_foodon_to_selective_threshold_8",
            }:
                threshold_by_method = {
                    "obo_foodon_to_selective_threshold_4": 4.0,
                    "obo_foodon_to_selective_threshold_8": 8.0,
                }
                memorized_extensions = self._predict_memorized_type_extensions(
                    types=row.get("types", []),
                    relation_memory=relation_memory,
                    parent_counts=parent_counts,
                    score_threshold=threshold_by_method.get(method, 1.0),
                )
                if method in {
                    "obo_memorized_selective",
                    "obo_foodon_selective",
                    "obo_foodon_to_selective",
                    "obo_foodon_to_selective_threshold_4",
                    "obo_foodon_to_selective_threshold_8",
                }:
                    obo_children = {triple[0] for triple in obo_extensions if len(triple) == 3 and triple[1] == "is-a"}
                    memorized_extensions = [
                        triple
                        for triple in memorized_extensions
                        if len(triple) != 3 or triple[1] != "is-a" or triple[0] not in obo_children
                    ]
                memorized_extensions.extend(
                    self._predict_memorized_term_typings(
                        terms=row.get("terms", []),
                        types=row.get("types", []),
                        relation_memory=relation_memory,
                    )
                )

            if method == "context_rules":
                candidate_triples = context_extensions
            elif method == "type_link":
                candidate_triples = term_extensions
            elif method == "hybrid_reuse":
                candidate_triples = context_extensions + type_extensions + term_extensions
            elif method in {"memorized_lexical", "memorized_lexical_strict"}:
                candidate_triples = memorized_extensions
            elif method in {"obo_direct", "obo_foodon_to_direct"}:
                candidate_triples = obo_extensions
            elif method == "obo_foodon_to_terms_only":
                candidate_triples = obo_extensions + self._predict_memorized_term_typings(
                    terms=row.get("terms", []),
                    types=row.get("types", []),
                    relation_memory=relation_memory,
                )
            elif method in {
                "obo_memorized_hybrid",
                "obo_memorized_selective",
                "obo_foodon_hybrid",
                "obo_foodon_selective",
                "obo_foodon_to_hybrid",
                "obo_foodon_to_selective",
                "obo_foodon_to_selective_threshold_4",
                "obo_foodon_to_selective_threshold_8",
            }:
                candidate_triples = obo_extensions + memorized_extensions
            else:
                candidate_triples = type_extensions + term_extensions

            extended = self._sanitize_extended_triples(candidate_triples, initial_triples)
            predictions.append(
                {
                    "id": row["id"],
                    "extended-primitive-ontology-triples": extended,
                }
            )
        return predictions
