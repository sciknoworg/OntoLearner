import types

from ontolearner.data_structure import PseudoSentence
from ontolearner.text2onto.synthesizer import SyntheticGenerator


class DummyTermTyping:
    def __init__(self, term, types):
        self.ID = f"TT_{term}"
        self.term = term
        self.types = types


class DummyTaxonomy:
    def __init__(self, parent, child):
        self.ID = f"TR_{parent}_{child}"
        self.parent = parent
        self.child = child


class DummyNonTax:
    def __init__(self, head, tail, relation):
        self.ID = f"NR_{head}_{tail}_{relation}"
        self.head = head
        self.tail = tail
        self.relation = relation


class DummyOntologyData:
    def __init__(self):
        self.term_typings = [DummyTermTyping("Apple", ["Fruit"])]
        self.type_taxonomies = types.SimpleNamespace(taxonomies=[DummyTaxonomy("Food", "Fruit")])
        self.type_non_taxonomic_relations = types.SimpleNamespace(
            non_taxonomies=[DummyNonTax("Apple", "Tree", "growsOn")]
        )


class DummyGenerator(SyntheticGenerator):
    def load(self, model_id=None):
        self.model_id = model_id or self.model_id
        self.tokenizer = object()
        self.model = object()


def test_placeholder_detection_and_json_extraction():
    generator = SyntheticGenerator(load_model=False)

    assert generator._looks_like_placeholder("N12")
    assert generator._looks_like_placeholder("N_abc")
    assert not generator._looks_like_placeholder("Nutrition")

    payload = generator._extract_json('```json\n{"title": "T", "fluent_passage_text": "P"}\n```')
    assert payload == {"title": "T", "fluent_passage_text": "P"}


def test_generate_uses_transformers_style_backend(monkeypatch):
    generator = DummyGenerator(load_model=False)

    def fake_generate_pseudo_sentences(parent_to_child):
        assert "Fruit" in parent_to_child
        return [
            PseudoSentence(
                id="0",
                pseudo_sentences=["Apple is a Fruit"],
                terms=["Apple"],
                types=["Fruit"],
            )
        ]

    def fake_generate_texts(prompts):
        assert len(prompts) == 1
        assert "Apple is a Fruit" in prompts[0]
        assert "Ontology context" in prompts[0]
        return ['{"title": "Fruit overview", "fluent_passage_text": "Apple is a Fruit in the Food domain."}']

    monkeypatch.setattr(generator, "generate_pseudo_sentences", fake_generate_pseudo_sentences)
    monkeypatch.setattr(generator, "_generate_texts", fake_generate_texts)

    synthetic = generator.generate(DummyOntologyData(), topic="Agriculture")

    assert synthetic.child_to_parent == {"Apple": ["Fruit"], "Fruit": ["Food"]}
    assert len(synthetic.pseudo_sentences) == 1
    assert len(synthetic.generated_docs) == 1
    assert synthetic.generated_docs[0].title == "Fruit overview"
    assert "Apple" in synthetic.generated_docs[0].text
    assert "Fruit" in synthetic.generated_docs[0].text
