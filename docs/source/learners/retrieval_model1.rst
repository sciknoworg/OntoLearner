rwth_dbis learners 
==================

Description
-----------

.. sidebar:: Examples

    * rwth_dbis Taxonomy Discovery Example: `llm_learner_rwthdbis_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_rwthdbis_taxonomy_discovery.py>`_
    * rwth_dbis Term Typing Example: `llm_learner_rwthdbis_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_rwthdbis_term_typing.py>`_


LLMs4OL learners address ontology learning tasks that leverage the reasoning capabilities of large language models to infer structured knowledge representations. In this study, two core tasks defined by the LLMs4OL Challenge were investigated: (1) Term Typing, which focuses on identifying the generalized semantic type for a given lexical term, and (2) Taxonomy Discovery, which aims to infer hierarchical (parent–child) relationships between ontological concepts. Together, these tasks form the foundation for constructing and refining domain-specific ontologies through automated linguistic and semantic analysis.

The experimental objectives were centered on evaluating the comparative effectiveness of open-source and commercial large language models in performing these ontology learning tasks. Specifically, the research sought to answer two guiding questions: (a) How do commercial LLMs compare with open-source models in terms of accuracy and generalization within domain-specific ontology learning scenarios?, and (b) To what extent can open-source models be enhanced through targeted training strategies and fine-tuning methods to close the performance gap with proprietary systems? Addressing these questions enables a deeper understanding of how different model architectures and adaptation techniques influence the capability of LLMs to perform ontology reasoning and structure induction efficiently and reliably.

   
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

    task = 'term-typing'

Next, initiate the learner by specifying ``top_k`` parameter and load the desired ``sentence-transformer`` based model as a retriever.

.. code-block:: python

    ret_learner = AutoRetrieverLearner(top_k=5)

    ret_learner.load(model_id='sentence-transformers/all-MiniLM-L6-v2')

    # Index the model on the training data for LLMs4OL task
    ret_learner.fit(train_data, task=task)

    predicts = ret_learner.predict(test_data, task=task)

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

This page documents two example pipelines implemented in **OntoLearner** — 
one for *term typing* (using the AgrO ontology) and another for *taxonomy-discovery*.

Each pipeline demonstrates how to load data, configure a learner, 
build a pipeline, and evaluate the model.

.. contents::
   :local:
   :depth: 2

--------------------
Term-Typing Pipeline 
--------------------

The following example shows how to train a **term typing** model using 
the ``RWTHDBISTermTypingLearner``.  

.. code-block:: python

        # Import core modules from the OntoLearner library
    from ontolearner import LearnerPipeline, train_test_split, AgrO
    from ontolearner import RWTHDBISTermTypingLearner

    #load the AgrO ontology.
    # AgrO provides term-typing supervision where each term can be annotated with one or more types.
    ontology = AgrO()
    ontology.load()
    data = ontology.extract()

    # Split the labeled term-typing data into train and test sets
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

    # Configure a supervised encoder-based classifier for term typing.
    # This fine-tunes DeBERTa v3 on (term → type) signals; increase epochs for stronger results.
    learner = RWTHDBISTermTypingLearner(
        model_name="microsoft/deberta-v3-small",
        output_dir="./results/deberta-v3",
        num_train_epochs=30,
        per_device_train_batch_size=16,
        gradient_accumulation_steps=2,
        learning_rate=2e-5,
        max_length=64,
        seed=42,
    )

    # Build the pipeline and pass raw structured objects end-to-end.
    pipeline = LearnerPipeline(
        llm=learner,
        llm_id=learner.model_name,
        ontologizer_data=False,
    )

    # Run the full learning pipeline on the term-typing task
    outputs = pipeline(
        train_data=train_data,
        test_data=test_data,
        task="term-typing",
        evaluate=True,
        ontologizer_data=False,
    )

    # Display the evaluation results
    print("Metrics:", outputs['metrics'])          # Shows {'precision': ..., 'recall': ..., 'f1_score': ...}

    # Display total elapsed time for training + prediction + evaluation
    print("Elapsed time:", outputs['elapsed_time'])

    # Print all returned outputs (include predictions)
    print(outputs)

---------------------------
Taxonomy Discovery Pipeline
---------------------------

The second pipeline example focuses on **taxonomy-discovery**, 
demonstrating how to adapt the pipeline for a different ontology or learner.

.. code-block:: python

    # Import core modules from the OntoLearner library
    from ontolearner import LearnerPipeline, train_test_split
    from ontolearner import ChordOntology, RWTHDBISTaxonomyLearner

    # Load the Chord ontology, which exposes hierarchical (parent, child) relations for taxonomy discovery
    ontology = ChordOntology()
    ontology.load()  # Read entities, type system, and taxonomic edges into memory

    # Extract typed taxonomic edges and split into train/test while preserving the structured shape
    train_data, test_data = train_test_split(
        ontology.extract(),
        test_size=0.2,
        random_state=42
    )

    # Initialize a supervised taxonomy classifier (encoder-based fine-tuning)
    # Negative sampling controls the number of non-edge examples; bidirectional templates create both (p→c) and (c→p) views
    # Context features are optional and can be enabled with with_context=True and a JSON path of type descriptions
    learner = RWTHDBISTaxonomyLearner(
        model_name="microsoft/deberta-v3-small",
        output_dir="./results/",
        num_train_epochs=1,
        per_device_train_batch_size=8,
        gradient_accumulation_steps=4,
        learning_rate=2e-5,
        max_length=256,
        seed=42,
        negative_ratio=5,
        bidirectional_templates=True,
        context_json_path=None,
        ontology_name=ontology.ontology_full_name,
    )

    # Build the pipeline
    pipeline = LearnerPipeline(
        llm=learner,
        llm_id=learner.model_name,
        ontologizer_data=False,
    )

    # # Run the full learning pipeline on the taxonomy-discovery task
    outputs = pipeline(
        train_data=train_data,
        test_data=test_data,
        task="taxonomy-discovery",
        evaluate=True,
        ontologizer_data=False,
    )

    # Display the evaluation results
    print("Metrics:", outputs['metrics'])          # Shows {'precision': ..., 'recall': ..., 'f1_score': ...}

    # Display total elapsed time for training + prediction + evaluation
    print("Elapsed time:", outputs['elapsed_time'])

    # Print all returned outputs (include predictions)
    print(outputs)


.. hint::
    See `Learning Tasks <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_ for possible tasks within Learners.


