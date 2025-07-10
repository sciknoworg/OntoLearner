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

import inspect
import ontolearner.ontology as ontology_module
from .base import BaseOntology

class AutoOntology:
    def __new__(self, ontology_id) -> BaseOntology:
        for name, obj in inspect.getmembers(ontology_module):
            if inspect.isclass(obj):
                if hasattr(obj, 'load') and callable(getattr(obj, 'load')) and hasattr(obj, 'ontology_id'):
                    instance = obj()
                    if str(obj).split("'")[-2].split(".")[-1].lower() == ontology_id.lower():
                        return instance
        return BaseOntology()
