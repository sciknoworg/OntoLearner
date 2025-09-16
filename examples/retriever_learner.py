# Import necessary modules from the ontolearner library
from ontolearner import AutoRetrieverLearner, AgrO, train_test_split, evaluation_report

# Load the AgrO ontology, which is a domain-specific ontology used in agronomy
ontology = AgrO()
ontology.load()  # Load the ontology from OntoLearner huggingface repository

# Extract axioms or statements from the ontology, then split them into training and testing sets
train_data, test_data = train_test_split(ontology.extract(), test_size=0.2, random_state=42)

# Initialize a retriever-style learner for relation extraction tasks
# batch_size is being used inside the AutoRetrieverLearner to allow for larger KB retrieval!
ret_learner = AutoRetrieverLearner(top_k=5)

# Load a pre-trained retriever model using its identifier
ret_learner.load(model_id='sentence-transformers/all-MiniLM-L6-v2')

# Index the model on the training data for LLMs4OL task
# use task='term-typing' for term typing task
# use task='taxonomy-discovery' for taxonomic discovery task.
ret_learner.fit(train_data, task="non-taxonomic-re")

# Use the trained model to predict relations on the test data
predicts = ret_learner.predict(test_data, task="non-taxonomic-re")

# Do the evaluation
truth = ret_learner.tasks_ground_truth_former(data=test_data, task="non-taxonomic-re")
metrics = evaluation_report(y_true=truth, y_pred=predicts, task="non-taxonomic-re")
print(metrics)
