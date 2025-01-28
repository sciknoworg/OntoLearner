
from rdflib import URIRef, BNode
from typing import List, Tuple

from ..base.ontology import BaseOntology
from ontolearner.data_structure.data import TermTyping, TaxonomicRelation, NonTaxonomicRelation

from .. import logger


class LifeOntology(BaseOntology):
    """Class for processing Life Ontology (LifO)."""

    def __init__(self):
        super().__init__()

        # TODO refactor -> don't define relations manually
        self.relations = [
            URIRef("http://purl.obolibrary.org/obo/BFO_0000050"),  # part_of
            URIRef("http://purl.obolibrary.org/obo/RO_0002202"),   # develops_from
            URIRef("http://purl.obolibrary.org/obo/RO_0002211"),   # regulates
            URIRef("http://purl.obolibrary.org/obo/RO_0002215"),    # capable_of
            URIRef("http://purl.obolibrary.org/obo/BFO_0000051"),  # has_part
            URIRef("http://purl.obolibrary.org/obo/RO_0002213"),  # positively_regulates
            URIRef("http://purl.obolibrary.org/obo/RO_0002212")  # negatively_regulates
        ]


    def build_graph(self) -> None:
        """
        Build graph representation of the Life Ontology structure
        TODO: refactor
            - move the function into the Base class
        """
        self.nx_graph.clear()

        rdf = self.get_namespace('rdf')
        owl = self.get_namespace('owl')

        # Add life process classes and their properties
        for s in self.rdf_graph.subjects(rdf.type, owl.Class):
            if isinstance(s, (URIRef, BNode)):
                s_label = self.get_term_label(s)
                properties = self._extract_node_properties(s)
                self.nx_graph.add_node(s_label, **properties)

        self._add_hierarchical_relationships()
        self._add_life_specific_relationships()

        logger.info(f"Built Life Ontology graph with {self.nx_graph.number_of_nodes()} nodes "
                    f"and {self.nx_graph.number_of_edges()} edges")


    def extract_term_typings(self) -> List[TermTyping]:
        """Extract term typings for life processes"""
        term_typings = []

        rdfs = self.get_namespace('rdfs')
        rdf = self.get_namespace('rdf')

        for s, p, o in self.rdf_graph.triples((None, rdfs.label, None)):
            term = str(o)
            types = set()

            for _, _, type_uri in self.rdf_graph.triples((s, rdf.type, None)):
                if isinstance(type_uri, (URIRef, BNode)):
                    type_label = self.get_term_label(type_uri)
                    if type_label:
                        types.add(type_label)

            if types:
                term_typings.append(TermTyping(term=term, types=list(types)))

        return term_typings


    def extract_type_taxonomies(self) -> Tuple[List[str], List[TaxonomicRelation]]:
        """Extract type taxonomies from Life Ontology"""
        types: List[str] = []
        taxonomies: List[TaxonomicRelation] = []

        rdfs = self.get_namespace('rdfs')
        rdf = self.get_namespace('rdf')
        owl = self.get_namespace('owl')

        for s in self.rdf_graph.subjects(rdf.type, owl.Class):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

        for s, _, o in self.rdf_graph.triples((None, rdfs.subClassOf, None)):
            if isinstance(o, (URIRef, BNode)):
                superclass_label = self.get_term_label(o)
                subclass_label = self.get_term_label(s)

                if superclass_label and subclass_label:
                    taxonomies.append(
                        TaxonomicRelation(
                            parent=superclass_label,
                            child=subclass_label,
                        )
                    )

        return types, taxonomies


    def extract_type_non_taxonomic_relations(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        """Extract non-taxonomic relations from Life Ontology"""
        types: List[str] = []
        relations: List[str] = [self.get_term_label(rel) for rel in self.relations]
        non_taxonomic_relations: List[NonTaxonomicRelation] = []

        rdf = self.get_namespace('rdf')
        owl = self.get_namespace('owl')

        for s in self.rdf_graph.subjects(rdf.type, owl.Class):
            if isinstance(s, (URIRef, BNode)):
                type_label = self.get_term_label(s)
                if type_label:
                    types.append(type_label)

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
                                relation=relation_label,
                            )
                        )

        return types, relations, non_taxonomic_relations


    def extract_term_typings_sparql(self) -> List[TermTyping]:
        query = """
        SELECT DISTINCT ?term (GROUP_CONCAT(DISTINCT ?type; separator="|") as ?types)
        WHERE {
            ?s rdfs:label ?term .
            ?s rdf:type ?typeUri .
            ?typeUri rdfs:label ?type .
            FILTER(isIRI(?typeUri))
        }
        GROUP BY ?term
        """
        results = self.rdf_graph.query(query)
        return [TermTyping(term=str(row.term), types=str(row.types).split("|"))
                for row in results]


    def extract_type_taxonomies_sparql(self) -> Tuple[List[str], List[TaxonomicRelation]]:
        # Get types
        type_query = """
       SELECT DISTINCT ?type
       WHERE {
           ?s rdf:type owl:Class ;
              rdfs:label ?type .
       }
       """
        types = [str(row.type) for row in self.rdf_graph.query(type_query)]

        # Get taxonomy relations
        tax_query = """
       SELECT DISTINCT ?superclass ?subclass
       WHERE {
           ?s rdfs:subClassOf ?o ;
              rdfs:label ?subclass .
           ?o rdfs:label ?superclass .
           FILTER(isIRI(?o))
       }
       """
        taxonomies = [
            TaxonomicRelation(
                parent=str(row.superclass),
                child=str(row.subclass)
            )
            for row in self.rdf_graph.query(tax_query)
        ]

        return types, taxonomies


    def extract_type_non_taxonomic_relations_sparql(self) -> Tuple[List[str], List[str], List[NonTaxonomicRelation]]:
        types = [str(row.type) for row in self.rdf_graph.query("""
           SELECT DISTINCT ?type
           WHERE {
               ?s rdf:type owl:Class ;
                  rdfs:label ?type .
           }
       """)]

        relations = [str(rel).split('/')[-1] for rel in self.relations]

        # Build VALUES clause for relations
        values_str = " ".join(f"<{r}>" for r in self.relations)

        non_tax_query = f"""
       SELECT DISTINCT ?head ?tail ?relation
       WHERE {{
           VALUES ?relationType {{ {values_str} }}
           ?s ?relationType ?o .
           ?s rdfs:label ?head .
           ?o rdfs:label ?tail .
           BIND(STRAFTER(STR(?relationType), "obo/") AS ?relation)
       }}
       """

        non_taxonomic_relations = [
            NonTaxonomicRelation(
                head=str(row.head),
                tail=str(row.tail),
                relation=str(row.relation)
            )
            for row in self.rdf_graph.query(non_tax_query)
        ]

        return types, relations, non_taxonomic_relations


    def _extract_node_properties(self, node: URIRef) -> dict:
        """Extract properties for a life process node"""
        properties = {
            'definition': None,
            'examples': [],
            'status': None,
            'comment': None
        }

        # Get definition
        definitions = list(self.rdf_graph.objects(node, self.namespaces.IAO['0000115']))
        if definitions:
            properties['definition'] = str(definitions[0])

        # Get examples
        examples = list(self.rdf_graph.objects(node, self.namespaces.IAO['0000112']))
        properties['examples'] = [str(ex) for ex in examples]

        # Get status
        status = list(self.rdf_graph.objects(node, self.namespaces.IAO['0000114']))
        if status:
            properties['status'] = str(status[0])

        return properties


    def _add_hierarchical_relationships(self) -> None:
        """Add hierarchical relationships between life processes"""

        rdfs = self.get_namespace('rdfs')

        for s, _, o in self.rdf_graph.triples((None, rdfs.subClassOf, None)):
            if isinstance(o, URIRef):
                s_label = self.get_term_label(s)
                o_label = self.get_term_label(o)

                if s_label and o_label:
                    self.nx_graph.add_edge(o_label, s_label, relation_type='subClassOf')


    def _add_life_specific_relationships(self) -> None:
        """Add life-specific relationships"""
        for relation in self.relations:
            relation_name = self.get_term_label(relation)

            for s, _, o in self.rdf_graph.triples((None, relation, None)):
                if isinstance(s, (URIRef, BNode)) and isinstance(o, (URIRef, BNode)):
                    s_label = self.get_term_label(s)
                    o_label = self.get_term_label(o)

                    if s_label and o_label:
                        self.nx_graph.add_edge(s_label, o_label, relation_type=relation_name)
