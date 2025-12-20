import numpy as np
from unittest.mock import MagicMock
import pytest

from ontolearner.learner.retriever.embedding import (
    Word2VecRetriever,
    GloveRetriever,
)


# -------------------------
# Fixtures for mocks
# -------------------------

@pytest.fixture
def mock_w2v_model():
    """Mock gensim KeyedVectors for Word2VecRetriever."""
    mock = MagicMock()
    mock.vector_size = 3
    mock.__contains__.side_effect = lambda w: w in {"hello", "world"}
    mock.__getitem__.side_effect = lambda w: np.array(
        [1, 2, 3] if w == "hello" else [4, 5, 6]
    )
    return mock


@pytest.fixture
def mock_glove_model():
    """Mock GloVe embedding dict."""
    return {
        "hello": [1.0, 2.0, 3.0],
        "world": [4.0, 5.0, 6.0],
    }


# -------------------------
# Word2VecRetriever tests
# -------------------------

def test_w2v_index_and_retrieve(mock_w2v_model):
    r = Word2VecRetriever()
    r.embedding_model = mock_w2v_model  # Skip load()

    docs = ["hello world", "hello", "unknown text"]
    r.index(docs)

    assert r.embeddings.shape == (3, 3)

    results = r.retrieve(["hello"], top_k=2)
    assert len(results) == 1
    assert len(results[0]) == 2
    assert results[0][0] in docs


# -------------------------
# GloveRetriever tests
# -------------------------

def test_glove_index_and_retrieve(mock_glove_model):
    r = GloveRetriever()
    r.embedding_model = mock_glove_model  # Skip load()

    docs = ["hello world", "hello"]
    r.index(docs)

    assert r.embeddings.shape[0] == 2

    results = r.retrieve(["world"], top_k=1)
    assert len(results) == 1
    assert results[0][0] in docs


# -------------------------
# Encoding tests
# -------------------------

def test_w2v_encode_single(mock_w2v_model):
    r = Word2VecRetriever()
    r.embedding_model = mock_w2v_model

    vec = r._encode_text("hello")
    assert np.allclose(vec, np.array([1, 2, 3]))


def test_glove_encode_single(mock_glove_model):
    r = GloveRetriever()
    r.embedding_model = mock_glove_model

    vec = r._encode_text("world")
    assert np.allclose(vec, np.array([4, 5, 6]))
