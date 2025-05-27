# Copyright (c) 2025 SciKnowOrg
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
from ..base import BaseOntology


class AFO(BaseOntology):
    """
    The AFO is an ontology suite that provides a standard vocabulary and semantic model
    for the representation of laboratory analytical processes. The AFO suite is aligned at the upper layer
    to the Basic Formal Ontology (BFO). The core domains modeled include, Equipment, Material, Process, and Results.
    This artifact contains all triples of Allotrope Foundation Merged Without QUDT Ontology Suite (REC/2023/12)
    together with triples inferred with HermiT.
    """
    ontology_id = "AFO"
    ontology_full_name = "Allotrope Foundation Ontology (AFO)"
    domain = "Chemistry"
    category = "Laboratory Analytical Processes"
    version = "2024-06"
    last_updated = "2024-06-28"
    creator = "Allotrope Foundation"
    license = "CC BY 4.0"
    format = "TTL"
    download_url = "https://terminology.tib.eu/ts/ontologies/AFO"


class ChEBI(BaseOntology):
    """
    Chemical Entities of Biological Interest (ChEBI) is a dictionary of molecular entities
    focused on ‘small’ chemical compounds. The term ‘molecular entity’ refers to any constitutionally
    or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer, etc.,
    identifiable as a separately distinguishable entity. The molecular entities in question
    are either products of nature or synthetic products used to intervene in the processes of living organisms.
    ChEBI incorporates an ontological classification, whereby the relationships between molecular entities
    or classes of entities and their parents and/or children are specified.
    """
    ontology_id = "ChEBI"
    ontology_full_name = "Chemical Entities of Biological Interest (ChEBI)"
    domain = "Chemistry"
    category = "Chemical Entities"
    version = "239"
    last_updated = "01/01/2025"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://www.ebi.ac.uk/chebi/"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle ChEBI-specific blank nodes."""
        # ChEBI-specific patterns
        if re.match(r'^CHEBI_[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class CHEMINF(BaseOntology):
    """
    The chemical information ontology (cheminf) describes information entities about chemical entities.
    It provides qualitative and quantitative attributes to richly describe chemicals.
    Includes terms for the descriptors commonly used in cheminformatics software applications
    and the algorithms which generate them.
    """
    ontology_id = "CHEMINF"
    ontology_full_name = "Chemical Information Ontology (CHEMINF)"
    domain = "Chemistry"
    category = "Chemistry"
    version = "2.1.0"
    last_updated = None
    creator = "Egon Willighagen, Nina Jeliazkova, Ola Spjuth, Valery Tkachenko"
    license = "Creative Commons 1.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/CHEMINF"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle CHEMINF-specific blank nodes."""
        # ChEBI-specific patterns
        if re.match(r'^CHEMINF_[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class CHIRO(BaseOntology):
    """
    CHEBI provides a distinct role hierarchy. Chemicals in the structural hierarchy are connected via a 'has role' relation.
    CHIRO provides links from these roles to useful other classes in other ontologies.
    This will allow direct connection between chemical structures (small molecules, drugs) and what they do.
    This could be formalized using 'capable of', in the same way Uberon and the Cell Ontology link structures to processes.
    """
    ontology_id = "CHIRO"
    ontology_full_name = "CHEBI Integrated Role Ontology (CHIRO)"
    domain = "Chemistry"
    category = "Chemicals, Roles"
    version = "2015-11-23"
    last_updated = "2015-11-23"
    creator = None
    license = "Creative Commons 1.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/chiro"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class ChMO(BaseOntology):
    """
    The Chemical Methods Ontology contains more than 3000 classes and describes methods used to:
    - collect data in chemical experiments, such as mass spectrometry and electron microscopy.
    - prepare and separate material for further analysis, such as sample ionisation, chromatography, and electrophoresis
    - synthesise materials, such as epitaxy and continuous vapour deposition It also describes the instruments used
        in these experiments, such as mass spectrometers and chromatography columns and their outputs.
    """
    ontology_id = "ChMO"
    ontology_full_name = "Chemical Methods Ontology (ChMO)"
    domain = "Chemistry"
    category = "Chemistry"
    version = None
    last_updated = "2022-04-19"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://github.com/rsc-ontologies/rsc-cmo"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle ChMO-specific blank nodes."""
        # ChEBI-specific patterns
        if re.match(r'^CHMO_[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class FIX(BaseOntology):
    """
    An ontology of physico-chemical methods and properties.
    """
    ontology_id = "FIX"
    ontology_full_name = "FIX Ontology (FIX)"
    domain = "Chemistry"
    category = "Chemicals, Properties"
    version = "2020-04-13"
    last_updated = "2020-04-13"
    creator = None
    license = None
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/FIX"


class MassSpectrometry(BaseOntology):
    """
    A structured controlled vocabulary for the annotation of experiments concerned with proteomics mass spectrometry.
    """
    ontology_id = "MassSpectrometry"
    ontology_full_name = "Mass Spectrometry Ontology (MassSpectrometry)"
    domain = "Chemistry"
    category = "Mass Spectrometry, Proteomics"
    version = None
    last_updated = "12:02:2025"
    creator = "Andreas Bertsch"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/MS"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle MassSpectrometry-specific blank nodes."""
        # MassSpectrometry-specific patterns
        if re.match(r'^PEFF_[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class MOP(BaseOntology):
    """
    MOP is the molecular process ontology. It contains the molecular processes that underlie
    the name reaction ontology RXNO, for example cyclization, methylation and demethylation.
    """
    ontology_id = "MOP"
    ontology_full_name = "Molecular Process Ontology (MOP)"
    domain = "Chemistry"
    category = "Chemistry, Molecular Biology"
    version = "2022-05-11"
    last_updated = "2022-05-11"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/MOP"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle MOP-specific blank nodes."""
        # MOP-specific patterns
        if re.match(r'^MOP_[0-9]+$', label):
            return True
        # ChEBI-specific patterns in MOP
        if re.match(r'^CHEBI_[0-9]+$', label):
            return True
        # RXNO-specific patterns in MOP
        if re.match(r'^RXNO_[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


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
    """
    ontology_id = "NMRCV"
    ontology_full_name = "Nuclear Magnetic Resonance Controlled Vocabulary (NMRCV)"
    domain = "Chemistry"
    category = "Chemistry"
    version = "1.1.0"
    last_updated = "2017-10-19"
    creator = "Daniel Schober"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/NMRCV"


class OntoKin(BaseOntology):
    """
    OntoKin is an ontology developed for representing chemical kinetic reaction mechanisms.
    """
    ontology_id = "OntoKin"
    ontology_full_name = "Chemical Kinetics Ontology (OntoKin)"
    domain = "Chemistry"
    category = "Chemistry"
    version = "1.0"
    last_updated = "08 February 2022"
    creator = "IEEE"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://www.ontologyportal.org/"


class PROCO(BaseOntology):
    """
    PROCO (PROcess Chemistry Ontology) is a formal ontology that aims to standardly represent entities
    and relations among entities in the domain of process chemistry.
    """
    ontology_id = "PROCO"
    ontology_full_name = "PROcess Chemistry Ontology (PROCO)"
    domain = "Chemistry"
    category = "Chemicals, Processes"
    version = "04-14-2022"
    last_updated = "04-14-2022"
    creator = "Anna Dun, Wes A. Schafer, Yongqun \"Oliver\" He (YH), Zachary Dance"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://github.com/proco-ontology/PROCO"


class PSIMOD(BaseOntology):
    """
    PSI-MOD is an ontology developed by the Proteomics Standards Initiative (PSI) that describes protein chemical modifications,
    logically linked by an is_a relationship in such a way as to form a direct acyclic graph (DAG).
    The PSI-MOD ontology has more than 45 top-level nodes, and provides alternative hierarchical paths
    for classifying protein modifications either by the molecular structure of the modification,
    or by the amino acid residue that is modified.
    """
    ontology_id = "PSIMOD"
    ontology_full_name = "Protein Modifications Ontology (PSIMOD)"
    domain = "Chemistry"
    category = "Protein Modifications"
    version = "1.031.6"
    last_updated = "2022-06-13"
    creator = None
    license = "Creative Commons Attribution 4.0"
    format = "OWL"
    download_url = "https://github.com/HUPO-PSI/psi-mod-CV"


class REX(BaseOntology):
    """
    REX is an ontology of physico-chemical processes, i.e. physico-chemical changes occurring in course of time.
    REX includes both microscopic processes (involving molecular entities or subatomic particles) and macroscopic processes.
    Some biochemical processes from Gene Ontology (GO Biological process) can be described as instances of REX.
    """
    ontology_id = "REX"
    ontology_full_name = "Physico-chemical process ontology (REX)"
    domain = "Chemistry"
    category = "Chemistry"
    version = "1.0"
    last_updated = "2025-03-11"
    creator = "University of Warsaw"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/REX"


class RXNO(BaseOntology):
    """
    RXNO is the name reaction ontology. It contains more than 500 classes representing organic reactions
    such as the Diels–Alder cyclization.
    """
    ontology_id = "RXNO"
    ontology_full_name = "Reaction Ontology (RXNO)"
    domain = "Chemistry"
    category = "Chemistry"
    version = None
    last_updated = "2021-12-16"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://github.com/rsc-ontologies/rxno"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle RXNO-specific blank nodes."""
        # RXNO-specific patterns
        if re.match(r'^RXNO_[0-9]+$', label):
            return True
        # MOP-specific patterns in RXNO
        if re.match(r'^MOP_[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class VIBSO(BaseOntology):
    """
    The Vibration Spectroscopy Ontology defines technical terms with which research data produced
    in vibrational spectroscopy experiments can be semantically enriched, made machine readable and FAIR.
    """
    ontology_id = "VIBSO"
    ontology_full_name = "Vibrational Spectroscopy Ontology (VIBSO)"
    domain = "Chemistry"
    category = "Spectroscopy"
    version = "2024-09-23"
    last_updated = "2024-09-23"
    creator = "VIBSO Workgroup"
    license = "Creative Commons Attribution 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/vibso"
