
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

Ontology Construction
---------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For ontology construction, we use the FOAF ontology as a running example. The ontology is loaded, and its taxonomic relations are split into training and test sets.

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

Synthetic Document Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ontology splits are used to generate synthetic textual documents through ``SyntheticGenerator``. The generated documents are subsequently processed using ``SyntheticDataPreprocessor`` to prepare training and test samples for ontology construction.

.. code-block:: python

   import os
   from openai import OpenAI
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

   # Configure the synthetic document generator
   model_id = os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct")
   api_key = os.getenv("OPENAI_API_KEY")
   hf_token = os.getenv("HF_TOKEN", "")

   generator = SyntheticGenerator(
       model_id=model_id,
       token=hf_token,
       extraction_method="openai",
       openai_api_key=api_key,
       openai_model="gpt-4o-mini",
       batch_size=5,
       generation_batch_size=2,
       min_pseudo_sentences=1,
       max_input_length=2000,
       max_new_tokens=2000,
   )

   # Generate synthetic documents from the ontology splits
   train_synthetic = generator.generate(ontological_data=train_ontology, topic=ontology.domain)
   test_synthetic = generator.generate(ontological_data=test_ontology, topic=ontology.domain)

   # Initialize the construction data preprocessor
   preprocessor = SyntheticDataPreprocessor(
       client=OpenAI(api_key=api_key),
       task="ontology_construction",
       random_state=42,
   )

   # Prepare labeled construction samples for fitting and evaluation
   train_data = preprocessor.preprocess(train_synthetic, train_ontology)
   test_data = preprocessor.preprocess(test_synthetic, test_ontology)


.. note::

   See the `Text2Onto Construction Example <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/text2onto_construction.py>`_ for the complete synthetic document generation and preprocessing workflow.

   * The prepared ``train_data`` and ``test_data`` contain textual context and reference ontology triples.
   * The OpenAI backend is used for synthetic data preparation, while BigDipperAI uses locally loaded models for ontology inference.

Initialize Learner
~~~~~~~~~~~~~~~~~~

Before defining the learner, choose the primitive ontology learning task. Available tasks have been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_. The task ID supported by ``BigDipperAIPrimitiveLearner`` is ``ontology_construction``.

.. code-block:: python

   task = "ontology_construction"

Next, we initialize ``BigDipperAIPrimitiveLearner``, which extends OntoLearner's ``PrimitiveOntologyLearner`` interface. The learner uses relation-aware weighted QLoRA to adapt the language model and prepares a graph index from the training annotations for ontology prediction.

.. code-block:: python

   from ontolearner.learner.primitive import BigDipperAIPrimitiveLearner

   # Optional auxiliary ontology expansion training samples
   auxiliary_data = None

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


With ``train_adapter=True``, fitting performs relation-aware weighted QLoRA fine-tuning and automatically loads the saved adapter for inference. No separate ``load()`` call is required.

.. note::

   BigDipperAI supports auxiliary Ontology Expansion training data through ``auxiliary_data``.

   * See the `Text2Onto Expansion Example <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/text2onto_expansion.py>`_ to prepare expansion samples.
   * For more diverse auxiliary supervision, consider using a different ontology, such as ``OM`` or ``AgrO``, instead of reusing ``FOAF`` from the construction training data.


Learn and Predict
~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Fine-tune and automatically load the trained adapter
    learner.fit(train_data, task=task)

    # Predict using the trained adapter
    predicts = learner.predict(test_data, task=task)


The predictions contain the sample ``id`` and the generated ``primitive-ontology-triples`` for each input document.

Pipeline Usage
~~~~~~~~~~~~~~

The ``BigDipperAIPrimitiveLearner`` can also be used through OntoLearner's ``LearnerPipeline`` to perform fitting, prediction, and evaluation in a single call.

.. code-block:: python

   from ontolearner import LearnerPipeline

   # Initialize the learner pipeline
   pipeline = LearnerPipeline(
       llm=learner,
       llm_id=learner.model_id,
       ontologizer_data=True,
   )

   # Fit, predict, and evaluate ontology construction
   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       task=task,
       evaluate=True,
       ontologizer_data=True,
   )

