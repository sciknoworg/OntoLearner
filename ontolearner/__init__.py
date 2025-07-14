# Copyright (c) 2025 SciKnowOrg
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__version__ = "1.3.0"

import logging
from ontolearner import (ontology,
                         text2onto,
                         learner,
                         utils,
                         tools,
                         data_structure)
from .ontology import * # noqa
from ._ontology import AutoOntology
from .learner import (AutoLLMLearner,
                      AutoRetrieverLearner,
                      AutoRAGLearner,
                      StandardizedPrompting,
                      LabelMapper)
from ._learner import LearnerPipeline

# from .processor import Processor
from .utils import train_test_split
from .evaluation import evaluation_report


__all__ = [
    "AutoLLMLearner",
    "AutoOntology",
    "AutoRetrieverLearner",
    "AutoRAGLearner",
    "StandardizedPrompting",
    "LabelMapper",
    "LearnerPipeline",
    # "Processor",
    "data_structure",
    "text2onto",
    "ontology",
    "utils",
    "tools",
    "learner",
    "train_test_split",
    "evaluation_report"
]

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("ontolearner")
