from ..base.ontology import BaseOntology


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
    domain = "Livestock"
    category = "Animal Science"
    version = "6.0"
    last_updated = "May 11, 2020"
    creator = "INRAE, France"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://bioportal.bioontology.org/ontologies/ATOL"
