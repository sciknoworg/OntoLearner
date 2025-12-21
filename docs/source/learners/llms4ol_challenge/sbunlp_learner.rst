SBU-NLP Learner
================


.. sidebar:: SBU-NLP Learner Examples

   * Text2Onto: `llm_learner_sbunlp_text2onto.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_sbunlp_text2onto.py>`_
   * Term Typing (Zero-Shot): `llm_learner_sbunlp_zs_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_sbunlp_zs_term_typing.py>`_
   * Taxonomy Discovery (Few-shot): `llm_learner_sbunlp_fs_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_sbunlp_fs_taxonomy_discovery.py>`_

The team participated in the LLMs4OL 2025 Shared Task, which included four subtasks: (A) Ontological term and type extraction (Text2Onto), (B) Term typing (Term Typing), (C) Taxonomy discovery (Taxonomy Discovery).


.. note::

	Read more about the model at `SBU-NLP at LLMs4OL 2025 Tasks A, B, and C: Stage-Wise Ontology Construction Through LLMs Without any Training Procedure <https://www.tib-op.org/ojs/index.php/ocp/article/view/2887>`_.

.. hint::

	The original implementation is available at `https://github.com/rarahnamoun/LLMs4OL-Challenge-ISWC-2025 <https://github.com/rarahnamoun/LLMs4OL-Challenge-ISWC-2025>`_ repository.



Overview
---------------------------------
The team focused on Tasks A, B, and C, adopting a unified prompting-based methodology that required no supervised training or fine-tuning. Instead, they applied prompt engineering combined with stratified and simple random sampling, as well as chunking-based strategies, to incorporate representative examples within the context window.

Methodological Summary:

- For **Term Typing**, the problem was framed as zero-shot label selection over an ontology-specific type inventory. The type inventory was derived from the training split, and Qwen-based LLMs were prompted to assign one or more valid type labels to each term without any parameter fine-tuning. Stratified sampling and prompt chunking were used to expose representative type examples within the context window while keeping prompts compact and model-agnostic.

- For **Taxonomy Discovery**, the focus was on detecting parent–child relationships between ontology terms. Due to the relational nature of this task, batch prompting was employed to efficiently handle multiple type pairs per inference, enabling the model to consider several candidate relations jointly.

- For **Text2Onto**, the objective was to extract ontology construction signals from text-like inputs: generating/using documents, identifying candidate terms, assigning types, and producing supporting mappings such as term–document and term–type associations. In OntoLearner, this is implemented by first generating synthetic pseudo-documents from an ontology (using an LLM-backed synthetic generator), then applying the SBU-NLP prompting strategy to infer structured outputs without any fine-tuning. Dataset splitting and optional Ontologizer-style processing are used to support reproducible evaluation and artifact generation.

Term Typing
-----------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For term typing (Task B), we use the AgrO ontology. Terms and their labels are split into train and test sets; the train split is used to derive the type inventory, while the test split is used for evaluation.

.. code-block:: python

   from ontolearner import AgrO, train_test_split

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

   task = "term-typing"

Next, we configure the SBU-NLP Zero-Shot learner for term typing, using a Qwen model.
The learner's ``fit`` phase infers the inventory of allowed type labels; the model itself is never fine-tuned.

.. code-block:: python

   from ontolearner import SBUNLPZSLearner

   llm_learner = SBUNLPZSLearner(
       # Model / decoding
       model_id="Qwen/Qwen2.5-0.5B-Instruct",
       max_new_tokens=64,  # sufficient length for JSON list of types
       temperature=0.0,    # deterministic (greedy) output
       # token=None,       # assuming public model access
   )

   # Load the underlying LLM and prepare it for zero-shot term typing
   llm_learner.load(llm_id=llm_learner.model_id)

Learn and Predict
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner import evaluation_report

   # Learn the type inventory from the training split
   llm_learner.fit(train_data, task=task)

   # Predict types for the held-out test terms
   predicts = llm_learner.predict(test_data, task=task)
   truth = llm_learner.tasks_ground_truth_former(data=test_data, task=task)

   # Evaluate zero-shot term typing performance
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Taxonomy Discovery
-----------------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For taxonomy discovery (Task C), we use the GeoNames ontology as an example. It provides geographic parent–child relations (an *is-a* hierarchy) that can be split into train and test sets.

.. code-block:: python

   from ontolearner import GeoNames, train_test_split

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

   task = "taxonomy-discovery"

Next, we configure the SBU-NLP Few-Shot learner using a Qwen model.
This learner performs in-context learning via an N × M batch prompting scheme over (parent, child) pairs.

.. code-block:: python

   from ontolearner import SBUNLPFewShotLearner

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

Learn and Predict
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner import evaluation_report

   # Run the few-shot prompting over (parent, child) pairs
   predicts = llm_learner.predict(test_data, task=task)

   # Build gold-standard labels for evaluation
   truth = llm_learner.tasks_ground_truth_former(data=test_data, task=task)

   # Evaluate taxonomy discovery performance
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Text2Onto
------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~

For the Text2Onto task, we load an ontology (via ``OM``), extract its structured content, and generate synthetic pseudo-sentences using an LLM-backed generator (DSPy + Ollama in this example).

.. code-block:: python

   import os
   import dspy

   # Import ontology loader/manager and Text2Onto utilities
   from ontolearner.ontology import OM
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataSplitter

   # ---- DSPy -> Ollama (LiteLLM-style) ----
   LLM_MODEL_ID = "ollama/llama3.2:3b"
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
   batch_size = int(os.getenv("TEXT2ONTO_BATCH", "10"))
   worker_count = int(os.getenv("TEXT2ONTO_WORKERS", "1"))

   text2onto_synthetic_generator = SyntheticGenerator(
       batch_size=batch_size,
       worker_count=worker_count,
   )

   # ---- Load ontology and extract structured data ----
   ontology = OM()
   ontology.load()
   ontological_data = ontology.extract()

   # Optional sanity checks to verify what was extracted from the ontology
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

We configure the SBU-NLP few-shot learner for the Text2Onto task.
This learner uses an LLM to produce predictions from the synthetic Text2Onto-style samples.

.. code-block:: python

   from ontolearner.learner.text2onto import SBUNLPFewShotLearner

   text2onto_learner = SBUNLPFewShotLearner(
       llm_model_id="Qwen/Qwen2.5-0.5B-Instruct",
       device="cpu",            # set "cuda" if available
       max_new_tokens=256,
       output_dir="./results/",
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
       ontologizer_data=True,
   )

   print("Metrics:", outputs.get("metrics"))
   print("Elapsed time:", outputs.get("elapsed_time"))

   # Print all returned outputs (often includes predictions/artifacts/logs)
   print(outputs)
