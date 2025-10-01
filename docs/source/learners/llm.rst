Large Language Models
========================


.. sidebar:: Examples

    * LLM Learner Example: `llm_learner.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner.py>`_
    * LLM Learner Pipeline Usage Example: `llm_learner_pipeline_usage.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_pipeline_usage.py>`_


LLM-only learners leverage the power of large language models to perform ontology learning tasks
without using retrieval components. This approach is particularly useful when you want to rely
on the model's inherent knowledge rather than specific examples from the training data.

Loading Ontological Data
----------------------------

We start by importing necessary components from the ontolearner package, loading ontology, and doing train-test splits.

.. code-block:: python

    from ontolearner import AutoLLMLearner, AgrO, train_test_split, LabelMapper, StandardizedPrompting, evaluation_report

    ontology = AgrO()

    ontology.load()

    ontological_data = ontology.extract()

    train_data, test_data = train_test_split(ontological_data, test_size=0.2, random_state=42)

.. note::

    * ``AutoLLMLearner``: A wrapper class to easily configure and run LLM-based learners.
    * ``LabelMapper``: Maps generated outputs to specified clases.
    * ``StandardizedPrompting``: A default prompting strategy for prompting LLMs in a consistent way.
    * ``evaluation_report``: A evaluation method for LLMs4OL tasks.

Initialize Learner
-----------------------------

Before defining the LLM learner, choose the task you want the LLM to perform. Available tasks has been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_. The task IDs are: 'term-typing', 'taxonomy-discovery', 'non-taxonomic-re'.

.. code-block:: python

    task = 'non-taxonomic-re'

Next, to use LLMs hosted on HuggingFace or other providers that require token, provide a valid access token:

.. code-block:: python

    token = '...'

Setup the learner with your prompting and label mapping strategies and then load the desired model:

.. code-block:: python

    llm_learner = AutoLLMLearner(
        prompting=StandardizedPrompting,
        label_mapper=LabelMapper(),
        token=token
    )
    llm_learner.load(model_id='Qwen/Qwen2.5-0.5B-Instruct')

Next, ``.fit`` the model and make the predictions:

.. code-block:: python

    llm_learner.fit(train_data, task=task)

    predicts = llm_learner.predict(test_data, task=task)

    truth = llm_learner.tasks_ground_truth_former(data=test_data, task=task)

    metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)

    print(metrics)

You will see a evaluations results.



.. hint::

    OntoLearner supports various LLM models, including (but not limited to):

    - Mistral models (e.g., "mistralai/Mistral-7B-Instruct-v0.1")
    - Llama models (e.g., "meta-llama/Llama-3.1-8B-Instruct")
    - Qwen models (e.g., "Qwen/Qwen3-0.6B")
    - DeepSeek models (e.g., "deepseek-ai/deepseek-llm-7b-base")
    - ...


Pipeline Usage
-----------------------
The OntoLearner package also offers a streamlined ``LearnerPipeline`` class that simplifies the entire process of initializing, training, predicting, and evaluating a RAG setup into a single call. This is particularly useful for rapid experimentation and deployment.

.. code-block:: python

    # Import the main components from the OntoLearner library
    from ontolearner import LearnerPipeline, AgrO, train_test_split

    # Load the AgrO ontology, which contains agricultural concepts and relationships
    ontology = AgrO()
    ontology.load()  # Parse and initialize internal ontology structures, including term-type pairs

    # Extract annotated examples (terms and their types), and split into train/test sets
    train_data, test_data = train_test_split(
        ontology.extract(),     # Extract raw (term, types) instances from the ontology
        test_size=0.2,          # 20% of the data is reserved for evaluation
        random_state=42         # Ensure reproducibility by setting a fixed seed
    )

    # Set up the learner pipeline using a lightweight instruction-tuned LLM
    pipeline = LearnerPipeline(
        llm_id='Qwen/Qwen2.5-0.5B-Instruct',   # Small-scale LLM for reasoning over term-type assignments
        hf_token='...',                        # Hugging Face access token for loading gated models
        batch_size=32                          # Batch size for parallel inference (if applicable)
    )

    # Run the full learning pipeline on the term-typing task
    outputs = pipeline(
        train_data=train_data,
        test_data=test_data,
        evaluate=True,               # Enables automatic computation of precision, recall, F1
        task='term-typing'           # The task is to classify terms into semantic types
    )

    # Display the evaluation results
    print("Metrics:", outputs['metrics'])          # Shows {'precision': ..., 'recall': ..., 'f1_score': ...}

    # Display total elapsed time for training + prediction + evaluation
    print("Elapsed time:", outputs['elapsed_time'])

    # Print all returned outputs (include predictions)
    print(outputs)


Custom AutoLLM
-----------------

