Retrieval Models
=================

.. sidebar:: Examples

    * Retrieval Learner Example: `retriever_learner.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/retriever_learner.py>`_
    * Retrieval Learner Pipeline Usage Example: `retriever_learner_pipeline_usage.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/retriever_learner_pipeline_usage.py>`_


Retriever-only learners use embedding-based retrieval models to perform ontology learning tasks without using LLMs. Retriever-only learners operate by: 1) Indexing: Creating embeddings for all examples in the training data, 2)  Retrieval: Finding the most similar examples to the input query based on embedding similarity. The methodology behind retriever-only learners is founded on vector representations of ontological elements, allowing for semantic comparison in a high-dimensional space.

By transforming terms, concepts, and relationships into embeddings through pre-trained language models, the system can measure semantic similarity between ontological components without relying on explicit linguistic patterns or rules. This approach leverages the distributional hypothesis—that semantically similar terms appear in similar contexts—to identify relationships between entities. The system then employs deterministic aggregation methods like majority voting or weighted consensus to derive predictions from the retrieved examples. This methodology is computationally efficient compared to LLM-based approaches and particularly effective for tasks with well-defined patterns across domain-specific ontologies.

Loading Ontological Data
----------------------------------
We start by importing necessary components from the ontolearner package, loading ontology, and doing train-test splits.


.. code-block:: python

    from ontolearner import AutoRetrieverLearner, AgrO, train_test_split, evaluation_report

    ontology = AgrO()

    ontology.load()

    ontological_data = ontology.extract()

    train_data, test_data = train_test_split(ontological_data, test_size=0.2, random_state=42)

.. note::

    * ``AutoRetrieverLearner``: A wrapper class to easily configure and run retriever-based learners.

Initialize Learner
----------------------------------

Before defining the Retriever learner, choose the task you want the Retriever to perform. Available tasks has been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_. The task IDs are: 'term-typing', 'taxonomy-discovery', 'non-taxonomic-re'.

.. code-block:: python

    task = 'non-taxonomic-re'

Next, initiate the learner by specifying ``top_k`` parameter and load the desired ``sentence-transformer`` based model as a retriever.

.. code-block:: python

    ret_learner = AutoRetrieverLearner(top_k=5)

    ret_learner.load(model_id='sentence-transformers/all-MiniLM-L6-v2')

    # Index the model on the training data for LLMs4OL task
    ret_learner.fit(train_data, task=task)

    predict = ret_learner.predict(test_data, task=task)

    truth = ret_learner.tasks_ground_truth_former(data=test_data, task=task)

    metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)

    print(metrics)

You will see a evaluations results.

.. hint::

    OntoLearner supports various retrieval models, including:

    * Various `sentence-transformers <https://huggingface.co/sentence-transformers>`_ models
    * T5 models (e.g., "google/flan-t5-base")
    * Nomic-AI models

Pipeline Usage
-----------------------

.. code-block:: python

    # Import core components from the OntoLearner library
    from ontolearner import LearnerPipeline, AgrO, train_test_split

    # Load the AgrO ontology, which includes structured agricultural knowledge
    ontology = AgrO()
    ontology.load()  # Load ontology data (e.g., entities, relations, metadata)

    # Extract relation instances from the ontology and split them into training and test sets
    train_data, test_data = train_test_split(
        ontology.extract(),      # Extract annotated (head, tail, relation) triples
        test_size=0.2,           # 20% for evaluation
        random_state=42          # Ensures reproducible splits
    )

    # Initialize the learning pipeline using a dense retriever
    # This configuration uses sentence embeddings to match similar relational contexts
    pipeline = LearnerPipeline(
        retriever_id='sentence-transformers/all-MiniLM-L6-v2',  # Hugging Face model ID for retrieval
        batch_size=10,       # Number of samples to process per batch (if batching is enabled internally)
        top_k=5              # Retrieve top-5 most relevant support instance per query
    )

    # Run the pipeline on the training and test data
    # The pipeline performs: fit() → predict() → evaluate() in sequence
    outputs = pipeline(
        train_data=train_data,
        test_data=test_data,
        evaluate=True,           # If True, computes precision, recall, and F1-score
        task='non-taxonomic-re'  # Specifies that we are doing non-taxonomic relation prediction
    )

    # Print the evaluation metrics (precision, recall, F1)
    print("Metrics:", outputs['metrics'])

    # Print the total elapsed time for training and evaluation
    print("Elapsed time:", outputs['elapsed_time'])

    # Print the full output dictionary (includes predictions)
    print(outputs)
