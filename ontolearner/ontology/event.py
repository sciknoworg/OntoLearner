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


class ICalendar(BaseOntology):
    """
    iCalendar is an Internet standard for exchanging calendar and scheduling data across different applications
    and platforms using a standardized text-based format (.ics). It enables interoperability for events, tasks,
    and scheduling, supporting features like recurring events, invitations, and time zone adjustments.
    While widely used in applications like Google Calendar and Outlook, its complexity and partial implementations
    pose challenges, leading to efforts to integrate it with Semantic Web technologies
    for enhanced data linking and automation.

    This class processes iCalendar ontology using default behavior.
    """
    ontology_full_name = "iCalendar Vocabulary"


class LODE(BaseOntology):
    """
    People conventionally refer to an action or occurrence taking place at a certain time
    at a specific location as an event. This notion is potentially useful for connecting individual facts
    recorded in the rapidly growing collection of linked data sets and for discovering more complex relationships
    between data. The LODE provide an overview and comparison of existing event models,
    looking at the different choices they make of how to represent events. It is a model for publishing records
    of events as Linked Data. A tools for populating this model and a prototype “event directory” web service,
    which can be used to locate stable URIs for events that have occurred,
    provide RDFS+OWL descriptions and link to related resources.

    This class processes LODE ontology using default behavior.
    """
    ontology_full_name = "Linking Open Descriptions of Events (LODE)"
