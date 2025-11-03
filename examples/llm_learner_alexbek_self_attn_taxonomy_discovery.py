from ontolearner import GeoNames, train_test_split, LearnerPipeline
from ontolearner import AlexbekCrossAttnLearner
# 1) Load & split
ontology = GeoNames()
ontology.load()
data = ontology.extract()
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# 2) Configure the cross-attention learner
cross_learner = AlexbekCrossAttnLearner(
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",  # or "Qwen/Qwen2.5-1.5B-... (if wrapped as ST)"
    device="cpu",
    num_heads=8,
    lr=5e-5,
    weight_decay=0.01,
    num_epochs=1,
    batch_size=256,
    neg_ratio=1.0,
    output_dir="./results/crossattn/",
    seed=42,
)

# 3) Build pipeline
pipeline = LearnerPipeline(
    llm=cross_learner,     # <- our learner
    llm_id="cross-attn",   # label for bookkeeping
    ontologizer_data=False # pass raw ontology objects as in your example
)

# 4) Train + predict + evaluate
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    task="taxonomy-discovery",
    evaluate=True,
    ontologizer_data=False,
)

print("Metrics:", outputs.get("metrics"))
print("Elapsed time:", outputs["elapsed_time"])
print(outputs)
