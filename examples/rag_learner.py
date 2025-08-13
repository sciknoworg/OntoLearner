# Import components from OntoLearner for ontology-based learning using LLMs and retrievers
from ontolearner import (
    AutoLLMLearner,         # Wrapper for zero-shot LLM-based learners
    AutoRetrieverLearner,   # Wrapper for dense retriever models
    AutoRAGLearner,         # Combines LLM + retriever into a RAG pipeline
    AgrO,                   # Example agricultural ontology
    train_test_split,       # Helper function for data splitting
    LabelMapper,            # Maps ontology labels to/from textual representations
    StandardizedPrompting,   # Standard prompting strategy across tasks
    evaluation_report
)

# Load the AgrO ontology (an agricultural domain ontology)
ontology = AgrO()
ontology.load()

# Extract structured data from the ontology and split into train/test sets
train_data, test_data = train_test_split(
    ontology.extract(),
    test_size=0.2,          # Use 20% for testing
    random_state=42         # Seed for reproducibility
)

# Choose the ontology learning task
# Options: 'term-typing', 'taxonomy-discovery', or 'non-taxonomic-re'
task = 'non-taxonomic-re'

# Provide your huggingface token for LLM access
token = '...'

# Initialize the LLM learner with prompting and label mapping strategies
llm_learner = AutoLLMLearner(
    prompting=StandardizedPrompting,  # Use a pre-defined prompt format
    label_mapper=LabelMapper(),       # Convert between label formats and natural language
    token=token                       # API token to access the LLM
)

# Initialize the retriever to find top-k relevant facts or examples
retriever_learner = AutoRetrieverLearner(top_k=2)  # Use top 2 retrieved candidates

# Create a RAG (Retrieval-Augmented Generation) pipeline by combining LLM and retriever
rag_learner = AutoRAGLearner(
    llm=llm_learner,
    retriever=retriever_learner
)

# Load the retriever and LLM models by their names or IDs
rag_learner.load(
    retriever_id='sentence-transformers/all-MiniLM-L6-v2',   # Sentence-level transformer for retrieval
    llm_id='Qwen/Qwen2.5-0.5B-Instruct'                      # Small-scale instruction-following LLM
)

# Train (or adapt) the RAG model on the training data for the selected task
rag_learner.fit(train_data, task=task)

# Predict the output on the test set using the trained RAG model
predicts = rag_learner.predict(test_data, task=task)

# Print prediction results
print(predicts)

# Do the evaluation
truth = llm_learner.tasks_ground_truth_former(data=test_data, task=task)
metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
print(metrics)
