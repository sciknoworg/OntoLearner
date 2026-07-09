from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest

from ontolearner.learner.text2onto.semanticswingers import (
    SemanticSwingersText2OntoLearner,
    _parse_triples_json,
    _require_qwen35_transformers,
    _to_triples,
    _VERIFIED_TRANSFORMERS_COMMIT,
)

MODULE = "ontolearner.learner.text2onto.semanticswingers"


# -- lazy import guard -----------------------------------------------------------------------


def test_lazy_import_guard_raises_actionable_error_without_qwen35():
    """The project's pinned transformers (4.57.6, no git-source install) lacks qwen3_5 — this
    exercises the real guard against the real installed library, no mocking needed."""
    with pytest.raises(ImportError) as exc_info:
        _require_qwen35_transformers()

    message = str(exc_info.value)
    assert "qwen3_5" in message
    assert _VERIFIED_TRANSFORMERS_COMMIT in message
    assert "pip install" in message


def test_load_raises_before_touching_the_network(monkeypatch):
    """load() must fail fast on the lazy-import guard, never reaching AutoModelForCausalLM."""
    learner = SemanticSwingersText2OntoLearner()
    with patch(f"{MODULE}.AutoRetriever"):
        with pytest.raises(ImportError):
            learner.load()


# -- adapter name resolution -------------------------------------------------------------------


def test_known_adapter_alias_resolves_to_hf_repo():
    learner = SemanticSwingersText2OntoLearner(adapter="raft")
    assert learner.adapter == "datagero/qwen3.5-9b-raft-taska"


def test_unknown_adapter_value_passed_through_unchanged():
    learner = SemanticSwingersText2OntoLearner(adapter="/local/path/to/adapter")
    assert learner.adapter == "/local/path/to/adapter"


# -- load() with the guard mocked out ------------------------------------------------------


@pytest.fixture
def mock_model_stack():
    """Mock transformers/peft so load() never touches the network or a real model."""
    with patch(f"{MODULE}._require_qwen35_transformers"), \
         patch("transformers.AutoTokenizer") as MockTok, \
         patch("transformers.AutoModelForCausalLM") as MockModel, \
         patch("peft.PeftModel") as MockPeft:
        MockTok.from_pretrained.return_value = MagicMock()
        MockModel.from_pretrained.return_value = MagicMock()
        MockPeft.from_pretrained.return_value = MagicMock()
        yield SimpleNamespace(tokenizer=MockTok, model=MockModel, peft=MockPeft)


def test_load_applies_peft_adapter_on_top_of_base(mock_model_stack):
    learner = SemanticSwingersText2OntoLearner(adapter="/some/adapter/dir", device="cpu")
    with patch(f"{MODULE}.SemanticSwingersTaxonomyLearner.load"):
        learner.load()

    mock_model_stack.model.from_pretrained.assert_called_once()
    assert mock_model_stack.model.from_pretrained.call_args[0][0] == "Qwen/Qwen3.5-9B"
    mock_model_stack.peft.from_pretrained.assert_called_once_with(
        mock_model_stack.model.from_pretrained.return_value, "/some/adapter/dir"
    )
    assert learner._model is not None


def test_load_is_idempotent(mock_model_stack):
    learner = SemanticSwingersText2OntoLearner()
    with patch(f"{MODULE}.SemanticSwingersTaxonomyLearner.load"):
        learner.load()
        learner.load()

    mock_model_stack.model.from_pretrained.assert_called_once()


# -- triple parsing helpers ------------------------------------------------------------------


def test_parse_triples_json_plain_array():
    text = '{"triples": [["poodle", "is-a", "dog"]]}'
    assert _parse_triples_json(text) == [["poodle", "is-a", "dog"]]


def test_parse_triples_json_markdown_fence():
    text = '```json\n{"triples": [["cat", "is-a", "mammal"]]}\n```'
    assert _parse_triples_json(text) == [["cat", "is-a", "mammal"]]


def test_parse_triples_json_garbage_returns_empty():
    assert _parse_triples_json("not json at all") == []


def test_to_triples_normalizes_relation_case_and_strips():
    raw = [[" Dog ", " IS-A ", " Animal "], {"subject": "Cat", "relation": "type", "object": "Mammal"}]
    triples = _to_triples(raw)
    assert triples == [("Dog", "is-a", "Animal"), ("Cat", "type", "Mammal")]


def test_to_triples_drops_incomplete_entries():
    raw = [["only", "two"], ["", "is-a", "animal"], ["dog", "is-a", "animal"]]
    assert _to_triples(raw) == [("dog", "is-a", "animal")]


# -- _text2onto: fit indexes exemplars, predict projects triples -------------------------------


def test_tasks_data_former_passes_data_through_unchanged():
    learner = SemanticSwingersText2OntoLearner()
    data = {"documents": []}
    assert learner.tasks_data_former(data, task="text2onto", test=True) is data
    assert learner.tasks_data_former(data, task="taxonomy-discovery", test=False) is data


def test_text2onto_fit_indexes_train_docs_and_returns_none():
    learner = SemanticSwingersText2OntoLearner()
    with patch.object(learner._retriever, "load"), patch.object(learner._retriever, "index") as mock_index:
        data = {
            "documents": [{"doc_id": "d1", "text": "A dog is a mammal."}],
            "triples": {"d1": [["dog", "is-a", "mammal"]]},
        }
        result = learner._text2onto(data, test=False)

    assert result is None
    assert learner._train_docs == [
        {"doc_id": "d1", "text": "A dog is a mammal.", "triples": [["dog", "is-a", "mammal"]]}
    ]
    mock_index.assert_called_once_with(["A dog is a mammal."])


