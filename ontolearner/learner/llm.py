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
import torch.nn.functional as F
from transformers import Mistral3ForConditionalGeneration
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

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

    @torch.no_grad()
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

    @torch.no_grad()
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


class LogitMistralLLM(AutoLLM):
    label_dict = {
        "yes": ["yes", "true", " yes", "Yes"],
        "no": ["no", "false", " no", "No"]
    }

    def _get_label_token_ids(self):
        label_token_ids = {}

        for label, words in self.label_dict.items():
            ids = []
            for w in words:
                messages = [{"role": "user", "content": [{"type": "text", "text": w}]}]
                tokenized = self.tokenizer.encode_chat_completion(ChatCompletionRequest(messages=messages))
                token_ids = tokenized.tokens[2:-1]
                ids.append(token_ids)
            label_token_ids[label] = ids
        return label_token_ids

    def load(self, model_id: str) -> None:
        self.tokenizer = MistralTokenizer.from_hf_hub(model_id)
        self.tokenizer.padding_side = 'left'
        device_map = "cpu" if self.device == "cpu" else "balanced"
        self.model = Mistral3ForConditionalGeneration.from_pretrained(
            model_id,
            device_map=device_map,
            torch_dtype=torch.bfloat16,
            token=self.token
        )
        self.pad_token_id = self.model.generation_config.eos_token_id
        self.label_token_ids = self._get_label_token_ids()

    @torch.no_grad()
    def generate(self, inputs: List[str], max_new_tokens: int = 1) -> List[str]:
        tokenized_list = []
        for prompt in inputs:
            messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
            req = ChatCompletionRequest(messages=messages)
            tokenized = self.tokenizer.encode_chat_completion(req)
            tokenized_list.append(tokenized.tokens)

        max_len = max(len(t) for t in tokenized_list)
        input_ids, attention_masks = [], []
        for tokens in tokenized_list:
            pad_len = max_len - len(tokens)
            input_ids.append(tokens + [self.pad_token_id] * pad_len)
            attention_masks.append([1] * len(tokens) + [0] * pad_len)

        input_ids = torch.tensor(input_ids).to(self.model.device)
        attention_masks = torch.tensor(attention_masks).to(self.model.device)

        outputs = self.model(input_ids=input_ids, attention_mask=attention_masks)
        # logits: [batch, seq_len, vocab]
        logits = outputs.logits
        # next-token prediction
        last_logits = logits[:, -1, :]
        probs = torch.softmax(last_logits, dim=-1)
        predictions = []
        for i in range(probs.size(0)):
            label_scores = {}
            for label, token_id_lists in self.label_token_ids.items():
                score = 0.0
                for token_ids in token_id_lists:
                    # single-token in practice, but safe
                    score += probs[i, token_ids[0]].item()
                label_scores[label] = score
            predictions.append(max(label_scores, key=label_scores.get))
        return predictions


class QwenInstructAutoLLM(AutoLLM):

    def generate(self, inputs: List[str], max_new_tokens: int = 50) -> List[str]:
        messages = [[{"role": "user", "content": prompt + " Please show your final response with 'answer': 'label'."}]
                    for prompt in inputs]

        texts = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

        encoded_inputs = self.tokenizer(texts, return_tensors="pt", padding="max_length", truncation=True,
                                        max_length=256).to(self.model.device)

        generated_ids = self.model.generate(**encoded_inputs,
                                            max_new_tokens=max_new_tokens,
                                            use_cache=False,
                                            pad_token_id=self.tokenizer.pad_token_id,
                                            eos_token_id=self.tokenizer.eos_token_id)
        decoded_outputs = []
        for i in range(len(generated_ids)):
            prompt_len = encoded_inputs.attention_mask[i].sum().item()
            output_ids = generated_ids[i][prompt_len:].tolist()
            output_content = self.tokenizer.decode(output_ids, skip_special_tokens=True).strip()
            decoded_outputs.append(output_content)
        return self.label_mapper.predict(decoded_outputs)


class QwenThinkingLLM(AutoLLM):

    @torch.no_grad()
    def generate(self, inputs: List[str], max_new_tokens: int = 50) -> List[str]:
        messages = [[{"role": "user", "content": prompt + " Please show your final response with 'answer': 'label'."}]
                    for prompt in inputs]
        texts = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        encoded_inputs = self.tokenizer(texts, return_tensors="pt", padding=True).to(self.model.device)
        generated_ids = self.model.generate(**encoded_inputs, max_new_tokens=max_new_tokens)
        decoded_outputs = []
        for i in range(len(generated_ids)):
            prompt_len = encoded_inputs.attention_mask[i].sum().item()
            output_ids = generated_ids[i][prompt_len:].tolist()
            try:
                end = len(output_ids) - output_ids[::-1].index(151668)
                thinking_ids = output_ids[:end]
            except ValueError:
                thinking_ids = output_ids
            thinking_content = self.tokenizer.decode(thinking_ids, skip_special_tokens=True).strip()
            decoded_outputs.append(thinking_content)
        return self.label_mapper.predict(decoded_outputs)


