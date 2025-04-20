from ..base import BaseOntology


class ENVO(BaseOntology):
    """
    ENVO is an expressive, community ontology which helps humans, machines,
    and semantic web applications understand environmental entities of all kinds,
    from microscopic to intergalactic scales. As a FAIR-compliant resource, it promotes interoperability
    through the concise, controlled description of all things environmental.
    """
    ontology_id = "ENVO"
    ontology_full_name = "Environment Ontology (ENVO)"
    domain = "Ecology & Environment"
    category = "Environment, Ecosystems, Habitats"
    version = "2024-07-01"
    last_updated = "2024-07-01"
    creator = "Pier Luigi Buttigieg (https://orcid.org/0000-0002-4366-3088)"
    license = "Creative Commons 1.0"
    format = "OWL, OBO, JSON"
    download_url = "https://obofoundry.org/ontology/envo.html"


class OEO(BaseOntology):
    """
    The Open Energy Ontology (OEO) is a domain ontology of the energy system analysis context.
    It is developed as part of the Open Energy Family. The OEO is published on GitHub under
    an open source license. The language used is the Manchester OWL Syntax, which was chosen
    because it is user-friendly for editing and viewing differences of edited files. The OEO is constantly
    being extended. The first version of the OEO has been released on June 11th 2020. A Steering Committee (OEO-SC)
    was created to accompany the development, increase awareness of the ontology and include it in current projects.
    """
    ontology_id = "OEO"
    ontology_full_name = "The Open Energy Ontology (OEO)"
    domain = "Ecology & Environment"
    category = "Energy"
    version = "2.7.0"
    last_updated = "03/2025"
    creator = None
    license = "Creative Commons Attribution 1.0 Generic (CC BY 1.0)"
    format = "OWL/XML"
    download_url = "https://github.com/OpenEnergyPlatform/ontology?tab=readme-ov-file"


class SWEET(BaseOntology):
    """
    The Semantic Web for Earth and Environment Technology Ontology (SWEET) is an investigation in improving discovery
    and use of Earth science data, through software understanding of the semantics of web resources.
    SWEET is a collection of ontologies conceptualizing a knowledge space for Earth system science,
    represented using the web ontology language (OWL). It includes both orthogonal concepts (space, time,
    Earth realms, physical quantities, etc.) and integrative science knowledge concepts (phenomena, events, etc.).
    """
    ontology_id = "SWEET"
    ontology_full_name = "Semantic Web for Earth and Environment Technology Ontology (SWEET)"
    domain = "Ecology & Environment"
    category = "Earth Science, Geoscience"
    version = "3.6.0"
    last_updated = "July 14, 2022"
    creator = "NASA, JPL, Caltech"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://bioportal.bioontology.org/ontologies/SWEET"
