
ProTeam Learner
===============

.. sidebar:: ProTeam Learner Examples

   * Ontology Construction: `llm_learner_proteam_construction.py <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/llm_learner_proteam_construction.py>`_
   * Ontology Expansion: `llm_learner_proteam_expansion.py <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/llm_learner_proteam_expansion.py>`_


The **pro-team** participated in the LLMs4OL 2026 Challenge, addressing two ontology learning tasks: **Ontology Construction** (Flagship Task A) and **Ontology Expansion** (Reuse Task B). Their approach employs an offline Retrieval-Augmented Generation (RAG) framework with few-shot prompting to construct primitive ontologies from unstructured text and extend existing ontologies with new relationships. The system combines ``Qwen2.5-14B-Instruct`` for ontology generation with ``sentence-transformers/all-MiniLM-L6-v2`` for semantic retrieval. For ontology expansion, the approach additionally integrates proximity-based term typing and vocabulary-constrained filtering to improve the consistency of generated ontology triples with the provided vocabulary and initial ontology.


.. note::

   Read more about the model at `pro-team at LLMs4OL 2026 Tasks Flagship and Reuse: Retrieval-Augmented Generation and Vocabulary-Constrained Filtering for Ontology Learning <https://www.tib-op.org/ojs/index.php/ocp/article/view/3663>`_.

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

   * Follow the example to prepare ``train_data`` and ``test_data`` containing textual context and reference ontology triples.
   * The OpenAI backend is used for synthetic data preparation, while ProTeam inference follows the offline RAG approach.

Initialize Learner
~~~~~~~~~~~~~~~~~~

Before defining the learner, choose the primitive ontology learning task. Available tasks have been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_. The ``ProTeamPrimitiveLearner`` supports two tasks: ``ontology_construction`` and ``ontology_expansion``.

.. code-block:: python

   task = "ontology_construction"

Next, we initialize ``ProTeamPrimitiveLearner``, which extends OntoLearner's ``PrimitiveOntologyLearner`` interface. The learner combines a sentence embedding model for retrieving similar training examples with an instruction-tuned language model for generating primitive ontology triples.

.. code-block:: python

   from ontolearner.learner.primitive import ProTeamPrimitiveLearner

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

Pipeline Usage
~~~~~~~~~~~~~~

The ``ProTeamPrimitiveLearner`` can also be used through OntoLearner's ``LearnerPipeline`` to perform fitting, prediction, and evaluation in a single call.

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

Ontology Expansion
------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For ontology expansion, we use the FOAF ontology as a running example. The ontology is loaded, and its taxonomic relations are split into training and test sets. The expansion task extends an initial primitive ontology by predicting additional relationships from textual context, terms, and types.

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

The ontology splits are used to generate synthetic textual documents through ``SyntheticGenerator``. The generated documents are subsequently processed using ``SyntheticDataPreprocessor`` to prepare training and test samples for ontology expansion.

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

   # Initialize the expansion data preprocessor
   preprocessor = SyntheticDataPreprocessor(
       client=OpenAI(api_key=api_key),
       task="ontology_expansion",
       random_state=42,
   )

   # Prepare labeled expansion samples for fitting and evaluation
   train_data = preprocessor.preprocess(train_synthetic, train_ontology)
   test_data = preprocessor.preprocess(test_synthetic, test_ontology)


.. note::

   See the `Text2Onto Expansion Example <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/text2onto_expansion.py>`_ for the complete synthetic document generation and preprocessing workflow.

   * The prepared ``train_data`` and ``test_data`` contain textual context, initial ontology triples, terms, types, and reference extension triples.
   * The OpenAI backend is used for synthetic data preparation, while ProTeam inference follows the offline RAG approach.

Initialize Learner
~~~~~~~~~~~~~~~~~~

Before defining the learner, choose the primitive ontology learning task. Available tasks have been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_. The ``ProTeamPrimitiveLearner`` supports two tasks: ``ontology_construction`` and ``ontology_expansion``.

.. code-block:: python

   task = "ontology_expansion"

Next, we initialize ``ProTeamPrimitiveLearner``, which extends OntoLearner's ``PrimitiveOntologyLearner`` interface. The learner combines a sentence embedding model for retrieving similar training examples with an instruction-tuned language model for generating ontology extensions. The expansion task additionally incorporates proximity-based term typing and vocabulary-constrained filtering.

.. code-block:: python

   from ontolearner.learner.primitive import ProTeamPrimitiveLearner

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
~~~~~~~~~~~~~~

The ``ProTeamPrimitiveLearner`` can also be used through OntoLearner's ``LearnerPipeline`` to perform fitting, prediction, and evaluation in a single call.

.. code-block:: python

   from ontolearner import LearnerPipeline

   # Initialize the learner pipeline
   pipeline = LearnerPipeline(
       llm=learner,
       llm_id=learner.model_id,
       ontologizer_data=True,
   )

   # Fit, predict, and evaluate ontology expansion
   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       task=task,
       evaluate=True,
       ontologizer_data=True,
   )

