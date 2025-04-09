"""
Industry-specific ontology implementations including GIST, IOF, DBO,
TUBES, PTO, DOAP, GoodRelations, and AUTO.
"""
from ..base import BaseOntology


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


class PTO(BaseOntology):
    """
    The Product Types Ontology is designed to be used in combination with GoodRelations,
    a standard vocabulary for the commercial aspects of offers.

    This class processes Product Types Ontology using default behavior.
    """
    ontology_full_name = "Product Types Ontology (PTO)"


class DOAP(BaseOntology):
    """
    The Description of a Project (DOAP) vocabulary, described using W3C RDF Schema and
    the Web Ontology Language to describe software projects, and in particular open source projects.

    This class processes DOAP ontology using default behavior.
    """
    ontology_full_name = "The Description of a Project (DOAP) vocabulary"


class AUTO(BaseOntology):
    """
    The AUTOMOTIVE ONTOLOGY (AUTO) defines the shared conceptual structures
    in the automotive industry. It is an OWL ontology. It is built upon the auto schema.org
    extension created by the W3C Automotive Ontology Community Group. AUTO's development process
    follows the best practices established by the EDMC FIBO Community.

    This class processes Automotive Ontology using default behavior.
    """
    ontology_full_name = "Automotive Ontology (AUTO)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True
