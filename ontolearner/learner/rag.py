from ..base import AutoLearner

from typing import Any

class RAGLearner(AutoLearner):
    def __init__(self, learner_retriever: Any, learner_llm: Any, prompt: str=None):
        super().__init__()
        pass

    def load(self, retriever_id: str, llm_id: str):
        pass

    def train(self, train_data: Any, task: str):
        pass

    def predict(self, eval_data: Any, task: str):
        pass

""""
from ontolearner import RAGLearner, AutoLLM, AutoBERTRetriever

learner_retriever = AutoBERTRetriever()
learner_llm = AutoLLM()

rag_learner = RAGLearner(learner_retriever=learner_retriever,
                         learner_llm=learner_llm)

rag_learner.load(retriever_id = "", llm_id="")

data = []
task = "A"

rag_learner.train(data=data, task=task)

predicts = rag_learner.train(data=data, task=task)
"""
