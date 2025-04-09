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


class DEB(BaseOntology):
    """
    The devices, experimental scaffolds, and biomaterials ontology (DEB) is an open resource
    for organizing information about biomaterials, their design, manufacture, and biological testing.
    It was developed using text analysis for identifying ontology terms from a biomaterials gold standard corpus,
    systematically curated to represent the domain's lexicon. Topics covered were validated by members
    of the biomaterials research community.
    """
    ontology_full_name = "Devices, Experimental scaffolds and Biomaterials Ontology (DEB)"


class ENM(BaseOntology):
    """
    The eNanoMapper project (https://www.enanomapper.net/), NanoCommons project (https://www.nanocommons.eu/)
    and ACEnano project (http://acenano-project.eu/) are creating a pan-European computational infrastructure
    for toxicological data management for ENMs, based on semantic web standards and ontologies.
    This ontology is an application ontology targeting the full domain of nanomaterial safety assessment.
    It re-uses several other ontologies including the NPO, CHEMINF, ChEBI, and ENVO.

    This class processes the Environmental Noise Measurement Ontology (ENM) using default behavior.
    """
    ontology_full_name = "Environmental Noise Measurement Ontology (ENM)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True
