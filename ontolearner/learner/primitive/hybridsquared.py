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

import ast
import gc
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

from tqdm import tqdm

from ...base import PrimitiveOntologyLearner

class _HybridAISquaredLearner(PrimitiveOntologyLearner):
    """Shared prompts, model loading, generation, parsing and cleaning of the HybridAI-Squared learners."""

    TARGET = "extended-primitive-ontology-triples"
    INITIAL_KEY = "initial-primitive-ontology-triples"
    ZS_BASE_MODEL = "Qwen/Qwen3-30B-A3B"
    SFT_BASE_MODEL = "Qwen/Qwen3-14B"
    Triple = List[str]
    # The submission's prompt templates, verbatim.
    TEMPLATES = {
        "direct_predict": """Analyze the provided **TITLE** and **CONTENT** to identify relations from **RELATIONS** among the given **TERMS** and **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Terms and Types**
   - Enumerate all provided **TERMS** and **TYPES**. Either list may be empty.

2. **Identify Relations**
   - Review the list of provided **RELATIONS**. For each relation:
     - Write a brief, one-line description.
     - Specify its domain and range (e.g., TERM–TERM, TERM–TYPE, TYPE–TYPE, etc.).
   - For each **TERM** and **TYPE**:
     - Identify possible new relations using only the provided **RELATIONS**.
     - Do not create new **TERMS** or **TYPES**.
     - There may be multiple applicable relations, or none, for each item.
     - Not all relation types may be relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TERMS**
{terms}

**TYPES**
{types}

**RELATIONS**
["is-a", "instance-of", "is defined by", "equivalent class", "disjoint with",, "type", "tree view", "exact match", "part_of", "database_cross_reference",, "has part", "same as", "develops_from", "see also", "is_conjugate_acid_of",, "is_conjugate_base_of", "disjoint-with", "is-defined-by", "regulates",, "range", "broader", "is tautomer of", "overlaps", "equivalent-class",, "ro_0002229", "has quality", "holds", "has name", "has prepared surface",, "close match", "is about", "derives from", "term replaced by", "domain",, "ro_0002220"]

**OUTPUT STRUCTURE**
[
    ["subject", "relation", "object"],
    ["subject", "relation", "object"],
    ["subject", "relation", "object"],
]

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_is-a": """Analyze the provided **TITLE** and **CONTENT** to identify 'is-a' relations among the given **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Types**
   - Enumerate all provided **TYPES**. The list may be empty.

2. **Identify 'is-a' Relations**
   - Identify 'is-a' relations only between different **TYPES** from the provided list. An 'is-a' relation designates one **TYPE** as a subclass of another **TYPE**. Do not identify any 'is-a' relations if the list contains zero or one **TYPE**.
   - Do not create new **TYPES**.
   - There may be multiple applicable 'is-a' relations, or none, relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified 'is-a' relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TYPES**
{types}

**OUTPUT STRUCTURE**
[
    ["subject", "is-a", "object"],
    ["subject", "is-a", "object"],
    ["subject", "is-a", "object"],
]

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_instance-of": """Analyze the provided **TITLE** and **CONTENT** to identify 'instance-of' relations among the given **TERMS** and **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Terms and Types**
   - Enumerate all provided **TERMS** and **TYPES**. Either list may be empty.

2. **Identify 'instance-of' Relations**
   - An 'instance-of' relation may only be established if the subject is a **TERM** from the provided **TERMS** list and the object is a **TYPE** from the provided **TYPES** list. The 'instance-of' relation designates a **TERM** as an instance of the specified **TYPE**. If the **TERMS** list is empty, do not create any new 'instance-of' relations.
   - For each **TERM** and **TYPE**:
     - Identify possible new 'instance-of' relations.
     - Do not create new **TERMS** or **TYPES**.
     - There may be multiple applicable 'instance-of' relations, or none, relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TERMS**
{terms}

**TYPES**
{types}

**OUTPUT STRUCTURE**
[
    ["subject", "instance-of", "object"],
    ["subject", "instance-of", "object"],
    ["subject", "instance-of", "object"],
]

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_is_defined_by": """Analyze the provided **TITLE** and **CONTENT** to identify 'is defined by' relations among the given **TERMS** and **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Terms and Types**
   - Enumerate all provided **TERMS** and **TYPES**. Either list may be empty.

2. **Identify 'is defined by' Relations**S
   - An 'is defined by' relation links a **TERM** or a **TYPE** from the provided list of **TERMS** and **TYPES** to another **TERM** or **TYPE** that provides its definition.
   - For each **TERM** and **TYPE**:
     - Identify possible new 'is defined by' relations.
     - Do not create new **TERMS** or **TYPES**.
     - There may be multiple applicable 'is defined by' relations, or none, relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TERMS**
{terms}

**TYPES**
{types}

**OUTPUT STRUCTURE**
[
    ["subject", "is defined by", "object"],
    ["subject", "is defined by", "object"],
    ["subject", "is defined by", "object"],
]

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_equivalent_class": """Annalyze the provided **TITLE** and **CONTENT** to identify 'equivalent class' relations among the given **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Types**
   - Enumerate all provided **TYPES**. The list may be empty.

2. **Identify 'equivalent class' Relations**
   - Identify 'equivalent class' relations only between different **TYPES** from the provided list. An 'equivalent class' relation designates two **TYPES** to have the same class extension i.e the same set of individuals. Do not identify any 'equivalent class' relations if the list contains zero or one **TYPE**.
   - Do not create new **TYPES**.
   - There may be multiple applicable 'equivalent class' relations, or none, relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified 'equivalent class' relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TYPES**
{types}

**OUTPUT STRUCTURE**
[
    ["subject", "equivalent class", "object"],
    ["subject", "equivalent class", "object"],
    ["subject", "equivalent class", "object"],
]

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_disjoint_with": """Analyze the provided **TITLE** and **CONTENT** to identify 'disjoint with' relations among the given **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Types**
   - Enumerate all provided **TYPES**. The list may be empty.

2. **Identify 'disjoint with' Relations**
   - Identify 'disjoint with' relations only between different **TYPES** from the provided list. A 'disjoint with' relation asserts that two **TYPES** have no individuals in common. Do not identify any 'disjoint with' relations if the list contains zero or one **TYPE**.
   - Do not create new **TYPES**.
   - There may be multiple applicable 'disjoint with' relations, or none, relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified 'disjoint with' relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TYPES**
{types}

**OUTPUT STRUCTURE**
[
    ["subject", "disjoint with", "object"],
    ["subject", "disjoint with", "object"],
    ["subject", "disjoint with", "object"],
]

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_type": """Analyze the provided **TITLE** and **CONTENT** to identify 'type' relations among the given **TERMS** and **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Terms and Types**
   - Enumerate all provided **TERMS** and **TYPES**. Either list may be empty.

2. **Identify 'type' Relations**
   - A 'type' relation may only be established between a **TERM** or a **TYPE** from the provided **TERMS** and **TYPES** lists and, a **TYPE** from the provided **TYPES** list. The 'type' relation designates a **TERM** or a **TYPE** as an instance of the specified **TYPE**. Do not identify any 'type' relations if the list contains zero or one **TYPE**.
   - For each **TERM** and **TYPE**:
     - Identify possible new 'type' relations.
     - Do not create new **TERMS** or **TYPES**.
     - There may be multiple applicable 'type' relations, or none, relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TERMS**
{terms}

**TYPES**
{types}

**OUTPUT STRUCTURE**
[
    ["subject", "type", "object"],
    ["subject", "type", "object"],
    ["subject", "type", "object"],
]

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_rest": """Analyze the provided **TITLE** and **CONTENT** to identify relations from **RELATIONS** among the given **TERMS** and **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Terms and Types**
   - Enumerate all provided **TERMS** and **TYPES**. Either list may be empty.

2. **Identify Relations**
   - Review the list of provided **RELATIONS**. For each relation:
     - Write a brief, one-line description.
     - Specify its domain and range (e.g., TERM–TERM, TERM–TYPE, TYPE–TYPE, etc.).
   - For each **TERM** and **TYPE**:
     - Identify possible new relations using only the provided **RELATIONS**.
     - Do not create new **TERMS** or **TYPES**.
     - There may be multiple applicable relations, or none, for each item.
     - Not all relation types may be relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TERMS**
{terms}

**TYPES**
{types}

**RELATIONS**
["tree view", "exact match", "part_of", "database_cross_reference",, "has part", "same as", "develops_from", "see also", "is_conjugate_acid_of",, "is_conjugate_base_of", "disjoint-with", "is-defined-by", "regulates",, "range", "broader", "is tautomer of", "overlaps", "equivalent-class",, "ro_0002229", "has quality", "holds", "has name", "has prepared surface",, "close match", "is about", "derives from", "term replaced by", "domain",, "ro_0002220"]

**OUTPUT STRUCTURE**
[
    ["subject", "relation", "object"],
    ["subject", "relation", "object"],
    ["subject", "relation", "object"],
]

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_rest_all": """Analyze the provided **TITLE** and **CONTENT** to identify relations from **RELATIONS** among the given **TERMS** and **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Terms and Types**
   - Enumerate all provided **TERMS** and **TYPES**. Either list may be empty.

2. **Identify Relations**
   - Review the list of provided **RELATIONS**. For each relation:
     - Write a brief, one-line description.
     - Specify its domain and range (e.g., TERM–TERM, TERM–TYPE, TYPE–TYPE, etc.).
   - For each **TERM** and **TYPE**:
     - Identify possible new relations using only the provided **RELATIONS**.
     - Do not create new **TERMS** or **TYPES**.
     - There may be multiple applicable relations, or none, for each item.
     - Not all relation types may be relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TERMS**
{terms}

**TYPES**
{types}

**RELATIONS**
["is defined by", "equivalent class", "disjoint with", "type", "tree view", "exact match", "part_of", "database_cross_reference",, "has part", "same as", "develops_from", "see also", "is_conjugate_acid_of",, "is_conjugate_base_of", "disjoint-with", "is-defined-by", "regulates",, "range", "broader", "is tautomer of", "overlaps", "equivalent-class",, "ro_0002229", "has quality", "holds", "has name", "has prepared surface",, "close match", "is about", "derives from", "term replaced by", "domain",, "ro_0002220"]

**OUTPUT STRUCTURE**
[
    ["subject", "relation", "object"],
    ["subject", "relation", "object"],
    ["subject", "relation", "object"],
]

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_chain_is-a": """Analyze the provided **TITLE** and **CONTENT** to identify 'is-a' relations among the given **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Types**
   - Enumerate all provided **TYPES**. The list may be empty.

2. **Identify 'is-a' Relations**
   - Identify 'is-a' relations only between different **TYPES** from the provided list. An 'is-a' relation designates one **TYPE** as a subclass of another **TYPE**. Do not identify any 'is-a' relations if the list contains zero or one **TYPE**.
   - Do not create new **TYPES**.
   - Exclude any relations already listed in **EXISTING TRIPLES**.
   - There may be multiple applicable 'is-a' relations, or none, relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified 'is-a' relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TYPES**
{types}

**OUTPUT STRUCTURE**
[
    ["subject", "is-a", "object"],
    ["subject", "is-a", "object"],
    ["subject", "is-a", "object"],
]

**EXISTING_TRIPLES**
{existing_triples}

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_chain_instance-of": """Analyze the provided **TITLE** and **CONTENT** to identify 'instance-of' relations among the given **TERMS** and **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Terms and Types**
   - Enumerate all provided **TERMS** and **TYPES**. Either list may be empty.

2. **Identify 'instance-of' Relations**
   - An 'instance-of' relation may only be established if the subject is a **TERM** from the provided **TERMS** list and the object is a **TYPE** from the provided **TYPES** list. The 'instance-of' relation designates a **TERM** as an instance of the specified **TYPE**. If the **TERMS** list is empty, do not create any new 'instance-of' relations.
   - For each **TERM** and **TYPE**:
     - Identify possible new 'instance-of' relations.
     - Do not create new **TERMS** or **TYPES**.
     - Exclude any relations already listed in **EXISTING TRIPLES**.
     - There may be multiple applicable 'instance-of' relations, or none, relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TERMS**
{terms}

**TYPES**
{types}

**OUTPUT STRUCTURE**
[
    ["subject", "instance-of", "object"],
    ["subject", "instance-of", "object"],
    ["subject", "instance-of", "object"],
]

**EXISTING TRIPLES**
{existing_triples}

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "per_relation_chain_rest_all": """Analyze the provided **TITLE** and **CONTENT** to identify relations from **RELATIONS** among the given **TERMS** and **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Terms and Types**
   - Enumerate all provided **TERMS** and **TYPES**. Either list may be empty.

2. **Identify Relations**
   - Review the list of provided **RELATIONS**. For each relation:
     - Write a brief, one-line description.
     - Specify its domain and range (e.g., TERM–TERM, TERM–TYPE, TYPE–TYPE, etc.).
   - For each **TERM** and **TYPE**:
     - Identify possible new relations using only the provided **RELATIONS**.
     - Do not create new **TERMS** or **TYPES**.
     - Exclude any relations already listed in **EXISTING TRIPLES**.
     - There may be multiple applicable relations, or none, for each item.
     - Not all relation types may be relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**TERMS**
{terms}

**TYPES**
{types}

**RELATIONS**
["is defined by", "equivalent class", "disjoint with",, "type", "tree view", "exact match", "part_of", "database_cross_reference",, "has part", "same as", "develops_from", "see also", "is_conjugate_acid_of",, "is_conjugate_base_of", "disjoint-with", "is-defined-by", "regulates",, "range", "broader", "is tautomer of", "overlaps", "equivalent-class",, "ro_0002229", "has quality", "holds", "has name", "has prepared surface",, "close match", "is about", "derives from", "term replaced by", "domain",, "ro_0002220"]

**OUTPUT STRUCTURE**
[
    ["subject", "relation", "object"],
    ["subject", "relation", "object"],
    ["subject", "relation", "object"],
]

**EXISTING TRIPLES**
{existing_triples}

**TITLE**
{title}

**CONTENT**
{content}

Respond only with the Python list of new relations as specified.
""",
        "finetune_system": """Analyze the provided **TITLE** and **CONTENT** to identify relations from **RELATIONS** among the given **TERMS** and **TYPES**. Follow the steps below explicitly:

**INSTRUCTIONS**

1. **List Terms and Types**
   - Enumerate all provided **TERMS** and **TYPES**. Either list may be empty.

2. **Identify Relations**
   - Review the list of provided **RELATIONS**. For each relation:
     - Write a brief, one-line description.
     - Specify its domain and range (e.g., TERM–TERM, TERM–TYPE, TYPE–TYPE, etc.).
   - For each **TERM** and **TYPE**:
     - Identify possible new relations using only the provided **RELATIONS**.
     - Do not create new **TERMS** or **TYPES**.
     - Exclude any relations already listed in **EXISTING TRIPLES**.
     - There may be multiple applicable relations, or none, for each item.
     - Not all relation types may be relevant to the **TITLE** and **CONTENT**.

3. **Generate Output**
   - Present only the newly identified relations as a valid Python list, following the **OUTPUT STRUCTURE**.

**OUTPUT STRUCTURE**
[
    ["subject", "relation", "object"],
    ["subject", "relation", "object"],
    ["subject", "relation", "object"],
]
""",
        "finetune_input": """**TERMS**
{terms}

**TYPES**
{types}

**RELATIONS**
["is-a", "instance-of", "is defined by", "equivalent class", "disjoint with",, "type", "tree view", "exact match", "part_of", "database_cross_reference",, "has part", "same as", "develops_from", "see also", "is_conjugate_acid_of",, "is_conjugate_base_of", "disjoint-with", "is-defined-by", "regulates",, "range", "broader", "is tautomer of", "overlaps", "equivalent-class",, "ro_0002229", "has quality", "holds", "has name", "has prepared surface",, "close match", "is about", "derives from", "term replaced by", "domain",, "ro_0002220"]

**EXISTING TRIPLES**
{existing_triples}

**TITLE**
{title}

**CONTENT**
{content}
""",
    }

    # Relation categories of the per-relation and chained prompts.
    PER_RELATION_CATEGORIES = {
        3: ["is-a", "instance-of", "rest_all"],
        7: ["is-a", "instance-of", "is_defined_by", "equivalent_class", "disjoint_with", "type", "rest"],
    }
    CHAIN_CATEGORIES = ["is-a", "instance-of", "rest_all"]

    # A relation (key) makes the listed relations redundant for the same pair.
    RELATION_PRECEDENCE = {
        "is-a": [
            "is defined by",
            "is-defined-by",
            "type",
            "equivalent class",
            "equivalent-class",
            "broader",
        ],
        "instance-of": [
            "broader",
        ],
    }
    SELF_RELATION_EXCLUDED = ["is defined by", "is-defined-by"]
    AVAILABLE_FILTERS = ("duplicates", "existing_triples", "self_relation", "relation_precedence")
    DEFAULT_FILTERS = ("existing_triples", "relation_precedence")

    def __init__(
        self,
        model_id: str,
        device: str = "cuda",
        max_new_tokens: int = 20000,
        temperature: float = 0.1,
        top_p: Optional[float] = None,
        top_k: Optional[int] = None,
        enable_thinking: bool = True,
        load_in_4bit: bool = False,
        filters: Sequence[str] = DEFAULT_FILTERS,
    ) -> None:
        """
        Initialize the learner.

        Args:
            model_id: Hugging Face model identifier or local path.
            device: Device for inference (``"cuda"`` or ``"cpu"``).
            max_new_tokens: Maximum number of generated tokens, reasoning included.
            temperature: Sampling temperature; 0 decodes greedily.
            top_p: Optional nucleus sampling threshold.
            top_k: Optional top-k sampling threshold.
            enable_thinking: Let Qwen3 reason before answering.
            load_in_4bit: Load the model in 4-bit (CUDA only).
            filters: Cleaning steps applied to the predicted triples.
        """
        super().__init__()
        unknown = set(filters) - set(self.AVAILABLE_FILTERS)
        if unknown:
            raise ValueError(f"Unknown filters {sorted(unknown)}; options are {list(self.AVAILABLE_FILTERS)}.")
        self.model_id = model_id
        self.device = device
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.enable_thinking = enable_thinking
        self.load_in_4bit = load_in_4bit
        self.filters = tuple(filters)

        self.tokenizer = None
        self.model = None
        self._loaded_model_id: Optional[str] = None

    def load(self, model_id: Optional[str] = None, **kwargs: Any) -> None:
        """
        Load the language model and tokenizer.

        Args:
            model_id: Optional Hugging Face model identifier or local path.
        """
        if model_id is not None:
            self.model_id = model_id
        if self.model is not None and self._loaded_model_id == self.model_id:
            return
        self.tokenizer, self.model = self._load_causal_lm(self.model_id)
        self._loaded_model_id = self.model_id

    def _load_causal_lm(self, model_id: str, adapter_path: Optional[Path] = None) -> Tuple[Any, Any]:
        """Load a tokenizer and causal language model, optionally in 4-bit and with a LoRA adapter."""
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

        tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True, padding_side="left")
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token

        kwargs: Dict[str, Any] = {"trust_remote_code": True}
        if self.device == "cpu":
            if self.load_in_4bit:
                raise ValueError("4-bit loading requires a CUDA device.")
            kwargs["torch_dtype"] = torch.float32
        else:
            dtype = torch.bfloat16 if torch.cuda.is_available() and torch.cuda.is_bf16_supported() else torch.float16
            kwargs.update(torch_dtype=dtype, device_map="auto")
            if self.load_in_4bit:
                kwargs["quantization_config"] = BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_compute_dtype=dtype,
                    bnb_4bit_use_double_quant=True,
                )
        model = AutoModelForCausalLM.from_pretrained(model_id, **kwargs)
        if adapter_path is not None:
            from peft import PeftModel

            model = PeftModel.from_pretrained(model, str(adapter_path))
        if self.device == "cpu":
            model = model.to("cpu")
        model.eval()
        return tokenizer, model

    def _ontology_construction(self, data: Any, test: bool = False) -> Optional[Any]:
        """Not supported: the submission addresses ontology expansion only."""
        raise NotImplementedError(
            f"{type(self).__name__} supports ontology expansion only (LLMs4OL 2026 Task B, Reuse)."
        )

    def _ontology_expansion(self, data: Any, test: bool = False) -> Optional[Any]:
        """Train on the labeled records, or predict the new triples of each test record."""
        samples = data if isinstance(data, list) else [data]
        if test:
            return self._predict(samples)
        self._fit(samples)
        return None

    def _fit(self, data: List[Dict[str, Any]]) -> None:
        """Do nothing: the zero-shot learners need no training."""

    def _predict(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict the new triples of every record."""
        raise NotImplementedError

    def _title_and_content(self, context: str) -> Tuple[str, str]:
        """Split a context into its title and content."""
        if "\n\n" not in context:
            return "", context.strip()
        title, content = context.split("\n\n", 1)
        title = title.replace("Title: ", "").strip()
        content = content.replace(" Content: \n", "").strip()
        return title, content

    def _fill(self, template_key: str, sample: Dict[str, Any], existing_triples: Any = None) -> str:
        """Fill a prompt template with a record's terms, types, existing triples, title and content."""
        title, content = self._title_and_content(sample["context"])
        return self.TEMPLATES[template_key].format(
            terms=sample.get("terms", []),
            types=sample.get("types", []),
            existing_triples=existing_triples if existing_triples is not None else sample.get(self.INITIAL_KEY, []),
            title=title,
            content=content,
        )

    def _chat_prompt(self, messages: List[Dict[str, str]]) -> str:
        """Format messages with the chat template, with Qwen3 reasoning if enabled."""
        kwargs = {"tokenize": False, "add_generation_prompt": True}
        try:
            return self.tokenizer.apply_chat_template(messages, enable_thinking=self.enable_thinking, **kwargs)
        except TypeError:
            return self.tokenizer.apply_chat_template(messages, **kwargs)

    def _generate(self, conversations: List[List[Dict[str, str]]], include_prompt: bool = False) -> List[str]:
        """Generate one answer per conversation, one conversation at a time."""
        import torch

        if self.model is None or self.tokenizer is None:
            raise RuntimeError("Call load() before predict().")
        generate_kwargs: Dict[str, Any] = {
            "max_new_tokens": self.max_new_tokens,
            "pad_token_id": self.tokenizer.pad_token_id,
        }
        if self.temperature and self.temperature > 0:
            generate_kwargs.update(do_sample=True, temperature=self.temperature)
            if self.top_p is not None:
                generate_kwargs["top_p"] = self.top_p
            if self.top_k is not None:
                generate_kwargs["top_k"] = self.top_k
        else:
            generate_kwargs.update(do_sample=False, temperature=None, top_p=None, top_k=None)

        responses: List[str] = []
        for messages in tqdm(conversations, desc=type(self).__name__):
            inputs = self.tokenizer([self._chat_prompt(messages)], return_tensors="pt").to(self.model.device)
            with torch.inference_mode():
                output = self.model.generate(**inputs, **generate_kwargs)[0]
            prompt_length = 0 if include_prompt else inputs["input_ids"].shape[1]
            responses.append(self.tokenizer.decode(output[prompt_length:], skip_special_tokens=True))
        return responses

    def _parse_response(self, response: str) -> Tuple[str, Any]:
        """Split a zero-shot answer into its reasoning and its list of triples."""
        response = response.replace("```", "")
        parts = response.rsplit("</think>", 1)
        reasoning = parts[0].replace("<think>", "").strip()
        if len(parts) == 1:
            prediction = []
        else:
            prediction = parts[1].strip()
            try:
                prediction = json.loads(prediction)
            except Exception:
                try:
                    check = ast.literal_eval(prediction)
                    if type(check) is list and check and type(check[0]) is list:
                        prediction = check
                    else:
                        prediction = prediction.split("],")
                        prediction = "[" + "],".join(prediction) + "]"
                        prediction = json.loads(prediction)
                except Exception:
                    check = re.split(
                        r"\*\*(Final )?(Correct |Corrected )?(Answer|Output):?\*\*",
                        prediction,
                    )
                    check = check[-1].split("[")[-1]
                    if (
                        "empty" in check
                        or "above" in check
                        or check.strip() == "]"
                        or check.replace(" ", "") == "[[]"
                    ):
                        prediction = "[]"
                    else:
                        prediction = "[[" + check
                    try:
                        prediction = json.loads(prediction)
                    except Exception:
                        prediction = []
            try:
                if prediction and type(prediction[0]) is not list:
                    prediction = [prediction]
            except (KeyError, TypeError):
                # A JSON object or number as the answer; the original script raises here.
                prediction = []
        return reasoning, prediction

    def _parse_finetune_response(self, response: str) -> Tuple[str, Any]:
        """Read the list of triples from a fine-tuned model's decoded prompt and answer."""
        response = response.replace("```", "")
        parts = response.rsplit("\nassistant", 1)
        reasoning = parts[0].replace("<think>", "").replace("</think>", "").strip()
        if len(parts) == 1:
            prediction = []
        else:
            prediction = parts[1].strip()
            first = prediction.index("[") if "[" in prediction else None
            if first is not None:
                prediction = prediction[first::]
                if prediction.startswith("[[["):
                    prediction = prediction[1::]
                if prediction.endswith("]]]"):
                    prediction = prediction[:-1]
                try:
                    prediction = prediction.replace('\\"', '"')
                    prediction = ast.literal_eval(prediction)
                    if not all([len(v) == 3 for v in prediction]):
                        prediction = [v for v in prediction if len(v) == 3]
                except Exception as exc:
                    prediction = []
            else:
                prediction = []
        return reasoning, prediction

    def _as_triples(self, prediction: Any) -> List[Triple]:
        """Keep the three-item rows of a parsed answer, as strings."""
        if not isinstance(prediction, (list, tuple)):
            return []
        return [[str(item) for item in row] for row in prediction
                if isinstance(row, (list, tuple)) and len(row) == 3]

    def _parse(self, response: str, finetuned: bool = False) -> Any:
        """Parse an answer into the predicted triples, before cleaning."""
        if finetuned:
            return self._parse_finetune_response(response)[1]
        if not self.enable_thinking and "</think>" not in response:
            # Without reasoning the answer has no </think>; add it so the answer is not discarded.
            response = "</think>" + response
        return self._parse_response(response)[1]

    def _drop_duplicates(self, triples: List[Triple]) -> List[Triple]:
        """Remove duplicate triples, keeping the order."""
        unique, seen = [], set()
        for triple in triples:
            if tuple(triple) not in seen:
                seen.add(tuple(triple))
                unique.append(triple)
        return unique

    def _drop_existing_triples(self, triples: List[Triple], existing: List[Any]) -> List[Triple]:
        # Compare as lists, as the submission did with triples loaded from JSON.
        """Drop triples that are already in the initial ontology."""
        existing = [list(t) if isinstance(t, tuple) else t for t in existing]
        return [t for t in triples if t not in existing]

    def _drop_self_relation(self, triples: List[Triple]) -> List[Triple]:
        """Drop ``is defined by`` triples and triples from an entity to itself."""
        return [t for t in triples if t[1] not in self.SELF_RELATION_EXCLUDED and t[0] != t[-1]]

    def _drop_relation_precedence(self, triples: List[Triple]) -> List[Triple]:
        """Drop ``type``, ``broader`` etc. where ``is-a`` or ``instance-of`` already links the same pair."""
        for subj, reln, obj in triples:
            for drop_relation in self.RELATION_PRECEDENCE.get(reln, []):
                if subj == obj and reln in ["is defined by", "is-defined-by"]:
                    continue
                if [subj, drop_relation, obj] in triples:
                    triples.remove([subj, drop_relation, obj])
        return triples

    def _clean(self, prediction: Any, existing: List[Any]) -> List[Triple]:
        """Apply the selected cleaning steps to the predicted triples."""
        triples = self._as_triples(prediction)
        if "duplicates" in self.filters:
            triples = self._drop_duplicates(triples)
        if "existing_triples" in self.filters:
            triples = self._drop_existing_triples(triples, existing)
        if "self_relation" in self.filters:
            triples = self._drop_self_relation(triples)
        if "relation_precedence" in self.filters:
            triples = self._drop_relation_precedence(triples)
        return triples

    def _finalise(self, sample: Dict[str, Any], cleaned: List[Triple]) -> Dict[str, Any]:
        """Return a record's prediction in the OntoLearner format."""
        return {"id": sample["id"], self.TARGET: cleaned}


class HybridAISquaredZSLearner(_HybridAISquaredLearner):
    """
    Zero-shot learner: one prompt per record predicts all new triples.

    The model sees the record's terms, types, title and text and the allowed relations; triples already in the
    initial ontology are removed afterwards. Score reported by the submission: 0.7357.
    """

    def __init__(
        self,
        model_id: str = _HybridAISquaredLearner.ZS_BASE_MODEL,
        device: str = "cuda",
        max_new_tokens: int = 20000,
        temperature: float = 0.1,
        enable_thinking: bool = True,
        load_in_4bit: bool = False,
        filters: Sequence[str] = _HybridAISquaredLearner.DEFAULT_FILTERS,
    ) -> None:
        """
        Initialize the learner.

        Args:
            model_id: Hugging Face model identifier (``Qwen/Qwen3-30B-A3B`` in the submission).
            device: Device for inference (``"cuda"`` or ``"cpu"``).
            max_new_tokens: Maximum number of generated tokens, reasoning included.
            temperature: Sampling temperature.
            enable_thinking: Let Qwen3 reason before answering.
            load_in_4bit: Load the model in 4-bit (CUDA only).
            filters: Cleaning steps applied to the predicted triples.
        """
        super().__init__(model_id=model_id, device=device, max_new_tokens=max_new_tokens, temperature=temperature,
                         enable_thinking=enable_thinking, load_in_4bit=load_in_4bit, filters=filters)

    def _predict(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict all new triples of each record with one prompt."""
        conversations = [[{"role": "user", "content": self._fill("direct_predict", sample)}] for sample in data]
        responses = self._generate(conversations)
        return [
            self._finalise(sample, self._clean(self._parse(response), sample.get(self.INITIAL_KEY, [])))
            for sample, response in zip(data, responses)
        ]


class HybridAISquaredPerRelationLearner(_HybridAISquaredLearner):
    """
    Zero-shot learner with one prompt per relation category.

    With 3 categories the prompts ask for ``is-a``, ``instance-of`` and the other relations; with 7, five
    relations get their own prompt. The predictions are combined, then cleaned. With ``chain=True`` each
    prompt also sees the earlier prompts' predictions. Score reported by the submission: 0.7113 (3 categories).
    """

    def __init__(
        self,
        model_id: str = _HybridAISquaredLearner.ZS_BASE_MODEL,
        categories: int = 3,
        chain: bool = False,
        device: str = "cuda",
        max_new_tokens: Optional[int] = None,
        temperature: float = 0.1,
        enable_thinking: bool = True,
        load_in_4bit: bool = False,
        filters: Sequence[str] = _HybridAISquaredLearner.DEFAULT_FILTERS,
        clean_combined: bool = True,
    ) -> None:
        """
        Initialize the learner.

        Args:
            model_id: Hugging Face model identifier (``Qwen/Qwen3-30B-A3B`` in the submission).
            categories: Number of relation categories, 3 or 7.
            chain: Chain the three category prompts.
            device: Device for inference (``"cuda"`` or ``"cpu"``).
            max_new_tokens: Maximum number of generated tokens per prompt (20000, or 25000 when chained).
            temperature: Sampling temperature.
            enable_thinking: Let Qwen3 reason before answering.
            load_in_4bit: Load the model in 4-bit (CUDA only).
            filters: Cleaning steps applied to the predicted triples.
            clean_combined: Clean the combined predictions; ``False`` cleans each category's predictions.
        """
        if categories not in self.PER_RELATION_CATEGORIES:
            raise ValueError(f"categories must be one of {sorted(self.PER_RELATION_CATEGORIES)}.")
        if chain and categories != 3:
            raise ValueError("Chained prompting is defined for the three-category setup only.")
        if max_new_tokens is None:
            max_new_tokens = 25000 if chain else 20000
        super().__init__(model_id=model_id, device=device, max_new_tokens=max_new_tokens, temperature=temperature,
                         enable_thinking=enable_thinking, load_in_4bit=load_in_4bit, filters=filters)
        self.categories = categories
        self.chain = chain
        self.clean_combined = clean_combined
        self.category_names = self.CHAIN_CATEGORIES if chain else self.PER_RELATION_CATEGORIES[categories]

    def _template_key(self, category: str) -> str:
        """Return the prompt template of a relation category."""
        return f"per_relation_chain_{category}" if self.chain else f"per_relation_{category}"

    def _predict(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Run each category's prompt and combine and clean the predictions of each record."""
        combined: List[List[Triple]] = [[] for _ in data]
        # Chained prompts see the initial triples plus each earlier prediction.
        context: List[List[Any]] = [list(sample.get(self.INITIAL_KEY, [])) for sample in data]
        for category in self.category_names:
            key = self._template_key(category)
            conversations = [
                [{"role": "user", "content": self._fill(key, sample, context[index] if self.chain else None)}]
                for index, sample in enumerate(data)
            ]
            responses = self._generate(conversations)
            for index, (sample, response) in enumerate(zip(data, responses)):
                prediction = self._parse(response)
                if self.chain:
                    context[index].append(prediction)
                if self.clean_combined:
                    combined[index].extend(self._as_triples(prediction))
                else:
                    combined[index].extend(self._clean(prediction, sample.get(self.INITIAL_KEY, [])))
        if self.clean_combined:
            combined = [self._clean(triples, sample.get(self.INITIAL_KEY, []))
                        for sample, triples in zip(data, combined)]
        return [self._finalise(sample, triples) for sample, triples in zip(data, combined)]


class HybridAISquaredSFTLearner(_HybridAISquaredLearner):
    """
    Fine-tuned learner: a LoRA adapter on Qwen3-14B predicts all new triples.

    ``fit`` fine-tunes a 4-bit LoRA adapter on the training records (CUDA only); ``predict`` generates with it
    and cleans the answers like the zero-shot learners. Score reported by the submission: 0.9013.
    """

    # Fine-tuning settings of the submission (4-bit LoRA).
    LORA_R = 32
    LORA_ALPHA = 32
    LORA_DROPOUT = 0.0
    TARGET_MODULES = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
    LEARNING_RATE = 2e-4
    NUM_TRAIN_EPOCHS = 1
    PER_DEVICE_TRAIN_BATCH_SIZE = 4
    GRADIENT_ACCUMULATION_STEPS = 4
    WARMUP_STEPS = 5
    WEIGHT_DECAY = 0.001
    EVAL_SAVE_STEPS = 20
    EARLY_STOPPING_PATIENCE = 5
    MAX_SEQ_LENGTH = 20000
    SPLIT_SEED = 3047
    TRAIN_SEED = 3407

    def __init__(
        self,
        model_id: str = _HybridAISquaredLearner.SFT_BASE_MODEL,
        device: str = "cuda",
        adapter_path: Optional[str] = None,
        output_dir: str = "./results/hybridaisquared",
        eval_size: float = 0.25,
        max_new_tokens: int = 20000,
        temperature: float = 0.6,
        top_p: float = 0.95,
        top_k: int = 20,
        enable_thinking: bool = True,
        filters: Sequence[str] = _HybridAISquaredLearner.DEFAULT_FILTERS,
    ) -> None:
        """
        Initialize the learner.

        Args:
            model_id: Base model to fine-tune (``Qwen/Qwen3-14B`` in the submission).
            device: Device for training and inference; training needs CUDA.
            adapter_path: Existing adapter directory; ``fit`` then skips training.
            output_dir: Directory for checkpoints and the trained adapter.
            eval_size: Share of the training records held out for early stopping.
            max_new_tokens: Maximum number of generated tokens, reasoning included.
            temperature: Sampling temperature.
            top_p: Nucleus sampling threshold.
            top_k: Top-k sampling threshold.
            enable_thinking: Let Qwen3 reason before answering.
            filters: Cleaning steps applied to the predicted triples.
        """
        super().__init__(model_id=model_id, device=device, max_new_tokens=max_new_tokens, temperature=temperature,
                         top_p=top_p, top_k=top_k, enable_thinking=enable_thinking,
                         load_in_4bit=device.startswith("cuda"), filters=filters)
        self.adapter_path = Path(adapter_path) if adapter_path is not None else None
        self._existing_adapter = adapter_path is not None
        self.output_dir = Path(output_dir)
        self.eval_size = eval_size

    def load(self, model_id: Optional[str] = None, **kwargs: Any) -> None:
        """
        Load the base model with its adapter; without an adapter, loading waits until ``fit`` has trained one.

        Args:
            model_id: Optional base model identifier or local path.
        """
        if model_id is not None:
            self.model_id = model_id
        if self.adapter_path is None:
            return
        self.tokenizer, self.model = self._load_causal_lm(self.model_id, adapter_path=self.adapter_path)
        self._loaded_model_id = self.model_id

    def build_messages(self, sample: Dict[str, Any], with_target: bool = False) -> List[Dict[str, str]]:
        """Build the chat messages for a record, with the gold triples as the answer if ``with_target``."""
        messages = [
            {"role": "system", "content": self.TEMPLATES["finetune_system"]},
            {"role": "user", "content": self._fill("finetune_input", sample)},
        ]
        if with_target:
            messages.append({"role": "assistant", "content": json.dumps(sample[self.TARGET], indent=4)})
        return messages

    def _fit(self, data: List[Dict[str, Any]]) -> None:
        """Fine-tune the LoRA adapter on the training records, unless an adapter was given."""
        if self._existing_adapter:
            return
        for sample in data:
            if self.TARGET not in sample:
                raise KeyError(f"Missing '{self.TARGET}' in expansion training sample.")
        if len(data) < 2:
            raise ValueError("Fine-tuning needs at least two labeled samples for the train/eval split.")
        if not self.device.startswith("cuda"):
            raise RuntimeError("4-bit LoRA fine-tuning requires a CUDA device.")

        from sklearn.model_selection import train_test_split

        train_rows, eval_rows = train_test_split(
            data, test_size=self.eval_size, shuffle=True, random_state=self.SPLIT_SEED
        )
        self.adapter_path = self.output_dir / "adapter"
        self._train(train_rows, eval_rows, self.adapter_path)
        self.load()

    def _to_dataset(self, tokenizer: Any, rows: List[Dict[str, Any]]) -> Any:
        """Tokenize the full training chats."""
        from datasets import Dataset

        texts = [
            tokenizer.apply_chat_template(self.build_messages(row, with_target=True), tokenize=False)
            for row in rows
        ]
        encoded = tokenizer(texts, truncation=True, max_length=self.MAX_SEQ_LENGTH)
        return Dataset.from_dict({"input_ids": encoded["input_ids"], "attention_mask": encoded["attention_mask"]})

    def _train(self, train_rows: List[Dict[str, Any]], eval_rows: List[Dict[str, Any]], adapter_dir: Path) -> None:
        """Fine-tune a 4-bit LoRA adapter with the submission's settings and save it."""
        import torch
        from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
        from transformers import (
            AutoModelForCausalLM,
            AutoTokenizer,
            BitsAndBytesConfig,
            DataCollatorForLanguageModeling,
            EarlyStoppingCallback,
            Trainer,
            TrainingArguments,
            set_seed,
        )

        set_seed(self.TRAIN_SEED)
        tokenizer = AutoTokenizer.from_pretrained(self.model_id, trust_remote_code=True)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        bf16 = torch.cuda.is_bf16_supported()
        dtype = torch.bfloat16 if bf16 else torch.float16
        model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            trust_remote_code=True,
            torch_dtype=dtype,
            device_map="auto",
            quantization_config=BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=dtype,
                bnb_4bit_use_double_quant=True,
            ),
        )
        model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=True)
        model = get_peft_model(
            model,
            LoraConfig(
                r=self.LORA_R,
                lora_alpha=self.LORA_ALPHA,
                lora_dropout=self.LORA_DROPOUT,
                bias="none",
                task_type="CAUSAL_LM",
                target_modules=self.TARGET_MODULES,
            ),
        )
        trainer = Trainer(
            model=model,
            args=TrainingArguments(
                output_dir=str(adapter_dir),
                per_device_train_batch_size=self.PER_DEVICE_TRAIN_BATCH_SIZE,
                per_device_eval_batch_size=self.PER_DEVICE_TRAIN_BATCH_SIZE,
                gradient_accumulation_steps=self.GRADIENT_ACCUMULATION_STEPS,
                warmup_steps=self.WARMUP_STEPS,
                num_train_epochs=self.NUM_TRAIN_EPOCHS,
                learning_rate=self.LEARNING_RATE,
                optim="adamw_8bit",
                weight_decay=self.WEIGHT_DECAY,
                lr_scheduler_type="linear",
                seed=self.TRAIN_SEED,
                bf16=bf16,
                fp16=not bf16,
                fp16_full_eval=True,
                gradient_checkpointing=True,
                gradient_checkpointing_kwargs={"use_reentrant": False},
                save_strategy="steps",
                save_steps=self.EVAL_SAVE_STEPS,
                eval_strategy="steps",
                eval_steps=self.EVAL_SAVE_STEPS,
                metric_for_best_model="eval_loss",
                greater_is_better=False,
                load_best_model_at_end=True,
                report_to="none",
            ),
            train_dataset=self._to_dataset(tokenizer, train_rows),
            eval_dataset=self._to_dataset(tokenizer, eval_rows),
            data_collator=DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False),
            callbacks=[EarlyStoppingCallback(early_stopping_patience=self.EARLY_STOPPING_PATIENCE)],
        )
        trainer.train()
        adapter_dir.mkdir(parents=True, exist_ok=True)
        trainer.save_model(str(adapter_dir))
        tokenizer.save_pretrained(str(adapter_dir))

        # Free training memory before the adapter is loaded for inference.
        del trainer, model
        gc.collect()
        torch.cuda.empty_cache()

    def _predict(self, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Predict all new triples of each record with the fine-tuned model."""
        conversations = [self.build_messages(sample) for sample in data]
        responses = self._generate(conversations, include_prompt=True)
        return [
            self._finalise(sample, self._clean(self._parse(response, finetuned=True), sample.get(self.INITIAL_KEY, [])))
            for sample, response in zip(data, responses)
        ]
