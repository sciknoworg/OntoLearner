

from transformers import AutoModelForCausalLM, AutoTokenizer
import numpy as np
import pandas as pd
from tqdm import tqdm

from ontolearner.metrics.ontology_analyzer import OntologyAnalyzer

model_name="meta-llama/Llama-3.1-8B-Instruct"
token = "huggingface_token"


class LLMIntegrationTester:
    def __init__(self, model_name):
        self.tokenizer     = AutoTokenizer.from_pretrained(model_name)
        self.model         = AutoModelForCausalLM.from_pretrained(model_name)
        self.onto_analyzer = OntologyAnalyzer("../../data/ontologies/CSO.3.4.owl")
        self.onto_analyzer.generate_report()


    def test_relationship_prediction(self, sample_size=1):
        """
        Test LLM's ability to predict relationships from CSO.
        """
        # Get all unique predicates (relationships)
        relationships = list(set(self.onto_analyzer.g.predicates()))

        print(f"Testing relationship prediction with {sample_size} samples.")

        print("Ontology Relationships:", [str(rel).split('#')[-1] for rel in relationships])

        correct_predictions = 0

        for _ in range(sample_size):
            # Select random relationship
            rel = np.random.choice(relationships)

            # Get all subject-object pairs for this relationship
            triples = list(self.onto_analyzer.g.triples((None, rel, None)))

            if triples:  # Make sure there are triples for this relationship
                # Select random triple
                subject, predicate, obj = np.random.choice(triples)

                # Get human-readable labels
                source_label = self.onto_analyzer.get_topic_label(subject)
                target_label = self.onto_analyzer.get_topic_label(obj)
                rel_name = str(predicate).split('#')[-1]  # Get the relationship name from URI

                prompt = f"In computer science, what is the relationship between {source_label} and {target_label}?"

                response = self.generate_response(prompt)

                # Compare with actual relationship
                if self.validate_relationship(response, rel_name):
                    correct_predictions += 1

        return correct_predictions / sample_size


    def test_concept_understanding(self, sample_size=1):
        """
        Test LLM's understanding of CSO concepts.
        """
        # Get concepts (topics) using the existing implementation
        concepts = self.onto_analyzer.topics
        results = []

        for concept in tqdm(concepts[:sample_size]):
            # Get human-readable label for the concept
            concept_label = self.onto_analyzer.get_topic_label(concept)

            prompt = f"Define the computer science concept: {concept_label}"
            response = self.generate_response(prompt)

            # Get concept definition from ontology if available
            definitions = list(self.onto_analyzer.g.objects(subject=concept,
                                                            predicate=self.onto_analyzer.RDFS.comment))
            ontology_definition = str(definitions[0]) if definitions else None

            # Compare with ontology definition if available
            accuracy = self.validate_definition(concept_label, response, ontology_definition)

            results.append({
                'concept': concept_label,
                'accuracy': accuracy,
                'has_definition': bool(ontology_definition)
            })

        return pd.DataFrame(results)


    @staticmethod
    def validate_definition(concept_label, llm_response, ontology_definition):
        """
        Validate LLM's concept definition against ontology.
        Basic implementation - can be enhanced with more sophisticated NLP techniques.
        """
        if ontology_definition is None:
            # If no ontology definition exists, return a neutral score
            return 0.5

        # Convert both to lowercase for comparison
        llm_response = llm_response.lower()
        ontology_definition = ontology_definition.lower()

        # Simple word overlap metric
        # Could be enhanced with more sophisticated semantic similarity measures
        response_words = set(llm_response.split())
        definition_words = set(ontology_definition.split())

        overlap = len(response_words.intersection(definition_words))
        total = len(response_words.union(definition_words))

        return overlap / total if total > 0 else 0


    def generate_response(self, prompt):
        """
        Generate response from LLM.
        """
        inputs  = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_new_tokens=100)

        return self.tokenizer.decode(outputs[0])


    def validate_relationship(self, response, actual_relation):
        """
        Validate if LLM's response matches the ontological relationship.
        """

        # Implement validation logic
        pass


if __name__ == "__main__":
    tester = LLMIntegrationTester(model_name)

    # Run llm_evaluations
    relationship_accuracy = tester.test_relationship_prediction()

    concept_understanding = tester.test_concept_understanding()

    print(f"Relationship Prediction Accuracy: {relationship_accuracy}")
    print("\nConcept Understanding Results:")
    print(concept_understanding.describe())