# Import core modules from the OntoLearner library
from ontolearner import GeoNames, train_test_split, LearnerPipeline
from ontolearner.learner.term_typing import AlexbekRFLearner # A random-forest term-typing learner over text+graph features

# Load the GeoNames ontology and extract labeled term-typing data

ontology = GeoNames()
ontology.load()

data = ontology.extract()

# Split the labeled term-typing data into train and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Configure the RF-based learner (embeddings + optional graph features)
#    - device: "cpu" or "cuda"
#    - threshold: decision threshold for multi-label assignment
#    - use_graph_features: include ontology-graph-derived features if available
rf_learner = AlexbekRFLearner(
    device="cpu",  # switch to "cuda" if you have a GPU
    batch_size=16,
    max_length=512,  # max tokenizer length for embedding model inputs
    threshold=0.30,  # probability cutoff for assigning each type
    use_graph_features=True,  # set False for pure RF on text embeddings only
)

# Build the pipeline and pass raw structured objects end-to-end.
pipe = LearnerPipeline(
    retriever=rf_learner,
    retriever_id="intfloat/e5-base-v2",  # or "Qwen/Qwen3-Embedding-4B" if you have sufficient GPU memory
    ontologizer_data=True,  # True if data is already {"term": ..., "types": [...], ...}
    device="cpu",
    batch_size=16,
)

# Run the full learning pipeline on the term-typing task
outputs = pipe(
    train_data=train_data,
    test_data=test_data,
    task="term-typing",
    evaluate=True,
    ontologizer_data=True,
)

# Display evaluation summary and runtime
print("Metrics:", outputs.get("metrics"))

print("Elapsed time:", outputs["elapsed_time"])

print(ontology)
