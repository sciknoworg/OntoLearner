from ..base import BaseOntology


class ICON(BaseOntology):
    """
    The ICON ontology deals with high granularity art interpretation. It was developed by conceptualizing
    Panofsky's theory of levels of interpretation, therefore artworks can be described according
    to Pre-iconographical, Iconographical and Iconological information.

    This class processes Icon Ontology using default behavior.
    """
    ontology_full_name = "Icon Ontology (ICON)"


class MusicOntology(BaseOntology):
    """
    The Music Ontology Specification provides main concepts and
    properties fo describing music (i.e. artists, albums and tracks)
    on the Semantic Web.

    This class processes the Music Ontology using default behavior.
    """
    ontology_full_name = "Music Ontology"


class TimelineOntology(BaseOntology):
    """
    The Timeline Ontology is centered around the notion of timeline,
    seen here as a way to identify a temporal backbone.
    A timeline may support a signal, a video, a score, a work, etc.

    This class processes the Timeline Ontology using default behavior.
    """
    ontology_full_name = "Timeline Ontology"


class ChordOntology(BaseOntology):
    """
    The Chord Ontology is an ontology for describing chords in musical pieces.

    This class processes the Chord Ontology using default behavior.
    """
    ontology_full_name = "Chord Ontology"
