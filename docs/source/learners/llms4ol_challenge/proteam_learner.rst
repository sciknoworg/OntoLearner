
ProTeam Learner
===============

.. sidebar:: ProTeam Learner Examples

   * Ontology Construction: `llm_learner_proteam_construction.py <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/llm_learner_proteam_construction.py>`_
   * Ontology Expansion: `llm_learner_proteam_expansion.py <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/llm_learner_proteam_expansion.py>`_

The **pro-team** participated in the LLMs4OL 2026 Challenge, addressing two ontology learning tasks: **Ontology Construction** (Flagship Task A) and **Ontology Expansion** (Reuse Task B). Their approach employs an offline Retrieval-Augmented Generation (RAG) framework with few-shot prompting to construct primitive ontologies from unstructured text and extend existing ontologies with new relationships. The system combines ``Qwen2.5-14B-Instruct`` for ontology generation with ``sentence-transformers/all-MiniLM-L6-v2`` for semantic retrieval. For ontology expansion, the approach additionally integrates proximity-based term typing and vocabulary-constrained filtering to improve the consistency of generated ontology triples with the provided vocabulary and initial ontology.

.. note::

   Read more about the methodology in `pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: Retrieval-Augmented Generation and Vocabulary-Constrained Filtering for Ontology Learning <https://www.tib-op.org/ojs/index.php/ocp/article/view/3663>`_.

.. hint::

   * The original implementation is available in the `ProTeam GitHub repository <https://github.com/shivam07041/team-pro-integration_OntoLearner_Submission>`_.
   * The OntoLearner-integrated implementation is available in `ProTeamPrimitiveLearner <https://github.com/sciknoworg/OntoLearner/blob/dev/ontolearner/learner/primitive/proteam.py>`_.

Overview
---------------------------------

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/dev/docs/source/learners/images/proteam-learner.png" alt="ProTeam Learner" width="40%"/>
   </div>
   <br>

The ProTeam methodology follows an offline Retrieval-Augmented Generation (RAG) workflow for primitive ontology learning. Input documents are embedded to retrieve semantically similar training examples, which are incorporated into few-shot prompts for ontology triple generation. Generated triples undergo parsing and post-processing before being returned in the required JSON format, with additional proximity-based term typing and vocabulary-constrained filtering for Ontology Expansion.

Methodological Summary:

1. **Retrieval-Augmented Ontology Generation.** During fitting, labeled training documents are encoded using ``sentence-transformers/all-MiniLM-L6-v2`` to prepare embeddings for semantic retrieval. During prediction, similar examples are retrieved using cosine similarity and incorporated into task-specific few-shot prompts. The ``Qwen2.5-14B-Instruct`` model then generates structured ontology triples in JSON format without fine-tuning.

2. **Task-Specific Ontology Learning.**

   * **Ontology Construction.** The system generates primitive ontology triples directly from textual documents without an initial ontology or predefined vocabulary, using the top-5 retrieved examples as demonstrations.

   * **Ontology Expansion.** The system extends an existing ontology using textual context, initial triples, terms, and types, with the top-2 retrieved examples. A proximity-based heuristic additionally generates ``instance-of`` relations from terms and types occurring within the same sentence.

3. **Triple Parsing and Post-Processing.** Generated outputs are parsed using JSON and regular-expression fallbacks, followed by normalization and duplicate removal. For ontology expansion, vocabulary-constrained filtering retains triples with at least one endpoint in the known vocabulary and excludes relationships already present in the initial ontology.

Data Preparation
----------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

The examples use the FOAF ontology as a running example. Its taxonomic relations are split into training and test sets before synthetic documents are generated.

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

Use ``SyntheticGenerator`` for the two ontology partitions. In this example, synthetic-data extraction uses ``gpt-4o-mini`` through an API, while ProTeam uses ``Qwen2.5-14B-Instruct`` locally for ontology learning.

.. code-block:: python

   from openai import OpenAI
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

   # Configure the synthetic document generator
   api_key = "OPENAI_API_KEY"
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

The selected task determines the dataset schema. Ontology Construction predicts ``primitive-ontology-triples``, while Ontology Expansion predicts ``extended-primitive-ontology-triples`` given ``initial-primitive-ontology-triples``. The examples below use alternative task settings, so rerun preprocessing when switching tasks. See `Text2Onto <https://ontolearner.readthedocs.io/learning_tasks/text2onto.html>`_ for details.

.. code-block:: python

   # Select the primitive ontology learning task
   task = "ontology_construction"  # Change to "ontology_expansion" for reuse

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

   See the `Text2Onto Construction Example <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/text2onto_construction.py>`_ and `Text2Onto Expansion Example <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/text2onto_expansion.py>`_ for complete data preparation workflows.

Ontology Construction
---------------------

Initialize Learner
~~~~~~~~~~~~~~~~~~

Choose ``task="ontology_construction"`` in the preprocessing step. The learner retrieves similar labeled training documents and predicts complete ontology triples for each test document.

.. code-block:: python

   from ontolearner.learner.primitive import ProTeamPrimitiveLearner

   task = "ontology_construction"
   # Initialize the ProTeam primitive ontology learner
   learner = ProTeamPrimitiveLearner(
       model_id="Qwen/Qwen2.5-14B-Instruct",
       retriever_model_id="sentence-transformers/all-MiniLM-L6-v2",
       device="cuda",
       batch_size=10,
       max_input_length=3072,
   )

   # Load the language model and sentence embedding model
   learner.load()

Learn and Predict
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Fit the learner on the training data
   learner.fit(train_data, task=task)

   # Predict primitive ontology triples
   predicts = learner.predict(test_data, task=task)

   print(predicts)

The predictions contain the sample ``id`` and the generated ``primitive-ontology-triples`` for each input document.

Ontology Expansion
------------------

Initialize Learner
~~~~~~~~~~~~~~~~~~

For Ontology Expansion, first rerun the preprocessing section with ``task="ontology_expansion"``. The learner retrieves similar labeled training documents and predicts additional ontology triples using the initial ontology, terms, and types.

.. code-block:: python

   from ontolearner.learner.primitive import ProTeamPrimitiveLearner

   task="ontology_expansion"
   # Initialize the ProTeam primitive ontology learner
   learner = ProTeamPrimitiveLearner(
       model_id="Qwen/Qwen2.5-14B-Instruct",
       retriever_model_id="sentence-transformers/all-MiniLM-L6-v2",
       device="cuda",
       batch_size=10,
       max_input_length=3072,
   )

   # Load the language model and sentence embedding model
   learner.load()

Learn and Predict
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Fit the learner on the training data
   learner.fit(train_data, task=task)

   # Predict extended primitive ontology triples
   predicts = learner.predict(test_data, task=task)

   print(predicts)

The predictions contain the sample ``id`` and the generated ``extended-primitive-ontology-triples`` for each input document.


Pipeline Usage
--------------

Alternatively, use ``LearnerPipeline`` to fit, predict, and evaluate Ontology Construction or Ontology Expansion in a single call. Initialize the learner as shown in the respective task section and use the corresponding preprocessed data.

.. code-block:: python

   from ontolearner import LearnerPipeline

   task = "ontology_construction"  # Or "ontology_expansion"

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

   For additional methods and configuration options, see :class:`~ontolearner.learner.primitive.proteam.ProTeamPrimitiveLearner` in the Package Reference.
