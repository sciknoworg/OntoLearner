Alexbek learners
================

Description
-----------

.. sidebar:: Examples
    
    * Alexbek Learner Text2Onto Example: `llm_learner_alexbek_text2onto.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_alexbek_text2onto.py>`_
    * Alexbek Learner Term Typing Example: `llm_learner_alexbek_rf_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_alexbek_rf_term_typing.py>`_
    * Alexbek Learner Taxonomy Discovery Example: `llm_learner_alexbek_self_attn_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_alexbek_self_attn_taxonomy_discovery.py>`_
   

Prior systems for Ontology Learning (OL) often rely on heavy fine-tuning or manually designed prompts, and typically lack a unified, efficient pipeline that works across different tasks and domains.

The primary aim was to design a **modular, lightweight, and scalable system** that tackles all three core OL tasks of the LLMs4OL 2025 benchmark:
* **Task A (Text2Onto):** Joint extraction of terms (A1) and their types (A2) from raw domain documents.
* **Task B (Term Typing):** Assigning types to given terms, evaluated in both few-shot (B1–B3) and zero-shot (B4–B6) settings.
* **Task C (Taxonomy Discovery):** Inducing *is-a* relationships between types to construct hierarchical taxonomies (C1–C8).

The system targets a single unified framework that avoids full encoder fine-tuning, yet remains competitive.

The work makes three main contributions:
1.  **Unified, Modular System:** Presenting a modular LLM-based system for ontology learning, covering term extraction, term typing, and taxonomy induction across Tasks A, B, and C.
2.  **Cross-Attention for Taxonomy:** Introducing a simple yet effective dedicated **cross-attention layer** for taxonomy discovery, which enables efficient graph inference over type embeddings without full encoder fine-tuning.
3.  **Competitive Performance:** Achieving competitive results across all subtasks, including top-2 placement in multiple domains and strong zero-shot generalization[cite: 302]. The method is fully task-agnostic, lightweight, and requires no large-scale fine-tuning.

This work successfully challenges the notion that OL requires heavy fine-tuning or complex multi-component pipelines, demonstrating that a lean system built on efficient prompting and adaptive lightweight modules can compete with or outperform more expensive methods, supporting scalable, domain-agnostic ontology learning.

   
Loading Ontological Data
----------------------------------
We start by importing necessary components from the ontolearner package, loading ontology, and doing train-test splits.


.. code-block:: python

    from ontolearner import AutoRetrieverLearner, AgrO, train_test_split, evaluation_report

    ontology = AgrO()

    ontology.load()

    ontological_data = ontology.extract()

    train_data, test_data = train_test_split(ontological_data, test_size=0.2, random_state=42)

.. note::

    * ``AutoRetrieverLearner``: A wrapper class to easily configure and run retriever-based learners.

Initialize Learner
----------------------------------

Before defining the Retriever learner, choose the task you want the Retriever to perform. Available tasks has been described in `LLMs4OL Paradigms <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_. The task IDs are: 'term-typing', 'taxonomy-discovery', 'non-taxonomic-re'.

.. code-block:: python

    task = 'term-typing'

Next, initiate the learner by specifying ``top_k`` parameter and load the desired ``sentence-transformer`` based model as a retriever.

.. code-block:: python

    ret_learner = AutoRetrieverLearner(top_k=5)

    ret_learner.load(model_id='sentence-transformers/all-MiniLM-L6-v2')

    # Index the model on the training data for LLMs4OL task
    ret_learner.fit(train_data, task=task)

    predicts = ret_learner.predict(test_data, task=task)

    truth = ret_learner.tasks_ground_truth_former(data=test_data, task=task)

    metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)

    print(metrics)

You will see a evaluations results.

.. hint::

    OntoLearner supports various retrieval models, including:

    * Various `sentence-transformers <https://huggingface.co/sentence-transformers>`_ models
    * T5 models (e.g., "google/flan-t5-base")
    * Nomic-AI models


