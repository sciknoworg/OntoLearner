# Import necessary modules from the ontolearner package
from ontolearner import AutoLLMLearner, AgrO, train_test_split, LabelMapper, StandardizedPrompting, evaluation_report

# Load the AgrO ontology (Agricultural Ontology)
ontology = AgrO()
ontology.load()  # Load the ontology data into memory

# Extract structured data (e.g., concept pairs, relations) and split it into training and test sets
train_data, test_data = train_test_split(ontology.extract(), test_size=0.2, random_state=42)

# Define the ontology learning task.
# Options include:
# - 'taxonomy-discovery' for learning hierarchical subclass relations,
# - 'term-typing' for concept classification,
# - 'non-taxonomic-re' for learning non-taxonomic (semantic) relations like "causes", "affects", etc.
task = 'non-taxonomic-re'

# Provide your Huggingface token for accessing the LLM (if needed for model hub or inference backend)
token = '...'

# Initialize the LLM-based learner with appropriate prompting and label mapping strategies
llm_learner = AutoLLMLearner(
    prompting=StandardizedPrompting,        # Prompting strategy to guide the LLM behavior
    label_mapper=LabelMapper(),    # Maps labels to natural language or model-friendly representations
    token=token                    # Token for authentication (e.g., Hugging Face or other providers)
)

# Load a specific LLM model, here Qwen2.5-0.5B-Instruct, a small instruction-tuned language model
llm_learner.load(model_id='Qwen/Qwen2.5-0.5B-Instruct')

# Fine-tune or adapt the LLM to the training data for the selected task
llm_learner.fit(train_data, task=task)

# Use the trained LLM to make predictions on the test set
predicts = llm_learner.predict(test_data, task=task)

# Print the prediction results
print(predicts)

# Do the evaluation
truth = llm_learner.tasks_ground_truth_former(data=test_data, task=task)
metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
print(metrics)
