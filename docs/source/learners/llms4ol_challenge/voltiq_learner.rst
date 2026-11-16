Volt-IQ Learner
===============

.. sidebar:: Volt-IQ Learner Examples

   * Ontology Construction: `llm_learner_voltiq_construction.py <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/llm_learner_voltiq_construction.py>`_
   * Ontology Expansion: `learner_voltiq_expansion.py <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/learner_voltiq_expansion.py>`_
   * Taxonomy Discovery: `learner_voltiq_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/learner_voltiq_taxonomy_discovery.py>`_

The **Volt-IQ** team participated in the LLMs4OL 2026 Challenge, addressing three ontology learning tasks: **Ontology Construction** (Flagship Task A), **Ontology Expansion** (Reuse Task B), and **Taxonomy Discovery** (Task C). Their evidence-routed approach selects task-specific candidate sources and constraints according to the available inputs. Ontology Construction uses constrained language-model extraction from textual context; Ontology Expansion combines training-derived relation memory with public-ontology parent evidence; and Taxonomy Discovery applies domain-calibrated lexical and ontology-backed induction. The branches share normalization, structural filtering, and output-schema validation.

.. note::

   Read more about the methodology in `Volt-IQ at LLMs4OL 2026: Constrained Graph Synthesis and Domain-Calibrated Ontology Learning Systems for the Flagship, Reuse, and Taxonomy Tasks <https://www.tib-op.org/ojs/index.php/ocp/article/view/3662>`_.

.. hint::

   * The original implementation is available in the `Volt-IQ GitHub repository <https://github.com/kebamt/llms4ol-challenge>`_.
   * The OntoLearner-integrated implementations are available in `VoltIQPrimitiveLearner <https://github.com/sciknoworg/OntoLearner/blob/dev/ontolearner/learner/primitive/voltiq.py>`_ and `VoltIQTaxonomyLearner <https://github.com/sciknoworg/OntoLearner/blob/dev/ontolearner/learner/taxonomy_discovery/voltiq.py>`_.

Overview
---------------------------------

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/refs/heads/dev/docs/source/learners/images/voltiq-learner.png" alt="Volt-IQ Learner" width="100%"/>
   </div>
   <br>


The Volt-IQ workflow begins with **schema-aware parsing and normalization**, followed by **task-routed candidate generation**. Task A obtains triples from document-grounded language-model extraction, Task B recovers extensions from training memory and public ontology parents, and Task C induces hierarchical relations using domain-selected lexical or ontology-backed evidence. The resulting candidates pass through constraint and graph filters before task-specific schema validation and JSON packaging.

Methodological Summary:

1. **Constrained Graph Synthesis.** For Ontology Construction, the executable system uses a locally deployed Ollama model (``qwen3.6:27b`` by default) to generate structured primitive ontology triples from textual context. Generated candidates undergo JSON parsing, relation normalization, entity-support checks, and filtering of malformed, self-referential, and duplicate triples.

2. **Ontology-Backed Constrained Extension.** For Ontology Expansion, the system combines training-derived relation memory with direct-parent recovery from public OBO ontologies, the Plant Trait Ontology, and FoodOn, using parent-frequency statistics where applicable. Ontology-backed parent relations are supplemented with training-supported term typing, while record-local constraints and structural filtering remove invalid, duplicate, or pre-existing triples. The integrated learner supports 17 expansion strategies, including lexical, contextual, memorized, and ontology-backed methods.

3. **Domain-Calibrated Taxonomy Induction.** For Taxonomy Discovery, the system uses source-domain taxonomy relations to derive lexical features and parent priors. It applies substring induction for Archeon and Phyra, lexical subsumption for Hylex, and OBO/OWL direct-parent recovery with lexical fallback for Biora. Candidate relations undergo normalization, deduplication, and applicable graph constraints. The integrated learner supports 15 taxonomy discovery methods, including lexical, hybrid, ontology-backed, and domain-calibrated strategies.

.. note::

   The OntoLearner integration preserves the executable methods available in the original repository. Some final submission steps could not be reproduced:

   * **Task A:** The complete merging procedure for the final extraction artifact is unavailable.
   * **Task C:** Manual corrections to the final taxonomy predictions have no reproducible post-processing implementation.

Ontology Construction
---------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For ontology construction, we use the FOAF ontology as a running example. We load the ontology and split its taxonomic relations into training and test sets before generating aligned text documents.

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

