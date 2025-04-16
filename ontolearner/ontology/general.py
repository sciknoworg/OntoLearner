from rdflib import URIRef, RDF, RDFS

from ..base import BaseOntology


class DBpedia(BaseOntology):
    """
    The DBpedia ontology is generated from the manually created specifications in the DBpedia Mappings Wiki.
    Each release of this ontology corresponds to a new release of the DBpedia dataset, which contains
    instance data extracted from various language versions of Wikipedia. The DBpedia ontology has evolved
    into a crowd-sourced effort, resulting in a shallow cross-domain ontology.
    """
    ontology_id = "DBpedia"
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
    """
    ontology_id = "DublinCore"
    ontology_full_name = "Dublin Core Vocabulary (DublinCore)"


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


class SchemaOrg(BaseOntology):
    """
    Schema.org is a collaborative, community activity with a mission to create,
    maintain, and promote schemas for structured data on the Internet, on web pages, in email messages, and beyond.
    """
    ontology_id = "SchemaOrg"
    ontology_full_name = "Schema.org Ontology (SchemaOrg)"


class UMBEL(BaseOntology):
    """
    UMBEL is the Upper Mapping and Binding Exchange Layer, designed to help content interoperate on the Web.
    UMBEL provides two valuable functions: First, it is a broad, general reference structure of 34,000 concepts,
    which provides a scaffolding to link and interoperate other datasets and domain vocabularies.
    Second, it is a base vocabulary for the construction of other concept-based domain ontologies,
    also designed for interoperation.
    """
    ontology_id = "UMBEL"
    ontology_full_name = "Upper Mapping and Binding Exchange Layer (UMBEL) Vocabulary"


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


class EDAM(BaseOntology):
    """
    EDAM is a domain ontology of data analysis and data management in bio- and other sciences, and science-based applications.
    It comprises concepts related to analysis, modelling, optimisation, and data life cycle. Targetting usability by diverse users,
    the structure of EDAM is relatively simple, divided into 4 main sections: Topic, Operation, Data (incl. Identifier), and Format.
    """
    ontology_id = "EDAM"
    ontology_full_name = "The ontology of data analysis and management (EDAM)"


class RO(BaseOntology):
    """
    The Relations Ontology (RO) is a collection of OWL relations (ObjectProperties) intended for use
    across a wide variety of biological ontologies.
    """
    ontology_id = "RO"
    ontology_full_name = "Relation Ontology (RO)"


class IAO(BaseOntology):
    """
    The Information Artifact Ontology (IAO) is an ontology of information entities,
    originally driven by work by the OBI digital entity and realizable information entity branch.
    """
    ontology_id = "IAO"
    ontology_full_name = "Information Artifact Ontology (IAO)"


class GIST(BaseOntology):
    """
    Gist is Semantic Arts' minimalist upper ontology for the enterprise.
    It is designed to have the maximum coverage of typical business ontology concepts
    with the fewest number of primitives and the least amount of ambiguity.
    """
    ontology_id = "GIST"
    ontology_full_name = "GIST Upper Ontology (GIST)"


class CCO(BaseOntology):
    """
    The Common Core Ontologies (CCO) is a widely-used suite of eleven ontologies that consist
    of logically well-defined generic terms and relations among them reflecting entities across all domains of interest.
    """
    ontology_id = "CCO"
    ontology_full_name = "Common Core Ontologies (CCO)"
