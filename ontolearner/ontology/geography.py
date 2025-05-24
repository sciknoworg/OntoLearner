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


class GEO(BaseOntology):
    """
    Geographical Entities Ontology (GEO) is an inventory of geopolitical entities (such as sovereign states
    and their administrative subdivisions) as well as various geographical regions (including but not limited
    to the specific ones over which the governments have jurisdiction)
    """
    ontology_id = "GEO"
    ontology_full_name = "Geographical Entities Ontology (GEO)"
    domain = "Geography"
    category = "Geographic Knowledge"
    version = None
    last_updated = "2019-02-17"
    creator = "William R Hogan"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://github.com/mcwdsi/geographical-entity-ontology/blob/master/geo-all.owl"

    def contains_imports(self) -> bool:
        """Hook: Check if the ontology contains imports."""
        return True


class GeoNames(BaseOntology):
    """
    The Geonames ontologies provides elements of description for geographical features,
    in particular those defined in the geonames.org database.
    """
    ontology_id = "GeoNames"
    ontology_full_name = "GeoNames Ontology (GeoNames)"
    domain = "Geography"
    category = "Geographic Knowledge"
    version = "3.3"
    last_updated = "2022-01-30"
    creator = "Bernard Vatant"
    license = "Creative Commons 3.0"
    format = "RDF"
    download_url = "https://www.geonames.org/ontology"


class GTS(BaseOntology):
    """
    This is an RDF/OWL representation of the GeoSciML Geologic Timescale model, which has been adapted
    from the model described in Cox, S.J.D, & Richard, S.M. (2005) A formal model for the geologic timescale and GSSP,
    compatible with geospatial information transfer standards, Geosphere, Geological Society of America.
    """
    ontology_id = "GTS"
    ontology_full_name = "Geologic Timescale model (GTS)"
    domain = "Geography"
    category = "geospatial Information, Geology"
    version = "1.0"
    last_updated = "2020-05-31"
    creator = "Simon J D Cox (simon.cox@csiro.au) of CSIRO"
    license = "Creative Commons 1.0"
    format = "TTL"
    download_url = "https://raw.githack.com/CGI-IUGS/timescale-ont/master/html/gts.html"


class Juso(BaseOntology):
    """
    Juso Ontology is a Web vocabulary for describing geographical addresses and features.
    """
    ontology_id = "Juso"
    ontology_full_name = "Juso Ontology (Juso)"
    domain = "Geography"
    category = "geographical knowledge"
    version = "0.1.1"
    last_updated = "2015-11-10"
    creator = "James G. Kim, LiST Inc."
    license = "Creative Commons 4.0"
    format = "TTL"
    download_url = "https://rdfs.co/juso/0.1.1/html"
