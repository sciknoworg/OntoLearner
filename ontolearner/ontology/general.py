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

import re
from rdflib import URIRef, RDF, RDFS

from ..base import BaseOntology


class CCO(BaseOntology):
    """
    The Common Core Ontologies (CCO) is a widely-used suite of eleven ontologies that consist
    of logically well-defined generic terms and relations among them reflecting entities across all domains of interest.
    """
    ontology_id = "CCO"
    ontology_full_name = "Common Core Ontologies (CCO)"
    domain = "General Knowledge"
    category = "General"
    version = "2.0"
    last_updated = "2024-11-06"
    creator = None
    license = "BSD-3-Clause license"
    format = "TTL"
    download_url = "https://github.com/CommonCoreOntology/CommonCoreOntologies"


class DBpedia(BaseOntology):
    """
    The DBpedia ontology is generated from the manually created specifications in the DBpedia Mappings Wiki.
    Each release of this ontology corresponds to a new release of the DBpedia dataset, which contains
    instance data extracted from various language versions of Wikipedia. The DBpedia ontology has evolved
    into a crowd-sourced effort, resulting in a shallow cross-domain ontology.
    """
    ontology_id = "DBpedia"
    ontology_full_name = "DBpedia Ontology (DBpedia)"
    domain = "General Knowledge"
    category = "Knowledge Graph"
    version = None
    last_updated = "2008-11-17"
    creator = "DBpedia Maintainers and Contributors"
    license = "Creative Commons 3.0"
    format = "OWL"
    download_url = "https://wiki.dbpedia.org/"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle DBpedia/Wikidata-specific blank nodes."""
        # DBpedia/Wikidata-specific patterns
        if re.match(r'^Q[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False

    def _is_valid_non_taxonomic_triple(self, s: URIRef, p: URIRef, o: URIRef) -> bool:
        # Include datatype properties and validate domain/range
        domain = self.rdf_graph.value(p, RDFS.domain)
        range = self.rdf_graph.value(p, RDFS.range)

        return (
            self.check_if_class(s) and
            (isinstance(o, URIRef) or self.check_if_class(o)) and
            p != RDFS.subClassOf and
            (domain is None or (s, RDF.type, domain) in self.rdf_graph) and
            (range is None or (o, RDF.type, range) in self.rdf_graph)
        )


class DublinCore(BaseOntology):
    """
    The Dublin Core Schema is a small set of vocabulary terms that can be used to describe several kinds of resources.
    Dublin Core Metadata may be used for multiple purposes, from simple resource description,
    to combining metadata vocabularies of different metadata standards, to providing interoperability
    for metadata vocabularies in the Linked Data cloud and Semantic Web implementations.
    """
    ontology_id = "DublinCore"
    ontology_full_name = "Dublin Core Vocabulary (DublinCore)"
    domain = "General Knowledge"
    category = "Metadata"
    version = "1.1"
    last_updated = "February 17, 2017"
    creator = "The Dublin Core Metadata Initiative"
    license = "Public Domain"
    format = "RDF"
    download_url = "https://bioportal.bioontology.org/ontologies/DC"


class EDAM(BaseOntology):
    """
    EDAM is a domain ontology of data analysis and data management in bio- and other sciences, and science-based applications.
    It comprises concepts related to analysis, modelling, optimisation, and data life cycle. Targetting usability by diverse users,
    the structure of EDAM is relatively simple, divided into 4 main sections: Topic, Operation, Data (incl. Identifier), and Format.
    """
    ontology_id = "EDAM"
    ontology_full_name = "The ontology of data analysis and management (EDAM)"
    domain = "General Knowledge"
    category = "General"
    version = "1.25-20240924T0027Z-unstable(1.26)"
    last_updated = "24.09.2024"
    creator = "Federico Bianchini, Hervé Ménager, Jon Ison, Matúš Kalaš"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/edam"


class GIST(BaseOntology):
    """
    Gist is Semantic Arts' minimalist upper ontology for the enterprise.
    It is designed to have the maximum coverage of typical business ontology concepts
    with the fewest number of primitives and the least amount of ambiguity.
    """
    ontology_id = "GIST"
    ontology_full_name = "GIST Upper Ontology (GIST)"
    domain = "General Knowledge"
    category = "Upper Ontology"
    version = "12.1.0"
    last_updated = "2024-Feb-27"
    creator = "Semantic Arts"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://semanticarts.com/gist"


class IAO(BaseOntology):
    """
    The Information Artifact Ontology (IAO) is an ontology of information entities,
    originally driven by work by the OBI digital entity and realizable information entity branch.
    """
    ontology_id = "IAO"
    ontology_full_name = "Information Artifact Ontology (IAO)"
    domain = "General Knowledge"
    category = "Information, Data, Knowledge"
    version = None
    last_updated = "2022-11-07"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/IAO"


class PROV(BaseOntology):
    """
    The PROV Ontology (PROV-O) expresses the PROV Data Model [PROV-DM] using the OWL2 Web Ontology Language (OWL2) [OWL2-OVERVIEW].
    It provides a set of classes, properties, and restrictions that can be used to represent
    and interchange provenance information generated in different systems and under different contexts.
    It can also be specialized to create new classes and properties to model provenance information
    for different applications and domains. The PROV Document Overview describes the overall state of PROV,
    and should be read before other PROV documents.
    """
    ontology_id = "PROV"
    ontology_full_name = "PROV Ontology (PROV-O)"
    domain = "General Knowledge"
    category = "General"
    version = "2013-04-30"
    last_updated = "2013-04-30"
    creator = None
    license = "W3C Software License"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/PROV"


class RO(BaseOntology):
    """
    The Relations Ontology (RO) is a collection of OWL relations (ObjectProperties) intended for use
    across a wide variety of biological ontologies.
    """
    ontology_id = "RO"
    ontology_full_name = "Relation Ontology (RO)"
    domain = "General Knowledge"
    category = "Relations"
    version = "2024-04-24"
    last_updated = "2024-04-24"
    creator = None
    license = "CC0"
    format = "OWL"
    download_url = "http://purl.obolibrary.org/obo/ro.owl"


class SchemaOrg(BaseOntology):
    """
    Schema.org is a collaborative, community activity with a mission to create,
    maintain, and promote schemas for structured data on the Internet, on web pages, in email messages, and beyond.
    """
    ontology_id = "SchemaOrg"
    ontology_full_name = "Schema.org Ontology (SchemaOrg)"
    domain = "General Knowledge"
    category = "Web Development"
    version = "28.1"
    last_updated = "2024-11-22"
    creator = "Schema.org Community"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://github.com/schemaorg/schemaorg/blob/main/data/releases/28.1/schemaorg.owl"


class UMBEL(BaseOntology):
    """
    UMBEL is the Upper Mapping and Binding Exchange Layer, designed to help content interoperate on the Web.
    UMBEL provides two valuable functions: First, it is a broad, general reference structure of 34,000 concepts,
    which provides a scaffolding to link and interoperate other datasets and domain vocabularies.
    Second, it is a base vocabulary for the construction of other concept-based domain ontologies,
    also designed for interoperation.
    """
    ontology_id = "UMBEL"
    ontology_full_name = "Upper Mapping and Binding Exchange Layer Vocabulary (UMBEL)"
    domain = "General Knowledge"
    category = "Web Development"
    version = "1.50"
    last_updated = "May 10, 2016"
    creator = None
    license = None
    format = "n3"
    download_url = "https://github.com/structureddynamics/UMBEL/tree/master/Ontology"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle UMBEL-specific blank nodes."""
        # UMBEL-specific patterns
        if re.match(r'^f5295f96ac3e649dcb1740b0d93d3e6c2b[0-9a-f]+$', label):  # Long hexadecimal identifiers
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class YAGO(BaseOntology):
    """
    YAGO is a large semantic knowledge base, derived from Wikipedia, WordNet, and GeoNames.
    It contains knowledge about more than 10 million entities and contains more than 120 million facts about these entities.
    YAGO is special in several ways: It has a clean taxonomy, which was manually built,
    and it is the only knowledge base with such a large coverage,
    the clean taxonomy, and the extraction from Wikipedia, WordNet, and GeoNames.
    """
    ontology_id = "YAGO"
    ontology_full_name = "YAGO Ontology (YAGO)"
    domain = "General Knowledge"
    category = "People, Cities, Countries, Movies, Organizations"
    version = "4.5"
    last_updated = "April, 2024"
    creator = "Max Planck Institute for Informatics"
    license = "Creative Commons 3.0"
    format = "TTL"
    download_url = "https://yago-knowledge.org/downloads/yago-4-5"
