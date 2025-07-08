# Import the main components from the OntoLearner library
from ontolearner import LearnerPipeline, AgrO, train_test_split

# Load the AgrO ontology, which contains agricultural concepts and relationships
ontology = AgrO()
ontology.load()  # Parse and initialize internal ontology structures, including term-type pairs

# Extract annotated examples (terms and their types), and split into train/test sets
train_data, test_data = train_test_split(
    ontology.extract(),     # Extract raw (term, types) instances from the ontology
    test_size=0.2,          # 20% of the data is reserved for evaluation
    random_state=42         # Ensure reproducibility by setting a fixed seed
)

# Set up the learner pipeline using a lightweight instruction-tuned LLM
pipeline = LearnerPipeline(
    llm_id='Qwen/Qwen2.5-0.5B-Instruct',   # Small-scale LLM for reasoning over term-type assignments
    hf_token='...',                        # Hugging Face access token for loading gated models
    batch_size=32                          # Batch size for parallel inference (if applicable)
)

# Run the full learning pipeline on the term-typing task
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    evaluate=True,               # Enables automatic computation of precision, recall, F1
    task='term-typing'           # The task is to classify terms into semantic types
)

# Display the evaluation results
print("Metrics:", outputs['metrics'])          # Shows {'precision': ..., 'recall': ..., 'f1_score': ...}

# Display total elapsed time for training + prediction + evaluation
print("Elapsed time:", outputs['elapsed_time'])

# Print all returned outputs (include predictions)
print(outputs)
