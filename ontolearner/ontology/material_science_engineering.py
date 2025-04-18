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
    """
    ontology_id = "MMO"
    ontology_full_name = "Materials Mechanics Ontology (MMO)"


class HPOnt(BaseOntology):
    """
    The Heat Pump Ontology (HPOnt) aims to formalize and represent all the relevant information of Heat Pumps.
    The HPOnt has been developed as part of the REACT project which has received funding
    from the European Union’s Horizon 2020 research and innovation programme under grant agreement no. 824395.
    """
    ontology_id = "HPOnt"
    ontology_full_name = "The Heat Pump Ontology (HPOnt)"


class MaterialInformation(BaseOntology):
    """
    The Material Information ontology is divided into smaller ontologies (partitions).
    The partitions are Environment, Geometry, Material Information, Manufacturing Process, Property,
    Substance, Unit Dimension, Structure, Equation and Physical Constant.
    """
    ontology_id = "MaterialInformation"
    ontology_full_name = "Material Information Ontology (MaterialInformation)"


class MatOnto(BaseOntology):
    """
    The Material Ontology (MatOnto) is based on the upper level ontology, the BFO.
    """
    ontology_id = "MatOnto"
    ontology_full_name = "Material Ontology (MatOnto)"


class EMMO(BaseOntology):
    """
    The Elementary Multiperspective Material Ontology (EMMO) is the result of a multidisciplinary effort within the EMMC,
    aimed at the development of a standard representational ontology framework based on current materials modelling
    and characterization knowledge. Instead of starting from general upper level concepts, as done by other ontologies,
    the EMMO development started from the very bottom level, using the actual picture of the physical world coming
    from applied sciences, and in particular from physics and material sciences.
    """
    ontology_id = "EMMO"
    ontology_full_name = "The Elementary Multiperspective Material Ontology (EMMO)"


class MDO(BaseOntology):
    """
    MDO is an ontology for materials design field, representing the domain knowledge specifically related
    to solid-state physics and computational materials science.
    """
    ontology_id = "MDO"
    ontology_full_name = "Materials Design Ontology (MDO)"


class FSO(BaseOntology):
    """
    The Flow Systems Ontology (FSO) is an ontology for describing interconnected systems
    with material or energy flow connections, and their components.
    """
    ontology_id = "FSO"
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
    """
    ontology_id = "SSN"
    ontology_full_name = "Semantic Sensor Network Ontology (SSN)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class OntoCAPE(BaseOntology):
    """
    OntoCAPE is a large-scale ontology for the domain of Computer Aided Process Engineering (CAPE). Represented in a formal,
    machine-interpretable ontology language, OntoCAPE captures consensual knowledge of the process engineering domain
    in a generic way such that it can be reused and shared by groups of people and across software systems.
    On the basis of OntoCAPE, novel software support for various engineering activities can be developed;
    possible applications include the systematic management and retrieval of simulation models and design documents,
    electronic procurement of plant equipment, mathematical modeling,
    as well as the integration of design data from distributed sources.
    """
    ontology_id = "OntoCAPE"
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


class SystemCapabilities(BaseOntology):
    """
    This ontology describes system capabilities, operating ranges, and survival ranges.
    """
    ontology_id = "SystemCapabilities"
    ontology_full_name = "System capabilities, operating ranges, and survival ranges ontology (SystemCapabilities)"


class CHAMEO(BaseOntology):
    """
    An ontology for materials characterization which represents the evolution of the CHADA template
    in an ontological form, allowing to generate FAIR documentation of Characterisation Experiments
    and that has been used as a basis for the development of a number of technique-specific
    or application-specific ontologies in the materials characterisation domain. CHAMEO
    has been used as a foundation for the definition of the new CHADA template during the CWA.
    """
    ontology_id = "CHAMEO"
    ontology_full_name = "Characterisation Methodology Domain Ontology (CHAMEO)"


class NanoMine(BaseOntology):
    """
    Polymer Nanocomposites based ontology which enable researchers to develop and test
    broad-reaching hypotheses about how inter-relationships between different materials
    processing methods and composition result in specific changes in material properties.
    """
    ontology_id = "NanoMine"
    ontology_full_name = "NanoMine Ontology (NanoMine)"


