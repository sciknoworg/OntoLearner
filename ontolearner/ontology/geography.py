from ..base import BaseOntology


class GeoNames(BaseOntology):
    """
    The Geonames ontologies provides elements of description for geographical features,
    in particular those defined in the geonames.org database.
    """
    ontology_id = "GeoNames"
    ontology_full_name = "GeoNames Ontology (GeoNames)"


class GEO(BaseOntology):
    """
    Geographical Entities Ontology (GEO) is an inventory of geopolitical entities (such as sovereign states
    and their administrative subdivisions) as well as various geographical regions (including but not limited
    to the specific ones over which the governments have jurisdiction)
    """
    ontology_id = "GEO"
    ontology_full_name = "Geographical Entities Ontology (GEO)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class GTS(BaseOntology):
    """
    This is an RDF/OWL representation of the GeoSciML Geologic Timescale model, which has been adapted
    from the model described in Cox, S.J.D, & Richard, S.M. (2005) A formal model for the geologic timescale and GSSP,
    compatible with geospatial information transfer standards, Geosphere, Geological Society of America.
    """
    ontology_id = "GTS"
    ontology_full_name = "Geologic Timescale model (GTS)"


class Juso(BaseOntology):
    """
    Juso Ontology is a Web vocabulary for describing geographical addresses and features.
    """
    ontology_id = "Juso"
    ontology_full_name = "Juso Ontology"
