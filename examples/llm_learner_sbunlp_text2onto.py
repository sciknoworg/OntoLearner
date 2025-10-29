import os
import torch
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
