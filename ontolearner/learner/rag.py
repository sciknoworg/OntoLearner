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
