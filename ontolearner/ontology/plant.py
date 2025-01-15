
from rdflib import URIRef, Namespace
from ..base.ontology import BaseOntology
from ..models.schemas import TermTyping, TaxonomyRelation, NonTaxonomicRelation
from typing import List, Dict, Tuple


class PlantOntology(BaseOntology):
    def __init__(self):
        super().__init__()
        self.PLANT_SCHEMA = Namespace("http://purl.obolibrary.org/obo/po#")
        self.relations = [
            URIRef("http://www.w3.org/2004/02/skos/core#related"),
            URIRef("http://www.w3.org/2004/02/skos/core#broadMatch")
        ]

    def extract_term_typings(self) -> List[Dict]:
        """Extract term typings from Plant Ontology."""
        term_typings = []

        for s, p, o in self.graph.triples((None, self.RDF_SCHEMA.label, None)):
            term = str(o)
            types = set()

            for _, _, type_uri in self.graph.triples((s, self.RDF.type, None)):
                type_label = self.get_term_label(type_uri)
                if type_label:
                    types.add(type_label)

            if types:
                term_typings.append(
                    TermTyping(term=term, types=list(types)).model_dump()
                )

        return term_typings

    def extract_type_taxonomies(self) -> Tuple[List, List[Dict]]:
        """Extract type taxonomies from Plant Ontology."""
        types = []
        taxonomies = []

        # Collect types using Plant Ontology specific classes
        for s in self.graph.subjects(self.RDF.type, self.PLANT_SCHEMA.Class):
            type_label = self.get_term_label(s)
            if type_label:
                types.append(type_label)

        # Extract taxonomic relationships
        subclass_relation = self.PLANT_SCHEMA.subClassOf
        for s, _, o in self.graph.triples((None, subclass_relation, None)):
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
        """Extract non-taxonomic relations from Plant Ontology."""
        types = []
        relations = [str(rel).split('#')[-1] for rel in self.relations]
        non_taxonomic_relations = []

        # Collect types
        for s in self.graph.subjects(self.RDF.type, self.PLANT_SCHEMA.Class):
            type_label = self.get_term_label(s)
            if type_label:
                types.append(type_label)

        # Extract non-taxonomic relations
        for relation in self.relations:
            for s, _, o in self.graph.triples((None, relation, None)):
                head_label = self.get_term_label(s)
                tail_label = self.get_term_label(o)
                relation_label = str(relation).split('#')[-1]

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