OntoLearner provides a default ``AutoLLM`` wrapper for handling popular model families (Mistral, Llama, Qwen, etc.) through HuggingFace or external providers. However, in some cases you may want to integrate a model family that is not natively supported (e.g., Falcon, DeepSeek, or a proprietary LLM).

For this, you can extend the ``AutoLLM`` class and implement the required
``load`` and ``generate`` methods. Basic requirements are:

1. Inherit from ``AutoLLM``
2. Implement ``load(model_id)``, if your loging model is different (as an example `mistralai/Mistral-Small-3.2-24B-Instruct-2506 <https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506>`_ uses different type of loading)
3. Implement ``generate(inputs, max_new_tokens)`` to encodes prompts, performs generation, decodes outputs, and maps them to labels.


.. tab::

	The following example shows how to build a Falcon integration:

	::

	    from ontolearner import AutoLLM
	    from typing import List
	    import torch

	    class FalconLLM(AutoLLM):

	        def generate(self, inputs: List[str], max_new_tokens: int = 50) -> List[str]:
	            encoded_inputs = self.tokenizer(
	                inputs,
	                return_tensors="pt",
	                padding=True,
	                truncation=True
	            ).to(self.model.device)

	            input_ids = encoded_inputs["input_ids"]
	            input_length = input_ids.shape[1]

	            outputs = self.model.generate(
	                input_ids,
	                max_new_tokens=max_new_tokens,
	                pad_token_id=self.tokenizer.eos_token_id
	            )

	            generated_tokens = outputs[:, input_length:]
	            decoded_outputs = [
	                self.tokenizer.decode(g, skip_special_tokens=True).strip()
	                for g in generated_tokens
	            ]

	            return self.label_mapper.predict(decoded_outputs)

.. tab::

	For Mistral, you can integrate the official ``mistral-common`` tokenizer and chat completion interface:

	::

    from ontolearner import AutoLLM
    from typing import List
    import torch

    class MistralLLM(AutoLLM):

        def load(self, model_id: str) -> None:
            from mistral_common.tokens.tokenizers.mistral import MistralTokenizer
            from mistral_common.models.modeling_mistral import Mistral3ForConditionalGeneration

            self.tokenizer = MistralTokenizer.from_hf_hub(model_id)

            device_map = "cpu" if self.device == "cpu" else "balanced"
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
            from mistral_common.protocol.instruct.messages import ChatCompletionRequest

            tokenized_list = []
            for prompt in inputs:
                messages = [{"role": "user", "content": [{"type": "text", "text": prompt}]}]
                tokenized = self.tokenizer.encode_chat_completion(ChatCompletionRequest(messages=messages))
                tokenized_list.append(tokenized.tokens)

            # Pad inputs and create attention masks
            max_len = max(len(tokens) for tokens in tokenized_list)
            input_ids, attention_masks = [], []
            for tokens in tokenized_list:
                pad_length = max_len - len(tokens)
                input_ids.append(tokens + [self.tokenizer.pad_token_id] * pad_length)
                attention_masks.append([1] * len(tokens) + [0] * pad_length)

            input_ids = torch.tensor(input_ids).to(self.model.device)
            attention_masks = torch.tensor(attention_masks).to(self.model.device)

            outputs = self.model.generate(
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


Once your custom class is defined, you can pass it into ``AutoLLMLearner``:

.. code-block:: python

    from ontolearner import AutoLLMLearner, LabelMapper, StandardizedPrompting

    falcon_learner = AutoLLMLearner(
        prompting=StandardizedPrompting,
        label_mapper=LabelMapper(),
        llm=FalconLLM,      # 👈 plug in custom Falcon
        token="...",
        device="cuda"
    )

    falcon_learner.llm.load(model_id="tiiuae/falcon-7b-instruct")

    # Train and evaluate
    falcon_learner.fit(train_data, task="term-typing")
    predictions = falcon_learner.predict(test_data, task="term-typing")

    print(predictions)

The following models are specialized within the OntoLearner:

- To use `mistralai/Mistral-Small-3.2-24B-Instruct-2506 <https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506>`_ you can use ``MistralLLM`` instead of ``AutoLLM`
- To use `Falcon-H` series of LLMs (e.g. `tiiuae/Falcon-H1-1.5B-Deep-Instruct <https://huggingface.co/tiiuae/Falcon-H1-1.5B-Deep-Instruct>`_ you can ``FalconLLM`` instead of ``AutoLLM`.

.. note::

   You can implement as many custom AutoLLM classes as needed (e.g., for proprietary APIs, local models, or new HF releases). As long as they subclass ``AutoLLM`` and implement ``load`` + ``generate``, they will work seamlessly with ``AutoLLMLearner``.


.. hint::
    See `Learning Tasks <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_ for possible tasks within Learners.
