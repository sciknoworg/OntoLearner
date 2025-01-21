
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Tuple
from rdflib import Graph, Namespace, URIRef, RDF
import networkx as nx
import logging

from ..base.data_model import OntologyData, TermTyping, TaxonomyRelation, NonTaxonomicRelation

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


@dataclass
class OntologyNamespaces:
    """Container for common ontology namespaces"""
    RDF_SCHEMA: Namespace = Namespace("http://www.w3.org/2000/01/rdf-schema#")
    SKOS: Namespace = Namespace("http://www.w3.org/2004/02/skos/core#")
    OWL: Namespace = Namespace("http://www.w3.org/2002/07/owl#")
    RDF: RDF = RDF


class BaseOntology(ABC):
    """
    Base class for ontology processing.
    """
    def __init__(self):
        """
        Initialize the ontology.
        """
        # Initialize both RDF and NetworkX graphs
        self.rdf_graph = Graph()
        self.nx_graph = nx.DiGraph()
        self.namespaces: OntologyNamespaces = OntologyNamespaces()


    def load(self, path: str) -> None:
        """
        Load an ontology from a file.

        :param path: Path to the ontology file
        :return: None
        """
        try:
            logger.info(f"Loading ontology from {path}")

            self.rdf_graph.parse(path, format="xml")

            if len(self.rdf_graph) == 0:
                raise ValueError("Loaded ontology contains no triples")

            logger.info(f"Loaded {len(self.rdf_graph)} triples")

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
        try:
            term_typings = self.extract_term_typings()
            types, taxonomies = self.extract_type_taxonomies()
            types_nt, relations, non_taxonomic = self.extract_type_non_taxonomic_relations()

            return OntologyData(
                term_typings=term_typings,
                type_taxonomies={
                    'types': types,
                    'taxonomies': taxonomies
                },
                type_non_taxonomic_relations={
                    'types': types_nt,
                    'relations': relations,
                    'grand_truths': non_taxonomic
                }
            )
        except Exception as e:
            logger.error(f"Error extracting ontology data: {e}")
            raise


    def get_term_label(self, uri: URIRef) -> str:
        """
        Get human-readable label for a term using standard label properties.
        """
        # Try standard label properties
        predicates = [
            self.namespaces.RDF_SCHEMA.label,
            self.namespaces.SKOS.prefLabel,
            self.namespaces.SKOS.altLabel
        ]

        for predicate in predicates:
            labels = list(self.rdf_graph.objects(subject=uri, predicate=predicate))

            if labels:
                return str(labels[0])

        # Fallback to URI fragment
        return str(uri).split('/')[-1]


    @abstractmethod
    def build_graph(self) -> None:
        """
        Build NetworkX graph from RDF data.

        This method should be implemented by each specific ontology class
        to handle their unique graph structure.
        """
        pass


    @abstractmethod
    def extract_term_typings(self) -> List[TermTyping]:
        """
        Extract term typings from the ontology.

        :return: List of validated term typing entries
        """
        pass


    @abstractmethod
    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomyRelation]]:
        """
        Extract taxonomy from the ontology

        :return: Types and their taxonomic relationships
        """
        pass


    @abstractmethod
    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        """
        Extract non-taxonomic relations from the ontology.

        :return: Types, relations, and validated relationship entries
        """
        pass
