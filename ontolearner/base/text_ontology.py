import json
from typing import List, Dict

from ontolearner.data_structure import TermTyping


class TextDataset:
    def get_llm_training_examples(self) -> List[Dict]:
        ...

    def get_ground_truth_concepts(self) -> List[TermTyping]:
        ...


class OLLMWikipedia(TextDataset):
    """
    OLLM Wikipedia Ontology is a synthetic ontology generated from Wikipedia articles.
    It is used to evaluate the performance of ontology learning algorithms.
    The ontology is generated from the Wikipedia dump and contains concepts and their relationships.

    This class processes OLLM Wikipedia Ontology using default behavior.
    """
    ontology_full_name: str = "OLLM Wikipedia Ontology"
    ontology_identifier: str = "ollm_wikipedia"

    def __init__(self, language: str = 'en', split: str = "train"):
        """Initialize the OLLMWikipedia class with the specified language and split."""
        super().__init__(language)
        self.documents = None  # Raw text for LLM input
        self.concept_list = None  # Concepts to predict, ground truth
        self.concept_to_doc_map = None  # For analysis
        self.split = split

    def load(self, path: str):
        """Load the ontology from a JSON files"""
        # Load documents
        with open(f"{path}/ollm_wikipedia_{self.split}_documents.jsonl", "r") as f:
            self.documents = [json.loads(line) for line in f]

        # Load concept lists
        with open(f"{path}/ollm_wikipedia_{self.split}_concept_list.json", "r") as f:
            self.concept_list = json.load(f)

        # Load concept-doc mapping
        with open(f"{path}/ollm_wikipedia_{self.split}_concept_to_doc_map.json", "r") as f:
            self.concept_to_doc_map = json.load(f)

    def get_llm_training_data(self) -> List[Dict]:
        """Format for LLM fine-tuning"""
        training_data = []
        for doc in self.documents:
            concepts = [
                c["concept"] for c in self.concept_list
                if any(m["doc_id"] == doc["id"] for m in self.concept_to_doc_map.get(c["concept"], []))
            ]
            training_data.append({
                "id": doc["id"],
                "text": doc["text"],
                "concepts": concepts
            })
        return training_data

    def get_llm_prompt_format(self):
        """Format for instruction tuning"""
        return [
            {"text": doc["text"], "target_concepts": [...]}
            for doc in self.documents
        ]

    def extract_term_typings(self) -> List[TermTyping]:
        """
        Provide ground truth for term typings
        """
        term_typings = []
        for concept_entry in self.concept_list:
            term = concept_entry["concept"]
            term_type = concept_entry["type"]
            term_typings.append(TermTyping(term=term, types=[term_type]))
        return term_typings

    def extract_type_taxonomies(self):
        raise NotImplementedError("Taxonomies not supported for text datasets")

    def extract_type_non_taxonomic_relations(self):
        raise NotImplementedError("Non-taxonomic relations not supported for text datasets")
