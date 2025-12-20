import pytest
import numpy as np
from unittest.mock import MagicMock, patch

from ontolearner.learner.retriever.crossencoder import CrossEncoderRetriever


@pytest.fixture
def mock_models():
    """
    Mock SentenceTransformer, CrossEncoder, and util.semantic_search inside the
    ontolearner.learner.retriever.crossencoder module so the retriever can be
    tested without loading real models.
    """
    module_path = "ontolearner.learner.retriever.crossencoder"

    with patch(f"{module_path}.SentenceTransformer") as MockST, \
         patch(f"{module_path}.CrossEncoder") as MockCE, \
         patch(f"{module_path}.util.semantic_search") as mock_search:

        # Mocked BiEncoder — returns fixed embeddings
        mock_bi = MagicMock()
        mock_bi.encode.return_value = np.array([[1.0, 0.0], [0.0, 1.0]])
        MockST.return_value = mock_bi

        # Mocked CrossEncoder — deterministic scoring
        mock_cross = MagicMock()
        mock_cross.predict.return_value = np.array([0.9, 0.1])  # doc1 > doc2
        MockCE.return_value = mock_cross

        # Mocked semantic search — two candidate docs
        mock_search.return_value = [
            [{"corpus_id": 0}, {"corpus_id": 1}]
        ]

        yield MockST, MockCE, mock_search


def test_load(mock_models):
    retriever = CrossEncoderRetriever()
    retriever.load("test-model")

    assert retriever.bi_encoder is not None
    assert retriever.cross_encoder is not None


def test_index(mock_models):
    retriever = CrossEncoderRetriever()
    retriever.load("test-model")

    docs = ["doc1", "doc2"]
    retriever.index(docs)

    assert retriever.documents == docs
    assert isinstance(retriever.document_embeddings, np.ndarray)
    assert retriever.document_embeddings.shape == (2, 2)


def test_retrieve(mock_models):
    retriever = CrossEncoderRetriever()
    retriever.load("test-model")
    retriever.index(["doc1", "doc2"])

    result = retriever.retrieve(["query"], top_k=1)

    # Should return top 1 reranked doc → "doc1"
    assert len(result) == 1
    assert result[0] == ["doc1"]
