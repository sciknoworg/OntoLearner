__version__ = "1.1.0"

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("ontolearner")

from ontolearner import base, data_structure, ontology, text2onto, utils, tools, learner
from .processor import Processor
from .learner_pipeline import LearnerPipeline

__all__ = [
    "base",
    "ontology",
    "text2onto",
    "learner",
    "LearnerPipeline",
    "Processor",
    "tools",
    "data_structure",
    "utils",
]
