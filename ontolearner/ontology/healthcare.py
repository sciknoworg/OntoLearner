from ..base import BaseOntology


class DOID(BaseOntology):
    """
    The Disease Ontology has been developed as a standardized ontology for human disease
    with the purpose of providing the biomedical community with consistent,
    reusable and sustainable descriptions of human disease terms,
    phenotype characteristics and related medical vocabulary disease concepts.

    This class processes the Human Disease Ontology (DOID) using default behavior.
    """
    ontology_full_name = "Human Disease Ontology"


class MFOEM(BaseOntology):
    """
    The Mental Functioning Ontology - Emotion Module (MFOEM) aims to include all relevant aspects of affective phenomena
    including their bearers, the different types of emotions, moods, etc., their different parts and dimensions
    of variation, their facial and vocal expressions, and the role of emotions and affective phenomena
    in general in influencing human behavior.This class processes Mental Functioning Ontology of Emotions (MFOEM)
    using default behavior.

    This class processes the Emotion Ontology (MFOEM) using default behavior.
    """
    ontology_full_name = "Emotion Ontology -- Mental Functioning Ontology of Emotions"


class OBI(BaseOntology):
    """
    The Ontology for Biomedical Investigations (OBI) helps you communicate clearly about scientific investigations
    by defining more than 2500 terms for assays, devices, objectives, and more.

    This class processes the Ontology for Biomedical Investigations (OBI) using default behavior.
    """
    ontology_full_name = "Ontology for Biomedical Investigations (OBI)"


class PRoteinOntology(BaseOntology):
    """
    The PRotein Ontology (PRO) formally defines taxon-specific and taxon-neutral protein-related entities
    in three major areas: proteins related by evolution; proteins produced from a given gene;
    and protein-containing complexes.

    This class processes the Protein Ontology (PRO) using default behavior.
    """
    ontology_full_name = "Protein Ontology (PRO)"


class BTO(BaseOntology):
    """
    A structured controlled vocabulary for the source of an enzyme comprising tissues,
    cell lines, cell types and cell cultures.

    This class processes the BRENDA Tissue Ontology (BTO) using default behavior.
    """
    ontology_full_name = "BRENDA Tissue Ontology (BTO)"


class NCIt(BaseOntology):
    """
    NCI Thesaurus (NCIt) is a reference terminology that includes broad coverage of the cancer domain,
    including cancer related diseases, findings and abnormalities. The NCIt OBO Edition aims to increase integration
    of the NCIt with OBO Library ontologies. NCIt OBO Edition releases should be considered experimental.

    This class processes the National Cancer Institute Thesaurus (NCIt) using default behavior.
    """
    ontology_full_name = "NCI Thesaurus (NCIt)"
