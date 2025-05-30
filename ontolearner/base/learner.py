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

from abc import ABC
from typing import Any, List


class AutoLearner(ABC):

    def __init__(self, **kwargs):
        pass

    def load(self, **kwargs):
        pass

    def fit(self, train_data: Any, task: str):
        pass

    def predict(self, eval_data: Any, task: str) -> Any:
        pass

    def fit_predict(self, train_data: Any, eval_data: Any, task: str) -> Any:
        self.fit(train_data, task)
        predicts = self.predict(eval_data, task)
        return predicts


class AutoLLM(ABC):
    def __init__(self):
        self.model = None
        self.tokenizer = None

    def load(self, model_id: str):
        pass

    def generate(self, inputs: List[Any]) -> List[Any]:
        pass


class AutoRetriever(ABC):
    def __init__(self):
        self.model = None

    def load(self, model_id: str):
        pass

    def index(self, inputs: List[Any]):
        pass

    def retrieve(self, inputs: List[Any], top_k: int) -> List[Any]:
        pass


class AutoPrompt(ABC):
    def __init__(self, prompt_template: str):
        self.prompt_template = prompt_template

    def format(self, **kwargs):
        pass
