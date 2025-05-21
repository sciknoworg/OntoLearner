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
RESULTS_DIR = Path("../../data/results")

ontology = Wine()
ontology.load()
train_data, test_data = train_test_split(ontology.extract(), test_size=0.2)

# # Retriever-only learner
# pipeline = LearnerPipeline(
#     task="term-typing",
#     retriever=BERTRetrieverLearner(),
#     retriever_id="sentence-transformers/all-MiniLM-L6-v2"
# )

# # LLM-only learner
# pipeline = LearnerPipeline(
#     task="taxonomy-discovery",
#     llm=AutoLearnerLLM(token=hf_token),
#     llm_id="mistralai/Mistral-7B-Instruct-v0.1"
# )

# Combined RAG learner (the most common case)
pipeline = LearnerPipeline(
    task="term-typing",
    retriever_id="sentence-transformers/all-MiniLM-L6-v2",
    llm_id="mistralai/Mistral-7B-Instruct-v0.1",
    hf_token=huggingface_token
)

results, metrics = pipeline.fit_predict_evaluate(
    train_data=train_data,
    test_data=test_data,
    output_dir=RESULTS_DIR
)
