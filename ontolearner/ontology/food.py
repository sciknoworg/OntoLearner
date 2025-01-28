
from rdflib import URIRef, BNode
from typing import List, Tuple

from .. import logger

from ..base.ontology import BaseOntology
from ontolearner.data_structure.data import TermTyping, TaxonomicRelation, NonTaxonomicRelation


class FoodOntology(BaseOntology):
    """
    Class for processing Food Ontology (FoodOn).

    This class implements the specific processing logic for the FoodOn ontology,
    handling food-specific concepts, relationships, and properties.).
    """
    def __init__(self):
        """Initialize Food Ontology with specific namespaces and relations"""
        super().__init__()

        # TODO refactor -> don't define relations manually
        # Food-specific relations
        self.relations = [
            URIRef("http://purl.obolibrary.org/obo/RO_0001000"),  # derives_from
            URIRef("http://purl.obolibrary.org/obo/RO_0002234"),  # has_ingredient
            URIRef("http://purl.obolibrary.org/obo/BFO_0000050"),  # part_of
            URIRef("http://www.w3.org/2004/02/skos/core#related")  # related
        ]

    def build_graph(self) -> None:
        """
        Build a graph representation of the Food Ontology structure.
        Captures food classes, their properties, and relationships.
        TODO: refactor
            - move the function into the Base class
        """
        self.nx_graph.clear()

        rdfs = self.get_namespace('rdfs')
        rdf = self.get_namespace('rdf')
        owl = self.get_namespace('owl')

        # Add food classes and their properties
        for s in self.rdf_graph.subjects(rdf.type, owl.Class):
            s_label = self.get_term_label(s)

            # Collect properties
            properties = {
                'definition': None,
                'examples': [],
                'curation_status': None,
                'source': None
            }

            # Get definition
            definitions = list(self.rdf_graph.objects(s, self.namespaces.IAO['0000115']))
            if definitions:
                properties['definition'] = str(definitions[0])

            # Get examples
            examples = list(self.rdf_graph.objects(s, self.namespaces.IAO['0000112']))
            properties['examples'] = [str(ex) for ex in examples]

            # Get curation status
            status = list(self.rdf_graph.objects(s, self.namespaces.IAO['0000114']))
            if status:
                properties['curation_status'] = str(status[0])

            # Get source references
            sources = list(self.rdf_graph.objects(s, self.namespaces.IAO['0000119']))
            if sources:
                properties['source'] = str(sources[0])

            self.nx_graph.add_node(s_label, **properties)

        # Add hierarchical relationships
        for s, _, o in self.rdf_graph.triples((None, rdfs.subClassOf, None)):
            if isinstance(o, URIRef):  # Skip blank nodes
                s_label = self.get_term_label(s)
                o_label = self.get_term_label(o)
                if s_label and o_label:
                    self.nx_graph.add_edge(o_label, s_label, relation_type='subClassOf')

        # Add food-specific relationships
        for relation in self.relations:
            relation_name = self.get_term_label(relation)

            for s, _, o in self.rdf_graph.triples((None, relation, None)):
                s_label = self.get_term_label(s)
                o_label = self.get_term_label(o)

                if s_label and o_label:
                    self.nx_graph.add_edge(s_label, o_label, relation_type=relation_name)

        logger.info(f"Built Food Ontology graph with {self.nx_graph.number_of_nodes()} nodes "
                    f"and {self.nx_graph.number_of_edges()} edges")


    def extract_term_typings(self) -> List[TermTyping]:
        """
        Extract term typings from Food Ontology.
        Maps food items to their types/categories.
        """
        term_typings = []

        rdfs = self.get_namespace('rdfs')
        rdf = self.get_namespace('rdf')
        foodon = self.get_default_namespace()

        for s, p, o in self.rdf_graph.triples((None, rdfs.label, None)):
            term = str(o)
            types = set()

            # Get types from class hierarchy
            for _, _, type_uri in self.rdf_graph.triples((s, rdf.type, None)):
                if isinstance(type_uri, (URIRef, BNode)):
                    type_label = self.get_term_label(type_uri)
                    if type_label:
                        types.add(type_label)

            # Add food categories
            for _, _, category in self.rdf_graph.triples((s, foodon.hasCategory, None)):
                if isinstance(category, (URIRef, BNode)):
                    category_label = self.get_term_label(category)
                    if category_label:
                        types.add(category_label)

            if types:
                # Append a validated TermTyping instance
                term_typings.append(TermTyping(term=term, types=list(types)))

        return term_typings


    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomicRelation]]:
        """
        Extract type taxonomies from Food Ontology.

        :return: Tuple containing list of types and list of taxonomy relations
        """
        types: List[str] = []
        taxonomies: List[TaxonomicRelation] = []

        rdfs = self.get_namespace('rdfs')
        rdf = self.get_namespace('rdf')
        owl = self.get_namespace('owl')

        # Collect food types
        for s in self.rdf_graph.subjects(rdf.type, owl.Class):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

        # Extract subclass relationships
        for s, _, o in self.rdf_graph.triples((None, rdfs.subClassOf, None)):
            if isinstance(o, URIRef):  # Skip blank nodes
                superclass_label = self.get_term_label(o)
                subclass_label = self.get_term_label(s)

                if superclass_label and subclass_label:
                    # Add direct subclass relationship
                    taxonomies.append(
                        TaxonomicRelation(
                            parent=superclass_label,
                            child=subclass_label
                        )
                    )

        return types, taxonomies


    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        """
        Extract non-taxonomic relations from Food Ontology.

        :return: Tuple containing (types list, relations list, non-taxonomic relations list)
        """
        types: List[str] = []
        relations: List[str] = [self.get_term_label(rel) for rel in self.relations]
        non_taxonomic_relations: List[NonTaxonomicRelation] = []

        rdf = self.get_namespace('rdf')
        owl = self.get_namespace('owl')

        # Collect food types
        for s in self.rdf_graph.subjects(rdf.type, owl.Class):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

        # Extract defined relationships
        for relation in self.relations:
            relation_label = self.get_term_label(relation)

            for s, _, o in self.rdf_graph.triples((None, relation, None)):
                if isinstance(s, (URIRef, BNode)) and isinstance(o, (URIRef, BNode)):
                    head_label = self.get_term_label(s)
                    tail_label = self.get_term_label(o)

                    if head_label and tail_label:
                        non_taxonomic_relations.append(
                            NonTaxonomicRelation(
                                head=head_label,
                                tail=tail_label,
                                relation=relation_label
                            )
                        )

        return types, relations, non_taxonomic_relations
