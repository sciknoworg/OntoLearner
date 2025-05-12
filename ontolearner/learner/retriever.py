from ..base import AutoLearnerRetriever
from typing import Any, List
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer


class AutoBERTRetriever(AutoLearnerRetriever):

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

    def retrieve(self, query: str, top_k: int = 5):
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
