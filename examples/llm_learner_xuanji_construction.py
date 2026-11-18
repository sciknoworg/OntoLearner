
import os
import json

from openai import OpenAI
from ontolearner import LearnerPipeline, train_test_split
from ontolearner.ontology import FOAF
from ontolearner.text2onto import (
    SyntheticGenerator,
    SyntheticDataPreprocessor,
)
from ontolearner.learner.primitive import XuanJiFSLearner


# Configuration
model_id = os.getenv("TEXT2ONTO_MODEL_ID", "Qwen/Qwen2.5-0.5B-Instruct")
learner_model_id = os.getenv("XUANJI_MODEL_ID", "gpt-5.4")
learner_base_url = os.getenv("XUANJI_BASE_URL")
api_key = os.getenv("OPENAI_API_KEY")
hf_token = os.getenv("HF_TOKEN", "")

if not api_key:
    raise EnvironmentError("Set OPENAI_API_KEY before running.")


# STEP 1: Load FOAF ontology
print("\nSTEP 1: Loading FOAF ontology")

ontology = FOAF()
ontology.load()
data = ontology.extract()

# Use taxonomy relations only for this small example.
data.term_typings = []
data.type_non_taxonomic_relations.non_taxonomies = []

print("Taxonomic relations:", len(data.type_taxonomies.taxonomies))


# STEP 2: Split ontology into train/test
print("\nSTEP 2: Splitting ontology")

train_ontology, test_ontology = train_test_split(
    data,
    test_size=0.5,
    random_state=42,
)

print("Train taxonomies:", len(train_ontology.type_taxonomies.taxonomies))
print("Test taxonomies:", len(test_ontology.type_taxonomies.taxonomies))


# STEP 3: Initialize synthetic generator
print("\nSTEP 3: Initializing generator")

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


# STEP 4: Generate training documents
print("\nSTEP 4: Generating TRAIN documents")

train_synthetic = generator.generate(
    ontological_data=train_ontology,
    topic=ontology.domain,
)

print("Generated train documents:", len(train_synthetic.generated_docs))


# STEP 5: Generate test documents
print("\nSTEP 5: Generating TEST documents")

test_synthetic = generator.generate(
    ontological_data=test_ontology,
    topic=ontology.domain,
)

print("Generated test documents:", len(test_synthetic.generated_docs))


# STEP 6: Initialize construction preprocessor
print("\nSTEP 6: Initializing preprocessor")

preprocessor = SyntheticDataPreprocessor(
    client=OpenAI(api_key=api_key),
    task="ontology_construction",
    random_state=42,
)


# STEP 7: Preprocess training data
print("\nSTEP 7: Preprocessing TRAIN documents")

train_data = preprocessor.preprocess(
    train_synthetic,
    train_ontology,
)

print("Train samples:", len(train_data))

if train_data:
    print("Example TRAIN sample:")
    print(json.dumps(train_data[0], indent=2, ensure_ascii=False)[:1500])


# STEP 8: Preprocess test data
print("\nSTEP 8: Preprocessing TEST documents")

test_data = preprocessor.preprocess(
    test_synthetic,
    test_ontology,
)

print("Test samples:", len(test_data))

if test_data:
    print("Example TEST sample:")
    print(json.dumps(test_data[0], indent=2, ensure_ascii=False)[:1500])

if not train_data or not test_data:
    raise ValueError("No usable train or test samples were generated.")


# STEP 9: Initialize XuanJi learner
print("\nSTEP 9: Initializing XuanJi learner")

learner = XuanJiFSLearner(
    model_id=learner_model_id,
    api_key=api_key,
    base_url=learner_base_url,
    adaptive_few_shot=True,
)

print("Learner:", type(learner).__name__)
print("Adaptive few-shot:", learner.adaptive_few_shot)


# STEP 10: Initialize LearnerPipeline
print("\nSTEP 10: Initializing LearnerPipeline")

pipe = LearnerPipeline(
    llm=learner,
    llm_id=learner_model_id,
    ontologizer_data=False,
)


# STEP 11: Train, predict, and evaluate
print("\nSTEP 11: Running construction pipeline", flush=True)

outputs = pipe(
    train_data=train_data,
    test_data=test_data,
    task="ontology_construction",
    evaluate=True,
    ontologizer_data=False,
)


# STEP 12: Display results
print("\nSTEP 12: Results")

print("Metrics:", outputs.get("metrics"))
print("Elapsed time:", outputs.get("elapsed_time"))

print(
    "Predictions:",
    json.dumps(
        outputs.get("predictions"),
        indent=2,
        ensure_ascii=False,
        default=str,
    ),
)