class GPO(BaseOntology):
    """
    Basically, this ontology aims to model processes. Processes are holistic perspective elements
    that transform inputs/educts (matter, energy, information) into output/products (matter, energy, information)
    with the help of tools (devices, algorithms). They can be decomposed into sub-processes
    and have predecessor and successor processes.
    """
    ontology_id = "GPO"
    ontology_full_name = "General Process Ontology (GPO)"


class BVCO(BaseOntology):
    """
    Basically, Battery Value Chain Ontology (BVCO) aims to model processes along the Battery value chain. Processes are
    holistic perspective elements that transform inputs/educts (matter, energy, information)
    into output/products (matter, energy, information) with the help of tools (devices, algorithms).
    They can be decomposed into sub-processes and have predecessor and successor processes.
    """
    ontology_id = "BVCO"
    ontology_full_name = "Battery Value Chain Ontology (BVCO)"


class EMMOCrystallography(BaseOntology):
    """
    A crystallography domain ontology based on EMMO and the CIF core dictionary. It is implemented as a formal language.
    """
    ontology_id = "EMMOCrystallography"
    ontology_full_name = "Crystallography Ontology (EMMOCrystallography)"


class CIFCore(BaseOntology):
    """
    (1) to explain the historical development of CIF dictionaries to define in a machine-actionable manner the contents
    of data files covering various aspects of crystallography and related structural sciences; (2) to demonstrate
    some of the more complex types of information that can be handled with this approach.
    """
    ontology_id = "CIFCore"
    ontology_full_name = "Crystallographic Information Framework (CIF) Core Dictionary (CIFCore)"


class Atomistic(BaseOntology):
    """
    An EMMO-based domain ontology for atomistic and electronic modelling.
    """
    ontology_id = "Atomistic"
    ontology_full_name = "Atomistic Ontology (Atomistic)"


class DISO(BaseOntology):
    """
    DISO is an ontology that defines the linear defect, in particular dislocation concepts
    and relations between them in crystalline materials.
    """
    ontology_id = "DISO"
    ontology_full_name = "Dislocation Ontology (DISO)"


class BattINFO(BaseOntology):
    """
    BattINFO is a foundational resource for harmonizing battery knowledge representation
    and enhancing data interoperability. The primary objective is to provide the necessary tools
    to create FAIR (Findable, Accessible, Interoperable, Reusable) battery data
    that can be integrated into the Semantic Web.
    """
    ontology_id = "BattINFO"
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
    ontology_id = "MAMBO"
    ontology_full_name = "Molecules And Materials Basic Ontology (MAMBO)"


class LPBFO(BaseOntology):
    """
    The LPBF Ontology can be used to describe the additive manufacturing of a component via
    Laser Powder Bed Fusion (LPBF) / Selective Laser Melting (SLM). The ontology builds on BFO2.0
    and BWMD_mid and has been developed to be used in conjunction with the digital workflows provided
    by Fraunhofer IWM. If possible, the terminology within this ontology was used as provided by ISO/ASTM 52900:2015.
    Recently, classes relevant for Life Cycle Analysis (LCA) were added that enable sustainability assessment.
    """
    ontology_id = "LPBFO"
    ontology_full_name = "Laser Powder Bed Fusion Ontology (LPBFO)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class AMOntology(BaseOntology):
    """
    The AM ontology has been developed following two major milestones. The ontology developed within the first milestone
    includes AMProcessOntology, ModelOntology and AMOntology files. AMProcessOntology contains the set of entities
    used to capture knowledge about additive manufacturing processes. ModelOntology contains the set of entities
    used to capture knowledge about modeling concepts that represent (possibly) multi-physics multi-scale processes.
    AMOntology uses AMProcessOntology and ModelOntology files to describe entities that capture knowledge
    about characteristics of computational models for AM processes.
    """
    ontology_id = "AMOntology"
    ontology_full_name = "Additive Manufacturing Ontology (AMOntology)"


class BMO(BaseOntology):
    """
    Building Material Ontology defines the main concepts of building material,
    types, layers, and properties.
    """
    ontology_full_name = "Building Material Ontology (BMO)"


class MatVoc(BaseOntology):
    """
    The official ontology produced in the context of the STREAM project.
    """
    ontology_id = "MatVoc"
    ontology_full_name = "Materials Vocabulary (MatVoc)"


class PRIMA(BaseOntology):
    """
    An ontology that captures the provenance information in the materials science domain.
    """
    ontology_id = "PRIMA"
    ontology_full_name = "PRovenance Information in MAterials science (PRIMA)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class MechanicalTesting(BaseOntology):
    """
    A domain ontology for mechanical testing based on EMMO.
    """
    ontology_id = "MechanicalTesting"
    ontology_full_name = "Mechanical Testing Ontology (MechanicalTesting)"


