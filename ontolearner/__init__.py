__version__ = "0.3.0"

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("ontolearner")

from .pipeline import ProcessorPipeline
from ontolearner import base, data_structure, ontology, text2onto, utils, tools

__all__ = [
    "base",
    "data_structure",
    "ontology",
    "text2onto",
    "tools",
    "utils",
    "ProcessorPipeline"
]
