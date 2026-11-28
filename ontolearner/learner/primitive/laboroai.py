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
import logging
import os
import re
import string
from collections import Counter
from typing import Any, Dict, List, Optional, Sequence, Set

import networkx as nx
import numpy as np

from ...base import PrimitiveOntologyLearner

logger = logging.getLogger(__name__)


class LaboroAIPrimitiveLearner(PrimitiveOntologyLearner):
    """
    Few-shot LLM learner for ontology construction and expansion (the LaboroAI submission).

    For each document, it retrieves the ``k`` most similar training records (BM25, plus embeddings if
    ``use_dense``), asks the model once for tab-separated triples, and cleans the answer with fixed rules.
    For expansion, it keeps only new triples between the record's seed terms.

    Example::

        learner = LaboroAIPrimitiveLearner(model_id="gpt-5.4", api_key=api_key)
        learner.load()
        learner.fit(train_data, task="ontology_construction", ontologizer=False)
        predictions = learner.predict(test_data, task="ontology_construction", ontologizer=False)

    ``get_config()`` returns the current settings, and ``build_prompt(text)`` shows the prompt for a text.
    """

    def __init__(self, model_id: str = "gpt-5.4", k: int = 6, use_dense: bool = True, *,
                 # Model and API
                 api_key: Optional[str] = None,
                 base_url: Optional[str] = None,
                 temperature: float = 0.0,
                 max_completion_tokens: int = 2048,
                 # Retrieval of examples
                 dense_model_id: str = "all-MiniLM-L6-v2",
                 device: Optional[str] = None,
                 # Relations
                 predicates: Optional[Sequence[str]] = None,
                 symmetric_predicates: Optional[Sequence[str]] = None,
                 # Prompt
                 prompt_template: Optional[str] = None,
                 candidate_terms_block: Optional[str] = None,
                 examples_block: Optional[str] = None,
                 example_format: Optional[str] = None,
                 # Record fields
                 construction_target: str = "primitive-ontology-triples",
                 expansion_target: str = "extended-primitive-ontology-triples",
                 initial_key: str = "initial-primitive-ontology-triples") -> None:
        """
        Args:
            model_id: LLM that writes the triples; ``gemini*`` models use Google's OpenAI-compatible endpoint.
            k: Training records shown as examples per document.
            use_dense: Retrieve with sentence embeddings as well as BM25.
            api_key: API key; ``None`` reads ``OPENAI_API_KEY`` (``GEMINI_API_KEY`` for ``gemini*`` models).
            base_url: Another OpenAI-compatible endpoint.
            temperature: Sampling temperature.
            max_completion_tokens: Longest answer, in tokens.
            dense_model_id: Sentence-transformers model for dense retrieval.
            device: Device of that model (``"cpu"``, ``"cuda"``); ``None`` picks one.
            predicates: Relations the model may use; ``None`` uses the submission's 26.
            symmetric_predicates: Relations mirrored when cleaning (``A p B`` adds ``B p A``); ``None`` uses
                ``"disjoint with"`` and ``"equivalent class"`` if they are in ``predicates``.
            prompt_template: The prompt, with ``{predicates}``, ``{candidate_terms}``, ``{examples}`` and
                ``{context}`` (required); ``None`` uses the submission's.
            candidate_terms_block: Text for ``{candidate_terms}`` (expansion); must contain ``{terms}``.
            examples_block: Text for ``{examples}``; must contain ``{examples}``.
            example_format: One example; must contain ``{context}`` and ``{triples}``.
            construction_target: Record field holding the triples (construction).
            expansion_target: Record field holding the triples to add (expansion).
            initial_key: Record field holding the seed triples (expansion).

        Raises:
            ValueError: If a setting is invalid, such as a prompt template without ``{context}``.
        """
        super().__init__()
        if k < 1:
            raise ValueError("k must be at least 1.")

        # ---- Model and API ----
        self.model_id = model_id
        self.api_key = api_key
        self.base_url = base_url
        self.temperature = temperature
        self.max_completion_tokens = max_completion_tokens
        self.client = None  # OpenAI SDK client, created by load()

        # ---- Retrieval of examples ----
        self.k = k
        self.use_dense = use_dense
        self.dense_model_id = dense_model_id
        self.device = device

        # ---- Relations ----
        if predicates is None:
            # The submission's relations, in the order the prompt lists them.
            predicates = [
                "is-a", "instance-of", "is defined by", "equivalent class", "disjoint with",
                "type", "part_of", "has part", "exact match", "same as", "database_cross_reference",
                "overlaps", "located in", "term replaced by", "see also", "broader",
                "develops_from", "derives from", "regulates", "positively regulates",
                "is_conjugate_base_of", "is_conjugate_acid_of", "has role", "domain", "range", "tree view",
            ]
        self.predicates: List[str] = list(predicates)
        if not self.predicates:
            raise ValueError("predicates must not be empty.")

        if symmetric_predicates is None:
            # Relations where "A p B" also means "B p A"; only those the learner may use.
            symmetric_predicates = [p for p in ("disjoint with", "equivalent class") if p in self.predicates]
        self.symmetric_predicates: Set[str] = set(symmetric_predicates)
        unknown = sorted(self.symmetric_predicates - set(self.predicates))
        if unknown:
            raise ValueError(f"symmetric_predicates must be among predicates; not found: {unknown}.")

        # ---- Prompt ----
        if prompt_template is None:
            # The submission's prompt; build_prompt fills the {placeholders}.
            prompt_template = (
                "You extract ontology triples from scientific text.\n"
                "Output ONLY triples, one per line, tab-separated: subject<TAB>predicate<TAB>object\n"
                "\n"
                "PREDICATE VOCABULARY, use ONLY these, with exact spelling:\n"
                "{predicates}\n"
                "{candidate_terms}\n"
                "RULES:\n"
                "1. Lowercase only for all subjects and objects.\n"
                "2. Only emit triples DIRECTLY supported by the text, missing a triple is far less harmful "
                "than emitting a wrong one.\n"
                "3. is-a vs instance-of: if there can be multiple things of this kind, use is-a; if it names "
                "a unique individual, use instance-of.\n"
                "4. Never emit cycles (A is-a B and B is-a A simultaneously).\n"
                "{examples}\n"
                "Text: {context}\n"
                "Triples:"
            )
        if candidate_terms_block is None:
            candidate_terms_block = "\nCandidate terms (from the seed ontology, use if relevant): {terms}\n"
        if examples_block is None:
            examples_block = "\nExamples:\n{examples}\n"
        if example_format is None:
            example_format = "Context: {context}\nTriples:\n{triples}"
        # Checked now, so that a typo in a placeholder fails here and not at the first prediction.
        self.prompt_template = self._check_template(
            "prompt_template", prompt_template,
            allowed=("predicates", "candidate_terms", "examples", "context"), required=("context",))
        self.candidate_terms_block = self._check_template("candidate_terms_block", candidate_terms_block, ("terms",))
        self.examples_block = self._check_template("examples_block", examples_block, ("examples",))
        self.example_format = self._check_template("example_format", example_format, ("context", "triples"))

        # ---- Record fields: where the triples are in the records ----
        self.construction_target = construction_target
        self.expansion_target = expansion_target
        self.initial_key = initial_key

        # ---- Built by fit(): the examples, their retrieval index and the gazetteer of their spellings ----
        self.pool: List[Dict[str, Any]] = []
        self.bm25 = None
        self.dense_model = None
        self.dense_active = False  # False when use_dense=False or the encoder could not be loaded
        self.pool_embeddings = None
        self.gazetteer: Dict[str, str] = {}

    def _check_template(self, name: str, template: str, allowed: Sequence[str],
                        required: Optional[Sequence[str]] = None) -> str:
        """Return the template if its placeholders are allowed and include the required ones."""
        required = allowed if required is None else required
        try:
            fields = {field for _, field, _, _ in string.Formatter().parse(template) if field is not None}
        except ValueError as exc:
            raise ValueError(
                f"{name} is not a valid template ({exc}). Write literal braces as {{{{ and }}}}."
            ) from None
        unknown = sorted(fields - set(allowed))
        if unknown:
            raise ValueError(
                f"{name} has unknown placeholders " + ", ".join("{" + f + "}" for f in unknown)
                + "; allowed are " + ", ".join("{" + f + "}" for f in allowed)
                + ". Write literal braces as {{ and }}."
            )
        missing = [f for f in required if f not in fields]
        if missing:
            raise ValueError(f"{name} must contain " + " and ".join("{" + f + "}" for f in missing) + ".")
        return template

    def get_config(self) -> Dict[str, Any]:
        """Return the current settings as a dict of ``__init__`` arguments, without ``api_key``."""
        return {
            # Model and API
            "model_id": self.model_id,
            "base_url": self.base_url,
            "temperature": self.temperature,
            "max_completion_tokens": self.max_completion_tokens,
            # Retrieval of examples
            "k": self.k,
            "use_dense": self.use_dense,
            "dense_model_id": self.dense_model_id,
            "device": self.device,
            # Relations
            "predicates": list(self.predicates),
            "symmetric_predicates": sorted(self.symmetric_predicates),
            # Prompt
            "prompt_template": self.prompt_template,
            "candidate_terms_block": self.candidate_terms_block,
            "examples_block": self.examples_block,
            "example_format": self.example_format,
            # Record fields
            "construction_target": self.construction_target,
            "expansion_target": self.expansion_target,
            "initial_key": self.initial_key,
        }

    # ----------------------------------------------------------------------------------------------------------------
    # Model access
    # ----------------------------------------------------------------------------------------------------------------

    def _is_gemini(self, model: str) -> bool:
        """Whether the model is called through Gemini's OpenAI-compatible endpoint."""
        return model.startswith("gemini")

    def load(self, model_id: Optional[str] = None, **kwargs: Any) -> None:
        """Create the API client for ``model_id``, or for the model given here."""
        if model_id is not None:
            self.model_id = model_id
        from openai import OpenAI

        key_env = "GEMINI_API_KEY" if self._is_gemini(self.model_id) else "OPENAI_API_KEY"
        api_key = self.api_key or os.getenv(key_env)
        if not api_key:
            raise EnvironmentError(
                f"No API key for '{self.model_id}': pass api_key=... to {type(self).__name__}, or set the "
                f"{key_env} environment variable."
            )
        # gemini* models: Google's OpenAI-compatible endpoint, so the same OpenAI SDK calls work.
        gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
        base_url = self.base_url or (gemini_url if self._is_gemini(self.model_id) else None)
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def call_llm(self, prompt: str) -> str:
        """Send one prompt to the model and return its answer."""
        if self.client is None:
            raise RuntimeError("Call load() before calling the model.")
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            max_completion_tokens=self.max_completion_tokens,
        )
        return response.choices[0].message.content or ""

    # ----------------------------------------------------------------------------------------------------------------
    # Framework hooks (called by fit and predict)
    # ----------------------------------------------------------------------------------------------------------------

    def _ontology_construction(self, data: Any, test: bool = False) -> Optional[Any]:
        """Index the training records, or predict the triples of each test record."""
        samples = data if isinstance(data, list) else [data]
        if test:
            return self._predict(samples, task="ontology_construction")
        self._fit(samples, task="ontology_construction")
        return None

    def _ontology_expansion(self, data: Any, test: bool = False) -> Optional[Any]:
        """Index the training records, or predict the new triples of each test record."""
        samples = data if isinstance(data, list) else [data]
        if test:
            return self._predict(samples, task="ontology_expansion")
        self._fit(samples, task="ontology_expansion")
        return None

    def _pool_entry(self, sample: Dict[str, Any], task: str) -> Dict[str, Any]:
        """Turn a training record into an example: its text and all its triples."""
        if task == "ontology_construction":
            if self.construction_target not in sample:
                raise ValueError(f"Construction training records need '{self.construction_target}'.")
            triples = sample[self.construction_target]
        else:
            if self.expansion_target not in sample:
                raise ValueError(f"Expansion training records need '{self.expansion_target}'.")
            # An expansion example shows the full ontology: the seed triples plus the added ones.
            triples = list(sample.get(self.initial_key) or []) + list(sample[self.expansion_target])
        return {"context": sample["context"], self.construction_target: self.dedupe([list(t) for t in triples])}

    def _fit(self, data: List[Dict[str, Any]], task: str) -> None:
        """Build the example pool, the retrieval index and the gazetteer."""
        pool = [self._pool_entry(sample, task) for sample in data]
        if not pool:
            raise ValueError(f"{type(self).__name__} needs at least one labeled training record for its example pool.")
        self._index_pool(pool)
        self.gazetteer = self.build_gazetteer(pool)

    def _predict(self, data: List[Dict[str, Any]], task: str) -> List[Dict[str, Any]]:
        """Predict the triples of every record, with one model call each."""
        self._require_fit()
        if self.client is None:
            raise RuntimeError("Call load() before predict().")
        target = self.construction_target if task == "ontology_construction" else self.expansion_target
        predictions = []
        for sample in data:
            raw = self.call_llm(self.build_task_prompt(sample, task))
            predictions.append({"id": sample["id"], target: self._finalise(sample, raw, task)})
        return predictions

    def _finalise(self, sample: Dict[str, Any], raw: str, task: str) -> List[List[str]]:
        """Parse an answer and post-process its triples for the task."""
        triples = self.parse_triples(raw)
        if task == "ontology_construction":
            return self.postprocess(triples, gazetteer=self.gazetteer)
        # Expansion: no gazetteer (the seed terms define the spellings); keep only new triples, and only
        # those between the record's own terms.
        triples = self.postprocess(triples)
        triples = self.subtract_seed_triples(triples, sample.get(self.initial_key, []))
        return self.filter_to_allowed_terms(triples, self.seed_terms(sample))

    def _require_fit(self) -> None:
        if self.bm25 is None:
            raise RuntimeError("Call fit() with labeled training records first.")

    # ----------------------------------------------------------------------------------------------------------------
    # Extraction
    # ----------------------------------------------------------------------------------------------------------------

    def extract_triples(self, context: str) -> List[List[str]]:
        """Extract the triples of any text, as construction does. Needs ``fit`` and ``load``."""
        return self._finalise({"context": context}, self.call_llm(self.build_task_prompt(
            {"context": context}, "ontology_construction")), "ontology_construction")

    # ----------------------------------------------------------------------------------------------------------------
    # Retrieval of examples
    # ----------------------------------------------------------------------------------------------------------------

    def _tokenize(self, text: str) -> List[str]:
        """Split text into lowercase word tokens for BM25."""
        return re.findall(r"\w+", text.lower())

    def _rank_norm(self, scores: np.ndarray) -> np.ndarray:
        """Turn scores into ranks scaled to [0, 1], 1 for the best."""
        order = np.argsort(-scores)
        ranks = np.empty_like(order, dtype=float)
        ranks[order] = np.arange(len(scores))
        return 1.0 - ranks / max(len(scores) - 1, 1)

    def _index_pool(self, pool: List[Dict[str, Any]]) -> None:
        """Index the examples with BM25 and, if available, sentence embeddings."""
        from rank_bm25 import BM25Okapi

        self.pool = pool
        self.bm25 = BM25Okapi([self._tokenize(s["context"]) for s in pool])
        self.dense_active = self.use_dense
        self.pool_embeddings = None
        if self.dense_active:
            try:
                if self.dense_model is None:
                    from sentence_transformers import SentenceTransformer
                    self.dense_model = SentenceTransformer(self.dense_model_id, device=self.device)
                self.pool_embeddings = self.dense_model.encode(
                    [s["context"] for s in pool], normalize_embeddings=True
                )
            except Exception as exc:
                # Retrieval still works without embeddings, so fall back instead of failing.
                logger.warning("Dense retrieval is off, BM25 only: could not use %s (%s).", self.dense_model_id, exc)
                self.dense_active = False

    def _retrieve_indices(self, query_context: str) -> List[int]:
        """Return the indices of the ``k`` examples most similar to a text."""
        bm25_scores = np.array(self.bm25.get_scores(self._tokenize(query_context)))
        combined = self._rank_norm(bm25_scores)
        if self.dense_active and len(self.pool) > 0:
            # Average the two rankings rather than the raw scores, whose scales differ.
            q_emb = self.dense_model.encode([query_context], normalize_embeddings=True)[0]
            dense_scores = self.pool_embeddings @ q_emb
            combined = 0.5 * combined + 0.5 * self._rank_norm(dense_scores)
        top_idx = np.argsort(-combined)[: self.k]
        return top_idx.tolist()

    def retrieve(self, context: str) -> List[Dict[str, Any]]:
        """Return the ``k`` training records most similar to a text. Needs ``fit``."""
        self._require_fit()
        return [self.pool[i] for i in self._retrieve_indices(context)]

    def format_examples(self, examples: List[Dict[str, Any]]) -> str:
        """Format records as prompt examples, with ``example_format``."""
        blocks = []
        for sample in examples:
            triple_lines = "\n".join(f"{s}\t{p}\t{o}" for s, p, o in sample[self.construction_target])
            blocks.append(self.example_format.format(context=sample["context"], triples=triple_lines))
        return "\n\n".join(blocks)

    # ----------------------------------------------------------------------------------------------------------------
    # Prompts and answers
    # ----------------------------------------------------------------------------------------------------------------

    def build_prompt(self, context: str, few_shot_text: str = "",
                     candidate_terms: Optional[List[str]] = None) -> str:
        """Fill ``prompt_template`` for a text. Needs neither ``fit`` nor ``load``."""
        return self.prompt_template.format(
            predicates="\n".join(f"  {p}" for p in self.predicates),
            candidate_terms=self.candidate_terms_block.format(terms=", ".join(candidate_terms))
            if candidate_terms else "",
            examples=self.examples_block.format(examples=few_shot_text) if few_shot_text else "",
            context=context,
        )

    def build_task_prompt(self, sample: Dict[str, Any], task: str) -> str:
        """Build the prompt that ``predict`` sends for a record. Needs ``fit``."""
        context = sample["context"]
        few_shot_text = self.format_examples(self.retrieve(context)) if self.pool else ""
        candidate_terms = self.seed_terms(sample) if task == "ontology_expansion" else None
        return self.build_prompt(context, few_shot_text=few_shot_text, candidate_terms=candidate_terms)

    def parse_triples(self, raw_text: str) -> List[List[str]]:
        r"""
        Read ``subject<TAB>predicate<TAB>object`` lines from a model answer; other lines are skipped.

        Example:
            >>> LaboroAIPrimitiveLearner().parse_triples("1. Wheel\tpart_of\tCar\nSure, here you go:")
            [['wheel', 'part_of', 'car']]
        """
        # One answer line: an optional bullet ("- ", "* ") or number ("1. ", "2) "), then three tab-separated fields.
        triple_line = re.compile(r"^\s*(?:[-*]\s*|\d+[.)]\s*)?(.+?)\t(.+?)\t(.+?)\s*$")
        triples = []
        for line in raw_text.splitlines():
            m = triple_line.match(line)
            if not m:
                continue
            s, p, o = (x.strip().lower() for x in m.groups())
            if p not in self.predicates:
                continue
            triples.append([s, p, o])
        return triples

    # ----------------------------------------------------------------------------------------------------------------
    # Cleaning rules
    # ----------------------------------------------------------------------------------------------------------------

    def postprocess(self, triples: List[List[str]], gazetteer: Optional[Dict[str, str]] = None) -> List[List[str]]:
        """
        Clean triples: normalize, respell with the gazetteer, dedupe, drop self-loops and cycles, mirror.

        Example:
            >>> LaboroAIPrimitiveLearner().postprocess([["Person", "is-a", "Agent"], ["person", "is-a", "person"],
            ...                                         ["Image", "disjoint with", "Person"]])
            [['person', 'is-a', 'agent'], ['image', 'disjoint with', 'person'], ['person', 'disjoint with', 'image']]
        """
        triples = self.normalize(triples)
        if gazetteer:
            triples = self.gazetteer_snap(triples, gazetteer)
        triples = self.dedupe(triples)
        triples = self.drop_self_isa(triples)
        triples = self.break_cycles(triples)
        triples = self.mirror_symmetric(triples)
        triples = self.dedupe(triples)
        return triples

    def _norm_span(self, s: str) -> str:
        """Normalize an entity: lowercase, underscores to spaces, single spaces, no trailing punctuation."""
        s = s.strip().lower().replace("_", " ")
        s = re.sub(r"\s+", " ", s)
        return s.rstrip(".,;:").strip()

    def normalize(self, triples: List[List[str]]) -> List[List[str]]:
        """Tidy entities (lowercase, no underscores); drop triples with an empty entity or unknown predicate."""
        out = []
        for s, p, o in triples:
            s2, o2 = self._norm_span(s), self._norm_span(o)
            if p in self.predicates and s2 and o2:
                out.append([s2, p, o2])
        return out

    def build_gazetteer(self, examples: List[Dict[str, Any]]) -> Dict[str, str]:
        """Map each entity of the records, written without spaces, to its preferred spelling."""
        variants: Dict[str, Counter] = {}
        for sample in examples:
            for s, p, o in sample.get(self.construction_target, []):
                for span in (s, o):
                    span_n = self._norm_span(span)
                    key = span_n.replace(" ", "")
                    variants.setdefault(key, Counter())[span_n] += 1
        gazetteer = {}
        for key, counter in variants.items():
            canonical = sorted(counter.items(), key=lambda kv: (-kv[0].count(" "), -kv[1], kv[0]))[0][0]
            gazetteer[key] = canonical
        return gazetteer

    def gazetteer_snap(self, triples: List[List[str]], gazetteer: Dict[str, str]) -> List[List[str]]:
        """Respell entities with a gazetteer from ``build_gazetteer``."""
        out = []
        for s, p, o in triples:
            out.append([gazetteer.get(s.replace(" ", ""), s), p, gazetteer.get(o.replace(" ", ""), o)])
        return out

    def dedupe(self, triples: List[List[str]]) -> List[List[str]]:
        """Remove duplicate triples, keeping the first of each."""
        seen = set()
        out = []
        for t in triples:
            key = tuple(t)
            if key not in seen:
                seen.add(key)
                out.append(t)
        return out

    def drop_self_isa(self, triples: List[List[str]]) -> List[List[str]]:
        """Drop ``is-a`` triples whose subject and object are the same."""
        return [[s, p, o] for s, p, o in triples if not (p == "is-a" and s == o)]

    def break_cycles(self, triples: List[List[str]]) -> List[List[str]]:
        """Remove ``is-a`` edges until there are no cycles; from each cycle, the edge whose subject sorts last."""
        isa_edges = [(s, o) for s, p, o in triples if p == "is-a"]
        other = [[s, p, o] for s, p, o in triples if p != "is-a"]
        g = nx.DiGraph()
        g.add_edges_from(isa_edges)
        while True:
            try:
                cycle = nx.find_cycle(g)
            except nx.NetworkXNoCycle:
                break
            edge_to_drop = max(cycle, key=lambda e: e[0])
            g.remove_edge(edge_to_drop[0], edge_to_drop[1])
        return [[s, "is-a", o] for s, o in g.edges()] + other

    def mirror_symmetric(self, triples: List[List[str]]) -> List[List[str]]:
        """Add the missing reverse of each triple with a symmetric predicate."""
        existing = set(map(tuple, triples))
        mirrored = list(triples)
        for s, p, o in triples:
            if p in self.symmetric_predicates and (o, p, s) not in existing:
                mirrored.append([o, p, s])
                existing.add((o, p, s))
        return mirrored

    # ----------------------------------------------------------------------------------------------------------------
    # Expansion: seed terms and filters
    # ----------------------------------------------------------------------------------------------------------------

    def _triple_entities(self, triples: List[List[str]]) -> Set[str]:
        """Return the subjects and objects of the triples."""
        ents = set()
        for s, p, o in triples:
            ents.add(s)
            ents.add(o)
        return ents

    def seed_terms(self, sample: Dict[str, Any]) -> List[str]:
        """Return a record's seed terms: its terms, its types and the entities of its seed triples."""
        terms = set(sample.get("terms", [])) | set(sample.get("types", []))
        terms |= self._triple_entities(sample.get(self.initial_key, []))
        return sorted({self._norm_span(t) for t in terms if t})

    def subtract_seed_triples(self, triples: List[List[str]], initial_triples: List[List[str]]) -> List[List[str]]:
        """Drop the triples that the seed ontology already has."""
        seed_set = {tuple(self._norm_span(x) for x in t) for t in initial_triples}
        return [t for t in triples if tuple(self._norm_span(x) for x in t) not in seed_set]

    def filter_to_allowed_terms(self, triples: List[List[str]], allowed_terms: List[str]) -> List[List[str]]:
        """Keep the triples whose subject and object are both allowed terms."""
        allowed = set(allowed_terms)
        return [[s, p, o] for s, p, o in triples if self._norm_span(s) in allowed and self._norm_span(o) in allowed]