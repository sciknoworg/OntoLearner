from pathlib import Path


from ontolearner import LearnerPipeline, BERTRetrieverLearner, Wine, train_test_split

token = ""

ontology = Wine()
ontology.load()
train_data, test_data = train_test_split(ontology.extract(), test_size=0.2, random_state=42)

pipeline = LearnerPipeline(
    task="non-taxonomy-discovery",
    retriever=BERTRetrieverLearner(),
    retriever_id="sentence-transformers/all-MiniLM-L6-v2"
)

results, metrics = pipeline.fit_predict_evaluate(
    train_data=train_data,
    test_data=test_data,
    top_k=5,
    test_limit=10,
    output_dir=Path("../../data/results/retriever")
)

print(metrics)
