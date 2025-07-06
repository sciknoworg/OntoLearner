from pathlib import Path
from ontolearner import LearnerPipeline, Wine, train_test_split

token = ""

ontology = Wine()
ontology.load()
data = ontology.extract()
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

pipeline = LearnerPipeline(
    task="term-typing",
    retriever_id="sentence-transformers/all-MiniLM-L6-v2",
    # llm_id="mistralai/Mistral-7B-Instruct-v0.1",
    llm_id = "Qwen/Qwen2.5-0.5B",
    hf_token=token
)

results, metrics = pipeline.fit_predict_evaluate(
    train_data=train_data,
    test_data=test_data,
    top_k=3,
    test_limit=10,
    output_dir=Path("../../data/results/rag")
)

print(metrics)
