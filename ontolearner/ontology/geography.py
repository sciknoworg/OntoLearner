from ..base import BaseOntology


class GeoNames(BaseOntology):
    """
    The Geonames ontologies provides elements of description for geographical features,
    in particular those defined in the geonames.org database.

    This class processes Geonames Ontology using default behavior.
    """
    ontology_full_name = "Geonames Ontology"


class GEO(BaseOntology):
    """
    Geographical Entities Ontology (GEO) is an inventory of geopolitical entities (such as sovereign states
    and their administrative subdivisions) as well as various geographical regions (including but not limited
    to the specific ones over which the governments have jurisdiction)

    This class processes Geographical Entities Ontology (GEO) using default behavior.
    """
    ontology_full_name = "Geographical Entities Ontology (GEO)"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class GTS(BaseOntology):
    """
    This is an RDF/OWL representation of the GeoSciML Geologic Timescale model, which has been adapted
    from the model described in Cox, S.J.D, & Richard, S.M. (2005) A formal model for the geologic timescale and GSSP,
    compatible with geospatial information transfer standards, Geosphere, Geological Society of America.

    This class processes Geologic Timescale model (GTS) using default behavior.
    """
    ontology_full_name = "Geologic Timescale model (GTS)"


class Juso(BaseOntology):
    """
    Juso Ontology is a Web vocabulary for describing geographical addresses and features.

    This class processes Juso Ontology using default behavior.
    """
    ontology_full_name = "Juso Ontology"
