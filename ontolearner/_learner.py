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
import time
from typing import Dict, Optional, Any

from .base import AutoPrompt
from .evaluation import evaluation_report
from .learner import (AutoRetrieverLearner,
                      AutoLLMLearner,
                      AutoRAGLearner,
                      StandardizedPrompting,
                      LabelMapper)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LearnerPipeline:
    """
    Unified pipeline for ontology learning using LLMs, retrievers, or RAG-based models.
    Supports end-to-end training, prediction, and evaluation in a scikit-learn-like interface.
    """

    def __init__(self,
                 retriever: Optional[Any] = None,
                 llm: Optional[Any] = None,
                 retriever_id: Optional[str] = None,
                 llm_id: Optional[str] = None,
                 prompting: Optional[AutoPrompt] = StandardizedPrompting,
                 label_mapper: Optional[LabelMapper] = LabelMapper(),
                 hf_token: Optional[str] = None,
                 ontologizer_data: bool = True,
                 top_k: int = 5,
                 batch_size: int = 10,
                 device: str = 'cpu',
                 max_new_tokens: int=10):
        """
        Initialize the pipeline for a specific ontology learning task.

        Args:
            task: One of ["term-typing", "taxonomy-discovery", "non-taxonomic-re"]
            prompting: Optional prompting strategy (defaults to StandardizedPrompting)
            retriever: Pre-initialized retriever learner (if any)
            llm: Pre-initialized LLM learner (if any)
            retriever_id: HF model ID for retriever (if not provided explicitly)
            llm_id: HF model ID for LLM (if not provided explicitly)
            hf_token: Hugging Face token (for gated LLM access)
            ontologizer_data: If True, uses Ontologizer-style datasets
            top_k: Number of top examples to retrieve for RAG or Retriever
        """
        self.ontologizer_data = ontologizer_data
        # Instantiate retriever
        if retriever is None and retriever_id is not None:
            retriever = AutoRetrieverLearner(top_k=top_k) # ToDO consider also `base_retriever`
            self.retriever_id = retriever_id
        retriever_id = retriever_id if retriever_id is not None else 'sentence-transformers/all-MiniLM-L6-v2'
        # Instantiate LLM
        if llm is None and llm_id is not None:
            llm = AutoLLMLearner(prompting=prompting,
                                 label_mapper=label_mapper,
                                 token=hf_token,
                                 device=device,
                                 batch_size=batch_size,
                                 max_new_tokens=max_new_tokens)
        llm_id = llm_id if llm_id is not None else 'Qwen/Qwen2.5-0.5B-Instruct'
        # Determine pipeline strategy
        if retriever and llm:
            self.learner = AutoRAGLearner(retriever=retriever, llm=llm)
            self.learner.load(retriever_id=retriever_id, llm_id=llm_id)
            self.model_type = "rag"
        elif retriever:
            self.learner = retriever
            self.learner.load(model_id=retriever_id)
            self.model_type = "retriever"
        elif llm:
            self.learner = llm
            self.learner.load(model_id=llm_id)
            self.model_type = "llm"
        else:
            raise ValueError("At least one of [retriever, llm, retriever_id, llm_id] must be specified.")

    def __call__(self,
                 train_data: Any,
                 task: str,
                 test_data: Any = None,
                 evaluate: bool=False,
                 ontologizer_data: bool=True) -> Dict[str, Any]:
        run_report = {"model": self.model_type}
        start_time = time.time()
        self.learner.fit(train_data, task=task, ontologizer=ontologizer_data)
        predictions = None
        if test_data:
            predictions = self.learner.predict(test_data, task=task, ontologizer=ontologizer_data)
            run_report['predictions'] = predictions
        if evaluate:
            if not test_data:
                raise ValueError("Testing data is required for evaluation.")
            else:
                if predictions:
                    y_true = self.learner.tasks_ground_truth_former(data=test_data, task=task)
                    metrics = evaluation_report(y_true=y_true, y_pred=predictions, task=task)
                    run_report['metrics'] = metrics
                else:
                    raise ValueError("Predictions is required for evaluation.")
        run_report['elapsed_time'] = time.time() - start_time
        return run_report
