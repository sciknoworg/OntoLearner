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

Use ``SyntheticGenerator`` for the two ontology partitions. In this example, synthetic-data extraction uses ``gpt-4o-mini`` through an API. Volt-IQ uses local ``qwen3.6:27b`` for construction, while expansion does not require an LLM.

.. code-block:: python

   from openai import OpenAI
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

   # Configure the synthetic document generator
   api_key = os.environ["OPENAI_API_KEY"]
   generator = SyntheticGenerator(
       model_id="Qwen/Qwen2.5-0.5B-Instruct",
       token="HF_TOKEN"
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

Choose ``task="ontology_construction"`` in the preprocessing step. The learner uses a local Ollama model to extract text-supported ontology triples and applies relation normalization and structural filtering.

.. code-block:: python

   from ontolearner.learner.primitive import VoltIQPrimitiveLearner

   task = "ontology_construction"

   # Initialize the Volt-IQ primitive ontology learner
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

   # Predict primitive ontology triples
   predicts = learner.predict(test_data, task=task)

   print(predicts)

The predictions contain the sample ``id`` and the generated ``primitive-ontology-triples`` for each input document.

Ontology Expansion
------------------

Initialize Learner
~~~~~~~~~~~~~~~~~~

For Ontology Expansion, first rerun the preprocessing section with ``task="ontology_expansion"``. The learner predicts additional ontology triples using the initial ontology, terms, and types. The default ``obo_foodon_to_terms_only`` strategy uses public-ontology parent evidence and training-supported term typing.

.. code-block:: python

   from ontolearner.learner.primitive import VoltIQPrimitiveLearner

   task = "ontology_expansion"

   # Initialize the learner with the default ontology-backed strategy
   learner = VoltIQPrimitiveLearner(
       expansion_method="obo_foodon_to_terms_only",
   )

.. note::

    Ontology-backed methods download and cache public OBO/OWL resources when needed.

Learn and Predict
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Prepare training annotations for ontology expansion
   learner.fit(train_data, task=task)

   # Predict new ontology extension triples
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


Taxonomy Discovery
------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For taxonomy discovery, we use GeoNames as a demonstration ontology, following the integrated example. The learner uses observed source taxonomy relations during fitting and predicts parent-child links between labels in the test ontology split.

.. code-block:: python

   from ontolearner import GeoNames, train_test_split

   # Load GeoNames and extract taxonomy data
   ontology = GeoNames()
   ontology.load()
   ontological_data = ontology.extract()

   # Split the taxonomy relations into training and test sets
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

   # Initialize the Volt-IQ taxonomy learner
   learner = VoltIQTaxonomyLearner(method="hybrid_cascade")

Learn and Predict
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner import evaluation_report

   # Prepare source taxonomy relations
   learner.fit(train_data, task=task)

   # Predict parent-child relations
   predicts = learner.predict(test_data, task=task)

   # Extract ground truth and evaluate predictions
   ground_truth = learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=ground_truth, y_pred=predicts, task=task)

   print("Predictions:", predicts)
   print("Metrics:", metrics)

The predictions contain ``parent`` and ``child`` fields for each predicted taxonomy relation.

.. note::

   * For domain-calibrated prediction, use ``method="domain_calibrated_primary"`` with the corresponding ``target_domain`` (Archeon, Biora, Hylex, or Phyra).
   * The corresponding target-domain files must be available and their labels prepared in OntoLearner's data format.


.. hint::

   For additional methods and configuration options, see :class:`~ontolearner.learner.primitive.voltiq.VoltIQPrimitiveLearner` and :class:`~ontolearner.learner.taxonomy_discovery.voltiq.VoltIQTaxonomyLearner` in the Package Reference.
