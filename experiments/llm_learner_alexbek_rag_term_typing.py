# Import core modules from the OntoLearner library
from ontolearner import GO, train_test_split, LearnerPipeline
from ontolearner.learner.term_typing.alexbek import AlexbekRAGLearner

# Load the GeoNames ontology.
ontology = GO()
ontology.load()

# Extract labeled items and split into train/test sets for evaluation
train_data, test_data = train_test_split(
    ontology.extract(), test_size=0.3, random_state=42
)

# Configure a Retrieval-Augmented Generation (RAG) term-typing classifier.
# - llm_model_id: generator used to predict types from the prompt + retrieved examples
# - retriever_model_id: encoder used to embed items and fetch top-k similar (RAG) examples
# - device: "cuda" for GPU or "cpu"
# - top_k: number of nearest examples to retrieve per query term
# - max_new_tokens: decoding budget of the LLM during prediction
# - output_dir: where intermediate artifacts / logs can be stored
rag_learner = AlexbekRAGLearner(
    llm_model_id="Qwen/Qwen2.5-0.5B-Instruct",
    retriever_model_id="sentence-transformers/all-MiniLM-L6-v2",
    device="cuda",
    top_k=3,
    max_new_tokens=256,
    output_dir="./results/",
)

# Build the pipeline and pass raw structured objects end-to-end.
# We place the RAG learner in the llm slot and set llm_id accordingly.
pipe = LearnerPipeline(
    llm=rag_learner,
    llm_id="Qwen/Qwen2.5-0.5B-Instruct",
    ontologizer_data=True,
)

# Run the full learning pipeline on the term-typing task
# - task="term-typing" (Task B)
# - evaluate=True computes precision/recall/F1 on the held-out test split
# - ontologizer_data=True must match the pipeline flag above
outputs = pipe(
    train_data=train_data,
    test_data=test_data,
    task="term-typing",
    evaluate=True,
    ontologizer_data=True,
)

# Display the evaluation results and runtime
print(
    "Metrics:", outputs.get("metrics")
)  # e.g., {'precision': ..., 'recall': ..., 'f1_micro': ..., ...}
print("Elapsed time (s):", outputs.get("elapsed_time"))
