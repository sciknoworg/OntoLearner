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

from ..base.ontology import BaseOntology


class AgrO(BaseOntology):
    """
    An ontology is a formal representation of a disciplinary domain, representing a semantic standard
    that can be employed to annotate data where key concepts are defined, as well as the relationships
    that exist between those concepts (Gruber, 2009). Ontologies provide a common language for different kinds of data
    to be easily interpretable and interoperable allowing easier aggregation and analysis. The Agronomy Ontology (AgrO)
    provides terms from the agronomy domain that are semantically organized and can facilitate the collection,
    storage and use of agronomic data, enabling easy interpretation and reuse of the data by humans and machines alike.
    To fully understand the implications of varying practices within cropping systems and derive insights,
    it is often necessary to pull together information from data in different disciplinary domains.
    For example, data on field management, soil, weather and crop phenotypes may need to be aggregated
    to assess performance of particular crop under different management interventions. However,
    agronomic data are often collected, described, and stored in inconsistent ways, impeding data comparison, mining,
    interpretation reuse. The use of standards for metadata and data annotation play a key role
    in addressing these challenges. While the CG Core Metadata Schema provides a metadata standard
    to describe agricultural datasets, the Agronomy Ontology enables the description
    of agronomic data variables using standard terms.
    """
    ontology_id = "AgrO"
    ontology_full_name = "Agronomy Ontology (AgrO)"
    domain = "Agriculture"
    category = "Agronomy"
    version = "1.0"
    last_updated = "2022-11-02"
    creator = "The Crop Ontology Consortium"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://agroportal.lirmm.fr/ontologies/AGRO?p=summary"


class AGROVOC(BaseOntology):
    """
    AGROVOC is a relevant Linked Open Data set about agriculture available for public use and facilitates
    access and visibility of data across domains and languages. It offers a structured collection of agricultural concepts,
    terms, definitions and relationships which are used to unambiguously identify resources, allowing standardized
    indexing processes and making searches more efficient.
    """
    ontology_id = "AGROVOC"
    ontology_full_name = "AGROVOC Multilingual Thesaurus (AGROVOC)"
    domain = "Agriculture"
    category = "Agricultural Knowledge"
    version = "2024-04"
    last_updated = "August 12, 2024"
    creator = "Food and Agriculture Organization of the United Nations"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://agroportal.lirmm.fr/ontologies/AGROVOC"


class ATOL(BaseOntology):
    """
    ATOL (Animal Trait Ontology for Livestock) is an ontology of characteristics defining phenotypes of livestock
    in their environment (EOL). ATOL aims to:
    - provide a reference ontology of phenotypic traits of farm animals for the international scientific and educational
    - communities, farmers, etc.;
    - deliver this reference ontology in a language which can be used by computers in order to support database management,
    semantic analysis and modeling;
    - represent traits as generic as possible for livestock vertebrates;
    - make the ATOL ontology as operational as possible and closely related to measurement techniques;
    - structure the ontology in relation to animal production.
    """
    ontology_id = "ATOL"
    ontology_full_name = "Animal Trait Ontology for Livestock (ATOL)"
    domain = "Agriculture"
    category = "Animal Science"
    version = "6.0"
    last_updated = "May 11, 2020"
    creator = "INRAE, France"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://bioportal.bioontology.org/ontologies/ATOL"


class FoodOn(BaseOntology):
    """
    FoodOn, the food ontology, contains vocabulary for naming food materials and their anatomical and taxonomic origins,
    from raw harvested food to processed food products, for humans and domesticated animals.
    It provides a neutral and ontology-driven standard for government agencies,
    industry, nonprofits and consumers to name and reference food products and their components
    throughout the food supply chain.
    """
    ontology_id = "FoodOn"
    ontology_full_name = "Food Ontology (FoodON)"
    domain = "Agriculture"
    category = "Diet, Metabolomics, and Nutrition"
    version = None
    last_updated = "2025-01-16"
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "http://purl.obolibrary.org/obo/foodon.owl"


class PO(BaseOntology):
    """
    The Plant Ontology (PO) is a structured vocabulary and database resource that links plant anatomy,
    morphology and growth and development to plant genomics data.
    """
    ontology_id = "PO"
    ontology_full_name = "Plant Ontology (PO)"
    domain = "Agriculture"
    category = "Plant Anatomy, Morphology, Growth and Development"
    version = None
    last_updated = None
    creator = None
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://github.com/Planteome/plant-ontology"
