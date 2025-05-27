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

import os
import re
from typing import Optional
from rdflib import URIRef

from ..base.ontology import BaseOntology


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
    domain = "Materials Science and Engineering"
    category = "Manufacturing"
    version = "1.0"
    last_updated = "2023-05-10"
    creator = "Iassou Souroko, Ali Riza Durmaz"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/iassouroko/AMontology"


class ASMO(BaseOntology):
    """
    ASMO is an ontology that aims to define the concepts needed to describe commonly
    used atomic scale simulation methods, i.e. density functional theory, molecular dynamics,
    Monte Carlo methods, etc. ASMO uses the Provenance Ontology (PROV-O) to describe the simulation process.
    """
    ontology_id = "ASMO"
    ontology_full_name = "Atomistic Simulation Methods Ontology (ASMO)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "1.0.0"
    last_updated = None
    creator = "https://orcid.org/0000-0001-7564-7990"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://github.com/OCDO/asmo?tab=readme-ov-file#atomistic-simulation-methods-ontology-asmo"


class Atomistic(BaseOntology):
    """
    An EMMO-based domain ontology for atomistic and electronic modelling.
    """
    ontology_id = "Atomistic"
    ontology_full_name = "Atomistic Ontology (Atomistic)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "0.0.2"
    last_updated = None
    creator = "Francesca L. Bleken, Jesper Friis"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/emmo-repo/domain-atomistic"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle Atomistic-specific blank nodes."""
        # EMMO-specific patterns (UUID format) in Atomistic
        if re.match(r'^EMMO_[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class BattINFO(BaseOntology):
    """
    BattINFO is a foundational resource for harmonizing battery knowledge representation
    and enhancing data interoperability. The primary objective is to provide the necessary tools
    to create FAIR (Findable, Accessible, Interoperable, Reusable) battery data
    that can be integrated into the Semantic Web.
    """
    ontology_id = "BattINFO"
    ontology_full_name = "Battery Interface Ontology (BattINFO)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = None
    last_updated = None
    creator = None
    license = None
    format = "TTL"
    download_url = "https://github.com/BIG-MAP/BattINFO"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle BattINFO-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        # Check for substance_, electrochemistry_, battery_ followed by UUIDs
        if re.match(r'^substance_' + uuid_pattern, label):
            return True
        if re.match(r'^electrochemistry_' + uuid_pattern, label):
            return True
        if re.match(r'^battery_' + uuid_pattern, label):
            return True
        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class BMO(BaseOntology):
    """
    Building Material Ontology defines the main concepts of building material,
    types, layers, and properties.
    """
    ontology_id = "BMO"
    ontology_full_name = "Building Material Ontology (BMO)"
    domain = "Materials Science and Engineering"
    category = "Materials"
    version = "0.1"
    last_updated = "2019-12-10"
    creator = "Janakiram Karlapudi, Prathap Valluru"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://matportal.org/ontologies/BUILDMAT"


class BVCO(BaseOntology):
    """
    Basically, Battery Value Chain Ontology (BVCO) aims to model processes along the Battery value chain. Processes are
    holistic perspective elements that transform inputs/educts (matter, energy, information)
    into output/products (matter, energy, information) with the help of tools (devices, algorithms).
    They can be decomposed into sub-processes and have predecessor and successor processes.
    """
    ontology_id = "BVCO"
    ontology_full_name = "Battery Value Chain Ontology (BVCO)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "0.4.3"
    last_updated = None
    creator = "Lukas Gold, Simon Stier"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/Battery-Value-Chain-Ontology/ontology"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle BVCO-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^BVCO_' + uuid_pattern, label):
            return True
        if re.match(r'^GPO_' + uuid_pattern, label):
            return True
        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True
        if re.match(r'^electrochemistry_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


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
    domain = "Materials Science and Engineering"
    category = "Manufacturing"
    version = "2.0"
    last_updated = None
    creator = "RWTH Aachen University"
    license = "GNU General Public License."
    format = "OWL"
    download_url = "https://www.avt.rwth-aachen.de/cms/avt/forschung/sonstiges/software/~ipts/ontocape/?lidx=1"

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


class CDCO(BaseOntology):
    """
    CDCO defines the common terminology shared across all types of crystallographic defects,
    providing a unified framework for data integration in materials science.
    """
    ontology_id = "CDCO"
    ontology_full_name = "Crystallographic Defect Core Ontology (CDCO)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "1.0.0"
    last_updated = None
    creator = "https://orcid.org/0000-0001-7564-7990"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://github.com/OCDO/cdco"


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
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "1.0.0"
    last_updated = "2024-04-12"
    creator = "https://orcid.org/0000-0002-4181-2852, https://orcid.org/0000-0002-5174-8508, https://orcid.org/0000-0002-9668-6961"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/emmo-repo/domain-characterisation-methodology"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle CHAMEO-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class CIFCore(BaseOntology):
    """
    (1) to explain the historical development of CIF dictionaries to define in a machine-actionable manner the contents
    of data files covering various aspects of crystallography and related structural sciences; (2) to demonstrate
    some of the more complex types of information that can be handled with this approach.
    """
    ontology_id = "CIFCore"
    ontology_full_name = "Crystallographic Information Framework Core Dictionary (CIFCore)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "0.1.0"
    last_updated = "May 24, 2023"
    creator = None
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/emmo-repo/CIF-ontology?tab=readme-ov-file"


class CMSO(BaseOntology):
    """
    CMSO is an ontology that aims to describe computational materials science samples (or structures),
    including crystalline defects. Initially focusing on the description at the atomic scale.
    """
    ontology_id = "CMSO"
    ontology_full_name = "Computational Material Sample Ontology (CMSO)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "0.0.1"
    last_updated = None
    creator = "https://orcid.org/0000-0001-7564-7990"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://github.com/OCDO/cmso/tree/main"


class DISO(BaseOntology):
    """
    DISO is an ontology that defines the linear defect, in particular dislocation concepts
    and relations between them in crystalline materials.
    """
    ontology_id = "DISO"
    ontology_full_name = "Dislocation Ontology (DISO)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "1.0"
    last_updated = "21.03.202"
    creator = "Ahmad Zainul Ihsan"
    license = "Creative Commons Attribution 3.0 International (CC BY 3.0)"
    format = "OWL"
    download_url = "https://github.com/Materials-Data-Science-and-Informatics/dislocation-ontology"


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
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "1.0"
    last_updated = "17.08.2023"
    creator = "Ahmad Zainul Ihsan"
    license = "Creative Commons Attribution 3.0 Unported (CC BY 3.0)"
    format = "OWL"
    download_url = "https://github.com/OCDO/DSIM"


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
    domain = "Materials Science and Engineering"
    category = "Materials Modelling"
    version = "1.0.0-rc3"
    last_updated = "2024-03"
    creator = "European Materials Modelling Council (EMMC)"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://emmo-repo.github.io/"


class EMMOCrystallography(BaseOntology):
    """
    A crystallography domain ontology based on EMMO and the CIF core dictionary. It is implemented as a formal language.
    """
    ontology_id = "EMMOCrystallography"
    ontology_full_name = "Crystallography Ontology (EMMOCrystallography)"
    domain = "Materials Science and Engineering"
    category = "Crystallography"
    version = "0.0.1"
    last_updated = None
    creator = None
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/emmo-repo/domain-crystallography"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle EMMOCrystallography-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class FSO(BaseOntology):
    """
    The Flow Systems Ontology (FSO) is an ontology for describing interconnected systems
    with material or energy flow connections, and their components.
    """
    ontology_id = "FSO"
    ontology_full_name = "Flow Systems Ontology (FSO)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "0.1.0"
    last_updated = "2020-08-06"
    creator = "Ali Kücükavci, Mads Holten Rasmussen, Ville Kukkonen"
    license = "Creative Commons 4.0"
    format = "TTL"
    download_url = "https://github.com/alikucukavci/FSO/"


class GPO(BaseOntology):
    """
    Basically, this ontology aims to model processes. Processes are holistic perspective elements
    that transform inputs/educts (matter, energy, information) into output/products (matter, energy, information)
    with the help of tools (devices, algorithms). They can be decomposed into sub-processes
    and have predecessor and successor processes.
    """
    ontology_id = "GPO"
    ontology_full_name = "General Process Ontology (GPO)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = None
    last_updated = None
    creator = "Simon Stier"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/General-Process-Ontology/ontology"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle GPO-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True
        if re.match(r'^GPO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class HPOnt(BaseOntology):
    """
    The Heat Pump Ontology (HPOnt) aims to formalize and represent all the relevant information of Heat Pumps.
    The HPOnt has been developed as part of the REACT project which has received funding
    from the European Union’s Horizon 2020 research and innovation programme under grant agreement no. 824395.
    """
    ontology_id = "HPOnt"
    ontology_full_name = "The Heat Pump Ontology (HPOnt)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "0.2"
    last_updated = None
    creator = "REACT project team"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://react2020.github.io/REACT-ONTOLOGY/HPOnt/index-en.html/"


class LDO(BaseOntology):
    """
    LDO is an ontology designed to describe line defects in crystalline materials,
    such as dislocations and disclinations.
    """
    ontology_id = "LDO"
    ontology_full_name = "Line Defect Ontology (LDO)"
    domain = "Materials Science and Engineering"
    category = "Materials Defects"
    version = "1.0.0"
    last_updated = None
    creator = "https://orcid.org/0000-0001-7564-7990"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://github.com/OCDO/ldo"


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
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "1.1.9"
    last_updated = "2022-09-20"
    creator = "Fraunhofer IWM"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://matportal.org/ontologies/LPBFO"

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
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = None
    last_updated = None
    creator = None
    license = "General Public License v3.0 (GPL-3.0)"
    format = "OWL"
    download_url = "https://github.com/daimoners/MAMBO"


class MAT(BaseOntology):
    """
    The Material Properties Ontology aims to provide the vocabulary to describe the building components,
    materials, and their corresponding properties, relevant within the construction industry. More specifically,
    the building elements and properties covered in this ontology support applications
    focused on the design of building renovation projects.
    """
    ontology_id = "MAT"
    ontology_full_name = "Material Properties Ontology (MAT)"
    domain = "Materials Science and Engineering"
    category = "Materials Properties"
    version = "0.0.8"
    last_updated = None
    creator = "María Poveda-Villalón, Serge Chávez-Feria"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://bimerr.iot.linkeddata.es/def/material-properties/"


class MaterialInformation(BaseOntology):
    """
    The Material Information ontology is divided into smaller ontologies (partitions).
    The partitions are Environment, Geometry, Material Information, Manufacturing Process, Property,
    Substance, Unit Dimension, Structure, Equation and Physical Constant.
    """
    ontology_id = "MaterialInformation"
    ontology_full_name = "Material Information Ontology (MaterialInformation)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = None
    last_updated = None
    creator = "Toshihiro Ashino"
    license = None
    format = "OWL"
    download_url = "https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MaterialInformation.owl"


class MatOnto(BaseOntology):
    """
    The Material Ontology (MatOnto) is based on the upper level ontology, the BFO.
    """
    ontology_id = "MatOnto"
    ontology_full_name = "Material Ontology (MatOnto)"
    domain = "Materials Science and Engineering"
    category = "Scholarly Knowledge"
    version = None
    last_updated = None
    creator = None
    license = None
    format = "OWL"
    download_url = "https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MatOnto.owl"


class MatVoc(BaseOntology):
    """
    The official ontology produced in the context of the STREAM project.
    """
    ontology_id = "MatVoc"
    ontology_full_name = "Materials Vocabulary (MatVoc)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "1.0.0"
    last_updated = "2022-12-12"
    creator = "Tatyana Sheveleva, Javad Chamanara"
    license = "MIT License"
    format = "RDF"
    download_url = "https://stream-project.github.io/#overv"


class MatWerk(BaseOntology):
    """
    NFDI-MatWerk aims to establish a digital infrastructure for Materials Science and Engineering (MSE),
    fostering improved data sharing and collaboration. This repository provides comprehensive documentation
    for NFDI MatWerk Ontology (MWO) v3.0, a foundational framework designed to structure research data
    and enhance interoperability within the MSE community. To ensure compliance with top-level ontology standards,
    MWO v3.0 is aligned with the Basic Formal Ontology (BFO) and incorporates the modular approach
    of the NFDIcore mid-level ontology, enriching metadata through standardized classes and properties.
    The MWO addresses key aspects of MSE research data, including the NFDI-MatWerk community structure,
    covering task areas, infrastructure use cases, projects, researchers, and organizations.
    It also describes essential NFDI resources, such as software, workflows, ontologies, publications,
    datasets, metadata schemas, instruments, facilities, and educational materials. Additionally,
    MWO represents NFDI-MatWerk services, academic events, courses, and international collaborations.
    As the foundation for the MSE Knowledge Graph, MWO facilitates efficient data integration and retrieval,
    promoting collaboration and knowledge representation across MSE domains. This digital transformation
    enhances data discoverability, reusability, and accelerates scientific exchange, innovation,
    and discoveries by optimizing research data management and accessibility.
    """
    ontology_id = "MatWerk"
    ontology_full_name = "NFDI MatWerk Ontology (MatWerk)"
    domain = "Materials Science and Engineering"
    category = "Research Data, Interoperability"
    version = "3.0.0"
    last_updated = "2025-03-01"
    creator = "Hossein Beygi Nasrabadi, Jörg Waitelonis, Ebrahim Norouzi, Kostiantyn Hubaiev, Harald Sack"
    license = "Creative Commons 1.0"
    format = "TTL"
    download_url = "https://github.com/ISE-FIZKarlsruhe/mwo?tab=readme-ov-file"


class MDO(BaseOntology):
    """
    MDO is an ontology for materials design field, representing the domain knowledge specifically related
    to solid-state physics and computational materials science.
    """
    ontology_id = "MDO"
    ontology_full_name = "Materials Design Ontology (MDO)"
    domain = "Materials Science and Engineering"
    category = "Materials Design"
    version = "1.1"
    last_updated = "2022-08-02"
    creator = "Materials Design Division, National Institute for Materials Science (NIMS)"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://github.com/LiUSemWeb/Materials-Design-Ontology/tree/master/"


class MDS(BaseOntology):
    """
    Materials Data Science (MDS) is an ontology encompassing multiple domains relevant to materials science,
    chemical synthesis and characterizations, photovoltaics and geospatial datasets. The terms used for classes,
    subclasses and instances are mapped to PMDCo and BFO Ontologies.
    """
    ontology_id = "MDS"
    ontology_full_name = "Materials Data Science Ontology (MDS)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "0.3.0.0"
    last_updated = "03/24/2024"
    creator = "SDLE Research Center"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://matportal.org/ontologies/MDS"


class MechanicalTesting(BaseOntology):
    """
    A domain ontology for mechanical testing based on EMMO.
    """
    ontology_id = "MechanicalTesting"
    ontology_full_name = "Mechanical Testing Ontology (MechanicalTesting)"
    domain = "Materials Science and Engineering"
    category = "Mechanical Testing"
    version = "1.0.0"
    last_updated = None
    creator = "Fraunhofer IWM"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://github.com/emmo-repo/domain-mechanical-testing"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle MechanicalTesting-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class MicroStructures(BaseOntology):
    """
    This is intended to be a domain ontology for metallic microstructures, covering aspects like: composition,
    particles, both stable (primary) and metastable (precipitates), grains, subgrains,
    grain boundaries & particle free zones (PFZs), texture, dislocations. The aim is to support
    both microstructure modelling as well as characterisation.
    """
    ontology_id = "MicroStructures"
    ontology_full_name = "EMMO-based ontology for microstructures (MicroStructures)"
    domain = "Materials Science and Engineering"
    category = "Microstructure"
    version = None
    last_updated = None
    creator = None
    license = None
    format = "OWL"
    download_url = "https://github.com/jesper-friis/emmo-microstructure"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle MicroStructures-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


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
    domain = "Materials Science and Engineering"
    category = "Scholarly Knowledge"
    version = "1.0.1"
    last_updated = "2024-01-30"
    creator = "Akhil Thomas, Ali Riza Durmaz"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://iwm-micro-mechanics-public.pages.fraunhofer.de/ontologies/materials-mechanics-ontology/index-en.html"


class MOLBRINELL(BaseOntology):
    """
    An ontology for describing the Brinell hardness testing process, made in the Materials Open Lab Project.
    """
    ontology_id = "MOLBRINELL"
    ontology_full_name = "MatoLab Brinell Test Ontology (MOL_BRINELL)"
    domain = "Materials Science and Engineering"
    category = "Materials Testing"
    version = "0.1"
    last_updated = "05/05/2022"
    creator = "Birgit Skrotzki, Hossein Beygi Nasrabadi, Philipp von Hartrott, Vinicius Carrillo Beber, Yue Chen"
    license = None
    format = "TTL"
    download_url = "https://matportal.org/ontologies/MOL_BRINELL"


class MOLTENSILE(BaseOntology):
    """
    An ontology for describing the tensile test process, made in the Materials Open Lab Project.
    """
    ontology_id = "MOLTENSILE"
    ontology_full_name = "Matolab Tensile Test Ontology (MOL_TENSILE)"
    domain = "Materials Science and Engineering"
    category = "Materials Testings"
    version = "0.4"
    last_updated = "04/16/2021"
    creator = "Markus Schilling, markus.schilling@bam.de; Philipp von Hartrott, philipp.von.hartrott@iwm.fraunhofer.de"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "RDF"
    download_url = "https://matportal.org/ontologies/MOL_TENSILE"


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
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = None
    last_updated = None
    creator = "Thomas Hanke, Fraunhofer IWM"
    license = "MIT License"
    format = "TTL"
    download_url = "https://github.com/Mat-O-Lab/MSEO"


class MSLE(BaseOntology):
    """
    The current ontology describes Material Science Lab Equipment.
    """
    ontology_id = "MSLE"
    ontology_full_name = "Material Science Lab Equipment Ontology (MSLE)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "1.1"
    last_updated = "Sep 15, 2022"
    creator = None
    license = None
    format = "TTL"
    download_url = "https://github.com/MehrdadJalali-AI/MSLE-Ontology"


class NanoMine(BaseOntology):
    """
    Polymer Nanocomposites based ontology which enable researchers to develop and test
    broad-reaching hypotheses about how inter-relationships between different materials
    processing methods and composition result in specific changes in material properties.
    """
    ontology_id = "NanoMine"
    ontology_full_name = "NanoMine Ontology (NanoMine)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = None
    last_updated = None
    creator = None
    license = "APACHE 2.0"
    format = "TTL"
    download_url = "https://github.com/tetherless-world/nanomine-ontology"


class OIECharacterisation(BaseOntology):
    """
    EMMO-compliant, domain-level OIE ontology tackling the areas of characterization methods.
    """
    ontology_id = "OIECharacterisation"
    ontology_full_name = "Open Innovation Environment Characterisation (OIECharacterisation)"
    domain = "Materials Science and Engineering"
    category = "Materials"
    version = None
    last_updated = None
    creator = "Daniele Toti, Gerhard Goldbeck, Pierluigi Del Nostro"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/emmo-repo/OIE-Ontologies/"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle OIECharacterisation-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class OIEManufacturing(BaseOntology):
    """
    The manufacturing module populates the physicalistic perspective with manufacturing subclasses categorised
    according to modern applied physical sciences.
    """
    ontology_id = "OIEManufacturing"
    ontology_full_name = "Open Innovation Environment Manufacturing (OIEManufacturing)"
    domain = "Materials Science and Engineering"
    category = "Materials"
    version = None
    last_updated = None
    creator = ("Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, Gerhard Goldbeck, "
               "Jesper Friis, Pierluigi Del Nostro")
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/emmo-repo/OIE-Ontologies/"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle OIEManufacturing-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class OIEMaterials(BaseOntology):
    """
    The materials module populates the physicalistic perspective with materials subclasses categorised
    according to modern applied physical sciences.
    """
    ontology_id = "OIEMaterials"
    ontology_full_name = "Open Innovation Environment Materials (OIEMaterials)"
    domain = "Materials Science and Engineering"
    category = "Materials"
    version = None
    last_updated = None
    creator = ("Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, "
               "Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro")
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/emmo-repo/OIE-Ontologies/"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle OIEMaterials-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class OIEModels(BaseOntology):
    """
    The models module defines models as semiotic signs that stands for an object by resembling or imitating it,
    in shape or by sharing a similar logical structure.
    """
    ontology_id = "OIEModels"
    ontology_full_name = "Open Innovation Environment Models (OIEModels)"
    domain = "Materials Science and Engineering"
    category = "Materials"
    version = None
    last_updated = None
    creator = ("Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, "
               "Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro")
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/emmo-repo/OIE-Ontologies/"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle OIEModels-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class OIESoftware(BaseOntology):
    """
    EMMO-compliant, domain-level OIE ontology tackling the areas of software products.
    """
    ontology_id = "OIESoftware"
    ontology_full_name = "Open Innovation Environment Software (OIESoftware)"
    domain = "Materials Science and Engineering"
    category = "Materials"
    version = "0.1"
    last_updated = None
    creator = ("Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, "
               "Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro")
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/emmo-repo/OIE-Ontologies/"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle OIESoftware-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


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
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = None
    last_updated = "2010-05-31"
    creator = "Diego Daz"
    license = "N/A"
    format = "TTL"
    download_url = "https://raw.githubusercontent.com/ISE-FIZKarlsruhe/mseo.github.io/master/Ontology_files/ONTORULEsteel.ttl"


class PeriodicTable(BaseOntology):
    """
    PeriodicTable.owl is a representation of the Periodic Table of the Elements in the OWL Web Ontology Language.
    It provides reference data to support Semantic Web applications in chemistry and related disciplines.
    """
    ontology_id = "PeriodicTable"
    ontology_full_name = "Periodic Table of the Elements Ontology (PeriodicTable)"
    domain = "Materials Science and Engineering"
    category = "Periodic Table of Elements"
    version = "1.10"
    last_updated = "2004/02/05"
    creator = "Michael Cook"
    license = None
    format = "OWL"
    download_url = "https://www.daml.org/2003/01/periodictable/"


class Photovoltaics(BaseOntology):
    """
    This ontology is describing Perovskite solar cells.
    """
    ontology_id = "Photovoltaics"
    ontology_full_name = "EMMO Domain Ontology for Photovoltaics (Photovoltaics)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "0.0.1"
    last_updated = None
    creator = "Casper Welzel Andersen, Simon Clark"
    license = "Creative Commons license Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/emmo-repo/domain-photovoltaics"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle Photovoltaics-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False

class PLDO(BaseOntology):
    """
    PLDO is an ontology designed to describe planar defects in crystalline materials,
    such as grain boundaries and stacking faults, with a focus on their atomic-scale structure and properties.
    """
    ontology_id = "PLDO"
    ontology_full_name = "Planar Defects Ontology (PLDO)"
    domain = "Materials Science and Engineering"
    category = "Materials Defects"
    version = "1.0.0"
    last_updated = None
    creator = "https://orcid.org/0000-0001-7564-7990"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://github.com/OCDO/pldo"


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
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "3.0.0-alpha1"
    last_updated = "2025-03-20"
    creator = "Jannis Grundmann"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://github.com/materialdigital/core-ontology?tab=readme-ov-file"


class PODO(BaseOntology):
    """
    PODO focuses on the description of point defects in crystalline materials.
    """
    ontology_id = "PODO"
    ontology_full_name = "Point Defects Ontology (PODO)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "1.0.0"
    last_updated = None
    creator = "https://orcid.org/0000-0001-7564-7990"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://github.com/OCDO/podo"


class PRIMA(BaseOntology):
    """
    An ontology that captures the provenance information in the materials science domain.
    """
    ontology_id = "PRIMA"
    ontology_full_name = "PRovenance Information in MAterials science (PRIMA)"
    domain = "Materials Science and Engineering"
    category = "Materials Science"
    version = "2.0"
    last_updated = "2024-01-29"
    creator = "Ahmad Zainul Ihsan, Mehrdad Jalali, Rossella Aversa"
    license = "Creative Commons Attribution 3.0 Unported (CC BY 3.0)"
    format = "TTL"
    download_url = "https://materials-data-science-and-informatics.github.io/MDMC-NEP-top-level-ontology/PRIMA/complete/ver_2_0/index.html"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


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
    domain = "Materials Science and Engineering"
    category = "Sensor Networks"
    version = "1.0"
    last_updated = "2017-04-17"
    creator = "W3C/OGC Spatial Data on the Web Working Group"
    license = "http://www.w3.org/Consortium/Legal/2015/copyright-software-and-document"
    format = "TTL"
    download_url = "https://github.com/w3c/sdw-sosa-ssn/tree/482484fe2edc1ba8aa7f19214a72bdb77123e833"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class SystemCapabilities(BaseOntology):
    """
    This ontology describes system capabilities, operating ranges, and survival ranges.
    """
    ontology_id = "SystemCapabilities"
    ontology_full_name = "System Capabilities Ontology (SystemCapabilities)"
    domain = "Materials Science and Engineering"
    category = "Materials Science, Engineering, Systems"
    version = None
    last_updated = "2017-05-14"
    creator = "W3C/OGC Spatial Data on the Web Working Group"
    license = "W3C Software and Document License"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/SSNSYSTEM"


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
    ontology_full_name = "Virtual Materials Marketplace Ontologies (VIMMP)"
    domain = "Materials Science and Engineering"
    category = "Materials Modeling"
    version = None
    last_updated = "2021-01-02"
    creator = "Ilian T. Todorov, Martin Thomas Horsch, Michael A. Seaton, Silvia Chiacchiera"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "OWL"
    download_url = "https://matportal.org/ontologies/VIMMP_ONTOLOGIES"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle VIMMP-specific blank nodes."""
        # UUID pattern for various prefixes
        uuid_pattern = r'[0-9a-f]{8}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{4}_[0-9a-f]{12}$'

        if re.match(r'^EMMO_' + uuid_pattern, label):
            return True

        if re.match(r'^SWO_[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False
