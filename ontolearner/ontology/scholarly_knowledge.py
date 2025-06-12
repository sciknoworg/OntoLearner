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

from rdflib import URIRef, RDF
from typing import Set, Tuple, List

from ..base.ontology import BaseOntology
from ..data_structure import TaxonomicRelation


class AIISO(BaseOntology):
    """
    The Academic Institution Internal Structure Ontology (AIISO) provides classes and properties
    to describe the internal organizational structure of an academic institution. AIISO is designed to work
    in partnership with Participation (http://purl.org/vocab/participation/schema),
    FOAF (http://xmlns.com/foaf/0.1/) and aiiso-roles (http://purl.org/vocab/aiiso-roles/schema)
    to describe the roles that people play within an institution.
    """
    ontology_id = "AIISO"
    ontology_full_name = "Academic Institution Internal Structure Ontology (AIISO)"
    domain = "Scholarly Knowledge"
    category = "Academic Institution"
    version = "1.0"
    last_updated = "2008-05-14"
    creator = "Open University"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://vocab.org/aiiso/"


class CiTO(BaseOntology):
    """
    The Citation Typing Ontology (CiTO) is an ontology that enables characterization of the nature or type of citations,
    both factually and rhetorically.
    """
    ontology_id = "CiTO"
    ontology_full_name = "Citation Typing Ontology (CiTO)"
    domain = "Scholarly Knowledge"
    category = "Scholarly Communication"
    version = "2.8.1"
    last_updated = "2018-02-16"
    creator = "Silvio Peroni, David Shotton"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://github.com/SPAROntologies/cito/tree/master/docs/current"


class CSO(BaseOntology):
    """
    The Computer Science Ontology (CSO) is a large-scale ontology of research areas in computer science.
    It provides a comprehensive vocabulary of research topics in computing, organized in a hierarchical structure.

    This class processes the Computer Science Ontology (CSO) with custom hooks for:
    - Topic-based class detection
    - superTopicOf relationships
    - contributesTo relationships
    """
    ontology_id = "CSO"
    ontology_full_name = "Computer Science Ontology (CSO)"
    domain = "Scholarly Knowledge"
    category = "Computer Science"
    version = "3.4"
    last_updated = None
    creator = "Knowledge Media Institute, Open University"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://cso.kmi.open.ac.uk/home"
    # CSO-specific URIs
    CSO_TOPIC = URIRef("http://cso.kmi.open.ac.uk/schema/cso#Topic")
    SUPER_TOPIC_OF = URIRef("http://cso.kmi.open.ac.uk/schema/cso#superTopicOf")
    CONTRIBUTES_TO = URIRef("http://cso.kmi.open.ac.uk/schema/cso#contributesTo")

    # ------------------- Term Typings Customization -------------------
    def _get_relevant_classes(self) -> Set[URIRef]:
        """Only consider CSO Topics as valid classes"""
        return set(self.rdf_graph.subjects(RDF.type, self.CSO_TOPIC))

    def check_if_class(self, entity) -> bool:
        """Check if entity is a CSO Topic"""
        return (entity, RDF.type, self.CSO_TOPIC) in self.rdf_graph

    # ------------------- Taxonomy Customization -------------------
    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomicRelation]]:
        """Extract taxonomy using superTopicOf instead of subClassOf"""
        taxonomies = []
        for parent, child in self.rdf_graph.subject_objects(self.SUPER_TOPIC_OF):
            parent_label = self.get_label(str(parent))
            child_label = self.get_label(str(child))
            if parent_label and child_label:
                taxonomies.append(TaxonomicRelation(parent=parent_label, child=child_label))

        types = list({rel.parent for rel in taxonomies} | {rel.child for rel in taxonomies})
        return sorted(types), taxonomies

    # ------------------- Non-Taxonomic Customization -------------------
    def _is_valid_non_taxonomic_triple(self, s: URIRef, p: URIRef, o: URIRef) -> bool:
        """Include contributesTo and other CSO-specific predicates"""
        valid_predicates = {self.CONTRIBUTES_TO}
        return (
            super()._is_valid_non_taxonomic_triple(s, p, o) and
            p in valid_predicates
        )

    # ------------------- Label Handling -------------------
    def get_label(self, uri: str) -> str:
        """CSO-specific label cleanup (handles URI fragments like 'computer_science')"""
        label = super().get_label(uri)
        if not label:
            # Fallback: Use last URI fragment without decoding
            return uri.split("/")[-1].replace("_", " ").title()
        return label


