RWTH-DBIS Learner
==================

.. sidebar:: RWTH-DBIS Learner Examples

	* Term Typing: `llm_learner_rwthdbis_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_rwthdbis_term_typing.py>`_
	* Taxonomy Discovery: `llm_learner_rwthdbis_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_rwthdbis_taxonomy_discovery.py>`_


The RWTH-DBIS team participated in the LLMs4OL Challenge at ISWC 2024, addressing two main tasks: **Term Typing** and **Taxonomy Discovery**. The team used LLaMA-3-8B (an open-source model) and GPT-3.5-Turbo (a commercial model) to rigorously compare the performance gaps and distinct capabilities between these two classes of Large Language Models (LLMs). This comparison was crucial for establishing baselines for future Ontology Learning research, particularly focusing on how well models can generalize and incorporate external knowledge for structured knowledge extraction. The evaluation was conducted across established benchmark datasets, including GeoNames, UMLS, Schema.org, and the Gene Ontology (GO).

.. note::

	Read more about the model at `RWTH-DBIS at LLMs4OL 2024 Tasks A and B Knowledge-Enhanced Domain-Specific Continual Learning and Prompt-Tuning of Large Language Models for Ontology Learning <https://www.tib-op.org/ojs/index.php/ocp/article/view/2491>`_.

.. hint::

	The original implementation is available at `https://github.com/MouYongli/LLMs4OL <https://github.com/MouYongli/LLMs4OL>`_ repository.



Overview
---------------------------------

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/refs/heads/dev/docs/source/learners/images/rwth-dbis-learner.png" alt="RWTH-DBIS Team" width="90%"/>
   </div>
   <br>

The methodology is involved three sequential stages: **data augmentation**, **model training**, and **inference**. A key part of the data augmentation phase involved gathering rich contextual descriptions for terms and types from public web sources like Wikipedia and specialized ontology APIs. Furthermore, the team leveraged advanced commercial LLMs—specifically GPT-4o, Claude-3, and Copilot—using zero-shot prompts to access their web search capabilities and generate additional, high-quality contextual information. This enriched data was vital for overcoming the limitations of base models and enhancing their semantic understanding of domain-specific concepts prior to training. For the open-source LLaMA-3-8B model, the training stage incorporated several advanced techniques to maximize performance. These included **domain-specific continual training** to adapt the LLM's vocabulary and knowledge base to the target ontology domain (e.g., biomedical for GO, geographical for GeoNames). Furthermore, **fine-tuning** was used to specialize the model for the direct objectives of Term Typing and Taxonomy Discovery. Crucially, **knowledge-enhanced prompt-tuning** was implemented, which integrated the collected external context (from Wikipedia and commercial LLM searches) directly into the model's prompts during inference.

Methodological Summary:

1. **Data Collection & Context Enrichment.** Term and type descriptions were gathered from public sources like Wikipedia via its API, followed by cleaning and structuring. Commercial LLMs with web search capabilities—GPT-4o, Claude-3, and Copilot—were accessed through APIs using zero-shot prompts to gather additional contextual information. Ontology datasets were accessed directly via APIs or downloads to obtain relevant context.

2. **Training (Multiple Training Methods).** The implementation supports multiple training strategies:

   * **Domain-Specific Continual Learning (DS-CL)**: Pretrains the model on domain-specific context information before task-specific fine-tuning.
   * **Fine-tuning for Text Classification (FT-TC)**: Direct fine-tuning on the target task, with optional context augmentation.
   * **Structured Knowledge Prompt Tuning (SKPT)**: Integrates structured knowledge directly into prompt-style inputs during training.

   Context information for terms and types is integrated into the training data. For GeoNames, context is collected for all terms and types, while for other datasets, context can be collected at term or type level depending on the training method.

3. **Task-Specific Modeling.**

   * **Task A (Term Typing).** Models are trained on terms and corresponding types from the competition data. Each type is assigned a unique label, forming a dataset of term–label pairs for supervised fine-tuning. Three training methods are available: DS-CL (train_method=1), FT-TC (train_method=2, default), and SKPT (train_method=3).
   * **Task B (Taxonomy Discovery).** Hierarchical relationships are transformed into a binary classification format. Positive samples (parent–child) are labeled as 1, and negative samples (randomly sampled non-relations) as 0. Two training methods are available: DS-CL + without_context FT-TC (train_method=1) and (no DS-CL) with_context FT-TC (train_method=2, default).


Term Typing
-----------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For term typing, we use the AgrO ontology as a running example. Terms and their semantic types are split into train and test sets for supervised encoder fine-tuning and evaluation.

