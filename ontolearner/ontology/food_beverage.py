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

from ..base import BaseOntology


class Wine(BaseOntology):
    """
    A project to define an RDF style ontology for wines and the wine-industry
    """
    ontology_id = "Wine"
    ontology_full_name = "Wine Ontology (Wine)"
    domain = "Food and Beverage"
    category = "Wine"
    version = None
    last_updated = None
    creator = None
    license = None
    format = "RDF"
    download_url = "https://github.com/UCDavisLibrary/wine-ontology"
