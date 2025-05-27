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


class ChordOntology(BaseOntology):
    """
    The Chord Ontology is an ontology for describing chords in musical pieces.
    """
    ontology_id = "ChordOntology"
    ontology_full_name = "Chord Ontology (ChordOntology)"
    domain = "Arts and Humanities"
    category = "Musical Works"
    version = "1.0"
    last_updated = "2007-10-25"
    creator = "Yves Raimond, Samer Abdallah, Centre for Digital Music, Queen Mary, University of London"
    license = "Creative Commons 3.0"
    format = "RDF"
    download_url = "https://github.com/motools/chordontology"


class ICON(BaseOntology):
    """
    The ICON ontology deals with high granularity art interpretation. It was developed by conceptualizing
    Panofsky's theory of levels of interpretation, therefore artworks can be described according
    to Pre-iconographical, Iconographical and Iconological information.
    """
    ontology_id = "ICON"
    ontology_full_name = "Icon Ontology (ICON)"
    domain = "Arts and Humanities"
    category = "Art History, Cultural Heritage"
    version = "2.1.0"
    last_updated = "April 26th, 2024"
    creator = "Knowledge Media Institute"
    license = "Creative Commons 4.0"
    format = "OWL"
    download_url = "https://w3id.org/icon/ontology/"


class MusicOntology(BaseOntology):
    """
    The Music Ontology Specification provides main concepts and
    properties fo describing music (i.e. artists, albums and tracks)
    on the Semantic Web.
    """
    ontology_id = "MusicOntology"
    ontology_full_name = "Music Ontology (MusicOntology)"
    domain = "Arts and Humanities"
    category = "Music Theory"
    version = "2.1.5"
    last_updated = "2013/07/22"
    creator = "Knowledge Media Institute, Open University"
    license = "Creative Commons 4.0"
    format = "RDF"
    download_url = "https://github.com/motools/musicontology"


class Nomisma(BaseOntology):
    """
    Nomisma Ontology is a collaborative project to provide stable digital representations of numismatic concepts according
    to the principles of Linked Open Data. These take the form of http URIs that provide access to the information
    about a concept in various formats. The project is a collaborative effort of the American Numismatic Society
    and the Institute for the Study of the Ancient World at New York University.
    """
    ontology_id = "Nomisma"
    ontology_full_name = "Nomisma Ontology (Nomisma)"
    domain = "Arts and Humanities"
    category = "Numismatics"
    version = None
    last_updated = "2025-01-22"
    creator = "American Numismatic Society, Institute for the Study of the Ancient World"
    license = "Creative Commons 4.0"
    format = "TTL"
    download_url = "https://www.dainst.org/forschung/projekte/noslug/2098"


class TimelineOntology(BaseOntology):
    """
    The Timeline Ontology is centered around the notion of timeline,
    seen here as a way to identify a temporal backbone.
    A timeline may support a signal, a video, a score, a work, etc.
    """
    ontology_id = "TimelineOntology"
    ontology_full_name = "Timeline Ontology (TimelineOntology)"
    domain = "Arts and Humanities"
    category = "Music Theory"
    version = "1.0"
    last_updated = "25th October 2007"
    creator = "Christopher Sutton, Yves Raimond, Matthias Mauch"
    license = "Creative Commons 1.0"
    format = "RDF"
    download_url = "https://github.com/motools/timelineontology"
