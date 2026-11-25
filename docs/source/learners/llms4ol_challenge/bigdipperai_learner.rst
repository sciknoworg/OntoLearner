
BigDipperAI Learner
===================

.. sidebar:: BigDipperAI Learner Example

   * Ontology Construction: `llm_learner_bigdipperai_construction.py <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/llm_learner_bigdipperai_construction.py>`_


The **BigDipperAI** team participated in the LLMs4OL 2026 Challenge, addressing **Ontology Construction** (Flagship Task A). Their approach combines schema-aligned auxiliary supervision, relation-aware weighted four-bit QLoRA, and structured ontology triple generation. The system fine-tunes ``Qwen3-8B`` using ontology construction data supplemented with Ontology Expansion (Reuse Task B) training records converted into a common schema. During inference, the model generates primitive ontology triples directly from unstructured text, followed by deterministic output recovery, training-supported graph completion, candidate selection, and structural validation.

.. note::

   Read more about the model at `BigDipperAI at LLMs4OL 2026 Task Flagship: Structured Generation of Primitive Ontology Triples with Schema-Aligned Auxiliary Supervision <https://www.tib-op.org/ojs/index.php/ocp/article/view/3657>`_.

.. hint::

   The original implementation is available in the `BigDipperAI GitHub repository <https://github.com/Qiaoyu1332/BigDipperAI-LLMs4OL-2026>`_.

   The OntoLearner-integrated implementation is available in `BigDipperAIPrimitiveLearner <https://github.com/sciknoworg/OntoLearner/blob/dev/ontolearner/learner/primitive/bigdipperai.py>`_.


Overview
---------------------------------

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/refs/heads/dev/docs/source/learners/images/bigdipperai-learner.png" alt="BigDipperAI Learner" width="90%"/>
   </div>
   <br>

The BigDipperAI methodology consists of three main stages: **model adaptation**, **direct generation**, and **output processing**. The model adaptation stage combines ontology construction and auxiliary expansion training data to prepare the language model for structured ontology learning. During direct generation, the adapted model extracts candidate ontology triples from raw text. Finally, the output processing stage recovers, refines, and validates the generated triples to produce the required structured output.

Methodological Summary:

1. **Schema-Aligned Auxiliary Supervision.** Ontology Construction training records are combined with Ontology Expansion records converted into the construction schema. The initial and extended ontology triples are merged, filtered against supported relation types, and deduplicated to provide additional labeled training examples.

2. **Relation-Aware Weighted QLoRA.** The system fine-tunes ``Qwen3-8B`` using four-bit QLoRA with relation-aware loss weighting. Training examples containing ``instance-of`` and ``type`` relations receive higher weights to account for differences in relation frequencies. The model learns to generate ontology triples in a structured JSON format.

3. **Structured Generation and Post-Processing.** During prediction, the adapted model generates primitive ontology triples from textual context using task-specific prompts and greedy decoding. Generated outputs undergo JSON recovery, relation normalization, and validation. A training-derived graph index provides additional self-relation candidates, which are combined with model predictions through score-based filtering and duplicate removal.

Data Preparation
----------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

The example uses the FOAF ontology as a running example. Its taxonomic relations are split into training and test sets before synthetic documents are generated.

.. code-block:: python

   from ontolearner import train_test_split
   from ontolearner.ontology import FOAF

   # Load the FOAF ontology and extract ontological data
   ontology = FOAF()
   ontology.load()
   ontological_data = ontology.extract()

   # Select taxonomic relations for synthetic document generation
   ontological_data.term_typings = []
   ontological_data.type_non_taxonomic_relations.non_taxonomies = []

   # Split the ontology into training and test sets
   train_ontology, test_ontology = train_test_split(
       ontological_data,
       test_size=0.5,
       random_state=42,
   )

Generating Documents
~~~~~~~~~~~~~~~~~~~~

Use ``SyntheticGenerator`` for the two ontology partitions. In this example, synthetic-data extraction uses ``gpt-4o-mini`` through an API, while BigDipperAI uses ``Qwen3-8B`` locally for ontology construction.

