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

from abc import ABC
from typing import Any, List, Dict
from openai import OpenAI
import time
from tqdm import tqdm

from ...base import AutoRetriever
from ...utils import load_json


class LLMAugmenterGenerator(ABC):
    """
    A generator class responsible for creating augmented query candidates using LLMs
    such as GPT-4 and GPT-3.5. This class provides augmentation support for
    three ontology-learning tasks:

    - term-typing
    - taxonomy-discovery
    - non-taxonomic relation extraction

    For taxonomy discovery, it invokes a function-calling LLM that returns
    candidate parent classes for each query term.

    Attributes:
        client (OpenAI): OpenAI API client used for LLM inference.
        model_id (str): The LLM model identifier.
        term_typing_function (list): Function call schema for term typing (currently unused).
        taxonomy_discovery_function (list): Function call schema for taxonomy discovery.
        non_taxonomic_re_function (list): Function call schema for non-taxonomic relation extraction.
        top_n_candidate (int): Number of augmented candidates to generate per query.
        term_typing_prompt (str): Prompt template used for term typing tasks.
        taxonomy_discovery_prompt (str): Prompt template used for taxonomy discovery.
        non_taxonomic_re_prompt (str): Prompt template for non-taxonomic RE.
    """

    def __init__(self, model_id: str = 'gpt-4.1-mini', token: str = '', top_n_candidate: int = 5) -> None:
        """
        Initialize the LLM augmenter generator.

        Args:
            model_id (str): Name of the OpenAI model to use.
            token (str): API key for authentication.
            top_n_candidate (int): Number of generated candidate parents per query.
        """
        self.client = OpenAI(api_key=token)

        self.model_id = model_id

        self.term_typing_function = []
        self.taxonomy_discovery_function = [
            {
                "name": "discover_taxonomy_parents",
                "description": "Given a specific type or class (the query), identify potential parent classes that form valid hierarchical (is-a) relationships within a taxonomy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_parents": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A ranked list of candidate parent classes representing higher-level categories."
                        }
                    },
                    "required": ["candidate_parents"]
                }
            }
        ]

        self.non_taxonomic_re_function = []
        self.top_n_candidate = top_n_candidate

        self.term_typing_prompt = ""
        self.taxonomy_discovery_prompt = (
            "Given a type (or class) {query}, generate a list of the top {top_n_candidate} candidate classes "
            "that can form hierarchical (is-a) relationships, where each of these classes is a parent of {query}."
        )
        self.non_taxonomic_re_prompt = ""

    def get_config(self) -> Dict[str, Any]:
        """
        Get augmenter configuration metadata.

        Returns:
            dict: Dictionary containing the augmentation configuration.
        """
        return {
            "top_n_candidate": self.top_n_candidate,
            "augmenter_model": self.model_id
        }

    def generate(self, conversation, function):
        """
        Call an LLM to produce augmented candidates using function-calling.

        Args:
            conversation (list): Dialogue messages to send to the LLM.
            function (list): Function schemas supplied to the model.

        Returns:
            list[str]: A list of top-k generated candidates.
        """
        while True:
            try:
                completion = self.client.chat.completions.create(
                    model=self.model_id,
                    messages=conversation,
                    functions=function
                )
                inference = eval(completion.choices[0].message.function_call.arguments)['candidate_parents'][:self.top_n_candidate]
                assert len(inference) == self.top_n_candidate
                break
            except Exception:
                print("sleep for 5 seconds")
                time.sleep(5)

        return inference

    def tasks_data_former(self, data: Any, task: str) -> List[str] | Dict[str, List[str]]:
        """
        Convert raw dataset input into query lists depending on the ontology-learning task.

        Args:
            data (Any): Input dataset object.
            task (str): One of {'term-typing', 'taxonomy-discovery', 'non-taxonomic-re'}.

        Returns:
            List[str] or Dict[str, List[str]]: Formatted query inputs.
        """
        formatted_data = []
        if task == "term-typing":
            for typing in data.term_typings:
                formatted_data.append(typing.term)
            formatted_data = list(set(formatted_data))

        if task == "taxonomy-discovery":
            for taxonomic_pairs in data.type_taxonomies.taxonomies:
                formatted_data.append(taxonomic_pairs.parent)
                formatted_data.append(taxonomic_pairs.child)
            formatted_data = list(set(formatted_data))

        if task == "non-taxonomic-re":
            non_taxonomic_types = []
            non_taxonomic_res = []
            for triplet in data.type_non_taxonomic_relations.non_taxonomies:
                non_taxonomic_types.extend([triplet.head, triplet.tail])
                non_taxonomic_res.append(triplet.relation)
            formatted_data = {"types": list(set(non_taxonomic_types)), "relations": list(set(non_taxonomic_res))}

        return formatted_data

    def _augment(self, query, conversations, function):
        """
        Internal helper to generate augmented candidates for a batch of queries.

        Args:
            query (list[str]): Input query terms.
            conversations (list): LLM conversation blocks for each query.
            function (list): Function-calling schemas.

        Returns:
            dict[str, list[str]]: Mapping from query → list of augmented candidates.
        """
        results = {}
        for qu, conversation in tqdm(zip(query, conversations)):
            results[qu] = self.generate(conversation=conversation, function=function)
        return results

    def augment_term_typing(self, query: List[str]) -> List[str]:
        """
        Augment term-typing queries.

        Currently a passthrough: no augmentation is performed.

        Args:
            query (list[str]): Query terms.

        Returns:
            list[str]: Unmodified query terms.
        """
        return query

    def augment_non_taxonomic_re(self, query: List[str]) -> List[str]:
        """
        Augment non-taxonomic relation extraction queries.

        Currently a passthrough.

        Args:
            query (list[str]): Query terms.

        Returns:
            list[str]: Unmodified query terms.
        """
        return query

    def augment_taxonomy_discovery(self, query: List[str]) -> Dict[str, List[str]]:
        """
        Generate augmented candidates for taxonomy discovery.

        Args:
            query (list[str]): List of type/class names to augment.

        Returns:
            dict[str, list[str]]: Mapping of original query → list of candidate parents.
        """
        conversations = []
        for qu in query:
            prompt = self.taxonomy_discovery_prompt.format(query=qu, top_n_candidate=self.top_n_candidate)
            conversation = [
                {"role": "system", "content": "Discover possible taxonomy parents."},
                {"role": "user", "content": prompt}
            ]
            conversations.append(conversation)

        return self._augment(query=query, conversations=conversations, function=self.taxonomy_discovery_function)

    def augment(self, data: Any, task: str):
        """
        Main entry point for all augmentation modes.

        Args:
            data (Any): Dataset object to format and augment.
            task (str): Task type.

        Returns:
            Any: Augmented output suitable for a retriever.

        Raises:
            ValueError: If an invalid task type is given.
        """
        data = self.tasks_data_former(data=data, task=task)
        if task == 'term-typing':
            return self.augment_term_typing(data)
        elif task == 'taxonomy-discovery':
            return self.augment_taxonomy_discovery(data)
        elif task == 'non-taxonomic-re':
            return self.augment_non_taxonomic_re(data)
        else:
            raise ValueError(f"{task} is not a valid task.")