.. code-block:: python

   from ontolearner import train_test_split, AgrO

   # Load the AgrO ontology and extract labeled term-typing data
   ontology = AgrO()
   ontology.load()
   ontological_data = ontology.extract()

   # Split data into train and test sets
   train_data, test_data = train_test_split(
       ontological_data,
       test_size=0.2,
       random_state=42,
   )

Initialize Learner
~~~~~~~~~~~~~~~~~~

Before defining the learner, choose the task you want the learner to perform.
Available tasks have been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_.
The task IDs are: ``term-typing``, ``taxonomy-discovery``, ``non-taxonomic-re``.

.. code-block:: python

   task = "term-typing"

Next, we initialize :class:`RWTHDBISSFTLearner`. This learner is based on a small, pre-trained encoder model that is fine-tuned for the specific task. The hyperparameters control the supervised training process (e.g., epochs, batch size, learning rate).

Training Methods
^^^^^^^^^^^^^^^^

The learner supports three training methods via the ``train_method`` parameter:

* **train_method=1**: **DS-CL (Domain-specific Continual Learning)**

  This method performs domain-specific continual learning by pretraining the model on context information extracted from ontology terms and types. The model (AutoModelForCausalLM) is pretrained using causal language modeling on context descriptions of all unique terms and types from the training data. The pretraining adapts the model's vocabulary and knowledge base to the target ontology domain. Note: This method currently only performs the pretraining step; for complete DS-CL + FT-TC, you may need to follow up with train_method=2 using the pretrained model as the backbone.

* **train_method=2**: **FT-TC (Fine-tuning for Text Classification)** (default)

  This is the standard fine-tuning approach for text classification. The model is directly fine-tuned on term-label pairs without prior domain-specific pretraining. This method is suitable when you have sufficient training data and want a straightforward training process.

* **train_method=3**: **SKPT (Structured Knowledge Prompt Tuning)**

  This method integrates structured knowledge (context information) directly into prompts during training. The model is trained on prompt-style inputs that include both the term and its contextual description, formatted as structured knowledge prompts. Each input follows a template like: "[Knowledge] Biological term in Gene Ontology: {term} Describe: {term_info} [Prediction] Text: '{term} in biological is a ?' Ans:". The model (AutoModelForSequenceClassification) is then fine-tuned on these prompt-formatted inputs. This approach is particularly effective when you have rich contextual information and want to leverage it explicitly during training.

.. note::

   The choice of training method depends on your dataset characteristics:

   * Small dataset + small number of types: Use FT-TC (train_method=2)
   * Large dataset + small number of types: Use DS-CL + FT-TC (train_method=1)
   * Small dataset + large number of types: Use SKPT (train_method=3)
   * Large dataset + large number of types: Use DS-CL + SKPT (train_method=1, then train_method=3)

Context Generation
^^^^^^^^^^^^^^^^^^

When ``context_json_path=None`` (the default), the learner automatically generates context information from the ontology during training. This process:

1. Extracts all unique terms from the ontology
2. Generates contextual descriptions for each term using GPT (via g4f library) or a custom provider function
3. Stores the context in a JSON file at ``{output_dir}/context/rwthdbis_onto_processed.json``
4. Performs re-inference for terms with short descriptions (< 50 characters) up to 5 retry rounds

The context information is then used during training (for train_method=1 and train_method=3) and inference to enhance semantic understanding. If you already have a preprocessed context file, you can provide its path via ``context_json_path`` to skip the generation step.

.. code-block:: python

   from ontolearner.learner.term_typing import RWTHDBISSFTLearner

   learner = RWTHDBISSFTLearner(
       model_name="microsoft/deberta-v3-small",
       trained_model_path=None,  # Optional: path to a pre-trained checkpoint
       output_dir="./results/deberta-v3",
       device="cpu",
       num_train_epochs=3,  # Default: 3 epochs
       per_device_train_batch_size=16,
       gradient_accumulation_steps=2,
       learning_rate=2e-5,
       weight_decay=0.01,
       max_length=64,
       logging_steps=50,
       save_strategy="epoch",
       save_total_limit=1,
       fp16=False,  # Enable FP16 mixed precision if supported
       bf16=False,  # Enable BF16 mixed precision if supported
       seed=42,
       train_method=2,  # FT-TC (default)
       context_json_path=None,  # Path to preprocessed context JSON, or None to auto-generate
       ontology_name="Geonames",  # Dataset/domain name used in prompts
   )

   # Load the base encoder and prepare it for supervised term typing
   learner.load(llm_id=learner.model_name)


