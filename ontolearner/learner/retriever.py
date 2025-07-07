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

from ..base import AutoRetriever, AutoLearner
from typing import Any, Optional
import warnings

class AutoRetrieverLearner(AutoLearner):
    def __init__(self, base_retriever: Any = AutoRetriever(), top_k: int = 5):
        super().__init__()
        self.retriever = base_retriever
        self.top_k = top_k
        self._is_term_typing_fit = False
        self._is_taxonomy_discovery_fit = False

    def load(self, model_id: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.retriever.load(model_id=model_id)

    def _retriever_fit(self, data: Any):
        if isinstance(data, list) and all(isinstance(item, str) for item in data):
            self.retriever.index(inputs=data)
        else:
            raise TypeError("Expected a list of strings for retriever at term-typing task.")

    def _retriever_predict(self, data:Any, top_k: int) -> Any:
        if isinstance(data, list):
            return self.retriever.retrieve(query=data, top_k=top_k)
        if isinstance(data, str):
            return self.retriever.retrieve(query=[data], top_k=top_k)
        raise TypeError(f"Unsupported data type {type(data)}. You should pass a List[str] or a str.")

    def _term_typing(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        during training: data = ["type-1", .... ],
        during testing: data = ['term-1', ...]
        """
        if test:
            if self._is_term_typing_fit:
                types = self._retriever_predict(data=data, top_k=self.top_k)
                return [{"term": term, "types": type} for term, type in zip(data, types)]
            else:
                raise RuntimeError("Term typing model must be fit before prediction.")
        else:
            self._retriever_fit(data=data)
            self._is_term_typing_fit = True

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        during training: data = ['type-1', ...],
        during testing (same data): data= ['type-1', ...]
        """
        if test:
            self._retriever_fit(data=data)
            candidates_lst =  self._retriever_predict(data=data, top_k=self.top_k + 1)
            taxonomic_pairs = [{"parent": query, "child": candidate}
                               for query, candidates in zip(data, candidates_lst)
                               for candidate in candidates if candidate != query]
            return taxonomic_pairs
        else:
            warnings.warn("No requirement for fiting the taxonomy discovery model, the predict module will use the input data to do the fit as well.")

    def _non_taxonomic_re(self, data: Any, test: bool = False) -> Optional[Any]:
        """
        during training: data = ['type-1', ...],
        during testing: {'types': [...], 'relations': [... ]}
        """
        if test:
            # print(data)
            if 'types' not in data or 'relations' not in data:
                raise ValueError("The non-taxonomic re predict should take {'types': [...], 'relations': [... ]}")
            if len(data['types']) == 0:
                warnings.warn("No `types` avaliable to do the non-taxonomic re-prediction.")
                return None
            self._retriever_fit(data=data['types'])
            candidates_lst = self._retriever_predict(data=data['types'], top_k=self.top_k + 1)
            taxonomic_pairs = []
            taxonomic_pairs_query = []
            for query, candidates in zip(data['types'], candidates_lst):
                for candidate in candidates:
                    if candidate != query:
                        taxonomic_pairs.append((query, candidate))
                        taxonomic_pairs_query.append(f"Head: {query} \n Tail: {candidate}")
            self._retriever_fit(data=data['relations'])
            candidate_relations_lst = self._retriever_predict(data=taxonomic_pairs_query, top_k=self.top_k)
            non_taxonomic_re = [{"head": head, "tail": tail, "relation": relation}
                                for (head, tail), candidate_relations in zip(taxonomic_pairs, candidate_relations_lst)
                                for relation in candidate_relations]
            return non_taxonomic_re
        else:
            warnings.warn("No requirement for fiting the non-taxonomic RE model, the predict module will use the input data to do the fit as well..")
