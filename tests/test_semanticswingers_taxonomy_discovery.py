from types import SimpleNamespace

import numpy as np
import pytest
from unittest.mock import MagicMock, patch

from ontolearner.learner.taxonomy_discovery.semanticswingers import (
    SemanticSwingersTaxonomyLearner,
)

MODULE = "ontolearner.learner.taxonomy_discovery.semanticswingers"


def _relation(parent, child):
    return SimpleNamespace(parent=parent, child=child)


def _ontology_data(types, taxonomies):
    return SimpleNamespace(
        type_taxonomies=SimpleNamespace(
            types=types,
            taxonomies=[_relation(p, c) for p, c in taxonomies],
        )
    )


def _make_encoder(vectors):
    """A fake SentenceTransformer whose ``encode`` looks vectors up by text."""
    def encode(texts, normalize_embeddings=True, show_progress_bar=False):
        return np.array([vectors[t] for t in texts])

    encoder = MagicMock()
    encoder.encode.side_effect = encode
    return encoder


# Unit vectors (the real encoder is called with normalize_embeddings=True).
# "Animal" sits at 45 degrees, equidistant from "Dog" (10 degrees) and "Cat"
# (80 degrees), so it has the highest mean similarity to the vocabulary and
# wins the generality tie-break; "Dog" and "Cat" are far apart from each other.
VECTORS = {
    "Animal": [0.70711, 0.70711],
    "Dog": [0.98481, 0.17365],
    "Cat": [0.17365, 0.98481],
}


@pytest.fixture
def mock_encoder():
    with patch(f"{MODULE}.SentenceTransformer") as MockST:
        MockST.return_value = _make_encoder(VECTORS)
        yield MockST


@pytest.fixture(autouse=True)
def no_openai_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)


def test_nodes_dedups_declared_types_and_edge_endpoints():
    data = _ontology_data(
        types=["Animal", "Dog"],
        taxonomies=[("Animal", "Dog"), ("Animal", "Cat")],
    )
    nodes = SemanticSwingersTaxonomyLearner._nodes(data)

    assert nodes == ["Animal", "Dog", "Cat"]


def test_tasks_data_former_passes_data_through_unchanged():
    data = _ontology_data(types=["Animal"], taxonomies=[])
    learner = SemanticSwingersTaxonomyLearner()

    assert learner.tasks_data_former(data, task="taxonomy-discovery", test=True) is data


def test_fit_is_a_noop():
    learner = SemanticSwingersTaxonomyLearner()
    data = _ontology_data(types=["Animal"], taxonomies=[])

    assert learner._taxonomy_discovery(data, test=False) is None


def test_predict_returns_parent_child_dicts(mock_encoder):
    learner = SemanticSwingersTaxonomyLearner(device="cpu")
    data = _ontology_data(
        types=["Animal", "Dog", "Cat"],
        taxonomies=[("Animal", "Dog"), ("Animal", "Cat")],
    )

    preds = learner._taxonomy_discovery(data, test=True)

    assert len(preds) > 0
    assert all(set(p.keys()) == {"parent", "child"} for p in preds)


def test_embedding_selector_picks_most_general_candidate(mock_encoder):
    learner = SemanticSwingersTaxonomyLearner(device="cpu", top_k=10)
    data = _ontology_data(
        types=["Animal", "Dog", "Cat"],
        taxonomies=[("Animal", "Dog"), ("Animal", "Cat")],
    )

    preds = learner._taxonomy_discovery(data, test=True)
    by_child = {p["child"]: p["parent"] for p in preds}

    assert by_child["Dog"] == "Animal"
    assert by_child["Cat"] == "Animal"
    # "Animal" is the most general node overall, so it never gets a parent.
    assert "Animal" not in by_child


def test_embedding_selector_is_deterministic(mock_encoder):
    learner = SemanticSwingersTaxonomyLearner(device="cpu")
    data = _ontology_data(
        types=["Animal", "Dog", "Cat"],
        taxonomies=[("Animal", "Dog"), ("Animal", "Cat")],
    )

    first = learner._taxonomy_discovery(data, test=True)
    second = learner._taxonomy_discovery(data, test=True)

    assert first == second


def test_openai_selector_without_api_key_falls_back_to_embedding(mock_encoder):
    with patch("openai.OpenAI") as MockOpenAI:
        learner = SemanticSwingersTaxonomyLearner(selector="openai", device="cpu")
        data = _ontology_data(
            types=["Animal", "Dog", "Cat"],
            taxonomies=[("Animal", "Dog"), ("Animal", "Cat")],
        )

        assert learner.api_key is None
        preds = learner._taxonomy_discovery(data, test=True)

        by_child = {p["child"]: p["parent"] for p in preds}
        assert by_child["Dog"] == "Animal"
        MockOpenAI.assert_not_called()


def test_ollama_selector_defaults():
    learner = SemanticSwingersTaxonomyLearner(selector="ollama")
    assert learner.llm_model == "llama3.1:8b"
    assert learner.base_url == "http://localhost:11434/v1"


