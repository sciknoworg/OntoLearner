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


class AutoLearner(ABC):
    """
    Abstract base class for ontology learning models.

    This class defines the standard interface for all learning models in OntoLearner,
    including retrieval-based, LLM-based, and hybrid approaches. All concrete learner
    implementations must inherit from this class and implement the required methods.
    """

    def __init__(self, **kwargs: Any) -> None:
        """
        Initialize the learner with optional configuration parameters.

        Args:
            **kwargs: Arbitrary keyword arguments for learner configuration.
                     Specific parameters depend on the concrete implementation.
        """
        pass

    @abstractmethod
    def load(self, **kwargs: Any) -> None:
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

    @abstractmethod
    def fit(self, train_data: Any, task: str) -> None:
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
        pass

    @abstractmethod
    def predict(self, eval_data: Any, task: str) -> Any:
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
        pass

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

    def __init__(self) -> None:
        """
        Initialize the LLM component.

        Sets up the basic structure with model and tokenizer attributes
        that will be populated when load() is called.
        """
        self.model: Optional[Any] = None
        self.tokenizer: Optional[Any] = None

    @abstractmethod
    def load(self, model_id: str, **kwargs: Any) -> None:
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
        pass

    @abstractmethod
    def generate(self, inputs: List[str], **kwargs: Any) -> List[str]:
        """
        Generate text responses for the given input prompts.

        This method takes a list of input prompts and generates corresponding
        text responses using the loaded language model.

        Args:
            inputs: List of input prompts/texts to generate responses for.
            **kwargs: Generation parameters such as:
                     - max_new_tokens: Maximum number of tokens to generate
                     - temperature: Sampling temperature for generation
                     - top_k: Top-k sampling parameter

        Returns:
            List of generated text responses, one for each input prompt.

        Raises:
            NotImplementedError: If not implemented by concrete class.
        """
        pass


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

    @abstractmethod
    def load(self, model_id: str, **kwargs: Any) -> None:
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
        pass

    @abstractmethod
    def index(self, inputs: List[Any]) -> None:
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
        pass

    @abstractmethod
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
        pass


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
