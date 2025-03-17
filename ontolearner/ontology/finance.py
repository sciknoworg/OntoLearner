from ..base import BaseOntology


class GoodRelations(BaseOntology):
    """
    GoodRelations is a standardized vocabulary (also known as "schema", "data dictionary", or "ontology") for product,
    price, store, and company data that can (1) be embedded into existing static and dynamic Web pages and that
    (2) can be processed by other computers. This increases the visibility of your products and services
    in the latest generation of search engines, recommender systems, and other novel applications.

    This class processes GoodRelations ontology using default behavior.
    """
    ontology_full_name = "Good Relations Language Reference (GoodRelations)"


class Nomisma(BaseOntology):
    """
    Nomisma Ontology is a collaborative project to provide stable digital representations of numismatic concepts according
    to the principles of Linked Open Data. These take the form of http URIs that provide access to the information
    about a concept in various formats. The project is a collaborative effort of the American Numismatic Society
    and the Institute for the Study of the Ancient World at New York University.

    This class processes Nomisma ontology using default behavior.
    """
    ontology_full_name = "Nomisma Ontology"
