from ..base.ontology import BaseOntology


class Hydra(BaseOntology):
    """
    Hydra is a lightweight vocabulary to create hypermedia-driven Web APIs. By specifying a number of concepts
    commonly used in Web APIs it enables the creation of generic API clients.
    """
    ontology_id = "Hydra"
    ontology_full_name = "Hydra Ontology"
    domain = "Web & Internet"
    category = "Web Development"
    version = None
    last_updated = "13 July 2021"
    creator = "Hydra W3C Community Group"
    license = "Creative Commons 4.0"
    format = "JSON-LD, RDF, TTL"
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
    domain = "Web & Internet"
    category = "interoperability"
    version = "3.2.1"
    last_updated = "2020-12-31"
    creator = "ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M)"
    license = None
    format = "OWL, RDF/XML, TTL, JSON-LD"
    download_url = "https://saref.etsi.org/core/v3.2.1/"
