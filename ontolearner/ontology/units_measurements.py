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
    ontology_id = "OM"
    ontology_full_name = "Ontology of Units of Measure (OM)"
    domain = "Units and Measurements"
    category = "Units and Measurements"
    version = "2.0.57"
    last_updated = "June 28, 2024"
    creator = "Hajo Rijgersberg, Don Willems, Jan Top"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://bioportal.bioontology.org/ontologies/OM"


class OWLTime(BaseOntology):
    """
    OWL-Time is an OWL-2 DL ontology of temporal concepts, for describing the temporal properties of resources
    in the world or described in Web pages. The ontology provides a vocabulary for expressing facts
    about topological (ordering) relations among instants and intervals, together with information about durations,
    and about temporal position including date-time information. Time positions and durations may be expressed
    using either the conventional (Gregorian) calendar and clock, or using another temporal reference system
    such as Unix-time, geologic time, or different calendars.
    """
    ontology_id = "OWLTime"
    ontology_full_name = "Time Ontology in OWL (OWL-Time)"
    domain = "Units and Measurements"
    category = "Temporal Reasoning"
    version = "1.0"
    last_updated = "15 November 2022"
    creator = "World Wide Web Consortium"
    license = "W3C Software Notice and Document License"
    format = "TTL"
    download_url = "https://www.w3.org/TR/owl-time/"


class QUDT(BaseOntology):
    """
    QUDT is an advocate for the development and implementation of standards to quantify data expressed in RDF and JSON.
    """
    ontology_id = "QUDT"
    ontology_full_name = "Quantities, Units, Dimensions and Data Types (QUDT)"
    domain = "Units and Measurements"
    category = "Physics"
    version = "2.1"
    last_updated = "March 1, 2022"
    creator = "NASA Ames Research Center"
    license = "Creative Commons 4.0"
    format = "TTL"
    download_url = "https://qudt.org/"


class QUDV(BaseOntology):
    """
    The SysML QUDV (Quantities, Units, Dimensions and Values) modelLibrary is specified in a UML/SysML
    class/block diagram. In order to generalize its potential usage and alignment with other standardization efforts
    concerning quantities and units, it is of interest to verify that the QUDV model can also be represented
    in the form of an ontology using a formal ontology definition language.
    """
    ontology_id = "QUDV"
    ontology_full_name = "Quantities, Units, Dimensions and Values (QUDV)"
    domain = "Units and Measurements"
    category = "Units and Measurements"
    version = "2009-10-30"
    last_updated = "2009-10-30"
    creator = "SysML"
    license = "Apache License 2.0"
    format = "OWL"
    download_url = "https://www.omgwiki.org/OMGSysML/doku.php?id=sysml-qudv:qudv_owl"


class UO(BaseOntology):
    """
    Metrical units for use in conjunction with PATO.
    """
    ontology_id = "UO"
    ontology_full_name = "Units of Measurement Ontology (UO)"
    domain = "Units and Measurements"
    category = "Units and Measurements"
    version = None
    last_updated = "2023-05-25"
    creator = "KAUST"
    license = "Creative Commons 3.0"
    format = "OWL"
    download_url = "https://bioportal.bioontology.org/ontologies/UO"
