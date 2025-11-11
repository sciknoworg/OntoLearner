SBU-NLP Team
================

Description
-----------

.. sidebar:: Examples
    
    * SBU-NLP Learner Text2Onto Example: `llm_learner_sbunlp_text2onto.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_sbunlp_text2onto.py>`_
    * SBU-NLP Learner Term Typing (Zero-Shot) Example: `llm_learner_sbunlp_zs_term_typing.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_sbunlp_zs_term_typing.py>`_
    * SBU-NLP Learner Taxonomy Discovery (Few-shot) Example: `llm_learner_sbunlp_fs_taxonomy_discovery.py <https://github.com/sciknoworg/OntoLearner/blob/main/examples/llm_learner_sbunlp_fs_taxonomy_discovery.py>`_


The team participated in the LLMs4OL 2025 Shared Task, which included four subtasks:
(A) Ontological term and type extraction (Text2Onto),
(B) Term typing (Term Typing),
(C) Taxonomy discovery (Taxonomy Discovery), and
(D) Non-taxonomic relation extraction (Non-Taxonomic Relation Extraction).

The team focused on Tasks A, B and C, adopting a unified prompting-based methodology that required no supervised training or fine-tuning. Instead, they applied prompt engineering combined with stratified and simple random sampling as well as chunking-based strategies to incorporate representative examples within the context window.

Datasets

Task A: Text2Onto: Ontology extraction from domain-specific corpora in ecology, engineering, and scholarly domains.

Task B: Term Typing: Semantic typing of terms using datasets from OBI and SWEET taxonomies.

Task C: Taxonomy Discovery: Identification of hierarchical relations using OBI, Schema.org, SWEET, and MatOnto ontologies. Test instances correspond to unique types rather than document IDs.


Methodology

For Text2Onto, two prompt formats were designed — one for term extraction and another for type identification — enabling effective use of few-shot in-context learning from the provided training examples.

For Taxonomy Discovery, the focus was on detecting parent–child relationships between ontology terms. Due to the relational nature of this task, only batch prompting was employed to efficiently handle multiple type pairs per inference.


   
Loading Ontological Data
----------------------------------
We start by importing necessary components from the ontolearner package, loading ontology, and doing train-test splits.


.. code-block:: python

    from ontolearner import AutoRetrieverLearner, AgrO, train_test_split, evaluation_report

    ontology = AgrO()

    ontology.load()

    ontological_data = ontology.extract()

    train_data, test_data = train_test_split(ontological_data, test_size=0.2, random_state=42)
 


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

The pipeline example focuses on text2onto task using the SBU-NLP learner with a local LLM model. It demonstrates the complete workflow from loading data, fitting the model with few-shot examples, making predictions, and evaluating the results.

