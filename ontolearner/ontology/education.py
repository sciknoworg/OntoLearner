
from ..base import BaseOntology


class Bibframe(BaseOntology):
    """
    The Bibframe vocabulary consists of RDF classes and properties used for the description of
    items cataloged principally by libraries, but may also be used to describe items cataloged by museums and archives.
    Classes include the three core classes - Work, Instance, and Item - in addition to many more
    classes to support description. Properties describe characteristics of the resource being
    described as well as relationships among resources. For example: one Work
    might be a "translation of" another Work; an Instance may be an
    "instance of" a particular Bibframe Work.  Other properties describe attributes of Works and Instances.  For
    example: the Bibframe property "subject" expresses an important attribute of a Work
    (what the Work is about), and the property "extent" (e.g. number of pages) expresses an
    attribute of an Instance.

    This class processes the Bibliographic Framework Ontology (BIBFRAME) using default behavior.
    """
    ontology_full_name = "Bibliographic Framework Ontology (BIBFRAME)"


class DoCO(BaseOntology):
    """
    DoCO, the Document Components Ontology, is an OWL 2 DL ontology that provides a general-purpose structured vocabulary
    of document elements. DoCO has been designed as a general unifying ontological framework for describing different aspects
    related to the content of scientific and other scholarly texts. Its primary goal has been to improve the interoperability
    and shareability of academic documents (and related services) when multiple formats are actually used for their storage.
    """
    ontology_full_name = "Document Components Ontology (DoCO)"


class Common(BaseOntology):
    """
    OSCCA is a computer course architectural ontology system for associating computer learners to select and
    explore a set of appropriate courses and curriculums. An ontology is used for defining relationships between
    items in order to assist the user to find their interesting knowledge points
    """
    ontology_full_name = "Common Ontology"
