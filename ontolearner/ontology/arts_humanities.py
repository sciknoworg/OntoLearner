from ..base import BaseOntology


class ICON(BaseOntology):
    """
    The ICON ontology deals with high granularity art interpretation. It was developed by conceptualizing
    Panofsky's theory of levels of interpretation, therefore artworks can be described according
    to Pre-iconographical, Iconographical and Iconological information.
    """
    ontology_id = "ICON"
    ontology_full_name = "Icon Ontology (ICON)"


class MusicOntology(BaseOntology):
    """
    The Music Ontology Specification provides main concepts and
    properties fo describing music (i.e. artists, albums and tracks)
    on the Semantic Web.
    """
    ontology_id = "MusicOntology"
    ontology_full_name = "Music Ontology"


class TimelineOntology(BaseOntology):
    """
    The Timeline Ontology is centered around the notion of timeline,
    seen here as a way to identify a temporal backbone.
    A timeline may support a signal, a video, a score, a work, etc.
    """
    ontology_id = "TimelineOntology"
    ontology_full_name = "Timeline Ontology"


class ChordOntology(BaseOntology):
    """
    The Chord Ontology is an ontology for describing chords in musical pieces.
    """
    ontology_id = "ChordOntology"
    ontology_full_name = "Chord Ontology"


class Nomisma(BaseOntology):
    """
    Nomisma Ontology is a collaborative project to provide stable digital representations of numismatic concepts according
    to the principles of Linked Open Data. These take the form of http URIs that provide access to the information
    about a concept in various formats. The project is a collaborative effort of the American Numismatic Society
    and the Institute for the Study of the Ancient World at New York University.
    """
    ontology_id = "Nomisma"
    ontology_full_name = "Nomisma Ontology (Nomisma)"
