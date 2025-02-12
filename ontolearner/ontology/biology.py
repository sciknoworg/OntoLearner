from ..base import BaseOntology


class LIFO(BaseOntology):
    """
    The Life Ontology (LifO) is an ontology of the life of organism. LifO represents the
    life processes of organisms and related entities and relations. LifO is a general
    purpose ontology that covers the common features associated with different
    organisms such as unicellular prokaryotes (e.g., E. coli) and multicellular organisms (e.g., human).

    This class processes Life Ontology using default behavior.
    """
    ontology_full_name = "Life Ontology (LifO)"


class GO(BaseOntology):
    """
    The Gene Ontology (GO) Provides structured controlled vocabularies for the annotation of gene products
    with respect to their molecular function, cellular component, and biological role.

    This class processes Gene Ontology using default behavior.
    """
    ontology_full_name = "Gene Ontology (GO)"


class RO(BaseOntology):
    """
    The Relations Ontology (RO) is a collection of OWL relations (ObjectProperties) intended for use
    across a wide variety of biological ontologies.

    This class processes Relation Ontology using default behavior.
    """
    ontology_full_name = "Relation Ontology (RO)"
