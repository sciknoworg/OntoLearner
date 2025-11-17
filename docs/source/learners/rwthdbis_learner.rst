RWTH-DBIS Learner
==================

Description
-----------

.. sidebar:: Examples

   * RWTH-DBIS Taxonomy Discovery Example: `llm_learner_rwthdbis_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_rwthdbis_taxonomy_discovery.py>`_
   * RWTH-DBIS Term Typing Example: `llm_learner_rwthdbis_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_rwthdbis_term_typing.py>`_

The RWTH-DBIS team participated in the LLMs4OL Challenge at ISWC 2024, addressing two main tasks: **Term Typing** and **Taxonomy Discovery**. The team used LLaMA-3-8B (an open-source model) and GPT-3.5-Turbo (a commercial model) to rigorously compare the performance gaps and distinct capabilities between these two classes of Large Language Models (LLMs). This comparison was crucial for establishing baselines for future Ontology Learning research, particularly focusing on how well models can generalize and incorporate external knowledge for structured knowledge extraction. The evaluation was conducted across established benchmark datasets, including GeoNames, UMLS, Schema.org, and the Gene Ontology (GO).

The experimental methodology was robust, involving three sequential stages: **data augmentation**, **model training**, and **inference**. A key part of the data augmentation phase involved gathering rich contextual descriptions for terms and types from public web sources like Wikipedia and specialized ontology APIs. Furthermore, the team leveraged advanced commercial LLMs—specifically GPT-4o, Claude-3, and Copilot—using zero-shot prompts to access their web search capabilities and generate additional, high-quality contextual information. This enriched data was vital for overcoming the limitations of base models and enhancing their semantic understanding of domain-specific concepts prior to training.

For the open-source LLaMA-3-8B model, the training stage incorporated several advanced techniques to maximize performance. These included **domain-specific continual training** to adapt the LLM's vocabulary and knowledge base to the target ontology domain (e.g., biomedical for GO, geographical for GeoNames). Furthermore, **fine-tuning** was used to specialize the model for the direct objectives of Term Typing and Taxonomy Discovery. Crucially, **knowledge-enhanced prompt-tuning** was implemented, which integrated the collected external context (from Wikipedia and commercial LLM searches) directly into the model's prompts during inference.

**Datasets**

* **Term Typing.** Labeled term–type pairs from benchmark ontologies, including GeoNames, UMLS, Schema.org, and GO, used to train and evaluate supervised encoders for semantic typing.
* **Taxonomy Discovery.** Hierarchical (parent–child) edges drawn from the same ontologies, converted into positive/negative relation pairs for binary classification of taxonomic relations.

**Methodology**

1. **Data Collection & Context Enrichment.** Term and type descriptions were gathered from public sources like Wikipedia via its API, followed by cleaning and structuring. Commercial LLMs with web search capabilities—GPT-4o, Claude-3, and Copilot—were accessed through APIs using zero-shot prompts to gather additional contextual information. Ontology datasets were accessed directly via APIs or downloads to obtain relevant context.

2. **Training (Domain-Specific Continual Training).** Context information for terms and types was integrated into the training data. For GeoNames, context was collected for all terms and types, while for other datasets, only type-level context was used.

3. **Task-Specific Modeling.**

   * **Task A (Term Typing).** Models were trained on terms and corresponding types from the competition data. Each type was assigned a unique label, forming a dataset of term–label pairs for supervised fine-tuning of encoder models such as DeBERTa or LLaMA adapters.
   * **Task B (Taxonomy Discovery).** Hierarchical relationships were transformed into a binary classification format. Positive samples (parent–child) were labeled as 1, and negative samples (reversed or corrupted pairs) as 0, creating the final dataset used to train taxonomic relation classifiers.


Term Typing
-----------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For term typing, we use the AgrO ontology as a running example. Terms and their semantic types are split into train and test sets for supervised encoder fine-tuning and evaluation.

.. code-block:: python

   from ontolearner import train_test_split, AgrO, evaluation_report
   from ontolearner.learner.term_typing import RWTHDBISSFTLearner

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

.. code-block:: python

   learner = RWTHDBISSFTLearner(
       model_name="microsoft/deberta-v3-small",
       output_dir="./results/deberta-v3",
       device="cpu",
       num_train_epochs=30,
       per_device_train_batch_size=16,
       gradient_accumulation_steps=2,
       learning_rate=2e-5,
       max_length=64,
       seed=42,
   )

   # Load the base encoder and prepare it for supervised term typing
   learner.load(llm_id=learner.model_name)

   # Indexing (fitting) the model on the training data for the LLMs4OL task
   learner.fit(train_data, task=task)

   # Perform prediction and evaluation directly
   predicts = learner.predict(test_data, task=task)
   truth = learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Pipeline Usage
~~~~~~~~~~~~~~

