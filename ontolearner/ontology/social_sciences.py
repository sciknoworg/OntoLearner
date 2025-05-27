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


class AS2(BaseOntology):
    """
    The Activity Streams 2.0 ontology is a vocabulary for describing social activities and actions.
    It is based on the Activity Streams 2.0 specification and provides a set of classes and properties
    for describing activities on the web.
    """
    ontology_id = "AS2"
    ontology_full_name = "Activity Streams 2.0 Ontology (AS2)"
    domain = "Social Sciences"
    category = "Social"
    version = "2.0"
    last_updated = "23 May 2017"
    creator = None
    license = "W3C Document License"
    format = "TTL"
    download_url = "https://github.com/w3c/activitystreams?tab=License-1-ov-file#readme"


class BIO(BaseOntology):
    """
    The BIO vocabulary contains terms useful for finding out more about people and their backgrounds and has some cross-over into genealogical information.
    The approach taken is to describe a person's life as a series of interconnected key events, around which other information can be woven.
    This vocabulary defines the event framework and supplies a set of core event types that cover many use cases, but it is expected that it
    will be extended in other vocabularies to suit their needs. The intention of this vocabulary is to describe biographical events of people
    and this intention carries through to the definitions of the properties and classes which are person-centric rather than neutral. For example
    the Employment event puts the person being employed as the principal agent in the event rather than the employer.
    """
    ontology_id = "BIO"
    ontology_full_name = "BIO: A vocabulary for biographical information (BIO)"
    domain = "Social Sciences"
    category = "Biographical Information"
    version = "0.1"
    last_updated = "2010-05-10"
    creator = "Ian Davis and David Galbraith"
    license = "Public Domain"
    format = "RDF"
    download_url = "https://vocab.org/bio/"


class Contact(BaseOntology):
    """
    Ontology to capture concepts related to contact information (addresses, phone numbers).
    Reuses the iContact Ontology developed by the Enterprise Integration Lab in Toronto.
    The iContact ontology is extended to introduce a specialized definition of Hours of Operation,
    defined as a subclass of both the iContact definition of hours of operation,
    and a subclass of the Recurring Event class defined in the iCity Recurring Event ontology.
    The Contact ontology also extends the definition of address to include an associated location.
    """
    ontology_id = "Contact"
    ontology_full_name = "Contact Ontology (Contact)"
    domain = "Social Sciences"
    category = "Social"
    version = "1.0"
    last_updated = "2018-07-06"
    creator = "Mark Fox, Megan Katsumi"
    license = None
    format = "RDF"
    download_url = "https://enterpriseintegrationlab.github.io/icity/Contact/Contact_1.0/doc/index-en.html"


class FOAF(BaseOntology):
    """
    FOAF is a project devoted to linking people and information using the Web.
    Regardless of whether information is in people's heads, in physical or digital documents,
    or in the form of factual data, it can be linked.
    """
    ontology_id = "FOAF"
    ontology_full_name = "Friend of a Friend (FOAF)"
    domain = "Social Sciences"
    category = "Social"
    version = "0.1"
    last_updated = "14 January 2014"
    creator = "Dan Brickley, Libby Miller"
    license = "Creative Commons"
    format = "RDF"
    download_url = "http://xmlns.com/foaf/0.1/"


class SIOC(BaseOntology):
    """
    The SIOC (Semantically-Interlinked Online Communities) Ontology is an ontology for describing the
    information in online communities. This includes sites that support online discussions, blogging,
    file sharing, photo sharing, social networking, etc.
    """
    ontology_id = "SIOC"
    ontology_full_name = "Semantically-Interlinked Online Communities (SIOC)"
    domain = "Social Sciences"
    category = "Social Networks"
    version = "1.36"
    last_updated = "2018/02/28"
    creator = "Data Science Institute, NUI Galway"
    license = "Creative Commons 3.0"
    format = "RDF"
    download_url = "http://rdfs.org/sioc/spec/"
