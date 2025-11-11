RWTH-DBIS team 
==================

Description
-----------

.. sidebar:: Examples

    * RWTH-DBIS Taxonomy Discovery Example: `llm_learner_rwthdbis_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_rwthdbis_taxonomy_discovery.py>`_
    * RWTH-DBIS Term Typing Example: `llm_learner_rwthdbis_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_rwthdbis_term_typing.py>`_


The RWTH-DBIS team participated in the LLMs4OL Challenge at ISWC 2024, addressing two main tasks: term typing and taxonomy discovery. The team used LLaMA-3-8B and GPT-3.5-Turbo to compare performance gaps between open-source and commercial LLMs. For open-source models, methods included domain-specific continual training, fine-tuning, and knowledge-enhanced prompt-tuning, evaluated on benchmark datasets such as GeoNames, UMLS, Schema.org, and the Gene Ontology (GO).

The experiments aimed to assess the effectiveness of both open-source and commercial LLMs in term typing and taxonomy discovery, following three stages: data augmentation, model training, and inference. For Task A (Term Typing), training data included an optional context sentence (only for WordNet), a lexical term, and one or more conceptual term types. The test set contained only the lexical term and optional context. For Task B (Taxonomy Discovery), training data consisted of type pairs {Ta, Tb}, where Ta is the parent and Tb the child, while the test set included only types, requiring identification of “is-a” relations.

1) Data Collection: Term and type descriptions were gathered from public sources like Wikipedia via its API, followed by cleaning and structuring. Commercial LLMs with web search capabilities—GPT-4o, Claude-3, and Copilot—were accessed through APIs using zero-shot prompts to gather additional contextual information. Ontology datasets were accessed directly via APIs or downloads to obtain relevant context.

2) Training (Domain-Specific Continual Training): Context information for terms and types was integrated into the training data. For GeoNames, context was collected for all terms and types, while for other datasets, only type-level context was used.

+---------+-------------------------------------------------------------------------------------------------------------------------------------+
| **Task**| **Description**                                                                                                                     |
+=========+=====================================================================================================================================+
| Task A  | Models were trained on terms and corresponding types from the competition data. Each type was assigned a unique label, forming a    |
|         | dataset of term–label pairs for fine-tuning.                                                                                        |
+---------+-------------------------------------------------------------------------------------------------------------------------------------+
| Task B  | Hierarchical relationships were transformed into a binary classification format. Positive samples (parent–child) were labeled as 1, |
|         | and negative samples (reversed pairs) as 0, creating the final dataset for training.                                                |
+---------+-------------------------------------------------------------------------------------------------------------------------------------+

Loading Ontological Data
----------------------------------
We start by importing necessary components from the ontolearner package, loading ontology, and doing train-test splits.


.. code-block:: python

    from ontolearner import AutoRetrieverLearner, AgrO, train_test_split, evaluation_report

    ontology = AgrO()

    ontology.load()

    ontological_data = ontology.extract()

    train_data, test_data = train_test_split(ontological_data, test_size=0.2, random_state=42)


Initialize Learner
----------------------------------

Before defining the learner, choose the task you want the Retriever to perform. Available tasks has been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_. The task IDs are: 'term-typing', 'taxonomy-discovery'.

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


