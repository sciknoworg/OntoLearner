"""Term-typing workflow example with OntoLearner."""
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from huggingface_hub import login

from ontolearner.learner_pipeline import LearnerPipeline
from ontolearner.ontology import Wine
from ontolearner.utils.train_test_split import train_test_split


_ = load_dotenv(find_dotenv())
huggingface_token = os.environ.get('HUGGINGFACE_ACCESS_TOKEN')
if huggingface_token:
    login(token=huggingface_token)
RESULTS_DIR = Path("../data/results")


def main():
    ontology = Wine()
    ontology.load()
    train_data, test_data = train_test_split(ontology.extract(), test_size=0.2)

    pipeline = LearnerPipeline(
        task="term-typing",
        llm_id="mistralai/Mistral-7B-Instruct-v0.1",
        retriever_id="sentence-transformers/all-MiniLM-L6-v2",
        hf_token=huggingface_token
    )

    results, metrics = pipeline.run_full_pipeline(
        train_data=train_data,
        test_data=test_data,
        task="term-typing",
        top_k=3,
        output_dir=RESULTS_DIR
    )

    print(f"\nTerm-typing metrics: {metrics}")

if __name__ == "__main__":
    main()
