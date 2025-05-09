from ..base import AutoLearnerRetriever
from typing import Any, List

class AutoBERTRetriever(AutoLearnerRetriever):

    def __init__(self):
        super().__init__()

    def load(self, model_id:str):
        pass

    def index(self, inputs: List[Any]):
        pass

    def retrieve(self, inputs: List[Any], top_k: int):
        pass