class DataCite(BaseOntology):
    """
    The DataCite Ontology (DataCite) is an ontology that enables the metadata properties
    of the DataCite Metadata Schema Specification (i.e., a list of metadata properties
    for the accurate and consistent identification of a resource for citation
    and retrieval purposes) to be described in RDF.
    """
    ontology_id = "DataCite"
    ontology_full_name = "DataCite Ontology (DataCite)"
    domain = "Scholarly Knowledge"
    category = "Metadata"
    version = "3.1"
    last_updated = "15/09/2022"
    creator = "David Shotton, Silvio Peroni"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://schema.datacite.org/"


class DCAT(BaseOntology):
    """
    Data Catalog Vocabulary (DCAT) is an RDF vocabulary designed to facilitate interoperability
    between data catalogs published on the Web. This document defines the schema and provides examples for its use.
    DCAT enables a publisher to describe datasets and data services in a catalog using a standard model
    and vocabulary that facilitates the consumption and aggregation of metadata from multiple catalogs.
    This can increase the discoverability of datasets and data services. It also makes it possible
    to have a decentralized approach to publishing data catalogs and makes federated search for datasets across catalogs
    in multiple sites possible using the same query mechanism and structure. Aggregated DCAT metadata
    can serve as a manifest file as part of the digital preservation process.
    """
    ontology_id = "DCAT"
    ontology_full_name = "Data Catalog Vocabulary (DCAT)"
    domain = "Scholarly Knowledge"
    category = "Data Catalogs"
    version = "3.0"
    last_updated = "22 August 2024"
    creator = "Digital Enterprise Research Institute (DERI)"
    license = "W3C Document License"
    format = "RDF"
    download_url = "https://www.w3.org/TR/vocab-dcat-3/"


