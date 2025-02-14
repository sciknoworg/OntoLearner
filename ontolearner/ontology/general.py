from typing import Any
from rdflib import URIRef, RDF, RDFS

from ..base import BaseOntology


class DBpedia(BaseOntology):
    """
    The DBpedia ontology is generated from the manually created specifications in the DBpedia Mappings Wiki.
    Each release of this ontology corresponds to a new release of the DBpedia dataset, which contains
    instance data extracted from various language versions of Wikipedia. The DBpedia ontology has evolved
    into a crowd-sourced effort, resulting in a shallow cross-domain ontology.

    This class processes DBpedia Ontology using default behavior.
    """
    ontology_full_name = "DBpedia Ontology"

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

    This class processes Dublin Core Ontology using default behavior.
    """
    ontology_full_name = "Dublin Core Ontology"

    @staticmethod
    def is_valid_label(label: str) -> Any:
        invalids = ['root']  # Allow 'Thing'
        if label.lower() in invalids:
            return None
        return label
