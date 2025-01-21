
from typing import List, Tuple, Set
from rdflib import URIRef, Namespace, BNode
import logging

from ..base.ontology import BaseOntology, OntologyNamespaces
from ..base.data_model import TermTyping, TaxonomyRelation, NonTaxonomicRelation


logger = logging.getLogger(__name__)


class PlantOntologyNamespaces(OntologyNamespaces):
    """Container for Plant Ontology specific namespaces"""
    PLANT_SCHEMA: Namespace = Namespace("http://purl.obolibrary.org/obo/po#")


class PlantOntology(BaseOntology):
    """
    Class for processing Plant Ontology.
    """
    def __init__(self):
        """
        Initialize the Plant Ontology.
        """
        super().__init__()
        self.namespaces = PlantOntologyNamespaces()

        # Plant Ontology specific relations
        self.relations = [
            URIRef("http://www.w3.org/2004/02/skos/core#related"),
            URIRef("http://www.w3.org/2004/02/skos/core#broadMatch")
        ]

    def build_graph(self) -> None:
        """
        Build a comprehensive graph representation of the Plant Ontology structure.
        Captures class hierarchy, relationships, and ontological properties.
        """
        self.nx_graph.clear()

        # Add classes and their properties
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.PLANT_SCHEMA.Class):
            s_label = self.get_term_label(s)

            properties = {}

            for p, o in self.rdf_graph.predicate_objects(s):
                if isinstance(o, URIRef):
                    o = self.get_term_label(o)
                    properties[str(p).split('#')[-1]] = str(o)

            self.nx_graph.add_node(s_label, **properties)

        # Add hierarchical relationships
        for s, p, o in self.rdf_graph.triples((None, self.namespaces.PLANT_SCHEMA.subClassOf, None)):
            s_label = self.get_term_label(s)
            o_label = self.get_term_label(o)
            self.nx_graph.add_edge(o_label, s_label, relation_type='subClassOf')

        # Add all defined relationships
        for relation in self.relations:
            relation_name = str(relation).split('#')[-1]

            for s, _, o in self.rdf_graph.triples((None, relation, None)):
                s_label = self.get_term_label(s)
                o_label = self.get_term_label(o)
                self.nx_graph.add_edge(o_label, s_label, relation_type=relation_name)

        logger.info("Built Plant Ontology graph:")
        logger.info(f"- Nodes: {self.nx_graph.number_of_nodes()}")
        logger.info(f"- Edges: {self.nx_graph.number_of_edges()}")


    def extract_term_typings(self) -> List[TermTyping]:
        """
        Extract term typings from Plant Ontology.

        :return: list of term typings
        """
        term_typings = []

        for s, p, o in self.rdf_graph.triples((None, self.namespaces.RDF_SCHEMA.label, None)):
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
        Extract type taxonomies from Plant Ontology.

        :return: types, taxonomies
        """
        types: List[str] = []
        taxonomies: List[TaxonomyRelation] = []

        # Collect types using Plant Ontology specific classes
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.PLANT_SCHEMA.Class):
            type_label = self.get_term_label(s)
            if type_label:
                types.append(type_label)

        # Extract taxonomic relationships
        subclass_relation = self.namespaces.PLANT_SCHEMA.subClassOf
        for s, _, o in self.rdf_graph.triples((None, subclass_relation, None)):
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
        Extract non-taxonomic relations from Plant Ontology.

        :return: types, relations, non_taxonomic_relations
        """
        types: List[str] = []
        relations: List[str] = [str(rel).split('/')[-1] for rel in self.relations]
        non_taxonomic_relations: List[NonTaxonomicRelation] = []

        # Collect types
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.PLANT_SCHEMA.Class):
            type_label = self.get_term_label(s)
            if type_label:
                types.append(type_label)

        # Extract non-taxonomic relations
        for relation in self.relations:
            relation_label = str(relation).split('#')[-1]

            for s, _, o in self.rdf_graph.triples((None, relation, None)):
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
