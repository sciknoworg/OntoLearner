
from pathlib import Path
import json
from typing import Any, Dict, Union

from .. import logger

def save_json(data: Dict[str, Any], output_path: Union[str, Path],) -> None:
    """
    Save dataset to JSON file.

    :arg:
        data: Dictionary containing dataset
        output_path: Path to save the JSON file
    """
    try:
        output_path = Path(output_path)

        if output_path.suffix.lower() != '.json':
            raise ValueError(f"Invalid file extension: {output_path.suffix}")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        logger.info(f"Successfully saved dataset to {output_path}")

    except Exception as e:
        logger.error(f"Error saving dataset to {output_path}: {e}")
        raise


def load_json(path: Union[str, Path]) -> Dict[str, Any]:
    """
    Load a dataset from a JSON file.

    :arg: filename (str): Path to the JSON file to load
    :return: Dict: The loaded dataset
    """
    logger.info(f"Loading dataset from {path}")

    file_path = Path(path)

    if not file_path.exists():
        raise ValueError(f"File not found: {file_path}")

    if file_path.suffix.lower() != '.json':
        raise ValueError(f"Invalid file extension: {file_path.suffix}")

    with file_path.open('r', encoding='utf-8') as f:
        dataset = json.load(f)

    logger.info(f"Successfully loaded dataset from {path}")

    return dataset
