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

from abc import ABC, abstractmethod
from typing import Any, List, Optional
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer

class AutoLearner(ABC):
    """
    Abstract base class for ontology learning models.

    This class defines the standard interface for all learning models in OntoLearner,
    including retrieval-based, LLM-based, and hybrid approaches. All concrete learner
    implementations must inherit from this class and implement the required methods.
    """

    def __init__(self, **kwargs: Any):
        """
        Initialize the learner with optional configuration parameters.

        Args:
            **kwargs: Arbitrary keyword arguments for learner configuration.
                     Specific parameters depend on the concrete implementation.
        """
        pass

    def load(self, **kwargs: Any):
        """
        Load pre-trained models, embeddings, or other required components.

        This method should initialize all necessary components for the learner,
        such as loading pre-trained language models, embedding models, or
        other resources required for the specific learning approach.

        Args:
            **kwargs: Configuration parameters for loading components.
                     Common parameters include model_id, token, device, etc.

        Raises:
            NotImplementedError: If not implemented by concrete class.
        """
        pass

    def fit(self, train_data: Any, task: str, ontologizer: bool=True):
        """
        Train the learner on the provided training data for a specific task.

        This method adapts the learner to the training data, which may involve
        indexing examples for retrieval, fine-tuning models, or preparing
        task-specific components.

        Args:
            train_data: Training data containing ontological information.
                       Format depends on the specific task and implementation.
            task: The ontology learning task to train for. Supported tasks:
                 - "term-typing": Predict semantic types for terms
                 - "taxonomy-discovery": Identify hierarchical relationships
                 - "non-taxonomy-discovery": Identify non-hierarchical relationships

        Raises:
            NotImplementedError: If not implemented by concrete class.
        """
        train_data = self._tasks_data_former(data=train_data, task=task, test=False) if ontologizer else train_data
        if task == 'term-typing':
            self._term_typing(train_data, test=False)
        elif task == 'taxonomy-discovery':
            self._taxonomy_discovery(train_data, test=False)
        elif task == 'non-taxonomic-re':
            self._non_taxonomic_re(train_data, test=False)
        else:
            raise ValueError(f"{task} is not a valid task.")


    def predict(self, eval_data: Any, task: str, ontologizer: bool=True) -> Any:
        """
        Make predictions on evaluation data for a specific task.

        This method applies the trained learner to new data and returns
        predictions in a format appropriate for the specified task.

        Args:
            eval_data: Evaluation data to make predictions on.
                      Format depends on the specific task and implementation.
            task: The ontology learning task to perform predictions for.
                 Must match the task used during training.

        Returns:
            Predictions in a format appropriate for the task:
            - term-typing: List of predicted types for each term
            - taxonomy-discovery: Boolean predictions for relationships
            - non-taxonomy-discovery: Predicted relation types

        Raises:
            NotImplementedError: If not implemented by concrete class.
        """
        eval_data = self._tasks_data_former(data=eval_data, task=task, test=False) if ontologizer else eval_data

        if task == 'term-typing':
            return self._term_typing(eval_data, test=True)
        elif task == 'taxonomy-discovery':
            return self._taxonomy_discovery(eval_data, test=True)
        elif task == 'non-taxonomic-re':
            return self._non_taxonomic_re(eval_data, test=True)
        else:
            raise ValueError(f"{task} is not a valid task.")

    def fit_predict(self, train_data: Any, eval_data: Any, task: str) -> Any:
        """
        Train the learner and make predictions in a single step.

        This convenience method combines the fit and predict operations,
        which is useful for workflows that don't require separate training
        and prediction phases.

        Args:
            train_data: Training data for the learner.
            eval_data: Evaluation data to make predictions on.
            task: The ontology learning task to perform.

        Returns:
            Predictions from the predict method.
        """
        self.fit(train_data, task)
        predictions = self.predict(eval_data, task)
        return predictions

    def _term_typing(self, data: Any, test: bool = False) -> Optional[Any]:
        pass

    def _taxonomy_discovery(self, data: Any, test: bool = False) -> Optional[Any]:
        pass

    def _non_taxonomic_re(self, data: Any, test: bool = False) -> Optional[Any]:
        pass

    def _tasks_data_former(self, data: Any, task: str, test: bool = False) -> Any:
        pass

