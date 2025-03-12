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
    ontology_full_name = "Chemical Methods Ontology (Chebi)"


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
