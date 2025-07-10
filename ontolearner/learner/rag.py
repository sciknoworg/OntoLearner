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

import warnings
from typing import Any
from ..base import AutoLearner


class AutoRAGLearner(AutoLearner):
    def __init__(self,
                 retriever: Any,
                 llm: Any):
        super().__init__()
        self.retriever = retriever
        self.llm = llm
        self._is_term_typing_fit = False

    def load(self,
             retriever_id: str = 'sentence-transformers/all-MiniLM-L6-v2',
             llm_id: str="mistralai/Mistral-7B-Instruct-v0.1"):
        self.retriever.load(retriever_id)
        self.llm.load(llm_id)

    def _term_typing(self, data: Any, test: bool = False) -> Any:
        """
        during training: data = ["type-1", .... ],
        during testing: data = ['term-1', ...]
        """
        task = 'term-typing'
        if test:
            if self._is_term_typing_fit:
                retriever_predictions = self.retriever.predict(data, task=task, ontologizer=False)
                prompting = self.llm.prompting(task=task)
                dataset = [{"term": retriever_prediction['term'], "type": type,
                            "prompt": prompting.format(term=retriever_prediction['term'], type=type)}
                           for retriever_prediction in retriever_predictions for type in retriever_prediction['types']]
                return self.llm._term_typing_predict(dataset=dataset)
            else:
                raise RuntimeError("Term typing model must be fit before prediction.")
        else:
            self.retriever.fit(data, task=task, ontologizer=False)
            self._is_term_typing_fit = True

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Any:
        """
        during training: data = ['type-1', ...],
        during testing (same data): data= ['type-1', ...]
        """
        task = 'taxonomy-discovery'
        if test:
            retriever_predictions = self.retriever.predict(data, task=task, ontologizer=False)
            prompting = self.llm.prompting(task=task)
            dataset = [{"parent": retriever_prediction['parent'], "child": retriever_prediction['child'],
                        "prompt": prompting.format(parent=retriever_prediction['parent'], child=retriever_prediction['child'])}
                       for retriever_prediction in retriever_predictions]
            return self.llm._taxonomy_discovery_predict(dataset=dataset)
        else:
            warnings.warn("No requirement for fiting the taxonomy discovery model, the predict module will use the input data to do the fit as well.")

    def _non_taxonomic_re(self, data: Any, test: bool = False) -> Any:
        """
        during training: data = ['type-1', ...],
        during testing: {'types': [...], 'relations': [... ]}
        """
        task = "non-taxonomic-re"
        if test:
            retriever_predictions = self.retriever.predict(data, task=task, ontologizer=False)
            prompting = self.llm.prompting(task='non-taxonomic-re')
            dataset = [{"head": retriever_prediction['head'],
                        "tail": retriever_prediction['tail'],
                        "relation": retriever_prediction['relation'],
                        "prompt": prompting.format(head=retriever_prediction['head'],
                                                   tail=retriever_prediction['tail'],
                                                   relation=retriever_prediction['relation'])}
                       for retriever_prediction in retriever_predictions]
            return self.llm._non_taxonomic_re_predict(dataset=dataset)
        else:
            warnings.warn("No requirement for fiting the non-taxonomic-re model, the predict module will use the input data to do the fit as well.")
