Alexbek Learner
================

Description
-----------

.. sidebar:: Examples

   * Alexbek Learner Text2Onto Example: `llm_learner_alexbek_text2onto.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_alexbek_text2onto.py>`_
   * Alexbek Learner Term Typing Example: `llm_learner_alexbek_rf_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_alexbek_rf_term_typing.py>`_
   * Alexbek Learner Taxonomy Discovery Example: `llm_learner_alexbek_cross_attn_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_alexbek_cross_attn_taxonomy_discovery.py>`_

The team presented a comprehensive system for addressing Tasks A, B, and C of the LLMs4OL 2025 challenge, which together span the full ontology construction pipeline: term extraction, typing, and taxonomy discovery. Their approach combines retrieval-augmented prompting, zero-shot classification, and attention-based graph modeling — each tailored to the demands of the respective task.

For **Task A (Text2Onto)**, they jointly extract domain-specific terms and their ontological types using a retrieval-augmented generation (RAG) pipeline. Training data is reformulated into a correspondence between documents, terms, and types, while test-time inference leverages semantically similar training examples. This single-pass method requires no model fine-tuning and leverages lexical augmentation.

For **Task B (Term Typing)**, which involves assigning types to given terms, they adopt a dual strategy. In the few-shot setting (for domains with labeled training data), they reuse the RAG scheme with few-shot prompting. In the zero-shot or label-scarce setting, they use a classifier that combines cosine similarity scores from multiple embedding models using confidence-based weighting (e.g., via random forests or RAG-style retrieval).

For **Task C (Taxonomy Discovery)**, they model taxonomy discovery as graph inference. Using embeddings of type labels, they train a lightweight cross-attention layer to predict *is-a* relations by approximating a soft adjacency matrix.

**Datasets**

* **Task A – Text2Onto.** Domain corpora and annotations from the LLMs4OL Task A benchmark, covering ontology extraction in specialized domains.
* **Task B – Term Typing.** Labeled term–type pairs from ontology-based benchmarks (e.g., GeoNames-style ontologies) used to train and evaluate both RF-based and RAG-based term-typing models.
* **Task C – Taxonomy Discovery.** Hierarchical (parent–child) type graphs, such as those derived from GeoNames, providing edges for taxonomic relation prediction.

**Methodology**

1. **Retrieval-Augmented Text2Onto.** Training data is restructured into document–term–type correspondences. At inference time, the system retrieves semantically similar training examples and feeds them, together with the query document, into a small generative LLM to jointly predict candidate terms and their types.

2. **Hybrid Term Typing.**

   * **Random-Forest Variant.** Uses dense text embeddings (and optionally graph-based features from the ontology) as input to a random-forest classifier, producing multi-label type assignments per term.
   * **RAG-Based Variant.** Combines a bi-encoder retriever with a generative LLM: for each query term, top-*k* labeled examples are retrieved and concatenated into the prompt. The LLM then predicts types in a structured format (e.g., JSON), which are parsed and evaluated.

3. **Cross-Attention Taxonomy Discovery.** Type labels (or term representations) are embedded using a sentence-transformer model and passed through a lightweight cross-attention layer. The resulting network approximates a soft adjacency matrix over types and is trained to distinguish positive (true parent–child) from negative (corrupted) edges.


Term Typing (Random-Forest)
---------------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For term typing, we use GeoNames as an example ontology. Labeled term–type pairs are extracted and split into train and test sets.

.. code-block:: python

   from ontolearner import GeoNames, train_test_split, evaluation_report

   # Load the GeoNames ontology and extract labeled term-typing data
   ontology = GeoNames()
   ontology.load()
   data = ontology.extract()

   # Split the labeled term-typing data into train and test sets
   train_data, test_data = train_test_split(
       data,
       test_size=0.2,
       random_state=42,
   )

Initialize Learner
~~~~~~~~~~~~~~~~~~

Before defining the learner, choose the ontology learning task to perform.
Available tasks have been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_.
The task IDs are: ``term-typing``, ``taxonomy-discovery``, ``non-taxonomic-re``.

.. code-block:: python

   from ontolearner.learner.term_typing import AlexbekRFLearner

   task = "term-typing"

We first configure the Alexbek random-forest learner.
This learner builds features from text embeddings (and optionally graph structure) and trains a random-forest classifier for term typing.

