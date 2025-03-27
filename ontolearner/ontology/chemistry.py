from ..base import BaseOntology


class ChEBI(BaseOntology):
    """
    Chemical Entities of Biological Interest (ChEBI) is a dictionary of molecular entities
    focused on ‘small’ chemical compounds. The term ‘molecular entity’ refers to any constitutionally
    or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer, etc.,
    identifiable as a separately distinguishable entity. The molecular entities in question
    are either products of nature or synthetic products used to intervene in the processes of living organisms.
    ChEBI incorporates an ontological classification, whereby the relationships between molecular entities
    or classes of entities and their parents and/or children are specified.

    This class processes Chemical Entities of Biological Interest using default behavior.
    """
    ontology_full_name = "Chemical Entities of Biological Interest (ChEBI)"


class ChMO(BaseOntology):
    """
    The Chemical Methods Ontology contains more than 3000 classes and describes methods used to:
    - collect data in chemical experiments, such as mass spectrometry and electron microscopy.
    - prepare and separate material for further analysis, such as sample ionisation, chromatography, and electrophoresis
    - synthesise materials, such as epitaxy and continuous vapour deposition It also describes the instruments used
        in these experiments, such as mass spectrometers and chromatography columns and their outputs.

    This class processes Chemical Methods Ontology using default behavior.
    """
    ontology_full_name = "Chemical Methods Ontology (ChMO)"


class RXNO(BaseOntology):
    """
    RXNO is the name reaction ontology. It contains more than 500 classes representing organic reactions
    such as the Diels–Alder cyclization.

    This class processes the Reaction Ontology (RXNO) using default behavior.
    """
    ontology_full_name = "Reaction Ontology (RXNO)"


class REX(BaseOntology):
    """
    REX is an ontology of physico-chemical processes, i.e. physico-chemical changes occurring in course of time.
    REX includes both microscopic processes (involving molecular entities or subatomic particles) and macroscopic processes.
    Some biochemical processes from Gene Ontology (GO Biological process) can be described as instances of REX.

    This class processes the Reaction Expression Ontology (REX) using default behavior.
    """
    ontology_full_name = "Physico-chemical process ontology (REX)"


class CHEMINF(BaseOntology):
    """
    The chemical information ontology (cheminf) describes information entities about chemical entities.
    It provides qualitative and quantitative attributes to richly describe chemicals.
    Includes terms for the descriptors commonly used in cheminformatics software applications
    and the algorithms which generate them.

    This class processes the Chemical Information Ontology (CHEMINF) using default behavior.
    """
    ontology_full_name = "Chemical Information Ontology (CHEMINF)"


class NMRCV(BaseOntology):
    """
    This artefact is an MSI-approved controlled vocabulary primarily developed under COSMOS EU and PhenoMeNal EU governance.
    The nmrCV is supporting the nmrML XML format with standardized terms. nmrML is a vendor agnostic open access NMR raw data standard.
    Its primaly role is analogous to the mzCV for the PSI-approved mzML XML format. It uses BFO2.0 as its Top level.
    This CV was derived from two predecessors (The NMR CV from the David Wishart Group, developed by Joseph Cruz)
    and the MSI nmr CV developed by Daniel Schober at the EBI. This simple taxonomy of terms (no DL semantics used)
    serves the nuclear magnetic resonance markup language (nmrML) with meaningful descriptors to amend the nmrML xml file
    with CV terms. Metabolomics scientists are encouraged to use this CV to annotrate their raw and experimental context data,
    i.e. within nmrML. The approach to have an exchange syntax mixed of an xsd and CV stems from the PSI mzML effort.
    The reason to branch out from an xsd into a CV is, that in areas where the terminology is likely to change faster
    than the nmrML xsd could be updated and aligned, an externally and decentrallised maintained CV can accompensate
    for such dynamics in a more flexible way. A second reason for this set-up is that semantic validity of CV terms
    used in an nmrML XML instance (allowed CV terms, position/relation to each other, cardinality) can be validated
    by rule-based proprietary validators: By means of cardinality specifications and XPath expressions defined
    in an XML mapping file (an instances of the CvMappingRules.xsd ), one can define what ontology terms are allowed
    in a specific location of the data model.

    This class processes the Nuclear Magnetic Resonance Controlled Vocabulary (NMRCV) using default behavior.
    """
    ontology_full_name = "Nuclear Magnetic Resonance Controlled Vocabulary (NMRCV)"


class OntoKin(BaseOntology):
    """
    OntoKin is an ontology developed for representing chemical kinetic reaction mechanisms.

    This class processes the OntoKin ontology using default behavior.
    """
    ontology_full_name = "OntoKin"


class MOP(BaseOntology):
    """
    MOP is the molecular process ontology. It contains the molecular processes that underlie
    the name reaction ontology RXNO, for example cyclization, methylation and demethylation.

    This class processes the Molecular Process Ontology (MOP) using default behavior.
    """
    ontology_full_name = "Molecular Process Ontology (MOP)"


class Chiro(BaseOntology):
    """
    CHEBI provides a distinct role hierarchy. Chemicals in the structural hierarchy are connected via a 'has role' relation.
    CHIRO provides links from these roles to useful other classes in other ontologies.
    This will allow direct connection between chemical structures (small molecules, drugs) and what they do.
    This could be formalized using 'capable of', in the same way Uberon and the Cell Ontology link structures to processes.

    This class processes the Chiro ontology using default behavior.
    """
    ontology_full_name = "Chiro"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class PROCO(BaseOntology):
    """
    PROCO (PROcess Chemistry Ontology) is a formal ontology that aims to standardly represent entities
    and relations among entities in the domain of process chemistry.

    This class processes the PROCO ontology using default behavior.
    """
    ontology_full_name = "PROcess Chemistry Ontology (PROCO)"


class FIX(BaseOntology):
    """
    An ontology of physico-chemical methods and properties.

    This class processes the FIX ontology using default behavior.
    """
    ontology_full_name = "FIX Ontology (FIX)"


class MassSpectrometry(BaseOntology):
    """
    A structured controlled vocabulary for the annotation of experiments concerned with proteomics mass spectrometry.

    This class processes the Mass Spectrometry ontology using default behavior.
    """
    ontology_full_name = "Mass Spectrometry Ontology (MS)"


class AFO(BaseOntology):
    """
    The AFO is an ontology suite that provides a standard vocabulary and semantic model
    for the representation of laboratory analytical processes. The AFO suite is aligned at the upper layer
    to the Basic Formal Ontology (BFO). The core domains modeled include, Equipment, Material, Process, and Results.
    This artifact contains all triples of Allotrope Foundation Merged Without QUDT Ontology Suite (REC/2023/12)
    together with triples inferred with HermiT.

    This class processes the Allotrope Foundation Ontology (AFO) using default behavior.
    """
    ontology_full_name = "Allotrope Foundation Ontology (AFO)"


class VIBSO(BaseOntology):
    """
    The Vibration Spectroscopy Ontology defines technical terms with which research data produced
    in vibrational spectroscopy experiments can be semantically enriched, made machine readable and FAIR.

    This class processes the Vibrational Spectroscopy Ontology (VIBSO) using default behavior.
    """
    ontology_full_name = "Vibrational Spectroscopy Ontology (VIBSO)"
