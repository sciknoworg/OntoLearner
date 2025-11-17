SBU-NLP Team
================

Description
-----------

.. sidebar:: Examples

   * SBU-NLP Learner Text2Onto Example: `llm_learner_sbunlp_text2onto.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_sbunlp_text2onto.py>`_
   * SBU-NLP Learner Term Typing (Zero-Shot) Example: `llm_learner_sbunlp_zs_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_sbunlp_zs_term_typing.py>`_
   * SBU-NLP Learner Taxonomy Discovery (Few-shot) Example: `llm_learner_sbunlp_fs_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_sbunlp_fs_taxonomy_discovery.py>`_

The team participated in the LLMs4OL 2025 Shared Task, which included four subtasks:
(A) Ontological term and type extraction (Text2Onto),
(B) Term typing (Term Typing),
(C) Taxonomy discovery (Taxonomy Discovery).

The team focused on Tasks A, B, and C, adopting a unified prompting-based methodology that required no supervised training or fine-tuning. Instead, they applied prompt engineering combined with stratified and simple random sampling, as well as chunking-based strategies, to incorporate representative examples within the context window.

**Datasets**

* **Task A – Text2Onto.** Ontology extraction from domain-specific corpora in ecology, engineering, and scholarly domains.
* **Task B – Term Typing.** Semantic typing of terms using datasets from OBI and SWEET taxonomies.
* **Task C – Taxonomy Discovery.** Identification of hierarchical relations using OBI, Schema.org, SWEET, and MatOnto ontologies. Test instances correspond to unique types rather than document IDs.

**Methodology**

For **Term Typing**, the problem was framed as zero-shot label selection over an ontology-specific type inventory. The type inventory was derived from the training split, and Qwen-based LLMs were prompted to assign one or more valid type labels to each term without any parameter fine-tuning. Stratified sampling and prompt chunking were used to expose representative type examples within the context window while keeping prompts compact and model-agnostic.

For **Taxonomy Discovery**, the focus was on detecting parent–child relationships between ontology terms. Due to the relational nature of this task, batch prompting was employed to efficiently handle multiple type pairs per inference, enabling the model to consider several candidate relations jointly.

Term Typing
-----------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For term typing (Task B), we use the AgrO ontology. Terms and their labels are split into train and test sets; the train split is used to derive the type inventory, while the test split is used for evaluation.

.. code-block:: python

   from ontolearner import AgrO, train_test_split, evaluation_report

   ontology = AgrO()
   ontology.load()
   data = ontology.extract()

   # Split the data into train (for type inventory) and test (terms to type)
   train_data, test_data = train_test_split(
       data,
       test_size=0.6,  # 60% of data used for testing
       random_state=42,
   )

Initialize Learner
~~~~~~~~~~~~~~~~~~

Before defining the learner, choose the ontology learning task to perform.
Available tasks have been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_.
The task IDs are: ``term-typing``, ``taxonomy-discovery``, ``non-taxonomic-re``.

.. code-block:: python

   from ontolearner import SBUNLPZSLearner

   task = "term-typing"

Next, we configure the SBU-NLP Zero-Shot learner for term typing, using a Qwen model.
The learner's ``fit`` phase infers the inventory of allowed type labels; the model itself is never fine-tuned.

.. code-block:: python

   llm_learner = SBUNLPZSLearner(
       # Model / decoding
       model_id="Qwen/Qwen2.5-0.5B-Instruct",
       max_new_tokens=64,  # sufficient length for JSON list of types
       temperature=0.0,    # deterministic (greedy) output
       # token=None,       # assuming public model access
   )

   # Load the underlying LLM and prepare it for zero-shot term typing
   llm_learner.load(llm_id=llm_learner.model_id)

   # Learn the type inventory from the training split
   llm_learner.fit(train_data, task=task)

   # Predict types for the held-out test terms
   predicts = llm_learner.predict(test_data, task=task)
   truth = llm_learner.tasks_ground_truth_former(data=test_data, task=task)

   # Evaluate zero-shot term typing performance
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Pipeline Usage
~~~~~~~~~~~~~~

The :class:`LearnerPipeline` class runs the zero-shot term typing learner end-to-end: it learns the type inventory, predicts types for unseen terms, and evaluates performance.

.. code-block:: python

    # Import core modules from the OntoLearner library
    from ontolearner import AgrO, train_test_split, LearnerPipeline, evaluation_report

    # Import the specific Zero-Shot Learner implementation for Term Typing
    from ontolearner.learner.term_typing import SBUNLPZSLearner

    # Load ontology and split
    # Load the AgrO ontology for type inventory and test data.
    ontology = AgrO()
    ontology.load()
    data = ontology.extract()  # Extract the full set of relationships/terms

    # Split the data into train (to learn type inventory) and test (terms to predict)
    train_data, test_data = train_test_split(
        data,
        test_size=0.6,  # 60% of data used for testing
        random_state=42,
    )

    # Configure the Qwen Zero-Shot learner (inference-only)
    # This learner's 'fit' phase learns the vocabulary of allowed type labels.
    llm_learner = SBUNLPZSLearner(
        device="cpu",
        max_new_tokens=64,
        temperature=0.0,
        model_id="Qwen/Qwen2.5-0.5B-Instruct",
        token=None,
    )

    # Build pipeline and run
    pipe = LearnerPipeline(
        llm=llm_learner,
        llm_id=llm_learner.model_id,
        ontologizer_data=False,
        device="cpu",  # select CUDA or CPU
    )

    # Run the full learning pipeline on the Term-Typing task
    outputs = pipe(
        train_data=train_data,
        test_data=test_data,
        task="term-typing",
        evaluate=True,
        ontologizer_data=False,
    )

    # Display the evaluation results
    print("Metrics:", outputs.get("metrics"))

    # Display total elapsed time for learning (type inventory) + prediction + evaluation
    print("Elapsed time:", outputs.get("elapsed_time"))

    # Print all returned outputs (include predictions)
    print(outputs)


