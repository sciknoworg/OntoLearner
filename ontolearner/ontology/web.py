from ..base.ontology import BaseOntology


class Hydra(BaseOntology):
    """
    Hydra is a lightweight vocabulary to create hypermedia-driven Web APIs. By specifying a number of concepts
    commonly used in Web APIs it enables the creation of generic API clients.

    This class processes the Hydra Ontology using default behavior.
    """
    ontology_full_name = "Hydra Ontology"


class SAREF(BaseOntology):
    """
    The Smart Applications REFerence (SAREF) suite of ontologies forms a shared model of consensus
    intended to enable semantic interoperability between solutions from different providers
    and among various activity sectors in the Internet of Things (IoT),
    thus contributing to the development of data spaces. SAREF is published as a set of open standards
    produced by ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M).

    This class processes the Smart Applications REFerence ontology (SAREF) using default behavior.
    """
    ontology_full_name = "Smart Applications REFerence ontology"
