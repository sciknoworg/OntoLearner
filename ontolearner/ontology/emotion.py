from rdflib import URIRef, BNode
from typing import List, Tuple, Set

from ..base import BaseOntology
from ..data_structure import TermTyping, TaxonomicRelation, NonTaxonomicRelation
from .. import logger

class EmotionOntology(BaseOntology):
    """
    Class for processing Mental Functioning Ontology of Emotions (MFOEM).

    This class implements specific processing logic for the Emotion Ontology,
    handling affective phenomena such as emotions and moods.
    """
    def build_graph(self) -> None:
        """
        Build graph representation of the Emotion Ontology structure
        TODO: refactor
            - move the function into the Base class
        """
        self.nx_graph.clear()

        # Get required namespaces
        rdfs = self.get_namespace('rdfs')
        rdf = self.get_namespace('rdf')
        owl = self.get_namespace('owl')
        obo = self.get_namespace('obo')

        # Add emotion classes and their properties
        for s in self.rdf_graph.subjects(rdf.type, owl.Class):
            if isinstance(s, (URIRef, BNode)):
                s_label = self.get_term_label(s)

                properties = {
                    'definition': None,
                    'examples': [],
                    'curation_status': None
                }

                # Get definition (IAO_0000115)
                definitions = list(self.rdf_graph.objects(s, obo['IAO_0000115']))
                if definitions:
                    properties['definition'] = str(definitions[0])

                # Get examples (IAO_0000112)
                examples = list(self.rdf_graph.objects(s, obo['IAO_0000112']))
                properties['examples'] = [str(ex) for ex in examples]

                # Get curation status (IAO_0000114)
                status = list(self.rdf_graph.objects(s, obo['IAO_0000114']))
                if status:
                    properties['curation_status'] = str(status[0])

                self.nx_graph.add_node(s_label, **properties)

        # Add hierarchical relationships (subClassOf)
        for s, _, o in self.rdf_graph.triples((None, rdfs.subClassOf, None)):
            s_label = self.get_term_label(s)
            o_label = self.get_term_label(o)
            if s_label and o_label:
                self.nx_graph.add_edge(o_label, s_label, relation_type='subClassOf')

        # Add emotion-specific relationships
        for relation in self.relations:
            relation_name = self.get_term_label(relation)

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

        # Get required namespaces
        rdfs = self.get_namespace('rdfs')
        rdf = self.get_namespace('rdf')
        mfoem = self.get_default_namespace()

        # Verify all required namespaces are available
        if not all([rdfs, rdf, mfoem]):
            logger.warning("Required namespaces (rdfs, rdf, mfoem) not found")
            return term_typings

        for s, p, o in self.rdf_graph.triples((None, rdfs.label, None)):
            term = str(o)
            types: Set[str] = set()

            # Get types from class hierarchy
            for _, _, type_uri in self.rdf_graph.triples((s, rdf.type, None)):
                if isinstance(type_uri, (URIRef, BNode)):
                    type_label = self.get_term_label(type_uri)
                    if type_label:
                        types.add(type_label)

            # Add emotional category if available
            emotional_predicate = mfoem['hasEmotionalCategory']
            for _, _, category in self.rdf_graph.triples((s, emotional_predicate, None)):
                if isinstance(category, (URIRef, BNode)):
                    category_label = self.get_term_label(category)
                    if category_label:
                        types.add(category_label)

            if types:
                # Append a validated TermTyping instance
                term_typings.append(TermTyping(term=term, types=list(types)))

        logger.debug(f"Extracted {len(term_typings)} term typings")

        return term_typings

    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomicRelation]]:
        """
        Extract type taxonomies from Emotion Ontology.

        :return: Tuple containing list of types and list of taxonomy relations
        """
        types: List[str] = []
        taxonomies: List[TaxonomicRelation] = []

        # Get required namespaces
        rdfs = self.get_namespace('rdfs')
        rdf = self.get_namespace('rdf')
        owl = self.get_namespace('owl')

        # Collect emotion types
        for s in self.rdf_graph.subjects(rdf.type, owl.Class):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

        # Extract subclass relationships
        for s, _, o in self.rdf_graph.triples((None, rdfs.subClassOf, None)):
            if isinstance(o, URIRef):
                superclass_label = self.get_term_label(o)
                subclass_label = self.get_term_label(s)

                if superclass_label and subclass_label:
                    # Append a validated TaxonomyRelation instance
                    taxonomies.append(
                        TaxonomicRelation(
                            parent=superclass_label,
                            child=subclass_label,
                        )
                    )

        return types, taxonomies

    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        """
        Extract non-taxonomic relations from Emotion Ontology.

        :return: emotion types and their non-hierarchical relationships.
        """
        types: List[str] = []
        relations: List[str] = [self.get_term_label(rel) for rel in self.relations]
        non_taxonomic_relations: List[NonTaxonomicRelation] = []

        rdf = self.get_namespace('rdf')
        owl = self.get_namespace('owl')

        # Collect emotion types
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
                        # Append a validated NonTaxonomicRelation instance
                        non_taxonomic_relations.append(
                            NonTaxonomicRelation(
                                head=head_label,
                                tail=tail_label,
                                relation=relation_label
                            )
                        )

        return types, relations, non_taxonomic_relations