class MicroStructures(BaseOntology):
    """
    This is intended to be a domain ontology for metallic microstructures, covering aspects like: composition,
    particles, both stable (primary) and metastable (precipitates), grains, subgrains,
    grain boundaries & particle free zones (PFZs), texture, dislocations. The aim is to support
    both microstructure modelling as well as characterisation.
    """
    ontology_id = "MicroStructures"
    ontology_full_name = "EMMO-based ontology for microstructures (MicroStructures)"


class MDS(BaseOntology):
    """
    Materials Data Science (MDS) is an ontology encompassing multiple domains relevant to materials science,
    chemical synthesis and characterizations, photovoltaics and geospatial datasets. The terms used for classes,
    subclasses and instances are mapped to PMDCo and BFO Ontologies.
    """
    ontology_id = "MDS"
    ontology_full_name = "Materials Data Science Ontology (MDS)"


class PMDco(BaseOntology):
    """
    The PMD Core Ontology (PMDco) is a comprehensive framework for representing knowledge that encompasses
    fundamental concepts from the domains of materials science and engineering (MSE). The PMDco
    has been designed as a mid-level ontology to establish a connection between specific MSE application ontologies
    and the domain neutral concepts found in established top-level ontologies. The primary goal of the PMDco
    is to promote interoperability between diverse domains.
    """
    ontology_id = "PMDco"
    ontology_full_name = "The Platform MaterialDigital core ontology (PMDco)"


class MSEO(BaseOntology):
    """
    MSEO utilizes the IOF Ontology stack giving materials scientists and engineers the ability
    to represent their experiments and resulting data. The goal is to create machine and human readable sematic data
    which can be easily digested by other science domains. It is a product of the joint venture Materials Open Lab Project
    between the Bundesanstalt für Materialforschung und -prüfung (BAM) and the Fraunhofer Group MATERIALS
    and uses the BWMD ontology created by Fraunhofer IWM as a starting point.
    """
    ontology_id = "MSEO"
    ontology_full_name = "Materials Science and Engineering Ontology (MSEO)"


class MOLTENSILE(BaseOntology):
    """
    An ontology for describing the tensile test process, made in the Materials Open Lab Project.
    """
    ontology_id = "MOLTENSILE"
    ontology_full_name = "Matolab Tensile Test Ontology (MOL_TENSILE)"


class ONTORULE(BaseOntology):
    """
    This deliverable consists of the ontology developed in ONTORULE for the steel industry use case.
    It is presented as an attachment to this document as an html document which was generated by SpecGen
    from the OWL file. The original OWL file is also included. This document describes the different concepts
    and attributes included in the ontology. For a better understanding of the decisions taken at the time
    of representing the knowledge in the ontology, the reader is encouraged to also read the document D5.4.
    """
    ontology_id = "ONTORULE"
    ontology_full_name = "Ontology for the Steel Domain (ONTORULE)"


class PeriodicTable(BaseOntology):
    """
    PeriodicTable.owl is a representation of the Periodic Table of the Elements in the OWL Web Ontology Language.
    It provides reference data to support Semantic Web applications in chemistry and related disciplines.
    """
    ontology_id = "PeriodicTable"
    ontology_full_name = "Periodic Table of the Elements Ontology (PeriodicTable)"


class VIMMP(BaseOntology):
    """
    The Virtual Materials Marketplace (VIMMP) project is developing an open platform for providing
    and accessing services related to materials modelling. Within VIMMP, a system of marketplace-level ontologies
    is developed to characterize services, models, and interactions between users; the European Materials
    and Modelling Ontology (EMMO, recently renamed while keeping the original acronym) is employed
    as a top-level ontology. The ontologies are used to annotate data that are stored in the ZONTAL Space component
    of VIMMP and to support the ingest and retrieval of data and metadata at the VIMMP marketplace front-end.
    """
    ontology_id = "VIMMP"
    ontology_full_name = "Virtual Materials Marketplace (VIMMP) Ontologies"


class MOLBRINELL(BaseOntology):
    """
    An ontology for describing the Brinell hardness testing process, made in the Materials Open Lab Project.
    """
    ontology_id = "MOLBRINELL"
    ontology_full_name = "MatoLab Brinell Test Ontology (MOL_BRINELL)"


