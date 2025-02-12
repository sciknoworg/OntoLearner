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

    This class processes the EUropean Research Information Ontology (EURIO) using default behavior.
    """
    ontology_full_name = "EUropean Research Information Ontology"


class NFDIcore(BaseOntology):
    """
    The National Research Data Infrastructure (NFDI) initiative has led to the formation of various consortia,
    each focused on developing a research data infrastructure tailored to its specific domain.
    To ensure interoperability across these consortia, the NFDIcore ontology has been developed
    as a mid-level ontology for representing metadata related to NFDI resources, including individuals,
    organizations, projects, data portals, and more.

    This class processes the National Research Data Infrastructure (NFDI) using default behavior.
    """
    ontology_full_name = "National Research Data Infrastructure Ontology (NFDIcore)"
