from pathlib import Path
from ontolearner.learner_pipeline import LearnerPipeline
from ontolearner.learner import AutoLearnerLLM
from ontolearner.ontology import Wine
from ontolearner.utils.train_test_split import train_test_split

token = ""

ontology = Wine()
ontology.load()
data = ontology.extract()
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

pipeline = LearnerPipeline(
    task="taxonomy-discovery",
    llm=AutoLearnerLLM(token=token),
    llm_id="mistralai/Mistral-7B-Instruct-v0.1"
)

results, metrics = pipeline.fit_predict_evaluate(
    train_data=train_data,
    test_data=test_data,
    test_limit=10,
    output_dir=Path("../../data/results/llm")
)

print(metrics)
