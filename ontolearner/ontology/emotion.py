
from rdflib import URIRef, Namespace
from typing import List, Dict, Tuple

from ..base.ontology import BaseOntology
from ..base.data_model import TermTyping, TaxonomyRelation, NonTaxonomicRelation


class EmotionOntology(BaseOntology):
    """
    Class for processing Mental Functioning Ontology of Emotions (MFOEM).
    This ontology captures affective phenomena such as emotions and moods.
    """
    def __init__(self):
        """
        Initialize the Emotion Ontology.
        Sets up namespaces and relations specific to MFOEM.
        """
        super().__init__()

        # MFOEM specific namespaces
        self.MFOEM_SCHEMA = Namespace("http://purl.obolibrary.org/obo/MFOEM#")
        self.OBO = Namespace("http://purl.obolibrary.org/obo/")
        self.IAO = Namespace("http://purl.obolibrary.org/obo/IAO_")

        # Emotion-specific relations
        self.relations = [
            URIRef("http://purl.obolibrary.org/obo/BFO_0000050"),  # part_of
            URIRef("http://purl.obolibrary.org/obo/RO_0000053"),   # has_characteristic
            URIRef("http://purl.obolibrary.org/obo/RO_0000057")    # has_participant
        ]

    def build_graph(self) -> None:
        """
        Build a comprehensive graph representation of the Emotion Ontology structure.
        Captures emotion classes, their properties, and relationships.
        """
        self.nx_graph.clear()

        # Add emotion classes and their properties
        for s in self.rdf_graph.subjects(self.RDF.type, self.OWL.Class):
            s_label = self.get_term_label(s)

            # Collect properties including definitions and examples
            properties = {
                'definition': None,
                'examples': [],
                'curation_status': None
            }

            # Get definition (IAO_0000115)
            definitions = list(self.rdf_graph.objects(s, self.IAO['0000115']))
            if definitions:
                properties['definition'] = str(definitions[0])

            # Get examples (IAO_0000112)
            examples = list(self.rdf_graph.objects(s, self.IAO['0000112']))
            properties['examples'] = [str(ex) for ex in examples]

            # Get curation status (IAO_0000114)
            status = list(self.rdf_graph.objects(s, self.IAO['0000114']))
            if status:
                properties['curation_status'] = str(status[0])

            self.nx_graph.add_node(s_label, **properties)

        # Add hierarchical relationships (subClassOf)
        for s, _, o in self.rdf_graph.triples((None, self.RDF_SCHEMA.subClassOf, None)):
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


    def extract_term_typings(self) -> List[Dict]:
        """
        Extract term typings from Emotion Ontology.
        Returns term-type mappings for emotions and related concepts.
        """
        term_typings = []

        for s, p, o in self.rdf_graph.triples((None, self.RDF_SCHEMA.label, None)):
            term = str(o)
            types = set()

            # Get types from class hierarchy
            for _, _, type_uri in self.rdf_graph.triples((s, self.RDF.type, None)):
                type_label = self.get_term_label(type_uri)
                if type_label:
                    types.add(type_label)

            # Add emotional category if available
            for _, _, category in self.rdf_graph.triples((s, self.MFOEM_SCHEMA.hasEmotionalCategory, None)):
                category_label = self.get_term_label(category)
                if category_label:
                    types.add(category_label)

            if types:
                term_typings.append(
                    TermTyping(term=term, types=list(types)).model_dump()
                )

        return term_typings

    def extract_type_taxonomies(self) -> Tuple[List, List[Dict]]:
        """
        Extract type taxonomies from Emotion Ontology.
        Returns emotion types and their hierarchical relationships.
        """
        types = []
        taxonomies = []

        # Collect emotion types
        for s in self.rdf_graph.subjects(self.RDF.type, self.OWL.Class):
            type_label = self.get_term_label(s)
            if type_label:
                types.append(type_label)

        # Extract subclass relationships
        for s, _, o in self.rdf_graph.triples((None, self.RDF_SCHEMA.subClassOf, None)):
            superclass_label = self.get_term_label(o)
            subclass_label = self.get_term_label(s)

            if superclass_label and subclass_label:
                taxonomies.append(
                    TaxonomyRelation(
                        term1=superclass_label,
                        term2=subclass_label,
                        relation=True,
                        relationship_type="direct"
                    ).model_dump()
                )

        return types, taxonomies

    def extract_type_non_taxonomic_relations(self) -> Tuple[List, List, List[Dict]]:
        """
        Extract non-taxonomic relations from Emotion Ontology.
        Returns emotion types and their non-hierarchical relationships.
        """
        types = []
        relations = [str(rel).split('/')[-1] for rel in self.relations]
        non_taxonomic_relations = []

        # Collect emotion types
        for s in self.rdf_graph.subjects(self.RDF.type, self.OWL.Class):
            type_label = self.get_term_label(s)
            if type_label:
                types.append(type_label)

        # Extract defined relationships
        for relation in self.relations:
            relation_label = str(relation).split('/')[-1]
            for s, _, o in self.rdf_graph.triples((None, relation, None)):
                head_label = self.get_term_label(s)
                tail_label = self.get_term_label(o)

                if head_label and tail_label:
                    non_taxonomic_relations.append(
                        NonTaxonomicRelation(
                            head=head_label,
                            tail=tail_label,
                            relation=relation_label,
                            valid=True
                        ).model_dump()
                    )

        return types, relations, non_taxonomic_relations
