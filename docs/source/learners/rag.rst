Retrieval Augmented Generation
=======================================
RAG (Retrieval Augmented Generation) learners combine the strengths of both retrieval models
and large language models to perform ontology learning tasks.

How RAG Learners Work
---------------------
RAG learners operate in two main steps:
1. **Retrieval**: First, the retriever component finds the most relevant examples from the training data based on similarity to the input query.
2. **Generation**: Then, the LLM component uses these retrieved examples as context to generate a response.

Setting Up a RAG Learner
------------------------
Here's how to set up a RAG learner using the OntoLearner pipeline:

.. code-block:: python

    from ontolearner.learner_pipeline import LearnerPipeline
    from ontolearner.ontology import Wine
    from ontolearner.utils.train_test_split import train_test_split

    ontology = Wine()
    ontology.load()
    train_data, test_data = train_test_split(ontology.extract(), test_size=0.2)

    pipeline = LearnerPipeline(
        task="term-typing",
        retriever_id="sentence-transformers/all-MiniLM-L6-v2",
        llm_id="mistralai/Mistral-7B-Instruct-v0.1",
        hf_token="your_huggingface_token"
    )

    results, metrics = pipeline.fit_predict_evaluate(
        train_data=train_data,
        test_data=test_data,
        top_k=3,
        test_limit=10
    )

Supported Tasks
--------------
RAG learners support all three main ontology learning tasks:
1. **Term Typing**: Predicting the type(s) of a given term
2. **Taxonomy Discovery**: Identifying hierarchical relationships
3. **Non-Taxonomy Discovery**: Identifying non-hierarchical relationships

Example
-------
For a complete example of using a RAG learner, see the example script:

.. code-block:: bash

    python scripts/examples/learner_example_rag.py
