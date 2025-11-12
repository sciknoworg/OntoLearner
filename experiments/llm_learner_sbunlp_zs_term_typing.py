# Import core modules from the OntoLearner library
from ontolearner import GO, train_test_split, LearnerPipeline

# Import the specific Zero-Shot Learner implementation for Term Typing
from ontolearner.learner.term_typing.sbunlp import SBUNLPZSLearner

# Load ontology and split
# Load the AgrO ontology for type inventory and test data.
ontology = GO()
ontology.load()
data = ontology.extract()  # Extract the full set of relationships/terms

# Split the data into train (to learn type inventory) and test (terms to predict)
train_data, test_data = train_test_split(
    data,
    test_size=0.3,  # 60% of data used for testing
    random_state=42,
)

# Configure the Qwen Zero-Shot learner (inference-only)
# This learner's 'fit' phase learns the vocabulary of allowed type labels.
llm_learner = SBUNLPZSLearner(
    device="cuda",
    max_new_tokens=64,
    temperature=0.0,
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    token=None,
)

# Build pipeline and run
# Build the pipeline, passing the Zero-Shot Learner.
pipe = LearnerPipeline(
    llm=llm_learner,
    llm_id=llm_learner.model_id,
    ontologizer_data=False,
    device="cuda",  #  select CUDA or CPU
)

# Run the full learning pipeline on the Term-Typing task
outputs = pipe(
    train_data=train_data,
    test_data=test_data,
    task="term-typing",
    evaluate=True,
    ontologizer_data=False,
)

# Display the evaluation results
print("Metrics:", outputs.get("metrics"))

# Display total elapsed time for learning (type inventory) + prediction + evaluation
print("Elapsed time:", outputs.get("elapsed_time"))

# Print all returned outputs (include predictions)
print(outputs)
