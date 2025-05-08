from ..base import BaseOntology


class GoodRelations(BaseOntology):
    """
    GoodRelations is a standardized vocabulary (also known as "schema", "data dictionary",
    or "ontology") for product, price, store, and company data that can (1) be embedded
    into existing static and dynamic Web pages and that (2) can be processed by other computers.
    This increases the visibility of your products and services in the latest generation
    of search engines, recommender systems, and other novel applications.
    """
    ontology_id = "GoodRelations"
    ontology_full_name = "Good Relations Language Reference (GoodRelations)"
    domain = "Finance"
    category = "E-commerce"
    version = "1.0"
    last_updated = "2011-10-01"
    creator = "Martin Hepp"
    license = "Creative Commons 3.0"
    format = "OWL"
    download_url = "https://www.heppnetz.de/ontologies/goodrelations/v1"
