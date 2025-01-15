
from abc import ABC, abstractmethod
from typing import List, Dict, Tuple
from rdflib import Graph, Namespace, URIRef, RDF
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class BaseOntology(ABC):

    def __init__(self):
        self.graph = Graph()
        self.RDF_SCHEMA = Namespace("http://www.w3.org/2000/01/rdf-schema#")
        self.SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
        self.RDF = RDF

    def load(self, path: str):
        """
        Load an ontology from a file.
        """
        try:
            logger.info(f"Loading ontology from {path}")
            self.graph.parse(path, format="xml")
            logger.info(f"Loaded {len(self.graph)} triples")
        except Exception as e:
            logger.error(f"Error loading ontology: {e}")
            raise

    def extract(self) -> Dict:
        """
        Extract all information from all the three functions below.

        :return:
        """
        try:
            term_typings = self.extract_term_typings()
            types, taxonomies = self.extract_type_taxonomies()
            types, relations, non_taxonomic_relations = self.extract_type_non_taxonomic_relations()

            return {
                'term_typings': term_typings,
                'type_taxonomies': {
                    'types': types,
                    'taxonomies': taxonomies
                },
                'type_non_taxonomic_relations': {
                    'types': types,
                    'relations': relations,
                    'grand_truths': non_taxonomic_relations
                }
            }
        except Exception as e:
            logger.error(f"Error extracting ontology data: {e}")
            raise

    def get_term_label(self, uri: URIRef) -> str:
        """
        Get human-readable label for a term.
        """
        labels = list(self.graph.objects(subject=uri, predicate=self.RDF_SCHEMA.label))

        if not labels:
            # Try SKOS label if RDF label not found
            labels = list(self.graph.objects(subject=uri, predicate=self.SKOS.prefLabel))

        return str(labels[0]) if labels else str(uri).split('/')[-1]


    @abstractmethod
    def extract_term_typings(self) -> List[Dict]:
        """
        Extract term typings from the ontology.

        :return:
        """
        pass


    @abstractmethod
    def extract_type_taxonomies(self) -> Tuple[List, List[Dict]]:
        """
        Extract taxonomy from the ontology.

        :return: types, taxonomies
        """
        pass


    @abstractmethod
    def extract_type_non_taxonomic_relations(self) -> Tuple[List, List, List[Dict]]:
        """
        Extract non-taxonomic relations from the ontology.

        :return: types, relations, grand_truths
        """
        pass
