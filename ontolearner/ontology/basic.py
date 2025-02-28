from ..base import BaseOntology


class BFO(BaseOntology):
    """
    The Basic Formal Ontology (BFO) is a small, upper-level ontology that describes
    the basic types of entities in the world and how they relate to each other.

    This class processes Basic Formal Ontology with BFO-specific behavior.
    """
    ontology_full_name = "Basic Formal Ontology (BFO)"


class GFO(BaseOntology):
    """
    The General Formal Ontology is a top-level ontology for conceptual modeling,
    which is being constantly further developed by Onto-Med. It includes elaborations of categories like objects,
    processes, time and space, properties, relations, roles, functions, facts, and situations.
    Moreover, we are working on an integration with the notion of levels of reality in order
    to more appropriately capture entities in the material, mental, and social areas.

    This class processes General Formal Ontology using default behavior
    """
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

    This class processes SIO using default behavior.
    """
    ontology_full_name = "Semanticscience Integrated Ontology (SIO)"