Pipeline Usage
-----------------------

.. contents::
   :local:
   :depth: 2


-------------------
Text2Onto Pipeline 
-------------------

The pipeline example focuses on **text2onto** task using AlexbekFewShotLearner with a local LLM. It illustrates term extraction and typing from domain documents, 
demonstrating how to adapt the pipeline for a different ontology or learner.

.. code-block:: python

    # LocalAutoLLM handles model loading/generation; AlexbekFewShotLearner provides fit/predict APIs
    from ontolearner.learner.text2onto.alexbek import LocalAutoLLM, AlexbekFewShotLearner

    # Local folder where the dataset is stored (relative to this script)
    DATA_DIR = "./dataset_llms4ol_2025/TaskA-Text2Onto/ecology"

    # Input paths (already saved)
    TRAIN_DOCS_PATH        = os.path.join(DATA_DIR, "train", "documents.jsonl")
    TRAIN_TERMS2DOCS_PATH  = os.path.join(DATA_DIR, "train", "terms2docs.json")
    TEST_DOCS_FULL_PATH    = os.path.join(DATA_DIR, "test", "text2onto_ecology_test_documents.jsonl")

    # Output paths
    DOC_TERMS_OUT_PATH     = os.path.join(DATA_DIR, "test", "extracted_terms_ecology.fast.jsonl")
    TERMS2TYPES_OUT_PATH   = os.path.join(DATA_DIR, "test", "terms2types_pred_ecology.fast.json")
    TYPES2DOCS_OUT_PATH    = os.path.join(DATA_DIR, "test", "types2docs_pred_ecology.fast.json")

    # Device selection
    DEVICE = (
        "cuda"
        if torch.cuda.is_available()
        else ("mps" if torch.backends.mps.is_available() else "cpu")
    )

    # Model config
    MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"
    LOAD_IN_4BIT = (DEVICE == "cuda")  # 4-bit helps on GPU

    # 1) Load LLM
    llm = LocalAutoLLM(device=DEVICE)
    llm.load(MODEL_ID, load_in_4bit=LOAD_IN_4BIT)

    # 2) Build few-shot exemplars from training split
    learner = AlexbekFewShotLearner(model=llm, device=DEVICE)
    learner.fit(
        train_docs_jsonl=TRAIN_DOCS_PATH,
        terms2doc_json=TRAIN_TERMS2DOCS_PATH,
        # use defaults for sample size/seed
    )

    # 3) Predict terms per test document
    os.makedirs(os.path.dirname(DOC_TERMS_OUT_PATH), exist_ok=True)
    num_written_doc_terms = learner.predict_terms(
        docs_test_jsonl=TEST_DOCS_FULL_PATH,
        out_jsonl=DOC_TERMS_OUT_PATH,
        # use defaults for max_new_tokens and few_shot_k
    )
    print(f"[terms] wrote {num_written_doc_terms} lines → {DOC_TERMS_OUT_PATH}")

    # 4) Predict types for extracted terms, using the JSONL we just wrote
    typing_summary = learner.predict_types_from_terms(
        doc_terms_jsonl=DOC_TERMS_OUT_PATH,   # read the predictions directly
        doc_terms_list=None,                  # (not needed when doc_terms_jsonl is provided)
        model_id=MODEL_ID,                    # reuse the same small model
        out_terms2types=TERMS2TYPES_OUT_PATH,
        out_types2docs=TYPES2DOCS_OUT_PATH,
        # use defaults for everything else
    )

    print(f"[types] {typing_summary['unique_terms']} unique terms | {typing_summary['types_count']} types")
    print(f"[saved] {TERMS2TYPES_OUT_PATH}")
    print(f"[saved] {TYPES2DOCS_OUT_PATH}")

    # 5) Small preview of term→types
    try:
        with open(TERMS2TYPES_OUT_PATH, "r", encoding="utf-8") as fin:
            preview = json.load(fin)[:3]
        print("[preview] first 3:")
        print(json.dumps(preview, ensure_ascii=False, indent=2))
    except Exception as e:
        print(f"[preview] skipped: {e}")

