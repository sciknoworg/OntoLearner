import logging
from pathlib import Path
from typing import Dict, List, Optional, Union, Tuple

from .base import AutoLearner, AutoPrompt
from .evaluation import calculate_term_typing_metrics, aggregate_metrics
from .evaluation.visualisations import plot_precision_recall_distribution
from .learner import BERTRetrieverLearner, AutoLearnerLLM, AutoRAGLearner, StandardizedPrompting

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LearnerPipeline:
    """
    Orchestrates the ontology learning pipeline with retriever, LLM, and prompting.
    """
    def __init__(self,
                 task: str,
                 llm_id: str,
                 retriever_id: str,
                 hf_token: Optional[str] = None,
                 learner: Optional[AutoLearner] = None,
                 prompting: Optional[AutoPrompt] = None):
        """
        Initialize the learning pipeline.
        """
        self.results = []
        self.metrics = {}
        self.model_info = {"llm": llm_id, "retriever": retriever_id}

        if learner is not None:
            self.learner = learner
        else:
            retriever = BERTRetrieverLearner()
            llm = AutoLearnerLLM(token=hf_token)
            self.prompting = prompting or StandardizedPrompting(task=task)
            self.learner = AutoRAGLearner(retriever, llm, self.prompting)
            self.learner.load(retriever_id=retriever_id, llm_id=llm_id)

        if prompting is not None:
            self.prompting = prompting

    def learn(self, train_data, task: str, top_k: int = 5):
        """Train the learner on the given data"""
        self.learner.train(train_data=train_data, task=task)

    def predict(self, test_data, task: str, limit: int = 10) -> List[Dict]:
        """Predict on test data and return results with metrics"""
        results = []
        test_subset = test_data.term_typings[:limit]

        for typing in test_subset:
            term = typing.term
            ground_truth = typing.types
            predicted = self.learner.predict(term, task=task)
            metrics = calculate_term_typing_metrics(predicted, ground_truth)
            results.append({
                'term': term,
                'ground_truth': ground_truth,
                'predicted': predicted,
                **metrics
            })
        self.results = results

        return results

    def evaluate(self, output_dir: Optional[Union[str, Path]] = None) -> Dict:
        """Evaluate results and generate metrics"""
        if not self.results:
            logger.warning("No prediction results available for evaluation")
            return {}

        self.metrics = aggregate_metrics(self.results, "term-typing")

        if output_dir:
            output_dir = Path(output_dir)
            output_dir.mkdir(exist_ok=True, parents=True)

            all_results = [{
                **self.model_info,
                'metrics': self.metrics,
                'detailed_results': self.results
            }]

            plot_precision_recall_distribution(all_results, output_dir)
            logger.info(f"Results visualization saved to {output_dir}")

        return self.metrics

    def run_full_pipeline(self,
                          train_data,
                          test_data,
                          task: str,
                          top_k: int = 5,
                          test_limit: int = 10,
                          output_dir: Optional[Union[str, Path]] = None) -> Tuple[List[Dict], Dict]:
        """Run the complete pipeline from training to evaluation"""
        self.learn(train_data, task, top_k)
        results = self.predict(test_data, task, limit=test_limit)
        metrics = self.evaluate(output_dir)
        return results, metrics
