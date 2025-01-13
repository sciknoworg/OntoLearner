
import json
import logging
from typing import Dict


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a logger
logger = logging.getLogger(__name__)


def save_dataset(dataset: Dict, filename: str):
    """
    Save a dataset to a JSON file.

    Args:
        dataset (Dict): The dataset to save
        filename (str): Path where to save the JSON file
    """
    logger.info(f"Saving dataset to {filename}")

    with open(filename, 'w') as f:
        json.dump(dataset, f, indent=2)

    logger.info(f"Successfully saved dataset to {filename}")


def load_dataset(filename: str) -> Dict:
    """
    Load a dataset from a JSON file.

    Args:
        filename (str): Path to the JSON file to load
    Returns:
        Dict: The loaded dataset
    """
    logger.info(f"Loading dataset from {filename}")

    with open(filename, 'r') as f:
        dataset = json.load(f)

    logger.info(f"Successfully loaded dataset from {filename}")

    return dataset
