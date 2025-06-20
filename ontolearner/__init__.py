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

__version__ = "1.1.2"

import logging
from ontolearner import base, data_structure, ontology, text2onto, utils, tools, learner
from .learner import AutoLearnerLLM, BERTRetrieverLearner
from .learner_pipeline import LearnerPipeline
from .processor import Processor
from .utils.train_test_split import train_test_split
from .ontology import * # noqa

__all__ = [
    "AutoLearnerLLM",
    "BERTRetrieverLearner",
    "LearnerPipeline",
    "Processor",
    "data_structure",
    "text2onto",
    "ontology",
    "utils",
    "tools",
    "learner",
    "base",
    "train_test_split"
]

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger("ontolearner")
