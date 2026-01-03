# Import the DSPy library for declarative prompting with LLMs
import dspy

# Import necessary modules from the OntoLearner library
from ontolearner.ontology import OM
from ontolearner.text2onto import SyntheticGenerator, SyntheticDataSplitter

# Define your LLM credentials and model configuration
LLM_MODEL_ID = "..."      # e.g., "gpt-4" or "ollama/mistral"
LLM_API_KEY = "..."       # API key for accessing the model
LLM_BASE_URL = "..."      # Base URL for the LLM provider (if using LiteLLM or similar)

# Configure DSPy to use the specified LLM via LiteLLM
# See: https://docs.litellm.ai/docs/providers for setting up providers
dspy_llm = dspy.LM(
    model=LLM_MODEL_ID,
    cache=True,           # Cache previous completions to save costs/time
    max_tokens=4000,      # Maximum tokens allowed in a single response
    temperature=0,        # Set to 0 for deterministic output
    api_key=LLM_API_KEY,
    base_url=LLM_BASE_URL
)

# Apply the LLM configuration to DSPy
dspy.configure(lm=dspy_llm)

# Set parameters for synthetic pseudo-sentence generation
pseudo_sentence_batch_size = 50
max_worker_count_for_llm_calls = 3

# Instantiate the synthetic sentence generator for ontology data
text2onto_synthetic_generator = SyntheticGenerator(
    batch_size=pseudo_sentence_batch_size,
    worker_count=max_worker_count_for_llm_calls
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

# Generate synthetic training data from the ontology using LLMs
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
