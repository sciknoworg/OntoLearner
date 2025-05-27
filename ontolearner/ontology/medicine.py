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


class BTO(BaseOntology):
    """
    A structured controlled vocabulary for the source of an enzyme comprising tissues,
    cell lines, cell types and cell cultures.
    """
    ontology_id = "BTO"
    ontology_full_name = "BRENDA Tissue Ontology (BTO)"
    domain = "Medicine"
    category = "Enzyme"
    version = "2021-10-26"
    last_updated = "2021-10-26"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/BTO"

    @staticmethod
    def _is_anonymous_id(label: str) -> bool:
        """Override to handle VIMMP-specific blank nodes."""
        if re.match(r'^BTO_[0-9]+$', label):
            return True

        # Check the general patterns from the parent class
        if BaseOntology._is_anonymous_id(label):
            return True

        return False


class DEB(BaseOntology):
    """
    The devices, experimental scaffolds, and biomaterials ontology (DEB) is an open resource
    for organizing information about biomaterials, their design, manufacture, and biological testing.
    It was developed using text analysis for identifying ontology terms from a biomaterials gold standard corpus,
    systematically curated to represent the domain's lexicon. Topics covered were validated by members
    of the biomaterials research community.
    """
    ontology_id = "DEB"
    ontology_full_name = "Devices, Experimental scaffolds and Biomaterials Ontology (DEB)"
    domain = "Medicine"
    category = "Biomaterials"
    version = "06/2021"
    last_updated = "Jun 2, 2021"
    creator = "Osnat Hakimi"
    license = "GPL-3.0"
    format = "OWL"
    download_url = "https://github.com/ProjectDebbie/Ontology_DEB"


class DOID(BaseOntology):
    """
    The Disease Ontology has been developed as a standardized ontology for human disease
    with the purpose of providing the biomedical community with consistent,
    reusable and sustainable descriptions of human disease terms,
    phenotype characteristics and related medical vocabulary disease concepts.
    """
    ontology_id = "DOID"
    ontology_full_name = "Human Disease Ontology (DOID)"
    domain = "Medicine"
    category = "Human Diseases"
    version = None
    last_updated = "2024-12-18"
    creator = "The Open Biological and Biomedical Ontology Foundry"
    license = "Creative Commons 1.0"
    format = "OWL"
    download_url = "http://purl.obolibrary.org/obo/doid/releases/2024-12-18/doid.owl"


class ENM(BaseOntology):
    """
    The eNanoMapper project (https://www.enanomapper.net/), NanoCommons project (https://www.nanocommons.eu/)
    and ACEnano project (http://acenano-project.eu/) are creating a pan-European computational infrastructure
    for toxicological data management for ENMs, based on semantic web standards and ontologies.
    This ontology is an application ontology targeting the full domain of nanomaterial safety assessment.
    It re-uses several other ontologies including the NPO, CHEMINF, ChEBI, and ENVO.
    """
    ontology_id = "ENM"
    ontology_full_name = "Environmental Noise Measurement Ontology (ENM)"
    domain = "Medicine"
    category = "Material Science and Engineering"
    version = "10.0"
    last_updated = "2025-02-17"
    creator = "eNanoMapper Consortium"
    license = "Creative Commons 3.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/ENM"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class MFOEM(BaseOntology):
    """
    The Mental Functioning Ontology - Emotion Module (MFOEM) aims to include all relevant aspects of affective phenomena
    including their bearers, the different types of emotions, moods, etc., their different parts and dimensions
    of variation, their facial and vocal expressions, and the role of emotions and affective phenomena
    in general in influencing human behavior.This class processes Mental Functioning Ontology of Emotions (MFOEM)
    using default behavior.
    """
    ontology_id = "MFOEM"
    ontology_full_name = "Mental Functioning Ontology of Emotions - Emotion Module (MFOEM)"
    domain = "Medicine"
    category = "Emotion"
    version = None
    last_updated = None
    creator = "Swiss Centre for Affective Sciences & University at Buffalo"
    license = "Creative Commons 3.0"
    format = "OWL"
    download_url = "http://purl.obolibrary.org/obo/MFOEM.owl"


class NCIt(BaseOntology):
    """
    NCI Thesaurus (NCIt) is a reference terminology that includes broad coverage of the cancer domain,
    including cancer related diseases, findings and abnormalities. The NCIt OBO Edition aims to increase integration
    of the NCIt with OBO Library ontologies. NCIt OBO Edition releases should be considered experimental.
    """
    ontology_id = "NCIt"
    ontology_full_name = "NCI Thesaurus (NCIt)"
    domain = "Medicine"
    category = "Cancer, Oncology"
    version = "24.04e"
    last_updated = "2023-10-19"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://terminology.tib.eu/ts/ontologies/NCIT"


class OBI(BaseOntology):
    """
    The Ontology for Biomedical Investigations (OBI) helps you communicate clearly about scientific investigations
    by defining more than 2500 terms for assays, devices, objectives, and more.
    """
    ontology_id = "OBI"
    ontology_full_name = "Ontology for Biomedical Investigations (OBI)"
    domain = "Medicine"
    category = "Biomedical Investigations"
    version = None
    last_updated = "2025-01-09"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://github.com/obi-ontology/obi/tree/master"


class PRotein(BaseOntology):
    """
    The PRotein Ontology (PRO) formally defines taxon-specific and taxon-neutral protein-related entities
    in three major areas: proteins related by evolution; proteins produced from a given gene;
    and protein-containing complexes.
    """
    ontology_id = "PRotein"
    ontology_full_name = "Protein Ontology (PRO)"
    domain = "Medicine"
    category = "Protein"
    version = "1.2"
    last_updated = "08:08:2024"
    creator = None
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "http://purl.obolibrary.org/obo/pr.owl"
