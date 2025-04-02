import os
from typing import Optional
from rdflib import URIRef

from ..base.ontology import BaseOntology


class MMO(BaseOntology):
    """
    The materials mechanics ontology is an application-level ontology that was created
    for supporting named entity recognition tasks for materials fatigue domain. The ontology covers
    some fairly general MSE concepts that could prospectively be merged into PMDco or other upper materials ontologies
    such as descriptions of crystallographic defects and microstructural entities.
    Furthermore, concepts related to the materials fatigue subdomain are also heavily incorporated.

    Materials Mechanics Ontology (MMO)
    """
    ontology_full_name = "Materials Mechanics Ontology (MMO)"


class HPOnt(BaseOntology):
    """
    The Heat Pump Ontology (HPOnt) aims to formalize and represent all the relevant information of Heat Pumps.
    The HPOnt has been developed as part of the REACT project which has received funding
    from the European Union’s Horizon 2020 research and innovation programme under grant agreement no. 824395.

    The Heat Pump Ontology (HPOnt)
    """
    ontology_full_name = "The Heat Pump Ontology (HPOnt)"


class MI(BaseOntology):
    """
    The Material Information ontology is divided into smaller ontologies (partitions).
    The partitions are Environment, Geometry, Material Information, Manufacturing Process, Property,
    Substance, Unit Dimension, Structure, Equation and Physical Constant.

    This class processes the Material Information ontology us using default behavior.
    """
    ontology_full_name = "Material Information Ontology (MI)"


class MatOnto(BaseOntology):
    """
    The Material Ontology (MatOnto) is based on the upper level ontology, the BFO.

    This class processes the Materials Ontology (MatOnto) using default behavior.
    """
    ontology_full_name = "Material Ontology (MatOnto)"


class EMMO(BaseOntology):
    """
    The Elementary Multiperspective Material Ontology (EMMO) is the result of a multidisciplinary effort within the EMMC,
    aimed at the development of a standard representational ontology framework based on current materials modelling
    and characterization knowledge. Instead of starting from general upper level concepts, as done by other ontologies,
    the EMMO development started from the very bottom level, using the actual picture of the physical world coming
    from applied sciences, and in particular from physics and material sciences.

    This class processes the Elementary Multiperspective Material Ontology (EMMO) using default behavior.
    """
    ontology_full_name = "The Elementary Multiperspective Material Ontology (EMMO)"


class MDO(BaseOntology):
    """
    MDO is an ontology for materials design field, representing the domain knowledge specifically related
    to solid-state physics and computational materials science.

    This class processes the Materials Design Ontology (MDO) using default behavior.
    """
    ontology_full_name = "Materials Design Ontology (MDO)"


class Metadata4Ing(BaseOntology):
    """
    The ontology Metadata4Ing provides a framework for the semantic description of research data
    and of the whole data generation process, embracing the object of investigation,
    all sample and data manipulation methods and tools, the data files themselves,
    and the roles of persons and institutions. The structure and application of the ontology
    are based on the principles of modularity and inheritance.

    This class processes the  Metadata for Intelligent Engineering (Metadata4Ing) using default behavior.
    """
    ontology_full_name = "Metadata for Intelligent Engineering (Metadata4Ing)"


class OM(BaseOntology):
    """
    The Ontology of units of Measure (OM) models concepts and relations important to scientific research.
    It has a strong focus on units, quantities, measurements, and dimensions.
    It includes, for instance, common units such as the SI units metre and kilogram,
    but also units from other systems of units such as the mile or nautical mile. For many application areas
    it includes more specific units and quantities, such as the unit of the Hubble constant or the quantity vaselife.
    The following application areas are supported by OM: Geometry; Mechanics; Thermodynamics; Electromagnetism;
    Fluid mechanics; Chemical physics; Photometry; Radiometry and Radiobiology; Nuclear physics;
    Astronomy and Astrophysics; Cosmology; Earth science; Meteorology; Material science; Microbiology;
    Economics; Information technology and Typography.

    This class processes the Ontology of Units of Measure and Related Concepts (OM) using default behavior.
    """
    ontology_full_name = "Ontology of Units of Measure (OM)"


class UO(BaseOntology):
    """
    Metrical units for use in conjunction with PATO.

    This class processes the Units of Measurement Ontology (UO) using default behavior.
    """
    ontology_full_name = "Units of Measurement Ontology (UO)"


