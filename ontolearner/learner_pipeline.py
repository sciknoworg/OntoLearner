# Copyright (c) 2025 SciKnowOrg
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from pathlib import Path
from typing import Dict, List, Optional, Union, Tuple, Any

from .base import AutoLearner, AutoPrompt
from .evaluation import calculate_term_typing_metrics, aggregate_metrics, calculate_taxonomy_metrics, \
    calculate_non_taxonomy_metrics
from .evaluation.visualisations import plot_precision_recall_distribution
from .learner import BERTRetrieverLearner, AutoLearnerLLM, AutoRAGLearner, StandardizedPrompting

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LearnerPipeline:
    """
    Unified pipeline for ontology learning with flexible model configurations.

    This class provides a high-level interface for ontology learning tasks, supporting
    multiple learning paradigms and handling the complete machine learning workflow
    from training to evaluation. It abstracts away the complexity of different learner
    types while providing fine-grained control over the learning process.
    """
    def __init__(self,
                 task: str,
                 learner: Optional[AutoLearner] = None,
                 prompting: Optional[AutoPrompt] = None,
                 retriever: Optional[Any] = None,
                 llm: Optional[Any] = None,
                 retriever_id: Optional[str] = None,
                 llm_id: Optional[str] = None,
                 hf_token: Optional[str] = None):
        """
        Initialize the learning pipeline with flexible configuration options.

        This constructor supports multiple initialization patterns to accommodate
        different use cases, from simple model ID specification to complex custom
        component configuration. The pipeline automatically determines the learning
        paradigm based on the provided components.

        Args:
            task: The ontology learning task to perform. Supported values:
                 - "term-typing": Predict semantic types for terms
                 - "taxonomy-discovery": Identify hierarchical relationships
                 - "non-taxonomy-discovery": Identify semantic associations
            learner: Pre-configured learner instance. If provided, other
                    component parameters are ignored.
            prompting: Custom prompting strategy. If None, uses StandardizedPrompting
                      with task-appropriate templates.
            retriever: Pre-configured retriever instance. Used for RAG or
                      retrieval-only approaches.
            llm: Pre-configured LLM instance. Used for RAG or LLM-only approaches.
            retriever_id: Hugging Face model ID for automatic retriever loading.
                         Common options: "sentence-transformers/all-MiniLM-L6-v2"
            llm_id: Hugging Face model ID for automatic LLM loading.
                   Common options: "mistralai/Mistral-7B-Instruct-v0.1"
            hf_token: Hugging Face authentication token for accessing gated models.
                     Required for some commercial or restricted models.

        Raises:
            ValueError: If no learner components are provided (all learner-related
                       parameters are None).
        """
        self.task = task
        self.results = []
        self.metrics = {}
        self.model_info = {"task": task}

        if retriever_id:
            self.model_info["retriever"] = retriever_id
        if llm_id:
            self.model_info["llm"] = llm_id

        # Case 1: Use pre-configured learner if provided
        if learner is not None:
            self.learner = learner
            if prompting is not None:
                self.prompting = prompting
            return

        # Case 2: Configure components based on what's provided
        if prompting is None:
            self.prompting = StandardizedPrompting(task=task)
        else:
            self.prompting = prompting

        # Case 3: Create retriever if needed
        if retriever is None and retriever_id is not None:
            retriever = BERTRetrieverLearner()
            if retriever_id:
                retriever.load(retriever_id)

        # Case 4: Create LLM if needed
        if llm is None and llm_id is not None:
            llm = AutoLearnerLLM(token=hf_token)
            if llm_id:
                llm.load(llm_id)

        if retriever is not None and llm is not None:
            # RAG-based learner (retriever + LLM)
            self.learner = AutoRAGLearner(retriever, llm, self.prompting)
        elif retriever is not None:
            # Retriever-only learner
            self.learner = retriever
        elif llm is not None:
            # LLM-only learner
            self.learner = llm
        else:
            raise ValueError("At least one of learner, retriever, or llm must be provided")

    def fit(self, train_data, top_k: int = 5) -> 'LearnerPipeline':
        """
        Train the learner on the given training data.

        Args:
            train_data: Training data containing ontology information
            top_k (int): Number of top examples to retrieve (for retrieval-based learners)

        Returns:
            LearnerPipeline: Self for method chaining
        """
        self.learner.fit(train_data=train_data, task=self.task)
        return self

    def predict(self, test_data, limit: int = 10) -> List[Dict]:
        """
        Make predictions on test data and return results with metrics.

        Args:
            test_data: Test data containing ontology information
            limit (int): Maximum number of test examples to process

        Returns:
            List[Dict]: List of prediction results with metrics for each example
        """
        results = []
        if self.task == "term-typing":
            test_subset = test_data.term_typings[:limit]
            for typing in test_subset:
                term = typing.term
                ground_truth = typing.types
                predicted = self.learner.predict(term, task=self.task)
                metrics = calculate_term_typing_metrics(predicted, ground_truth)
                results.append({
                    'term': term,
                    'ground_truth': ground_truth,
                    'predicted': predicted,
                    **metrics
                })
        elif self.task == "taxonomy-discovery":
            test_subset = test_data.type_taxonomies.taxonomies[:limit]
            for relation in test_subset:
                parent = relation.parent
                child = relation.child
                ground_truth = "is-a"  # Always "is-a" for taxonomic relations
                predicted = self.learner.predict((parent, child), task=self.task)
                metrics = calculate_taxonomy_metrics(predicted, ground_truth)
                results.append({
                    'parent': parent,
                    'child': child,
                    'ground_truth': ground_truth,
                    'predicted': predicted[0],
                    **metrics
                })
        elif self.task == "non-taxonomic-re":
            test_subset = test_data.type_non_taxonomic_relations.non_taxonomies[:limit]
            for relation in test_subset:
                head = relation.head
                tail = relation.tail
                ground_truth = relation.relation
                predicted = self.learner.predict((head, tail), task=self.task)
                metrics = calculate_non_taxonomy_metrics(predicted, ground_truth)
                results.append({
                    'head': head,
                    'tail': tail,
                    'ground_truth': ground_truth,
                    'predicted': predicted[0],
                    **metrics
                })

        self.results = results
        return results

    def evaluate(self, output_dir: Optional[Union[str, Path]] = None) -> Dict:
        """
        Evaluate prediction results and generate aggregated metrics.

        Args:
            output_dir (Optional[Union[str, Path]]): Directory to save evaluation results and visualizations

        Returns:
            Dict: Aggregated metrics for the predictions
        """
        if not self.results:
            logger.warning("No prediction results available for evaluation")
            return {}

        self.metrics = aggregate_metrics(self.results, self.task)

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

    def fit_predict(self,
                    train_data,
                    test_data,
                    top_k: int = 5,
                    test_limit: int = 10) -> List[Dict]:
        """
        Run fit and predict steps in sequence (sklearn-style).

        Args:
            train_data: Training data containing ontology information
            test_data: Test data containing ontology information
            top_k (int): Number of top examples to retrieve (for retrieval-based learners)
            test_limit (int): Maximum number of test examples to process

        Returns:
            List[Dict]: List of prediction results with metrics for each example
        """
        self.fit(train_data, top_k)
        return self.predict(test_data, limit=test_limit)

    def fit_predict_evaluate(self,
                             train_data,
                             test_data,
                             top_k: int = 5,
                             test_limit: int = 10,
                             output_dir: Optional[Union[str, Path]] = None) -> Tuple[List[Dict], Dict]:
        """
        Run fit, predict and evaluate steps in one call.

        This is the most convenient method for running a complete pipeline workflow.

        Args:
            train_data: Training data containing ontology information
            test_data: Test data containing ontology information
            top_k (int): Number of top examples to retrieve (for retrieval-based learners)
            test_limit (int): Maximum number of test examples to process
            output_dir (Optional[Union[str, Path]]): Directory to save evaluation results

        Returns:
            Tuple[List[Dict], Dict]: Tuple of (prediction results, aggregated metrics)
        """
        self.fit(train_data, top_k)
        results = self.predict(test_data, limit=test_limit)
        metrics = self.evaluate(output_dir)
        return results, metrics
