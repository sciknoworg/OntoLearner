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

import copy
import json
import logging
import re
import time
import unicodedata
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

from ..data_structure import OntologyData, SyntheticText2OntoData

logger = logging.getLogger(__name__)

TRIPLES_KEY = "primitive-ontology-triples"
TAXONOMIC_RELATIONS = ("is-a", "instance-of")
RELATION_STYLES = ("hyphen", "snake", "space")
PSEUDO_SENTENCE_PATTERNS = ((" is subclass of ", "is-a"), (" is instance of ", "instance-of"))
DEFAULT_LABEL_CACHE = {"disjointWith": "disjoint with"}

CONTEXT_CLEANING_PROMPT = (
    "Given a raw text, there might be phrases that don't have spaces. \n"
    "- Add space between them, lowercase it (if it is the start of a sentence, the first word should start "
    "with an upper case)\n"
    "- Remove the sentence from the end if the sentence is incomplete.\n"
    "- Do not add new context or change the existing context.\n"
    "\n"
    "{context}\n"
)

LABEL_CLEANING_PROMPT = """\
Given a raw phrases containing one or more phrases, there might be words that are stuck together without spaces.

Your task:
- Insert spaces where words are incorrectly joined.
- Convert everything to lowercase.
- Do NOT apply word-style capitalization (since these are phrases, not full sentences).
- Do NOT add punctuation unless it already exists.
- Do NOT add, remove, or change meaning — only fix spacing and formatting.
- Return only the cleaned phrases, nothing else.

Input:
{context}
"""

DEEP_CLEANING_PROMPT = """You are an expert ontology-aware data cleaning system operating in CLEANING mode.

RULES:
- Apply corrections directly. Do NOT explain or add commentary.
- Return ONLY a valid JSON object. No markdown fences. No prose outside JSON.
- Do NOT add new factual information, triples, or taxonomic relations not present in input.
- Do NOT modify or split structured codes (e.g. H.PNDSN, S.LOCK, A.ADM1H, T.BLOW).
- Do NOT modify proper nouns, acronyms, or scientific symbols.
- Cleaning must be IDEMPOTENT: running twice must produce the same result.

TASKS:
1. context_cleaned: Fix grammar, spelling, punctuation, and whitespace in the provided context text.
   Normalize ontology CamelCase labels embedded in prose to natural English sentence casing.
   Do NOT add new facts. Do NOT change semantic meaning.

2. entity_corrections: For each flagged entity, return its corrected form if fixable,
   or the original unchanged if correct. Only split concatenated words when highly confident.
   Do NOT invent entity replacements.

OUTPUT SCHEMA (return exactly this):
{
  "context_cleaned": "<cleaned context text>",
  "entity_corrections": {
    "<original_entity>": "<corrected_entity>"
  }
}
"""

ALIGNMENT_PROMPT = """
You are evaluating whether a generated text aligns with ontology triples.

Definitions:
- A triple is aligned if BOTH head and tail entities are clearly present in the text.
- Misalignment occurs if:
  - head or tail is missing.
  - the text contains hallucinated or unrelated information to the topic or the head tail entities.

Your task:
- Check each triple against the text
- Determine overall alignment

Return:
- alignment: "aligned", "partially_aligned", or "not_aligned"
- rating: 1 = poor, 2= not too bad, 3= acceptable, 4=good, 5=excellent
- rational: short explanation for rating

Rating scale:
1 = poor → most triples missing or text is irrelevant/hallucinated
2 = not too bad → some triples present but many missing or weak support
3 = acceptable → about half of triples supported, limited hallucination
4 = good → most triples supported, minor issues
5 = excellent → all triples clearly supported, no hallucination


Text:
{text}

Triples:
{triples}

"""

ALIGNMENT_SCHEMA = {
    "alignment": {"type": "string", "enum": ["aligned", "partially_aligned", "not_aligned"]},
    "rating": {"type": "integer", "enum": [1, 2, 3, 4, 5]},
    "rational": {"type": "string"},
}