We use ``SyntheticGenerator`` to create textual documents from the ontology splits, then ``SyntheticDataPreprocessor`` to prepare construction samples containing text and reference primitive ontology triples.

.. code-block:: python

   import os
   from openai import OpenAI
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

   # Configure synthetic document generation
   model_id = os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct")
   api_key = os.getenv("OPENAI_API_KEY")
   hf_token = os.getenv("HF_TOKEN", "")

   if not api_key:
       raise EnvironmentError("Set OPENAI_API_KEY before running.")

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

   # Generate synthetic documents for both ontology splits
   train_synthetic = generator.generate(ontological_data=train_ontology, topic=ontology.domain)
   test_synthetic = generator.generate(ontological_data=test_ontology, topic=ontology.domain)

   # Prepare construction records with the correct target field
   preprocessor = SyntheticDataPreprocessor(
       client=OpenAI(api_key=api_key),
       task="ontology_construction",
       random_state=42,
   )

   train_data = preprocessor.preprocess(train_synthetic, train_ontology)
   test_data = preprocessor.preprocess(test_synthetic, test_ontology)

.. note::

   See the `Text2Onto Construction Example <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/text2onto_construction.py>`_ for the complete synthetic document generation and preprocessing workflow.

   * The prepared ``train_data`` and ``test_data`` contain textual context and reference ontology triples.
   * The OpenAI backend is used for synthetic data preparation, while Volt-IQ uses local installed Ollama models for inference.

Initialize Learner
~~~~~~~~~~~~~~~~~~

The ``VoltIQPrimitiveLearner`` extends OntoLearner's ``PrimitiveOntologyLearner`` interface. For ``ontology_construction``, the learner uses a locally deployed Ollama model to generate structured ontology triples through constrained extraction and post-processing.

.. code-block:: python

   from ontolearner.learner.primitive import VoltIQPrimitiveLearner

   task = "ontology_construction"

   # Configure the local Ollama extractor
   learner = VoltIQPrimitiveLearner(
       model_id="qwen3.6:27b",
       base_url="http://127.0.0.1:11434",
       workers=1,
       timeout=600.0,
   )

   # Configure the learner; Ollama availability is checked at prediction time
   learner.load()

.. note::

   Ontology Construction uses the local Ollama model ``qwen3.6:27b``. Ensure the model is installed and the Ollama server is running before inference.

Learn and Predict
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Prepare the learner for ontology construction
   learner.fit(train_data, task=task)

   # Generate primitive ontology triples
   predicts = learner.predict(test_data, task=task)

   print("Predictions:", predicts)

The predictions contain the sample ``id`` and generated ``primitive-ontology-triples`` for each input document.

Pipeline Usage
~~~~~~~~~~~~~~

The ``VoltIQPrimitiveLearner`` can also run through OntoLearner's ``LearnerPipeline`` to fit, predict, and evaluate in a single call. This is an alternative to the preceding direct invocation.

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

   print("Metrics:", metrics)

Ontology Expansion
------------------


Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For Ontology Expansion, we use the FOAF ontology as a running example. The ontology is loaded, and its taxonomic relations are split into training and test sets. The expansion task extends an initial primitive ontology by predicting additional relationships based on textual context, terms, and types.

.. code-block:: python

   from ontolearner import train_test_split
   from ontolearner.ontology import FOAF

   # Load and extract the FOAF ontology
   ontology = FOAF()
   ontology.load()
   ontological_data = ontology.extract()

   # Retain taxonomic relations for the example
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

The synthetic documents are preprocessed for ``ontology_expansion`` so that initial ontology triples and reference extensions are retained separately. The training data supplies relation memory used by the selected expansion strategy.

.. code-block:: python

   import os
   from openai import OpenAI
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

   model_id = os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct")
   api_key = os.getenv("OPENAI_API_KEY")
   hf_token = os.getenv("HF_TOKEN", "")

   if not api_key:
       raise EnvironmentError("Set OPENAI_API_KEY before running.")

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

   train_synthetic = generator.generate(ontological_data=train_ontology, topic=ontology.domain)
   test_synthetic = generator.generate(ontological_data=test_ontology, topic=ontology.domain)

   # Prepare expansion samples with initial and extended triples
   preprocessor = SyntheticDataPreprocessor(
       client=OpenAI(api_key=api_key),
       task="ontology_expansion",
       random_state=42,
   )

   train_data = preprocessor.preprocess(train_synthetic, train_ontology)
   test_data = preprocessor.preprocess(test_synthetic, test_ontology)

