# Import necessary modules from the ontolearner library
from ontolearner import AutoRetrieverLearner, AgrO, train_test_split

# Load the AgrO ontology, which is a domain-specific ontology used in agronomy
ontology = AgrO()
ontology.load()  # Load the ontology from OntoLearner huggingface repository

# Extract axioms or statements from the ontology, then split them into training and testing sets
train_data, test_data = train_test_split(ontology.extract(), test_size=0.2, random_state=42)

# Initialize a retriever-style learner for relation extraction tasks
ret_learner = AutoRetrieverLearner()

# Load a pre-trained retriever model using its identifier
ret_learner.load(model_id='sentence-transformers/all-MiniLM-L6-v2')

# Index the model on the training data for LLMs4OL task
# use task='term-typing' for term typing task
# use task='taxonomy-discovery' for taxonomic discovery task.
ret_learner.fit(train_data, task="non-taxonomic-re")

# Use the trained model to predict relations on the test data
predict = ret_learner.predict(test_data, task="non-taxonomic-re")