class MAT(BaseOntology):
    """
    The Material Properties Ontology aims to provide the vocabulary to describe the building components,
    materials, and their corresponding properties, relevant within the construction industry. More specifically,
    the building elements and properties covered in this ontology support applications
    focused on the design of building renovation projects.
    """
    ontology_id = "MAT"
    ontology_full_name = "Material Properties Ontology (MAT)"


class CMSO(BaseOntology):
    """
    CMSO is an ontology that aims to describe computational materials science samples (or structures),
    including crystalline defects. Initially focusing on the description at the atomic scale.
    """
    ontology_id = "CMSO"
    ontology_full_name = "Computational Material Sample Ontology (CMSO)"


class Photovoltaics(BaseOntology):
    """
    This ontology is describing Perovskite solar cells.
    """
    ontology_id = "Photovoltaics"
    ontology_full_name = "EMMO Domain Ontology for Photovoltaics (Photovoltaics)"


class DSIM(BaseOntology):
    """
    Dislocation simulation and model ontology (DSIM) is an ontology developed to model various concepts
    and relationships in the discrete dislocation dynamics domain and microscopy techniques
    used in the dislocation domain. The various concepts are the numerical representation
    of dislocation applied in the dislocation dynamic simulation and the pictorial concept of pixel
    applied in representing dislocation in the experimental image, eg., TEM image, SEM image, and FIM image.
    """
    ontology_id = "DSIM"
    ontology_full_name = "Dislocation Simulation and Model Ontology (DSIM)"


class ASMO(BaseOntology):
    """
    ASMO is an ontology that aims to define the concepts needed to describe commonly
    used atomic scale simulation methods, i.e. density functional theory, molecular dynamics,
    Monte Carlo methods, etc. ASMO uses the Provenance Ontology (PROV-O) to describe the simulation process.
    """
    ontology_id = "ASMO"
    ontology_full_name = "Atomistic Simulation Methods Ontology (ASMO)"


class PODO(BaseOntology):
    """
    PODO focuses on the description of point defects in crystalline materials.
    """
    ontology_id = "PODO"
    ontology_full_name = "Point Defects Ontology (PODO)"


class CDCO(BaseOntology):
    """
    CDCO defines the common terminology shared across all types of crystallographic defects,
    providing a unified framework for data integration in materials science.
    """
    ontology_id = "CDCO"
    ontology_full_name = "Crystallographic Defect Core Ontology (CDCO)"


class LDO(BaseOntology):
    """
    LDO is an ontology designed to describe line defects in crystalline materials,
    such as dislocations and disclinations.
    """
    ontology_id = "LDO"
    ontology_full_name = "Line Defect Ontology (LDO)"


class PLDO(BaseOntology):
    """
    PLDO is an ontology designed to describe planar defects in crystalline materials,
    such as grain boundaries and stacking faults, with a focus on their atomic-scale structure and properties.
    """
    ontology_id = "PLDO"
    ontology_full_name = "Planar Defects Ontology (PLDO)"


class MSLE(BaseOntology):
    """
    The current ontology describes Material Science Lab Equipment.
    """
    ontology_id = "MSLE"
    ontology_full_name = "Material Science Lab Equipment Ontology (MSLE)"


class OIEMaterials(BaseOntology):
    """
    The materials module populates the physicalistic perspective with materials subclasses categorised
    according to modern applied physical sciences.
    """
    ontology_id = "OIEMaterials"
    ontology_full_name = "Open Innovation Environment (OIE) domain ontologies, Materials module (OIEMaterials)"


class OIEManufacturing(BaseOntology):
    """
    The manufacturing module populates the physicalistic perspective with manufacturing subclasses categorised
    according to modern applied physical sciences.
    """
    ontology_id = "OIEManufacturing"
    ontology_full_name = "Open Innovation Environment (OIE) domain ontologies, Manufacturing module (OIEManufacturing)"


class OIESoftware(BaseOntology):
    """
    Software module.
    """
    ontology_id = "OIESoftware"
    ontology_full_name = "Open Innovation Environment (OIE) domain ontologies, Software module (OIESoftware)"


class OIEModels(BaseOntology):
    """
    The models module defines models as semiotic signs that stands for an object by resembling or imitating it,
    in shape or by sharing a similar logical structure.
    """
    ontology_id = "OIEModels"
    ontology_full_name = "Open Innovation Environment (OIE) domain ontologies, Models module (OIEModels)"
