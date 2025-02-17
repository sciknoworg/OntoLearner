
from ..base.ontology import BaseOntology


class SIOC(BaseOntology):
    """
    The SIOC (Semantically-Interlinked Online Communities) Ontology is an ontology for describing the
    information in online communities. This includes sites that support online discussions, blogging,
    file sharing, photo sharing, social networking, etc.

    This class processes the SIOC ontology using default behavior.
    """
    ontology_full_name = "Semantically-Interlinked Online Communities (SIOC) Ontology"


class FOAF(BaseOntology):
    """
    FOAF is a project devoted to linking people and information using the Web.
    Regardless of whether information is in people's heads, in physical or digital documents,
    or in the form of factual data, it can be linked.

    This class processes the FOAF ontology using default behavior.
    """
    ontology_full_name = "Friend of a Friend (FOAF) Ontology"


class BIO(BaseOntology):
    """
    The BIO vocabulary contains terms useful for finding out more about people and their backgrounds and has some cross-over into genealogical information.
    The approach taken is to describe a person's life as a series of interconnected key events, around which other information can be woven.
    This vocabulary defines the event framework and supplies a set of core event types that cover many use cases, but it is expected that it
    will be extended in other vocabularies to suit their needs. The intention of this vocabulary is to describe biographical events of people
    and this intention carries through to the definitions of the properties and classes which are person-centric rather than neutral. For example
    the Employment event puts the person being employed as the principal agent in the event rather than the employer.

    This class processes BIO Ontology using default behavior.
    """
    ontology_full_name = "BIO: A vocabulary for biographical information"


class VOAF(BaseOntology):
    """
    The Vocabulary of a Friend (VOAF) is a vocabulary to describe vocabularies (meta-vocabulary), allowing to document
    and publish information about vocabularies (RDFS vocabularies or OWL ontologies) on the Semantic Web.

    This class processes the VOAF ontology using default behavior.
    """
    ontology_full_name = "Vocabulary of a Friend (VOAF) Ontology"
