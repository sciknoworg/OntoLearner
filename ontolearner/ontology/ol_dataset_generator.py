
from rdflib import Graph, Namespace, URIRef, RDF
from typing import Dict, List, Set
import random
import logging

from ontolearner.utils.utils import save_dataset

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class OntologyLearningDatasetGenerator:
    def __init__(self, rdf_file: str = None, sparql_endpoint: str = None):
        """
        Initialize with either an RDF file or SPARQL endpoint.

        :arg:
            rdf_file: Path to RDF/OWL file
            sparql_endpoint: URL of SPARQL endpoint
        """
        self.g = Graph()
        self.endpoint = None

        if rdf_file:
            logger.info(f"Loading ontology from RDF file: {rdf_file}")
            self.g.parse(rdf_file, format="xml")
            logging.info(f"Loaded {len(self.g)} triples")
        elif sparql_endpoint:
            self.endpoint = sparql_endpoint
            logging.info(f"Using SPARQL endpoint: {sparql_endpoint}")

        # Common namespaces
        # self.CSO_SCHEMA = Namespace("http://cso.kmi.open.ac.uk/schema/cso#")
        self.RDF_SCHEMA = Namespace("http://www.w3.org/2000/01/rdf-schema#")
        self.SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

    ####################################################################################################
    # Dataset Generation Functions
    ####################################################################################################
    def generate_term_typing_dataset(self, sample_size: int = 100) -> List[Dict]:
        """
        Generates dataset for Task A - Term Typing.

        :param:  sample_size (int): Maximum number of samples to include in the dataset
        :return: List[Dict]: Training dataset, containing dictionary with 'term' and 'type' keys
        """
        logger.info("Starting term typing dataset generation")

        term_type_pairs = []

        # Get all terms with labels and their types
        for s, p, o in self.g.triples((None, self.RDF_SCHEMA.label, None)):
            term = str(o)

            # Find types for this term by traversing up the hierarchy
            types = set()
            for _, _, type_uri in self.g.triples((s, RDF.type, None)):
                type_label = self.get_term_label(type_uri)
                if type_label:
                    types.add(type_label)

            if types:
                term_type_pairs.append({
                    "term": term,
                    "types": list(types)
                })

        logger.info(f"Generated {len(term_type_pairs)} term-types pairs")

        # Apply sampling if needed
        if len(term_type_pairs) > sample_size > 0:
            logger.info(f"Sampling {sample_size} pairs from total {len(term_type_pairs)}")
            term_type_pairs = random.sample(term_type_pairs, sample_size)

        logger.info(f"Final dataset: {len(term_type_pairs)} training samples\n")

        return term_type_pairs


    def generate_taxonomy_dataset(self, sample_size: int = 100) -> List[Dict]:
        """
         Generate dataset for Task B - Taxonomy Discovery.

        :param sample_size:
        :return:
        """
        logger.info("Starting taxonomy dataset generation")

        # Pre-compute topic labels to avoid repeated queries
        taxonomy_pairs = []

        # Find direct relationships using cached labels
        for s, _, o in self.g.triples((None, self.RDF_SCHEMA.subClassOf, None)):
            superclass_label = self.get_term_label(o)
            subclass_label = self.get_term_label(s)

            if superclass_label and subclass_label:
                taxonomy_pairs.append({
                    "term1": superclass_label,
                    "term2": subclass_label,
                    "relation": True
                })

                # Add transitive relationships
                for _, _, grandchild in self.g.triples((o, self.RDF_SCHEMA.subClassOf, None)):
                    grandchild_label = self.get_term_label(grandchild)
                    if grandchild_label:
                        taxonomy_pairs.append({
                            "term1": grandchild_label,
                            "term2": subclass_label,
                            "relation": True
                        })

        logger.info(f"Found {len(taxonomy_pairs)} direct taxonomy relationships")

        # Early sampling for transitive relationships if sample_size is small
        if sample_size and len(taxonomy_pairs) > sample_size:
            taxonomy_pairs = random.sample(taxonomy_pairs, sample_size)
            logger.info(f"Sampled {sample_size} pairs from total {len(taxonomy_pairs)}")

        logger.info(f"Final dataset: {len(taxonomy_pairs)} training samples\n")

        return taxonomy_pairs


    def generate_relation_dataset(self, relations: List[URIRef], sample_size: int = 100) -> List[Dict]:
        """
        Generate dataset for Task C - Non-taxonomic Relation Extraction.

        Args:
            relations: List of relation URIs to include
            sample_size: Number of samples to generate
        """
        relation_pairs = []

        # Find all instances of specified relations
        for relation in relations:
            for s, _, o in self.g.triples((None, relation, None)):
                head_label = self.get_term_label(s)
                tail_label = self.get_term_label(o)
                relation_label = self.get_term_label(relation)

                if head_label and tail_label:
                    relation_pairs.append({
                        "head": head_label,
                        "tail": tail_label,
                        "relation": relation_label
                    })

        # Apply sampling if needed
        if sample_size and len(relation_pairs) > sample_size:
            relation_pairs = (random.sample(relation_pairs, sample_size))

        return relation_pairs

    ####################################################################################################
    # Helper functions for ontology traversal and analysis
    ####################################################################################################
    def get_term_label(self, uri: URIRef) -> str:
        """
        Get human-readable label for a term.
        """
        labels = list(self.g.objects(subject=uri, predicate=self.RDF_SCHEMA.label))

        if not labels:
            # Try SKOS label if RDF label not found
            labels = list(self.g.objects(subject=uri, predicate=self.SKOS.prefLabel))

        return str(labels[0]) if labels else str(uri).split('/')[-1]


    def explore_term_hierarchy(self, term: str, max_depth: int = 10) -> None:
        """
        Explores and displays the complete ancestor hierarchy for a given term.
        Shows the path(s) from the term to its top-level ancestors, helping debug type assignment.

        Args:
            term (str): The term to explore (e.g., "transceivers")
            max_depth (int): Maximum depth to prevent infinite recursion in case of cycles
        """
        logger.info(f"Exploring hierarchy for term: '{term}'")

        # First, find the URI for this term by looking up its label
        term_uri = None
        for s, p, o in self.g.triples((None, self.RDF_SCHEMA.label, None)):
            if str(o).lower() == term.lower():
                term_uri = s
                break

        if not term_uri:
            logger.error(f"Term '{term}' not found in the ontology")
            return

        def print_hierarchy(uri: URIRef, depth: int = 0, visited: set = None) -> bool:
            """
            Recursively prints the hierarchy with proper indentation.
            Returns True if this branch leads to a top-level topic.
            """
            if visited is None:
                visited = set()

            if depth >= max_depth or uri in visited:
                return False

            visited.add(uri)
            indent = "  " * depth

            # Get the label for current topic
            current_label = self.get_topic_label(uri)

            # Find immediate parent topics
            parents = list(self.g.subjects(predicate=self.CSO_SCHEMA.superTopicOf, object=uri))

            # Check if this is a top-level topic
            is_top_level = len(parents) == 0 and any(self.g.triples((uri, self.CSO_SCHEMA.superTopicOf, None)))

            # Print current topic with appropriate marker
            if is_top_level:
                print(f"{indent}📍 {current_label} (TOP LEVEL)")
                return True
            else:
                print(f"{indent}└─ {current_label}")

            # Recursively process parents
            leads_to_top = False
            for parent in parents:
                leads_to_top |= print_hierarchy(parent, depth + 1, visited.copy())

            return leads_to_top

        # Print basic information about the term
        print("\n=== Term Analysis ===")
        print(f"Term: {term}")
        print(f"URI: {term_uri}")
        print("\nHierarchy (📍 indicates top-level topics):")

        # Print the complete hierarchy
        leads_to_top = print_hierarchy(term_uri)

        # Additional information
        print("\n=== Additional Information ===")

        # Get equivalent terms if any
        equivalents = list(self.g.objects(term_uri, self.CSO_SCHEMA.relatedEquivalent))
        if equivalents:
            print("\nEquivalent terms:")
            for eq in equivalents:
                eq_label = self.get_topic_label(eq)
                print(f"- {eq_label}")

        # Get sub-topics if any
        subtopics = list(self.g.objects(term_uri, self.CSO_SCHEMA.superTopicOf))
        if subtopics:
            print("\nSub-topics:")
            for sub in subtopics:
                sub_label = self.get_topic_label(sub)
                print(f"- {sub_label}")

        # Final assessment
        print("\n=== Type Assignment Assessment ===")
        if not leads_to_top:
            print("⚠️  Warning: This term does not lead to any top-level topics!")
            print("    Type assignment might not be optimal.")
        else:
            print("✓ Term successfully traced to top-level topic(s)")

        # Get the types that would be assigned by our dataset generator
        types = self.find_topic_types(term_uri)
        if types:
            print("\nTypes that would be assigned:")
            for type_uri in types:
                type_label = self.get_topic_label(type_uri)
                print(f"- {type_label}")
        else:
            print("\nNo types would be assigned by the current algorithm!")


    def explore_taxonomy_relationship(self, term1: str, term2: str) -> None:
        """
        Enhanced exploration of taxonomic relationships between terms.
        Shows all possible paths and validates relationships.
        """
        # Find URIs for both terms
        uri1 = None
        uri2 = None
        for s, p, o in self.g.triples((None, self.RDF_SCHEMA.label, None)):
            if str(o).lower() == term1.lower():
                uri1 = s
            elif str(o).lower() == term2.lower():
                uri2 = s

        if not (uri1 and uri2):
            logger.error("One or both terms not found in the ontology")
            return

        print("\n=== Taxonomy Analysis ===")
        print(f"Term 1: {term1} ({uri1})")
        print(f"Term 2: {term2} ({uri2})")

        # Find all paths in both directions
        paths_1_to_2 = self.find_all_paths_between_topics(uri1, uri2)
        paths_2_to_1 = self.find_all_paths_between_topics(uri2, uri1)

        print("\nPaths from term1 to term2:")
        for i, path in enumerate(paths_1_to_2, 1):
            print(f"\nPath {i}:")
            for j, uri in enumerate(path):
                label = self.get_topic_label(uri)
                prefix = "  └─" if j > 0 else "  "
                print(f"{prefix} {label}")

        print("\nPaths from term2 to term1:")
        for i, path in enumerate(paths_2_to_1, 1):
            print(f"\nPath {i}:")
            for j, uri in enumerate(path):
                label = self.get_topic_label(uri)
                prefix = "  └─" if j > 0 else "  "
                print(f"{prefix} {label}")

        print("\nRelationship Analysis:")

    def find_all_paths_between_topics(self, start: URIRef, end: URIRef, max_paths: int = 5) -> List[List[URIRef]]:
        """
        Finds multiple possible paths between two topics in the ontology.

        Args:
            start (URIRef): Starting topic URI
            end (URIRef): Target topic URI
            max_paths (int): Maximum number of paths to return
        Returns:
            List[List[URIRef]]: List of paths, where each path is a list of URIs
        """
        all_paths = []
        queue = [(start, [start])]
        visited = set()  # Track visited combinations of node and path

        while queue and len(all_paths) < max_paths:
            current, path = queue.pop(0)

            if current == end:
                all_paths.append(path)
                continue

            # Create a unique key for this node in this path context
            path_key = (current, tuple(path))
            if path_key in visited:
                continue
            visited.add(path_key)

            # Look for both super-topics and sub-topics
            neighbors = (
                    list(self.g.subjects(predicate=self.CSO_SCHEMA.superTopicOf, object=current)) +
                    list(self.g.objects(predicate=self.CSO_SCHEMA.superTopicOf, subject=current))
            )

            for next_topic in neighbors:
                if next_topic not in path:  # Avoid cycles
                    queue.append((next_topic, path + [next_topic]))

        return all_paths


    def find_topic_types(self, topic_uri: URIRef, visited: Set[URIRef] = None) -> Set[URIRef]:
        """
        Finds the true top-level types for a given topic by traversing all possible paths
        up the hierarchy.

        Args:
            topic_uri (URIRef): The topic to find types for
            visited (Set[URIRef]): Set of already visited topics to prevent cycles

        Returns:
            Set[URIRef]: Set of URIs representing the topic's top-level types
        """
        if visited is None:
            visited = set()

        if topic_uri in visited:
            return set()

        visited.add(topic_uri)

        # Find all immediate parent topics (those that have this topic as a subtopic)
        parent_topics = set(self.g.subjects(predicate=self.CSO_SCHEMA.superTopicOf, object=topic_uri))

        # If this is a top-level topic (has no parents but has children), return it
        if not parent_topics and any(self.g.triples((topic_uri, self.CSO_SCHEMA.superTopicOf, None))):
            return {topic_uri}

        # Recursively collect all top-level ancestors from all paths
        all_types = set()
        for parent in parent_topics:
            parent_types = self.find_topic_types(parent, visited.copy())
            all_types.update(parent_types)

        return all_types


