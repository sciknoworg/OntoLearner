import os

from openai import OpenAI
from ontolearner import LearnerPipeline, train_test_split
from ontolearner.learner.primitive import HybridAISquaredSFTLearner
from ontolearner.ontology import FOAF
from ontolearner.text2onto import (
    SyntheticGenerator,
    SyntheticDataPreprocessor,
)
# Configuration
# HybridAI-Squared fine-tunes a Hugging Face model locally through transformers, not an API model.
# The submission fine-tuned Qwen/Qwen3-14B in 4-bit on a GPU; on CPU, a small Qwen3 model is fine-tuned in full
# precision instead.
learner_device = os.getenv("HYBRIDAI_DEVICE", "cpu")
learner_model_id = os.getenv(
    "HYBRIDAI_MODEL_ID",
    "Qwen/Qwen3-0.6B" if learner_device == "cpu" else "Qwen/Qwen3-14B",
)
model_id = os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct")
api_key = os.getenv("OPENAI_API_KEY")
hf_token = os.getenv("HF_TOKEN", "")

if not api_key:
    raise EnvironmentError("Set OPENAI_API_KEY before running.")

print("\nSTEP 1: Loading the FOAF ontology")
ontology = FOAF()
ontology.load()

data = ontology.extract()

# FOAF is a very small ontology. Its term typings, and most of its non-taxonomic relations, only state that
# each class is a Class, so the examples use its taxonomy (is-a relations) only.
data.term_typings = []
data.type_non_taxonomic_relations.non_taxonomies = []
print("Taxonomic relations:", len(data.type_taxonomies.taxonomies))

print("\nSTEP 2: Splitting the ontology into train and test parts")
# The train and test documents are generated from different relations.
train_ontology, test_ontology = train_test_split(
    data,
    test_size=0.5,
    random_state=42
)
print("Train taxonomies:", len(train_ontology.type_taxonomies.taxonomies))
print("Test taxonomies:", len(test_ontology.type_taxonomies.taxonomies))

print("\nSTEP 3: Loading the dataset generator")
generator = SyntheticGenerator(
    model_id=model_id,
    token=hf_token,
    extraction_method="openai",
    openai_api_key=api_key,
    openai_model="gpt-4o-mini",
    batch_size=5,
    generation_batch_size=2,
    min_pseudo_sentences=1,
    max_input_length=2000,
    max_new_tokens=2000,
)
print("Generator ready:", model_id)

print("\nSTEP 4: Generating synthetic TRAIN documents")
train_synthetic = generator.generate(
    ontological_data=train_ontology, topic=ontology.domain
)
print("Generated train documents:", len(train_synthetic.generated_docs))

print("\nSTEP 5: Generating synthetic TEST documents")
test_synthetic = generator.generate(
    ontological_data=test_ontology, topic=ontology.domain
)
print("Generated test documents:", len(test_synthetic.generated_docs))

print("\nSTEP 6: Initializing the preprocessor")
# One preprocessor for train and test: both get the same text cleaning, six-stage deep cleaning and LLM-judge
# alignment filter, and are then turned into expansion samples (each record's triples split into an initial ontology
# and the triples that extend it; records with nothing to extend are dropped).
preprocessor = SyntheticDataPreprocessor(
    client=OpenAI(api_key=api_key),
    task="ontology_expansion",
    random_state=42,
)

print("\nSTEP 7: Preprocessing TRAIN documents")
train_data = preprocessor.preprocess(train_synthetic, train_ontology)
print("Train samples:", len(train_data))

print("\nSTEP 8: Preprocessing TEST documents")
test_data = preprocessor.preprocess(test_synthetic, test_ontology)
print("Test samples:", len(test_data))

# The preprocessor drops documents whose text does not support their triples. With a small
# generator and a small ontology, a split can end up empty. Fine-tuning holds out part of the
# training samples for early stopping, so it needs at least two.
if len(train_data) < 2 or not test_data:
    raise ValueError(
        "Fine-tuning needs at least two training samples and one test sample "
        f"(train: {len(train_data)}, test: {len(test_data)}). Run again, or use a larger "
        "generator, e.g. set TEXT2ONTO_MODEL_ID=Qwen/Qwen2.5-1.5B-Instruct."
    )

print("\nSTEP 9: Running the HybridAI-Squared fine-tuned learner through LearnerPipeline", flush=True)
# Fitting trains a LoRA adapter on train_data; predicting uses it for all new triples (0.9013 in the submission).
# The adapter is saved to ./results/hybridaisquared/adapter; pass adapter_path= to reuse it without retraining.
if learner_device == "cpu":
    # Quick CPU run: full-precision LoRA, short answers without Qwen3 reasoning.
    learner = HybridAISquaredSFTLearner(
        model_id=learner_model_id,
        device="cpu",
        output_dir="./results/hybridaisquared",
        max_new_tokens=512,
        temperature=0.0,
        enable_thinking=False,
    )
else:
    # The submission's settings: 4-bit LoRA training, reasoning on, up to 20,000 new tokens.
    learner = HybridAISquaredSFTLearner(
        model_id=learner_model_id,
        device=learner_device,
        output_dir="./results/hybridaisquared",
    )
print("Learner model:", learner.model_id, "on", learner_device)

# llm_id must be the learner's Hugging Face base model: the pipeline passes it to learner.load(model_id=llm_id).
pipe = LearnerPipeline(
    llm=learner,
    llm_id=learner.model_id,
    ontologizer_data=False,
)

# Fits on train_data, predicts test_data with the answers hidden, and evaluates the predictions.
outputs = pipe(
    train_data=train_data,
    test_data=test_data,
    task="ontology_expansion",
    evaluate=True,
    ontologizer_data=False,
)

print("Metrics:", outputs.get("metrics"))
print("Elapsed time:", outputs["elapsed_time"])