Learn and Predict
~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: python

   from ontolearner import evaluation_report

   # Indexing (fitting) the model on the training data for the LLMs4OL task
   learner.fit(train_data, task=task)

   # Perform prediction and evaluation directly
   predicts = learner.predict(test_data, task=task)
   truth = learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)


Taxonomy Discovery
------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For taxonomy discovery, we use the Chord ontology as a running example. It exposes hierarchical (parent, child) relations that can be transformed into labeled edges for taxonomic relation classification.

.. code-block:: python

   from ontolearner import train_test_split, ChordOntology

   # Load the Chord ontology (taxonomy discovery benchmark)
   ontology = ChordOntology()
   ontology.load()

   # Extract hierarchical (parent, child) edges and split into train/test
   train_data, test_data = train_test_split(
       ontology.extract(),
       test_size=0.2,
       random_state=42,
   )

Initialize Learner
~~~~~~~~~~~~~~~~~~

Before defining the learner, choose the ontology learning task to perform.
Available tasks have been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_.
The task IDs are: ``term-typing``, ``taxonomy-discovery``, ``non-taxonomic-re``.

.. code-block:: python

   task = "taxonomy-discovery"

Next, we initialize :class:`RWTHDBISSFTLearner`. This learner fine-tunes a transformer model to classify pairs of terms as positive or negative taxonomic relations (e.g., parent–child vs. non-parent–child).

Training Methods
^^^^^^^^^^^^^^^^

The learner supports two training methods via the ``train_method`` parameter:

* **train_method=1**: **DS-CL + without_context FT-TC (Domain-specific Continual Learning + Fine-tuning for Text Classification without context)**

  This method combines domain-specific continual learning with fine-tuning. First, the model is pretrained on context information extracted from ontology terms using causal language modeling (AutoModelForCausalLM) for 2 epochs. The pretrained model is saved and used as the backbone for the classification task. Then, the model is fine-tuned for binary classification of taxonomic relations using AutoModelForSequenceClassification, but **without** including context information in the input texts (the "## Context." suffix is removed from input_texts). This approach adapts the model to the domain vocabulary while training on relation templates only.

* **train_method=2**: **with_context FT-TC (Fine-tuning for Text Classification with context)** (default)

  This method fine-tunes the model directly on relation pairs **with** context information included in the input. Each training example includes the relation template (e.g., "parent is the superclass of child") augmented with contextual descriptions of both parent and child terms. This approach leverages external knowledge (from GPT or ontology) during training to improve semantic understanding.

Context Generation
^^^^^^^^^^^^^^^^^^

When ``context_json_path=None`` (the default), the learner automatically generates context information from the ontology during training. This process:

1. Extracts all unique terms (both parent and child) from the ontology taxonomy
2. Generates contextual descriptions for each term using GPT (via g4f library) or a custom provider function
3. Stores the context in a JSON file at ``{output_dir}/context/rwthdbis_onto_processed.json``
4. Performs re-inference for terms with short descriptions (< 50 characters) up to 5 retry rounds

The context information is then appended to relation templates during training (for train_method=2) and inference. If you already have a preprocessed context file, you can provide its path via ``context_json_path`` to skip the generation step.

.. code-block:: python

   from ontolearner.learner.taxonomy_discovery import RWTHDBISSFTLearner

   learner = RWTHDBISSFTLearner(
       model_name="distilroberta-base",
       output_dir="./results/taxonomy-discovery",
       device="cpu",
       num_train_epochs=1,
       per_device_train_batch_size=8,
       gradient_accumulation_steps=4,
       learning_rate=2e-5,
       weight_decay=0.01,
       max_length=256,
       logging_steps=25,
       save_strategy="epoch",
       save_total_limit=1,
       fp16=True,  # Enable FP16 mixed precision if supported
       bf16=False,  # Enable BF16 mixed precision if supported
       seed=42,
       train_method=2,  # with_context FT-TC (default)
       negative_ratio=5,  # Number of negative samples per positive sample
       bidirectional_templates=True,  # If True, also add reversed template examples
       context_json_path=None,  # Path to preprocessed context JSON, or None to auto-generate
       ontology_name=ontology.ontology_full_name,  # Dataset/domain name used in prompts
       min_predictions=1,  # Minimum number of predictions to return if none are positive
   )

   # Load the base model and prepare it for supervised taxonomy learning
   learner.load(llm_id=learner.model_name)


Learn and Predict
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from ontolearner import evaluation_report

   # Fine-tune the model on the taxonomic training data
   learner.fit(train_data, task=task)

   # Perform prediction and evaluation directly
   predicts = learner.predict(test_data, task=task)
   truth = learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)
