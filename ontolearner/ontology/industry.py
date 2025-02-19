
from ..base import BaseOntology


class GIST(BaseOntology):
    """
    Gist is Semantic Arts' minimalist upper ontology for the enterprise.
    It is designed to have the maximum coverage of typical business ontology concepts
    with the fewest number of primitives and the least amount of ambiguity.

    This class processes GIST ontology using default behavior.
    """
    ontology_full_name = "GIST Upper Ontology"


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


class DBO(BaseOntology):
    """
    The Digital Buildings ontology (DBO) is used by Google to represent structured information
    about buildings and building-installed equipment.

    This class processes DBO Ontology using default behavior.
    """
    ontology_full_name = "Digital Buildings Ontology (DBO)"


class TUBES(BaseOntology):
    """
    The scope of the TUBES System Ontology is to explicitly define interconnected building service system
    in the AECO industry, their hierarchical subdivisions, structural and functional aspects,
    and links to spatial entities. As such, TSO supports the effort to represent linkable information
    in a future semantic web of building data. It has a strong alignment to other ontologies within the W3C community.

    This class processes TUBES ontology using default behavior.
    """
    ontology_full_name = "TUBES System Ontology"
