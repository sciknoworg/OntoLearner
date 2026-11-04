import os
import json

from openai import OpenAI
from ontolearner import train_test_split
from ontolearner.ontology import OM
from ontolearner.text2onto import (
    SyntheticGenerator,
    SyntheticDataPreprocessor,
    PrimitiveOntologyDataset,
)

# Configuration
model_id = os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct")
api_key = os.getenv("OPENAI_API_KEY")
hf_token = os.getenv("HF_TOKEN", "")

if not api_key:
    raise EnvironmentError("Set OPENAI_API_KEY before running.")

print("\nSTEP 1: Loading the complete OM ontology")
ontology = OM()
ontology.load()

data = ontology.extract()

# Keep 10 taxonomic relations of OM: a few short documents, each with several triples (the
# expansion task needs records with more than one triple per type to extend)
data.term_typings = []
data.type_taxonomies.taxonomies = data.type_taxonomies.taxonomies[:10]
data.type_non_taxonomic_relations.non_taxonomies = []

print("Selected relations:", len(data.type_taxonomies.taxonomies))

print("\nSTEP 2: Splitting the ontology into train and test parts")
# The train and test documents are generated from different relations.
train_ontology, test_ontology = train_test_split(
    data,
    test_size=0.5,
    random_state=42
)
print("Train taxonomies:", len(train_ontology.type_taxonomies.taxonomies))
print("Test taxonomies:", len(test_ontology.type_taxonomies.taxonomies))

print("\nSTEP 3: Loading the dataset generator")
generator = SyntheticGenerator(
    model_id=model_id,
    token=hf_token,
    extraction_method="openai",
    openai_api_key=api_key,
    openai_model="gpt-4o-mini",
    batch_size=5,
    generation_batch_size=2,
    min_pseudo_sentences=1,
    max_input_length=2000,
    max_new_tokens=2000,
)
print("Generator ready:", model_id)

print("\nSTEP 4: Generating synthetic TRAIN documents")
train_synthetic = generator.generate(
    ontological_data=train_ontology, topic=ontology.domain
)
print("Generated train documents:", len(train_synthetic.generated_docs))

print("\nSTEP 5: Generating synthetic TEST documents")
test_synthetic = generator.generate(
    ontological_data=test_ontology, topic=ontology.domain
)
print("Generated test documents:", len(test_synthetic.generated_docs))

print("\nSTEP 6: Initializing preprocessors")
# an LLM judge keeps the train records whose text
# supports their triples, and the test records get the six-stage cleaning.
client = OpenAI(api_key=api_key)
train_preprocessor = SyntheticDataPreprocessor(client=client, alignment_filter=True)
test_preprocessor = SyntheticDataPreprocessor(client=client, deep_clean=True)

print("\nSTEP 7: Preprocessing TRAIN documents")
train_records = train_preprocessor.preprocess(train_synthetic, train_ontology)
print("Train records:", len(train_records))

print("\nSTEP 8: Preprocessing TEST documents")
test_records = test_preprocessor.preprocess(test_synthetic, test_ontology)
print("Test records:", len(test_records))

print("\nSTEP 9: Preparing the expansion train and test data")
# expansion: every record is a sample as it is (a text and its complete ontology).
dataset = PrimitiveOntologyDataset(task="ontology_expansion", random_state=42)
train_data = dataset.prepare(train_records)
test_data = dataset.prepare(test_records)
print("Train samples:", len(train_data))
print("Test samples:", len(test_data))

