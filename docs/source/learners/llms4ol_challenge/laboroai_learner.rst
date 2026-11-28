LaboroAI Learner
================

.. sidebar:: LaboroAI Learner Examples

   * `Ontology Construction <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_laboroai_construction.py>`_
   * `Ontology Expansion <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_laboroai_expansion.py>`_

The LaboroAI team addressed both **Task A (Flagship)** and **Task B (Reuse)**
in the LLMs4OL 2026 challenge. These correspond to **ontology construction**
and **ontology expansion** in OntoLearner. Their approach combines retrieved
few-shot examples, a single LLM extraction call and rule-based post-processing.

.. note::

   Read more in `LaboroAI at LLMs4OL 2026 Tasks Flagship and Reuse:
   Less is More for LLM-based Ontology Learning
   <https://www.tib-op.org/ojs/index.php/ocp/article/view/3681>`_
   by Xinyi Zhao and Jiachen Xu (2026).

.. hint::

   The OntoLearner implementation is available in
   `laboroai.py <https://github.com/sciknoworg/OntoLearner/blob/main/ontolearner/learner/primitive/laboroai.py>`_.

Overview
--------

.. image:: ../images/laboroai.PNG
   :alt: LaboroAI learner
   :align: center
   :width: 90%

For **ontology construction**, the learner predicts a primitive ontology from
text, including ``is-a``, ``instance-of`` and other relation triples. For
**ontology expansion**, it receives an initial ontology and predicts only
new triples between the supplied entities.

Methodological Summary:

1. **Exemplar Retrieval.** ``fit`` indexes labeled documents. At prediction
   time, BM25 and optional dense embeddings retrieve ``k`` relevant examples.
2. **Single-Pass Extraction.** The LLM receives retrieved examples and a
   document and returns subject--predicate--object triples.
3. **Symbolic Post-Processing.** The learner normalizes names, removes
   duplicates, avoids ``is-a`` cycles and handles symmetric relations.
4. **Expansion Filtering.** Existing triples are removed, and the endpoints of
   predicted triples are restricted to allowed entities from the seed ontology.

.. note::

   The team's reported best **exact graph similarity** scores were **0.6440**
   for construction and **0.6989** for expansion. These are results from the
   original challenge, not from the examples below. ``fit`` prepares the
   retrieval index; it does **not** fine-tune the model.

Data Preparation
----------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

The examples use FOAF, a small ontology. We keep its taxonomic relations for
compact synthetic documents, then split the ontology before generating the
train and test documents.

.. code-block:: python

   from ontolearner import train_test_split
   from ontolearner.ontology import FOAF

   ontology = FOAF()
   ontology.load()
   data = ontology.extract()

   data.term_typings = []
   data.type_non_taxonomic_relations.non_taxonomies = []

   train_ontology, test_ontology = train_test_split(
       data, test_size=0.5, random_state=42
   )

Generating Documents
~~~~~~~~~~~~~~~~~~~~

Use ``SyntheticGenerator`` for the two ontology partitions. In this example,
synthetic-data extraction uses ``gpt-4o-mini`` through an API. Fill in your
keys directly in the script, and do not commit them.

.. code-block:: python

   from openai import OpenAI
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

   api_key = ""   # OpenAI API key
   hf_token = ""  # Hugging Face token, if the model needs one

   generator = SyntheticGenerator(
       model_id="Qwen/Qwen2.5-0.5B-Instruct",
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

   train_synthetic = generator.generate(
       ontological_data=train_ontology, topic=ontology.domain
   )
   test_synthetic = generator.generate(
       ontological_data=test_ontology, topic=ontology.domain
   )

Preprocessing
~~~~~~~~~~~~~

The selected task determines the dataset schema. Construction predicts
``primitive-ontology-triples``; expansion predicts
``extended-primitive-ontology-triples`` given
``initial-primitive-ontology-triples``. The examples below are two
**alternative task settings**; rerun preprocessing when changing tasks.
See `Text2Onto <https://ontolearner.readthedocs.io/learning_tasks/text2onto.html>`_
for a detailed explanation.

.. code-block:: python

   task = "ontology_construction"  # Change to "ontology_expansion" for reuse
   preprocessor = SyntheticDataPreprocessor(
       client=OpenAI(api_key=api_key),
       task=task,
       random_state=42,
   )

   train_data = preprocessor.preprocess(train_synthetic, train_ontology)
   test_data = preprocessor.preprocess(test_synthetic, test_ontology)

   print("Train samples:", len(train_data))
   print("Test samples:", len(test_data))

Ontology Construction
---------------------

Initialize Learner
~~~~~~~~~~~~~~~~~~

Choose ``task="ontology_construction"`` in the preprocessing step. The
learner retrieves similar labeled training documents and predicts complete
ontology triples for each test document.

.. code-block:: python

   from ontolearner.learner.primitive import LaboroAIPrimitiveLearner

   task = "ontology_construction"
   learner = LaboroAIPrimitiveLearner(
       model_id="gpt-5.4",
       api_key=api_key,
       k=6,
       use_dense=True,
   )

Learn and Predict
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner import LearnerPipeline

   pipe = LearnerPipeline(
       llm=learner,
       llm_id=learner.model_id,
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
   print("Predictions:", outputs.get("predictions"))

Ontology Expansion
------------------

Initialize Learner
~~~~~~~~~~~~~~~~~~

To run expansion instead, **first rerun the preprocessing section** with
``task="ontology_expansion"``. The same learner class then receives the seed
ontology and predicts only additional relations.

.. code-block:: python

   from ontolearner.learner.primitive import LaboroAIPrimitiveLearner

   task = "ontology_expansion"
   learner = LaboroAIPrimitiveLearner(
       model_id="gpt-5.4",
       api_key=api_key,
       k=6,
       use_dense=True,
   )

Learn and Predict
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner import LearnerPipeline

   pipe = LearnerPipeline(
       llm=learner,
       llm_id=learner.model_id,
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
   print("Predictions:", outputs.get("predictions"))

.. tip::

   Set ``use_dense=False`` for BM25-only retrieval if you do not want to load
   the sentence-embedding model. LaboroAI uses a hosted LLM through the
   OpenAI SDK (or Google's OpenAI-compatible endpoint for ``gemini`` models),
   not a locally deployed model.

   Every setting is a constructor argument, such as ``predicates=[...]`` or
   ``prompt_template="..."`` (which must keep ``{context}``).
   ``learner.get_config()`` returns the current settings, and
   ``learner.build_prompt(text)`` shows the prompt for a text.