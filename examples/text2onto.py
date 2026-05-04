import os

# Import necessary modules from the OntoLearner library
from ontolearner.ontology import OM
from ontolearner.text2onto import SyntheticGenerator, SyntheticDataSplitter

# Define the Hugging Face model configuration used for synthetic generation.
MODEL_ID = os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct")
HF_TOKEN = os.getenv("HF_TOKEN", "")
DEVICE = os.getenv("TEXT2ONTO_DEVICE", "auto")

# Set parameters for synthetic pseudo-sentence generation
pseudo_sentence_batch_size = 50
max_worker_count_for_llm_calls = 3

# Instantiate the synthetic sentence generator for ontology data
text2onto_synthetic_generator = SyntheticGenerator(
    batch_size=pseudo_sentence_batch_size,
    worker_count=max_worker_count_for_llm_calls,  # used as a generation micro-batch size
    model_id=MODEL_ID,
    token=HF_TOKEN,
    device=DEVICE,
)

# Load an example ontology using the OM class
ontology = OM()
ontology.load()

# Extract structured data from the ontology
ontological_data = ontology.extract()

# Print statistics about the extracted ontology content
print(f"term types: {len(ontological_data.term_typings)}")
print(f"taxonomic relations: {len(ontological_data.type_taxonomies.taxonomies)}")
print(f"non-taxonomic relations: {len(ontological_data.type_non_taxonomic_relations.non_taxonomies)}")

# Generate synthetic training data from the ontology using the transformers backend
synthetic_data = text2onto_synthetic_generator.generate(
    ontological_data=ontological_data,
    topic=ontology.domain    # Pass the ontology's domain as a topic prompt
)

# Initialize the data splitter for train/val/test splits
splitter = SyntheticDataSplitter(
    synthetic_data=synthetic_data,
    onto_name=ontology.ontology_id
)

# split the train, val, test
train_data, val_data, test_data = splitter.train_test_val_split(
    train=0.8,
    val=0.0,
    test=0.2,
)

# print train split
print("\nTRAIN split:")
print("  docs:", len(train_data.get("documents", [])))
print("  terms:", len(train_data.get("terms", [])))
print("  types:", len(train_data.get("types", [])))
print("  terms2docs:", len(train_data.get("terms2docs", {})))
print("  terms2types:", len(train_data.get("terms2types", {})))

# print val split
print("\nVAL split:")
print("  docs:", len(val_data.get("documents", [])))
print("  terms:", len(val_data.get("terms", [])))
print("  types:", len(val_data.get("types", [])))
print("  terms2docs:", len(val_data.get("terms2docs", {})))
print("  terms2types:", len(val_data.get("terms2types", {})))

# print test split
print("\nTEST split:")
print("  docs:", len(test_data.get("documents", [])))
print("  terms:", len(test_data.get("terms", [])))
print("  types:", len(test_data.get("types", [])))
print("  terms2docs:", len(test_data.get("terms2docs", {})))
print("  terms2types:", len(test_data.get("terms2types", {})))
