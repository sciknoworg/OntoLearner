
from rdflib import URIRef, BNode
from typing import List, Tuple, Set

from ..base.ontology import BaseOntology
from ontolearner.data_structure.data import TermTyping, TaxonomicRelation, NonTaxonomicRelation

from .. import logger


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

        # TODO refactor -> don't define relations manually
        # CS-specific relations
        self.relations = [
            URIRef("http://cso.kmi.open.ac.uk/schema/cso#contributesTo"),
        ]

        # CS-specific class axioms
        # class_axioms = [
        #     URIRef("http://cso.kmi.open.ac.uk/schema/cso#relatedEquivalent")
        # ]


    def build_graph(self) -> None:
        """
        Build graph representation of the Computer Science Ontology structure

        TODO: refactor
            - move the function into the Base class
            - separate the steps and make each step as function
            - for any ontology that the steps are different you can define the function for it
            Steps:
                1. Adding classes and their properties
                2. Adding hierarchical relations
                3. Adding all defined relationships!
                4. Adapt this behavior in all the ontology classes that you have on the list for now!
        """
        self.nx_graph.clear()

        rdf = self.get_namespace('rdf')
        cso = self.get_namespace('ns0')

        # Add all topics
        for s in self.rdf_graph.subjects(rdf.type, cso.Topic):
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
        cso = self.get_namespace('ns0')

        for s, _, o in self.rdf_graph.triples((None, cso.superTopicOf, None)):
            if isinstance(s, (URIRef, BNode)) and isinstance(o, (URIRef, BNode)):
                s_label = self.get_term_label(s)
                o_label = self.get_term_label(o)

                if s_label and o_label:
                    self.nx_graph.add_edge(s_label, o_label)


    def _add_contribution_relationships(self) -> None:
        """Add contribution relationships between topics"""
        for relation in self.relations:
            relation_name = self.get_term_label(relation)

            for s, _, o in self.rdf_graph.triples((None, relation, None)):
                if isinstance(s, (URIRef, BNode)) and isinstance(o, (URIRef, BNode)):
                    s_label = self.get_term_label(s)
                    o_label = self.get_term_label(o)
                    if s_label and o_label:
                        self.nx_graph.add_edge(s_label, o_label, relation_type=relation_name)


    def extract_term_typings(self) -> List[TermTyping]:
        """
        Extract term typings for Computer Science Ontology.

        :return: List of validated term-type mappings
        """
        term_typings = []

        # Get required namespaces
        rdfs = self.get_namespace('rdfs')
        rdf = self.get_namespace('rdf')
        cso = self.get_namespace('ns0')

        if not all([rdfs, rdf, cso]):
            logger.warning("Required namespaces not found")
            return term_typings

        for s, p, o in self.rdf_graph.triples((None, rdfs.label, None)):
            if (s, rdf.type, cso.Topic) in self.rdf_graph:
                term = str(o)
                types: Set[str] = set()

                # Collect all types for this term
                for _, _, type_uri in self.rdf_graph.triples((s, rdf.type, None)):
                    if isinstance(type_uri, (URIRef, BNode)):
                        type_label = self.get_term_label(type_uri)

                        if type_label:
                            types.add(type_label)

                if types:
                    # Append a validated TermTyping instance
                    term_typings.append(TermTyping(term=term, types=list(types)))

        logger.debug(f"Extracted {len(term_typings)} term typings")

        return term_typings


    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomicRelation]]:
        """
        Extract type taxonomies from CSO.

        This method performs two main tasks:
        1. Collects all types (topics) defined in the ontology
        2. Extracts hierarchical relationships between these types using superTopicOf relations

        :return:
            A tuple containing:
                - List of all types found in the ontology
                - List of taxonomic relationships between these types
        """
        types: List[str] = []
        taxonomies: List[TaxonomicRelation] = []

        # Get required namespaces
        rdf = self.get_namespace('rdf')
        cso = self.get_namespace('ns0')

        if not all([rdf, cso]):
            logger.warning("Required namespaces (rdf, cso) not found")
            return [], []

        # Collect all types
        for s in self.rdf_graph.subjects(rdf.type, cso.Topic):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

        # Extract taxonomic relationships using superTopicOf predicate
        for s, _, o in self.rdf_graph.triples((None, cso.superTopicOf, None)):
            superclass_label = self.get_term_label(o)
            subclass_label = self.get_term_label(s)

            if superclass_label and subclass_label:
                # Append a validated TaxonomyRelation instance
                taxonomies.append(
                    TaxonomicRelation(
                        parent=superclass_label,
                        child=subclass_label
                    )
                )

        logger.debug(f"Extracted {len(types)} types and {len(taxonomies)} taxonomic relations")

        return types, taxonomies


    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        """
        Extract non-taxonomic relations from the Computer Science Ontology.

        This method performs three main tasks:
            1. Collects all types (topics) from the ontology
            2. Gets the labels for all defined relations
            3. Extracts non-taxonomic relationships between topics using these relations

        :returns:
            Tuple containing:
            - List[str]: All types found in the ontology
            - List[str]: Names of all non-taxonomic relations
            - List[NonTaxonomicRelation]: The actual relationship instances found
        """
        types: List[str] = []
        relations: List[str] = [self.get_term_label(rel) for rel in self.relations]
        non_taxonomic_relations: List[NonTaxonomicRelation] = []

        # Get required namespaces
        rdf = self.get_namespace('rdf')
        cso = self.get_namespace('ns0')

        if not all([rdf, cso]):
            logger.warning("Required namespaces (rdf, cso) not found")
            return [], [], []

        # Collect all types first
        for s in self.rdf_graph.subjects(rdf.type, cso.Topic):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)

                if type_label:
                    types.append(type_label)

        # Extract non-taxonomic relations
        for relation in self.relations:
            relation_label = self.get_term_label(relation)

            # Find all triples using this relation
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
                                relation=relation_label
                            )
                        )

        logger.debug(
            f"Extracted non-taxonomic relations:\n"
            f"- {len(types)} types\n"
            f"- {len(relations)} relation types\n"
            f"- {len(non_taxonomic_relations)} relationship instances"
        )

        return types, relations, non_taxonomic_relations
