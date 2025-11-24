import os
import json
import torch

# LocalAutoLLM handles model loading/generation; AlexbekFewShotLearner provides fit/predict APIs
from ontolearner.learner.text2onto.alexbek import LocalAutoLLM, AlexbekFewShotLearner

# Local folder where the dataset is stored (relative to this script)
DATA_DIR = "./dataset_llms4ol_2025/TaskA-Text2Onto/ecology"

# Input paths (already saved)
TRAIN_DOCS_PATH = os.path.join(DATA_DIR, "train", "documents.jsonl")
TRAIN_TERMS2DOCS_PATH = os.path.join(DATA_DIR, "train", "terms2docs.json")
TEST_DOCS_FULL_PATH = os.path.join(
    DATA_DIR, "test", "text2onto_ecology_test_documents.jsonl"
)

# Output paths
DOC_TERMS_OUT_PATH = os.path.join(
    DATA_DIR, "test", "extracted_terms_ecology.fast.jsonl"
)
TERMS2TYPES_OUT_PATH = os.path.join(
    DATA_DIR, "test", "terms2types_pred_ecology.fast.json"
)
TYPES2DOCS_OUT_PATH = os.path.join(
    DATA_DIR, "test", "types2docs_pred_ecology.fast.json"
)

# Device selection
DEVICE = (
    "cuda"
    if torch.cuda.is_available()
    else ("mps" if torch.backends.mps.is_available() else "cpu")
)

# Model config
MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"
LOAD_IN_4BIT = DEVICE == "cuda"  # 4-bit helps on GPU

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
    doc_terms_jsonl=DOC_TERMS_OUT_PATH,  # read the predictions directly
    doc_terms_list=None,  # (not needed when doc_terms_jsonl is provided)
    model_id=MODEL_ID,  # reuse the same small model
    out_terms2types=TERMS2TYPES_OUT_PATH,
    out_types2docs=TYPES2DOCS_OUT_PATH,
    # use defaults for everything else
)

print(
    f"[types] {typing_summary['unique_terms']} unique terms | {typing_summary['types_count']} types"
)
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
