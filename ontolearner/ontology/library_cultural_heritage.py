from ontolearner.base import BaseOntology


class GND(BaseOntology):
    """
    GND stands for Gemeinsame Normdatei (Integrated Authority File) and offers a broad range of elements
    to describe authorities. The GND originates from the German library community and aims
    to solve the name ambiguity problem in the library world.
    """
    ontology_id = "GND"
    ontology_full_name = "Gemeinsame Normdatei (GND)"
