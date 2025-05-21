Large Language Models
========================
LLM-only learners leverage the power of large language models to perform ontology learning tasks
without using retrieval components. This approach is particularly useful when you want to rely
on the model's inherent knowledge rather than specific examples from the training data.

How LLM-only Learners Work
--------------------------
LLM-only learners operate by:
1. **Prompting**: Formulating a task-specific prompt that describes the ontology learning task
2. **Generation**: Using the LLM to generate a response based on the prompt and its pre-trained knowledge

Setting Up an LLM-only Learner
-----------------------------
Here's how to set up an LLM-only learner using the OntoLearner pipeline:

.. code-block:: python

    from ontolearner.learner_pipeline import LearnerPipeline
    from ontolearner.learner import AutoLearnerLLM
    from ontolearner.ontology import Wine
    from ontolearner.utils.train_test_split import train_test_split

    ontology = Wine()
    ontology.load()
    train_data, test_data = train_test_split(ontology.extract(), test_size=0.2)

    pipeline = LearnerPipeline(
        task="taxonomy-discovery",
        llm=AutoLearnerLLM(token="your_huggingface_token"),
        llm_id="mistralai/Mistral-7B-Instruct-v0.1"
    )

    results, metrics = pipeline.fit_predict_evaluate(
        train_data=train_data,
        test_data=test_data,
        test_limit=10
    )

Supported Models
---------------
OntoLearner supports various LLM models, including:

- Mistral models (e.g., "mistralai/Mistral-7B-Instruct-v0.1")
- Llama models (e.g., "meta-llama/Llama-3.1-8B-Instruct")
- Qwen models (e.g., "Qwen/Qwen3-0.6B")
- DeepSeek models (e.g., "deepseek-ai/deepseek-llm-7b-base")

Supported Tasks
--------------
LLM-only learners support all three main ontology learning tasks:

1. **Term Typing**: Predicting the type(s) of a given term
2. **Taxonomy Discovery**: Identifying hierarchical relationships
3. **Non-Taxonomy Discovery**: Identifying non-hierarchical relationships

Example
-------
For a complete example of using an LLM-only learner, see the example script:

.. code-block:: bash

    python scripts/examples/learner_example_llm.py
