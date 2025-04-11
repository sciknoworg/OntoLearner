from ..base.ontology import BaseOntology


class FoodOn(BaseOntology):
    """
    FoodOn, the food ontology, contains vocabulary for naming food materials and their anatomical and taxonomic origins,
    from raw harvested food to processed food products, for humans and domesticated animals.
    It provides a neutral and ontology-driven standard for government agencies,
    industry, nonprofits and consumers to name and reference food products and their components
    throughout the food supply chain.
    """
    ontology_id = "FoodOn"
    ontology_full_name = "Food Ontology (FoodON)"


class AGROVOC(BaseOntology):
    """
    AGROVOC is a relevant Linked Open Data set about agriculture available for public use and facilitates
    access and visibility of data across domains and languages. It offers a structured collection of agricultural concepts,
    terms, definitions and relationships which are used to unambiguously identify resources, allowing standardized
    indexing processes and making searches more efficient.
    """
    ontology_id = "AGROVOC"
    ontology_full_name = "AGROVOC Multilingual Thesaurus"


class PO(BaseOntology):
    """
    The Plant Ontology (PO) is a structured vocabulary and database resource that links plant anatomy,
    morphology and growth and development to plant genomics data.
    """
    ontology_id = "PO"
    ontology_full_name = "Plant Ontology (PO)"