.. note::

   See the `Text2Onto Expansion Example <https://github.com/sciknoworg/OntoLearner/blob/dev/examples/text2onto_expansion.py>`_ for the complete synthetic document generation and preprocessing workflow.

   * The prepared ``train_data`` and ``test_data`` contain textual context, initial ontology triples, terms, types, and reference extension triples.
   * Synthetic data preparation uses OpenAI, but the Volt-IQ Ontology Expansion strategies do not require an LLM.

Initialize Learner
~~~~~~~~~~~~~~~~~~

The ``VoltIQPrimitiveLearner`` supports seventeen ontology expansion strategies, including lexical, contextual, memorized, and ontology-backed methods. The default strategy, ``obo_foodon_to_terms_only``, combines public-ontology parent recovery with training-supported term typing.

.. code-block:: python

   from ontolearner.learner.primitive import VoltIQPrimitiveLearner

   task = "ontology_expansion"

   #Initialize the learner with the default ontology-backed strategy
   learner = VoltIQPrimitiveLearner(
       expansion_method="obo_foodon_to_terms_only",
   )

.. note::

   * Ontology-backed methods download and cache public OBO/OWL resources when needed.
   * Parent relations are restricted to labels in the current record.

Learn and Predict
~~~~~~~~~~~~~~~~~

.. code-block:: python


    from ontolearner.evaluation import evaluation_report

    # Prepare training annotations for ontology expansion
    learner.fit(train_data, task=task)

    # Predict new ontology extension triples
    predicts = learner.predict(test_data, task=task)

    # Extract ground truth and evaluate predictions
    ground_truth = learner.tasks_ground_truth_former(data=test_data,task=task)

    metrics = evaluation_report(y_true=ground_truth,y_pred=predicts,task=task)

    print("Metrics:", metrics)

Taxonomy Discovery
------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For taxonomy discovery, we use GeoNames as a demonstration ontology, following the integrated example. The learner uses observed source taxonomy relations during fitting and predicts parent-child links between labels in the test ontology split.

.. code-block:: python

   from ontolearner import GeoNames, train_test_split

   # Load GeoNames and split its taxonomy relations
   ontology = GeoNames()
   ontology.load()
   ontological_data = ontology.extract()

   train_data, test_data = train_test_split(
       ontological_data,
       test_size=0.2,
       random_state=42,
   )

Initialize Learner
~~~~~~~~~~~~~~~~~~

The ``VoltIQTaxonomyLearner`` extends OntoLearner's ``AutoLearner`` interface. The example uses ``hybrid_cascade`` to predict taxonomy relations using lexical features and parent priors derived from training data.

.. code-block:: python

   from ontolearner.learner.taxonomy_discovery import VoltIQTaxonomyLearner

   task = "taxonomy-discovery"

   # Initialize a taxonomy learner for the GeoNames benchmark example
   learner = VoltIQTaxonomyLearner(method="hybrid_cascade")

Learn and Predict
~~~~~~~~~~~~~~~~~

The learner returns predictions with ``parent`` and ``child`` fields. Its taxonomy methods preserve target labels while excluding self-relations and duplicate edges. Cycle prevention is applied by the applicable candidate-selection methods.

.. code-block:: python

   from ontolearner import evaluation_report

   # Prepare source taxonomy relations and parent priors
   learner.fit(train_data, task=task)

   # Predict parent-child relations for the test label inventory
   predicts = learner.predict(test_data, task=task)

   # Extract ground truth and evaluate predictions
   ground_truth = learner.tasks_ground_truth_former(data=test_data,task=task)

   metrics = evaluation_report(y_true=ground_truth,y_pred=predicts,task=task)

   print("Predictions:", predicts)
   print("Metrics:", metrics)

.. note::

   * To reproduce the VoltIQ's Task C methodology, use ``method="domain_calibrated_primary"`` with the corresponding ``target_domain`` (Archeon, Biora, Hylex, or Phyra).
   * The GeoNames example demonstrates general taxonomy discovery; the original approach uses the challenge target domains and OntoLearner source taxonomies.
