
from abc import ABC

from typing import Any, List

class AutoLearner(ABC):

    def __init__(self, **kwargs):
        pass

    def load(self, **kwargs):
        pass

    def train(self, train_data: Any, task: str):
        pass

    def predict(self, eval_data: Any, task: str) -> Any:
        pass

    def train_predict(self, train_data:Any, eval_data:Any, task:str) -> Any:
        self.train(train_data, task)
        predicts = self.predict(eval_data, task)
        return predicts

class AutoLearnerLLM(ABC):
    def __init__(self):
        self.model = None
        self.tokenizer = None

    def load(self, model_id:str):
        pass

    def generate(self, inputs: List[Any]):
        pass

class AutoLearnerRetriever(ABC):
    def __init__(self):
        self.model = None

    def load(self, model_id:str):
        pass

    def index(self, inputs: List[Any]):
        pass

    def retrieve(self, inputs: List[Any], top_k: int):
        pass

class AutoPrompt(ABC):
    def __init__(self, prompt_template: str):
        self.prompt_template = prompt_template

    def format(self, **kwargs):
        pass
