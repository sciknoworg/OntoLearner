from ontolearner.base import BaseOntology


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
    """
    ontology_full_name = "Ontology of Units of Measure (OM)"


class QUDV(BaseOntology):
    """
    The SysML QUDV (Quantities, Units, Dimensions and Values) modelLibrary is specified in a UML/SysML
    class/block diagram. In order to generalize its potential usage and alignment with other standardization efforts
    concerning quantities and units, it is of interest to verify that the QUDV model can also be represented
    in the form of an ontology using a formal ontology definition language.
    """
    ontology_full_name = "Quantities, Units, Dimensions and Values (QUDV)"


class UO(BaseOntology):
    """
    Metrical units for use in conjunction with PATO.
    """
    ontology_full_name = "Units of Measurement Ontology (UO)"


class QUDT(BaseOntology):
    """
    QUDT is an advocate for the development and implementation of standards to quantify data expressed in RDF and JSON.
    """
    ontology_full_name = "Quantities, Units, Dimensions and Data Types (QUDT)"


class OWLTime(BaseOntology):
    """
    OWL-Time is an OWL-2 DL ontology of temporal concepts, for describing the temporal properties of resources
    in the world or described in Web pages. The ontology provides a vocabulary for expressing facts
    about topological (ordering) relations among instants and intervals, together with information about durations,
    and about temporal position including date-time information. Time positions and durations may be expressed
    using either the conventional (Gregorian) calendar and clock, or using another temporal reference system
    such as Unix-time, geologic time, or different calendars.
    """
    ontology_full_name = "Time Ontology in OWL (OWL-Time)"
