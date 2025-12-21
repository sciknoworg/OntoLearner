Alexbek Learner
================

.. sidebar:: Alexbek Learner Examples

   * Text2Onto: `llm_learner_alexbek_text2onto.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_alexbek_text2onto.py>`_
   * Term Typing: `llm_learner_alexbek_rf_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_alexbek_rf_term_typing.py>`_
   * Taxonomy Discovery: `llm_learner_alexbek_cross_attn_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_alexbek_cross_attn_taxonomy_discovery.py>`_

The team presented a comprehensive system for addressing Tasks A, B, and C of the LLMs4OL 2025 challenge, which together span the full ontology construction pipeline: term extraction, typing, and taxonomy discovery. Their approach combines retrieval-augmented prompting, zero-shot classification, and attention-based graph modeling — each tailored to the demands of the respective task.

.. note::

	Read more about the model at `Alexbek at LLMs4OL 2025 Tasks A, B, and C: Heterogeneous LLM Methods for Ontology Learning (Few-Shot Prompting, Ensemble Typing, and Attention-Based Taxonomies) <https://www.tib-op.org/ojs/index.php/ocp/article/view/2899>`_.

.. hint::

	The original implementation is available at `https://github.com/BelyaevaAlex/LLMs4OL-Challenge-Alexbek <https://github.com/BelyaevaAlex/LLMs4OL-Challenge-Alexbek>`_ repository.

Overview
---------------------------------

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/refs/heads/dev/docs/source/learners/images/alexbek-learner.png" alt="Alexbek Team" width="90%"/>
   </div>
   <br>

For **Task A (Text2Onto)**, they jointly extract domain-specific terms and their ontological types using a retrieval-augmented generation (RAG) pipeline. Training data is reformulated into a correspondence between documents, terms, and types, while test-time inference leverages semantically similar training examples. This single-pass method requires no model fine-tuning and leverages lexical augmentation. For **Task B (Term Typing)**, which involves assigning types to given terms, they adopt a dual strategy. In the few-shot setting (for domains with labeled training data), they reuse the RAG scheme with few-shot prompting. In the zero-shot or label-scarce setting, they use a classifier that combines cosine similarity scores from multiple embedding models using confidence-based weighting (e.g., via random forests or RAG-style retrieval). For **Task C (Taxonomy Discovery)**, they model taxonomy discovery as graph inference. Using embeddings of type labels, they train a lightweight cross-attention layer to predict *is-a* relations by approximating a soft adjacency matrix.

Methodological Summary:

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

   from ontolearner import GeoNames, train_test_split

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

   task = "term-typing"

We first configure the Alexbek random-forest learner.
This learner builds features from text embeddings (and optionally graph structure) and trains a random-forest classifier for term typing.

.. code-block:: python

   from ontolearner.learner.term_typing import AlexbekRFLearner

   rf_learner = AlexbekRFLearner(
       device="cpu",           # switch to "cuda" if available
       batch_size=16,
       max_length=512,         # max tokenizer length for embedding inputs
       threshold=0.30,         # probability cutoff for assigning each type
       use_graph_features=True # set False for pure text-based features
   )

Learn and Predict
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner import evaluation_report
   # Fit the RF-based learner on the training split
   rf_learner.fit(train_data, task=task)

   # Predict types for the held-out test terms
   predicts = rf_learner.predict(test_data, task=task)

   # Build gold labels and evaluate
   truth = rf_learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Term Typing (RAG-based)
-----------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

The RAG-based term-typing setup also uses GeoNames. We again load the ontology and split labeled term–type instances into train and test sets.

.. code-block:: python

   from ontolearner import GeoNames, train_test_split

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

   task = "term-typing"

Next, we configure a Retrieval-Augmented Generation (RAG) term-typing classifier.
An encoder retrieves top-k similar training examples, and a generative LLM predicts types conditioned on the query term plus retrieved examples.

.. code-block:: python

   from ontolearner.learner.term_typing import AlexbekRAGLearner

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

Learn and Predict
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner import evaluation_report

   # Index the training data for retrieval and prepare prompts
   rag_learner.fit(train_data, task=task)

   # Predict types for the held-out test terms
   predicts = rag_learner.predict(test_data, task=task)

   # Build gold labels and evaluate
   truth = rag_learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)


Taxonomy Discovery
------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For taxonomy discovery, we again use the GeoNames ontology. It exposes parent–child relations that can be embedded and fed to a cross-attention model.

.. code-block:: python

   from ontolearner import GeoNames, train_test_split

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

   task = "taxonomy-discovery"

Next, we configure the Alexbek cross-attention learner.
It uses embeddings of type labels and a lightweight cross-attention layer to predict *is-a* relations.

.. code-block:: python

   from ontolearner import AlexbekCrossAttnLearner

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

