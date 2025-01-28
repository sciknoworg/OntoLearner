
from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Optional
from rdflib import Graph, Namespace, URIRef
import networkx as nx

from ontolearner.data_structure.data import (
    OntologyData, TermTyping, TaxonomicRelation, NonTaxonomicRelation,
    TypeTaxonomies, NonTaxonomicRelations
)

from .. import logger


class BaseOntology(ABC):
    """
    Base class for ontology processing
    """
    CORE_NAMESPACES = {
        'rdf': "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
        'rdfs': "http://www.w3.org/2000/01/rdf-schema#",
        'owl': "http://www.w3.org/2002/07/owl#",
        'xsd': "http://www.w3.org/2001/XMLSchema#",
        'skos': "http://www.w3.org/2004/02/skos/core#"
    }

    def __init__(self):
        """Initialize the ontology"""
        self.rdf_graph = Graph()
        self.nx_graph = nx.DiGraph()
        self.namespaces: Dict[str, Namespace] = {}


    def load(self, path: str) -> None:
        """
         Load an ontology from a file and initialize its namespaces.

        :param path: Path to the ontology file
        """
        try:
            logger.info(f"Loading ontology from {path}")

            self.rdf_graph.parse(path, format="xml")

            # Initialize namespaces
            self._initialize_namespaces()

            if len(self.rdf_graph) == 0:
                raise ValueError("Loaded ontology contains no triples")

            logger.info(
                f"Successfully loaded ontology:\n"
                f"- {len(self.rdf_graph)} triples\n"
                f"- {len(self.namespaces)} namespaces"
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
        types_nt, relations, non_taxonomic = self.extract_type_non_taxonomic_relations()

        return OntologyData(
            term_typings=term_typings,
            type_taxonomies=TypeTaxonomies(
                types=types,
                taxonomies=taxonomies
            ),
            type_non_taxonomic_relations=NonTaxonomicRelations(
                types=types_nt,
                relations=relations,
                ground_truths=non_taxonomic
            )
        )


    def get_term_label(self, uri: URIRef) -> str:
        """
        Get human-readable label for a term using standard label properties.

        TODO:
            - consider the languages
            - the current code retrieves all available languages, like in this example:
                <rdfs:label xml:lang="es">organización</rdfs:label>
                <rdfs:label xml:lang="en">Membership</rdfs:label>
                <rdfs:label xml:lang="it">Appartenenza</rdfs:label>
                <rdfs:label xml:lang="fr">Engagement</rdfs:label>
            - currently, it only returns the first label
            - we should discuss how to focus on a specific language (e.g., en),
            - but ensure that the code is adaptable for multi-language support.
            - we can adjust the code to prioritize en while keeping it generic for future language handling.

        :param: The URI to get a label for
        :returns: The human-readable label, or the URI fragment if no label is found
        """

        rdfs = self.namespaces['rdfs']
        skos = self.namespaces['skos']

        # Try standard label properties
        for predicate in [rdfs.label, skos.prefLabel, skos.altLabel]:
            labels = list(self.rdf_graph.objects(subject=uri, predicate=predicate))
            if labels:
                return str(labels[0])

        # Fallback to URI fragment
        return str(uri).split('#')[-1]


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
    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomicRelation]]:
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


    def get_namespace(self, prefix: str) -> Optional[Namespace]:
        """
        Get a namespace by prefix.

        :param: prefix: The namespace prefix to look up
        :returns: The namespace if found, None otherwise
        """
        return self.namespaces.get(prefix)


    def get_default_namespace(self) -> Optional[Namespace]:
        """
        Get the default namespace of the ontology.

        :returns: The default namespace if one exists, None otherwise
        """
        return self.default_namespace


    def _initialize_namespaces(self) -> None:
        """
        Load all namespaces from the RDF graph that aren't already defined
        """
        # First, ensure core namespaces are available
        for prefix, uri in self.CORE_NAMESPACES.items():
            self.namespaces[prefix] = Namespace(uri)

        # Then load namespaces from the RDF file
        default_ns = None
        for prefix, uri in self.rdf_graph.namespaces():
            if prefix == '':  # Default namespace
                default_ns = uri
                self.default_namespace = Namespace(uri)
                logger.debug(f"Found default namespace: {uri}")
            else:
                # Don't override core namespaces if they're defined differently
                if prefix not in self.CORE_NAMESPACES:
                    self.namespaces[prefix] = Namespace(uri)
                    logger.debug(f"Added namespace {prefix}: {uri}")

        if not default_ns:
            logger.warning("No default namespace found in the ontology")
