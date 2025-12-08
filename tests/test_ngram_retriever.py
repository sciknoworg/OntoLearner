import pytest
from ontolearner.learner.retriever.ngram import NgramRetriever

def test_ngram_retriever_tfidf():
    # Initialize retriever
    retriever = NgramRetriever(ngram_range=(1, 2))
    retriever.load("tfidf")

    # Index some documents
    docs = ["The quick brown fox", "jumps over the lazy dog", "hello world"]
    retriever.index(docs)

    # Check embeddings shape
    assert retriever.embeddings.shape[0] == len(docs)

    # Retrieve top 2 documents
    results = retriever.retrieve(["quick fox", "hello"], top_k=2)
    assert len(results) == 2
    assert all(len(r) <= 2 for r in results)
    # Ensure retrieved documents are from original set
    for r in results:
        for doc in r:
            assert doc in docs

def test_ngram_retriever_count():
    retriever = NgramRetriever(ngram_range=(1, 1))
    retriever.load("count")

    docs = ["apple orange banana", "banana fruit salad", "fruit apple pie"]
    retriever.index(docs)

    results = retriever.retrieve(["apple banana"], top_k=2)
    assert len(results) == 1
    assert all(doc in docs for doc in results[0])

def test_retrieve_without_indexing_raises():
    retriever = NgramRetriever()
    retriever.load("tfidf")
    with pytest.raises(RuntimeError):
        retriever.retrieve(["test query"])
