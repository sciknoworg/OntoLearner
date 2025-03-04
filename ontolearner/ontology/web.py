from ..base.ontology import BaseOntology


class SecurityOntology(BaseOntology):
    """
    The vocabulary used to ensure the authenticity and integrity of Verifiable Credentials and similar types
    of constrained digital documents using cryptography, especially through the use of digital signatures
    and related mathematical proofs.

    This class processes the Security Ontology using default behavior.
    """
    ontology_full_name = "Security Ontology"


class Hydra(BaseOntology):
    """
    Hydra is a lightweight vocabulary to create hypermedia-driven Web APIs. By specifying a number of concepts
    commonly used in Web APIs it enables the creation of generic API clients.

    This class processes the Hydra Ontology using default behavior.
    """
    ontology_full_name = "Hydra Ontology"
