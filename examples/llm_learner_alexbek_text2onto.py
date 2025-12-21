import os
import dspy

# Import ontology loader/manager
from ontolearner.ontology import OM

# Import Text2Onto utilities: synthetic sample generation + dataset splitting
from ontolearner.text2onto import SyntheticGenerator, SyntheticDataSplitter

# Import pipeline orchestrator + the specific Few-Shot learner you want to run
from ontolearner import LearnerPipeline
from ontolearner.learner.text2onto import AlexbekRAGFewShotLearner

# ---- DSPy -> Ollama (LiteLLM-style) ----
# Configure DSPy to send prompts to a locally running Ollama server (via LiteLLM-compatible args).
LLM_MODEL_ID = "ollama/llama3.2:3b"      # use your pulled Ollama model
LLM_API_KEY  = "NA"                      # Ollama local doesn't use a key; kept for interface compatibility
LLM_BASE_URL = "http://localhost:11434"  # default Ollama server endpoint

# Create the DSPy language model wrapper.
# Note: DSPy uses LiteLLM-style parameters under the hood when given model/base_url/api_key.
dspy_llm = dspy.LM(
    model=LLM_MODEL_ID,
    cache=True,          # cache generations to speed up repeated runs
    max_tokens=4000,     # generous context for synthetic generation prompts
    temperature=0,       # deterministic output; helpful for reproducibility
    api_key=LLM_API_KEY,
    base_url=LLM_BASE_URL,
)

# Register the LM globally so DSPy modules (and generator internals) use it.
dspy.configure(lm=dspy_llm)

# ---- Synthetic generation configuration ----
# Allow scaling generation without editing code by using environment variables:
#   TEXT2ONTO_BATCH=20 TEXT2ONTO_WORKERS=2 python script.py
pseudo_sentence_batch_size = int(os.getenv("TEXT2ONTO_BATCH", "10"))
max_worker_count_for_llm_calls = int(os.getenv("TEXT2ONTO_WORKERS", "1"))

# Instantiate the generator that turns ontology structures into pseudo-text samples.
text2onto_synthetic_generator = SyntheticGenerator(
    batch_size=pseudo_sentence_batch_size,       # number of samples requested per batch
    worker_count=max_worker_count_for_llm_calls, # parallel LLM calls (increase if your machine can handle it)
)

# ---- Load ontology and extract structured data ----
# OM loads the ontology configured in your OntoLearner setup and exposes domain metadata.
ontology = OM()
ontology.load()
ontological_data = ontology.extract()  # structured: term typings, taxonomies, relations, etc.

# ---- Generate synthetic Text2Onto samples ----
# Uses the extracted ontology structures + domain/topic to create synthetic training examples.
synthetic_data = text2onto_synthetic_generator.generate(
    ontological_data=ontological_data,
    topic=ontology.domain
)

# ---- Dataset splitter ----
# Wrap the synthetic dataset with a splitter utility for reproducible partitioning.
splitter = SyntheticDataSplitter(
    synthetic_data=synthetic_data,
    onto_name=ontology.ontology_id  # used to tag/identify outputs for this ontology
)

# Optional sanity checks to verify what was extracted from the ontology.
print(f"term types: {len(ontological_data.term_typings)}")
print(f"taxonomic relations: {len(ontological_data.type_taxonomies.taxonomies)}")
print(f"non-taxonomic relations: {len(ontological_data.type_non_taxonomic_relations.non_taxonomies)}")

# ---- Split into train/val/test ----
# val=0.0 keeps the API consistent while skipping validation split for this run.
train_data, val_data, test_data = splitter.train_test_val_split(train=0.8, val=0.0, test=0.2)

# ---- Configure the Few-Shot learner for Text2Onto ----
# This learner will be used by the pipeline to learn/predict from Text2Onto-style samples.
text2ontolearner = AlexbekRAGFewShotLearner(
    llm_model_id="Qwen/Qwen2.5-0.5B-Instruct",               # generator model used inside the learner
    retriever_model_id="sentence-transformers/all-MiniLM-L6-v2",  # embedding model for retrieval
    device="cpu",                                            # set "cuda" if you have GPU support
    top_k=3,                                                 # number of retrieved examples/chunks
    max_new_tokens=256,                                      # response length for the learner's generator
    use_tfidf=True,                                          # optional lexical retrieval alongside embeddings
)

# ---- Build pipeline ----
# LearnerPipeline orchestrates training/prediction/evaluation for the chosen task.
pipe = LearnerPipeline(
    llm=text2ontolearner,                   # the learner implementation used by the pipeline
    llm_id="Qwen/Qwen2.5-0.5B-Instruct",    # label/id recorded with results
    ontologizer_data=False,                 # whether to run Ontologizer-related processing
)

# ---- Run end-to-end (train -> predict -> evaluate) ----
outputs = pipe(
    train_data=train_data,
    test_data=test_data,
    task="text2onto",
    evaluate=True,                          # compute evaluation metrics on the test set
    ontologizer_data=False,                 # keep consistent with pipeline setting above
)

# ---- Display results ----
# Metrics typically include task-specific scores (depends on OntoLearner implementation).
print("Metrics:", outputs.get("metrics"))

# Total elapsed time for training + prediction + evaluation.
print("Elapsed time:", outputs["elapsed_time"])

# Print everything returned (often includes predictions, logs, artifacts, etc.)
print(outputs)
