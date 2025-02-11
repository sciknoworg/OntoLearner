from typing import Tuple, List
from rdflib import RDFS, RDF, OWL

from ..base import BaseOntology
from ..data_structure import NonTaxonomicRelation


class BFO(BaseOntology):
    """Processes Basic Formal Ontology with BFO-specific behavior."""
    ontology_full_name = "Basic Formal Ontology"

    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        types_set = set()
        relations_set = set()
        non_taxonomic_pairs = []

        # Iterate over all ObjectProperties
        for prop in self.rdf_graph.subjects(RDF.type, OWL.ObjectProperty):
            prop_label = self.get_label(str(prop))
            if not prop_label:
                continue

            # Get domain and range
            domain = next(self.rdf_graph.objects(prop, RDFS.domain), None)
            range_ = next(self.rdf_graph.objects(prop, RDFS.range), None)

            if domain and range_:
                domain_label = self.get_label(str(domain))
                range_label = self.get_label(str(range_))
                if domain_label and range_label:
                    non_taxonomic_pairs.append(
                        NonTaxonomicRelation(
                            head=domain_label,
                            tail=range_label,
                            relation=prop_label
                        )
                    )
                    types_set.update([domain_label, range_label])
                    relations_set.add(prop_label)

        types = sorted(types_set)
        relations = sorted(relations_set)
        return types, relations, non_taxonomic_pairs


class GFO(BaseOntology):
    ontology_full_name = "General Formal Ontology"


class DOLCE(BaseOntology):
    ontology_full_name = "Descriptive Ontology for Linguistic and Cognitive Engineering"
