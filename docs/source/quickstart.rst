Quickstart Guide
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