# Structural cleanup (test_annotation.ipynb, stage 1)
_CONTROL_CHARS = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]")
_MULTI_SPACE = re.compile(r"[ \t]+")
_MULTI_NEWLINE = re.compile(r"\n{3,}")
_REPEATED_PUNCT = re.compile(r"([!?,;])\1{2,}")
_ELLIPSIS_NORM = re.compile(r"\.{4,}")
_MALFORMED_DASH = re.compile(r"(?<!\-)\-{2,3}(?!\-)")
_BROKEN_QUOTE_OPEN = re.compile(r"\bâ€œ\b|\bâ€˜\b")
_BROKEN_QUOTE_CLOSE = re.compile(r"\bâ€\b|\bâ€™\b")
_HTML_TAG = re.compile(r"<[^>]{0,80}>")
_HTML_ENTITY = re.compile(r"&(?:[a-zA-Z]{2,6}|#\d{1,5});")
_XML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
_URI_NOISE = re.compile(r"https?://\S+")
_STACK_TRACE = re.compile(r"(?:Traceback \(most recent call last\)|at \w+\.\w+\(.*?\)|\s+File \".*?\", line \d+).*",
                          re.DOTALL)
_JSON_ARTIFACT = re.compile(r"\{\"[a-zA-Z_]+\":\s*[^}]{0,200}\}")
_BACKTICK_LABEL = re.compile(r"`([^`]+)`")
_ESCAPED_CHARS = re.compile(r"\\([ntr\"'\\])")
_DUPLICATE_DELIM = re.compile(r"([,:;])\1+")
# Entities (stages 2 and 4)
_DOT_NOTATION_CODE = re.compile(r"^[A-Za-z]\.[A-Z]{2,}$")      # H.PNDSN, S.LOCK, A.ADM1H
_SPURIOUS_DOT_SPACE = re.compile(r"([A-Za-z])\.\s+([A-Za-z])")  # "h. sea" -> "h.sea"
_BLANK_NODE = re.compile(r"^(_:.*|q\d+|node_\d+|anon_\d+|tmp_\d+|x\d+|\?[a-z]+)$", re.IGNORECASE)
_ONLY_PUNCT_OR_DIGITS = re.compile(r"^[\W\d]+$")
_KNOWN_TYPE_SPLITS = {
    "amorphousmetal": "amorphous metal",
    "electronicandelectrical": "electronic and electrical",
    "compoundsubstance": "compound substance",
    "nonmetaliccompound": "non-metalic compound",
    "frustumofpyramid": "frustum of pyramid",
    "frustumofcone": "frustum of cone",
    "rectangularparallelopiped": "rectangular parallelopiped",
    "activationenergy": "activation energy",
    "electronmobility": "electron mobility",
    "hallmobility": "hall mobility",
    "electricalresistivity": "electrical resistivity",
    "electricpotentialdifference": "electric potential difference",
    "electriccurrent": "electric current",
    "electricresistance": "electric resistance",
    "electricconductance": "electric conductance",
    "effectivemassofelectronsinconductionband": "effective mass of electrons in conduction band",
}


@dataclass
class CleaningStats:
    """Per-record report of the six-stage cleaning (``SyntheticDataPreprocessor.deep_clean_record``)."""
    record_id: str = ""
    triples_before: int = 0
    triples_after: int = 0
    triples_removed_blank: int = 0
    triples_deduped: int = 0
    llm_called: bool = False
    llm_fallback: bool = False          # the LLM was called but its result was not used
    llm_context_reverted: bool = False
    flags: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