class DUO(BaseOntology):
    """
    DUO is an ontology which represent data use conditions.
    """
    ontology_id = "DUO"
    ontology_full_name = "Data Use Ontology (DUO)"
    domain = "Scholarly Knowledge"
    category = "Scholarly Knowledge"
    version = "1.0"
    last_updated = "2025-02-17"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/DUO/"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle DUO-specific blank nodes."""
        if re.match(r'^APOLLO_SV_[0-9]+$', label):
            return True

        if re.match(r'^PATO_[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class EURIO(BaseOntology):
    """
    EURIO (EUropean Research Information Ontology) conceptualises, formally encodes and makes available in an open,
    structured and machine-readable format data about resarch projects funded by the EU's
    framework programmes for research and innovation.
    """
    ontology_id = "EURIO"
    ontology_full_name = "EUropean Research Information Ontology (EURIO)"
    domain = "Scholarly Knowledge"
    category = "Research Information"
    version = "2.4"
    last_updated = "2023-10-19"
    creator = "Publications Office of the European Commission"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://op.europa.eu/de/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurio"


class EXPO(BaseOntology):
    """
    Formalise generic knowledge about scientific experimental design, methodology, and results representation.
    """
    ontology_id = "EXPO"
    ontology_full_name = "Ontology of Scientific Experiments (EXPO)"
    domain = "Scholarly Knowledge"
    category = "Scientific Experiments"
    version = None
    last_updated = None
    creator = None
    license = "Academic Free License (AFL)"
    format = "OWL"
    download_url = "https://expo.sourceforge.net/"


class Framester(BaseOntology):
    """
    Framester is a a frame-based ontological resource acting as a hub
    between linguistic resources such as FrameNet, WordNet, VerbNet, BabelNet,
    DBpedia, Yago, DOLCE-Zero, and leveraging this wealth of links to create
    an interoperable predicate space formalized according to frame semantics and semiotics.
    Framester uses WordNet and FrameNet at its core, expands it to other resources
    transitively, and represents them in a formal version of frame semantics.
    """
    ontology_id = "Framester"
    ontology_full_name = "Framester Ontology (Framester)"
    domain = "Scholarly Knowledge"
    category = "Linguistics"
    version = "1.0"
    last_updated = "19-04-2016"
    creator = "Aldo Gangemi"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "http://150.146.207.114/lode/extract?url=http://ontologydesignpatterns.org/ont/framester/framester.owl"


class FRAPO(BaseOntology):
    """
    The Funding, Research Administration and Projects Ontology (FRAPO) is an ontology
    for describing the administrative information of research projects, e.g., grant applications,
    funding bodies, project partners, etc.
    """
    ontology_id = "FRAPO"
    ontology_full_name = "Funding, Research Administration and Projects Ontology (FRAPO)"
    domain = "Scholarly Knowledge"
    category = "Administration"
    version = None
    last_updated = None
    creator = "David Shotton"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "http://www.sparontologies.net/ontologies/frapo"


class FRBRoo(BaseOntology):
    """
    The FRBRoo (Functional Requirements for Bibliographic Records - object-oriented) initiative
    is a joint effort of the CIDOC Conceptual Reference Model
    and Functional Requirements for Bibliographic Records international working groups to establish
    a formal ontology intended to capture and represent the underlying semantics of bibliographic information
    and to facilitate the integration, mediation, and interchange of bibliographic and museum information.
    """
    ontology_id = "FRBRoo"
    ontology_full_name = "Functional Requirements for Bibliographic Records - object-oriented (FRBRoo)"
    domain = "Scholarly Knowledge"
    category = "Bibliographic Records"
    version = "2.4"
    last_updated = "November 2015"
    creator = None
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://ontome.net/namespace/6#summary"


class LexInfo(BaseOntology):
    """
    LexInfo allows us to associate linguistic information to elements in an ontology with respect
    to any level of linguistic description and expressivity. LexInfo has been implemented as an OWL ontology
    and is available together with an API.
    """
    ontology_id = "LexInfo"
    ontology_full_name = "LexInfo (LexInfo)"
    domain = "Scholarly Knowledge"
    category = "Linguistics"
    version = "3.0"
    last_updated = None
    creator = None
    license = "Apache 2.0"
    format = "RDF"
    download_url = "https://lexinfo.net/index.html"


class Metadata4Ing(BaseOntology):
    """
    The ontology Metadata4Ing provides a framework for the semantic description of research data
    and of the whole data generation process, embracing the object of investigation,
    all sample and data manipulation methods and tools, the data files themselves,
    and the roles of persons and institutions. The structure and application of the ontology
    are based on the principles of modularity and inheritance.
    """
    ontology_id = "Metadata4Ing"
    ontology_full_name = "Metadata for Intelligent Engineering (Metadata4Ing)"
    domain = "Scholarly Knowledge"
    category = "Materials Science"
    version = "1.3.1"
    last_updated = "2025-03-10"
    creator = "Metadata4Ing Workgroup"
    license = "Creative Commons 4.0"
    format = "TTL"
    download_url = "https://git.rwth-aachen.de/nfdi4ing/metadata4ing/metadata4ing"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle Metadata4Ing-specific blank nodes."""
        if re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class NFDIcore(BaseOntology):
    """
    The National Research Data Infrastructure (NFDI) initiative has led to the formation of various consortia,
    each focused on developing a research data infrastructure tailored to its specific domain.
    To ensure interoperability across these consortia, the NFDIcore ontology has been developed
    as a mid-level ontology for representing metadata related to NFDI resources, including individuals,
    organizations, projects, data portals, and more.
    """
    ontology_id = "NFDIcore"
    ontology_full_name = "National Research Data Infrastructure Ontology (NFDIcore)"
    domain = "Scholarly Knowledge"
    category = "Research Data Infrastructure"
    version = "3.0.0"
    last_updated = "2025-02-07"
    creator = "Jörg Waitelonis, Oleksandra Bruns, Tabea Tietz, Etienne Posthumus, Hossein Beygi Nasrabadi, Harald Sack"
    license = "Creative Commons 1.0"
    format = "OWL"
    download_url = "https://ise-fizkarlsruhe.github.io/nfdicore/"


class OBOE(BaseOntology):
    """
    The Extensible Observation Ontology (OBOE) is a formal ontology for capturing the semantics
    of scientific observation and measurement. The ontology supports researchers to add detailed semantic annotations
    to scientific data, thereby clarifying the inherent meaning of scientific observations.
    """
    ontology_id = "OBOE"
    ontology_full_name = "Extensible Observation Ontology (OBOE)"
    domain = "Scholarly Knowledge"
    category = "Scientific Observation"
    version = "1.2"
    last_updated = None
    creator = "The Regents of the University of California"
    license = "Creative Commons 3.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/OBOE"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class OPMW(BaseOntology):
    """
    The Open Provenance Model for Workflows (OPMW) is an ontology for describing workflow traces
    and their templates based on the Open Provenance Model. It has been designed as a profile for OPM,
    extending and reusing OPM's core ontologies OPMV (OPM-Vocabulary) and OPMO (OPM-Ontology).
    """
    ontology_id = "OPMW"
    ontology_full_name = "Open Provenance Model for Workflows (OPMW)"
    domain = "Scholarly Knowledge"
    category = "Workflows"
    version = "3.1"
    last_updated = "2014-12-22"
    creator = "http://delicias.dia.fi.upm.es/members/DGarijo/#me, http://www.isi.edu/~gil/"
    license = "Creative Commons Attribution 2.0 Generic (CC BY 2.0)"
    format = "OWL"
    download_url = "https://www.opmw.org/model/OPMW_20141222/"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class PPlan(BaseOntology):
    """
    The Ontology for Provenance and Plans (P-Plan) is an extension of the PROV-O ontology [PROV-O]
    created to represent the plans that guided the execution of scientific processes. P-Plan describes
    how the plans are composed and their correspondence to provenance records that describe the execution itself.
    """
    ontology_id = "PPlan"
    ontology_full_name = "Ontology for Provenance and Plans (P-Plan)"
    domain = "Scholarly Knowledge"
    category = "Scholarly Knowledge"
    version = "1.3"
    last_updated = "2014-03-12"
    creator = "http://www.isi.edu/~gil/"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://vocab.linkeddata.es/p-plan/index.html"


class PreMOn(BaseOntology):
    """
    The PreMOn Ontology is an extension of lemon (W3C Ontology Lexicon Community Group, 2015)
    for representing predicate models and their mappings. The Core Module of the PreMOn Ontology
    defines the main abstractions for modelling semantic classes with their semantic roles,
    mappings between different predicate models, and annotations.
    """
    ontology_id = "PreMOn"
    ontology_full_name = "Pre-Modern Ontology (PreMOn)"
    domain = "Scholarly Knowledge"
    category = "Linguistics"
    version = "2018a"
    last_updated = "2018-02-15"
    creator = "Francesco Corcoglioniti, Marco Rospocher <https://dkm.fbk.eu/rospocher>"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://premon.fbk.eu/ontology/core#"


class SEPIO(BaseOntology):
    """
    The SEPIO ontology is in its early stages of development, undergoing iterative refinement
    as new requirements emerge and alignment with existing standards is explored. The SEPIO core file imports two files
    which can be resolved at the URLs below:
    IAO ontology-metadata import: https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/imports/ontology-metadata.owl
    bfo mireot: https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/mireots/bfo-mireot.owl
    """
    ontology_id = "SEPIO"
    ontology_full_name = "Scientific Evidence and Provenance Information Ontology (SEPIO)"
    domain = "Scholarly Knowledge"
    category = "Scientific Evidence"
    version = None
    last_updated = "2015-02-23"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/SEPIO"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class SPDocument(BaseOntology):
    """
    SMART Protocols Ontology: Document Module is an ontology designed
    to represent metadata used to report an experimental protocol.
    """
    ontology_id = "SPDocument"
    ontology_full_name = "SMART Protocols Ontology: Document Module (SP-Document)"
    domain = "Scholarly Knowledge"
    category = "Materials Science"
    version = "4.0"
    last_updated = "2013-07-01"
    creator = "http://oxgiraldo.wordpress.com"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://github.com/SMARTProtocols/SMART-Protocols"


class SPWorkflow(BaseOntology):
    """
    SP-Workflow module represents: i) the executable  elements of a protocol; ii) the experimental actions
    and material entities that participates in instructions (sample/specimen, organisms, reagents,
    instruments);  and iii) the order of execution of the instructions.
    """
    ontology_id = "SPWorkflow"
    ontology_full_name = "SMART Protocols Ontology: Workflow Module (SP-Workflow)"
    domain = "Scholarly Knowledge"
    category = "Workflows"
    version = "4.0"
    last_updated = "2013-07-01"
    creator = "http://oxgiraldo.wordpress.com"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://github.com/SMARTProtocols/SMART-Protocols"


class SWO(BaseOntology):
    """
    The Software Ontology (SWO) is a resource for describing software tools, their types, tasks, versions,
    provenance and associated data. It contains detailed information on licensing and formats
    as well as software applications themselves, mainly (but not limited) to the bioinformatics community.
    """
    ontology_id = "SWO"
    ontology_full_name = "Software Ontology (SWO)"
    domain = "Scholarly Knowledge"
    category = "Software"
    version = "1.0"
    last_updated = "2013-07-01"
    creator = "Allyson Lister, Andy Brown, Duncan Hull, Helen Parkinson, James Malone, Jon Ison, Nandini Badarinarayan, Robert Stevens"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/SWO"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle SWO-specific blank nodes."""
        if re.match(r'^SWO_[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class TribAIn(BaseOntology):
    """
    TribAIn is an ontology for the description of tribological experiments and their results.
    It is designed to be used in the context of the TribAIn project, which aims to develop
    a knowledge-based system for the design of tribological systems.
    """
    ontology_id = "TribAIn"
    ontology_full_name = "Tribology and Artificial Intelligence Ontology (TribAIn)"
    domain = "Scholarly Knowledge"
    category = "Scholarly Knowledge"
    version = None
    last_updated = None
    creator = "Patricia Kügler"
    license = "Creative Commons 4.0"
    format = "TTL"
    download_url = "https://github.com/snow0815/tribAIn"


class VOAF(BaseOntology):
    """
    The Vocabulary of a Friend (VOAF) is a vocabulary specification providing elements allowing the description
    of vocabularies (RDFS vocabularies or OWL ontologies). It is based on Dublin Core and VOID.
    """
    ontology_id = "VOAF"
    ontology_full_name = "Vocabulary of a Friend (VOAF)"
    domain = "Scholarly Knowledge"
    category = "Social Network"
    version = "2.3"
    last_updated = "2013-05-24"
    creator = "Bernard Vatant"
    license = "Creative Commons 3.0"
    format = "RDF"
    download_url = "https://lov.linkeddata.es/vocommons/voaf/v2.3/"


class WiLD(BaseOntology):
    """
    Ontology to describe Workflows in Linked Data.
    """
    ontology_id = "WiLD"
    ontology_full_name = "Workflows in Linked Data (WiLD)"
    domain = "Scholarly Knowledge"
    category = "Materials Science"
    version = None
    last_updated = "2020-06-10"
    creator = "Tobias Käfer"
    license = "DBpedia License"
    format = "TTL"
    download_url = "https://databus.dbpedia.org/ontologies/purl.org/wild--vocab/2020.06.10-210552"
