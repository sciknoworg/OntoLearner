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

import inspect
import os
import xml.etree.ElementTree as ET
from rdflib import Graph, URIRef, Literal, Namespace, RDF
from xml.dom import minidom

import ontolearner.ontology as ontology_module
from .base import BaseOntology

class AutoOntology:
    """
       Factory class to automatically instantiate an ontology class from the `ontolearner.ontology` module
       based on a given ontology ID.

       This class scans all classes defined in the `ontolearner.ontology` module and returns an instance
       of the first class that:
         - has a callable `load` method,
         - has an `ontology_id` attribute,
         - and whose class name matches the given `ontology_id` (case-insensitive).

       If no matching class is found, an instance of `BaseOntology` is returned by default.

       Args:
           ontology_id (str): The identifier (name) of the ontology class to instantiate.

       Returns:
           BaseOntology: An instance of the matching ontology class or a `BaseOntology` fallback.

       Example:
           >>> auto_onto = AutoOntology("AgrO")
           >>> print(type(auto_onto))
           >>> <class 'ontolearner.ontology.AgrO'>

           If no class matches "unknownontology":
           >>> auto_onto = AutoOntology("unknownontology")
           >>> print(type(auto_onto))
           >>> <class 'ontolearner.base.BaseOntology'>
       """
    def __new__(self, ontology_id) -> BaseOntology:
        for name, obj in inspect.getmembers(ontology_module):
            if inspect.isclass(obj):
                if hasattr(obj, 'load') and callable(getattr(obj, 'load')) and hasattr(obj, 'ontology_id'):
                    instance = obj()
                    if str(obj).split("'")[-2].split(".")[-1].lower() == ontology_id.lower():
                        return instance
        return BaseOntology()



class OntoLearnerMetadataExporter:
    """Generates Dublin Core metadata for ontology classes."""
    def __init__(self):
        self.format: str = "pretty-xml"

    def get_url(self, domain, ontology_id):
        return f"https://ontolearner.readthedocs.io/benchmarking/{domain.lower().replace(' ', '_')}/{ontology_id.lower()}.html"

    def export(self, path: str = "DCMI-Metadata.rdf"):
        DC = Namespace("http://purl.org/dc/elements/1.1/")
        DCTERMS = Namespace("http://purl.org/dc/terms/")
        ONTOLOGIZER = Namespace("https://ontolearner.readthedocs.io/ontologizer/ontology_modularization.html#")

        g_head = Graph()
        g_head.bind("dc", DC)
        g_head.bind("dcterms", DCTERMS)
        g_head.bind("ontologizer", ONTOLOGIZER)

        collection_uri = URIRef("https://ontolearner.readthedocs.io/benchmarking/benchmark.html")
        g_head.add((collection_uri, RDF.type, ONTOLOGIZER.Collection))
        g_head.add((collection_uri, DC.title, Literal("OntoLearner Benchmark Ontologies")))
        g_head.add((collection_uri, DC.description, Literal(
            "This Dublin Core metadata collection describes ontologies benchmarked in OntoLearner. "
            "It includes information such as title, creator, format, license, and version."
        )))
        g_head.add((collection_uri, DC.creator, Literal("OntoLearner Team")))
        g_head.add((collection_uri, DCTERMS.license, Literal("MIT License")))
        g_head.add((collection_uri, DCTERMS.hasVersion,
                    Literal(open(os.path.join(os.path.dirname(__file__), 'VERSION')).read().strip())))

        g_body = Graph()
        g_body.bind("dc", DC)
        g_body.bind("dcterms", DCTERMS)
        g_body.bind("ontologizer", ONTOLOGIZER)

        for name, obj in inspect.getmembers(ontology_module):
            if inspect.isclass(obj) and name != "BaseOntology":
                if hasattr(obj, 'load') and callable(getattr(obj, 'load')) and hasattr(obj, 'ontology_id'):
                    onto = obj()
                    uri = URIRef(self.get_url(onto.domain, onto.ontology_id))
                    g_body.add((uri, RDF.type, ONTOLOGIZER.Ontology))
                    g_body.add((uri, DC.identifier, Literal(onto.ontology_id)))
                    g_body.add((uri, DCTERMS.title, Literal(onto.ontology_full_name)))
                    g_body.add((uri, DCTERMS.description, Literal(onto.__doc__.replace("\n", " "))))
                    if onto.creator:
                        g_body.add((uri, DCTERMS.creator, Literal(onto.creator)))
                    if onto.format:
                        g_body.add((uri, DCTERMS['format'], Literal(onto.format)))
                    if onto.last_updated:
                        g_body.add((uri, DCTERMS.date, Literal(onto.last_updated)))
                    if onto.license:
                        g_body.add((uri, DCTERMS.license, Literal(onto.license)))
                    if onto.download_url:
                        g_body.add((uri, DCTERMS.source, Literal(onto.download_url)))
                    if onto.domain:
                        g_body.add((uri, DCTERMS.subject, Literal(onto.domain)))
                    if onto.category:
                        g_body.add((uri, DCTERMS.subject, Literal(onto.category)))
                    if onto.version:
                        g_body.add((uri, DCTERMS.hasVersion, Literal(onto.version)))

        head_xml = g_head.serialize(format=self.format)
        body_xml = g_body.serialize(format=self.format)
        nsmap = {
            "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "dc": "http://purl.org/dc/elements/1.1/",
            "dcterms": "http://purl.org/dc/terms/",
            "ontologizer": str(ONTOLOGIZER),
        }
        for p, u in nsmap.items():
            ET.register_namespace(p, u)

        head_root = ET.fromstring(head_xml)
        body_root = ET.fromstring(body_xml)

        rdf_tag = f'{{{nsmap["rdf"]}}}RDF'
        merged_root = ET.Element(rdf_tag)
        for child in list(head_root):
            merged_root.append(child)
        for child in list(body_root):
            merged_root.append(child)

        rough_str = ET.tostring(merged_root, encoding="utf-8")
        reparsed = minidom.parseString(rough_str)
        pretty_str = reparsed.toprettyxml(indent="    ", encoding="utf-8").decode("utf-8")
        pretty_str = "\n".join([line for line in pretty_str.splitlines() if line.strip()])
        with open(path, "w", encoding="utf-8") as f:
            f.write(pretty_str)
