Quickstart Guide
=================
This guide will walk you through using OntoLearner to perform various ontology learning tasks using machine learning and large language models.

Installation
--------------
First, install OntoLearner using pip:

.. code-block:: bash

    pip install -e .

You'll also need to set up your Hugging Face token for accessing models:

1. Create an account on `Hugging Face <https://huggingface.co/>`_
2. Generate an access token in your account settings
3. Create a `.env` file in your project root with:

.. code-block:: bash

    HUGGINGFACE_ACCESS_TOKEN=your_token_here

Machine Learning Workflow
---------------------------
OntoLearner follows a standard machine learning workflow:

1. **Import ontology data** - Load existing ontologies
2. **Perform train-test split** - Divide data for training and evaluation
3. **Train models** - Use retrieval-augmented generation with LLMs
4. **Make predictions** - Apply the trained models to new data
5. **Evaluate results** - Assess performance using metrics

Example Tasks
---------------
OntoLearner supports three main ontology learning tasks:

1. **Term Typing** - Predicting the type(s) of a given term
2. **Taxonomy Discovery** - Identifying hierarchical relationships
3. **Non-Taxonomy Discovery** - Identifying non-hierarchical relationships

Below we walk through examples of each task.

Term Typing Example
~~~~~~~~~~~~~~~~~~~~~~~

Term typing involves predicting the semantic type(s) of a given term. For example, predicting that "Chardonnay" is a "WhiteWine".

.. code-block:: python

    # Import required libraries
    from ontolearner import Learner
    from ontolearner.learner import BERTRetrieverLearner, AutoLearnerLLM, AutoRAGLearner
    from ontolearner.learner.prompt import StandardizedPrompting
    from ontolearner.ontology import Wine
    from ontolearner.utils.train_test_split import ontology_train_test_split

    # Load ontology
    ontology = Wine()
    ontology.load("path/to/wine.owl")
    data = ontology.extract()

    # Split data
    train_data, test_data = ontology_train_test_split(data, test_size=0.2)

    # Set up learner components
    retriever = BERTRetrieverLearner()
    llm = AutoLearnerLLM(token="your_huggingface_token")  # Pass token here
    prompting = StandardizedPrompting(task="term-typing")
    rag_learner = AutoRAGLearner(retriever, llm, prompting)
    learner = Learner(learner=rag_learner, prompting=prompting)

    # Train the learner
    learner.learn(
        train_data,
        task="term-typing",
        retriever_id="sentence-transformers/all-MiniLM-L6-v2",
        llm_id="mistralai/Mistral-7B-Instruct-v0.1",
        top_k=3
    )

    # Make a prediction
    term = "Chardonnay"
    predicted_types = rag_learner.predict(term, task="term-typing")
    print(f"Term: {term}")
    print(f"Predicted Types: {predicted_types}")

For a complete example, see `examples/term_typing_example.py`.


Taxonomy Discovery Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Taxonomy discovery involves predicting whether a hierarchical relationship exists between two terms.
For example, determining if "WhiteWine" is a parent class of "Chardonnay".

.. code-block:: python

    # Similar setup as above, but with different task
    prompting = StandardizedPrompting(task="taxonomy-discovery")
    rag_learner = AutoRAGLearner(retriever, llm, prompting)
    learner = Learner(learner=rag_learner, prompting=prompting)

    # Train the learner
    learner.learn(
        train_data,
        task="taxonomy-discovery",
        retriever_id="sentence-transformers/all-MiniLM-L6-v2",
        llm_id="mistralai/Mistral-7B-Instruct-v0.1",
        top_k=3
    )

    # Make a prediction
    parent = "WhiteWine"
    child = "Chardonnay"
    prediction = rag_learner.predict((parent, child), task="taxonomy-discovery")
    print(f"Parent: {parent}")
    print(f"Child: {child}")
    print(f"Prediction: {prediction}")

For a complete example, see `examples/taxonomy_discovery_example.py`.


Non-Taxonomy Discovery Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Non-taxonomy discovery involves predicting the type of non-hierarchical relationship between two terms.
For example, determining the relationship between "Wine" and "WineGrape".

.. code-block:: python

    # Similar setup as above, but with different task
    prompting = StandardizedPrompting(task="non-taxonomy-discovery")
    rag_learner = AutoRAGLearner(retriever, llm, prompting)
    learner = Learner(learner=rag_learner, prompting=prompting)

    # Train the learner
    learner.learn(
        train_data,
        task="non-taxonomy-discovery",
        retriever_id="sentence-transformers/all-MiniLM-L6-v2",
        llm_id="mistralai/Mistral-7B-Instruct-v0.1",
        top_k=3
    )

    # Make a prediction
    head = "Wine"
    tail = "WineGrape"
    prediction = rag_learner.predict((head, tail), task="non-taxonomy-discovery")
    print(f"Head: {head}")
    print(f"Tail: {tail}")
    print(f"Predicted Relation: {prediction}")

For a complete example, see `examples/non_taxonomy_discovery_example.py`.

Running the Examples
-----------------------
To run the example scripts:

.. code-block:: bash

    # Run term typing example
    python examples/term_typing_example.py

    # Run taxonomy discovery example
    python examples/taxonomy_discovery_example.py

    # Run non-taxonomy discovery example
    python examples/non_taxonomy_discovery_example.py

Customizing the Pipeline
---------------------------
You can customize various aspects of the pipeline:

- **Ontology Source**: Use any of the built-in ontologies or import your own
- **LLM Model**: Choose from various Hugging Face models
- **Retriever Model**: Select different embedding models for retrieval
- **Prompting Strategy**: Customize the prompts used for each task

For more advanced usage, see the API documentation.
