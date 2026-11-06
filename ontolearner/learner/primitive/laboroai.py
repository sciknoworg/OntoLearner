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
from collections import Counter
from typing import Any, Dict, List, Optional

import networkx as nx
import numpy as np

from ...base import PrimitiveOntologyLearner

class LaboroAIPrimitiveLearner(PrimitiveOntologyLearner):
    """
    Few-shot LLM learner for primitive ontology construction and expansion.

    ``fit`` indexes the training records as examples; nothing is trained. ``predict`` retrieves the most
    similar examples for each document, asks the model for its triples in one call and cleans them with
    rules. For expansion, only new triples between the given terms are kept.
    """

    # Predicates the model may use; the symmetric ones are mirrored in post-processing.
    PREDICATE_VOCAB = [
        "is-a", "instance-of", "is defined by", "equivalent class", "disjoint with",
        "type", "part_of", "has part", "exact match", "same as", "database_cross_reference",
        "overlaps", "located in", "term replaced by", "see also", "broader",
        "develops_from", "derives from", "regulates", "positively regulates",
        "is_conjugate_base_of", "is_conjugate_acid_of", "has role", "domain", "range", "tree view",
    ]
    SYMMETRIC_PREDICATES = [{"disjoint with", "equivalent class"}]

    # Dense retrieval encoder and model call settings.
    DENSE_MODEL_ID = "all-MiniLM-L6-v2"
    TEMPERATURE = 0.0
    MAX_COMPLETION_TOKENS = 2048
    GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

    CONSTRUCTION_TARGET = "primitive-ontology-triples"
    EXPANSION_TARGET = "extended-primitive-ontology-triples"
    INITIAL_KEY = "initial-primitive-ontology-triples"

    _TRIPLE_LINE = re.compile(r"^\s*(?:[-*]\s*|\d+[.)]\s*)?(.+?)\t(.+?)\t(.+?)\s*$")

    def __init__(self, model_id: str = "gpt-5.4", k: int = 6, use_dense: bool = True) -> None:
        """
        Initialize the learner.

        Args:
            model_id: Model used when ``load`` gets none (``gpt-5.4`` in the submission).
            k: Number of retrieved examples per document.
            use_dense: Combine BM25 with dense retrieval.
        """
        super().__init__()
        if k < 1:
            raise ValueError("k must be at least 1.")
        self.model_id = model_id
        self.k = k
        self.use_dense = use_dense
        self.client = None  # OpenAI SDK client (OpenAI or Gemini endpoint)
        # Retrieval index and gazetteer built by fit().
        self.pool: List[Dict[str, Any]] = []
        self.bm25 = None
        self.dense_model = None
        self.dense_active = False
        self.pool_embeddings = None
        self.gazetteer: Dict[str, str] = {}

    def _is_gemini(self, model: str) -> bool:
        """Whether the model is called through Gemini's OpenAI-compatible endpoint."""
        return model.startswith("gemini")

    def load(self, model_id: Optional[str] = None, **kwargs: Any) -> None:
        """
        Create the API client: Gemini for ``gemini*`` models, otherwise OpenAI.

        Args:
            model_id: Optional model name; defaults to the constructor's ``model_id``.
        """
        if model_id is not None:
            self.model_id = model_id
        from openai import OpenAI

        if self._is_gemini(self.model_id):
            self.client = OpenAI(api_key=os.environ["GEMINI_API_KEY"], base_url=self.GEMINI_BASE_URL)
        else:
            self.client = OpenAI()  # reads OPENAI_API_KEY from the environment

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
        """Turn a training record into an example: its context and all its triples."""
        if task == "ontology_construction":
            if self.CONSTRUCTION_TARGET not in sample:
                raise ValueError(f"Construction training records need '{self.CONSTRUCTION_TARGET}'.")
            triples = sample[self.CONSTRUCTION_TARGET]
        else:
            if self.EXPANSION_TARGET not in sample:
                raise ValueError(f"Expansion training records need '{self.EXPANSION_TARGET}'.")
            triples = list(sample.get(self.INITIAL_KEY) or []) + list(sample[self.EXPANSION_TARGET])
        return {"context": sample["context"], self.CONSTRUCTION_TARGET: self._dedupe([list(t) for t in triples])}

    def _fit(self, data: List[Dict[str, Any]], task: str) -> None:
        """Build the example pool, the retrieval index and the gazetteer."""
        pool = [self._pool_entry(sample, task) for sample in data]
        if not pool:
            raise ValueError("LaboroAILearner needs at least one labeled training record for its exemplar pool.")
        self._index_pool(pool)
        self.gazetteer = self._build_gazetteer(pool)

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
                    self.dense_model = SentenceTransformer(self.DENSE_MODEL_ID)
                self.pool_embeddings = self.dense_model.encode(
                    [s["context"] for s in pool], normalize_embeddings=True
                )
            except Exception as exc:
                self.dense_active = False

    def _retrieve(self, query_context: str) -> List[int]:
        """Return the indices of the ``k`` examples most similar to a context."""
        bm25_scores = np.array(self.bm25.get_scores(self._tokenize(query_context)))
        combined = self._rank_norm(bm25_scores)
        if self.dense_active and len(self.pool) > 0:
            q_emb = self.dense_model.encode([query_context], normalize_embeddings=True)[0]
            dense_scores = self.pool_embeddings @ q_emb
            combined = 0.5 * combined + 0.5 * self._rank_norm(dense_scores)
        top_idx = np.argsort(-combined)[: self.k]
        return top_idx.tolist()

    def _get_few_shot_text(self, query_context: str) -> str:
        """Format the retrieved examples for the prompt."""
        if not self.pool:
            return ""
        blocks = []
        for i in self._retrieve(query_context):
            sample = self.pool[i]
            triple_lines = "\n".join(f"{s}\t{p}\t{o}" for s, p, o in sample["primitive-ontology-triples"])
            blocks.append(f"Context: {sample['context']}\nTriples:\n{triple_lines}")
        return "\n\n".join(blocks)

    def _build_prompt(self, context: str, few_shot_text: str = "",
                      candidate_terms: Optional[List[str]] = None) -> str:
        """Build the extraction prompt: allowed predicates, rules, examples and the text."""
        vocab_lines = "\n".join(f"  {p}" for p in self.PREDICATE_VOCAB)
        terms_block = ""
        if candidate_terms:
            terms_block = ("\nCandidate terms (from the seed ontology, use if relevant): "
                           + ", ".join(candidate_terms) + "\n")
        exemplar_block = f"\nExamples:\n{few_shot_text}\n" if few_shot_text else ""
        return f"""You extract ontology triples from scientific text.
Output ONLY triples, one per line, tab-separated: subject<TAB>predicate<TAB>object

PREDICATE VOCABULARY, use ONLY these, with exact spelling:
{vocab_lines}
{terms_block}
RULES:
1. Lowercase only for all subjects and objects.
2. Only emit triples DIRECTLY supported by the text, missing a triple is far less harmful than emitting a wrong one.
3. is-a vs instance-of: if there can be multiple things of this kind, use is-a; if it names a unique individual, use instance-of.
4. Never emit cycles (A is-a B and B is-a A simultaneously).
{exemplar_block}
Text: {context}
Triples:"""

    def _call_llm(self, prompt: str) -> str:
        """Send one prompt to the model and return its answer."""
        response = self.client.chat.completions.create(
            model=self.model_id,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.TEMPERATURE,
            max_completion_tokens=self.MAX_COMPLETION_TOKENS,
        )
        return response.choices[0].message.content or ""

    def _parse_triples(self, raw_text: str) -> List[List[str]]:
        """Read tab-separated triples from the answer, keeping allowed predicates only."""
        triples = []
        for line in raw_text.splitlines():
            m = self._TRIPLE_LINE.match(line)
            if not m:
                continue
            s, p, o = (x.strip().lower() for x in m.groups())
            if p not in self.PREDICATE_VOCAB:
                continue
            triples.append([s, p, o])
        return triples

    def _norm_span(self, s: str) -> str:
        """Normalize an entity: lowercase, underscores to spaces, no trailing punctuation."""
        s = s.strip().lower().replace("_", " ")
        s = re.sub(r"\s+", " ", s)
        return s.rstrip(".,;:").strip()

    def _normalize(self, triples: List[List[str]]) -> List[List[str]]:
        """Normalize the entities of the triples and drop incomplete triples."""
        out = []
        for s, p, o in triples:
            s2, o2 = self._norm_span(s), self._norm_span(o)
            if p in self.PREDICATE_VOCAB and s2 and o2:
                out.append([s2, p, o2])
        return out

    def _build_gazetteer(self, pool: List[dict]) -> Dict[str, str]:
        """Map each entity, written without spaces, to its best spelling in the examples."""
        variants: Dict[str, Counter] = {}
        for sample in pool:
            for s, p, o in sample.get("primitive-ontology-triples", []):
                for span in (s, o):
                    span_n = self._norm_span(span)
                    key = span_n.replace(" ", "")
                    variants.setdefault(key, Counter())[span_n] += 1
        gazetteer = {}
        for key, counter in variants.items():
            canonical = sorted(counter.items(), key=lambda kv: (-kv[0].count(" "), -kv[1], kv[0]))[0][0]
            gazetteer[key] = canonical
        return gazetteer

    def _gazetteer_snap(self, triples: List[List[str]], gazetteer: Dict[str, str]) -> List[List[str]]:
        """Respell entities with the gazetteer (``lengthunit`` -> ``length unit``)."""
        out = []
        for s, p, o in triples:
            out.append([gazetteer.get(s.replace(" ", ""), s), p, gazetteer.get(o.replace(" ", ""), o)])
        return out

    def _dedupe(self, triples: List[List[str]]) -> List[List[str]]:
        """Remove duplicate triples, keeping the order."""
        seen = set()
        out = []
        for t in triples:
            key = tuple(t)
            if key not in seen:
                seen.add(key)
                out.append(t)
        return out

    def _drop_self_isa(self, triples: List[List[str]]) -> List[List[str]]:
        """Drop ``is-a`` triples whose subject and object are the same."""
        return [[s, p, o] for s, p, o in triples if not (p == "is-a" and s == o)]

    def _break_cycles(self, triples: List[List[str]]) -> List[List[str]]:
        """Remove ``is-a`` edges until the ``is-a`` graph has no cycles."""
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

    def _mirror_symmetric(self, triples: List[List[str]]) -> List[List[str]]:
        """Add the reverse of symmetric triples (``disjoint with``, ``equivalent class``)."""
        flat = set().union(*self.SYMMETRIC_PREDICATES)
        existing = set(map(tuple, triples))
        mirrored = list(triples)
        for s, p, o in triples:
            if p in flat and (o, p, s) not in existing:
                mirrored.append([o, p, s])
                existing.add((o, p, s))
        return mirrored

    def _postprocess(self, triples: List[List[str]], gazetteer: Optional[Dict[str, str]] = None) -> List[List[str]]:
        """Clean the extracted triples with the rules, in the submission's order."""
        triples = self._normalize(triples)
        if gazetteer:
            triples = self._gazetteer_snap(triples, gazetteer)
        triples = self._dedupe(triples)
        triples = self._drop_self_isa(triples)
        triples = self._break_cycles(triples)
        triples = self._mirror_symmetric(triples)
        triples = self._dedupe(triples)
        return triples

    def _triple_entities(self, triples: List[List[str]]):
        """Return the subjects and objects of the triples."""
        ents = set()
        for s, p, o in triples:
            ents.add(s)
            ents.add(o)
        return ents

    def _seed_terms(self, sample: dict) -> List[str]:
        """Return the terms, types and initial-ontology entities of an expansion record."""
        terms = set(sample.get("terms", [])) | set(sample.get("types", []))
        terms |= self._triple_entities(sample.get("initial-primitive-ontology-triples", []))
        return sorted({self._norm_span(t) for t in terms if t})

    def _subtract_seed_triples(self, triples: List[List[str]], initial_triples: List[List[str]]) -> List[List[str]]:
        """Drop triples that are already in the initial ontology."""
        seed_set = {tuple(self._norm_span(x) for x in t) for t in initial_triples}
        return [t for t in triples if tuple(self._norm_span(x) for x in t) not in seed_set]

    def _filter_to_allowed_terms(self, triples: List[List[str]], allowed_terms: List[str]) -> List[List[str]]:
        """Keep the triples whose subject and object are both seed terms."""
        allowed = set(allowed_terms)
        return [[s, p, o] for s, p, o in triples if self._norm_span(s) in allowed and self._norm_span(o) in allowed]

    def _build_task_prompt(self, sample: Dict[str, Any], task: str) -> str:
        """Build a record's prompt; for expansion it also lists the seed terms."""
        context = sample["context"]
        few_shot_text = self._get_few_shot_text(context)
        candidate_terms = self._seed_terms(sample) if task == "ontology_expansion" else None
        return self._build_prompt(context, few_shot_text=few_shot_text, candidate_terms=candidate_terms)

    def _finalise(self, sample: Dict[str, Any], raw: str, task: str) -> List[List[str]]:
        """Parse an answer and post-process its triples for the task."""
        triples = self._parse_triples(raw)
        if task == "ontology_construction":
            return self._postprocess(triples, gazetteer=self.gazetteer)
        triples = self._postprocess(triples)
        triples = self._subtract_seed_triples(triples, sample.get(self.INITIAL_KEY, []))
        return self._filter_to_allowed_terms(triples, self._seed_terms(sample))

    def _predict(self, data: List[Dict[str, Any]], task: str) -> List[Dict[str, Any]]:
        """Predict the triples of every record, with one model call each."""
        if self.bm25 is None:
            raise RuntimeError("Call fit() with labeled training records before predict().")
        if self.client is None:
            raise RuntimeError("Call load() before predict().")
        target = self.CONSTRUCTION_TARGET if task == "ontology_construction" else self.EXPANSION_TARGET
        predictions = []
        for sample in data:
            raw = self._call_llm(self._build_task_prompt(sample, task))
            predictions.append({"id": sample["id"], target: self._finalise(sample, raw, task)})
        return predictions
