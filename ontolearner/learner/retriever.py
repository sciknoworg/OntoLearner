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
    def __init__(self, top_k: int = 5):
        super().__init__()
        self.retriever = AutoRetriever()
        self.top_k = top_k
        self._is_term_typing_fit = False
        self._is_taxonomy_discovery_fit = False

    def load(self, model_id: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.retriever.load(model_id=model_id)

    def _tasks_data_former(self, data: Any, task: str, test: bool = False) -> Any:
        formatted_data = []
        if task == "term-typing":
            for typing in data.term_typings:
                if test:
                    formatted_data.append(typing.term)
                else:
                    formatted_data += typing.types
            formatted_data = list(set(formatted_data))
        if task == "taxonomy-discovery":
            for taxonomic_pairs in data.type_taxonomies.taxonomies:
                formatted_data.append(taxonomic_pairs.parent)
                formatted_data.append(taxonomic_pairs.child)
            formatted_data = list(set(formatted_data))
        if task == "non-taxonomic-re":
            non_taxonomic_types = []
            non_taxonomic_res = []
            for non_taxonomic_triplets in data.type_non_taxonomic_relations.non_taxonomies:
                non_taxonomic_types.append(non_taxonomic_triplets.head)
                non_taxonomic_types.append(non_taxonomic_triplets.tail)
                non_taxonomic_res.append(non_taxonomic_triplets.relation)
            non_taxonomic_types = list(set(non_taxonomic_types))
            non_taxonomic_res = list(set(non_taxonomic_res))
            formatted_data = {"types": non_taxonomic_types, "relations": non_taxonomic_res}
        return formatted_data

    def _retriever_fit(self, data: Any):
        if isinstance(data, list) and all(isinstance(item, str) for item in data):
            self.retriever.index(inputs=data)
        else:
            raise TypeError("Expected a list of strings for for retriever at term-typing task.")

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
                term_typings = []
                for term, type in zip(data, types):
                    term_typings.append({"term": term, "types": type})
                return term_typings
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
            if self._is_taxonomy_discovery_fit:
                candidates_lst =  self._retriever_predict(data=data, top_k=self.top_k + 1)
                taxonomic_pairs = []
                for query, candidates in zip(data, candidates_lst):
                    for candidate in candidates:
                        if candidate != query:
                            taxonomic_pairs.append({"parent": query, "child":candidate})
                return taxonomic_pairs
            else:
                raise RuntimeError("Taxonomy discovery model must be fit before prediction.")
        else:
            self._retriever_fit(data=data)
            self._is_taxonomy_discovery_fit = True

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
            non_taxonomic_re = []
            for (head, tail), candidate_relations in zip(taxonomic_pairs, candidate_relations_lst):
                for relation in candidate_relations:
                    non_taxonomic_re.append({"head": head, "tail": tail, "relation": relation})
            return non_taxonomic_re
        else:
            warnings.warn("No requirement for fiting the non-taxonomic RE model, the predict module will use the input data to do the fit as well..")
