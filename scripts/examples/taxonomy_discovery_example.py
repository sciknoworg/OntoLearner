"""
Example script demonstrating the taxonomy discovery workflow with OntoLearner.

This script shows how to:
1. Import an ontology
2. Perform train-test split
3. Run taxonomy discovery task with selected LLM and retriever
4. Evaluate and visualize results
"""

import logging
import os
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from huggingface_hub import login

from ontolearner import Learner
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
    """Run the taxonomy discovery example workflow"""

    # Step 1: Import an ontology
    logger.info("Step 1: Importing ontology")
    ontology = Wine()  # Choose your ontology
    ontology_domain = ontology.domain.lower().replace(' ', '_')
    ontology_path = ONTOLOGIES_DIR / ontology_domain / f"{ontology.ontology_id.lower()}.{ontology.format.lower()}"

    logger.info(f"Loading ontology from {ontology_path}")
    ontology.load(str(ontology_path))
    data = ontology.extract()

    logger.info(f"Extracted {len(data.type_taxonomies.taxonomies)} taxonomic relations")

    # Step 2: Perform train-test split
    logger.info("Step 2: Performing train-test split")
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
    logger.info(f"Split data into {len(train_data.type_taxonomies.taxonomies)} train and {len(test_data.type_taxonomies.taxonomies)} test taxonomic relations")

    # Step 3: Set up the learner with chosen models
    logger.info("Step 3: Setting up learner with chosen models")

    # Choose your models
    llm_id = "mistralai/Mistral-7B-Instruct-v0.1"  # You can change this to any supported model
    retriever_id = "sentence-transformers/all-MiniLM-L6-v2"  # You can change this to any supported model

    # Initialize components
    retriever = BERTRetrieverLearner()
    llm = AutoLearnerLLM(token=huggingface_token)
    prompting = StandardizedPrompting(task="taxonomy-discovery")
    rag_learner = AutoRAGLearner(retriever, llm, prompting)
    learner = Learner(learner=rag_learner, prompting=prompting)

    # Step 4: Train the learner
    logger.info(f"Step 4: Training learner with LLM={llm_id}, Retriever={retriever_id}")
    learner.learn(
        train_data,
        task="taxonomy-discovery",
        retriever_id=retriever_id,
        llm_id=llm_id,
        top_k=3  # Number of examples to retrieve
    )

    # Step 5: Make predictions and evaluate
    logger.info("Step 5: Making predictions and evaluating results")
    results = []

    # Test on a subset for demonstration (use all test data in production)
    test_subset = test_data.type_taxonomies.taxonomies[:10]

    for tax_rel in test_subset:
        parent = tax_rel.parent
        child = tax_rel.child
        ground_truth = True  # In taxonomy discovery, the ground truth is the existence of the relation

        # Make prediction
        raw_input = (parent, child)
        predicted = rag_learner.predict(raw_input, task="taxonomy-discovery")

        # Calculate metrics (simplified for this example)
        # You would need to implement a proper calculate_taxonomy_metrics function
        is_correct = predicted.lower() == "yes" or "true" in predicted.lower()

        results.append({
            'parent': parent,
            'child': child,
            'ground_truth': ground_truth,
            'predicted': predicted,
            'is_correct': is_correct
        })

        # Log results
        logger.info("-" * 50)
        logger.info(f"Parent: {parent}")
        logger.info(f"Child: {child}")
        logger.info("Ground Truth: Taxonomic relation exists")
        logger.info(f"Predicted: {predicted}")
        logger.info(f"Correct: {is_correct}")

    # Step 6: Aggregate and analyze results
    logger.info("Step 6: Aggregating and analyzing results")

    # Calculate simple accuracy
    correct_count = sum(1 for r in results if r['is_correct'])
    accuracy = correct_count / len(results) if results else 0

    logger.info("Aggregated Metrics:")
    logger.info(f"Accuracy: {accuracy:.4f}")

    # Optional: You could implement more sophisticated metrics and visualizations

if __name__ == "__main__":
    main()