class LogitAutoLLM(AutoLLM):
    def _get_label_token_ids(self):
        label_token_ids = {}
        for label, words in self.label_mapper.label_dict.items():
            ids = []
            for w in words:
                token_ids = self.tokenizer.encode(w, add_special_tokens=False)
                ids.append(token_ids)
            label_token_ids[label] = ids
        return label_token_ids

    def load(self, model_id: str) -> None:
        super().load(model_id)
        self.label_token_ids = self._get_label_token_ids()

    @torch.no_grad()
    def generate(self, inputs: List[str], max_new_tokens: int = 1) -> List[str]:
        encoded = self.tokenizer(inputs, return_tensors="pt", truncation=True, padding=True).to(self.model.device)
        outputs = self.model(**encoded)
        logits = outputs.logits # logits: [batch, seq_len, vocab]
        last_logits = logits[:, -1, :]  # [batch, vocab] # we only care about the NEXT token prediction
        probs = F.softmax(last_logits, dim=-1)
        predictions = []
        for i in range(probs.size(0)):
            label_scores = {}
            for label, token_id_lists in self.label_token_ids.items():
                score = 0.0
                for token_ids in token_id_lists:
                    if len(token_ids) == 1:
                        score += probs[i, token_ids[0]].item()
                    else:
                        score += probs[i, token_ids[0]].item() # multi-token fallback (rare but safe)
                label_scores[label] = score
            predictions.append(max(label_scores, key=label_scores.get))
        return predictions


class LogitQuantAutoLLM(AutoLLM):
    label_dict = {
        "yes": ["yes", "true", " yes", "Yes"],
        "no": ["no", "false", " no", "No"]
    }

    def _get_label_token_ids(self):
        label_token_ids = {}

        for label, words in self.label_dict.items():
            ids = []
            for w in words:
                token_ids = self.tokenizer.encode(
                    w,
                    add_special_tokens=False
                )
                # usually single-token, but be safe
                ids.append(token_ids)
            label_token_ids[label] = ids

        return label_token_ids

    def load(self, model_id: str) -> None:

        self.tokenizer = AutoTokenizer.from_pretrained(model_id, padding_side='left', token=self.token)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        if self.device == "cpu":
            # device_map = "cpu"
            self.model = AutoModelForCausalLM.from_pretrained(
                model_id,
                # device_map=device_map,
                torch_dtype=torch.bfloat16,
                token=self.token
            )
        else:
            device_map = "balanced"
            # self.model = AutoModelForCausalLM.from_pretrained(
            #     model_id,
            #     device_map=device_map,
            #     torch_dtype=torch.bfloat16,
            #     token=self.token
            # )
            bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True
            )
            self.model = AutoModelForCausalLM.from_pretrained(
                model_id,
                quantization_config=bnb_config,
                device_map=device_map,
                token=self.token,
                # trust_remote_code=True,
                # attn_implementation="flash_attention_2"
            )
        self.label_token_ids = self._get_label_token_ids()

    @torch.no_grad()
    def generate(self, inputs: List[str], max_new_tokens: int = 1) -> List[str]:
        encoded = self.tokenizer(
            inputs,
            return_tensors="pt",
            max_length=256,
            truncation=True,
            padding=True
        ).to(self.model.device)

        outputs = self.model(**encoded)

        # logits: [batch, seq_len, vocab]
        logits = outputs.logits

        # we only care about the NEXT token prediction
        last_logits = logits[:, -1, :]  # [batch, vocab]

        probs = F.softmax(last_logits, dim=-1)

        predictions = []

        for i in range(probs.size(0)):
            label_scores = {}

            for label, token_id_lists in self.label_token_ids.items():
                score = 0.0
                for token_ids in token_id_lists:
                    if len(token_ids) == 1:
                        score += probs[i, token_ids[0]].item()
                    else:
                        # multi-token fallback (rare but safe)
                        score += probs[i, token_ids[0]].item()
                label_scores[label] = score

            predictions.append(max(label_scores, key=label_scores.get))
        return predictions
