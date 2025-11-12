# Import core components from the OntoLearner library
from ontolearner import LearnerPipeline, AgrO, train_test_split

# Load the AgrO ontology, which includes structured agricultural knowledge
ontology = AgrO()
ontology.load()  # Load ontology data (e.g., entities, relations, metadata)

# Extract relation instances from the ontology and split them into training and test sets
train_data, test_data = train_test_split(
    ontology.extract(),      # Extract annotated (head, tail, relation) triples
    test_size=0.2,           # 20% for evaluation
    random_state=42          # Ensures reproducible splits
)

# Initialize the learning pipeline using a dense retriever
# This configuration uses sentence embeddings to match similar relational contexts
pipeline = LearnerPipeline(
    retriever_id='sentence-transformers/all-MiniLM-L6-v2',  # Hugging Face model ID for retrieval
    batch_size=10,       # Number of samples to process per batch (if batching is enabled internally)
    top_k=5              # Retrieve top-5 most relevant support instance per query
)

# Run the pipeline on the training and test data
# The pipeline performs: fit() → predict() → evaluate() in sequence
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    evaluate=True,           # If True, computes precision, recall, and F1-score
    task='non-taxonomic-re'  # Specifies that we are doing non-taxonomic relation prediction
)

# Print the evaluation metrics (precision, recall, F1)
print("Metrics:", outputs['metrics'])

# Print the total elapsed time for training and evaluation
print("Elapsed time:", outputs['elapsed_time'])

# Print the full output dictionary (includes predictions)
print(outputs)
