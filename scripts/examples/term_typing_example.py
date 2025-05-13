"""
Example script demonstrating the term-typing workflow with OntoLearner.

This script shows how to:
1. Import an ontology
2. Perform train-test split
3. Run term-typing task with selected LLM and retriever
4. Evaluate and visualize results
"""

import logging
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from huggingface_hub import login

from ontolearner import Learner
from ontolearner.evaluation.metrics import calculate_term_typing_metrics
from ontolearner.evaluation.evaluate import aggregate_metrics
from ontolearner.evaluation.visualisations import plot_precision_recall_distribution
from ontolearner.learner import BERTRetrieverLearner, AutoLearnerLLM, AutoRAGLearner
from ontolearner.learner.prompt import StandardizedPrompting
from ontolearner.ontology import Wine
from ontolearner.utils.train_test_split import train_test_split

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables and authenticate with Hugging Face
_ = load_dotenv(find_dotenv())
huggingface_token = os.environ.get('HUGGINGFACE_ACCESS_TOKEN')
if huggingface_token:
    login(token=huggingface_token)
    logger.info("Authenticated with Hugging Face")
else:
    logger.warning("No Hugging Face token found. Some models may not be accessible.")

# Define paths
DATA_DIR = Path("../data")
ONTOLOGIES_DIR = DATA_DIR / "ontologies"
RESULTS_DIR = DATA_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True, parents=True)


def main():
    """Run the term-typing example workflow"""

    # Step 1: Import an ontology
    logger.info("Step 1: Importing ontology")
    ontology = Wine()  # Choose your ontology
    ontology_domain = ontology.domain.lower().replace(' ', '_')
    ontology_path = ONTOLOGIES_DIR / ontology_domain / f"{ontology.ontology_id.lower()}.{ontology.format.lower()}"

    logger.info(f"Loading ontology from {ontology_path}")
    ontology.load(str(ontology_path))
    data = ontology.extract()

    logger.info(f"Extracted {len(data.term_typings)} term typings")

    # Step 2: Perform train-test split
    logger.info("Step 2: Performing train-test split")
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    logger.info(f"Split data into {len(train_data.term_typings)} train and {len(test_data.term_typings)} test samples")

    # Step 3: Set up the learner with chosen models
    logger.info("Step 3: Setting up learner with chosen models")

    # Choose your models
    llm_id = "mistralai/Mistral-7B-Instruct-v0.1"  # You can change this to any supported model
    retriever_id = "sentence-transformers/all-MiniLM-L6-v2"  # You can change this to any supported model

    # Initialize components
    retriever = BERTRetrieverLearner()
    llm = AutoLearnerLLM(token=huggingface_token)
    prompting = StandardizedPrompting(task="term-typing")
    rag_learner = AutoRAGLearner(retriever, llm, prompting)
    learner = Learner(learner=rag_learner, prompting=prompting)

    # Step 4: Train the learner
    logger.info(f"Step 4: Training learner with LLM={llm_id}, Retriever={retriever_id}")
    learner.learn(
        train_data,
        task="term-typing",
        retriever_id=retriever_id,
        llm_id=llm_id,
        top_k=3  # Number of examples to retrieve
    )

    # Step 5: Make predictions and evaluate
    logger.info("Step 5: Making predictions and evaluating results")
    results = []

    # Test on a subset for demonstration (use all test data in production)
    test_subset = test_data.term_typings[:10]

    for typing in test_subset:
        term = typing.term
        ground_truth = typing.types

        # Make prediction
        predicted = rag_learner.predict(term, task="term-typing")

        # Calculate metrics
        metrics = calculate_term_typing_metrics(predicted, ground_truth)

        results.append({
            'term': term,
            'ground_truth': ground_truth,
            'predicted': predicted,
            **metrics
        })

        # Log results
        logger.info("-" * 50)
        logger.info(f"Term: {term}")
        logger.info(f"Ground Truth: {ground_truth}")
        logger.info(f"Predicted: {predicted}")
        logger.info(f"F1 Score: {metrics['f1_score']:.4f}")

    # Step 6: Aggregate and analyze results
    logger.info("Step 6: Aggregating and analyzing results")
    agg_metrics = aggregate_metrics(results, "term-typing")

    logger.info("Aggregated Metrics:")
    logger.info(f"Average Precision: {agg_metrics['avg_precision_score']:.4f}")
    logger.info(f"Average Recall: {agg_metrics['avg_recall_score']:.4f}")
    logger.info(f"Average F1 Score: {agg_metrics['avg_f1_score']:.4f}")
    logger.info(f"Average Exact Match: {agg_metrics['avg_exact_match']:.4f}")

    # Optional: Visualize results
    all_results = [{
        'llm': llm_id,
        'retriever': retriever_id,
        'metrics': agg_metrics,
        'detailed_results': results
    }]

    plot_precision_recall_distribution(all_results, RESULTS_DIR)
    logger.info(f"Results visualization saved to {RESULTS_DIR}")

if __name__ == "__main__":
    main()
