from rdflib import URIRef, RDF
from typing import Set, Tuple, List

from ..base.ontology import BaseOntology
from ..data_structure import TaxonomicRelation


class CSO(BaseOntology):
    """
    The Computer Science Ontology (CSO) is a large-scale ontology of research areas in computer science.
    It provides a comprehensive vocabulary of research topics in computing, organized in a hierarchical structure.

    This class processes the Computer Science Ontology (CSO) with custom hooks for:
    - Topic-based class detection
    - superTopicOf relationships
    - contributesTo relationships
    """
    ontology_full_name = "Computer Science Ontology"
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


class EURIO(BaseOntology):
    """
    EURIO (EUropean Research Information Ontology) conceptualises, formally encodes and makes available in an open,
    structured and machine-readable format data about resarch projects funded by the EU's
    framework programmes for research and innovation.
    """
    ontology_full_name = "EUropean Research Information Ontology"


class NFDIcore(BaseOntology):
    """
    The National Research Data Infrastructure (NFDI) initiative has led to the formation of various consortia,
    each focused on developing a research data infrastructure tailored to its specific domain.
    To ensure interoperability across these consortia, the NFDIcore ontology has been developed
    as a mid-level ontology for representing metadata related to NFDI resources, including individuals,
    organizations, projects, data portals, and more.
    """
    ontology_full_name = "National Research Data Infrastructure Ontology (NFDIcore)"


class AIISO(BaseOntology):
    """
    The Academic Institution Internal Structure Ontology (AIISO) provides classes and properties
    to describe the internal organizational structure of an academic institution. AIISO is designed to work
    in partnership with Participation (http://purl.org/vocab/participation/schema),
    FOAF (http://xmlns.com/foaf/0.1/) and aiiso-roles (http://purl.org/vocab/aiiso-roles/schema)
    to describe the roles that people play within an institution.
    """
    ontology_full_name = "Academic Institution Internal Structure Ontology (AIISO)"


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
    ontology_full_name = "Data Catalog Vocabulary (DCAT)"


class CiTO(BaseOntology):
    """
    The Citation Typing Ontology (CiTO) is an ontology that enables characterization of the nature or type of citations,
    both factually and rhetorically.
    """
    ontology_full_name = "Citation Typing Ontology (CiTO)"


class FRBRoo(BaseOntology):
    """
    The FRBRoo (Functional Requirements for Bibliographic Records - object-oriented) initiative
    is a joint effort of the CIDOC Conceptual Reference Model
    and Functional Requirements for Bibliographic Records international working groups to establish
    a formal ontology intended to capture and represent the underlying semantics of bibliographic information
    and to facilitate the integration, mediation, and interchange of bibliographic and museum information.
    """
    ontology_full_name = "Functional Requirements for Bibliographic Records - object-oriented (FRBRoo)"


class LexInfo(BaseOntology):
    """
    LexInfo allows us to associate linguistic information to elements in an ontology with respect
    to any level of linguistic description and expressive. LexInfo has been implemented as an OWL ontology
    and is available together with an API.
    """
    ontology_full_name = "LexInfo"


class PreMOn(BaseOntology):
    """
    The PreMOn Ontology is an extension of lemon (W3C Ontology Lexicon Community Group, 2015)
    for representing predicate models and their mappings. The Core Module of the PreMOn Ontology
    defines the main abstractions for modelling semantic classes with their semantic roles,
    mappings between different predicate models, and annotations.
    """
    ontology_full_name = "Pre-Modern Ontology (PreMOn)"


class DataCite(BaseOntology):
    """
    The DataCite Ontology (DataCite) is an ontology that enables the metadata properties
    of the DataCite Metadata Schema Specification (i.e., a list of metadata properties
    for the accurate and consistent identification of a resource for citation
    and retrieval purposes) to be described in RDF.
    """
    ontology_full_name = "DataCite"


class DUO(BaseOntology):
    """
    DUO is an ontology which represent data use conditions.
    """
    ontology_full_name = "Data Use Ontology (DUO)"


