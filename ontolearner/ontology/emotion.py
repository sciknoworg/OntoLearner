
from dataclasses import dataclass
from rdflib import URIRef, Namespace, BNode
from typing import List, Tuple, Set
import logging

from ..base.ontology import BaseOntology, OntologyNamespaces
from ..base.data_model import TermTyping, TaxonomyRelation, NonTaxonomicRelation

logger = logging.getLogger(__name__)


@dataclass
class EmotionOntologyNamespaces(OntologyNamespaces):
    """Extended namespaces for Mental Functioning Ontology of Emotions (MFOEM)"""
    MFOEM_SCHEMA: Namespace = Namespace("http://purl.obolibrary.org/obo/MFOEM#")
    OBO: Namespace = Namespace("http://purl.obolibrary.org/obo/")
    IAO: Namespace = Namespace("http://purl.obolibrary.org/obo/IAO_")


class EmotionOntology(BaseOntology):
    """
    Class for processing Mental Functioning Ontology of Emotions (MFOEM).

    This class implements specific processing logic for the Emotion Ontology,
    handling affective phenomena such as emotions and moods.
    """
    def __init__(self):
        """
        Initialize the Emotion Ontology.
        Sets up namespaces and relations specific to MFOEM.
        """
        super().__init__()
        self.namespaces = EmotionOntologyNamespaces()

        # Emotion-specific relations
        self.relations = [
            URIRef("http://purl.obolibrary.org/obo/BFO_0000050"),  # part_of
            URIRef("http://purl.obolibrary.org/obo/RO_0000053"),   # has_characteristic
            URIRef("http://purl.obolibrary.org/obo/RO_0000057")    # has_participant
        ]

    def build_graph(self) -> None:
        """Build graph representation of the Emotion Ontology structure"""
        self.nx_graph.clear()

        # Add emotion classes and their properties
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.OWL.Class):
            if isinstance(s, (URIRef, BNode)):
                s_label = self.get_term_label(s)

                properties = {
                    'definition': None,
                    'examples': [],
                    'curation_status': None
                }

                # Get definition (IAO_0000115)
                definitions = list(self.rdf_graph.objects(s, self.namespaces.IAO['0000115']))
                if definitions:
                    properties['definition'] = str(definitions[0])

                # Get examples (IAO_0000112)
                examples = list(self.rdf_graph.objects(s, self.namespaces.IAO['0000112']))
                properties['examples'] = [str(ex) for ex in examples]

                # Get curation status (IAO_0000114)
                status = list(self.rdf_graph.objects(s, self.namespaces.IAO['0000114']))
                if status:
                    properties['curation_status'] = str(status[0])

                self.nx_graph.add_node(s_label, **properties)

        # Add hierarchical relationships (subClassOf)
        for s, _, o in self.rdf_graph.triples((None, self.namespaces.RDF_SCHEMA.subClassOf, None)):
            s_label = self.get_term_label(s)
            o_label = self.get_term_label(o)
            if s_label and o_label:
                self.nx_graph.add_edge(o_label, s_label, relation_type='subClassOf')

        # Add emotion-specific relationships
        for relation in self.relations:
            relation_name = str(relation).split('/')[-1]
            for s, _, o in self.rdf_graph.triples((None, relation, None)):
                s_label = self.get_term_label(s)
                o_label = self.get_term_label(o)
                if s_label and o_label:
                    self.nx_graph.add_edge(s_label, o_label, relation_type=relation_name)

        logger.info(f"Built Emotion Ontology graph with {self.nx_graph.number_of_nodes()} "
                    f"nodes and {self.nx_graph.number_of_edges()} edges")


    def extract_term_typings(self) -> List[TermTyping]:
        """
        Extract term typings from Emotion Ontology.

        :return: term-type mappings for emotions and related concepts.
        """
        term_typings = []

        for s, p, o in self.rdf_graph.triples((None, self.namespaces.RDF_SCHEMA.label, None)):
            term = str(o)
            types: Set[str] = set()

            # Get types from class hierarchy
            for _, _, type_uri in self.rdf_graph.triples((s, self.namespaces.RDF.type, None)):
                if isinstance(type_uri, (URIRef, BNode)):
                    type_label = self.get_term_label(type_uri)
                    if type_label:
                        types.add(type_label)

            # Add emotional category if available
            for _, _, category in self.rdf_graph.triples((s, self.namespaces.MFOEM_SCHEMA.hasEmotionalCategory, None)):
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
        Extract type taxonomies from Emotion Ontology.

        :return: Tuple containing list of types and list of taxonomy relations
        """
        types: List[str] = []
        taxonomies: List[TaxonomyRelation] = []

        # Collect emotion types
        for s in self.rdf_graph.subjects(self.namespaces.RDF.type, self.namespaces.OWL.Class):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

        # Extract subclass relationships
        for s, _, o in self.rdf_graph.triples((None, self.namespaces.RDF_SCHEMA.subClassOf, None)):
            if isinstance(o, URIRef):
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
        Extract non-taxonomic relations from Emotion Ontology.

        :return: emotion types and their non-hierarchical relationships.
        """
        types: List[str] = []
        relations: List[str] = [str(rel).split('/')[-1] for rel in self.relations]
        non_taxonomic_relations: List[NonTaxonomicRelation] = []

        # Collect emotion types
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
