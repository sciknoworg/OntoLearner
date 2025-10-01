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
from typing import Any, List
import warnings
from tqdm import tqdm
from torch.utils.data import DataLoader
import torch
from transformers import Mistral3ForConditionalGeneration
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

class AutoLLMLearner(AutoLearner):

    def __init__(self,
                 prompting,
                 label_mapper,
                 llm: AutoLLM = AutoLLM,
                 token: str = "",
                 max_new_tokens: int = 5,
                 batch_size: int = 10,
                 device='cpu') -> None:
        super().__init__()
        self.llm = llm(token=token, label_mapper=label_mapper, device=device)
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


class FalconLLM(AutoLLM):

    def generate(self, inputs: List[str], max_new_tokens: int = 50) -> List[str]:
        encoded_inputs = self.tokenizer(inputs,
                                        return_tensors="pt",
                                        padding=True,
                                        truncation=True).to(self.model.device)
        input_ids = encoded_inputs["input_ids"]
        input_length = input_ids.shape[1]
        outputs = self.model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id
        )
        generated_tokens = outputs[:, input_length:]
        decoded_outputs = [self.tokenizer.decode(g, skip_special_tokens=True).strip() for g in generated_tokens]
        return self.label_mapper.predict(decoded_outputs)

class MistralLLM(AutoLLM):

    def load(self, model_id: str) -> None:
        self.tokenizer = MistralTokenizer.from_hf_hub(model_id)
        if self.device == "cpu":
            device_map = "cpu"
        else:
            device_map = "balanced"
        self.model = Mistral3ForConditionalGeneration.from_pretrained(
            model_id,
            device_map=device_map,
            torch_dtype=torch.bfloat16,
            token=self.token
        )
        if not hasattr(self.tokenizer, "pad_token_id") or self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token_id = self.model.generation_config.eos_token_id
        self.label_mapper.fit()

    def generate(self, inputs: List[str], max_new_tokens: int = 50) -> List[str]:
        tokenized_list = []
        for prompt in inputs:
            messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
            tokenized = self.tokenizer.encode_chat_completion(ChatCompletionRequest(messages=messages))
            tokenized_list.append(tokenized.tokens)
        max_len = max(len(tokens) for tokens in tokenized_list)
        input_ids, attention_masks = [], []
        for tokens in tokenized_list:
            pad_length = max_len - len(tokens)
            input_ids.append(tokens + [self.tokenizer.pad_token_id] * pad_length)
            attention_masks.append([1] * len(tokens) + [0] * pad_length)

        input_ids = torch.tensor(input_ids).to(self.model.device)
        attention_masks = torch.tensor(attention_masks).to(self.model.device)

        outputs =self.model.generate(
            input_ids=input_ids,
            attention_mask=attention_masks,
            eos_token_id=self.model.generation_config.eos_token_id,
            pad_token_id=self.tokenizer.pad_token_id,
            max_new_tokens=max_new_tokens,
        )
        decoded_outputs = []
        for i, tokens in enumerate(outputs):
            output_text = self.tokenizer.decode(tokens[len(tokenized_list[i]):])
            decoded_outputs.append(output_text)
        return self.label_mapper.predict(decoded_outputs)