.. code-block:: python

   rf_learner = AlexbekRFLearner(
       device="cpu",           # switch to "cuda" if available
       batch_size=16,
       max_length=512,         # max tokenizer length for embedding inputs
       threshold=0.30,         # probability cutoff for assigning each type
       use_graph_features=True # set False for pure text-based features
   )

   # Fit the RF-based learner on the training split
   rf_learner.fit(train_data, task=task)

   # Predict types for the held-out test terms
   predicts = rf_learner.predict(test_data, task=task)

   # Build gold labels and evaluate
   truth = rf_learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Pipeline Usage
~~~~~~~~~~~~~~

The :class:`LearnerPipeline` class integrates the random-forest term-typing learner with a retriever, runs training, and evaluates performance on the test split.

.. code-block:: python

   # Import core modules from the OntoLearner library
   from ontolearner import GeoNames, train_test_split, LearnerPipeline
   from ontolearner.learner.term_typing import AlexbekRFLearner  # RF learner over text+graph features

   # Load the GeoNames ontology and extract labeled term-typing data
   ontology = GeoNames()
   ontology.load()
   data = ontology.extract()

   # Split the labeled term-typing data into train and test sets
   train_data, test_data = train_test_split(
       data,
       test_size=0.2,
       random_state=42,
   )

   # Configure the RF-based learner (embeddings + optional graph features)
   rf_learner = AlexbekRFLearner(
       device="cpu",            # switch to "cuda" if you have a GPU
       batch_size=16,
       max_length=512,          # max tokenizer length for embedding model inputs
       threshold=0.30,          # probability cutoff for assigning each type
       use_graph_features=True, # set False for pure RF on text embeddings only
   )

   # Build the pipeline and pass raw structured objects end-to-end.
   pipe = LearnerPipeline(
       retriever=rf_learner,
       retriever_id="intfloat/e5-base-v2",  # or "Qwen/Qwen3-Embedding-4B" if you have sufficient GPU memory
       ontologizer_data=True,               # True if data is already {"term": ..., "types": [...], ...}
       device="cpu",
       batch_size=16,
   )

   # Run the full learning pipeline on the term-typing task
   outputs = pipe(
       train_data=train_data,
       test_data=test_data,
       task="term-typing",
       evaluate=True,
       ontologizer_data=True,
   )

   # Display evaluation summary and runtime
   print("Metrics:", outputs.get("metrics"))
   print("Elapsed time:", outputs["elapsed_time"])
   print(outputs)


Term Typing (RAG-based)
-----------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

The RAG-based term-typing setup also uses GeoNames. We again load the ontology and split labeled term–type instances into train and test sets.

.. code-block:: python

   from ontolearner import GeoNames, train_test_split, evaluation_report

   ontology = GeoNames()
   ontology.load()
   data = ontology.extract()

   # Extract labeled items and split into train/test sets for evaluation
   train_data, test_data = train_test_split(
       data,
       test_size=0.2,
       random_state=42,
   )

Initialize Learner
~~~~~~~~~~~~~~~~~~

Before defining the learner, choose the ontology learning task to perform.
Available tasks have been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_.
The task IDs are: ``term-typing``, ``taxonomy-discovery``, ``non-taxonomic-re``.

.. code-block:: python

   from ontolearner.learner.term_typing import AlexbekRAGLearner

   task = "term-typing"

Next, we configure a Retrieval-Augmented Generation (RAG) term-typing classifier.
An encoder retrieves top-k similar training examples, and a generative LLM predicts types conditioned on the query term plus retrieved examples.

.. code-block:: python

   rag_learner = AlexbekRAGLearner(
       llm_model_id="Qwen/Qwen2.5-0.5B-Instruct",
       retriever_model_id="sentence-transformers/all-MiniLM-L6-v2",
       device="cuda",      # or "cpu"
       top_k=3,
       max_new_tokens=256,
       output_dir="./results/",
   )

   # Load the underlying LLM and retriever for RAG-based term typing
   rag_learner.load(llm_id=rag_learner.llm_model_id)

   # Index the training data for retrieval and prepare prompts
   rag_learner.fit(train_data, task=task)

   # Predict types for the held-out test terms
   predicts = rag_learner.predict(test_data, task=task)

   # Build gold labels and evaluate
   truth = rag_learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Pipeline Usage
~~~~~~~~~~~~~~

We place the RAG learner in the ``llm`` slot of :class:`LearnerPipeline`.
The pipeline handles retrieval, LLM calls, and evaluation end-to-end.

