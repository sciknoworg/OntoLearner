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

from ..base import AutoLLM, AutoLearner
from typing import Any
import warnings
from tqdm import tqdm
from torch.utils.data import DataLoader


class AutoLLMLearner(AutoLearner):

    def __init__(self,
                 prompting,
                 label_mapper,
                 token: str = "",
                 max_new_tokens: int = 5,
                 batch_size: int = 10,
                 device='cpu') -> None:
        super().__init__()
        self.llm = AutoLLM(token=token, label_mapper=label_mapper, device=device)
        self.prompting = prompting
        self.batch_size = batch_size
        self.max_new_tokens = max_new_tokens
        self._is_term_typing_fit = False

    def load(self, model_id: str = "mistralai/Mistral-7B-Instruct-v0.1", **kwargs: Any):
        self.llm.load(model_id=model_id)

    def _term_typing_predict(self, dataset):
        dataloader = DataLoader(dataset, batch_size=self.batch_size, shuffle=False)
        predictions = {}
        for batch in tqdm(dataloader):
            prediction = self.llm.generate(inputs=batch['prompt'], max_new_tokens=self.max_new_tokens)
            for term, type, predict in zip(batch['term'], batch['type'], prediction):
                if term not in predictions:
                    predictions[term] = []
                if predict == 'yes':
                    predictions[term].append(type)
        predicts = [{"term": term, "types": types} for term, types in predictions.items()]
        return predicts

    def _term_typing(self, data: Any, test: bool = False) -> Any:
        """
        during training: data = ["type-1", .... ],
        during testing: data = ['term-1', ...]
        """
        if not isinstance(data, list) and not all(isinstance(item, str) for item in data):
            raise TypeError("Expected a list of strings (types) for llm  at term-typing task.")
        if test:
            if self._is_term_typing_fit:
                prompting = self.prompting(task='term-typing')
                dataset = [{"term": term, "type": type, "prompt": prompting.format(term=term, type=type)}
                           for term in data for type in self.candidate_types]
                return self._term_typing_predict(dataset=dataset)
            else:
                raise RuntimeError("Term typing model must be fit before prediction.")
        else:
            self.candidate_types = data
            self._is_term_typing_fit = True

    def _taxonomy_discovery_predict(self, dataset):
        dataloader = DataLoader(dataset, batch_size=self.batch_size, shuffle=False)
        predictions = []
        for batch in tqdm(dataloader):
            prediction = self.llm.generate(inputs=batch['prompt'], max_new_tokens=self.max_new_tokens)
            predictions.extend({"parent": parent, "child": child}
                                for parent, child, predict in zip(batch['parent'], batch['child'], prediction)
                                if predict == 'yes')
        return predictions

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Any:
        """
        during training: data = ['type-1', ...],
        during testing (same data): data= ['type-1', ...]
        """
        if test:
            if not isinstance(data, list) and not all(isinstance(item, str) for item in data):
                raise TypeError("Expected a list of strings (types) for llm  at term-typing task.")
            prompting = self.prompting(task='taxonomy-discovery')
            dataset = [{"parent": type_i, "child": type_j, "prompt": prompting.format(parent=type_i, child=type_j)}
                       for idx, type_i in enumerate(data) for jdx, type_j in enumerate(data) if idx < jdx]
            return self._taxonomy_discovery_predict(dataset=dataset)
        else:
            warnings.warn("No requirement for fiting the taxonomy-discovery model, the predict module will use the input data to do the 'is-a' relationship detection")

    def _non_taxonomic_re_predict(self, dataset):
        dataloader = DataLoader(dataset, batch_size=self.batch_size, shuffle=False)
        predictions = []
        for batch in tqdm(dataloader):
            prediction = self.llm.generate(inputs=batch['prompt'], max_new_tokens=self.max_new_tokens)
            predictions.extend({"head": head, "tail": tail, "relation": relation}
                                for head, tail, relation, predict in
                                zip(batch['head'], batch['tail'], batch['relation'], prediction)
                                if predict == 'yes')
        return predictions

    def _non_taxonomic_re(self, data: Any, test: bool = False) -> Any:
        """
        during training: data = ['type-1', ...],
        during testing: {'types': [...], 'relations': [... ]}
        """
        if test:
            if 'types' not in data or 'relations' not in data:
                raise ValueError("The non-taxonomic re predict should take {'types': [...], 'relations': [... ]}")
            if len(data['types']) == 0:
                warnings.warn("No `types` avaliable to do the non-taxonomic re-prediction.")
                return None
            # paring and finding paris that can have a relationship
            prompting = self.prompting(task='taxonomy-discovery')
            dataset = [{"parent": type_i, "child": type_j, "prompt": prompting.format(parent=type_i, child=type_j)}
                       for idx, type_i in enumerate(data['types']) for jdx, type_j in enumerate(data['types']) if idx < jdx]
            dataloader = DataLoader(dataset, batch_size=self.batch_size, shuffle=False)
            predicts_lst = []
            for batch in tqdm(dataloader):
                prediction = self.llm.generate(inputs=batch['prompt'], max_new_tokens=self.max_new_tokens)
                predicts_lst.extend((parent, child)
                                    for parent, child, predict in zip(batch['parent'], batch['child'], prediction)
                                    if predict == 'yes')
            # finding relationships
            prompting = self.prompting(task='non-taxonomic-re')
            dataset = [{"head": head, "tail": tail, "relation": relation,
                        "prompt": prompting.format(head=head, tail=tail, relation=relation)}
                       for head, tail in predicts_lst for relation in data['relations']]
            return self._non_taxonomic_re_predict(dataset=dataset)
        else:
            warnings.warn("No requirement for fiting the non-taxonomic-re model, the predict module will use the input data to do the task.")
