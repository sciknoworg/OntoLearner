Quickstart
================

Welcome to OntoLearner! This hands-on guide will get you performing ontology learning with large language models in under 5 minutes.

.. note::
   **New to OntoLearner?** Make sure you've installed the library first. See the :doc:`installation` guide for setup instructions.

Your First Ontology Learning Task
------------------------------------
Here's a complete example that predicts wine types using AI:

.. code-block:: python

    from ontolearner import LearnerPipeline, Wine, train_test_split

    # 1. Load a pre-built ontology (downloads automatically)
    ontology = Wine()
    ontology.load()
    data = ontology.extract()

    # 2. Split data for training and testing
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

    # 3. Create an AI learning pipeline
    pipeline = LearnerPipeline(
        task="term-typing",  # Predict: "What type of wine is Chardonnay?"
        retriever_id="sentence-transformers/all-MiniLM-L6-v2",
        llm_id="mistralai/Mistral-7B-Instruct-v0.1"
    )

    # 4. Train and evaluate the AI model
    results, metrics = pipeline.fit_predict_evaluate(
        train_data=train_data,
        test_data=test_data,
        top_k=3,
        test_limit=5
    )

    # 5. See how well it performed
    print(f"F1-Score: {metrics['avg_f1_score']:.3f}")
    print(f"Exact Match: {metrics['avg_exact_match']:.3f}")


Try Different AI Approaches
------------------------------
Want to experiment? OntoLearner offers three AI approaches:

.. code-block:: python

    # RAG (Best Results) - Combines retrieval + LLM
    pipeline = LearnerPipeline(
        task="term-typing",
        retriever_id="sentence-transformers/all-MiniLM-L6-v2",
        llm_id="mistralai/Mistral-7B-Instruct-v0.1"
    )

    # LLM-Only - Pure language model reasoning
    from ontolearner import AutoLearnerLLM
    pipeline = LearnerPipeline(
        task="taxonomy-discovery",
        llm=AutoLearnerLLM(),
        llm_id="mistralai/Mistral-7B-Instruct-v0.1"
    )

    # Retrieval-Only - Fast semantic similarity
    from ontolearner import BERTRetrieverLearner
    pipeline = LearnerPipeline(
        task="non-taxonomy-discovery",
        retriever=BERTRetrieverLearner(),
        retriever_id="sentence-transformers/all-MiniLM-L6-v2"
    )

Three Types of AI Learning Tasks
---------------------------------
OntoLearner can teach AI to understand three types of knowledge:

.. code-block:: python

    # Task 1: Term Typing - "What type is Chardonnay?"
    pipeline = LearnerPipeline(task="term-typing", ...)
    # → Answer: "WhiteWine"

    # Task 2: Taxonomy Discovery - "Is Wine a parent of RedWine?"
    pipeline = LearnerPipeline(task="taxonomy-discovery", ...)
    # → Answer: True

    # Task 3: Relation Discovery - "What's the relationship between Wine and Grape?"
    pipeline = LearnerPipeline(task="non-taxonomy-discovery", ...)
    # → Answer: "madeFrom"

**Want to try all three?** Just change the ``task`` parameter and run the same code from our first example!


Explore 100+ Ready-to-Use Ontologies
---------------------------------------
Swap out ``Wine()`` for any domain that interests you:

.. code-block:: python

    from ontolearner import ENVO, ChEBI, MGED, AFO

    # 🌱 Environmental science
    ontology = ENVO()

    # ⚗️ Chemistry
    ontology = ChEBI()

    # 🧬 Gene expression
    ontology = MGED()

    # 🚜 Agriculture
    ontology = AFO()

**Available domains:** Biology • Chemistry • Medicine • Agriculture • Environment • Geography • Industry • Materials Science • Law • Finance • and more!


Quick Customizations
----------------------
**Try different AI models:**

.. code-block:: python

    # Swap in different models
    pipeline = LearnerPipeline(
        task="term-typing",
        llm_id="meta-llama/Llama-3.1-8B-Instruct",  # Different LLM
        retriever_id="sentence-transformers/all-mpnet-base-v2"  # Different retriever
    )

What's Next?
---------------
→ :doc:`learning_tasks/learning_tasks` - Deep dive into all three tasks
→ :doc:`learning_tasks/llms4ol` - Advanced LLM techniques
→ :doc:`ontologizer/adding_ontologies` - Add your own ontologies