class OBOE(BaseOntology):
    """
    The Extensible Observation Ontology (OBOE) is a formal ontology for capturing the semantics
    of scientific observation and measurement. The ontology supports researchers to add detailed semantic annotations
    to scientific data, thereby clarifying the inherent meaning of scientific observations.
    """
    ontology_full_name = "Extensible Observation Ontology (OBOE)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class SWO(BaseOntology):
    """
    The Software Ontology (SWO) is a resource for describing software tools, their types, tasks, versions,
    provenance and associated data. It contains detailed information on licensing and formats
    as well as software applications themselves, mainly (but not limited) to the bioinformatics community.
    """
    ontology_full_name = "Software Ontology (SWO)"


class Metadata4Ing(BaseOntology):
    """
    The ontology Metadata4Ing provides a framework for the semantic description of research data
    and of the whole data generation process, embracing the object of investigation,
    all sample and data manipulation methods and tools, the data files themselves,
    and the roles of persons and institutions. The structure and application of the ontology
    are based on the principles of modularity and inheritance.
    """
    ontology_full_name = "Metadata for Intelligent Engineering (Metadata4Ing)"


class M4I(BaseOntology):
    """
    Metadata4Ing is an ontology for describing engineering results and their corresponding workflow.
    The ontology is maintained by the Metadata4Ing working group, a subgroup of the Special Interest Group (SIG)
    Metadata & Ontologies within NFDI4Ing.
    """
    ontology_full_name = "Metadata for Engineering (M4I)"


class SEPIO(BaseOntology):
    """
    The SEPIO ontology is in its early stages of development, undergoing iterative refinement
    as new requirements emerge and alignment with existing standards is explored. The SEPIO core file imports two files
    which can be resolved at the URLs below:
    IAO ontology-metadata import: https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/imports/ontology-metadata.owl
    bfo mireot: https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/mireots/bfo-mireot.owl
    """
    ontology_full_name = "Scientific Evidence and Provenance Information Ontology (SEPIO)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class SPWorkflow(BaseOntology):
    """
    SP-Workflow module represents: i) the executable  elements of a protocol; ii) the experimental actions
    and material entities that participates in instructions (sample/specimen, organisms, reagents,
    instruments);  and iii) the order of execution of the instructions.
    """
    ontology_full_name = "SMART Protocols Ontology: Workflow Module (SP-Workflow)"


class SPDocument(BaseOntology):
    """
    SMART Protocols Ontology: Document Module is an ontology designed
    to represent metadata used to report an experimental protocol.
    """
    ontology_full_name = "SMART Protocols Ontology: Document Module (SP-Document)"


class WiLD(BaseOntology):
    """
    Ontology to describe Workflows in Linked Data.
    """
    ontology_full_name = "Workflows in Linked Data (WiLD)"


class OPMW(BaseOntology):
    """
    The Open Provenance Model for Workflows (OPMW) is an ontology for describing workflow traces
    and their templates based on the Open Provenance Model. It has been designed as a profile for OPM,
    extending and reusing OPM's core ontologies OPMV (OPM-Vocabulary) and OPMO (OPM-Ontology).
    """
    ontology_full_name = "Open Provenance Model for Workflows (OPMW)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class VOAF(BaseOntology):
    """
    The Vocabulary of a Friend (VOAF) is a vocabulary to describe vocabularies (meta-vocabulary), allowing to document
    and publish information about vocabularies (RDFS vocabularies or OWL ontologies) on the Semantic Web.
    """
    ontology_full_name = "Vocabulary of a Friend (VOAF) Ontology"


class FRAPO(BaseOntology):
    """
    The Funding, Research Administration and Projects Ontology (FRAPO) is an ontology
    for describing the administrative information of research projects, e.g., grant applications,
    funding bodies, project partners, etc.
    """
    ontology_full_name = "Funding, Research Administration and Projects Ontology (FRAPO)"
