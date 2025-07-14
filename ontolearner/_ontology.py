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
    """
       Factory class to automatically instantiate an ontology class from the `ontolearner.ontology` module
       based on a given ontology ID.

       This class scans all classes defined in the `ontolearner.ontology` module and returns an instance
       of the first class that:
         - has a callable `load` method,
         - has an `ontology_id` attribute,
         - and whose class name matches the given `ontology_id` (case-insensitive).

       If no matching class is found, an instance of `BaseOntology` is returned by default.

       Args:
           ontology_id (str): The identifier (name) of the ontology class to instantiate.

       Returns:
           BaseOntology: An instance of the matching ontology class or a `BaseOntology` fallback.

       Example:
           >>> auto_onto = AutoOntology("AgrO")
           >>> print(type(auto_onto))
           <class 'ontolearner.ontology.AgrO'>

           If no class matches "unknownontology":
           >>> auto_onto = AutoOntology("unknownontology")
           >>> print(type(auto_onto))
           <class 'ontolearner.base.BaseOntology'>
       """
    def __new__(self, ontology_id) -> BaseOntology:
        for name, obj in inspect.getmembers(ontology_module):
            if inspect.isclass(obj):
                if hasattr(obj, 'load') and callable(getattr(obj, 'load')) and hasattr(obj, 'ontology_id'):
                    instance = obj()
                    if str(obj).split("'")[-2].split(".")[-1].lower() == ontology_id.lower():
                        return instance
        return BaseOntology()
