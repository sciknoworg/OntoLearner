from openai import OpenAI
from ontolearner import LearnerPipeline, train_test_split
from ontolearner.ontology import FOAF
from ontolearner.text2onto import SyntheticGenerator, SyntheticDataPreprocessor
from ontolearner.learner.primitive import LaboroAIPrimitiveLearner

# Your keys (do not commit them)
api_key = ""   # OpenAI API key
hf_token = ""  # Hugging Face token, if the model needs one
if not api_key:
    raise ValueError("Set api_key at the top of this script.")

# 1) Load & split (FOAF taxonomy only, to keep it quick)
ontology = FOAF()
ontology.load()
data = ontology.extract()
data.term_typings = []
data.type_non_taxonomic_relations.non_taxonomies = []
train_ontology, test_ontology = train_test_split(data, test_size=0.5, random_state=42)

# 2) Generate synthetic documents from each part
generator = SyntheticGenerator(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",  # writes the documents
    token=hf_token,
    extraction_method="openai",  # OpenAI parses the model's output
    openai_api_key=api_key,
    openai_model="gpt-4o-mini",
    batch_size=5,  # relations per document
    min_pseudo_sentences=1,
    generation_batch_size=2,
    max_input_length=2000,
    max_new_tokens=2000,
)
train_synthetic = generator.generate(ontological_data=train_ontology, topic=ontology.domain)
test_synthetic = generator.generate(ontological_data=test_ontology, topic=ontology.domain)

# 3) Turn the documents into expansion records
preprocessor = SyntheticDataPreprocessor(client=OpenAI(api_key=api_key), task="ontology_expansion", random_state=42)
train_data = preprocessor.preprocess(train_synthetic, train_ontology)
test_data = preprocessor.preprocess(test_synthetic, test_ontology)

# 4) Configure the LaboroAI learner (help(LaboroAIPrimitiveLearner) lists all settings)
learner = LaboroAIPrimitiveLearner(
    model_id="gpt-5.4",
    api_key=api_key,
    k=6,  # retrieved examples per document
    use_dense=True,  # retrieve with BM25 + embeddings
)

# 5) Build pipeline
pipeline = LearnerPipeline(
    llm=learner,
    llm_id="gpt-5.4",  # label for bookkeeping
    ontologizer_data=False,  # records go to the learner as they are
)

# 6) Train + predict + evaluate
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    task="ontology_expansion",
    evaluate=True,
    ontologizer_data=False,
)

print("Metrics:", outputs.get("metrics"))
print("Elapsed time:", outputs["elapsed_time"])