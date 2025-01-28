
from typing import List, Tuple

from ..base.ontology import BaseOntology
from ontolearner.data_structure.data import NonTaxonomicRelation



class PlantOntology(BaseOntology):
    """
    Class for processing Plant Ontology.
    """
    def __init__(self, **kwargs):
        """
        Initialize the Plant Ontology.
        """
        super().__init__(**kwargs)

    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        """
        Extract non-taxonomic relations from Plant Ontology.

        :return: types, relations, non_taxonomic_relations
        """
        types: List[str] = []
        relations: List[str] = [self.get_term_label(rel) for rel in self.relations]
        non_taxonomic_relations: List[NonTaxonomicRelation] = []

        rdf = self.get_namespace('rdf')
        owl = self.get_namespace('owl')

        # Collect types
        for s in self.rdf_graph.subjects(rdf.type, owl.Class):
            type_label = self.get_term_label(s)
            if type_label:
                types.append(type_label)

        # Extract non-taxonomic relations
        for relation in self.relations:
            relation_label = self.get_term_label(relation)

            for s, _, o in self.rdf_graph.triples((None, relation, None)):
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
