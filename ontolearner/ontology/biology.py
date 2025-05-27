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

from ..base import BaseOntology


class BioPAX(BaseOntology):
    """
    BioPAX is a standard language that aims to enable integration, exchange, visualization and analysis
    of biological pathway data. Specifically, BioPAX supports data exchange between pathway data
    groups and thus reduces the complexity of interchange between data formats by providing an
    accepted standard format for pathway data.
    """
    ontology_id = "BioPAX"
    ontology_full_name = "Biological Pathways Exchange (BioPAX)"
    domain = "Biology and Life Sciences"
    category = "Bioinformatics"
    version = "1.0"
    last_updated = "16 April 2015"
    creator = None
    license = None
    format = "OWL"
    download_url = "http://www.biopax.org/"


class EFO(BaseOntology):
    """
    The Experimental Factor Ontology (EFO) provides a systematic description of many experimental variables
    available in EBI databases, and for projects such as the GWAS catalog. It combines parts of several biological ontologies,
    such as UBERON anatomy, ChEBI chemical compounds, and Cell Ontology. The scope of EFO is to support the annotation,
    analysis and visualization of data handled by many groups at the EBI and as the core ontology for Open Targets.
    EFO is developed by the EMBL-EBI Samples, Phenotypes and Ontologies Team (SPOT).
    """
    ontology_id = "EFO"
    ontology_full_name = "Experimental Factor Ontology (EFO)"
    domain = "Biology and Life Sciences"
    category = "Biology"
    version = "3.75.0"
    last_updated = "2025-02-17"
    creator = None
    license = "Apache 2.0"
    format = "OWL"
    download_url = "https://www.ebi.ac.uk/efo"


class GO(BaseOntology):
    """
    The Gene Ontology (GO) Provides structured controlled vocabularies for the annotation of gene products
    with respect to their molecular function, cellular component, and biological role.
    """
    ontology_id = "GO"
    ontology_full_name = "Gene Ontology (GO)"
    domain = "Biology and Life Sciences"
    category = "Molecular Biology, Genetics"
    version = None
    last_updated = "2024-11-03"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://geneontology.org/docs/download-ontology/"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle GO-specific blank nodes."""
        # Check the general patterns from the parent class
        # GO-specific patterns
        if label.startswith('GO_'):
            return True

        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class LIFO(BaseOntology):
    """
    The Life Ontology (LifO) is an ontology of the life of organism. LifO represents the
    life processes of organisms and related entities and relations. LifO is a general
    purpose ontology that covers the common features associated with different
    organisms such as unicellular prokaryotes (e.g., E. coli) and multicellular organisms (e.g., human).
    """
    ontology_id = "LIFO"
    ontology_full_name = "Life Ontology (LifO)"
    domain = "Biology and Life Sciences"
    category = "General Purpose"
    version = "1.0.17"
    last_updated = "March 11, 2018"
    creator = "Yongqun \"Oliver\" He (YH)"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://bioportal.bioontology.org/ontologies/LIFO"


class MarineTLO(BaseOntology):
    """
    MarineTLO is a top level ontology, generic enough to provide consistent abstractions or
    specifications of concepts included in all data models or ontologies of marine data sources and
    provide the necessary properties to make this distributed knowledge base a coherent source of
    facts relating observational data with the respective spatiotemporal context and categorical
    (systematic) domain knowledge. It can be used as the core schema for publishing Linked Data, as
    well as for setting up integration systems for the marine domain. It can be extended to any level
    of detail on demand, while preserving monotonicity. For its development and evolution we have
    adopted an iterative and incremental methodology where a new version is released every two
    months. For the implementation we use OWL 2, and to evaluate it we use a set of competency
    queries, formulating the domain requirements provided by the related communities.
    """
    ontology_id = "MarineTLO"
    ontology_full_name = "Marine Taxonomy and Life Ontology (MarineTLO)"
    domain = "Biology and Life Sciences"
    category = "Marine Science, Oceanography"
    version = "1.0"
    last_updated = "2017-01-05"
    creator = "Information System Laboratory (ISL), Institute of Computer Science (ICS), Foundation for Research and Technology - Hellas (FORTH)"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://projects.ics.forth.gr/isl/MarineTLO/"


class MGED(BaseOntology):
    """
    An ontology for microarray experiments in support of MAGE v.1. Concepts, definitions, terms,
    and resources for standardized description of a microarray experiment in support of MAGE v.1.
    The MGED ontology is divided into the MGED Core ontology which is intended to be stable and
    in synch with MAGE v.1; and the MGED Extended ontology which adds further associations
    and classes not found in MAGE v.1
    """
    ontology_id = "MGED"
    ontology_full_name = "MGED Ontology (MGED)"
    domain = "Biology and Life Sciences"
    category = "Domain Ontology"
    version = "1.3.1.1"
    last_updated = "Feb. 9, 2007"
    creator = "Chris Stoeckert, Helen Parkinson, Trish Whetzel, Paul Spellman, Catherine A. Ball, Joseph White, John Matese, Liju Fan, Gilberto Fragoso, Mervi Heiskanen, Susanna Sansone, Helen Causton, Laurence Game, Chris Taylor"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://mged.sourceforge.net/ontologies/MGEDontology.php/"


class MO(BaseOntology):
    """
    The Microscopy Ontology (MO) extends the ontological framework of the PMDco. The MO facilitates semantic integration
    and the interoperable connection of diverse data sources from the fields of microscopy and microanalysis. Consequently,
    the MO paves the way for new, adaptable data applications and analyses across various experiments and studies
    """
    ontology_id = "MO"
    ontology_full_name = "Microscopy Ontology (MO)"
    domain = "Biology and Life Sciences"
    category = "Microscopy"
    version = "2.0"
    last_updated = None
    creator = "https://orcid.org/0000-0002-3717-7104,https://orcid.org/0000-0002-7094-5371"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "TTL"
    download_url = "https://github.com/materialdigital/microscopy-ontology?tab=readme-ov-file"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class NPO(BaseOntology):
    """
    NanoParticle Ontology (NPO) is developed within the framework of the Basic Formal Ontology (BFO),
    and implemented in the Ontology Web Language (OWL) using well-defined ontology design principles.
    The NPO was developed to represent knowledge underlying the preparation, chemical composition,
    and characterization of nanomaterials involved in cancer research. Public releases of the NPO
    are available through BioPortal website, maintained by the National Center for Biomedical Ontology.
    Mechanisms for editorial and governance processes are being developed for the maintenance,
    review, and growth of the NPO.
    """
    ontology_id = "NPO"
    ontology_full_name = "NanoParticle Ontology (NPO)"
    domain = "Biology and Life Sciences"
    category = "Materials Science"
    version = "2013-05-31"
    last_updated = "2013-05-31"
    creator = "Dennis G. Thomas"
    license = "BSD-3-Clause license"
    format = "OWL"
    download_url = "https://github.com/sobolevnrm/npo?tab=readme-ov-file"


class PATO(BaseOntology):
    """
    An ontology of phenotypic qualities (properties, attributes or characteristics).
    """
    ontology_id = "PATO"
    ontology_full_name = "Phenotype and Trait Ontology (PATO)"
    domain = "Biology and Life Sciences"
    category = "Biology"
    version = "1.2"
    last_updated = "2025-02-01"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/PATO"
