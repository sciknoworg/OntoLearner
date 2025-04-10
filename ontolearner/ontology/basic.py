from ..base import BaseOntology


class BFO(BaseOntology):
    """
    The Basic Formal Ontology (BFO) is a small, upper-level ontology that describes
    the basic types of entities in the world and how they relate to each other.
    """
    ontology_id = "BFO"
    ontology_full_name = "Basic Formal Ontology (BFO)"


class GFO(BaseOntology):
    """
    The General Formal Ontology is a top-level ontology for conceptual modeling,
    which is being constantly further developed by Onto-Med. It includes elaborations of categories like objects,
    processes, time and space, properties, relations, roles, functions, facts, and situations.
    Moreover, we are working on an integration with the notion of levels of reality in order
    to more appropriately capture entities in the material, mental, and social areas.
    """
    ontology_id = "GFO"
    ontology_full_name = "General Formal Ontology (GFO)"


class DOLCE(BaseOntology):
    """
    The Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE) is a foundational ontology
    that provides a conceptual framework for the formalization of domain ontologies.

    This class processes DOLCE using default behavior.
    """
    ontology_full_name = "Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE)"


class SIO(BaseOntology):
    """
    The semanticscience integrated ontology (SIO) provides a simple, integrated upper level ontology (types, relations)
    for consistent knowledge representation across physical, processual and informational entities.
    This project provides foundational support for the Bio2RDF (http://bio2rdf.org) and SADI (http://sadiframework.org) projects.
    """
    ontology_id = "SIO"
    ontology_full_name = "Semanticscience Integrated Ontology (SIO)"


class SUMO(BaseOntology):
    """
    The Suggested Upper Merged Ontology (SUMO) and its domain ontologies form the largest formal public ontology
    in existence today. They are being used for research and applications in search, linguistics and reasoning.
    SUMO is the only formal ontology that has been mapped to all of the WordNet lexicon.
    """
    ontology_id = "SUMO"
    ontology_full_name = "Suggested Upper Merged Ontology (SUMO)"


class FAIR(BaseOntology):
    """
    This is the formal vocabulary (ontology) describing the FAIR principles.
    """
    ontology_id = "FAIR"
    ontology_full_name = "FAIR Vocabulary (FAIR)"