class FSO(BaseOntology):
    """
    The Flow Systems Ontology (FSO) is an ontology for describing interconnected systems
    with material or energy flow connections, and their components.

    This class processes the Flow Systems Ontology (FSO) using default behavior.
    """
    ontology_full_name = "Flow Systems Ontology (FSO)"


class SSN(BaseOntology):
    """
    The Semantic Sensor Network (SSN) ontology is an ontology for describing sensors and their observations,
    the involved procedures, the studied features of interest, the samples used to do so, and the observed properties,
    as well as actuators. SSN follows a horizontal and vertical modularization architecture
    by including a lightweight but self-contained core ontology called SOSA (Sensor, Observation, Sample, and Actuator)
    for its elementary classes and properties. With their different scope and different degrees of axiomatization,
    SSN and SOSA are able to support a wide range of applications and use cases, including satellite imagery,
    large-scale scientific monitoring, industrial and household infrastructures, social sensing, citizen science,
    observation-driven ontology engineering, and the Web of Things. Both ontologies are described below,
    and examples of their usage are given.

    This class processes the Semantic Sensor Network Ontology (SSN) using default behavior.
    """
    ontology_full_name = "Semantic Sensor Network Ontology (SSN)"


class OntoCAPE(BaseOntology):
    """
    OntoCAPE is a large-scale ontology for the domain of Computer Aided Process Engineering (CAPE). Represented in a formal,
    machine-interpretable ontology language, OntoCAPE captures consensual knowledge of the process engineering domain
    in a generic way such that it can be reused and shared by groups of people and across software systems.
    On the basis of OntoCAPE, novel software support for various engineering activities can be developed;
    possible applications include the systematic management and retrieval of simulation models and design documents,
    electronic procurement of plant equipment, mathematical modeling,
    as well as the integration of design data from distributed sources.

    This class processes the Ontology of Computer-Aided Process Engineering (OntoCAPE) using default behavior.
    """
    ontology_full_name = "Ontology of Computer-Aided Process Engineering (OntoCAPE)"

    def __init__(self, language: str = 'en', base_dir: Optional[str] = None):
        super().__init__(language=language, base_dir=base_dir)

    def _resolve_import_def(self, uri: URIRef) -> Optional[str]:
        uri_str = str(uri)
        # Process file URI
        if uri_str.startswith("file:///"):
            file_path = uri_str[8:]
        elif uri_str.startswith("file://"):
            file_path = uri_str[7:]
        else:
            file_path = uri_str

        file_path = file_path.replace('\\', '/')

        # Handle Windows drive letter
        if ':' in file_path:
            file_path = file_path.split(':', 1)[1]

        # OntoCAPE-specific handling: extract path after 'OntoCAPE/'
        if 'OntoCAPE/' in file_path:
            parts = file_path.split('OntoCAPE/', 1)
            if len(parts) > 1:
                relative_path = parts[1]
                resolved_path = os.path.join(self.base_dir, relative_path)
                if os.path.exists(resolved_path):
                    return resolved_path
        return super()._resolve_import_def(uri)


class QUDT(BaseOntology):
    """
    QUDT is an advocate for the development and implementation of standards to quantify data expressed in RDF and JSON.

    This class processes the Quantities, Units, Dimensions and Data Types (QUDT) using default behavior.
    """
    ontology_full_name = "Quantities, Units, Dimensions and Data Types (QUDT)"


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


class SWO(BaseOntology):
    """
    The Software Ontology (SWO) is a resource for describing software tools, their types, tasks, versions,
    provenance and associated data. It contains detailed information on licensing and formats
    as well as software applications themselves, mainly (but not limited) to the bioinformatics community.

    This class processes the Software Ontology (SWO) using default behavior.
    """
    ontology_full_name = "Software Ontology (SWO)"


class SystemCapabilities(BaseOntology):
    """
    This ontology describes system capabilities, operating ranges, and survival ranges.
    """
    ontology_full_name = "System capabilities, operating ranges, and survival ranges ontology (SystemCapabilities)"


class SEPIO(BaseOntology):
    """
    The SEPIO ontology is in its early stages of development, undergoing iterative refinement
    as new requirements emerge and alignment with existing standards is explored. The SEPIO core file imports two files
    which can be resolved at the URLs below:
    IAO ontology-metadata import: https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/imports/ontology-metadata.owl
    bfo mireot: https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/mireots/bfo-mireot.owl
    """
    ontology_full_name = "Scientific Evidence and Provenance Information Ontology (SEPIO)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class MGED(BaseOntology):
    """
    The Materials Genome Ontology (MGED) is a domain ontology for materials science and engineering.
    """
    ontology_full_name = "Materials Genome Ontology (MGED)"


