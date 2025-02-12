from ..base.ontology import BaseOntology


class IOF(BaseOntology):
    """
    The IOF Core Ontology contains notions found to be common across multiple manufacturing domains.
    This file is an RDF implementation of these notions. The ontology utilizes the Basic Formal Ontology or BFO
    as a top-level ontology but also borrows terms from various domain-independent or mid-level ontologies.
    The purpose of the ontology is to serve as a foundation for ensuring consistency
    and interoperability across various domain-specific reference ontologies the IOF publishes.

    This class processes the Industrial Ontology Foundry (IOF) ontology using default behavior.
    """
    ontology_full_name = "Industrial Ontology Foundry (IOF)"
