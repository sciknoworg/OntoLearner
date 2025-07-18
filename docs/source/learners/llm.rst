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

.. hint::
    See `Learning Tasks <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_ for possible tasks within Learners.
