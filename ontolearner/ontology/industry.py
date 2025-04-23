from ..base import BaseOntology


class AUTO(BaseOntology):
    """
    The AUTOMOTIVE ONTOLOGY (AUTO) defines the shared conceptual structures
    in the automotive industry. It is an OWL ontology. It is built upon the auto schema.org
    extension created by the W3C Automotive Ontology Community Group. AUTO's development process
    follows the best practices established by the EDMC FIBO Community.
    """
    ontology_id = "AUTO"
    ontology_full_name = "Automotive Ontology (AUTO)"
    domain = "Industry"
    category = "Automotive"
    version = None
    last_updated = "2021-03-01"
    creator = "EDM Council"
    license = "MIT"
    format = "RDF"
    download_url = "https://github.com/edmcouncil/auto/tree/master"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class DBO(BaseOntology):
    """
    The Digital Buildings ontology (DBO) is used by Google to represent structured information
    about buildings and building-installed equipment.
    """
    ontology_id = "DBO"
    ontology_full_name = "Digital Buildings Ontology (DBO)"
    domain = "Industry"
    category = "Building Information"
    version = "0.0.1"
    last_updated = "02/23/2023"
    creator = "Google"
    license = "Apache 2.0"
    format = "OWL, CSV, RDF/XML"
    download_url = "https://github.com/google/digitalbuildings?tab=readme-ov-file"


class DOAP(BaseOntology):
    """
    The Description of a Project (DOAP) vocabulary, described using W3C RDF Schema and
    the Web Ontology Language to describe software projects, and in particular open source projects.
    """
    ontology_id = "DOAP"
    ontology_full_name = "The Description of a Project (DOAP) vocabulary"
    domain = "Industry"
    category = "Software"
    version = None
    last_updated = "2020-04-03"
    creator = "Edd Wilder-James"
    license = "Apache License 2.0"
    format = "RDF"
    download_url = "https://github.com/ewilderj/doap/blob/master/schema/doap.rdf"


class IOF(BaseOntology):
    """
    The IOF Core Ontology contains notions found to be common across multiple manufacturing domains.
    This file is an RDF implementation of these notions. The ontology utilizes the Basic Formal Ontology or BFO
    as a top-level ontology but also borrows terms from various domain-independent or mid-level ontologies.
    The purpose of the ontology is to serve as a foundation for ensuring consistency
    and interoperability across various domain-specific reference ontologies the IOF publishes.
    """
    ontology_id = "IOF"
    ontology_full_name = "Industrial Ontology Foundry (IOF)"
    domain = "Industry"
    category = "Scholarly Knowledge"
    version = "1.0"
    last_updated = "2020"
    creator = "IOF Core Working Group"
    license = "MIT"
    format = "RDF, OWL, TTL, CSV, NT"
    download_url = "https://oagi.org/pages/Released-Ontologies"


class PTO(BaseOntology):
    """
    The Product Types Ontology is designed to be used in combination with GoodRelations,
    a standard vocabulary for the commercial aspects of offers.
    """
    ontology_id = "PTO"
    ontology_full_name = "Product Types Ontology (PTO)"
    domain = "Industry"
    category = "Industry"
    version = "1.0"
    last_updated = "2025-02-21"
    creator = "Martin Hepp"
    license = "Creative Commons 3.0"
    format = "RDF, OWL, TTL, CSV, NT"
    download_url = "http://www.productontology.org/"


class TUBES(BaseOntology):
    """
    The scope of the TUBES System Ontology is to explicitly define interconnected building service system
    in the AECO industry, their hierarchical subdivisions, structural and functional aspects,
    and links to spatial entities. As such, TSO supports the effort to represent linkable information
    in a future semantic web of building data. It has a strong alignment to other ontologies within the W3C community.
    """
    ontology_id = "TUBES"
    ontology_full_name = "TUBES System Ontology"
    domain = "Industry"
    category = "Building Services"
    version = "0.3.0"
    last_updated = "2022-02-01"
    creator = "Nicolas Pauen"
    license = "Creative Commons 4.0"
    format = "RDF/XML, Turtle, JSON-LD"
    download_url = "https://rwth-e3d.github.io/tso/"