class AutoLLM(ABC):
    """
    Abstract base class for Large Language Model components.

    This class defines the interface for LLM components used in ontology learning.
    It provides a standardized way to load and interact with various language models
    from different providers (Hugging Face, OpenAI, etc.).

    Attributes:
        model: The loaded language model instance.
        tokenizer: The tokenizer associated with the model.
    """

    def __init__(self, token: str="") -> None:
        """
        Initialize the LLM component.

        Sets up the basic structure with model and tokenizer attributes
        that will be populated when load() is called.
        """
        self.token = token
        self.model: Optional[Any] = None
        self.tokenizer: Optional[Any] = None


    def load(self, model_id: str) -> None:
        """
        Load a language model and its associated tokenizer.

        This method should initialize the model and tokenizer from the specified
        model identifier, handling authentication, device placement, and other
        configuration as needed.

        Args:
            model_id: Identifier for the model to load (e.g., Hugging Face model ID).
            **kwargs: Additional configuration parameters such as:
                     - token: Authentication token for gated models
                     - device: Target device for model placement
                     - torch_dtype: Data type for model weights

        Raises:
            NotImplementedError: If not implemented by concrete class.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_id, token=self.token)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype=torch.bfloat16,
            token=self.token
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


class AutoRetriever(ABC):
    """
    Abstract base class for retrieval components.

    This class defines the interface for retrieval components used in ontology learning.
    Retrievers are responsible for finding semantically similar examples from training
    data to provide context for language models or to make direct predictions.

    Attributes:
        model: The loaded retrieval/embedding model instance.
    """

    def __init__(self) -> None:
        """
        Initialize the retriever component.

        Sets up the basic structure with a model attribute that will be
        populated when load() is called.
        """
        self.model: Optional[Any] = None
        self.embedding_model = None
        self.documents = []
        self.embeddings = None

    def load(self, model_id: str) -> None:
        """
        Load a retrieval/embedding model.

        This method should initialize the embedding model from the specified
        model identifier, preparing it for encoding and similarity computation.

        Args:
            model_id: Identifier for the model to load (e.g., sentence-transformers model ID).
            **kwargs: Additional configuration parameters such as:
                     - device: Target device for model placement
                     - cache_folder: Directory for caching model files

        Raises:
            NotImplementedError: If not implemented by concrete class.
        """
        self.embedding_model = SentenceTransformer(model_id)

    def index(self, inputs: List[str]):
        """
        Index the provided inputs for efficient retrieval.

        This method processes and indexes the training examples to enable
        fast similarity search during retrieval operations.

        Args:
            inputs: List of examples to index. Format depends on the specific
                   retrieval implementation and task requirements.

        Raises:
            NotImplementedError: If not implemented by concrete class.
        """
        self.documents = inputs
        self.embeddings = self.embedding_model.encode(inputs, convert_to_tensor=True)

    def retrieve(self, query: Any, top_k: int = 5) -> List[Any]:
        """
        Retrieve the most similar examples for a given query.

        This method finds and returns the top-k most similar examples from
        the indexed training data based on semantic similarity.

        Args:
            query: Query example to find similar items for.
                  Format depends on the specific task and implementation.
            top_k: Number of most similar examples to retrieve.

        Returns:
            List of the top-k most similar examples from the indexed data.

        Raises:
            NotImplementedError: If not implemented by concrete class.
        """

        if self.embeddings is None:
            return []

        query_embedding = self.embedding_model.encode(query, convert_to_tensor=True)

        if query_embedding.shape[-1] != self.embeddings.shape[-1]:
            raise ValueError(
                f"Embedding dimension mismatch: query embedding dim={query_embedding.shape[-1]}, "
                f"document embedding dim={self.embeddings.shape[-1]}"
            )
        query_embedding = self.embedding_model.encode(query, convert_to_tensor=True)  # shape [10, 384]

        # Average across the sequence
        # query_embedding = query_embedding.mean(dim=0)  # shape [384]
        #
        # query_expanded = query_embedding.unsqueeze(0).expand(self.embeddings.size(0), -1)
        similarities = F.cosine_similarity(query_embedding, self.embeddings, dim=1)
        top_k = min(top_k, len(self.documents))
        indices = similarities.topk(top_k).indices.tolist()
        #
        # top_k = min(top_k, len(self.documents))
        #
        # indices = similarities.topk(top_k).indices.tolist()

        return [self.documents[i] for i in indices]


class AutoPrompt(ABC):
    """
    Abstract base class for prompt formatting components.

    This class defines the interface for prompt templates used in ontology learning
    tasks. Prompts are responsible for formatting input data and context into
    appropriate text prompts for language models.

    Attributes:
        prompt_template: The template string used for formatting prompts.
    """

    def __init__(self, prompt_template: str) -> None:
        """
        Initialize the prompt component with a template.

        Args:
            prompt_template: Template string with placeholders for dynamic content.
                           Should use Python string formatting syntax (e.g., {term}, {context}).
        """
        self.prompt_template = prompt_template

    @abstractmethod
    def format(self, **kwargs: Any) -> str:
        """
        Format the prompt template with the provided arguments.

        This method takes the template and fills in the placeholders with
        the provided keyword arguments to create a complete prompt.

        Args:
            **kwargs: Keyword arguments to fill template placeholders.
                     Common arguments include:
                     - term: Term to predict types for
                     - context: Retrieved examples or additional context
                     - parent/child: Concepts for taxonomy discovery
                     - head/tail: Entities for relation discovery

        Returns:
            Formatted prompt string ready for language model input.

        Raises:
            NotImplementedError: If not implemented by concrete class.
        """
        pass
