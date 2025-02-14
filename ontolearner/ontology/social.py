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
