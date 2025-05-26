Retrieval Models
=================
Retriever-only learners use embedding-based retrieval models
to perform ontology learning tasks without using LLMs.

How Retriever-only Learners Work
--------------------------------
Retriever-only learners operate by:
1. **Indexing**: Creating embeddings for all examples in the training data
2. **Retrieval**: Finding the most similar examples to the input query based on embedding similarity
3. **Prediction**: Using the retrieved examples to make a prediction (e.g., by majority voting)

The methodology behind retriever-only learners is founded on vector representations of ontological elements,
allowing for semantic comparison in a high-dimensional space. By transforming terms, concepts,
and relationships into embeddings through pre-trained language models, the system can measure semantic similarity
between ontological components without relying on explicit linguistic patterns or rules.
This approach leverages the distributional hypothesis—that semantically similar terms
appear in similar contexts—to identify relationships between entities. The system then employs
deterministic aggregation methods like majority voting or weighted consensus to derive predictions
from the retrieved examples. This methodology is computationally efficient compared to LLM-based approaches
and particularly effective for tasks with well-defined patterns across domain-specific ontologies.

Setting Up a Retriever-only Learner
----------------------------------
Here's how to set up a Retriever-only learner using the OntoLearner pipeline:

.. code-block:: python

    from ontolearner.learner_pipeline import LearnerPipeline
    from ontolearner.learner import BERTRetrieverLearner
    from ontolearner.ontology import Wine
    from ontolearner.utils.train_test_split import train_test_split

    ontology = Wine()
    ontology.load()
    train_data, test_data = train_test_split(ontology.extract(), test_size=0.2)

    pipeline = LearnerPipeline(
        task="non-taxonomy-discovery",
        retriever=BERTRetrieverLearner(),
        retriever_id="sentence-transformers/all-MiniLM-L6-v2"
    )

    results, metrics = pipeline.fit_predict_evaluate(
        train_data=train_data,
        test_data=test_data,
        top_k=5,
        test_limit=10
    )

Supported Models
---------------
OntoLearner supports various retrieval models, including:

- Sentence Transformers (e.g., "sentence-transformers/all-MiniLM-L6-v2")
- T5 models (e.g., "google/flan-t5-base")
- N-gram based retrieval (for lightweight applications)

Supported Tasks
--------------
Retriever-only learners support all three main ontology learning tasks:

1. **Term Typing**: Predicting the type(s) of a given term
2. **Taxonomy Discovery**: Identifying hierarchical relationships
3. **Non-Taxonomy Discovery**: Identifying non-hierarchical relationships

Example
-------
For a complete example of using a Retriever-only learner, see the example script:

.. code-block:: bash

    python scripts/examples/learner_example_retriever.py

.. note::

   The code is available at `OntoLearner GitHub repository <https://github.com/sciknoworg/OntoLearner/blob/dev/scripts/examples/learner_example_retriever.py>`_
