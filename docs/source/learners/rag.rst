Retrieval Augmented Generation
==============================

.. sidebar:: Examples

    * RAG Learner Example: `rag_learner.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/rag_learner.py>`_
    * RAG Learner Pipeline Usage Example: `rag_learner_pipeline_usage.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/rag_learner_pipeline_usage.py>`_

Retrieval Augmented Generation (RAG) learners combine the strengths of both retrieval models
and large language models to perform ontology learning tasks. RAG learners operate in two main steps: 1) **Retrieval** component that finds the most relevant examples from the training data based on similarity to the input query. 2) **Generation** component that uses  retrieved examples as context to generate a response. The methodology behind RAG learners combines vector retrieval with generative language modeling to enhance ontology learning tasks. This hybrid approach addresses the limitations of using LLMs alone by grounding the model's responses in specific ontological examples from the training data. By encoding ontological elements into a vector space, the retriever can identify semantically similar concepts, relations, or taxonomic structures. These retrieved examples serve as few-shot demonstrations that provide the LLM with domain-specific context, enabling more accurate and consistent ontological inferences. This approach is particularly effective for specialized domains where the model's pre-trained knowledge may be insufficient or where precise ontological alignments are critical.

Loading Ontological Data
----------------------------
We start by importing necessary components from the ontolearner package, loading ontology, and doing train-test splits.


.. code-block:: python

    # Import components from OntoLearner for ontology-based learning using LLMs and retrievers
    from ontolearner import (
        AutoLLMLearner,         # Wrapper for zero-shot LLM-based learners
        AutoRetrieverLearner,   # Wrapper for dense retriever models
        AutoRAGLearner,         # Combines LLM + retriever into a RAG pipeline
        AgrO,                   # Example agricultural ontology
        train_test_split,       # Helper function for data splitting
        LabelMapper,            # Maps ontology labels to/from textual representations
        StandardizedPrompting   # Standard prompting strategy across tasks
        evaluation_report
    )

    # Load the AgrO ontology (an agricultural domain ontology)
    ontology = AgrO()
    ontology.load()
    ontological_data = ontology.extract(),

    # Extract structured data from the ontology and split into train/test sets
    train_data, test_data = train_test_split(
        ontological_data,
        test_size=0.2,          # Use 20% for testing
        random_state=42         # Seed for reproducibility
    )

.. note::

    * ``AutoRAGLearner``: A wrapper class to easily configure and run RAG-based learners.

Initialize Learner
--------------------


.. code-block:: python

    task = 'non-taxonomic-re'

    # Provide your huggingface token for LLM access
    token = '...'

    # Initialize the LLM learner with prompting and label mapping strategies
    llm_learner = AutoLLMLearner(
        prompting=StandardizedPrompting,  # Use a pre-defined prompt format
        label_mapper=LabelMapper(),       # Convert between label formats and natural language
        token=token                       # API token to access the LLM
    )

    # Initialize the retriever to find top-k relevant facts or examples
    retriever_learner = AutoRetrieverLearner(top_k=2)  # Use top 2 retrieved candidates

    # Create a RAG (Retrieval-Augmented Generation) pipeline by combining LLM and retriever
    rag_learner = AutoRAGLearner(
        llm=llm_learner,
        retriever=retriever_learner
    )

    # Load the retriever and LLM models by their names or IDs
    rag_learner.load(
        retriever_id='sentence-transformers/all-MiniLM-L6-v2',   # Sentence-level transformer for retrieval
        llm_id='Qwen/Qwen2.5-0.5B-Instruct'                      # Small-scale instruction-following LLM
    )

    # Train (or adapt) the RAG model on the training data for the selected task
    rag_learner.fit(train_data, task=task)

    # Predict the output on the test set using the trained RAG model
    truth = rag_learner.predict(test_data, task=task)

    # do the evaluation.
    metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)

    print(metrics)

Pipeline Usage
---------------------

.. code-block:: python

    # Import core modules from the OntoLearner library
    from ontolearner import LearnerPipeline, AgrO, train_test_split

    # Load the AgrO ontology, which contains concepts related to wines, their properties, and categories
    ontology = AgrO()
    ontology.load()  # Load entities, types, and structured term annotations from the ontology
    ontological_data = ontology.extract(),
    # Extract term-typing instances and split into train and test sets
    train_data, test_data = train_test_split(
        ontological_data,
        test_size=0.2,          # Use 20% of the data for evaluation
        random_state=42         # Ensure reproducibility of the data split
    )
    # Initialize a multi-component learning pipeline (retriever + LLM)
    # This configuration enables a Retrieval-Augmented Generation (RAG) setup
    pipeline = LearnerPipeline(
        retriever_id='sentence-transformers/all-MiniLM-L6-v2',      # Dense retriever model for nearest neighbor search
        llm_id='Qwen/Qwen2.5-0.5B-Instruct',                        # Lightweight instruction-tuned LLM for reasoning
        hf_token='...',                                             # Hugging Face token for accessing gated models
        batch_size=32,                                              # Batch size for training/prediction if supported
        top_k=5                                                     # Number of top retrievals to include in RAG prompting
    )
    # Run the pipeline: training, prediction, and evaluation in one call
    outputs = pipeline(
        train_data=train_data,
        test_data=test_data,
        evaluate=True,              # Compute metrics like precision, recall, and F1
        task='term-typing'          # Specifies the task
    )
    # Print final evaluation metrics
    print("Metrics:", outputs['metrics'])
    # Print the total time taken for the full pipeline execution
    print("Elapsed time:", outputs['elapsed_time'])
    # Print all outputs (including predictions)
    print(outputs)
