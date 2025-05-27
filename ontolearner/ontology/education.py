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


class BIBFRAME(BaseOntology):
    """
    The Bibframe vocabulary consists of RDF classes and properties used for the description of
    items cataloged principally by libraries, but may also be used to describe items cataloged by museums and archives.
    Classes include the three core classes - Work, Instance, and Item - in addition to many more
    classes to support description. Properties describe characteristics of the resource being
    described as well as relationships among resources. For example: one Work
    might be a "translation of" another Work; an Instance may be an
    "instance of" a particular Bibframe Work.  Other properties describe attributes of Works and Instances.  For
    example: the Bibframe property "subject" expresses an important attribute of a Work
    (what the Work is about), and the property "extent" (e.g. number of pages) expresses an
    attribute of an Instance.
    """
    ontology_id = "BIBFRAME"
    ontology_full_name = "Bibliographic Framework Ontology (BIBFRAME)"
    domain = "Education"
    category = "Library, Museums, Archives"
    version = "2.5.0"
    last_updated = "2022-10-03"
    creator = "United States, Library of Congress"
    license = "Creative Commons 1.0"
    format = "RDF"
    download_url = "https://id.loc.gov/ontologies/bflc.html"


class Common(BaseOntology):
    """
    Ontology for the representation of commons elements in the Trias ontology
    """
    ontology_id = "Common"
    ontology_full_name = "Common Ontology (Common)"
    domain = "Education"
    category = "Computer Science"
    version = "0.1.0"
    last_updated = None
    creator = "Jhon Toledo, Miguel Angel García, Oscar Corcho"
    license = "Creative Commons Attribution 4.0 International (CC BY 4.0)"
    format = "RDF"
    download_url = "https://w3id.org/mobility/trias/common/0.1.0"


class DoCO(BaseOntology):
    """
    DoCO, the Document Components Ontology, is an OWL 2 DL ontology that provides a general-purpose structured vocabulary
    of document elements. DoCO has been designed as a general unifying ontological framework for describing different aspects
    related to the content of scientific and other scholarly texts. Its primary goal has been to improve the interoperability
    and shareability of academic documents (and related services) when multiple formats are actually used for their storage.
    """
    ontology_id = "DoCO"
    ontology_full_name = "Document Components Ontology (DoCO)"
    domain = "Education"
    category = "document components"
    version = "1.3"
    last_updated = "2015-07-03"
    creator = "David Shotton and Silvio Peroni"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "http://www.sparontologies.net/ontologies/doco"
