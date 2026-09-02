import numpy as np
import pytest
from unittest.mock import MagicMock, patch

from ontolearner.learner.term_typing.semanticswingers import (
    SemanticSwingersTermTypingLearner,
)

MODULE = "ontolearner.learner.term_typing.semanticswingers"


def _make_encoder(vectors):
    """A fake SentenceTransformer whose ``encode`` looks vectors up by text."""
    def encode(texts, normalize_embeddings=True, show_progress_bar=False):
        return np.array([vectors[t] for t in texts])

    encoder = MagicMock()
    encoder.encode.side_effect = encode
    return encoder


VECTORS = {
    "Animal": [1.0, 0.0],
    "Plant": [0.0, 1.0],
    "dog": [0.9, 0.1],
    "rose": [0.1, 0.9],
}


@pytest.fixture
def mock_encoder():
    with patch(f"{MODULE}.SentenceTransformer") as MockST:
        MockST.return_value = _make_encoder(VECTORS)
        yield MockST


@pytest.fixture(autouse=True)
def no_openai_key(monkeypatch):
    """Hermetic default: no OPENAI_API_KEY leaks in from the environment."""
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)


def test_fit_learns_type_inventory_from_list():
    learner = SemanticSwingersTermTypingLearner()
    learner._term_typing(["Animal", "Plant", "Animal"], test=False)

    assert learner._allowed_types == ["Animal", "Plant"]


def test_predict_returns_entry_per_term(mock_encoder):
    learner = SemanticSwingersTermTypingLearner(device="cpu")
    learner._allowed_types = ["Animal", "Plant"]

    preds = learner._term_typing(["dog", "rose"], test=True)

    assert len(preds) == 2
    assert {p["term"] for p in preds} == {"dog", "rose"}
    assert all(set(p.keys()) == {"term", "types"} for p in preds)


def test_embedding_selector_picks_nearest_type(mock_encoder):
    learner = SemanticSwingersTermTypingLearner(device="cpu")
    learner._allowed_types = ["Animal", "Plant"]

    preds = learner._term_typing(["dog", "rose"], test=True)
    by_term = {p["term"]: p["types"] for p in preds}

    assert by_term["dog"] == ["Animal"]
    assert by_term["rose"] == ["Plant"]


def test_predict_empty_terms_and_empty_vocab_short_circuit():
    learner = SemanticSwingersTermTypingLearner()
    learner._allowed_types = ["Animal"]
    assert learner._term_typing([], test=True) == []

    learner2 = SemanticSwingersTermTypingLearner()
    learner2._allowed_types = []
    assert learner2._term_typing(["dog"], test=True) == [{"term": "dog", "types": []}]


def test_embedding_selector_is_deterministic(mock_encoder):
    learner = SemanticSwingersTermTypingLearner(device="cpu")
    learner._allowed_types = ["Animal", "Plant"]

    first = learner._term_typing(["dog", "rose"], test=True)
    second = learner._term_typing(["dog", "rose"], test=True)

    assert first == second


class TestParseTypings:
    def setup_method(self):
        self.learner = SemanticSwingersTermTypingLearner()
        self.allowed = {"Animal", "Plant"}

    def test_parses_plain_json(self):
        content = '{"typings": [{"term": "dog", "types": ["Animal"]}]}'
        result = self.learner._parse_typings(content, self.allowed)
        assert result == {"dog": ["Animal"]}

    def test_drops_types_outside_closed_vocabulary(self):
        content = '{"typings": [{"term": "dog", "types": ["Animal", "Robot"]}]}'
        result = self.learner._parse_typings(content, self.allowed)
        assert result == {"dog": ["Animal"]}

    def test_malformed_json_returns_empty_dict(self):
        result = self.learner._parse_typings("not json at all", self.allowed)
        assert result == {}

    def test_recovers_fenced_json(self):
        content = (
            "Here is the answer:\n```json\n"
            '{"typings": [{"term": "rose", "types": ["Plant"]}]}\n```'
        )
        result = self.learner._parse_typings(content, self.allowed)
        assert result == {"rose": ["Plant"]}

    def test_top_level_list_payload(self):
        content = '[{"term": "dog", "types": ["Animal"]}]'
        result = self.learner._parse_typings(content, self.allowed)
        assert result == {"dog": ["Animal"]}


def test_openai_selector_without_api_key_falls_back_to_embedding(mock_encoder):
    with patch("openai.OpenAI") as MockOpenAI:
        learner = SemanticSwingersTermTypingLearner(selector="openai", device="cpu")
        learner._allowed_types = ["Animal", "Plant"]

        assert learner.api_key is None
        preds = learner._term_typing(["dog", "rose"], test=True)

        by_term = {p["term"]: p["types"] for p in preds}
        assert by_term["dog"] == ["Animal"]
        assert by_term["rose"] == ["Plant"]
        MockOpenAI.assert_not_called()


def test_ollama_selector_defaults():
    learner = SemanticSwingersTermTypingLearner(selector="ollama")
    assert learner.llm_model == "llama3.1:8b"
    assert learner.base_url == "http://localhost:11434/v1"


def test_openai_selector_defaults():
    learner = SemanticSwingersTermTypingLearner(selector="openai")
    assert learner.llm_model == "gpt-4.1-mini"
    assert learner.base_url is None


def test_explicit_llm_model_overrides_default():
    learner = SemanticSwingersTermTypingLearner(selector="ollama", llm_model="qwen3.5")
    assert learner.llm_model == "qwen3.5"


def test_reasoning_off_only_for_qwen3():
    """qwen3.x is a thinking model: without this the selector gets empty output (F1=0)."""
    from ontolearner.learner.term_typing.semanticswingers import _reasoning_off

    assert _reasoning_off("qwen3.5-nothink:9b") == {
        "extra_body": {"reasoning_effort": "none"}
    }
    assert _reasoning_off("qwen3.5:9b") == {"extra_body": {"reasoning_effort": "none"}}
    assert _reasoning_off("gpt-4.1-mini") == {}
    assert _reasoning_off("llama3.1:8b") == {}
    assert _reasoning_off(None) == {}


def test_system_prompt_is_injectable_and_defaults():
    from ontolearner.learner.term_typing.semanticswingers import (
        SemanticSwingersTermTypingLearner, _SYSTEM,
    )
    assert SemanticSwingersTermTypingLearner().system_prompt == _SYSTEM
    assert SemanticSwingersTermTypingLearner(system_prompt="CUSTOM").system_prompt == "CUSTOM"
