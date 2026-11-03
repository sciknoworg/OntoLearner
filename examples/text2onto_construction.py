"""Full OM Text2Onto construction example. Runs top-to-bottom; no saved files.

Windows Command Prompt:
    conda activate ontolearner
    set OPENAI_API_KEY=YOUR_COMPLETE_API_KEY
    python -u text2onto_construction.py

Optional: set FULL_PREPROCESS=1 to enable extra LLM cleaning (API charges).
"""

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
full_preprocess = os.getenv("FULL_PREPROCESS", "0") == "1"

if not api_key:
    raise EnvironmentError("Set OPENAI_API_KEY before running.")

print("\nSTEP 1: Loading the complete OM ontology", flush=True)
ontology = OM()
ontology.load()

data = ontology.extract()

# Keep only 2 taxonomic relations from OM
data.term_typings = []
data.type_taxonomies.taxonomies = data.type_taxonomies.taxonomies[:2]
data.type_non_taxonomic_relations.non_taxonomies = []

print("Selected relations:", len(data.type_taxonomies.taxonomies))

train_ontology, test_ontology = train_test_split(
    data,
    test_size=0.5,
    random_state=42
)

print("Train term typings:", len(train_ontology.term_typings), flush=True)
print("Train taxonomies:", len(train_ontology.type_taxonomies.taxonomies), flush=True)
print("Test term typings:", len(test_ontology.term_typings), flush=True)
print("Test taxonomies:", len(test_ontology.type_taxonomies.taxonomies), flush=True)

print("\nSTEP 3: Loading the Hugging Face generator", flush=True)
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
print("Generator ready:", model_id, flush=True)

print("\nSTEP 4: Generating synthetic TRAIN documents", flush=True)
train_synthetic = generator.generate(
    ontological_data=train_ontology, topic=ontology.domain
)
print("Generated train documents:", len(train_synthetic.generated_docs), flush=True)

print("\nSTEP 5: Generating synthetic TEST documents", flush=True)
test_synthetic = generator.generate(
    ontological_data=test_ontology, topic=ontology.domain
)
print("Generated test documents:", len(test_synthetic.generated_docs), flush=True)

print("\nSTEP 6: Initializing preprocessors", flush=True)
print("Full LLM-based preprocessing:", full_preprocess, flush=True)
client = OpenAI(api_key=api_key) if full_preprocess else None
train_preprocessor = SyntheticDataPreprocessor(
    client=client,
    clean_text=full_preprocess,
    alignment_filter=full_preprocess,
)
test_preprocessor = SyntheticDataPreprocessor(
    client=client,
    clean_text=full_preprocess,
    deep_clean=full_preprocess,
)

print("\nSTEP 7: Preprocessing TRAIN documents", flush=True)
train_records = train_preprocessor.preprocess(train_synthetic, train_ontology)
print("Train records:", len(train_records), flush=True)

print("\nSTEP 8: Preprocessing TEST documents", flush=True)
test_records = test_preprocessor.preprocess(test_synthetic, test_ontology)
print("Test records:", len(test_records), flush=True)

print("\nSTEP 9: Preparing construction dataset", flush=True)
dataset = PrimitiveOntologyDataset(
    task="construction", random_state=42, drop_empty=True
)
train_data = dataset.prepare(train_records)
test_data = dataset.prepare(test_records)
print("Train samples:", len(train_data), flush=True)
print("Test samples:", len(test_data), flush=True)

print("\nSTEP 10: Example training record", flush=True)
if train_data:
    print(json.dumps(train_data[0], indent=2, ensure_ascii=False)[:2000], flush=True)
else:
    print("No train samples were retained.", flush=True)

print("\nSTEP 11: Example test record (includes gold labels)", flush=True)
if test_data:
    print(json.dumps(test_data[0], indent=2, ensure_ascii=False)[:2000], flush=True)
else:
    print("No test samples were retained.", flush=True)

print("\nDONE: train_data and test_data are available in memory.", flush=True)
# During prediction, hide gold fields from the learner (e.g. via
# dataset.prepare(test_records, test=True)); retain test_data for evaluation.
# This example prepares data only; it does not call a learner.
