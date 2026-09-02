from ontolearner import Wine, train_test_split, LearnerPipeline
from ontolearner.learner.term_typing import SemanticSwingersTermTypingLearner

# 1) Load & split
ontology = Wine()
ontology.load()
data = ontology.extract()
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# 2) Configure the semantic-swingers term-typing learner.
#    Offline default (no API key): the "embedding" selector (nearest type label).
#    Champion: selector="openai" + api_key=... for gpt-4.1-mini classification.
#    Local champion-reproduction (no API key): selector="ollama" (local Ollama server).
learner = SemanticSwingersTermTypingLearner(
    embedding_model="mixedbread-ai/mxbai-embed-large-v1",
    selector="embedding",
    device="cpu",
)

# 3) Build pipeline (pass our learner as `llm`)
pipeline = LearnerPipeline(
    llm=learner,
    llm_id="semanticswingers-term-typing",
)

# 4) Train (learn the type inventory) + predict + evaluate
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    task="term-typing",
    evaluate=True,
)

print("Metrics:", outputs.get("metrics"))
print("Elapsed time:", outputs["elapsed_time"])
