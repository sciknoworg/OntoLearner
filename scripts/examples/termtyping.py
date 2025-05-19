"""
Example script demonstrating the term-typing workflow with OntoLearner.

This script shows how to:
1. Import an ontology
2. Perform train-test split
3. Run term-typing task with selected LLM and retriever
4. Evaluate and visualize results
"""
from ontolearner import ontology, utils, learner
onto = ontology.Wine()
data = onto.extract()
train_data, test_data = utils.train_test_split(data,
                                               test_size=0.2,
                                               random_state=42)
retriever=learner.BERTRetrieverLearner()
llm=learner.AutoLearnerLLM()
prompt = learner.StandardizedPrompting(task="term-typing")
learner = learner.AutoRAGLearner(learner_retriever=retriever,
                                 learner_llm=llm,
                                 prompting=prompt)
learner.load(retriever_id="mistralai/Mistral-7B-Instruct-v0.1",
             llm_id="sentence-transformers/all-MiniLM-L6-v2")
learner.train(train_data=train_data, task="term-typing")
predicted = learner.predict(test_data, task="term-typing")
