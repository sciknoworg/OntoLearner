
from dataclasses import dataclass
from rdflib import URIRef, Namespace, BNode
from typing import List, Tuple, Set
import logging

from ..base.ontology import BaseOntology, OntologyNamespaces
from ..base.data_model import TermTyping, TaxonomyRelation, NonTaxonomicRelation

logger = logging.getLogger(__name__)


@dataclass
class ComputerOntologyNamespaces(OntologyNamespaces):
    """Extended namespaces for Computer Science Ontology"""
    CSO_SCHEMA: Namespace = Namespace("http://cso.kmi.open.ac.uk/schema/cso#")


class ComputerOntology(BaseOntology):
    """
    Class for processing Computer Science Ontology.

    This class implements specific processing logic for the Computer Science Ontology,
    handling computer science concepts and their relationships.
    """
    def __init__(self):
        """
        Initialize the Computer Science Ontology.
        """
        super().__init__()
        self.namespaces = ComputerOntologyNamespaces()

        # CS-specific relations
        self.relations = [
            URIRef("http://cso.kmi.open.ac.uk/schema/cso#contributesTo"),
            URIRef("http://cso.kmi.open.ac.uk/schema/cso#relatedEquivalent")
        ]


    def build_graph(self) -> None:
        """
        Build graph representation of the Computer Science Ontology structure
        """
        self.nx_graph.clear()

        # Add all topics
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.CSO_SCHEMA.Topic):
            if isinstance(s, (URIRef, BNode)):
                s_label = self.get_term_label(s)
                self.nx_graph.add_node(s_label)

        # Add hierarchical relationships
        self._add_topic_relationships()
        self._add_contribution_relationships()

        logger.info(f"Built Computer Science Ontology graph with {self.nx_graph.number_of_nodes()} "
                    f"nodes and {self.nx_graph.number_of_edges()} edges")


    def _add_topic_relationships(self) -> None:
        """Add topic hierarchical relationships"""
        for s, _, o in self.rdf_graph.triples((None, self.namespaces.CSO_SCHEMA.superTopicOf, None)):
            if isinstance(s, (URIRef, BNode)) and isinstance(o, (URIRef, BNode)):
                s_label = self.get_term_label(s)
                o_label = self.get_term_label(o)
                if s_label and o_label:
                    self.nx_graph.add_edge(s_label, o_label)


    def _add_contribution_relationships(self) -> None:
        """Add contribution relationships between topics"""
        for relation in self.relations:
            relation_name = str(relation).split('#')[-1]
            for s, _, o in self.rdf_graph.triples((None, relation, None)):
                if isinstance(s, (URIRef, BNode)) and isinstance(o, (URIRef, BNode)):
                    s_label = self.get_term_label(s)
                    o_label = self.get_term_label(o)
                    if s_label and o_label:
                        self.nx_graph.add_edge(s_label, o_label, relation_type=relation_name)


    def extract_term_typings(self) -> List[TermTyping]:
        """
        Extract term typings for Computer Science Ontology.

        :return: List of term typings
        """
        term_typings = []

        for s, p, o in self.rdf_graph.triples((None, self.namespaces.RDF_SCHEMA.label, None)):
            if (s, self.namespaces.RDF.type, self.namespaces.CSO_SCHEMA.Topic) in self.rdf_graph:
                term = str(o)
                types: Set[str] = set()

                for _, _, type_uri in self.rdf_graph.triples((s, self.namespaces.RDF.type, None)):
                    if isinstance(type_uri, (URIRef, BNode)):
                        type_label = self.get_term_label(type_uri)
                        if type_label:
                            types.add(type_label)

                if types:
                    # Append a validated TermTyping instance
                    term_typings.append(TermTyping(term=term, types=list(types)))

        return term_typings


    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomyRelation]]:
        """
        Extract type taxonomies from CSO.

        :return: Tuple containing list of types and list of taxonomy relations
        """
        types: List[str] = []
        taxonomies: List[TaxonomyRelation] = []

        # Collect all types
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.CSO_SCHEMA.Topic):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

        # Extract taxonomic relationships
        for s, _, o in self.rdf_graph.triples((None, self.namespaces.CSO_SCHEMA.superTopicOf, None)):
            if isinstance(s, (URIRef, BNode)) and isinstance(o, (URIRef, BNode)):
                superclass_label = self.get_term_label(o)
                subclass_label = self.get_term_label(s)

                if superclass_label and subclass_label:
                    # Append a validated TaxonomyRelation instance
                    taxonomies.append(
                        TaxonomyRelation(
                            term1=superclass_label,
                            term2=subclass_label,
                            relation=True,
                            relationship_type="direct"
                        )
                    )

        return types, taxonomies


    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        """
        Extract non-taxonomic relations from CSO.
        Returns types, non_taxonomic_relations, and their grand truths.
        """
        types: List[str] = []
        relations: List[str] = [str(rel).split('#')[-1] for rel in self.relations]
        non_taxonomic_relations: List[NonTaxonomicRelation] = []

        # Collect all types first
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.CSO_SCHEMA.Topic):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

        # Extract non-taxonomic relations
        for relation in self.relations:
            relation_label = str(relation).split('#')[-1]

            for s, _, o in self.rdf_graph.triples((None, relation, None)):
                if isinstance(s, (URIRef, BNode)) and isinstance(o, (URIRef, BNode)):
                    head_label = self.get_term_label(s)
                    tail_label = self.get_term_label(o)

                    if head_label and tail_label:
                        # Append a validated NonTaxonomicRelation instance
                        non_taxonomic_relations.append(
                            NonTaxonomicRelation(
                                head=head_label,
                                tail=tail_label,
                                relation=relation_label,
                                valid=True
                            )
                        )

        return types, relations, non_taxonomic_relations