class SyntheticDataPreprocessor:
    """
    Turns the output of ``SyntheticGenerator`` into cleaned primitive-ontology records.

    ``preprocess`` runs the steps below; each one is also a public method.

    1. ``prepare_items``: pair every generated document with the pseudo-sentence batch it was written from.
    2. ``prepare_record``: pseudo-sentences become triples (``X is subclass of Y`` -> ``[X, is-a, Y]``,
       ``X is instance of Y`` -> ``[X, instance-of, Y]``), the ontology's non-taxonomic relations between the
       document's types are added, and with a client the text and labels are cleaned (``clean_context``,
       ``clean_gold``). Relation labels keep the form the label cleaning gives them (``disjoint with``).
       (annotation.ipynb, ``make_the_flagship``)
    3. ``deep_clean`` (optional): the six-stage cleaning of test_annotation.ipynb, which also brings relation
       labels to ``relation_style``, with a ``CleaningStats`` report per record in ``cleaning_stats``.
    4. ``annotate_alignment`` + ``filter_by_alignment`` (optional): the LLM judge of annotation.ipynb. The kept
       records hold only ``id``, ``context`` and the triples, as in the released train set.

    The OpenAI calls happen here, once; the records can then be prepared for both tasks with
    ``PrimitiveOntologyDataset``.

    Example:
        >>> preprocessor = SyntheticDataPreprocessor(client=OpenAI(), alignment_filter=True)
        >>> records = preprocessor.preprocess(synthetic_data, train_ontology)
    """

    def __init__(self,
                 client: Any = None,
                 model: str = "gpt-4o-mini",
                 deep_clean_model: str = "gpt-5.4",
                 clean_text: bool = True,
                 deep_clean: bool = False,
                 alignment_filter: bool = False,
                 relation_style: Optional[str] = "hyphen",
                 min_partial_rating: int = 3,
                 max_entity_length: int = 120,
                 max_context_tokens: int = 3000,
                 max_expansion_ratio: float = 1.5,
                 max_retries: int = 5,
                 annotation_retries: Optional[int] = None,
                 max_workers: int = 10) -> None:
        """
        Args:
            client: ``openai.OpenAI`` client. ``None`` runs only the deterministic steps.
            model: OpenAI model for the text cleaning and the judge (the release used ``gpt-4o-mini``).
            deep_clean_model: OpenAI model for the six-stage cleaning (the release used ``gpt-5.4``).
            clean_text: LLM cleaning of the text and labels in ``prepare_record``.
            deep_clean: Run the six-stage cleaning in ``preprocess`` (the released test set used it).
            alignment_filter: Keep only records the judge rates as aligned (the released train set used it).
            relation_style: Style the six-stage cleaning gives relation labels: ``"hyphen"`` (``is-defined-by``,
                as in the released test set), ``"snake"`` (``is_defined_by``), ``"space"`` (``is defined by``) or
                ``None`` to keep them as they are. See ``normalize_relation``. Without ``deep_clean`` relation
                labels are not restyled, as in the released train set.
            min_partial_rating: Lowest rating at which a ``partially_aligned`` record is kept.
            max_entity_length: Entities longer than this are sent to the LLM during the six-stage cleaning.
            max_context_tokens: Context sent to the LLM is cut beyond this many tokens (estimated).
            max_expansion_ratio: An LLM-cleaned context longer than this ratio of the input is rejected.
            max_retries: Attempts per OpenAI request (text cleaning and six-stage cleaning).
            annotation_retries: Attempts per judge request. ``None`` retries until it succeeds, as annotation.ipynb
                did, so no record is lost to a failed request; with a number, records whose request still fails
                are dropped by ``filter_by_alignment``.
            max_workers: Parallel OpenAI requests.
        """
        if relation_style is not None and relation_style not in RELATION_STYLES:
            raise ValueError(f"relation_style must be one of {RELATION_STYLES} or None, got {relation_style!r}")
        if alignment_filter and client is None:
            raise ValueError("alignment_filter=True needs an OpenAI `client`.")
        self.client = client
        self.model = model
        self.deep_clean_model = deep_clean_model
        self.clean_text = clean_text
        self.deep_clean_enabled = deep_clean
        self.alignment_filter = alignment_filter
        self.relation_style = relation_style
        self.min_partial_rating = min_partial_rating
        self.max_entity_length = max_entity_length
        self.max_context_tokens = max_context_tokens
        self.max_expansion_ratio = max_expansion_ratio
        self.max_retries = max_retries
        self.annotation_retries = annotation_retries
        self.max_workers = max_workers
        self.label_cache: Dict[str, str] = dict(DEFAULT_LABEL_CACHE)
        self.cleaning_stats: List[CleaningStats] = []

    # ------------------------------------------------------------------ #
    # Entry point
    # ------------------------------------------------------------------ #
    def preprocess(self,
                   synthetic_data: Union[SyntheticText2OntoData, List[Dict[str, Any]]],
                   ontological_data: Union[OntologyData, Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Turn generated documents into cleaned primitive-ontology records.

        Args:
            synthetic_data: ``SyntheticGenerator.generate`` output, or a list of ``prepare_items``-style dicts
                (for example a ``*_text2onto.json`` file written by an earlier generation run).
            ontological_data: The ontology split the documents were generated from (``OntologyData`` or its dict).

        Returns:
            ``[{"id", "context", "terms", "types", "primitive-ontology-triples"}]``; with ``alignment_filter``
            ``[{"id", "context", "primitive-ontology-triples"}]``, as in the released train set. With
            ``deep_clean`` the per-record reports are in ``self.cleaning_stats``.
        """
        items = synthetic_data if isinstance(synthetic_data, list) else self.prepare_items(synthetic_data)
        records = self._parallel_map(lambda item: self.prepare_record(item, ontological_data), items)
        if self.deep_clean_enabled:
            records = self.deep_clean(records)
        if self.alignment_filter:
            records = self.filter_by_alignment(self.annotate_alignment(records))
        logger.info("Preprocessed %d documents into %d records.", len(items), len(records))
        return records

    # ------------------------------------------------------------------ #
    # 1-2. Documents -> records, light LLM cleaning (annotation.ipynb)
    # ------------------------------------------------------------------ #
    @staticmethod
    def prepare_items(synthetic_data: SyntheticText2OntoData) -> List[Dict[str, Any]]:
        """
        Pair every generated document with the pseudo-sentence batch it was generated from.

        Returns:
            ``[{"id", "title", "text", "structured_data"}]`` where ``structured_data`` holds the document's
            ``pseudo_sentences``, ``terms`` and ``types``.
        """
        rows = {str(batch.id): batch.model_dump() for batch in synthetic_data.pseudo_sentences}
        items = []
        for doc in synthetic_data.generated_docs:
            row = rows.get(str(doc.id))
            if row is None:
                logger.warning("No pseudo-sentence batch for document %s; skipping it.", doc.id)
                continue
            items.append({"id": doc.id, "title": doc.title, "text": doc.text, "structured_data": row})
        return items

    def prepare_record(self, item: Dict[str, Any],
                       ontological_data: Union[OntologyData, Dict[str, Any]]) -> Dict[str, Any]:
        """
        Turn one generated document into a primitive-ontology record (``make_the_flagship``).

        Returns:
            ``{"id", "context", "terms", "types", "primitive-ontology-triples"}``.
        """
        structured = item["structured_data"]
        types = structured.get("types", []) or []
        triples = []
        for sentence in structured.get("pseudo_sentences", []) or []:
            for marker, relation in PSEUDO_SENTENCE_PATTERNS:
                if marker in sentence:
                    parts = sentence.split(marker)
                    triples.append([parts[0], relation, parts[1]])
                    break
            else:
                logger.warning("Unrecognised pseudo-sentence: %r", sentence)
        type_set = set(types)
        triples += [t for t in self._non_taxonomic_triples(ontological_data) if t[0] in type_set and t[2] in type_set]

        text = item["text"]
        if self.clean_text and self.client is not None:
            text = self.clean_context(text)
        triples = self.clean_gold(triples)
        return {
            "id": uuid.uuid4().hex,
            "context": f"Title: {item['title']} \n\n Content: \n{text}",
            "terms": [term.lower() for term in structured.get("terms", []) or []],
            "types": [typ.lower() for typ in types],
            TRIPLES_KEY: triples,
        }

    def clean_context(self, text: str) -> str:
        """Insert missing spaces and drop an unfinished last sentence; ``text`` is returned unchanged on failure."""
        if self.client is None:
            return text
        result = self._call_tool(CONTEXT_CLEANING_PROMPT.format(context=text), "clean_paragraph",
                                 "Return a cleaned, well-formed paragraph.",
                                 {"paragraph": {"type": "string", "description": "The cleaned paragraph."}},
                                 self.max_retries)
        paragraph = (result or {}).get("paragraph")
        return paragraph if isinstance(paragraph, str) and paragraph.strip() else text

    def clean_gold(self, triples: Sequence[Sequence[str]]) -> List[List[str]]:
        """
        Fix glued words in every head, relation and tail label (``CompoundSubstance`` -> ``compound substance``).

        Each label is requested once and kept in ``self.label_cache`` for every later document. ``is-a`` and
        ``instance-of`` are never sent. Without a client (or with ``clean_text=False``) only the cache is used.
        """
        use_llm = self.clean_text and self.client is not None

        def _clean(label: str) -> str:
            if label in TAXONOMIC_RELATIONS or label in self.label_cache or not use_llm:
                return self.label_cache.get(label, label)
            result = self._call_tool(LABEL_CLEANING_PROMPT.format(context=label), "clean_phrase",
                                     "Return a cleaned, well-formed phrase.",
                                     {"phrase": {"type": "string", "description": "The cleaned phrase."}},
                                     self.max_retries)
            phrase = (result or {}).get("phrase")
            if not (isinstance(phrase, str) and phrase.strip()):
                logger.warning("Label cleaning failed for %r; keeping it unchanged.", label)
                return label
            self.label_cache[label] = phrase
            return phrase

        return [[_clean(head), _clean(relation), _clean(tail)] for head, relation, tail in triples]

    # ------------------------------------------------------------------ #
    # 3. Six-stage cleaning (test_annotation.ipynb)
    # ------------------------------------------------------------------ #
    def deep_clean(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        ``deep_clean_record`` on every record. A record that raises is kept unchanged and flagged. The reports
        are stored in ``self.cleaning_stats`` (same order as the records).
        """
        def _safe(record: Dict[str, Any]) -> Tuple[Dict[str, Any], CleaningStats]:
            try:
                return self.deep_clean_record(record)
            except Exception as exc:
                logger.error("Cleaning failed for record %s, keeping it unchanged: %s", record.get("id"), exc)
                return record, CleaningStats(record_id=str(record.get("id")), flags=[f"Processing error: {exc}"])

        results = self._parallel_map(_safe, records)
        self.cleaning_stats = [stats for _, stats in results]
        self.summarize_stats()
        return [record for record, _ in results]

    def deep_clean_record(self, record: Dict[str, Any]) -> Tuple[Dict[str, Any], CleaningStats]:
        """
        Clean one record: structural cleanup of the context, normalisation and filtering of the triples,
        ``normalize_types``, and with a client an LLM pass on the context and over-long entities. The LLM result
        is only accepted when the context grows by at most ``max_expansion_ratio`` and the entities stay valid.

        Returns:
            ``(cleaned copy of the record, CleaningStats)``; the input is not modified.
        """
        cleaned = copy.deepcopy(record)
        stats = CleaningStats(record_id=str(record.get("id", "?")))
        cleaned["context"] = self.structural_cleanup(cleaned.get("context", ""), strip_backticks=True)
        raw_triples = cleaned.get(TRIPLES_KEY, [])
        stats.triples_before = len(raw_triples)
        triples, flagged, stats.triples_removed_blank, stats.triples_deduped = self._normalize_triples(raw_triples)
        if stats.triples_removed_blank:
            stats.flags.append(f"{stats.triples_removed_blank} triples removed (blank node / malformed)")
        if stats.triples_deduped:
            stats.flags.append(f"{stats.triples_deduped} duplicate triples removed")
        if isinstance(cleaned.get("types"), list):
            cleaned["types"] = self.normalize_types(cleaned["types"])
        if self.client is not None and cleaned["context"]:
            cleaned["context"], triples = self._llm_clean(cleaned["context"], triples, flagged, stats)
        cleaned[TRIPLES_KEY] = triples
        stats.triples_after = len(triples)
        return cleaned, stats

    def filter_triples(self, triples: Sequence[Sequence[str]]) -> List[List[str]]:
        """Normalise entities and relation labels, drop blank-node or malformed triples, and remove duplicates."""
        return self._normalize_triples(triples)[0]

    def check_idempotency(self, records: List[Dict[str, Any]], sample_size: int = 20) -> bool:
        """Clean a sample twice; the second pass should change nothing. Differences are logged."""
        differences = []
        for record in records[:sample_size]:
            first, _ = self.deep_clean_record(record)
            second, _ = self.deep_clean_record(first)
            differences += [f"[{record.get('id')}] {key}: {str(first.get(key))[:80]} -> {str(second.get(key))[:80]}"
                            for key in first if first.get(key) != second.get(key)]
        if differences:
            logger.warning("Idempotency check failed:\n%s", "\n".join(differences[:20]))
            return False
        logger.info("Idempotency check passed on %d records.", min(sample_size, len(records)))
        return True

    def summarize_stats(self) -> Dict[str, int]:
        """Totals over ``self.cleaning_stats`` (also logged)."""
        stats = self.cleaning_stats
        summary = {
            "records": len(stats),
            "llm_calls": sum(s.llm_called for s in stats),
            "llm_fallbacks": sum(s.llm_fallback for s in stats),
            "contexts_reverted": sum(s.llm_context_reverted for s in stats),
            "triples_before": sum(s.triples_before for s in stats),
            "triples_after": sum(s.triples_after for s in stats),
            "blank_or_malformed_removed": sum(s.triples_removed_blank for s in stats),
            "duplicates_removed": sum(s.triples_deduped for s in stats),
        }
        logger.info("Cleaning summary: %s", summary)
        return summary

    @staticmethod
    def structural_cleanup(text: str, strip_backticks: bool = False) -> str:
        """Unicode normalisation; removes control characters, HTML/XML, URLs, stack traces, OCR artefacts and
        extra whitespace."""
        if not isinstance(text, str):
            return ""
        text = unicodedata.normalize("NFC", text)
        text = _CONTROL_CHARS.sub("", text)
        text = _ESCAPED_CHARS.sub(lambda m: {"n": "\n", "t": "\t", "r": ""}.get(m.group(1), m.group(1)), text)
        text = _XML_COMMENT.sub("", text)
        text = _HTML_TAG.sub("", text)
        text = _HTML_ENTITY.sub(" ", text)
        text = _STACK_TRACE.sub("", text)
        text = _JSON_ARTIFACT.sub("", text)
        text = _URI_NOISE.sub("", text)
        text = _REPEATED_PUNCT.sub(r"\1", text)
        text = _ELLIPSIS_NORM.sub("...", text)
        text = _MALFORMED_DASH.sub("—", text)
        text = _BROKEN_QUOTE_OPEN.sub('"', text)
        text = _BROKEN_QUOTE_CLOSE.sub('"', text)
        text = _DUPLICATE_DELIM.sub(r"\1", text)
        if strip_backticks:
            text = _BACKTICK_LABEL.sub(r"\1", text)
        text = _MULTI_SPACE.sub(" ", text)
        text = _MULTI_NEWLINE.sub("\n\n", text)
        return text.strip()

    @staticmethod
    def normalize_entity(entity: str) -> str:
        """Split CamelCase, replace underscores, collapse spaces; dot-notation codes such as ``H.PNDSN`` are kept."""
        if not isinstance(entity, str):
            return ""
        entity = entity.strip()
        if _DOT_NOTATION_CODE.match(entity):
            return entity
        entity = _SPURIOUS_DOT_SPACE.sub(r"\1.\2", entity)
        if re.search(r"[A-Z]", entity):
            entity = entity.replace("-", " ")
            entity = re.sub(r"([a-z])([A-Z])", r"\1 \2", entity)
            entity = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", entity).lower()
        else:
            entity = entity.replace("_", " ")
        return re.sub(r"\s+", " ", entity).strip()

    @staticmethod
    def normalize_relation(relation: str, style: Optional[str] = "hyphen") -> str:
        """
        Bring a relation label to one style; ``madeFrom``, ``made_from`` and ``made from`` all become

        * ``"hyphen"``: ``made-from`` (keeps ``is-a`` / ``instance-of`` as ``primitive_ontology_metrics`` expects),
        * ``"snake"``: ``made_from``,
        * ``"space"``: ``made from`` (``is-a`` and ``instance-of`` keep their hyphens).

        ``style=None`` returns the label stripped but otherwise unchanged.
        """
        if not isinstance(relation, str):
            return ""
        if style is None:
            return relation.strip()
        if style not in RELATION_STYLES:
            raise ValueError(f"relation style must be one of {RELATION_STYLES} or None, got {style!r}")
        relation = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", relation.strip())
        tokens = [t for t in re.split(r"[\s\-_]+", relation.lower()) if t]
        if style == "snake":
            return "_".join(tokens)
        hyphenated = "-".join(tokens)
        return hyphenated if style == "hyphen" or hyphenated in TAXONOMIC_RELATIONS else " ".join(tokens)

    @staticmethod
    def normalize_types(types: Sequence[str]) -> List[str]:
        """Lowercase, split known glued names, keep dot-notation codes and de-duplicate (order is kept)."""
        result, seen = [], set()
        for typ in types:
            if not isinstance(typ, str) or not typ.strip():
                continue
            typ = typ.strip().lower()
            if not re.match(r"^[a-z]\.[a-z]+$", typ):
                typ = _KNOWN_TYPE_SPLITS.get(typ, typ)
            if typ not in seen:
                seen.add(typ)
                result.append(typ)
        return result

    @staticmethod
    def is_invalid_entity(entity: str) -> bool:
        """Blank nodes (``_:b1``, ``q42``, ``node_7``...), empty or one-character labels, labels without letters."""
        entity = entity.strip()
        return len(entity) <= 1 or bool(_BLANK_NODE.match(entity)) or bool(_ONLY_PUNCT_OR_DIGITS.match(entity))

    def _normalize_triples(self, triples: Sequence[Sequence[str]]) -> Tuple[List[List[str]], List[str], int, int]:
        """Stages 2-4. Returns ``(triples, flagged long entities, n removed as blank/malformed, n duplicates)``."""
        normalized, valid = [], []
        for triple in triples:
            if isinstance(triple, (list, tuple)) and len(triple) == 3:
                head, relation, tail = (self.normalize_entity(str(triple[0])),
                                        self.normalize_relation(str(triple[1]), self.relation_style),
                                        self.normalize_entity(str(triple[2])))
                if head and relation and tail:
                    normalized.append([head, relation, tail])
                    # Blank nodes are also checked before normalisation, which turns "node_7" into "node 7"
                    # and "_:b1" into ":b1" so that the pattern no longer matches them.
                    if not any(self.is_invalid_entity(e) for e in (head, tail, str(triple[0]), str(triple[2]))):
                        valid.append([head, relation, tail])
        flagged = sorted({e for t in valid if max(len(t[0]), len(t[2])) > self.max_entity_length for e in (t[0], t[2])})
        kept, seen = [], set()
        for triple in valid:
            if tuple(triple) not in seen:
                seen.add(tuple(triple))
                kept.append(triple)
        return kept, flagged, len(normalized) - len(valid), len(valid) - len(kept)

    def _llm_clean(self, context: str, triples: List[List[str]], flagged: List[str],
                   stats: CleaningStats) -> Tuple[str, List[List[str]]]:
        """Stages 5-6: LLM pass, accepted only if it passes the safety checks."""
        stats.llm_called = True
        sent = context[: self.max_context_tokens * 4] if len(context) // 4 > self.max_context_tokens else context
        result = self._call_json(DEEP_CLEANING_PROMPT,
                                 json.dumps({"context": sent, "flagged_entities": flagged}, ensure_ascii=False))
        if result is None:
            stats.llm_fallback = True
            stats.flags.append("LLM call failed - using deterministic result")
            return context, triples

        new_context = result.get("context_cleaned")
        if isinstance(new_context, str) and new_context.strip():
            if len(new_context) / max(len(context), 1) > self.max_expansion_ratio:
                logger.warning("[%s] LLM context grew too much; reverting.", stats.record_id)
                stats.llm_context_reverted = True
                new_context = context
        else:
            stats.llm_context_reverted = True
            new_context = context

        corrections = result.get("entity_corrections") or {}
        if not isinstance(corrections, dict):
            return new_context, triples
        corrected = []
        for head, relation, tail in triples:
            new_head, new_tail = corrections.get(head, head), corrections.get(tail, tail)
            if not (isinstance(new_head, str) and isinstance(new_tail, str)) \
                    or self.is_invalid_entity(new_head) or self.is_invalid_entity(new_tail):
                new_head, new_tail = head, tail
            corrected.append([new_head, relation, new_tail])
        return new_context, corrected

    # ------------------------------------------------------------------ #
    # 4. Alignment filter (annotation.ipynb, LLM as judge)
    # ------------------------------------------------------------------ #
    def annotate_alignment(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Ask the LLM how well each context supports its triples.

        Returns:
            Copies of the records with an ``"annotation"`` of ``{"alignment", "rating", "rational"}``
            (``None`` only when ``annotation_retries`` is set and every attempt failed).
        """
        if self.client is None:
            raise ValueError("annotate_alignment needs an OpenAI `client`.")

        def _annotate(record: Dict[str, Any]) -> Dict[str, Any]:
            prompt = ALIGNMENT_PROMPT.format(text=record["context"], triples=record[TRIPLES_KEY])
            annotation = self._call_tool(prompt, "annotation", "Evaluate alignment between text and ontology triples.",
                                         ALIGNMENT_SCHEMA, self.annotation_retries)
            return {**record, "annotation": annotation}

        annotated = self._parallel_map(_annotate, records)
        failed = sum(r["annotation"] is None for r in annotated)
        if failed:
            logger.warning("%d of %d records could not be annotated; filter_by_alignment will drop them.", failed,
                           len(annotated))
        return annotated

    def filter_by_alignment(self, records: Union[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]
                            ) -> List[Dict[str, Any]]:
        """
        Keep records annotated ``aligned``, or ``partially_aligned`` with a rating of at least
        ``min_partial_rating``, as ``{"id", "context", "primitive-ontology-triples"}`` (the released train set has
        no ``terms`` or ``types``). Also accepts the ``{id: record}`` files written by annotation.ipynb.
        """
        def _keep(annotation: Optional[Dict[str, Any]]) -> bool:
            if not annotation:
                return False
            if annotation.get("alignment") == "aligned":
                return True
            try:
                return (annotation.get("alignment") == "partially_aligned"
                        and int(annotation.get("rating", 0)) >= self.min_partial_rating)
            except (TypeError, ValueError):
                return False

        items = records.values() if isinstance(records, dict) else records
        return [{"id": r["id"], "context": r["context"], TRIPLES_KEY: r[TRIPLES_KEY]}
                for r in items if _keep(r.get("annotation"))]

    @staticmethod
    def _non_taxonomic_triples(ontological_data: Union[OntologyData, Dict[str, Any]]) -> List[List[str]]:
        if isinstance(ontological_data, dict):
            relations = (ontological_data.get("type_non_taxonomic_relations") or {}).get("non_taxonomies") or []
            return [[r["head"], r["relation"], r["tail"]] for r in relations]
        section = getattr(ontological_data, "type_non_taxonomic_relations", None)
        return [[r.head, r.relation, r.tail] for r in (getattr(section, "non_taxonomies", None) or [])]

    def _call_tool(self, prompt: str, name: str, description: str, properties: Dict[str, Any],
                   attempts: Optional[int]) -> Optional[Dict[str, Any]]:
        """Force one function call and return its parsed arguments; ``None`` after ``attempts`` failures
        (``attempts=None`` retries until it succeeds)."""
        tool = {"type": "function",
                "function": {"name": name, "description": description,
                             "parameters": {"type": "object", "properties": properties,
                                            "required": list(properties)}}}
        attempt = 0
        while attempts is None or attempt < attempts:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    tools=[tool],
                    tool_choice={"type": "function", "function": {"name": name}},
                )
                return json.loads(response.choices[0].message.tool_calls[0].function.arguments)
            except Exception as exc:
                attempt += 1
                logger.warning("%s attempt %d/%s failed: %s", name, attempt, attempts or "unlimited", exc)
                if attempts is None or attempt < attempts:
                    time.sleep(min(2 ** (attempt - 1), 60))
        return None

    def _call_json(self, system_prompt: str, user_content: str) -> Optional[Dict[str, Any]]:
        """Request a JSON object from ``deep_clean_model``; ``None`` on invalid JSON (not retried) or after
        ``max_retries`` failures."""
        for attempt in range(self.max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=self.deep_clean_model,
                    temperature=0.0,
                    response_format={"type": "json_object"},
                    messages=[{"role": "system", "content": system_prompt},
                              {"role": "user", "content": user_content}],
                )
                raw = (response.choices[0].message.content or "").strip()
                raw = re.sub(r"\s*```$", "", re.sub(r"^```(?:json)?\s*", "", raw))
                return json.loads(raw)
            except json.JSONDecodeError as exc:
                logger.warning("LLM returned invalid JSON: %s", exc)
                return None
            except Exception as exc:
                logger.warning("JSON request attempt %d/%d failed: %s", attempt + 1, self.max_retries, exc)
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)
        return None

    def _parallel_map(self, func: Callable[[Any], Any], items: Sequence[Any]) -> List[Any]:
        """``map`` over a thread pool of ``max_workers``; results keep the input order."""
        if self.max_workers <= 1 or len(items) <= 1:
            return [func(item) for item in items]
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            return list(executor.map(func, items))