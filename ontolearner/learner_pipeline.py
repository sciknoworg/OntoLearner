from abc import ABC

from .base import AutoLearner, AutoPrompt

class Learner(ABC):

    def __init__(self, learner:AutoLearner, prompting: AutoPrompt):
        pass

    def learn(self, data, task, retriever_id:str=None, llm_id:str=None, top_k: int = 5):
        pass



""""
from ontolearner import RAGLearner, AutoLLM, AutoBERTRetriever, Learner, StandardizedPrompting
rag_learner = RAGLearner(learner_retriever=AutoBERTRetriever(), learner_llm=AutoLLM())
learner = Learner(learner = rag_learner, prompting=prompting)
learner.learn(data=[], task="A", retriever_id, llm_id, top_k, return_result=False, save_path="",...)
    # rag_learner.load(retriever_id = "", llm_id="")
    # rag_learner.train(data=data, task=task)
    # predicts = rag_learner.train(data=data, task=task)
"""
