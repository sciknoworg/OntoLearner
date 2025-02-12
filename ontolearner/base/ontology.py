from abc import ABC
from typing import List, Tuple, Any, Set
from rdflib import Graph, OWL, URIRef, RDFS, RDF
import networkx as nx

from ..data_structure import (OntologyData, TermTyping, TaxonomicRelation, NonTaxonomicRelation,
                              TypeTaxonomies, NonTaxonomicRelations)
from .. import logger


class BaseOntology(ABC):
    """
    Base class for ontology processing
    """
    ontology_full_name: str = None

    def __init__(self, language: str = 'en'):
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

    @staticmethod
    def is_valid_label(label: str) -> Any:
        invalids = ['root', 'thing']
        if label.lower() in invalids:
            return None
        return label

    def get_label(self, uri: str) -> str:
        """
        Extracts the label for a given URI in the specified language from the RDF graph.
        If no valid label is found, returns None.

        :param uri: URI of the entity to retrieve the label for.
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
        if "#" in uri:
            local_name = uri.split("#")[-1]
        elif "/" in uri:
            local_name = uri.split("/")[-1]
        else:
            local_name = uri
        label = self.is_valid_label(local_name)
        if not label:
            logger.warning(f"No valid label for URI: {uri}")
        return label

    def build_graph(self) -> None:
        """
        Build NetworkX graph from RDF data.

        This method should be implemented by each specific ontology class
        to handle their unique graph structure.
        """
        self.nx_graph = nx.DiGraph()
        for subject, predicate, obj in self.rdf_graph:
            subject_label = self.get_label(str(subject))
            object_label = self.get_label(str(obj))
            predicate_label = self.get_label(str(predicate))

            if subject_label and object_label and predicate_label:
                self.nx_graph.add_node(subject_label)
                self.nx_graph.add_node(object_label)
                self.nx_graph.add_edge(subject_label, object_label, label=predicate_label)

    # ------------------- Term Typings -------------------
    def extract_term_typings(self) -> List[TermTyping]:
        """
        Extract term-to-type mappings (e.g., instances of classes).
        """
        term_typings = []
        for class_uri in self._get_relevant_classes():
            for instance in self._get_instances_for_class(class_uri):
                term = self.get_label(uri=str(instance))
                types = self.get_label(uri=str(class_uri))
                if term and types:
                    term_typings.append(TermTyping(term=term, types=list(types)))
        logger.debug(f"Extracted {len(term_typings)} term typings for the Ontology.")
        return term_typings

    def _get_relevant_classes(self) -> Set[URIRef]:
        """Hook: Define which classes to process (default: all classes)."""
        return (set(self.rdf_graph.subjects(RDF.type, RDFS.Class)) |
                set(self.rdf_graph.subjects(RDF.type, OWL.Class)))

    def _get_instances_for_class(self, class_uri: URIRef) -> Set[URIRef]:
        """Hook: Get instances of a class (default: direct instances)."""
        return set(self.rdf_graph.subjects(RDF.type, class_uri))

    # ------------------- Taxonomy Extraction -------------------
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
                    taxonomies.append(TaxonomicRelation(parent=parent, child=child))
        types = list(set(types))
        logger.debug(f"Extracted {len(taxonomies)} taxonomic relations for the Ontology.")
        return types, taxonomies

    # ------------------- Non-Taxonomic Relations -------------------
    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        """
         Extract non-taxonomic relations from the ontology.

         :return: Types, relations, and validated relationship entries
         """
        types_set = set()
        relations_set = set()
        non_taxonomic_pairs: List[NonTaxonomicRelation] = []

        # Iterate over all triples in the RDF graph
        for s, p, o in self.rdf_graph:
            # If both subject and object are classes and the predicate is not rdfs:subClassOf,
            # it's a non-taxonomic relationship
            if self._is_valid_non_taxonomic_triple(s, p, o):
                # Retrieve labels for subject, object, and predicate
                head = self.get_label(str(s))
                tail = self.get_label(str(o))
                relation = self.get_label(str(p))

                if head and tail and relation:
                    non_taxonomic_pairs.append(
                        NonTaxonomicRelation(
                            head=head,
                            tail=tail,
                            relation=relation
                        )
                    )
                    types_set.update([head, tail])
                    relations_set.add(relation)

        # Convert sets to sorted lists for consistent output
        types = sorted(types_set)
        relations = sorted(relations_set)
        logger.debug(f"Extracted {len(non_taxonomic_pairs)} non-taxonomic relations for the Ontology.")
        return types, relations, non_taxonomic_pairs

    def _is_valid_non_taxonomic_triple(self, s: URIRef, p: URIRef, o: URIRef) -> bool:
        """Hook: Validate if a triple represents a non-taxonomic relation."""
        return (
            self.check_if_class(s) and
            self.check_if_class(o) and
            p != RDFS.subClassOf
        )

    def check_if_class(self, entity):
        """Check if an entity is a class (i.e., rdf:type rdfs:Class or owl:Class)."""
        for _, _, obj in self.rdf_graph.triples((entity, RDF.type, None)):
            if obj in (RDFS.Class, OWL.Class):
                return True
        return False