The :class:`LearnerPipeline` class offers a streamlined, end-to-end wrapper for Supervised Fine-Tuning (SFT) models like :class:`RWTHDBISTermTypingLearner`. It encapsulates the full workflow—from initializing the model and its training parameters to executing training, prediction, and evaluation—in a single, clean function call.

.. code-block:: python

   # Import core modules from the OntoLearner library
   from ontolearner import LearnerPipeline, train_test_split, AgrO
   from ontolearner import RWTHDBISTermTypingLearner

   # Load the AgrO ontology.
   ontology = AgrO()
   ontology.load()
   data = ontology.extract()

   # Split the labeled term-typing data into train and test sets
   train_data, test_data = train_test_split(
       data,
       test_size=0.2,
       random_state=42,
   )

   # Configure a supervised encoder-based classifier for term typing.
   learner = RWTHDBISTermTypingLearner(
       model_name="microsoft/deberta-v3-small",
       output_dir="./results/deberta-v3",
       num_train_epochs=30,
       per_device_train_batch_size=16,
       gradient_accumulation_steps=2,
       learning_rate=2e-5,
       max_length=64,
       seed=42,
   )

   # Build the pipeline and pass raw structured objects end-to-end.
   pipeline = LearnerPipeline(
       llm=learner,
       llm_id=learner.model_name,
       ontologizer_data=False,
   )

   # Run the full learning pipeline on the term-typing task
   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       task="term-typing",
       evaluate=True,
       ontologizer_data=False,
   )

   print("Metrics:", outputs["metrics"])
   print("Elapsed time:", outputs["elapsed_time"])
   print(outputs)


Taxonomy Discovery
------------------

Loading Ontological Data
~~~~~~~~~~~~~~~~~~~~~~~~

For taxonomy discovery, we use the Chord ontology as a running example. It exposes hierarchical (parent, child) relations that can be transformed into labeled edges for taxonomic relation classification.

.. code-block:: python

   from ontolearner import train_test_split, evaluation_report
   from ontolearner import ChordOntology
   from ontolearner import RWTHDBISTaxonomyLearner

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

Next, we initialize :class:`RWTHDBISTaxonomyLearner`. This learner fine-tunes a transformer model to classify pairs of terms as positive or negative taxonomic relations (e.g., parent–child vs. non-parent–child).

.. code-block:: python

   learner = RWTHDBISTaxonomyLearner(
       model_name="microsoft/deberta-v3-small",
       output_dir="./results/",
       num_train_epochs=1,
       per_device_train_batch_size=8,
       gradient_accumulation_steps=4,
       learning_rate=2e-5,
       max_length=256,
       seed=42,
       negative_ratio=5,
       bidirectional_templates=True,
       context_json_path=None,
       ontology_name=ontology.ontology_full_name,
   )

   # Load the base model and prepare it for supervised taxonomy learning
   learner.load(llm_id=learner.model_name)

   # Fine-tune the model on the taxonomic training data
   learner.fit(train_data, task=task)

   # Perform prediction and evaluation directly
   predicts = learner.predict(test_data, task=task)
   truth = learner.tasks_ground_truth_former(data=test_data, task=task)
   metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
   print(metrics)

Pipeline Usage
~~~~~~~~~~~~~~

The pipeline example for :class:`RWTHDBISTaxonomyLearner` demonstrates how to adapt the workflow to a specific ontology and run taxonomy discovery end-to-end.

.. code-block:: python

   # Import core modules from the OntoLearner library
   from ontolearner import LearnerPipeline, train_test_split
   from ontolearner import ChordOntology, RWTHDBISTaxonomyLearner

   # Load the Chord ontology, which exposes hierarchical (parent, child) relations for taxonomy discovery
   ontology = ChordOntology()
   ontology.load()

   # Extract typed taxonomic edges and split into train/test while preserving the structured shape
   train_data, test_data = train_test_split(
       ontology.extract(),
       test_size=0.2,
       random_state=42,
   )

   learner = RWTHDBISTaxonomyLearner(
       model_name="microsoft/deberta-v3-small",
       output_dir="./results/",
       num_train_epochs=1,
       per_device_train_batch_size=8,
       gradient_accumulation_steps=4,
       learning_rate=2e-5,
       max_length=256,
       seed=42,
       negative_ratio=5,
       bidirectional_templates=True,
       context_json_path=None,
       ontology_name=ontology.ontology_full_name,
   )

   # Build the pipeline and run taxonomy discovery
   pipeline = LearnerPipeline(
       llm=learner,
       llm_id=learner.model_name,
       ontologizer_data=False,
   )

   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       task="taxonomy-discovery",
       evaluate=True,
       ontologizer_data=False,
   )

   print("Metrics:", outputs["metrics"])
   print("Elapsed time:", outputs["elapsed_time"])
   print(outputs)
