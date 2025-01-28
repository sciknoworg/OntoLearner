from abc import ABC, abstractmethod
from typing import List, Tuple, Any
from rdflib import Graph, OWL, URIRef, RDFS, RDF
import networkx as nx

from ..data_structure import (OntologyData, TermTyping, TaxonomicRelation, NonTaxonomicRelation,
                              TypeTaxonomies, NonTaxonomicRelations)
from .. import logger


class BaseOntology(ABC):
    """
    Base class for ontology processing
    """
    def __init__(self, language: str ='en'):
        """Initialize the ontology"""
        self.rdf_graph = None
        self.nx_graph = None
        self.language = language

    def load(self, path: str) -> None:
        """
         Load an ontology from a file and initialize its namespaces.

        :param path: Path to the ontology file
        """
        try:
            logger.info(f"Loading ontology from {path}")
            self.rdf_graph = Graph()
            self.rdf_graph.parse(path, format="xml")
            if len(self.rdf_graph) == 0:
                raise ValueError("Loaded ontology contains no triples")
            logger.info(
                f"Successfully loaded ontology:\n"
                f"- {len(self.rdf_graph)} triples\n"
            )
        except FileNotFoundError:
            logger.error(f"Ontology file not found: {path}")
            raise
        except Exception as e:
            logger.error(f"Error loading ontology: {str(e)}")
            raise

    def extract(self) -> OntologyData:
        """
        Extract all information from all the three functions below.

        :return: Dict containing term typings, taxonomies, and relations
        """
        term_typings = self.extract_term_typings()
        types, taxonomies = self.extract_type_taxonomies()
        types_nt, relations, non_taxonomies = self.extract_type_non_taxonomic_relations()

        return OntologyData(
            term_typings=term_typings,
            type_taxonomies=TypeTaxonomies(
                types=types,
                taxonomies=taxonomies
            ),
            type_non_taxonomic_relations=NonTaxonomicRelations(
                types=types_nt,
                relations=relations,
                non_taxonomies=non_taxonomies
            )
        )

    def is_valid_label(self, label: str) -> Any:
        invalids = ['root', 'thing']
        if label.lower() in invalids:
            return None
        return label

    def get_label(self, uri: str) -> str:
        """
        Extracts the label for a given URI in the specified language from the RDF graph.
        If no valid label is found, returns None.

        :param uri: URI of the entity to retrieve the label for.
        :param graph: RDF graph (rdflib.Graph) containing the ontology data.
        :param language: The language code to extract the label (default is 'en').
        :return: The label in the specified language, or None if no label found.
        """
        entity = URIRef(uri)
        labels = list(self.rdf_graph.objects(subject=entity, predicate=RDFS.label))
        for label in labels:
            if label.language == self.language:
                return self.is_valid_label(str(label))
        if labels:
            first_label = str(labels[0])
            if len(first_label) > 3 and not first_label.startswith("http"):
                return self.is_valid_label(first_label)
        return self.is_valid_label(uri.split("#")[-1]) if "#" in uri else None

    @abstractmethod
    def build_graph(self) -> None:
        """
        Build NetworkX graph from RDF data.

        This method should be implemented by each specific ontology class
        to handle their unique graph structure.
        """
        self.nx_graph = nx.DiGraph()
        for subject, predicate, obj in self.rdf_graph:
            subject_str = str(subject)
            predicate_str = str(predicate)
            object_str = str(obj)
            self.nx_graph.add_node(subject_str)
            self.nx_graph.add_node(object_str)
            self.nx_graph.add_edge(subject_str, object_str, label=predicate_str)

    @abstractmethod
    def extract_term_typings(self) -> List[TermTyping]:
        """
        Extract term typings from the ontology.

        :return: List of validated term typing entries
        """
        term_typings = []
        classes = set(self.rdf_graph.subjects(predicate=RDF.type, object=RDFS.Class)) | \
                  set(self.rdf_graph.subjects(predicate=RDF.type, object=OWL.Class))
        for class_uri in classes:
            instances = self.rdf_graph.subjects(predicate=RDF.type, object=class_uri)
            for instance in instances:
                term = self.get_label(uri=str(instance))
                types = self.get_label(uri=str(class_uri))
                if term and types:
                    term_typings.append(TermTyping(term=term, types=list(types)))
        return term_typings

    @abstractmethod
    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomicRelation]]:
        """
        Extract taxonomy from the ontology

        :return: Types and their taxonomic relationships
        """
        types, taxonomies = [], []
        subclasses = self.rdf_graph.subjects(predicate=RDFS.subClassOf)
        for subclass in subclasses:
            parent_class = self.rdf_graph.objects(subject=subclass, predicate=RDFS.subClassOf)
            for parent in parent_class:
                child = self.get_label(uri=str(subclass))
                parent = self.get_label(uri=str(parent))
                if child and parent:
                    types.append(child)
                    types.append(parent)
                    taxonomies.append(TaxonomicRelation(parent=parent,child=child))
        types = list(set(types))
        return types, taxonomies

    @abstractmethod
    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        """
        Extract non-taxonomic relations from the ontology.

        :return: Types, relations, and validated relationship entries
        """
        pass