class CHAMEO(BaseOntology):
    """
    An ontology for materials characterization which represents the evolution of the CHADA template
    in an ontological form, allowing to generate FAIR documentation of Characterisation Experiments
    and that has been used as a basis for the development of a number of technique-specific
    or application-specific ontologies in the materials characterisation domain. CHAMEO
    has been used as a foundation for the definition of the new CHADA template during the CWA.
    """
    ontology_full_name = "Characterisation Methodology Domain Ontology (CHAMEO)"


class NanoMine(BaseOntology):
    """
    Polymer Nanocomposites based ontology which enable researchers to develop and test
    broad-reaching hypotheses about how inter-relationships between different materials
    processing methods and composition result in specific changes in material properties.
    """
    ontology_full_name = "NanoMine Ontology (NanoMine)"


class GPO(BaseOntology):
    """
    Basically, this ontology aims to model processes. Processes are holistic perspective elements
    that transform inputs/educts (matter, energy, information) into output/products (matter, energy, information)
    with the help of tools (devices, algorithms). They can be decomposed into sub-processes
    and have predecessor and successor processes.
    """
    ontology_full_name = "General Process Ontology (GPO)"


class BVCO(BaseOntology):
    """
    Basically, Battery Value Chain Ontology (BVCO) aims to model processes along the Battery value chain. Processes are
    holistic perspective elements that transform inputs/educts (matter, energy, information)
    into output/products (matter, energy, information) with the help of tools (devices, algorithms).
    They can be decomposed into sub-processes and have predecessor and successor processes.
    """
    ontology_full_name = "Battery Value Chain Ontology (BVCO)"


class EMMOCrystallography(BaseOntology):
    """
    A crystallography domain ontology based on EMMO and the CIF core dictionary. It is implemented as a formal language.
    """
    ontology_full_name = "Crystallography Ontology (EMMOCrystallography)"


class CIFCore(BaseOntology):
    """
    (1) to explain the historical development of CIF dictionaries to define in a machine-actionable manner the contents
    of data files covering various aspects of crystallography and related structural sciences; (2) to demonstrate
    some of the more complex types of information that can be handled with this approach.
    """
    ontology_full_name = "Crystallographic Information Framework (CIF) Core Dictionary (CIFCore)"


class Atomistic(BaseOntology):
    """
    An EMMO-based domain ontology for atomistic and electronic modelling.
    """
    ontology_full_name = "Atomistic Ontology (Atomistic)"


class DISO(BaseOntology):
    """
    DISO is an ontology that defines the linear defect, in particular dislocation concepts
    and relations between them in crystalline materials.
    """
    ontology_full_name = "Dislocation Ontology (DISO)"


class BattINFO(BaseOntology):
    """
    BattINFO is a foundational resource for harmonizing battery knowledge representation
    and enhancing data interoperability. The primary objective is to provide the necessary tools
    to create FAIR (Findable, Accessible, Interoperable, Reusable) battery data
    that can be integrated into the Semantic Web.
    """
    ontology_full_name = "Battery Interface Ontology (BattINFO)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class MAMBO(BaseOntology):
    """
    MAMBO (Molecules And Materials Basic Ontology) is a domain ontology for molecular materials.
    Its main targets are: Allowing the retrieval of structured information regarding molecular materials
    and related applications (i.e. devices based on molecular materials) Supporting the development of new,
    complex workflows for modelling systems based on molecular materials (computational modelling
    and data-driven techniques) Integrating data generated via computational simulations and empirical experiments.
    """
    ontology_full_name = "Molecules And Materials Basic Ontology (MAMBO)"


class LPBFO(BaseOntology):
    """
    The LPBF Ontology can be used to describe the additive manufacturing of a component via
    Laser Powder Bed Fusion (LPBF) / Selective Laser Melting (SLM). The ontology builds on BFO2.0
    and BWMD_mid and has been developed to be used in conjunction with the digital workflows provided
    by Fraunhofer IWM. If possible, the terminology within this ontology was used as provided by ISO/ASTM 52900:2015.
    Recently, classes relevant for Life Cycle Analysis (LCA) were added that enable sustainability assessment.
    """
    ontology_full_name = "Laser Powder Bed Fusion Ontology (LPBFO)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True
