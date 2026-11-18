import os

from openai import OpenAI
from ontolearner import LearnerPipeline, train_test_split
from ontolearner.learner.primitive import HybridAISquaredPerRelationLearner
from ontolearner.ontology import BBCCoreConcepts
from ontolearner.text2onto import (
    SyntheticGenerator,
    SyntheticDataPreprocessor,
)
# Configuration
# HybridAI-Squared runs a Hugging Face model locally through transformers, not an API model.
# The submission used Qwen/Qwen3-30B-A3B on a large GPU; on CPU, a small Qwen3 model is used instead.
learner_device = os.getenv("HYBRIDAI_DEVICE", "cpu")
learner_model_id = os.getenv(
    "HYBRIDAI_MODEL_ID",
    "Qwen/Qwen3-0.6B" if learner_device == "cpu" else "Qwen/Qwen3-30B-A3B",
)
model_id = os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-1.5B-Instruct")
api_key = os.getenv("OPENAI_API_KEY")
hf_token = os.getenv("HF_TOKEN", "")

if not api_key:
    raise EnvironmentError("Set OPENAI_API_KEY before running.")

print("\nSTEP 1: Loading the BBC Core Concepts ontology")
ontology = BBCCoreConcepts()
ontology.load()

data = ontology.extract()

# BBC Core Concepts is a small, general ontology (people, places, events, organisations, themes) with 25 is-a
# relations and several subclasses per class. An expansion sample needs a document with at least two relations to
# the same parent, which a flatter ontology such as FOAF rarely gives. Only the taxonomy (is-a relations) is used.
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
# generator and a small ontology, a split can end up empty. The zero-shot learner does not
# use the training samples, so only the test samples are required.
if not test_data:
    raise ValueError(
        "No usable expansion test samples were generated. Run again, or use a larger "
        "generator, e.g. set TEXT2ONTO_MODEL_ID=Qwen/Qwen2.5-1.5B-Instruct."
    )

print("\nSTEP 9: Running the HybridAI-Squared per-relation learner through LearnerPipeline", flush=True)
# One prompt each for is-a, instance-of and the other relations (0.7113 in the submission).
# categories=7 gives five relations their own prompt; chain=True lets each prompt see the earlier predictions.
if learner_device == "cpu":
    # Quick CPU run: short answers without Qwen3 reasoning.
    learner = HybridAISquaredPerRelationLearner(
        model_id=learner_model_id,
        categories=3,
        device="cpu",
        max_new_tokens=512,
        temperature=0.0,
        enable_thinking=False,
    )
else:
    # The submission's settings: reasoning on, up to 20,000 new tokens per prompt, temperature 0.1.
    learner = HybridAISquaredPerRelationLearner(model_id=learner_model_id, categories=3, device=learner_device)
print("Learner model:", learner.model_id, "on", learner_device)

# llm_id must be the learner's Hugging Face model: the pipeline loads it with learner.load(model_id=llm_id).
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