.. code-block:: python

   from openai import OpenAI
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

   # Configure the synthetic document generator
   api_key = = "OPENAI_API_KEY"
   generator = SyntheticGenerator(
       model_id="Qwen/Qwen2.5-0.5B-Instruct",
       token="hf_token",
       extraction_method="openai",
       openai_api_key=api_key,
       openai_model="gpt-4o-mini",
       batch_size=5,
       generation_batch_size=2,
       min_pseudo_sentences=1,
       max_input_length=2000,
       max_new_tokens=2000,
   )

   # Generate documents for the training and test ontology splits
   train_synthetic = generator.generate(ontological_data=train_ontology, topic=ontology.domain)
   test_synthetic = generator.generate(ontological_data=test_ontology, topic=ontology.domain)

Preprocessing
~~~~~~~~~~~~~

For Ontology Construction, preprocess the generated documents into labeled samples containing textual context and reference ``primitive-ontology-triples``. See `Text2Onto <https://ontolearner.readthedocs.io/learning_tasks/text2onto.html>`_ for details.

.. code-block:: python

   # Select the primitive ontology learning task
   task = "ontology_construction"

   preprocessor = SyntheticDataPreprocessor(
       client=OpenAI(api_key=api_key),
       task=task,
       random_state=42,
   )

   # Preprocess training and test documents
   train_data = preprocessor.preprocess(train_synthetic, train_ontology)
   test_data = preprocessor.preprocess(test_synthetic, test_ontology)

   print("Train samples:", len(train_data))
   print("Test samples:", len(test_data))

.. note::

   * See the `Text2Onto Construction Example <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/text2onto_construction.py>`_ for the complete data preparation workflow.
   * Optional auxiliary training samples can be prepared with the `Text2Onto Expansion Example <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/text2onto_expansion.py>`_.
   * Consider using a different ontology to diversify training examples and avoid overlap with the construction data.

Ontology Construction
---------------------

Initialize Learner
~~~~~~~~~~~~~~~~~~

Choose ``task="ontology_construction"`` in the preprocessing step. The learner uses relation-weighted QLoRA to adapt the language model and training-derived graph completion to predict ontology triples.

.. code-block:: python

   from ontolearner.learner.primitive import BigDipperAIPrimitiveLearner

   task = "ontology_construction"
   auxiliary_data = None  # Optional labeled ontology expansion training samples

   # Initialize the BigDipperAI primitive ontology learner
   learner = BigDipperAIPrimitiveLearner(
       model_id="Qwen/Qwen3-8B",
       auxiliary_data=auxiliary_data,
       device="cuda",
       train_adapter=True,
       output_dir="./results/bigdipperai",
       max_input_tokens=3072,
       max_output_tokens=1536,
       retry_output_tokens=3072,
   )

.. note::

   * With ``train_adapter=True``, fitting requires a CUDA GPU and enough labeled construction samples to form a development split.
   * For a lightweight test, use a smaller model with ``train_adapter=False`` and call ``learner.load()`` before fitting.

Learn and Predict
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Train and load the QLoRA adapter
   learner.fit(train_data, task=task)

   # Predict primitive ontology triples
   predicts = learner.predict(test_data, task=task)

   print(predicts)

The predictions contain the sample ``id`` and the generated ``primitive-ontology-triples`` for each input document.

Pipeline Usage
--------------

Alternatively, use ``LearnerPipeline`` to fit, predict, and evaluate Ontology Construction in a single call. Initialize the learner as shown above and use the corresponding preprocessed data.

.. code-block:: python

   from ontolearner import LearnerPipeline

   # Initialize the pipeline
   pipeline = LearnerPipeline(
       llm=learner,
       llm_id=learner.model_id,
   )

   # Train, predict, and evaluate
   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       task=task,
       evaluate=True,
   )

   print("Predictions:", outputs["predictions"])
   print("Metrics:", outputs["metrics"])

.. hint::

   For additional methods and configuration options, see :class:`~ontolearner.learner.primitive.bigdipperai.BigDipperAIPrimitiveLearner` in the Package Reference.
