from ..base import AutoRetriever
from typing import Any, List
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer


class BERTRetrieverLearner(AutoRetriever):
    def __init__(self):
        super().__init__()
        self.embedding_model = None
        self.documents = []
        self.embeddings = None

    def load(self, model_id: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.embedding_model = SentenceTransformer(model_id)

    def index(self, inputs: List[Any]):
        self.documents = inputs
        self.embeddings = self.embedding_model.encode(inputs, convert_to_tensor=True)

    def retrieve(self, query: str, top_k: int = 5) -> List[Any]:
        if self.embeddings is None:
            return []

        query_embedding = self.embedding_model.encode(query, convert_to_tensor=True)

        similarities = F.cosine_similarity(
            query_embedding.unsqueeze(0),
            self.embeddings
        )

        top_k = min(top_k, len(self.documents))

        indices = similarities.topk(top_k).indices.tolist()

        return [self.documents[i] for i in indices]


class NGramRetrieverLearner(AutoRetriever):
    def __init__(self):
        super().__init__()
        self.documents = []
        self.terms = []

    def load(self, model_id=None):
        # No model to load for NGrams
        pass

    def index(self, inputs):
        self.documents = inputs
        self.terms = [self._extract_terms(doc) for doc in inputs]

    def retrieve(self, query, top_k=5):
        query_ngrams = self._extract_terms(query)
        scores = []

        for idx, doc_ngrams in enumerate(self.terms):
            intersection = len(set(query_ngrams) & set(doc_ngrams))
            union = len(set(query_ngrams) | set(doc_ngrams))
            similarity = intersection / union if union > 0 else 0
            scores.append((idx, similarity))

        # Sort by similarity
        scores.sort(key=lambda x: x[1], reverse=True)
        top_indices = [idx for idx, _ in scores[:top_k]]

        return [self.documents[idx] for idx in top_indices]

    @staticmethod
    def _extract_terms(text, n=3):
        # Extract character-level n-grams
        return [text[i:i+n] for i in range(len(text)-n+1)]
