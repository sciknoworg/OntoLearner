from ..base import AutoLLM
from typing import List
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class AutoLearnerLLM(AutoLLM):
    def __init__(self):
        super().__init__()

    def load(self, model_id: str = "mistralai/Mistral-7B-Instruct-v0.1"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype=torch.bfloat16
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
