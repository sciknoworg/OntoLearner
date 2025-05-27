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

from ..base.ontology import BaseOntology


class Hydra(BaseOntology):
    """
    Hydra is a lightweight vocabulary to create hypermedia-driven Web APIs. By specifying a number of concepts
    commonly used in Web APIs it enables the creation of generic API clients.
    """
    ontology_id = "Hydra"
    ontology_full_name = "Hydra Ontology (Hydra)"
    domain = "Web and Internet"
    category = "Web Development"
    version = None
    last_updated = "13 July 2021"
    creator = "Hydra W3C Community Group"
    license = "Creative Commons 4.0"
    format = "JSONLD"
    download_url = "https://www.hydra-cg.com/spec/latest/core/#references"


class SAREF(BaseOntology):
    """
    The Smart Applications REFerence (SAREF) suite of ontologies forms a shared model of consensus
    intended to enable semantic interoperability between solutions from different providers
    and among various activity sectors in the Internet of Things (IoT),
    thus contributing to the development of data spaces. SAREF is published as a set of open standards
    produced by ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M).
    """
    ontology_id = "SAREF"
    ontology_full_name = "Smart Applications REFerence ontology (SAREF)"
    domain = "Web and Internet"
    category = "interoperability"
    version = "3.2.1"
    last_updated = "2020-12-31"
    creator = "ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M)"
    license = None
    format = "RDF"
    download_url = "https://saref.etsi.org/core/v3.2.1/"