.. code-block:: python

    # Import core modules from the OntoLearner library
    from ontolearner import GeoNames, train_test_split, LearnerPipeline
    from ontolearner.learner.term_typing import AlexbekRAGLearner

    # Load the GeoNames ontology.
    ontology = GeoNames()
    ontology.load()

    # Extract labeled items and split into train/test sets for evaluation
    train_data, test_data = train_test_split(
        ontology.extract(),
        test_size=0.2,
        random_state=42,
    )

    # Configure a Retrieval-Augmented Generation (RAG) term-typing classifier.
    rag_learner = AlexbekRAGLearner(
        llm_model_id="Qwen/Qwen2.5-0.5B-Instruct",
        retriever_model_id="sentence-transformers/all-MiniLM-L6-v2",
        device="cuda",
        top_k=3,
        max_new_tokens=256,
        output_dir="./results/",
    )

    # Build the pipeline and pass raw structured objects end-to-end.
    pipe = LearnerPipeline(
        llm=rag_learner,
        llm_id="Qwen/Qwen2.5-0.5B-Instruct",
        ontologizer_data=True,
    )

    # Run the full learning pipeline on the term-typing task
    outputs = pipe(
        train_data=train_data,
        test_data=test_data,
        task="term-typing",
        evaluate=True,
        ontologizer_data=True,
    )

    # Display the evaluation results and runtime
    print("Metrics:", outputs.get("metrics"))  # e.g., {'precision': ..., 'recall': ..., 'f1_micro': ..., ...}
    print("Elapsed time (s):", outputs.get("elapsed_time"))


Taxonomy Discovery
------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For taxonomy discovery, we again use the GeoNames ontology. It exposes parent–child relations that can be embedded and fed to a cross-attention model.

.. code-block:: python

   from ontolearner import GeoNames, train_test_split, evaluation_report

   ontology = GeoNames()
   ontology.load()
   data = ontology.extract()

   train_data, test_data = train_test_split(
       data,
       test_size=0.2,
       random_state=42,
   )

Initialize Learner
~~~~~~~~~~~~~~~~~~

Before defining the learner, choose the ontology learning task to perform.
Available tasks have been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_.
The task IDs are: ``term-typing``, ``taxonomy-discovery``, ``non-taxonomic-re``.

.. code-block:: python

   from ontolearner import AlexbekCrossAttnLearner

   task = "taxonomy-discovery"

Next, we configure the Alexbek cross-attention learner.
It uses embeddings of type labels and a lightweight cross-attention layer to predict *is-a* relations.

.. code-block:: python

   cross_learner = AlexbekCrossAttnLearner(
       embedding_model="sentence-transformers/all-MiniLM-L6-v2",
       device="cpu",
       num_heads=8,
       lr=5e-5,
       weight_decay=0.01,
       num_epochs=1,
       batch_size=256,
       neg_ratio=1.0,
       output_dir="./results/crossattn/",
       seed=42,
   )

   # Train the cross-attention model on taxonomic edges
   cross_learner.fit(train_data, task=task)

   # Predict taxonomic relations on the test set
   predicts = cross_learner.predict(test_data, task=task)

   # Build gold labels and evaluate
   truth = cross_learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Pipeline Usage
~~~~~~~~~~~~~~

Here, :class:`LearnerPipeline` trains the cross-attention model on train edges, predicts taxonomic relations on the test set, and reports evaluation metrics.

.. code-block:: python

   from ontolearner import GeoNames, train_test_split, LearnerPipeline
   from ontolearner.learner.taxonomy_discovery import AlexbekCrossAttnLearner

   # Load & split
   ontology = GeoNames()
   ontology.load()
   data = ontology.extract()
   train_data, test_data = train_test_split(
       data,
       test_size=0.2,
       random_state=42,
   )

   # Configure the cross-attention learner
   cross_learner = AlexbekCrossAttnLearner(
       embedding_model="sentence-transformers/all-MiniLM-L6-v2",
       device="cpu",
       num_heads=8,
       lr=5e-5,
       weight_decay=0.01,
       num_epochs=1,
       batch_size=256,
       neg_ratio=1.0,
       output_dir="./results/crossattn/",
       seed=42,
   )

   # Build pipeline
   pipeline = LearnerPipeline(
       llm=cross_learner,    # cross-attention learner
       llm_id="cross-attn",  # label for bookkeeping
       ontologizer_data=False,
   )

   # Train + predict + evaluate
   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       task="taxonomy-discovery",
       evaluate=True,
       ontologizer_data=False,
   )

   print("Metrics:", outputs.get("metrics"))
   print("Elapsed time:", outputs["elapsed_time"])
   print(outputs)
