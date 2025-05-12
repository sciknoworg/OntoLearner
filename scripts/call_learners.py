import logging
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from huggingface_hub import login

from ontolearner import Learner
from ontolearner.data_structure import OntologyData
from ontolearner.learner import BERTRetrieverLearner, AutoLearnerLLM, AutoRAGLearner
from ontolearner.learner.prompt import StandardizedPrompting
from ontolearner.ontology import Wine


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

_ = load_dotenv(find_dotenv())
huggingface_key = os.environ.get('HUGGINGFACE_ACCESS_TOKEN')
login(token=huggingface_key)

DATA_DIR = Path("../data")
ONTOLOGIES_DIR = DATA_DIR / "ontologies"

wine = Wine()
ontology_domain = wine.domain.lower().replace(' ', '_')
ontology_path = ONTOLOGIES_DIR / ontology_domain / f"{wine.ontology_id.lower()}.{wine.format.lower()}"


def use_rag_learner():
    wine.load(str(ontology_path))
    data: OntologyData = wine.extract()

    if not data.term_typings:
        logger.warning(f"No term typings found in the {wine.ontology_id} ontology data!")
        return

    retriever = BERTRetrieverLearner()
    llm = AutoLearnerLLM()
    prompting = StandardizedPrompting(task="term-typing")
    rag_learner = AutoRAGLearner(retriever, llm, prompting)
    learner = Learner(learner=rag_learner, prompting=prompting)

    learner.learn(
        data,
        task="term-typing",
        retriever_id="sentence-transformers/all-MiniLM-L6-v2",
        llm_id="meta-llama/Llama-3.1-8B-Instruct",
        top_k=1
    )

    logger.info("Testing term typing predictions:")

    for typing in data.term_typings[:5]:
        raw_term = typing.term
        predicted = rag_learner.predict(raw_term, task="term-typing")[0]
        logger.info(f"Term: {raw_term}\n"
                    f"Predicted: {predicted}")

if __name__ == "__main__":
    use_rag_learner()
