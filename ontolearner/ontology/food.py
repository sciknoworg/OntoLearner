
from dataclasses import dataclass
from rdflib import URIRef, Namespace, BNode
from typing import List, Tuple
import logging

from ..base.ontology import BaseOntology, OntologyNamespaces
from ..base.data_model import TermTyping, TaxonomyRelation, NonTaxonomicRelation

logger = logging.getLogger(__name__)


@dataclass
class FoodOntologyNamespaces(OntologyNamespaces):
    """Extended namespaces for Food Ontology"""
    FOODON_SCHEMA: Namespace = Namespace("http://purl.obolibrary.org/obo/foodon#")
    OBO: Namespace = Namespace("http://purl.obolibrary.org/obo/")
    IAO: Namespace = Namespace("http://purl.obolibrary.org/obo/IAO_")
    CHEBI: Namespace = Namespace("http://purl.obolibrary.org/obo/chebi/")


class FoodOntology(BaseOntology):
    """
    Class for processing Food Ontology (FoodOn).

    This class implements the specific processing logic for the FoodOn ontology,
    handling food-specific concepts, relationships, and properties.).
    """
    def __init__(self):
        """Initialize Food Ontology with specific namespaces and relations"""
        super().__init__()
        self.namespaces = FoodOntologyNamespaces()

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
        """
        self.nx_graph.clear()

        # Add food classes and their properties
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.OWL.Class):
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
        for s, _, o in self.rdf_graph.triples((None, self.namespaces.RDF_SCHEMA.subClassOf, None)):
            if isinstance(o, URIRef):  # Skip blank nodes
                s_label = self.get_term_label(s)
                o_label = self.get_term_label(o)
                if s_label and o_label:
                    self.nx_graph.add_edge(o_label, s_label, relation_type='subClassOf')

        # Add food-specific relationships
        for relation in self.relations:
            relation_name = str(relation).split('/')[-1]
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

        for s, p, o in self.rdf_graph.triples((None, self.namespaces.RDF_SCHEMA.label, None)):
            term = str(o)
            types = set()

            # Get types from class hierarchy
            for _, _, type_uri in self.rdf_graph.triples((s, self.namespaces.RDF.type, None)):
                if isinstance(type_uri, (URIRef, BNode)):
                    type_label = self.get_term_label(type_uri)
                    if type_label:
                        types.add(type_label)

            # Add food categories
            for _, _, category in self.rdf_graph.triples((s, self.namespaces.FOODON_SCHEMA.hasCategory, None)):
                if isinstance(category, (URIRef, BNode)):
                    category_label = self.get_term_label(category)
                    if category_label:
                        types.add(category_label)

            if types:
                # Append a validated TermTyping instance
                term_typings.append(TermTyping(term=term, types=list(types)))

        return term_typings


    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomyRelation]]:
        """
        Extract type taxonomies from Food Ontology.

        :return: Tuple containing list of types and list of taxonomy relations
        """
        types: List[str] = []
        taxonomies: List[TaxonomyRelation] = []

        # Collect food types
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.OWL.Class):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

        # Extract subclass relationships
        for s, _, o in self.rdf_graph.triples((None, self.namespaces.RDF_SCHEMA.subClassOf, None)):
            if isinstance(o, URIRef):  # Skip blank nodes
                superclass_label = self.get_term_label(o)
                subclass_label = self.get_term_label(s)

                if superclass_label and subclass_label:
                    # Add direct subclass relationship
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
        Extract non-taxonomic relations from Food Ontology.

        :return: Tuple containing (types list, relations list, non-taxonomic relations list)
        """
        types: List[str] = []
        relations: List[str] = [str(rel).split('/')[-1] for rel in self.relations]
        non_taxonomic_relations: List[NonTaxonomicRelation] = []

        # Collect food types
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.OWL.Class):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

        # Extract defined relationships
        for relation in self.relations:
            relation_label = str(relation).split('/')[-1]

            for s, _, o in self.rdf_graph.triples((None, relation, None)):
                if isinstance(s, (URIRef, BNode)) and isinstance(o, (URIRef, BNode)):
                    head_label = self.get_term_label(s)
                    tail_label = self.get_term_label(o)

                    if head_label and tail_label:
                        non_taxonomic_relations.append(
                            NonTaxonomicRelation(
                                head=head_label,
                                tail=tail_label,
                                relation=relation_label,
                                valid=True
                            )
                        )

        return types, relations, non_taxonomic_relations
