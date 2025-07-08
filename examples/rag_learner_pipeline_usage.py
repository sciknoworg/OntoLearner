# Import core modules from the OntoLearner library
from ontolearner import LearnerPipeline, AgrO, train_test_split

# Load the AgrO ontology, which contains concepts related to wines, their properties, and categories
ontology = AgrO()
ontology.load()  # Load entities, types, and structured term annotations from the ontology

# Extract term-typing instances and split into train and test sets
train_data, test_data = train_test_split(
    ontology.extract(),     # Extract (term, type) annotations from the ontology
    test_size=0.2,          # Use 20% of the data for evaluation
    random_state=42         # Ensure reproducibility of the data split
)

# Initialize a multi-component learning pipeline (retriever + LLM)
# This configuration enables a Retrieval-Augmented Generation (RAG) setup
pipeline = LearnerPipeline(
    retriever_id='sentence-transformers/all-MiniLM-L6-v2',      # Dense retriever model for nearest neighbor search
    llm_id='Qwen/Qwen2.5-0.5B-Instruct',                        # Lightweight instruction-tuned LLM for reasoning
    hf_token='...',                                             # Hugging Face token for accessing gated models
    batch_size=32,                                              # Batch size for training/prediction if supported
    top_k=5                                                     # Number of top retrievals to include in RAG prompting
)

# Run the pipeline: training, prediction, and evaluation in one call
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    evaluate=True,              # Compute metrics like precision, recall, and F1
    task='term-typing'          # Specifies the task
)

# Print final evaluation metrics
print("Metrics:", outputs['metrics'])

# Print the total time taken for the full pipeline execution
print("Elapsed time:", outputs['elapsed_time'])

# Print all outputs (including predictions)
print(outputs)
