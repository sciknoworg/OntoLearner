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
    """
    Large Language Model component for ontology learning tasks.

    This class provides a concrete implementation of the AutoLLM interface using
    Hugging Face Transformers. It supports loading and using various instruction-tuned
    language models for ontology learning tasks, with optimized configurations for
    structured text generation.

    Attributes:
        token: Hugging Face authentication token for gated models.
        model: Loaded causal language model instance.
        tokenizer: Associated tokenizer for text processing.
    """

    def __init__(self, token: str = "") -> None:
        """
        Initialize the LLM component.

        Args:
            token: Hugging Face authentication token. Required for gated models
                  like Llama or other restricted models.
        """
        super().__init__()
        self.token = token

    def load(self, model_id: str = "mistralai/Mistral-7B-Instruct-v0.1", token: Optional[str] = None) -> None:
        """
        Load a language model and tokenizer from Hugging Face.

        This method downloads and initializes the specified model with optimized
        settings for ontology learning tasks. It configures automatic device
        placement, memory-efficient data types, and proper tokenization.

        Args:
            model_id: Hugging Face model identifier. Should be an instruction-tuned
                     model for best results with ontology learning tasks.
            token: Authentication token for this specific load operation.
                  If None, uses the token provided during initialization.

        Raises:
            OSError: If model cannot be downloaded or loaded.
            ValueError: If authentication fails for gated models.
        """
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
        """
        Generate text responses for the given input prompts.

        This method processes a batch of input prompts and generates corresponding
        text responses using the loaded language model. It uses optimized settings
        for consistent, high-quality generation suitable for ontology learning tasks.

        Generation Settings:
        - Temperature: 0.1 (low randomness for consistent outputs)
        - Padding: Automatic handling for batch processing
        - Device placement: Automatic GPU/CPU selection

        Args:
            inputs: List of input prompts to generate responses for.
                   Each prompt should be a complete, well-formatted string.
            max_new_tokens: Maximum number of new tokens to generate per input.
                          Shorter values encourage concise responses.

        Returns:
            List of generated text responses, one for each input prompt.
            Responses include the original input plus generated continuation.
        """
        encoded_inputs = self.tokenizer(inputs, return_tensors="pt",
                                        padding=True).to(self.model.device)
        outputs = self.model.generate(
            **encoded_inputs,
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id,
            temperature=0.1
        )
        return [self.tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
