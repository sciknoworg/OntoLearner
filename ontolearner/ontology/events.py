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


class Conference(BaseOntology):
    """
    The conference-ontology is a new self-contained ontology for modeling knowledge about conferences.
    The conference-ontology adopts the best ontology design practices (e.g., Ontology Design Patterns,
    ontology reuse and interlinking) and guarantees interoperability with SWC ontology
    and all other pertinent vocabularies.
    """
    ontology_id = "Conference"
    ontology_full_name = "Conference Ontology (Conference)"
    domain = "Events"
    category = "Conferences"
    version = None
    last_updated = "2016/04/30"
    creator = "Aldo Gangemi et al."
    license = "Creative Commons 3.0"
    format = "OWL"
    download_url = "http://www.scholarlydata.org/ontology/conference-ontology.owl"


class iCalendar(BaseOntology):
    """
    iCalendar is an Internet standard for exchanging calendar and scheduling data across different applications
    and platforms using a standardized text-based format (.ics). It enables interoperability for events, tasks,
    and scheduling, supporting features like recurring events, invitations, and time zone adjustments.
    While widely used in applications like Google Calendar and Outlook, its complexity and partial implementations
    pose challenges, leading to efforts to integrate it with Semantic Web technologies
    for enhanced data linking and automation.
    """
    ontology_id = "iCalendar"
    ontology_full_name = "iCalendar Vocabulary (iCalendar)"
    domain = "Events"
    category = "Calendar and Scheduling"
    version = "1.14"
    last_updated = "2004/04/07"
    creator = "Dan Connolly, W3C, Libby Miller, ASemantics"
    license = "Open Publication License"
    format = "RDF"
    download_url = "https://www.w3.org/2002/12/cal/"


class LODE(BaseOntology):
    """
    People conventionally refer to an action or occurrence taking place at a certain time
    at a specific location as an event. This notion is potentially useful for connecting individual facts
    recorded in the rapidly growing collection of linked data sets and for discovering more complex relationships
    between data. The LODE provide an overview and comparison of existing event models,
    looking at the different choices they make of how to represent events. It is a model for publishing records
    of events as Linked Data. A tools for populating this model and a prototype “event directory” web service,
    which can be used to locate stable URIs for events that have occurred,
    provide RDFS+OWL descriptions and link to related resources.
    """
    ontology_id = "LODE"
    ontology_full_name = "Linking Open Descriptions of Events (LODE)"
    domain = "Events"
    category = "Events"
    version = "2020-10-31"
    last_updated = "2020-10-31"
    creator = "Ryan Shaw"
    license = "Creative Commons Attribution 3.0"
    format = "RDF"
    download_url = "https://linkedevents.org/ontology/"
