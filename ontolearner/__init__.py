__version__ = "1.2.2"

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("ontolearner")

from .pipeline import ProcessorPipeline
from ontolearner import base, data_structure, ontology, utils, tools

__all__ = [
    "base",
    "data_structure",
    "ontology",
    "tools",
    "utils",
    "ProcessorPipeline"
]
