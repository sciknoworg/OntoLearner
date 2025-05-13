import logging
from abc import ABC

from .base import AutoLearner, AutoPrompt

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Learner(ABC):
    """Orchestrates the learning pipeline with retriever, LLM, and prompting."""
    def __init__(self, learner: AutoLearner, prompting: AutoPrompt):
        self.learner = learner
        self.prompting = prompting

    def learn(self, data, task, retriever_id: str = None, llm_id: str = None, top_k: int = 5, **kwargs):
        if retriever_id and llm_id:
            self.learner.load(retriever_id=retriever_id, llm_id=llm_id)

        self.learner.train(train_data=data, task=task)
