import pytest
from unittest.mock import MagicMock, patch
from ontolearner.learner.retriever.augmented_retriever import (
    LLMAugmenterGenerator,
    LLMAugmenter,
    LLMAugmentedRetriever,
)
from ontolearner.base import AutoRetriever


class DummyData:
    """Dummy ontology-like object for testing data formatting."""

    class TermTyping:
        def __init__(self, term):
            self.term = term

    class TypingContainer:
        def __init__(self, typings):
            self.term_typings = typings

    class TaxPair:
        def __init__(self, parent, child):
            self.parent = parent
            self.child = child

    class TaxonomyContainer:
        def __init__(self, pairs):
            self.taxonomies = pairs

    class NonTax:
        def __init__(self, head, tail, relation):
            self.head = head
            self.tail = tail
            self.relation = relation

    class NonTaxContainer:
        def __init__(self, triples):
            self.non_taxonomies = triples


@pytest.fixture
def mock_openai():
    """Patch OpenAI client and return a controlled response for function calling."""
    with patch("ontolearner.learner.retriever.llm_retriever.OpenAI") as mock_client:
        instance = mock_client.return_value

        fake_response = MagicMock()
        fake_response.choices = [
            MagicMock(
                message=MagicMock(
                    function_call=MagicMock(
                        arguments="{'candidate_parents': ['A', 'B', 'C', 'D', 'E']}"
                    )
                )
            )
        ]

        instance.chat.completions.create.return_value = fake_response
        yield mock_client


def test_tasks_data_former_taxonomy():
    """Test taxonomy data formatting logic."""
    generator = LLMAugmenterGenerator(token="fake")

    data = DummyData()
    data.type_taxonomies = DummyData.TaxonomyContainer(
        [
            DummyData.TaxPair("Animal", "Dog"),
            DummyData.TaxPair("Vehicle", "Car"),
        ]
    )

    result = generator.tasks_data_former(data, "taxonomy-discovery")
    assert set(result) == {"Animal", "Dog", "Vehicle", "Car"}


def test_augment_taxonomy_discovery(mock_openai):
    """Ensure LLM function-calling generation works and returns fixed parents."""
    generator = LLMAugmenterGenerator(token="fake", top_n_candidate=5)

    output = generator.augment_taxonomy_discovery(["Dog"])
    assert "Dog" in output
    assert output["Dog"] == ["A", "B", "C", "D", "E"]


def test_llm_augmenter_transform():
    """Test augmentation lookup behavior."""
    fake_json = {
        "config": {"top_n_candidate": 3},
        "taxonomy-discovery": {"Dog": ["Animal", "Mammal", "Pet"]},
    }

    with patch("ontolearner.learner.retriever.llm_retriever.load_json", return_value=fake_json):
        augmenter = LLMAugmenter("dummy/path.json")

    assert augmenter.transform("Dog", "taxonomy-discovery") == ["Animal", "Mammal", "Pet"]
    assert augmenter.transform("X", "taxonomy-discovery") == ["X"]


def test_llm_augmented_retriever_taxonomy(monkeypatch):
    retriever = LLMAugmentedRetriever()

    def fake_retrieve(self, query, top_k=5, batch_size=32):
        return [[f"doc_{q}_{i}" for i in range(top_k)] for q in query]

    monkeypatch.setattr(
        AutoRetriever,
        "retrieve",
        fake_retrieve
    )

    class FakeAug:
        top_n_candidate = 2
        def transform(self, q, task):
            return [f"{q}_A", f"{q}_B"]

    retriever.set_augmenter(FakeAug())

    results = retriever.retrieve(["Dog"], top_k=2, task="taxonomy-discovery")
    assert len(results) == 1
    assert len(results[0]) == 4



def test_llm_augmented_retriever_normal(monkeypatch):
    """Test normal retrieval path (no taxonomy discovery)."""
    retriever = LLMAugmentedRetriever()

    def fake_retrieve(self, query, top_k=5, batch_size=32):
        return [[f"doc_{query[0]}_{i}" for i in range(top_k)]]

    monkeypatch.setattr(AutoRetriever, "retrieve", fake_retrieve)

    results = retriever.retrieve(["Cat"], top_k=3)
    assert results == [["doc_Cat_0", "doc_Cat_1", "doc_Cat_2"]]