if __name__ == "__main__":
    # Initialize analyzer and generator
    generator_for_cs_ontology = OntologyLearningDatasetGenerator(
        "../../data/ontologies/CSO.3.4.owl"
    )

    generator_for_plant_ontology = OntologyLearningDatasetGenerator(
        "../../data/ontologies/plant-ontology.owl"
    )

    ## Explore term hierarchy
    # generator_for_cso.explore_term_hierarchy("time slots")

    ## Explore taxonomy relationship
    # generator.explore_taxonomy_relationship("computer science", "transceivers")
    # generator.explore_taxonomy_relationship("transceivers", "computer science")

    ####################################################################################################
    # Term Typing Dataset Generation (Task A)
    ####################################################################################################
    cso_term_typing_dataset = generator_for_cs_ontology.generate_term_typing_dataset(sample_size=200)

    save_dataset(
        cso_term_typing_dataset,
        "../../data/datasets/bkp/cso_typing_dataset.json"
    )

    plant_term_typing_dataset = generator_for_plant_ontology.generate_term_typing_dataset(sample_size=200)

    save_dataset(
        plant_term_typing_dataset,
        "../../data/datasets/bkp/plant_typing_dataset.json"
    )

    ####################################################################################################
    # Taxonomy Dataset Generation (Task B)
    ####################################################################################################
    cso_taxonomy_dataset = generator_for_cs_ontology.generate_taxonomy_dataset(sample_size=200)

    save_dataset(
        cso_taxonomy_dataset,
        "../../data/datasets/bkp/cso_taxonomy_dataset.json"
    )

    plant_taxonomy_dataset = generator_for_plant_ontology.generate_taxonomy_dataset(sample_size=200)

    save_dataset(
        plant_taxonomy_dataset,
        "../../data/datasets/bkp/plant_taxonomy_dataset.json"
    )

    ####################################################################################################
    # Relation Dataset Generation (Task C)
    ####################################################################################################
    cs_o_relations = [
        URIRef("http://cso.kmi.open.ac.uk/schema/cso#contributesTo"),
        URIRef("http://cso.kmi.open.ac.uk/schema/cso#relatedEquivalent")
    ]

    cso_relation_dataset = generator_for_cs_ontology.generate_relation_dataset(
        relations=cs_o_relations,
        sample_size=200
    )

    save_dataset(
        cso_relation_dataset,
        "../../data/datasets/bkp/cso_relation_dataset.json"
    )

    plant_o_relations = [
        URIRef("http://www.w3.org/2004/02/skos/core#related"),
        URIRef("http://www.w3.org/2004/02/skos/core#broadMatch")
    ]

    plant_relation_dataset = generator_for_plant_ontology.generate_relation_dataset(
        relations=plant_o_relations,
        sample_size=200
    )

    save_dataset(
        plant_relation_dataset,
        "../../data/datasets/bkp/plant_relation_dataset.json"
    )
