from ..base.ontology import BaseOntology


class FoodOn(BaseOntology):
    """
    FoodOn, the food ontology, contains vocabulary for naming food materials and their anatomical and taxonomic origins,
    from raw harvested food to processed food products, for humans and domesticated animals.
    It provides a neutral and ontology-driven standard for government agencies,
    industry, nonprofits and consumers to name and reference food products and their components
    throughout the food supply chain.

    This class processes Food Ontology (FoodOn) using default behavior.
    """
    ontology_full_name = "Food Ontology (FoodON)"


class PO(BaseOntology):
    """
    The Plant Ontology (PO) is a structured vocabulary and database resource that links plant anatomy,
    morphology and growth and development to plant genomics data.

    This class processes Plant Ontology using default behavior.
    """
    ontology_full_name = "Plant Ontology (PO)"
