from ontolearner import Wine, train_test_split, LearnerPipeline
from ontolearner.learner.taxonomy_discovery import SemanticSwingersTaxonomyLearner

# 1) Load & split
ontology = Wine()
ontology.load()
data = ontology.extract()
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# 2) Configure the semantic-swingers taxonomy learner.
#    Offline default (no API key): the "embedding" selector.
#    Champion: selector="openai" + api_key=... for gpt-4.1-mini parent selection.
learner = SemanticSwingersTaxonomyLearner(
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",  # champion: mxbai-embed-large-v1
    top_k=10,
    selector="embedding",
    device="cpu",
)

# 3) Build pipeline (pass our learner as `llm`, raw ontology objects)
pipeline = LearnerPipeline(
    llm=learner,
    llm_id="semanticswingers-taxonomy",
    ontologizer_data=False,
)

# 4) Train (no-op) + predict + evaluate
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    task="taxonomy-discovery",
    evaluate=True,
    ontologizer_data=False,
)

print("Metrics:", outputs.get("metrics"))
print("Elapsed time:", outputs["elapsed_time"])