def test_openai_selector_defaults():
    learner = SemanticSwingersTaxonomyLearner(selector="openai")
    assert learner.llm_model == "gpt-4.1-mini"
    assert learner.base_url is None


def test_explicit_llm_model_overrides_default():
    learner = SemanticSwingersTaxonomyLearner(selector="ollama", llm_model="qwen3.5")
    assert learner.llm_model == "qwen3.5"


def test_reasoning_off_only_for_qwen3():
    """qwen3.x is a thinking model: without this the selector gets empty output (F1=0)."""
    from ontolearner.learner.taxonomy_discovery.semanticswingers import _reasoning_off

    assert _reasoning_off("qwen3.5-nothink:9b") == {
        "extra_body": {"reasoning_effort": "none"}
    }
    assert _reasoning_off("qwen3.5:9b") == {"extra_body": {"reasoning_effort": "none"}}
    assert _reasoning_off("gpt-4.1-mini") == {}
    assert _reasoning_off("llama3.1:8b") == {}
    assert _reasoning_off(None) == {}


def test_selection_prompt_is_injectable_and_defaults():
    from ontolearner.learner.taxonomy_discovery.semanticswingers import (
        SemanticSwingersTaxonomyLearner, _SELECTION_PROMPT,
    )
    assert SemanticSwingersTaxonomyLearner().selection_prompt == _SELECTION_PROMPT
    custom = SemanticSwingersTaxonomyLearner(selection_prompt="parent of {child}: {candidates}")
    out = custom.selection_prompt.format(child="Chianti", candidates="- Wine")
    assert out == "parent of Chianti: - Wine"


# --- Structural-matrix champion (SemanticSwingersMatrixTaxonomyLearner) --------

def test_bilinear_layer_scores_child_parent_pairs():
    import torch
    from ontolearner.learner.taxonomy_discovery.semanticswingers import (
        BilinearAdjacencyLayer,
    )

    layer = BilinearAdjacencyLayer(embedding_dim=4)
    child = torch.randn(3, 4)
    parent = torch.randn(3, 4)
    scores = layer(child, parent)

    # one score per (child, parent) row, and it equals <W.child, parent>
    assert scores.shape == (3,)
    expected = torch.sum(layer.W(child) * parent, dim=-1)
    assert torch.allclose(scores, expected)


def test_cleanup_graph_breaks_cycles_and_transitively_reduces():
    from ontolearner.learner.taxonomy_discovery.semanticswingers import (
        SemanticSwingersMatrixTaxonomyLearner,
    )

    learner = SemanticSwingersMatrixTaxonomyLearner()

    # A->B, B->C, A->C : the redundant A->C must be dropped by transitive reduction.
    reduced = learner._cleanup_graph([
        {"parent": "A", "child": "B"},
        {"parent": "B", "child": "C"},
        {"parent": "A", "child": "C"},
    ])
    edges = {(e["parent"], e["child"]) for e in reduced}
    assert ("A", "C") not in edges
    assert ("A", "B") in edges and ("B", "C") in edges

    # A->B, B->A : a cycle must be broken so the result is a DAG.
    import networkx as nx
    deacycled = learner._cleanup_graph([
        {"parent": "A", "child": "B"},
        {"parent": "B", "child": "A"},
    ])
    G = nx.DiGraph((e["parent"], e["child"]) for e in deacycled)
    assert nx.is_directed_acyclic_graph(G)

    assert learner._cleanup_graph([]) == []


def test_matrix_learner_defaults_to_public_hf_registry():
    from ontolearner.learner.taxonomy_discovery.semanticswingers import (
        SemanticSwingersMatrixTaxonomyLearner,
    )

    learner = SemanticSwingersMatrixTaxonomyLearner()
    assert learner.hf_repo_id == "datagero/taxonomy-structural-matrix-1024-mxbai"


def test_resolve_matrix_weights_prefers_local_then_falls_back_to_hf():
    from ontolearner.learner.taxonomy_discovery.semanticswingers import (
        SemanticSwingersMatrixTaxonomyLearner,
    )

    learner = SemanticSwingersMatrixTaxonomyLearner(
        matrix_weights_path="structural_matrix_w_1024_mxbai.pt",
    )

    # Local file present -> used as-is, no download.
    with patch(f"{MODULE}.os.path.exists", return_value=True):
        assert learner._resolve_matrix_weights() == "structural_matrix_w_1024_mxbai.pt"

    # Local file absent -> fetched from the HF registry by basename.
    with patch(f"{MODULE}.os.path.exists", return_value=False), \
            patch("huggingface_hub.hf_hub_download", return_value="/cache/x.pt") as dl:
        assert learner._resolve_matrix_weights() == "/cache/x.pt"
        dl.assert_called_once_with(
            repo_id="datagero/taxonomy-structural-matrix-1024-mxbai",
            filename="structural_matrix_w_1024_mxbai.pt",
        )
