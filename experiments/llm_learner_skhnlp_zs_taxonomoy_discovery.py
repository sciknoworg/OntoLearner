# Import core modules from the OntoLearner library
from ontolearner import GO, train_test_split, LearnerPipeline
from ontolearner.learner.taxonomy_discovery.skhnlp import SKHNLPZSLearner

# Load ontology and split data
# The GeoNames ontology provides geographic term types and relationships.
ontology = GO()
ontology.load()
train_data, test_data = train_test_split(
    ontology.extract(),
    test_size=0.3,
    random_state=42,
)

# Configure the learner with user-defined generation and normalization settings
# Configure the Zero-Shot Qwen Learner for taxonomy discovery.
# This model uses a fixed prompt and string normalization (Levenshtein) to classify terms.
llm_learner = SKHNLPZSLearner(
    model_name="Qwen/Qwen2.5-0.5B-Instruct",
    device="cuda",  # use "cuda" if you have a GPU
    max_new_tokens=16,
    save_path="./outputs/",  # directory or full file path for CSV
    verbose=True,
    normalize_mode="levenshtein",  # "none" | "substring" | "levenshtein" | "auto"
)

# Build pipeline and run
pipe = LearnerPipeline(
    llm=llm_learner,
    llm_id="Qwen/Qwen2.5-0.5B-Instruct",
    ontologizer_data=False,
    device="cuda",
)

# Run the full learning pipeline on the taxonomy-discovery task
outputs = pipe(
    train_data=train_data,  # zero-shot; ignored by the LLM learner
    test_data=test_data,
    task="taxonomy-discovery",
    evaluate=True,
    ontologizer_data=False,
)

# Display the evaluation results
print("Metrics:", outputs.get("metrics"))

# Display total elapsed time for training + prediction + evaluation
print("Elapsed time:", outputs["elapsed_time"])

# Print all returned outputs (include predictions)
print(outputs)
