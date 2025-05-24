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


class BFO(BaseOntology):
    """
    The Basic Formal Ontology (BFO) is a small, upper-level ontology that describes
    the basic types of entities in the world and how they relate to each other.
    """
    ontology_id = "BFO"
    ontology_full_name = "Basic Formal Ontology (BFO)"
    domain = "Upper Ontology"
    category = "Basic"
    version = "2.0"
    last_updated = "2020"
    creator = "University at Buffalo"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://github.com/BFO-ontology/BFO-2020/"


class DOLCE(BaseOntology):
    """
    The Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE) is a foundational ontology
    that provides a conceptual framework for the formalization of domain ontologies.
    """
    ontology_id = "DOLCE"
    ontology_full_name = "Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE)"
    domain = "Upper Ontology"
    category = "Linguistics, Cognitive Science"
    version = None
    last_updated = None
    creator = "Laboratory for Applied Ontology, ISTC-CNR"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://www.loa.istc.cnr.it/index.php/dolce/"


class FAIR(BaseOntology):
    """
    This is the formal vocabulary (ontology) describing the FAIR principles.
    """
    ontology_id = "FAIR"
    ontology_full_name = "FAIR Vocabulary (FAIR)"
    domain = "Upper Ontology"
    category = "Data, Metadata"
    version = None
    last_updated = None
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/FAIR"


class GFO(BaseOntology):
    """
    The General Formal Ontology is a top-level ontology for conceptual modeling,
    which is being constantly further developed by Onto-Med. It includes elaborations of categories like objects,
    processes, time and space, properties, relations, roles, functions, facts, and situations.
    Moreover, we are working on an integration with the notion of levels of reality in order
    to more appropriately capture entities in the material, mental, and social areas.
    """
    ontology_id = "GFO"
    ontology_full_name = "General Formal Ontology (GFO)"
    domain = "Upper Ontology"
    category = "Upper Ontology"
    version = None
    last_updated = "2024-11-18"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://onto-med.github.io/GFO/release/2024-11-18/index-en.html"


class SIO(BaseOntology):
    """
    The semanticscience integrated ontology (SIO) provides a simple, integrated upper level ontology (types, relations)
    for consistent knowledge representation across physical, processual and informational entities.
    This project provides foundational support for the Bio2RDF (http://bio2rdf.org) and SADI (http://sadiframework.org) projects.
    """
    ontology_id = "SIO"
    ontology_full_name = "Semanticscience Integrated Ontology (SIO)"
    domain = "Upper Ontology"
    category = "Basic"
    version = "1.59"
    last_updated = "03/25/2024"
    creator = "M. Dumontier"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://bioportal.bioontology.org/ontologies/SIO"


class SUMO(BaseOntology):
    """
    The Suggested Upper Merged Ontology (SUMO) and its domain ontologies form the largest formal public ontology
    in existence today. They are being used for research and applications in search, linguistics and reasoning.
    SUMO is the only formal ontology that has been mapped to all of the WordNet lexicon.
    """
    ontology_id = "SUMO"
    ontology_full_name = "Suggested Upper Merged Ontology (SUMO)"
    domain = "Upper Ontology"
    category = "Upper Ontology"
    version = "1.0"
    last_updated = "2025-02-17"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://www.ontologyportal.org/"