.. code-block:: python

    #Import all the required classes
    from ontolearner import SBUNLPText2OntoLearner
    from ontolearner.learner.text2onto.sbunlp import LocalAutoLLM

    # Local folder where the dataset is stored
    # This path is relative to the directory where the script is executed
    # (e.g., E:\OntoLearner\examples)
    LOCAL_DATA_DIR = "./dataset_llms4ol_2025/TaskA-Text2Onto/ecology"

    # Ensure the base directories exist
    # Creates the train and test subdirectories if they don't already exist.
    os.makedirs(os.path.join(LOCAL_DATA_DIR, 'train'), exist_ok=True)
    os.makedirs(os.path.join(LOCAL_DATA_DIR, 'test'), exist_ok=True)

    # Define local file paths: POINTING TO ALREADY SAVED FILES
    # These files are used as input for the Fit and Predict phases.
    DOCS_ALL_PATH = "./dataset_llms4ol_2025/TaskA-Text2Onto/ecology/train/documents.jsonl"
    TERMS2DOC_PATH = "./dataset_llms4ol_2025/TaskA-Text2Onto/ecology/train/terms2docs.json"
    DOCS_TEST_PATH = "./dataset_llms4ol_2025/TaskA-Text2Onto/ecology/test/text2onto_ecology_test_documents.jsonl"

    # Output files for predictions (saved directly under LOCAL_DATA_DIR/test)
    # These files will be created by the predict_terms/types methods.
    TERMS_PRED_OUT = "./dataset_llms4ol_2025/TaskA-Text2Onto/ecology/test/extracted_terms_ecology.jsonl"
    TYPES_PRED_OUT = "./dataset_llms4ol_2025/TaskA-Text2Onto/ecology/test/extracted_types_ecology.jsonl"

    #Initialize and Load Learner ---
    MODEL_ID = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    # Determine the device for inference (GPU or CPU)
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

    # Instantiate the underlying LLM helper
    # (LocalAutoLLM handles model loading and generation)
    llm_model_helper = LocalAutoLLM(device=DEVICE)

    # Instantiate the main learner class, passing the LLM helper to its constructor
    learner = SBUNLPText2OntoLearner(model=llm_model_helper, device=DEVICE)

    # Load the model (This calls llm_model_helper.load)
    LOAD_IN_4BIT = torch.cuda.is_available()
    learner.model.load(MODEL_ID, load_in_4bit=LOAD_IN_4BIT)

    # Build Few-Shot Exemplars (Fit Phase)
    # The fit method uses the local data paths to build the in-context learning prompts.
    learner.fit(
        train_docs_jsonl=DOCS_ALL_PATH,
        terms2doc_json=TERMS2DOC_PATH,
        sample_size=28,
        seed=123 # Seed for stratified random sampling stability
    )

    MAX_NEW_TOKENS = 100

    terms_written = learner.predict_terms(
        docs_test_jsonl=DOCS_TEST_PATH,
        out_jsonl=TERMS_PRED_OUT,
        max_new_tokens=MAX_NEW_TOKENS
    )
    print(f"✅ Term Extraction Complete. Wrote {terms_written} prediction lines.")

    # Type Extraction subtask
    types_written = learner.predict_types(
        docs_test_jsonl=DOCS_TEST_PATH,
        out_jsonl=TYPES_PRED_OUT,
        max_new_tokens=MAX_NEW_TOKENS
    )
    print(f"✅ Type Extraction Complete. Wrote {types_written} prediction lines.")

    try:
        # Evaluate Term Extraction using the custom F1 function and gold data
        f1_term = learner.evaluate_extraction_f1(TERMS2DOC_PATH, TERMS_PRED_OUT, key="term")
        print(f"Final Term Extraction F1: {f1_term:.4f}")

        # Evaluate Type Extraction
        f1_type = learner.evaluate_extraction_f1(TERMS2DOC_PATH, TYPES_PRED_OUT, key="type")
        print(f"Final Type Extraction F1: {f1_type:.4f}")

    except Exception as e:
        # Catches errors like missing sklearn (ImportError) or missing prediction files (FileNotFoundError)
        print(f"❌ Evaluation Error: {e}. Ensure sklearn is installed and prediction files were created.")


--------------------
Term-Typing Pipeline 
--------------------

The pipeline example focuses on term-typing task using the SBU-NLP Zero-Shot learner with the Qwen model.

