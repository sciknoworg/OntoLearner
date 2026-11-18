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
import random
import re
import time
import unicodedata
import uuid
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

from ..data_structure import OntologyData, SyntheticText2OntoData

logger = logging.getLogger(__name__)

class SyntheticDataPreprocessor:
    """
    Turns the documents of ``SyntheticGenerator`` into the samples of a primitive-ontology task. ``preprocess``
    runs the same five steps on train and test data:

    1. Records: every document is paired with the pseudo-sentences it was written from. Its ``is subclass of``
       and ``is instance of`` sentences become ``is-a`` and ``instance-of`` triples, and the ontology's
       non-taxonomic relations between the document's types are added.
    2. Text cleaning: the LLM (``model``) adds missing spaces to the text and to the triple labels, and drops an
       unfinished last sentence.
    3. Deep cleaning, in six stages: (1) structural cleanup of the text, (2) entity and type normalisation,
       (3) relation labels in ``relation_style``, (4) triples with invalid entities and duplicate triples
       removed, and with ``deep_clean_model`` (5) the text corrected and (6) overlong entities corrected.
    4. Alignment filter: an LLM judge rates how well each text supports its triples; the records rated
       ``aligned``, or ``partially_aligned`` with a rating of at least ``min_partial_rating``, are kept.
    5. Task samples, for ``task``:

       * ``"ontology_construction"`` (text -> complete ontology): ``{"id", "context", "terms", "types",
         "primitive-ontology-triples"}``; the triples are the target.
       * ``"ontology_expansion"`` (text + initial ontology -> extended ontology): each record's triples are
         split into an initial ontology and the triples that extend it (``split_triples``), giving ``{"id",
         "context", "terms", "types", "initial-primitive-ontology-triples",
         "extended-primitive-ontology-triples"}``, where ``terms`` and ``types`` are the entities of the extension
         triples. Records with nothing to extend are dropped.
    """

    TASKS = ("ontology_construction", "ontology_expansion")
    TRIPLES_KEY = "primitive-ontology-triples"
    INITIAL_KEY = "initial-primitive-ontology-triples"
    EXTENDED_KEY = "extended-primitive-ontology-triples"
    TAXONOMIC_RELATIONS = ("is-a", "instance-of")
    RELATION_STYLES = ("hyphen", "snake", "space")

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

    # Stage 1 of the cleaning: (pattern, replacement) rules applied to the text in this order, then
    # _BACKTICK_LABEL (with strip_backticks) and _SPACE_RULES.
    _TEXT_RULES = (
        # control characters
        (re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]"), ""),
        # escaped characters: \n, \t, \r, quotes, backslashes
        (re.compile(r"\\([ntr\"'\\])"),
         lambda m: {"n": "\n", "t": "\t", "r": ""}.get(m.group(1), m.group(1))),
        # XML comments
        (re.compile(r"<!--.*?-->", re.DOTALL), ""),
        # HTML/XML tags
        (re.compile(r"<[^>]{0,80}>"), ""),
        # HTML entities
        (re.compile(r"&(?:[a-zA-Z]{2,6}|#\d{1,5});"), " "),
        # stack traces
        (re.compile(r"(?:Traceback \(most recent call last\)|at \w+\.\w+\(.*?\)|\s+File \".*?\", line \d+).*",
                    re.DOTALL), ""),
        # JSON fragments
        (re.compile(r"\{\"[a-zA-Z_]+\":\s*[^}]{0,200}\}"), ""),
        # URLs
        (re.compile(r"https?://\S+"), ""),
        # repeated punctuation: !!! -> !
        (re.compile(r"([!?,;])\1{2,}"), r"\1"),
        # long ellipses: .... -> ...
        (re.compile(r"\.{4,}"), "..."),
        # -- and --- -> —
        (re.compile(r"(?<!\-)\-{2,3}(?!\-)"), "—"),
        # garbled opening quotes
        (re.compile(r"\bâ€œ\b|\bâ€˜\b"), '"'),
        # garbled closing quotes
        (re.compile(r"\bâ€\b|\bâ€™\b"), '"'),
        # doubled delimiters: ,, -> ,
        (re.compile(r"([,:;])\1+"), r"\1"),
    )
    _BACKTICK_LABEL = re.compile(r"`([^`]+)`")    # `label` -> label
    _SPACE_RULES = ((re.compile(r"[ \t]+"), " "), (re.compile(r"\n{3,}"), "\n\n"))

    # Stages 2 and 4 of the cleaning: entity normalisation and invalid entities
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

    def __init__(self,
                 client: Any,
                 task: str = "ontology_construction",
                 model: str = "gpt-4o-mini",
                 deep_clean_model: str = "gpt-5.4",
                 relation_style: Optional[str] = "hyphen",
                 min_partial_rating: int = 3,
                 max_entity_length: int = 120,
                 max_context_tokens: int = 3000,
                 max_expansion_ratio: float = 1.5,
                 max_retries: int = 5,
                 annotation_retries: Optional[int] = None,
                 max_workers: int = 10,
                 random_state: int = 42) -> None:
        """
        Args:
            client: ``openai.OpenAI`` client, used by the text cleaning, the deep cleaning and the alignment filter.
            task: ``"ontology_construction"`` or ``"ontology_expansion"``: the samples ``preprocess`` returns.
            model: OpenAI model that cleans the text and the labels and judges the alignment (the release used
                ``gpt-4o-mini``).
            deep_clean_model: OpenAI model of stages 5-6 of the deep cleaning (the release used ``gpt-5.4``).
            relation_style: The style the deep cleaning gives relation labels: ``"hyphen"`` (``is-defined-by``,
                the form ``primitive_ontology_metrics`` expects), ``"snake"`` (``is_defined_by``), ``"space"``
                (``is defined by``), or ``None`` to leave them as they are.
            min_partial_rating: Lowest judge rating at which a ``partially_aligned`` record is kept.
            max_entity_length: Triples with an entity longer than this many characters have their entities sent
                to the LLM for correction (stage 6).
            max_context_tokens: The text sent to the LLM in stage 5 is cut after about this many tokens.
            max_expansion_ratio: An LLM-corrected text longer than this many times the original is rejected, and
                the original is kept (stage 5).
            max_retries: Attempts per OpenAI request that cleans text or labels.
            annotation_retries: Attempts per judge request. ``None`` retries until the request succeeds, as in the
                release, so no record is lost to a failed request. With a number, a record whose requests all
                fail gets no rating and is dropped by ``filter_by_alignment``.
            max_workers: Number of OpenAI requests sent in parallel.
            random_state: Seed of the initial/extension split of ``ontology_expansion``. Every ``preprocess`` call
                starts from this seed, so the same records are always split the same way.
        """
        if client is None:
            raise ValueError("SyntheticDataPreprocessor needs an OpenAI `client`.")
        if task not in self.TASKS:
            raise ValueError(f"task must be one of {self.TASKS}, got {task!r}")
        if relation_style is not None and relation_style not in self.RELATION_STYLES:
            raise ValueError(f"relation_style must be one of {self.RELATION_STYLES} or None, got {relation_style!r}")
        self.client = client
        self.task = task
        self.model = model
        self.deep_clean_model = deep_clean_model
        self.relation_style = relation_style
        self.min_partial_rating = min_partial_rating
        self.max_entity_length = max_entity_length
        self.max_context_tokens = max_context_tokens
        self.max_expansion_ratio = max_expansion_ratio
        self.max_retries = max_retries
        self.annotation_retries = annotation_retries
        self.max_workers = max_workers
        self.random_state = random_state
        self.label_cache: Dict[str, str] = {"disjointWith": "disjoint with"}   # labels already cleaned

    # ------------------------------------------------------------------ #
    # Entry point
    # ------------------------------------------------------------------ #
    def preprocess(self,
                   synthetic_data: Union[SyntheticText2OntoData, List[Dict[str, Any]]],
                   ontological_data: OntologyData) -> List[Dict[str, Any]]:
        """
        Turn generated documents into the samples of ``task``, with all five steps of the class description.
        Call it once for the train documents and once for the test documents.

        Args:
            synthetic_data: What ``SyntheticGenerator.generate`` returned, or a list of items made from it by
                ``prepare_items`` (to process only some of the documents).
            ontological_data: The ontology (train or test part) the documents were generated from; its
                non-taxonomic relations are added to the records.

        Returns:
            The samples of ``task`` (see the class description), one per kept record.
        """
        items = synthetic_data if isinstance(synthetic_data, list) else self.prepare_items(synthetic_data)
        records = self._parallel_map(lambda item: self.prepare_record(item, ontological_data), items)
        records = self.deep_clean(records)
        records = self.filter_by_alignment(self.annotate_alignment(records))
        samples = self.prepare_samples(records)
        logger.info("Preprocessed %d documents into %d records and %d %s samples.", len(items), len(records),
                    len(samples), self.task)
        return samples

    # ------------------------------------------------------------------ #
    # Steps 1-2: documents -> records, with the LLM adding missing spaces
    # ------------------------------------------------------------------ #
    def prepare_items(self, synthetic_data: SyntheticText2OntoData) -> List[Dict[str, Any]]:
        """
        Pair every generated document with the pseudo-sentences it was written from (matched by ID). A
        document without pseudo-sentences is skipped with a warning.

        Returns:
            ``[{"id", "title", "text", "structured_data"}]``, where ``structured_data`` holds the document's
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

    def prepare_record(self, item: Dict[str, Any], ontological_data: OntologyData) -> Dict[str, Any]:
        """
        Turn one item of ``prepare_items`` into a record (steps 1-2 of the class description).

        Args:
            item: One item of ``prepare_items``.
            ontological_data: The ontology the document was generated from.

        Returns:
            ``{"id", "context", "terms", "types", "primitive-ontology-triples"}``, where ``id`` is a new random
            ID and ``context`` is ``"Title: <title> \\n\\n Content: \\n<text>"``.
        """
        structured = item["structured_data"]
        types = structured.get("types", []) or []
        triples = []
        for sentence in structured.get("pseudo_sentences", []) or []:
            for marker, relation in ((" is subclass of ", "is-a"), (" is instance of ", "instance-of")):
                if marker in sentence:
                    parts = sentence.split(marker)
                    triples.append([parts[0], relation, parts[1]])
                    break
            else:
                logger.warning("Unrecognised pseudo-sentence: %r", sentence)
        type_set = set(types)
        triples += [t for t in self._non_taxonomic_triples(ontological_data) if t[0] in type_set and t[2] in type_set]

        text = self.clean_context(item["text"])
        triples = self.clean_gold(triples)
        return {
            "id": uuid.uuid4().hex,
            "context": f"Title: {item['title']} \n\n Content: \n{text}",
            "terms": [term.lower() for term in structured.get("terms", []) or []],
            "types": [typ.lower() for typ in types],
            self.TRIPLES_KEY: triples,
        }

    def clean_context(self, text: str) -> str:
        """Ask the LLM to add missing spaces to ``text`` and drop an unfinished last sentence. If the request
        fails, ``text`` is returned unchanged."""
        result = self._call_tool(self.CONTEXT_CLEANING_PROMPT.format(context=text), "clean_paragraph",
                                 "Return a cleaned, well-formed paragraph.",
                                 {"paragraph": {"type": "string", "description": "The cleaned paragraph."}},
                                 self.max_retries)
        paragraph = (result or {}).get("paragraph")
        return paragraph if isinstance(paragraph, str) and paragraph.strip() else text

    def clean_gold(self, triples: Sequence[Sequence[str]]) -> List[List[str]]:
        """
        Add missing spaces to the head, relation and tail of every triple (``CompoundSubstance`` -> ``compound
        substance``), with ``clean_label``.

        Each label is sent to the LLM once and its answer kept in ``self.label_cache`` for later documents (the
        cache starts with ``disjointWith`` -> ``disjoint with``); ``is-a`` and ``instance-of`` are never sent.
        """
        return [[self.clean_label(head), self.clean_label(relation), self.clean_label(tail)]
                for head, relation, tail in triples]

    def clean_label(self, label: str) -> str:
        """Clean one label for ``clean_gold``: take it from ``self.label_cache``, or ask the LLM and cache the
        answer. A label the LLM could not clean is returned unchanged."""
        if label in self.TAXONOMIC_RELATIONS or label in self.label_cache:
            return self.label_cache.get(label, label)
        result = self._call_tool(self.LABEL_CLEANING_PROMPT.format(context=label), "clean_phrase",
                                 "Return a cleaned, well-formed phrase.",
                                 {"phrase": {"type": "string", "description": "The cleaned phrase."}},
                                 self.max_retries)
        phrase = (result or {}).get("phrase")
        if not (isinstance(phrase, str) and phrase.strip()):
            logger.warning("Label cleaning failed for %r; keeping it unchanged.", label)
            return label
        self.label_cache[label] = phrase
        return phrase

    # ------------------------------------------------------------------ #
    # Step 3: six-stage deep cleaning
    # ------------------------------------------------------------------ #
    def deep_clean(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Clean every record with ``deep_clean_record``. A record whose cleaning raises an error is logged and
        kept unchanged."""
        return self._parallel_map(self._deep_clean_or_keep, records)

    def _deep_clean_or_keep(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """``deep_clean_record``, or the record unchanged if cleaning it raises an error."""
        try:
            return self.deep_clean_record(record)
        except Exception as exc:
            logger.error("Cleaning failed for record %s, keeping it unchanged: %s", record.get("id"), exc)
            return record

    def deep_clean_record(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Clean one record in the six stages of the class description: ``structural_cleanup`` of the context,
        ``filter_triples`` (stages 2-4), ``normalize_types``, and the LLM stage (5-6).

        Returns:
            A cleaned copy of the record; the input record is not modified.
        """
        cleaned = copy.deepcopy(record)
        cleaned["context"] = self.structural_cleanup(cleaned.get("context", ""), strip_backticks=True)
        triples, flagged = self._normalize_triples(cleaned.get(self.TRIPLES_KEY, []))
        if isinstance(cleaned.get("types"), list):
            cleaned["types"] = self.normalize_types(cleaned["types"])
        if cleaned["context"]:
            cleaned["context"], triples = self._llm_clean(str(record.get("id", "?")), cleaned["context"],
                                                          triples, flagged)
        cleaned[self.TRIPLES_KEY] = triples
        return cleaned

    def filter_triples(self, triples: Sequence[Sequence[str]]) -> List[List[str]]:
        """Stages 2-4 of the cleaning: normalise the entities (``normalize_entity``) and relation labels
        (``normalize_relation`` in ``relation_style``), drop triples that are not ``[head, relation, tail]`` or
        have an empty, blank-node or otherwise invalid entity (``is_invalid_entity``), and remove duplicates."""
        return self._normalize_triples(triples)[0]

    def structural_cleanup(self, text: str, strip_backticks: bool = False) -> str:
        """Stage 1 of the cleaning, on a text: Unicode normalisation; removes control characters, HTML/XML tags
        and comments, HTML entities, URLs, stack traces and JSON fragments; repairs escaped characters, repeated
        punctuation, dashes and garbled quotes; removes backticks around labels (``strip_backticks``) and extra
        spaces and blank lines."""
        if not isinstance(text, str):
            return ""
        text = unicodedata.normalize("NFC", text)
        for pattern, replacement in self._TEXT_RULES:
            text = pattern.sub(replacement, text)
        if strip_backticks:
            text = self._BACKTICK_LABEL.sub(r"\1", text)
        for pattern, replacement in self._SPACE_RULES:
            text = pattern.sub(replacement, text)
        return text.strip()

    def normalize_entity(self, entity: str) -> str:
        """Stage 2 of the cleaning, for one entity. A label with capitals is split at CamelCase and hyphens and
        lowercased (``Non-MetalicCompound`` -> ``non metalic compound``); in an all-lowercase label underscores
        become spaces. Extra spaces are removed, and dot-notation codes such as ``H.PNDSN`` are kept as they
        are."""
        if not isinstance(entity, str):
            return ""
        entity = entity.strip()
        if self._DOT_NOTATION_CODE.match(entity):
            return entity
        entity = self._SPURIOUS_DOT_SPACE.sub(r"\1.\2", entity)
        if re.search(r"[A-Z]", entity):
            entity = entity.replace("-", " ")
            entity = re.sub(r"([a-z])([A-Z])", r"\1 \2", entity)
            entity = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", entity).lower()
        else:
            entity = entity.replace("_", " ")
        return re.sub(r"\s+", " ", entity).strip()

    def normalize_relation(self, relation: str, style: Optional[str] = "hyphen") -> str:
        """
        Stage 3 of the cleaning, for one relation label: write it in one style, lowercase. ``madeFrom``,
        ``made_from``, ``made-from`` and ``made from`` all become

        * ``"hyphen"``: ``made-from``, and ``is-a`` and ``instance-of`` stay as they are (the form
          ``primitive_ontology_metrics`` expects);
        * ``"snake"``: ``made_from``, and also ``is_a`` and ``instance_of``;
        * ``"space"``: ``made from``, but ``is-a`` and ``instance-of`` keep their hyphens.

        ``style=None`` only strips surrounding spaces.
        """
        if not isinstance(relation, str):
            return ""
        if style is None:
            return relation.strip()
        if style not in self.RELATION_STYLES:
            raise ValueError(f"relation style must be one of {self.RELATION_STYLES} or None, got {style!r}")
        relation = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", relation.strip())
        tokens = [t for t in re.split(r"[\s\-_]+", relation.lower()) if t]
        if style == "snake":
            return "_".join(tokens)
        hyphenated = "-".join(tokens)
        return hyphenated if style == "hyphen" or hyphenated in self.TAXONOMIC_RELATIONS else " ".join(tokens)

    def normalize_types(self, types: Sequence[str]) -> List[str]:
        """Normalise a record's ``types``: lowercase them, split a few known glued names (``amorphousmetal`` ->
        ``amorphous metal``), and remove empty entries and duplicates, keeping the order."""
        result, seen = [], set()
        for typ in types:
            if not isinstance(typ, str) or not typ.strip():
                continue
            typ = typ.strip().lower()
            if not re.match(r"^[a-z]\.[a-z]+$", typ):
                typ = self._KNOWN_TYPE_SPLITS.get(typ, typ)
            if typ not in seen:
                seen.add(typ)
                result.append(typ)
        return result

    def is_invalid_entity(self, entity: str) -> bool:
        """Stage 4 of the cleaning: ``True`` for an entity that is a blank node or placeholder (``_:b1``,
        ``q42``, ``node_7``, ``?x``), has at most one character, or consists only of digits and punctuation."""
        entity = entity.strip()
        return (len(entity) <= 1 or bool(self._BLANK_NODE.match(entity))
                or bool(self._ONLY_PUNCT_OR_DIGITS.match(entity)))

    def _normalize_triples(self, triples: Sequence[Sequence[str]]) -> Tuple[List[List[str]], List[str]]:
        """Stages 2-4 (see ``filter_triples``). Returns the kept triples, and the entities of the triples that
        have an entity longer than ``max_entity_length``, which the LLM stage is asked to correct."""
        valid = []
        for triple in triples:
            if isinstance(triple, (list, tuple)) and len(triple) == 3:
                head, relation, tail = (self.normalize_entity(str(triple[0])),
                                        self.normalize_relation(str(triple[1]), self.relation_style),
                                        self.normalize_entity(str(triple[2])))
                # Blank nodes are also checked before normalisation, which turns "node_7" into "node 7"
                # and "_:b1" into ":b1" so that the pattern no longer matches them.
                if head and relation and tail and \
                        not any(self.is_invalid_entity(e) for e in (head, tail, str(triple[0]), str(triple[2]))):
                    valid.append([head, relation, tail])
        flagged = sorted({e for t in valid if max(len(t[0]), len(t[2])) > self.max_entity_length for e in (t[0], t[2])})
        kept, seen = [], set()
        for triple in valid:
            if tuple(triple) not in seen:
                seen.add(tuple(triple))
                kept.append(triple)
        return kept, flagged

    def _llm_clean(self, record_id: str, context: str, triples: List[List[str]],
                   flagged: List[str]) -> Tuple[str, List[List[str]]]:
        """
        Stages 5-6 of the cleaning. The LLM gets the context (cut after ``max_context_tokens``) and the flagged
        entities, and returns a corrected context and entity corrections. A corrected context is rejected when it
        is more than ``max_expansion_ratio`` times longer than the original; an entity correction is rejected
        when it is not a string or is an invalid entity (``is_invalid_entity``). If the request fails, the
        context and triples are returned unchanged.

        Returns:
            ``(context, triples)``.
        """
        sent = context[: self.max_context_tokens * 4] if len(context) // 4 > self.max_context_tokens else context
        result = self._call_json(self.DEEP_CLEANING_PROMPT,
                                 json.dumps({"context": sent, "flagged_entities": flagged}, ensure_ascii=False))
        if result is None:
            logger.warning("[%s] LLM cleaning failed; using the deterministic result.", record_id)
            return context, triples

        new_context = result.get("context_cleaned")
        if isinstance(new_context, str) and new_context.strip():
            if len(new_context) / max(len(context), 1) > self.max_expansion_ratio:
                logger.warning("[%s] LLM context grew too much; reverting.", record_id)
                new_context = context
        else:
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
    # Step 4: alignment filter, an LLM as judge
    # ------------------------------------------------------------------ #
    def annotate_alignment(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Ask the LLM judge how well each context supports its triples.

        Returns:
            Copies of the records, each with an ``"annotation"``: ``{"alignment", "rating", "rational"}``, where
            ``alignment`` is ``aligned``, ``partially_aligned`` or ``not_aligned`` and ``rating`` goes from 1
            (poor) to 5 (excellent). The annotation is ``None`` only when ``annotation_retries`` is set and every
            attempt failed.
        """
        annotated = self._parallel_map(self._annotate, records)
        failed = sum(r["annotation"] is None for r in annotated)
        if failed:
            logger.warning("%d of %d records could not be annotated; filter_by_alignment will drop them.", failed,
                           len(annotated))
        return annotated

    def _annotate(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """A copy of ``record`` with the judge's ``"annotation"``."""
        prompt = self.ALIGNMENT_PROMPT.format(text=record["context"], triples=record[self.TRIPLES_KEY])
        annotation = self._call_tool(prompt, "annotation", "Evaluate alignment between text and ontology triples.",
                                     self.ALIGNMENT_SCHEMA, self.annotation_retries)
        return {**record, "annotation": annotation}

    def filter_by_alignment(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Keep the records ``annotate_alignment`` rated ``aligned``, or ``partially_aligned`` with a rating of at
        least ``min_partial_rating``. They are returned without their ``"annotation"``.
        """
        return [{key: value for key, value in r.items() if key != "annotation"}
                for r in records if self._is_aligned(r.get("annotation"))]

    def _is_aligned(self, annotation: Optional[Dict[str, Any]]) -> bool:
        """Whether ``filter_by_alignment`` keeps a record with this annotation."""
        if not annotation:
            return False
        if annotation.get("alignment") == "aligned":
            return True
        try:
            return (annotation.get("alignment") == "partially_aligned"
                    and int(annotation.get("rating", 0)) >= self.min_partial_rating)
        except (TypeError, ValueError):
            return False

    def _non_taxonomic_triples(self, ontological_data: OntologyData) -> List[List[str]]:
        """The ontology's non-taxonomic relations as ``[head, relation, tail]`` triples."""
        section = getattr(ontological_data, "type_non_taxonomic_relations", None)
        return [[r.head, r.relation, r.tail] for r in (getattr(section, "non_taxonomies", None) or [])]

    # ------------------------------------------------------------------ #
    # Step 5: task samples (ontology construction or expansion)
    # ------------------------------------------------------------------ #
    def prepare_samples(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Turn records into the samples of ``task`` (step 5 of the class description). ``preprocess`` calls it
        last; call it directly to turn records you already have into samples.

        Returns:
            For ``ontology_construction``, one sample per record. For ``ontology_expansion``, one sample per
            record with at least one triple to extend; the split is seeded with ``random_state``.
        """
        if self.task == "ontology_construction":
            return [{"id": r["id"],
                     "context": r["context"],
                     "terms": list(r.get("terms", [])),
                     "types": list(r.get("types", [])),
                     self.TRIPLES_KEY: [list(triple) for triple in r[self.TRIPLES_KEY]]}
                    for r in records]

        rng = random.Random(self.random_state)
        samples = []
        for record in records:
            initial, extended = self.split_triples(record[self.TRIPLES_KEY], rng)
            if not extended:
                continue
            terms, types = set(), set()
            for head, relation, tail in extended:
                if self.normalize_relation(relation, "hyphen") == "instance-of":
                    terms.add(head)
                else:
                    types.add(head)
                types.add(tail)
            samples.append({"id": record["id"],
                            "context": record["context"],
                            "terms": sorted(terms),
                            "types": sorted(types),
                            self.INITIAL_KEY: initial,
                            self.EXTENDED_KEY: extended})
        return samples

    def split_triples(self, triples: Sequence[Sequence[str]],
                      rng: random.Random) -> Tuple[List[List[str]], List[List[str]]]:
        """
        Split a record's triples into an initial ontology and the triples that extend it, for
        ``ontology_expansion``. The shuffled triples are grouped by tail; the first half of each group (at least one
        triple) goes to the initial ontology and the rest to the extension.

        Returns:
            ``(initial, extended)``.
        """
        shuffled = [list(triple) for triple in triples]
        rng.shuffle(shuffled)
        groups: Dict[str, List[List[str]]] = {}
        for triple in shuffled:
            groups.setdefault(triple[2], []).append(triple)
        initial, extended = [], []
        for group in groups.values():
            cut = max(1, len(group) // 2)
            initial.extend(group[:cut])
            extended.extend(group[cut:])
        return initial, extended

    # ------------------------------------------------------------------ #
    # OpenAI requests
    # ------------------------------------------------------------------ #
    def _call_tool(self, prompt: str, name: str, description: str, properties: Dict[str, Any],
                   attempts: Optional[int]) -> Optional[Dict[str, Any]]:
        """Send ``prompt`` to ``model`` with one function (tool) the model must call, and return the arguments
        of the call. Failed requests are retried with a growing pause; ``None`` is returned after ``attempts``
        failures (``attempts=None`` retries until a request succeeds)."""
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
        """Ask ``deep_clean_model`` for a JSON object and return it. Returns ``None`` if the answer is not valid
        JSON (not retried) or after ``max_retries`` failed requests."""
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
        """Apply ``func`` to every item with ``max_workers`` threads; the results keep the order of the items."""
        if self.max_workers <= 1 or len(items) <= 1:
            return [func(item) for item in items]
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            return list(executor.map(func, items))
