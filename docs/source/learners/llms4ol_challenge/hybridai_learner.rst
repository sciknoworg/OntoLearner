HybridAI-Squared Learner
========================

.. sidebar:: HybridAI-Squared Learner Examples

   * `Zero-Shot Expansion <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_hybridsquared_zs_expansion.py>`_
   * `Per-Relation Expansion <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_hybridsquared_per_relation_expansion.py>`_
   * `Fine-Tuned Expansion <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_hybridsquared_sft_expansion.py>`_

The HybridAI-Squared team addressed **Task B (Reuse)** in the LLMs4OL 2026
challenge, corresponding to **ontology expansion** in OntoLearner. Given a
text, its terms and types, and an initial set of ontology triples, the learner
predicts additional taxonomic and non-taxonomic relation triples.

.. note::

   Read more in `HybridAI-Squared at LLMs4OL 2026 Task Reuse: Divide and
   Conquer does not help LLMs perform Ontology Learning
   <https://www.tib-op.org/ojs/index.php/ocp/article/view/3660>`_ by
   Upal Bhattacharya, Maaike de Boer and Sergey Sosnovsky (2026).

.. hint::

   The `original HybridAI-Squared implementation
   <https://codeberg.org/upalbhattacharya/llms4ol_2026_reuse>`_ is available
   online. OntoLearner's integration is in
   ``ontolearner/learner/primitive/hybridsquared.py``.

Overview
--------

The team investigated three approaches for identifying new relations between
provided entities. All three extract triples of the form ``[subject, relation,
object]`` and filter predicted relations already present in the initial
ontology.

Methodological Summary:

1. **Joint Direct Prediction (zero-shot).** One structured prompt asks a Qwen3
   model to predict all allowed relation types together.
2. **Per-Relation Prediction (zero-shot).** Separate prompts predict ``is-a``,
   ``instance-of`` and other relations. The implementation supports three or
   seven relation categories, and an optional chained three-category variant.
3. **Fine-Tuned Direct Prediction.** A Qwen3 model is fine-tuned with a LoRA
   adapter to predict all new relations jointly.
4. **Relation Filtering.** Predicted existing triples are removed. A semantic
   precedence rule also drops competing lower-priority relations (for example,
   ``type`` when ``is-a`` is predicted for the same pair).

The original challenge reported the following **average graph similarity**
results. These are not results from the small synthetic examples below.

.. list-table:: Results reported by HybridAI-Squared
   :header-rows: 1
   :widths: 75 25

   * - Approach
     - Graph similarity
   * - Joint direct prediction
     - 0.7357
   * - Per-relation prediction (3 categories)
     - 0.7113
   * - Per-relation prediction (7 categories)
     - 0.4812
   * - Fine-tuned direct prediction
     - **0.9013**

The learners load Hugging Face models **locally** with ``transformers``. They
do not call an OpenAI API to make their own predictions. The separate
synthetic-data preparation example below *does* use an OpenAI API.

Ontology Expansion
------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

The following example uses the BBC Core Concepts ontology, whose taxonomic
relations provide a compact demonstration of ontology expansion. The zero-shot
and fine-tuning example scripts linked above use FOAF instead. We retain only
taxonomic relations to keep the synthetic example small.

.. code-block:: python

   from ontolearner import train_test_split
   from ontolearner.ontology import BBCCoreConcepts

   ontology = BBCCoreConcepts()
   ontology.load()
   data = ontology.extract()

   data.term_typings = []
   data.type_non_taxonomic_relations.non_taxonomies = []

   train_ontology, test_ontology = train_test_split(
       data, test_size=0.5, random_state=42
   )

Generating Documents
~~~~~~~~~~~~~~~~~~~~

Generate training and test documents from their corresponding ontology splits
using ``SyntheticGenerator``. This example uses the OpenAI extraction method
for synthetic-data preparation, not for the HybridAI-Squared learner itself.

.. code-block:: python

   import os
   from openai import OpenAI
   from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor

   api_key = os.environ["OPENAI_API_KEY"]
   generator = SyntheticGenerator(
       model_id=os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-1.5B-Instruct"),
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

``SyntheticDataPreprocessor`` prepares ontology-expansion examples containing
``context``, ``terms``, ``types``, ``initial-primitive-ontology-triples`` and
``extended-primitive-ontology-triples``. The last field is the prediction
target. See the `Text2Onto documentation
<https://ontolearner.readthedocs.io/learning_tasks/text2onto.html>`_ for
preprocessing details.

.. code-block:: python

   task = "ontology_expansion"
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

Choose **one** of the learners below. All three support
``task="ontology_expansion"`` only.

**Zero-Shot Direct Prediction**

.. code-block:: python

   from ontolearner.learner.primitive import HybridAISquaredZSLearner

   learner = HybridAISquaredZSLearner(
       model_id="Qwen/Qwen3-0.6B",
       device="cpu",
       max_new_tokens=512,
       temperature=0.0,
       enable_thinking=False,
   )

**Per-Relation Direct Prediction**

.. code-block:: python

   from ontolearner.learner.primitive import HybridAISquaredPerRelationLearner

   learner = HybridAISquaredPerRelationLearner(
       model_id="Qwen/Qwen3-0.6B",
       categories=3,          # is-a, instance-of, rest
       chain=False,           # only categories=3 supports chaining
       device="cpu",
       max_new_tokens=512,
       temperature=0.0,
       enable_thinking=False,
   )

**Fine-Tuned Direct Prediction**

.. code-block:: python

   from ontolearner.learner.primitive import HybridAISquaredSFTLearner

   learner = HybridAISquaredSFTLearner(
       model_id="Qwen/Qwen3-0.6B",
       device="cpu",
       output_dir="./results/hybridaisquared",
       max_new_tokens=512,
       temperature=0.0,
       enable_thinking=False,
   )

.. note::

   These are **small CPU examples**, not the original challenge settings.
   The paper used Qwen3-30B-A3B for prompting and 4-bit LoRA fine-tuning of
   Qwen3-14B. Fine-tuning requires at least two training samples; all methods
   require usable test samples. Large models and longer generation settings
   generally require a suitable GPU.

Learn and Predict
~~~~~~~~~~~~~~~~~

Run the selected learner through ``LearnerPipeline``. The zero-shot learners
perform no gradient-based training during ``fit``; the fine-tuned learner
trains or loads its LoRA adapter.

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

.. tip::

   By default, predicted triples already present in the initial ontology are
   removed, and relation precedence filtering is applied. Additional filters
   such as ``duplicates`` and ``self_relation`` can be enabled through the
   learner's ``filters`` parameter.