.. code-block:: python

   # Import core modules from the OntoLearner library
    from ontolearner import AgrO, train_test_split, LearnerPipeline
    # Import the specific Zero-Shot Learner implementation for Term Typing
    from ontolearner import SBUNLPZSLearner

    # Load ontology and split
    # Load the AgrO ontology for type inventory and test data.
    ontology = AgrO()
    ontology.load()
    data = ontology.extract() # Extract the full set of relationships/terms

    # Split the data into train (to learn type inventory) and test (terms to predict)
    train_data, test_data = train_test_split(
        data,
        test_size=0.6, # 60% of data used for testing
        random_state=42,
    )

    # Configure the Qwen Zero-Shot learner (inference-only)
    # This learner's 'fit' phase learns the vocabulary of allowed type labels.
    llm_learner = SBUNLPZSLearner(
        # Model / decoding
        model_id="Qwen/Qwen2.5-0.5B-Instruct", # The Qwen model to load
        # device= is auto-detected
        max_new_tokens=64,         # Sufficient length for JSON list of types
        temperature=0.0,           # Ensures deterministic (greedy) output
        # token= None,             # Assuming public model access
    )

    # Build pipeline and run
    # Build the pipeline, passing the Zero-Shot Learner.
    pipe = LearnerPipeline(
        llm=llm_learner,
        llm_id=llm_learner.model_id,
        ontologizer_data=False,
        device="cpu",             #  select CUDA or CPU
    )

    # Run the full learning pipeline on the Term-Typing task
    outputs = pipe(
        train_data=train_data,
        test_data=test_data,
        task="term-typing",
        evaluate=True,
        ontologizer_data=False,
    )

    # Display the evaluation results
    print("Metrics:", outputs.get("metrics"))

    # Display total elapsed time for learning (type inventory) + prediction + evaluation
    print("Elapsed time:", outputs.get("elapsed_time"))

    # Print all returned outputs (include predictions)
    print(outputs)

---------------------------
Taxonomy Discovery Pipeline 
---------------------------

The pipeline example focuses on taxonomy-discovery task using the SBU-NLP Few-Shot learner with the Qwen model. 

.. code-block:: python

   # Import core modules from the OntoLearner library
    from ontolearner import GeoNames, train_test_split, LearnerPipeline
    # Import the specific Few-Shot Learner implementation
    from ontolearner import SBUNLPFewShotLearner

    # Load ontology and split
    # Load the GeoNames ontology for taxonomy discovery.
    # GeoNames provides geographic parent-child relationships (is-a hierarchy).
    ontology = GeoNames()
    ontology.load()
    data = ontology.extract() # Extract the list of taxonomic relationships from the ontology object

    # Split the taxonomic relationships into train and test sets
    train_data, test_data = train_test_split(
        data,
        test_size=0.6, # 60% of data used for testing (terms to find relations for)
        random_state=42,
    )

    # Configure the learner with user-defined inference args + device
    # Configure the SBUNLP Few-Shot Learner using the Qwen model.
    # This performs in-context learning via N x M batch prompting.
    llm_learner = SBUNLPFewShotLearner(
        # Model / decoding
        model_name="Qwen/Qwen2.5-0.5B-Instruct", # The Qwen model to load
        try_4bit=True,              # uses 4-bit if bitsandbytes + CUDA available for memory efficiency
        max_new_tokens=140,         # limit the length of the model's response (for JSON output)
        max_input_tokens=1500,      # limit the total prompt length (context window)
        temperature=0.0,            # set to 0.0 for deterministic output (best for structured JSON)
        top_p=1.0,                  # top-p sampling disabled with temperature=0.0

        # Grid settings (N x M prompts)
        n_train_chunks=7,           # N: split training examples (few-shot context) into 7 chunks
        m_test_chunks=7,            # M: split test terms (vocabulary) into 7 chunks (total 49 prompts)

        # Run controls
        limit_prompts=None,         # None runs all N x M prompts; set to an integer for a dry-run
        output_dir="./outputs/taskC_batches",  # Optional: dump per-prompt JSON results for debugging
    )

    # Build pipeline and run
    # Build the pipeline, passing the Few-Shot Learner.
    pipe = LearnerPipeline(
        llm=llm_learner,
        llm_id=llm_learner.model_name,
        ontologizer_data=True,      # Let the learner flatten structured ontology objects via its tasks_* helpers
        device="auto",              # automatically select CUDA or CPU
    )

    # Run the full learning pipeline on the taxonomy-discovery task
    outputs = pipe(
        train_data=train_data,
        test_data=test_data,
        task="taxonomy-discovery",
        evaluate=True,
        ontologizer_data=True,
    )

    # Display the evaluation results
    print("Metrics:", outputs.get("metrics"))

    # Display total elapsed time for training + prediction + evaluation
    print("Elapsed time:", outputs["elapsed_time"])

    # Print all returned outputs (include predictions)
    print(outputs)