class LLMAugmenter:
    """
    A lightweight augmenter that loads precomputed augmentation data from disk.

    Attributes:
        augments (dict): Loaded augmentation data.
        top_n_candidate (int): Number of augmentation candidates per query.
    """

    def __init__(self, path: str) -> None:
        """
        Initialize an augmenter that uses offline augmentation data.

        Args:
            path (str): Path to a JSON file containing saved augmentations.
        """
        self.augments = load_json(path)
        self.top_n_candidate = self.augments['config']['top_n_candidate']

    def transform(self, query: str, task: str) -> List[str]:
        """
        Retrieve the augmented versions of a query term for a specific task.

        Args:
            query (str): Input query term.
            task (str): Task identifier.

        Returns:
            list[str]: Augmented query candidates.
        """
        if task == 'taxonomy-discovery':
            return self.augments[task].get(query, [query])
        else:
            return [query]


class LLMAugmentedRetriever(AutoRetriever):
    """
    A retriever that enhances queries using LLM-based augmentation before retrieving documents.

    Supports special augmentation logic for taxonomy discovery where each input query
    is expanded into several augmented variants.

    Attributes:
        augmenter: An augmenter instance that provides transform() and top_n_candidate.
    """

    def __init__(self) -> None:
        """
        Initialize the augmented retriever with no augmenter attached.
        """
        super().__init__()
        self.augmenter = None

    def set_augmenter(self, augmenter):
        """
        Attach an augmenter instance.

        Args:
            augmenter: An object providing `transform(query, task)` and `top_n_candidate`.
        """
        self.augmenter = augmenter

    def retrieve(self, query: List[str], top_k: int = 5, batch_size: int = -1, task: str = None) -> List[List[str]]:
        """
        Retrieve documents for a batch of queries, optionally using query augmentation.

        Args:
            query (list[str]): List of input query terms.
            top_k (int): Number of documents to retrieve.
            batch_size (int): Batch size for retrieval.
            task (str): Optional task identifier that determines augmentation behavior.

        Returns:
            list[list[str]]: A list of document lists, one per input query.
        """
        parent_retrieve = super(LLMAugmentedRetriever, self).retrieve

        if task == 'taxonomy-discovery':
            query_sets = []
            for idx in range(self.augmenter.top_n_candidate):
                query_set = []
                for qu in query:
                    query_set.append(self.augmenter.transform(qu, task=task)[idx])
                query_sets.append(query_set)

            retrieves = [
                parent_retrieve(query=query_set, top_k=top_k, batch_size=batch_size)
                for query_set in query_sets
            ]

            results = []
            for qu_idx, qu in enumerate(query):
                qu_result = []
                for top_idx in range(self.augmenter.top_n_candidate):
                    qu_result += retrieves[top_idx][qu_idx]
                results.append(list(set(qu_result)))

            return results

        else:
            return parent_retrieve(query=query, top_k=top_k, batch_size=batch_size)
