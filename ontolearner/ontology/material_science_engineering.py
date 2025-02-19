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


class FSO(BaseOntology):
    """
    The Flow Systems Ontology (FSO) is an ontology for describing interconnected systems
    with material or energy flow connections, and their components.

    This class processes the Food Study Ontology (FSO) using default behavior.
    """
    ontology_full_name = "Food Study Ontology (FSO)"