def test_text2onto_fit_with_no_documents_skips_indexing():
    learner = SemanticSwingersText2OntoLearner()
    with patch.object(learner._retriever, "load") as mock_load:
        result = learner._text2onto({"documents": []}, test=False)

    assert result is None
    assert learner._train_docs == []
    mock_load.assert_not_called()


def test_text2onto_rejects_non_dict_input():
    learner = SemanticSwingersText2OntoLearner()
    with pytest.raises(ValueError):
        learner._text2onto(["not", "a", "dict"], test=True)


def test_text2onto_predict_projects_triples_to_terms_and_types():
    learner = SemanticSwingersText2OntoLearner()
    learner._model = MagicMock()  # short-circuits load()

    canned_triples = [
        ("poodle", "is-a", "dog"),
        ("dog", "is-a", "mammal"),
        ("mammal", "instance-of", "animal-class"),
    ]
    with patch.object(learner, "_retrieve_exemplars", return_value=[]), \
         patch.object(learner, "_generate_triples", return_value=canned_triples):
        result = learner._text2onto({"documents": [{"doc_id": "d2", "text": "..."}]}, test=True)

    assert result["terms"] == [
        {"doc_id": "d2", "term": "poodle"},
        {"doc_id": "d2", "term": "dog"},
        {"doc_id": "d2", "term": "mammal"},
    ]
    assert result["types"] == [
        {"doc_id": "d2", "type": "dog"},
        {"doc_id": "d2", "type": "mammal"},
        {"doc_id": "d2", "type": "animal-class"},
    ]


def test_text2onto_predict_dedupes_repeated_terms_and_types():
    learner = SemanticSwingersText2OntoLearner()
    learner._model = MagicMock()

    canned_triples = [("dog", "is-a", "mammal"), ("dog", "is-a", "mammal")]
    with patch.object(learner, "_retrieve_exemplars", return_value=[]), \
         patch.object(learner, "_generate_triples", return_value=canned_triples):
        result = learner._text2onto({"documents": [{"doc_id": "d3", "text": "..."}]}, test=True)

    assert result["terms"] == [{"doc_id": "d3", "term": "dog"}]
    assert result["types"] == [{"doc_id": "d3", "type": "mammal"}]


# -- _text2onto: raw triples pass through under an extra key (harness-ignored) -----------------


def test_text2onto_predict_includes_raw_triples_alongside_terms_and_types():
    """The 'triples' key is additive: terms/types shape is unchanged, and the raw (unprojected)
    triples — including non-typing relations text2onto_metrics never sees — survive alongside."""
    learner = SemanticSwingersText2OntoLearner()
    learner._model = MagicMock()

    canned_triples = [
        ("poodle", "is-a", "dog"),
        ("dog", "part_of", "canine-family"),  # non-typing relation: absent from terms/types logic
    ]
    with patch.object(learner, "_retrieve_exemplars", return_value=[]), \
         patch.object(learner, "_generate_triples", return_value=canned_triples):
        result = learner._text2onto({"documents": [{"doc_id": "d4", "text": "..."}]}, test=True)

    assert set(result.keys()) == {"terms", "types", "triples"}
    assert result["triples"] == [
        ["d4", "poodle", "is-a", "dog"],
        ["d4", "dog", "part_of", "canine-family"],
    ]
    # terms/types content is unaffected by the extra key: still exactly what the projection produces
    assert result["terms"] == [
        {"doc_id": "d4", "term": "poodle"},
        {"doc_id": "d4", "term": "dog"},
    ]
    assert result["types"] == [{"doc_id": "d4", "type": "dog"}]


def test_text2onto_predict_triples_empty_list_when_no_triples_generated():
    learner = SemanticSwingersText2OntoLearner()
    learner._model = MagicMock()

    with patch.object(learner, "_retrieve_exemplars", return_value=[]), \
         patch.object(learner, "_generate_triples", return_value=[]):
        result = learner._text2onto({"documents": [{"doc_id": "d5", "text": "..."}]}, test=True)

    assert result == {"terms": [], "types": [], "triples": []}


# -- _taxonomy_discovery: composed delegation, not a rewrite -----------------------------------


def test_taxonomy_discovery_delegates_to_composed_taxonomy_learner():
    learner = SemanticSwingersText2OntoLearner()
    sentinel_data = SimpleNamespace(type_taxonomies=SimpleNamespace(types=[], taxonomies=[]))

    with patch.object(
        learner._taxonomy_learner, "_taxonomy_discovery", return_value=[{"parent": "a", "child": "b"}]
    ) as mock_delegate:
        result = learner._taxonomy_discovery(sentinel_data, test=True)

    mock_delegate.assert_called_once_with(sentinel_data, test=True)
    assert result == [{"parent": "a", "child": "b"}]


def test_taxonomy_discovery_fit_is_a_noop_via_delegation():
    learner = SemanticSwingersText2OntoLearner()
    sentinel_data = SimpleNamespace(type_taxonomies=SimpleNamespace(types=[], taxonomies=[]))

    assert learner._taxonomy_discovery(sentinel_data, test=False) is None
