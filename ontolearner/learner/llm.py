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

from ..base import AutoLLM
from typing import List, Optional
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class AutoLearnerLLM(AutoLLM):
    def __init__(self, token: str = ""):
        super().__init__()
        self.token = token

    def load(self, model_id: str = "mistralai/Mistral-7B-Instruct-v0.1", token: Optional[str] = None):
        auth_token = token if token is not None else self.token

        self.tokenizer = AutoTokenizer.from_pretrained(model_id, token=auth_token)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype=torch.bfloat16,
            token=auth_token
        )

    def generate(self, inputs: List[str], max_new_tokens: int = 50) -> List[str]:
        encoded_inputs = self.tokenizer(inputs, return_tensors="pt",
                                        padding=True).to(self.model.device)
        outputs = self.model.generate(
            **encoded_inputs,
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id,
            temperature=0.1
        )
        return [self.tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