---------------------------
Taxonomy Discovery Pipeline 
---------------------------

The pipeline example focuses on **taxonomy-discovery** task using AlexbekCrossAttnLearner with a sentence-transformer embedding model. It illustrates inducing hierarchical relationships between types, 
demonstrating how to adapt the pipeline for a different ontology or learner.

.. code-block:: python

    from ontolearner import GeoNames, train_test_split, LearnerPipeline
    from ontolearner import AlexbekCrossAttnLearner
    # 1) Load & split
    ontology = GeoNames()
    ontology.load()
    data = ontology.extract()
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

    # 2) Configure the cross-attention learner
    cross_learner = AlexbekCrossAttnLearner(
        embedding_model="sentence-transformers/all-MiniLM-L6-v2",  # or "Qwen/Qwen2.5-1.5B-... (if wrapped as ST)"
        device="cpu",
        num_heads=8,
        lr=5e-5,
        weight_decay=0.01,
        num_epochs=1,
        batch_size=256,
        neg_ratio=1.0,
        output_dir="./results/crossattn/",
        seed=42,
    )

    # 3) Build pipeline
    pipeline = LearnerPipeline(
        llm=cross_learner,     # <- our learner
        llm_id="cross-attn",   # label for bookkeeping
        ontologizer_data=False # pass raw ontology objects as in your example
    )

    # 4) Train + predict + evaluate
    outputs = pipeline(
        train_data=train_data,
        test_data=test_data,
        task="taxonomy-discovery",
        evaluate=True,
        ontologizer_data=False,
    )

    print("Metrics:", outputs.get("metrics"))
    print("Elapsed time:", outputs["elapsed_time"])
    print(outputs)


--------------------
Term Typing Pipeline 
--------------------

The pipeline example focuses on **term-typing** task using AlexbekRFLearner with a retriever model. It illustrates type assignment to given terms, 
demonstrating how to adapt the pipeline for a different ontology or learner.

.. code-block:: python

    # Import core modules from the OntoLearner library
    from ontolearner import GeoNames, train_test_split, LearnerPipeline
    from ontolearner import AlexbekRFLearner   # A random-forest term-typing learner over text+graph features

    # Load the GeoNames ontology and extract labeled term-typing data

    ontology = GeoNames()
    ontology.load()

    data = ontology.extract()

    # Split the labeled term-typing data into train and test sets
    train_data, test_data = train_test_split(
        data,
        test_size=0.2,
        random_state=42
    )

    # Configure the RF-based learner (embeddings + optional graph features)
    #    - device: "cpu" or "cuda"
    #    - threshold: decision threshold for multi-label assignment
    #    - use_graph_features: include ontology-graph-derived features if available
    rf_learner = AlexbekRFLearner(
        device="cpu",            # switch to "cuda" if you have a GPU
        batch_size=16,
        max_length=512,          # max tokenizer length for embedding model inputs
        threshold=0.30,          # probability cutoff for assigning each type
        use_graph_features=True  # set False for pure RF on text embeddings only
    )

    # Build the pipeline and pass raw structured objects end-to-end.
    pipe = LearnerPipeline(
        retriever=rf_learner,
        retriever_id="intfloat/e5-base-v2",   # or "Qwen/Qwen3-Embedding-4B" if you have sufficient GPU memory
        ontologizer_data=True,                # True if data is already {"term": ..., "types": [...], ...}
        device="cpu",
        batch_size=16
    )

    # Run the full learning pipeline on the term-typing task
    outputs = pipe(
        train_data=train_data,
        test_data=test_data,
        task="term-typing",
        evaluate=True,
        ontologizer_data=True,
    )

    # Display evaluation summary and runtime
    print("Metrics:", outputs.get("metrics"))

    print("Elapsed time:", outputs["elapsed_time"])

    print(ontology)