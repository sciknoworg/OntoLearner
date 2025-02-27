from ..base import BaseOntology


class ConferenceOntology(BaseOntology):
    """
    The conference-ontology is a new self-contained ontology for modeling knowledge about conferences.
    The conference-ontology adopts the best ontology design practices (e.g., Ontology Design Patterns,
    ontology reuse and interlinking) and guarantees interoperability with SWC ontology
    and all other pertinent vocabularies.

    This class processes Conference Ontology using default behavior.
    """
    ontology_full_name = "Conference Ontology"


class OWLTime(BaseOntology):
    """
    OWL-Time is an OWL-2 DL ontology of temporal concepts, for describing the temporal properties of resources
    in the world or described in Web pages. The ontology provides a vocabulary for expressing facts
    about topological (ordering) relations among instants and intervals, together with information about durations,
    and about temporal position including date-time information. Time positions and durations may be expressed
    using either the conventional (Gregorian) calendar and clock, or using another temporal reference system
    such as Unix-time, geologic time, or different calendars.

    This class processes OWL-Time ontology using default behavior.
    """
    ontology_full_name = "Time Ontology in OWL (OWL-Time)"
