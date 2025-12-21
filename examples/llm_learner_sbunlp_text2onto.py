import os
import dspy

# Import ontology loader/manager and Text2Onto utilities
from ontolearner.ontology import OM
from ontolearner.text2onto import SyntheticGenerator, SyntheticDataSplitter

# Import the pipeline orchestrator and the specific Few-Shot learner for Text2Onto
from ontolearner import LearnerPipeline
from ontolearner.learner.text2onto import SBUNLPFewShotLearner

# ---- DSPy -> Ollama (LiteLLM-style) ----
# Configure DSPy to send prompts to a locally running Ollama server.
LLM_MODEL_ID = "ollama/llama3.2:3b"
LLM_API_KEY = "NA"  # Ollama local doesn't use a key; kept for interface compatibility.
LLM_BASE_URL = "http://localhost:11434"  # default Ollama endpoint

# Create the DSPy language model wrapper (LiteLLM-compatible settings)
dspy_llm = dspy.LM(
    model=LLM_MODEL_ID,
    cache=True,          # cache generations to speed up iterative runs
    max_tokens=4000,
    temperature=0,       # deterministic output; useful for reproducible synthetic data
    api_key=LLM_API_KEY,
    base_url=LLM_BASE_URL,
)

# Register the LM globally so DSPy modules (and generator internals) use it
dspy.configure(lm=dspy_llm)

# ---- Synthetic generation configuration ----
# Allow scaling generation without code edits via environment variables:
#   TEXT2ONTO_BATCH=20 TEXT2ONTO_WORKERS=2 python script.py
batch_size = int(os.getenv("TEXT2ONTO_BATCH", "10"))
worker_count = int(os.getenv("TEXT2ONTO_WORKERS", "1"))

# Instantiate the generator that turns ontology structures into pseudo-text samples
text2onto_synthetic_generator = SyntheticGenerator(
    batch_size=batch_size,       # number of samples requested per batch
    worker_count=worker_count,   # parallel LLM calls (increase if your machine can handle it)
)

# ---- Load ontology and extract structured data ----
# OM loads the ontology configured in your OntoLearner setup and exposes its domain metadata.
ontology = OM()
ontology.load()
ontological_data = ontology.extract()  # structured: term typings, taxonomies, relations, etc.

# ---- Generate synthetic Text2Onto samples ----
# Uses the ontology's extracted structures + domain/topic to create synthetic training examples.
synthetic_data = text2onto_synthetic_generator.generate(
    ontological_data=ontological_data,
    topic=ontology.domain,
)

# Optional sanity checks to verify what was extracted from the ontology
print(f"term types: {len(ontological_data.term_typings)}")
print(f"taxonomic relations: {len(ontological_data.type_taxonomies.taxonomies)}")
print(f"non-taxonomic relations: {len(ontological_data.type_non_taxonomic_relations.non_taxonomies)}")

# ---- Split into train/val/test ----
# Wrap the synthetic dataset with a splitter utility for reproducible partitioning.
splitter = SyntheticDataSplitter(
    synthetic_data=synthetic_data,
    onto_name=ontology.ontology_id,  # used to tag/identify outputs for this ontology
)

# Create splits for training and evaluation.
# val=0.0 keeps the API consistent while skipping validation split in this run.
train_data, val_data, test_data = splitter.train_test_val_split(
    train=0.8,
    val=0.0,
    test=0.2,
)

# ---- Configure the Few-Shot learner for Text2Onto ----
# This learner will be used by the pipeline to learn/predict from Text2Onto-style samples.
text2ontolearner = SBUNLPFewShotLearner(
    llm_model_id="Qwen/Qwen2.5-0.5B-Instruct",
    device="cpu",
    max_new_tokens=256,
)

# Build pipeline and run
# Build the pipeline, passing the Few-Shot Learner.
pipe = LearnerPipeline(
    llm=text2ontolearner,
    llm_id="Qwen/Qwen2.5-0.5B-Instruct",
    ontologizer_data=False,
)

# Run the full learning pipeline on the text2onto task
outputs = pipe(
    train_data=train_data,
    test_data=test_data,
    task="text2onto",
    evaluate=True,
    ontologizer_data=True,
)

# Display the evaluation results
print("Metrics:", outputs.get("metrics"))

# Display total elapsed time for training + prediction + evaluation
print("Elapsed time:", outputs["elapsed_time"])

# Print all returned outputs (include predictions)
print(outputs)
