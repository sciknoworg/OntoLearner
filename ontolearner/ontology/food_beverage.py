from ..base import BaseOntology


class Wine(BaseOntology):
    """
    A project to define an RDF style ontology for wines and the wine-industry
    """
    ontology_id = "Wine"
    ontology_full_name = "Wine Ontology (Wine)"
    domain = "Food & Beverage"
    category = "Wine"
    version = None
    last_updated = None
    creator = None
    license = None
    format = "RDF/XML"
    download_url = "https://github.com/UCDavisLibrary/wine-ontology"