Taxonomy Discovery
-----------------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For taxonomy discovery (Task C), we use the GeoNames ontology as an example. It provides geographic parent–child relations (an *is-a* hierarchy) that can be split into train and test sets.

.. code-block:: python

   from ontolearner import GeoNames, train_test_split, evaluation_report

   ontology = GeoNames()
   ontology.load()
   data = ontology.extract()  # list of taxonomic relationships

   # Split the taxonomic relationships into train and test sets
   train_data, test_data = train_test_split(
       data,
       test_size=0.6,  # 60% of data used for testing
       random_state=42,
   )

Initialize Learner
~~~~~~~~~~~~~~~~~~

Before defining the learner, choose the ontology learning task to perform.
Available tasks have been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_.
The task IDs are: ``term-typing``, ``taxonomy-discovery``, ``non-taxonomic-re``.

.. code-block:: python

   from ontolearner import SBUNLPFewShotLearner

   task = "taxonomy-discovery"

Next, we configure the SBU-NLP Few-Shot learner using a Qwen model.
This learner performs in-context learning via an N × M batch prompting scheme over (parent, child) pairs.

.. code-block:: python

   llm_learner = SBUNLPFewShotLearner(
       # Model / decoding
       model_name="Qwen/Qwen2.5-0.5B-Instruct",
       try_4bit=True,              # use 4-bit if bitsandbytes + CUDA are available
       max_new_tokens=140,         # limit the length of the model's response (JSON output)
       max_input_tokens=1500,      # limit the total prompt length (context window)
       temperature=0.0,            # set to 0.0 for deterministic output
       top_p=1.0,

       # Grid settings (N × M prompts)
       n_train_chunks=7,           # N: split training examples into 7 chunks
       m_test_chunks=7,            # M: split test terms into 7 chunks (total 49 prompts)

       # Run controls
       limit_prompts=None,         # None runs all N × M prompts; set an int for a restricted run
       output_dir="./outputs/taskC_batches",  # dump per-prompt JSON results for debugging
   )

   # Load the underlying LLM and prepare it for few-shot taxonomy discovery
   llm_learner.load(llm_id=llm_learner.model_name)

   # Run the few-shot prompting over (parent, child) pairs
   predicts = llm_learner.predict(test_data, task=task)

   # Build gold-standard labels for evaluation
   truth = llm_learner.tasks_ground_truth_former(data=test_data, task=task)

   # Evaluate taxonomy discovery performance
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Pipeline Usage
~~~~~~~~~~~~~~

The :class:`LearnerPipeline` can also be used with :class:`SBUNLPFewShotLearner`
to run few-shot taxonomy-discovery experiments end-to-end. It constructs few-shot batches,
calls the LLM, aggregates predictions, and computes evaluation metrics.

.. code-block:: python

    # Import core modules from the OntoLearner library
    from ontolearner import GeoNames, train_test_split, LearnerPipeline

    # Import the specific Few-Shot Learner implementation
    from ontolearner.learner.taxonomy_discovery import SBUNLPFewShotLearner

    # Load ontology and split
    # Load the GeoNames ontology for taxonomy discovery.
    # GeoNames provides geographic parent-child relationships (is-a hierarchy).
    ontology = GeoNames()
    ontology.load()
    data = ontology.extract()  # Extract the list of taxonomic relationships from the ontology object

    # Split the taxonomic relationships into train and test sets
    train_data, test_data = train_test_split(
        data,
        test_size=0.6,  # 60% of data used for testing (terms to find relations for)
        random_state=42,
    )

    # Configure the learner with user-defined inference args + device
    # Configure the SBUNLP Few-Shot Learner using the Qwen model.
    # This performs in-context learning via N x M batch prompting.
    llm_learner = SBUNLPFewShotLearner(
        # Model / decoding
        model_name="Qwen/Qwen2.5-0.5B-Instruct",  # The Qwen model to load
        try_4bit=True,            # uses 4-bit if bitsandbytes + CUDA available for memory efficiency
        max_new_tokens=140,       # limit the length of the model's response (for JSON output)
        max_input_tokens=1500,    # limit the total prompt length (context window)
        temperature=0.0,          # deterministic output (best for structured JSON)
        top_p=1.0,                # top-p sampling disabled with temperature=0.0

        # Grid settings (N x M prompts)
        n_train_chunks=7,         # N: split training examples (few-shot context) into 7 chunks
        m_test_chunks=7,          # M: split test terms (vocabulary) into 7 chunks (total 49 prompts)

        # Run controls
        limit_prompts=None,       # None runs all N x M prompts; set to an integer for a dry-run
        output_dir="./outputs/taskC_batches",  # Optional: dump per-prompt JSON results for debugging
    )

    # Build pipeline and run
    pipe = LearnerPipeline(
        llm=llm_learner,
        llm_id=llm_learner.model_name,
        ontologizer_data=True,   # Let the learner flatten structured ontology objects via its tasks_* helpers
        device="auto",           # automatically select CUDA or CPU
    )

    # Run the full learning pipeline on the taxonomy-discovery task
    outputs = pipe(
        train_data=train_data,
        test_data=test_data,
        task="taxonomy-discovery",
        evaluate=True,
        ontologizer_data=True,
    )

    # Display the evaluation results
    print("Metrics:", outputs.get("metrics"))

    # Display total elapsed time for training + prediction + evaluation
    print("Elapsed time:", outputs["elapsed_time"])

    # Print all returned outputs (include predictions)
    print(outputs)
