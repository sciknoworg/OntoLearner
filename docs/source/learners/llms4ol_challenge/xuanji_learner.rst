XuanJi Learner
==============

.. sidebar:: XuanJi Learner Examples

   * `Ontology Construction <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_xuanji_construction.py>`_

The XuanJi team (ZTE Corporation) addressed **Task A (Flagship)** in the
LLMs4OL 2026 challenge, corresponding to **ontology construction** in
OntoLearner. Their approach combines a few-shot LLM extraction call with
rule-based graph corrections. Its final predictions include taxonomy and
term-typing relations, but omit non-taxonomic relations.

.. note::

   Read more in `XuanJi at LLMs4OL 2026 Task Flagship: A Partial
   Graph-Oriented System for Taxonomy and Typing
   <https://www.tib-op.org/ojs/index.php/ocp/article/view/3682>`_
   by Jiaqi Jin (2026).

.. hint::

   The `original implementation <https://github.com/daiping8/llms4ol_Task_A>`_
   is available online. OntoLearner's learner is implemented in
   ``ontolearner/learner/primitive/xuanji.py``.

Overview
--------

.. image:: ../images/xuanji.PNG
   :alt: XuanJi learner
   :align: center
   :width: 90%

XuanJi asks a chat model to extract primitive ontology triples from text.
It favors a **precise taxonomy and typing graph** over predicting every
possible relation type.

Methodological Summary:

1. **Few-Shot Example Selection.** The learner selects fixed demonstrations
   or adaptively retrieves similar training examples for each document.
2. **Unified Triple Extraction.** One API request generates ``head | relation
   | tail`` triples from a document and its demonstrations.
3. **Graph Correction.** Deterministic rules normalize entity spans, correct
   selected naming variants and adjust high-confidence typing/taxonomy edges.
4. **Relation Filtering.** The final graph contains only ``is-a`` and
   ``instance-of`` triples, omitting non-taxonomic relations.

.. note::

   The reported official **semantic graph similarity** was **0.7790**
   (exact: 0.5485; fuzzy: 0.7355). These are the original team's results,
   not evaluation results from the synthetic example below. Because the model
   is accessed via an API, this learner does not require local LLM deployment.

Ontology Construction
---------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

The example loads FOAF and retains only its taxonomy for compact synthetic
input. Train and test ontology partitions are created before generating the
corresponding documents.

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

``SyntheticGenerator`` produces documents associated with the two ontology
partitions. The OpenAI-based extraction settings below belong to
**synthetic-data preparation**, not to XuanJi's own inference method.

.. code-block:: python

   import os
   from openai import OpenAI
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

   api_key = os.environ["OPENAI_API_KEY"]
   generator = SyntheticGenerator(
       model_id=os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct"),
       token=os.getenv("HF_TOKEN", ""),
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

Preprocessing with ``task="ontology_construction"`` creates samples with
``context`` and the target field ``primitive-ontology-triples``. The target is
used for training examples and evaluation, not passed as the test answer.
See `Text2Onto <https://ontolearner.readthedocs.io/learning_tasks/text2onto.html>`_
for details of synthetic-data preprocessing.

.. code-block:: python

   task = "ontology_construction"
   preprocessor = SyntheticDataPreprocessor(
       client=OpenAI(api_key=api_key),
       task=task,
       random_state=42,
   )

   train_data = preprocessor.preprocess(train_synthetic, train_ontology)
   test_data = preprocessor.preprocess(test_synthetic, test_ontology)

   print("Train samples:", len(train_data))
   print("Test samples:", len(test_data))

Initialize Learner
~~~~~~~~~~~~~~~~~~

``XuanJiFSLearner`` uses an OpenAI-compatible chat endpoint. Set
``adaptive_few_shot=True`` to retrieve different demonstrations for each
document, matching the submission's adaptive setting. ``fit`` prepares the
examples and retrieval index; it does not update model weights.

.. code-block:: python

   from ontolearner.learner.primitive import XuanJiFSLearner

   learner = XuanJiFSLearner(
       model_id=os.getenv("XUANJI_MODEL_ID", "gpt-5.4"),
       api_key=api_key,
       base_url=os.getenv("XUANJI_BASE_URL"),
       adaptive_few_shot=True,
   )

Learn and Predict
~~~~~~~~~~~~~~~~~

Run construction with ``LearnerPipeline``. Each predicted record contains
``id`` and ``primitive-ontology-triples``.

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
   print("Elapsed time:", outputs.get("elapsed_time"))

.. note::

   ``XuanJiFSLearner`` supports **ontology construction only**.
   ``ontology_expansion`` raises ``NotImplementedError``. Some canonical-name
   correction rules are specific to the LLMs4OL challenge data and may not
   generalize to other ontologies.