**Congratulations!** 🎉 You've just trained AI to understand ontological knowledge. Welcome to the future of knowledge engineering!


Quick Tutorial: Using OntoLearner with AgrO Ontology
=====================================================

This tutorial demonstrates how to use the `OntoLearner` framework in a Google Colab environment for ontology learning tasks. We will walk through ontology loading, data preparation, learner configuration, and evaluation using the AgrO ontology.

.. contents::
   :local:
   :depth: 2

1. Installation
---------------

First, install the required dependencies in your Colab or local environment:

.. code-block:: python

   !pip install ontolearner sentence-transformers qwen

Explanation:

- `ontolearner`: Core library for ontology learning and benchmarking.
- `sentence-transformers`: Provides pretrained models for semantic retrieval (used in RAG pipelines).
- `qwen`: Lightweight LLM for instruction-following inference (ensure compatibility with HuggingFace).

2. Load the Ontology
--------------------

OntoLearner provides built-in access to several standard ontologies. Here we use the `AgrO` ontology:

.. code-block:: python

   from ontolearner import AgrO

   ontology = AgrO()
   ontology.load()

Explanation:

- `AgrO()` is a dataset wrapper class included in OntoLearner.
- `.load()` downloads and parses the OWL/RDF ontology into an internal format.

3. Extract and Split the Data
-----------------------------

Once the ontology is loaded, we extract the training examples and split them into training and testing subsets:

.. code-block:: python

   from ontolearner import train_test_split

   train_data, test_data = train_test_split(
       ontology.extract(),
       test_size=0.2,
       random_state=42
   )

Explanation:

- `.extract()` retrieves candidate triples or axioms for a selected learning task.
- `train_test_split()` is a utility function for random shuffling and splitting (80/20 here).

4. Configure the Learning Pipeline
----------------------------------

We now configure the learner pipeline using a small instruction-tuned model (`Qwen`) and a retriever model:

.. code-block:: python

   from ontolearner import LearnerPipeline

   pipeline = LearnerPipeline(
       retriever_id='sentence-transformers/all-MiniLM-L6-v2',
       llm_id='Qwen/Qwen2.5-0.5B-Instruct',
       hf_token='<YOUR_HF_TOKEN>',
       batch_size=16,
       top_k=3
   )

Explanation:

- `retriever_id`: Semantic retriever that retrieves relevant context from ontology fragments.
- `llm_id`: The instruction-following language model used to generate candidate outputs.
- `top_k`: Number of retrieved examples passed to the LLM (used in RAG setup).
- `hf_token`: Required for loading gated models from Hugging Face.

5. Run the Pipeline
-------------------

Once configured, the pipeline is executed on the training and test data:

.. code-block:: python

   outputs = pipeline(
       train_data=train_data,
       test_data=test_data,
       evaluate=True,
       task='non-taxonomic-re'
   )

Explanation:

- `task`: One of `term-typing`, `taxonomy-discovery`, or `non-taxonomic-re`.
- `evaluate=True`: Computes performance metrics like precision, recall, and F1-score.
- Returns a dictionary with predictions, metrics, logs, and timing.

6. Evaluate the Results
------------------------

You can inspect the metrics and runtime performance:

.. code-block:: python

   print("Metrics:", outputs['metrics'])
   print("Elapsed time:", outputs['elapsed_time'])

Explanation:

- Useful to monitor model accuracy and speed.
- Helps compare different LLM/retriever configurations across tasks.

7. Explore Predictions
-----------------------

You can examine a few sample predictions for inspection:

.. code-block:: python

   import pandas as pd

   pd.DataFrame(outputs['predictions'][:5])

Explanation:

- Displays the first 5 predictions in a readable format.
- Each row may include the input, predicted output, true label (if available), and confidence scores.

8. Run in Google Colab
-----------------------

To interactively run this tutorial, use the Colab notebook provided here:

`Open in Colab <https://colab.research.google.com/drive/1DuElAyEFzd1vtqTjDEXWcc0zCbiV2Yee?usp=sharing>`_

.. note::

   Ensure your Hugging Face token has access to gated models like `Qwen2.5-0.5B-Instruct`. You can get one at https://huggingface.co/settings/tokens.

---

This quickstart guide should help you get started with `OntoLearner` in minutes. For more complex tasks or datasets, refer to the full documentation and examples.
