from ..base import AutoLearnerLLM
from typing import Any, List

class AutoLLM(AutoLearnerLLM):
    def __init__(self):
        super().__init__()

    def load(self, model_id:str):
        pass

    def generate(self, inputs: List[Any]):
        pass
