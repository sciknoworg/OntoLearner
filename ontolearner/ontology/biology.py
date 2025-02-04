from ..base import BaseOntology


class LIFO(BaseOntology):
    """Processes Life Ontology using default behavior."""
    ontology_full_name = "Life Ontology"


class GO(BaseOntology):
    """Processes Gene Ontology using default behavior."""
    ontology_full_name = "Gene Ontology"


class RO(BaseOntology):
    """Processes Relation Ontology using default behavior."""
    ontology_full_name = "Relation Ontology"
