import json

from openai import OpenAI
from ontolearner import LearnerPipeline, train_test_split
from ontolearner.ontology import FOAF
from ontolearner.text2onto import (
    SyntheticGenerator,
    SyntheticDataPreprocessor,
)
from ontolearner.learner.primitive import BigDipperAIPrimitiveLearner


# Configuration
model_id = "Qwen/Qwen2.5-0.5B-Instruct"
api_key = "OPENAI_API_KEY"
hf_token = ""

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
# alignment filter, and are then turned into construction samples containing text context and reference triples.
preprocessor = SyntheticDataPreprocessor(
    client=OpenAI(api_key=api_key),
    task="ontology_construction",
    random_state=42,
)


print("\nSTEP 7: Preprocessing TRAIN documents")
train_data = preprocessor.preprocess(train_synthetic, train_ontology)
print("Train samples:", len(train_data))

if train_data:
    print("\nExample train sample:")
    print(json.dumps(train_data[0], indent=2, ensure_ascii=False)[:1500])


print("\nSTEP 8: Preprocessing TEST documents")
test_data = preprocessor.preprocess(test_synthetic, test_ontology)
print("Test samples:", len(test_data))

if test_data:
    print("\nExample test sample:")
    print(json.dumps(test_data[0], indent=2, ensure_ascii=False)[:1500])


print("\nSTEP 9: Running the BigDipperAI learner through LearnerPipeline")

if not train_data or not test_data:
    raise ValueError(
        "Preprocessing produced no training or test construction samples."
    )


# Optional: Use ontology expansion samples as auxiliary training data.
# Keep text2onto_expansion.py in the same directory.
# Consider using a different ontology to diversify training examples.

auxiliary_data = None

# import runpy
# from pathlib import Path
#
# expansion_path = Path(__file__).with_name("text2onto_expansion.py")
# expansion_outputs = runpy.run_path(str(expansion_path))
# auxiliary_data = expansion_outputs["train_data"]
#
# print("Auxiliary expansion samples:", len(auxiliary_data))


# Configure a smaller pretrained language model for CPU testing.
learner_model_id = "Qwen/Qwen3-0.6B"

learner = BigDipperAIPrimitiveLearner(
    model_id=learner_model_id,
    auxiliary_data=auxiliary_data,
    device="cpu",
    train_adapter=False,
    max_input_tokens=1024,
    max_output_tokens=384,
    retry_output_tokens=512,
)

# The pipeline loads the pretrained language model.
# BigDipperAI prepares construction supervision, optional auxiliary expansion supervision, and the graph index used during inference.
# No QLoRA adapter is trained in this CPU example.
pipeline = LearnerPipeline(
    llm=learner,
    llm_id=learner_model_id,
    ontologizer_data=True,
)

# Prepare training data, predict ontology triples for all test documents,
# and evaluate predictions against the reference triples.
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    task="ontology_construction",
    evaluate=True,
    ontologizer_data=True,
)

print("\nMetrics:", outputs.get("metrics"))
print("\nElapsed time:", outputs["elapsed_time"])
