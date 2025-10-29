# Import core modules from the OntoLearner library
from ontolearner import GeoNames, train_test_split, LearnerPipeline
# Import the specific Few-Shot Learner implementation
from ontolearner import SBUNLPFewShotLearner

# Load ontology and split
# Load the GeoNames ontology for taxonomy discovery.
# GeoNames provides geographic parent-child relationships (is-a hierarchy).
ontology = GeoNames()
ontology.load()
data = ontology.extract() # Extract the list of taxonomic relationships from the ontology object

# Split the taxonomic relationships into train and test sets
train_data, test_data = train_test_split(
    data,
    test_size=0.6, # 60% of data used for testing (terms to find relations for)
    random_state=42,
)

# Configure the learner with user-defined inference args + device
# Configure the SBUNLP Few-Shot Learner using the Qwen model.
# This performs in-context learning via N x M batch prompting.
llm_learner = SBUNLPFewShotLearner(
    # Model / decoding
    model_name="Qwen/Qwen2.5-0.5B-Instruct", # The Qwen model to load
    try_4bit=True,              # uses 4-bit if bitsandbytes + CUDA available for memory efficiency
    max_new_tokens=140,         # limit the length of the model's response (for JSON output)
    max_input_tokens=1500,      # limit the total prompt length (context window)
    temperature=0.0,            # set to 0.0 for deterministic output (best for structured JSON)
    top_p=1.0,                  # top-p sampling disabled with temperature=0.0

    # Grid settings (N x M prompts)
    n_train_chunks=7,           # N: split training examples (few-shot context) into 7 chunks
    m_test_chunks=7,            # M: split test terms (vocabulary) into 7 chunks (total 49 prompts)

    # Run controls
    limit_prompts=None,         # None runs all N x M prompts; set to an integer for a dry-run
    output_dir="./outputs/taskC_batches",  # Optional: dump per-prompt JSON results for debugging
)

# Build pipeline and run
# Build the pipeline, passing the Few-Shot Learner.
pipe = LearnerPipeline(
    llm=llm_learner,
    llm_id=llm_learner.model_name,
    ontologizer_data=True,      # Let the learner flatten structured ontology objects via its tasks_* helpers
    device="auto",              # automatically select CUDA or CPU
)

# Run the full learning pipeline on the taxonomy-discovery task
outputs = pipe(
    train_data=train_data,
    test_data=test_data,
    task="taxonomy-discovery",
    evaluate=True,
    ontologizer_data=True,
)

# Display the evaluation results
print("Metrics:", outputs.get("metrics"))

# Display total elapsed time for training + prediction + evaluation
print("Elapsed time:", outputs["elapsed_time"])

# Print all returned outputs (include predictions)
print(outputs)
