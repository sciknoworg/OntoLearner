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

    def learn(self, data, task, retriever_id: str = None, llm_id: str = None,
              top_k: int = 5, **kwargs):
        if retriever_id and llm_id:
            self.learner.load(retriever_id=retriever_id, llm_id=llm_id)

        self.learner.train(train_data=data, task=task)

        if task == "term-typing":
            for term_typing in data.term_typings[:5]:
                raw_input = term_typing.term
                prediction = self.learner.predict(raw_input, task=task)[0]
                logger.info(f"Term: {raw_input}\n"
                            f"Predicted: {prediction}")
        elif task == "taxonomy-discovery":
            for tax_rel in data.type_taxonomies.taxonomies[:5]:
                raw_input = (tax_rel.parent, tax_rel.child)
                prediction = self.learner.predict(raw_input, task=task)
        elif task == "task-non-taxonomic-relations":
            for non_tax_rel in data.type_non_taxonomic_relations.non_taxonomies[:5]:
                raw_input = (non_tax_rel.head, non_tax_rel.tail)
                prediction = self.learner.predict(raw_input, task=task)
        else:
            raise ValueError(f"Task {task} not supported. Supported tasks: term-typing, "
                             f"taxonomy-discovery, task-non-taxonomic-relations")

        return prediction