Learn and Predict
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner import evaluation_report

   # Train the cross-attention model on taxonomic edges
   cross_learner.fit(train_data, task=task)

   # Predict taxonomic relations on the test set
   predicts = cross_learner.predict(test_data, task=task)

   # Build gold labels and evaluate
   truth = cross_learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Text2Onto
------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~

For the Text2Onto task, we load an ontology (via ``OM``), extract its structured content, and then generate synthetic pseudo-sentences using an LLM-backed generator (DSPy + Ollama in this example).

.. code-block:: python

   import os
   import dspy

   # Ontology loader/manager
   from ontolearner.ontology import OM

   # Text2Onto utilities: synthetic generation + dataset splitting
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataSplitter

   # ---- DSPy -> Ollama (LiteLLM-style) ----
   LLM_MODEL_ID = "ollama/llama3.2:3b"      # use your pulled Ollama model
   LLM_API_KEY  = "NA"                      # local Ollama doesn't use a key
   LLM_BASE_URL = "http://localhost:11434"  # default Ollama endpoint

   dspy_llm = dspy.LM(
       model=LLM_MODEL_ID,
       cache=True,
       max_tokens=4000,
       temperature=0,
       api_key=LLM_API_KEY,
       base_url=LLM_BASE_URL,
   )
   dspy.configure(lm=dspy_llm)

   # ---- Synthetic generation configuration ----
   pseudo_sentence_batch_size = int(os.getenv("TEXT2ONTO_BATCH", "10"))
   max_worker_count_for_llm_calls = int(os.getenv("TEXT2ONTO_WORKERS", "1"))

   text2onto_synthetic_generator = SyntheticGenerator(
       batch_size=pseudo_sentence_batch_size,
       worker_count=max_worker_count_for_llm_calls,
   )

   # ---- Load ontology and extract structured data ----
   ontology = OM()
   ontology.load()
   ontological_data = ontology.extract()

   print(f"term types: {len(ontological_data.term_typings)}")
   print(f"taxonomic relations: {len(ontological_data.type_taxonomies.taxonomies)}")
   print(f"non-taxonomic relations: {len(ontological_data.type_non_taxonomic_relations.non_taxonomies)}")

   # ---- Generate synthetic Text2Onto samples ----
   synthetic_data = text2onto_synthetic_generator.generate(
       ontological_data=ontological_data,
       topic=ontology.domain,
   )

Split Synthetic Data
~~~~~~~~~~~~~~~~~~~~

We split the synthetic dataset into train/val/test sets using ``SyntheticDataSplitter``.
Each split is a dict with keys:

- ``documents``
- ``terms``
- ``types``
- ``terms2docs``
- ``terms2types``

.. code-block:: python

   splitter = SyntheticDataSplitter(
       synthetic_data=synthetic_data,
       onto_name=ontology.ontology_id,
   )

   train_data, val_data, test_data = splitter.train_test_val_split(
       train=0.8,
       val=0.0,
       test=0.2,
   )

   print("TRAIN sizes:")
   print("  documents:", len(train_data.get("documents", [])))
   print("  terms:", len(train_data.get("terms", [])))
   print("  types:", len(train_data.get("types", [])))
   print("  terms2docs:", len(train_data.get("terms2docs", {})))
   print("  terms2types:", len(train_data.get("terms2types", {})))

   print("TEST sizes:")
   print("  documents:", len(test_data.get("documents", [])))
   print("  terms:", len(test_data.get("terms", [])))
   print("  types:", len(test_data.get("types", [])))
   print("  terms2docs:", len(test_data.get("terms2docs", {})))
   print("  terms2types:", len(test_data.get("terms2types", {})))

Initialize Learner
~~~~~~~~~~~~~~~~~~

We configure a retrieval-augmented few-shot learner for the Text2Onto task.
The learner retrieves relevant synthetic examples and uses an LLM to predict structured outputs.

.. code-block:: python

   from ontolearner.learner.text2onto import AlexbekRAGFewShotLearner

   text2onto_learner = AlexbekRAGFewShotLearner(
       llm_model_id="Qwen/Qwen2.5-0.5B-Instruct",
       retriever_model_id="sentence-transformers/all-MiniLM-L6-v2",
       device="cpu",          # set "cuda" if available
       top_k=3,
       max_new_tokens=256,
       use_tfidf=True,
   )

Learn and Predict
~~~~~~~~~~~~~~~~~

We run the end-to-end pipeline (train -> predict -> evaluate) with ``LearnerPipeline`` using the ``text2onto`` task id.

.. code-block:: python

   from ontolearner import LearnerPipeline

   task = "text2onto"

   pipe = LearnerPipeline(
       llm=text2onto_learner,
       llm_id="Qwen/Qwen2.5-0.5B-Instruct",
       ontologizer_data=False,
   )

   outputs = pipe(
       train_data=train_data,
       test_data=test_data,
       task=task,
       evaluate=True,
       ontologizer_data=False,
   )

   print("Metrics:", outputs.get("metrics"))
   print("Elapsed time:", outputs.get("elapsed_time"))
