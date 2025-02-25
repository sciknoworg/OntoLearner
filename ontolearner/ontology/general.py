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


class YAGO(BaseOntology):
    """
    YAGO is a large semantic knowledge base, derived from Wikipedia, WordNet, and GeoNames.
    It contains knowledge about more than 10 million entities and contains more than 120 million facts about these entities.
    YAGO is special in several ways: It has a clean taxonomy, which was manually built, and it is the only knowledge base with such a large coverage,
    the clean taxonomy, and the extraction from Wikipedia, WordNet, and GeoNames.

    This class processes YAGO Ontology using default behavior.
    """
    ontology_full_name = "YAGO Ontology"
