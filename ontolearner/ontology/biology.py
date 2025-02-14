from typing import Any

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


class MarineTLO(BaseOntology):
    """
    MarineTLO is a top level ontology, generic enough to provide consistent abstractions or
    specifications of concepts included in all data models or ontologies of marine data sources and
    provide the necessary properties to make this distributed knowledge base a coherent source of
    facts relating observational data with the respective spatiotemporal context and categorical
    (systematic) domain knowledge. It can be used as the core schema for publishing Linked Data, as
    well as for setting up integration systems for the marine domain. It can be extended to any level
    of detail on demand, while preserving monotonicity. For its development and evolution we have
    adopted an iterative and incremental methodology where a new version is released every two
    months. For the implementation we use OWL 2, and to evaluate it we use a set of competency
    queries, formulating the domain requirements provided by the related communities.

    This class processes MarineTLO Ontology using default behavior.
    """
    ontology_full_name = "Marine Taxonomy and Life Ontology (MarineTLO)"

    @staticmethod
    def is_valid_label(label: str) -> Any:
        invalids = ['root']  # Allow 'Thing'
        if label.lower() in invalids:
            return None
        return label
