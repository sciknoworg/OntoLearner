
from pathlib import Path
import json
import logging
from typing import Any, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a logger
logger = logging.getLogger(__name__)


def save_dataset(data: Dict[str, Any], output_path: str) -> None:
    """
    Save dataset to JSON file.

    Args:
        data: Dictionary containing dataset
        output_path: Path to save the JSON file
    """
    try:
        output_path = Path(output_path)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logger.info(f"Successfully saved dataset to {output_path}")
    except Exception as e:
        logger.error(f"Error saving dataset to {output_path}: {e}")
        raise


# def save_dataset(dataset: Dict, filename: str):
#     """
#     Save a dataset to a JSON file.
#
#     Args:
#         dataset (Dict): The dataset to save
#         filename (str): Path where to save the JSON file
#     """
#     logger.info(f"Saving dataset to {filename}")
#
#     with open(filename, 'w') as f:
#         json.dump(dataset, f, indent=2)
#
#     logger.info(f"Successfully saved dataset to {filename}")


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
