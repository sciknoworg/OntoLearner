from collections import defaultdict

from rdflib import Graph, Namespace, URIRef, RDF
from typing import Dict, List, Set
import random
import logging

from src.utils.utils import save_dataset

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


class OntologyLearningDatasetGenerator:
    def __init__(self, rdf_file):
        """
        Initialize with an OntologyAnalyzer instance.
        """
        logger.info(f"Loading CSO ontology from {rdf_file}")

        self.g = Graph()
        self.g.parse(rdf_file, format="xml")

        logger.info(f"Loaded ontology with {len(self.g)} triples")

        self.CSO_SCHEMA = Namespace("http://cso.kmi.open.ac.uk/schema/cso#")
        self.RDF_SCHEMA = Namespace("http://www.w3.org/2000/01/rdf-schema#")


    def get_top_level_topics(self) -> Set[URIRef]:
        """
        Identifies the top-level topics in the ontology hierarchy.
        These are topics that are not subtopics of any other topic but have subtopics themselves.

        Returns:
            Set[URIRef]: Set of URIs representing top-level topics
        """
        # Get all topics that are sources of superTopicOf relations (parent topics)
        parent_topics = set(self.g.subjects(predicate=self.CSO_SCHEMA.superTopicOf, object=None))

        # Get all topics that are targets of superTopicOf relations (child topics)
        child_topics = set(self.g.objects(predicate=self.CSO_SCHEMA.superTopicOf, subject=None))

        # Top-level topics are those that are parents but not children
        top_level = parent_topics - child_topics

        logger.info(f"Found {len(top_level)} top-level topics in the ontology")

        return top_level


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


    def generate_term_typing_dataset(self, sample_size: int = 100) -> List[Dict]:
        """
        Generates training and test datasets for term typing by finding proper type relationships
        through hierarchy traversal.

        The function:
            1. Identifies all topics and their labels in the ontology
            2. For each topic, finds its type(s) by traversing up the hierarchy
            3. Creates term-type pairs with proper type assignments
            4. Samples and splits the data into training and test sets

        Args:
            sample_size (int): Maximum number of samples to include in the dataset

        Returns:
            List[Dict], Training dataset, containing dictionary with 'term' and 'type' keys
        """
        logger.info("Starting term typing dataset generation")

        # Initialize container for term-type pairs
        term_type_pairs = []

        # Get all topics that have labels
        topic_count = 0
        processed_count = 0

        for s, p, o in self.g.triples((None, self.RDF_SCHEMA.label, None)):
            topic_count += 1

            # Verify this is a Topic in our ontology
            if (s, RDF.type, self.CSO_SCHEMA.Topic) not in self.g:
                continue

            term = str(o)

            # Find all types for this topic by traversing up the hierarchy
            type_uris = self.find_topic_types(s)

            # TODO
            if type_uris:
                processed_count += 1
                # Create a term-type pair for each type found
                for type_uri in type_uris:
                    type_label = self.get_topic_label(type_uri)
                    if type_label:  # Only add if we have a valid type label
                        term_type_pairs.append({
                            "term": term,
                            "type": type_label,
                            # "path": self.get_path_to_type(s, type_uri)
                        })

        logger.info(f"Processed {processed_count} topics out of {topic_count} total topics")
        logger.info(f"Generated {len(term_type_pairs)} term-type pairs")

        # Apply sampling if needed
        if len(term_type_pairs) > sample_size > 0:
            logger.info(f"Sampling {sample_size} pairs from total {len(term_type_pairs)}")
            term_type_pairs = random.sample(term_type_pairs, sample_size)

        logger.info(f"Final dataset: {len(term_type_pairs)} training samples")

        return term_type_pairs


    def generate_taxonomy_dataset(self, sample_size: int = 100) -> List[Dict]:
        logger.info("Starting taxonomy dataset generation")

        # Pre-compute topic labels to avoid repeated queries
        topic_label_cache = {}
        for s, _, o in self.g.triples((None, self.RDF_SCHEMA.label, None)):
            if (s, RDF.type, self.CSO_SCHEMA.Topic) in self.g:
                topic_label_cache[s] = str(o)

        # Initialize containers with estimated capacity
        positive_pairs = []
        processed_pairs = set()

        # Find direct relationships using cached labels
        for s, _, o in self.g.triples((None, self.CSO_SCHEMA.superTopicOf, None)):
            term1_label = topic_label_cache.get(s)
            term2_label = topic_label_cache.get(o)

            if term1_label and term2_label:
                pair_key = (term1_label, term2_label)
                if pair_key not in processed_pairs:
                    positive_pairs.append({
                        "term1": term1_label,
                        "term2": term2_label,
                        "relation": True,
                        "relationship_type": "direct"
                    })
                    processed_pairs.add(pair_key)

        # Early sampling for transitive relationships if sample_size is small
        if sample_size and len(positive_pairs) > sample_size:
            all_topics = [(uri, label) for uri, label in topic_label_cache.items()]
            sampled_topics = random.sample(all_topics, min(len(all_topics), sample_size * 2))
        else:
            all_topics = [(uri, label) for uri, label in topic_label_cache.items()]
            sampled_topics = all_topics

        # Find transitive relationships using sampled topics
        for topic1, label1 in sampled_topics:
            for topic2, label2 in sampled_topics:
                if topic1 != topic2:
                    pair_key = (label1, label2)
                    if pair_key not in processed_pairs:
                        paths = self.find_all_paths_between_topics(topic1, topic2, max_paths=1)
                        if paths:
                            positive_pairs.append({
                                "term1": label1,
                                "term2": label2,
                                "relation": True,
                                "relationship_type": "transitive",
                                "path_length": len(paths[0]) - 1
                            })
                            processed_pairs.add(pair_key)

        if sample_size and len(positive_pairs) > sample_size:
            sampled_positive = random.sample([p for p in positive_pairs if p["relation"]], sample_size // 2)
            positive_pairs = sampled_positive

        return positive_pairs


    # def generate_taxonomy_dataset(self, sample_size: int = 100) -> List[Dict]:
    #     """
    #     Generates a dataset for taxonomy learning that captures hierarchical relationships between topics.
    #     This function creates both positive examples (actual hierarchical relationships) and
    #     negative examples (non-hierarchical relationships) to train models in distinguishing
    #     valid taxonomic relationships.
    #
    #     The function follows these steps:
    #         1. Identifies all valid superTopicOf relationships in the ontology
    #         2. Creates positive examples from these direct relationships
    #         3. Adds positive examples from transitive relationships (if A > B > C, then A > C)
    #         4. Generates balanced negative examples by finding unrelated topic pairs
    #         5. Samples and splits the data into training and test sets
    #
    #     Args:
    #         sample_size (int): Maximum number of examples to include in the dataset
    #                           (will be split between positive and negative examples)
    #
    #     Returns:
    #         List[Dict]: Training dataset containing dictionary with 'term1', 'term2', and 'relation' keys
    #     """
    #     logger.info("Starting taxonomy dataset generation")
    #
    #     # Store all taxonomic relationships
    #     positive_pairs = []
    #
    #     # First, collect direct superTopicOf relationships
    #     direct_relationships = set()
    #
    #     # Find direct superTopicOf relationships
    #     for s, p, o in self.g.triples((None, self.CSO_SCHEMA.superTopicOf, None)):
    #         # Get labels for both topics
    #         term1_label = self.get_topic_label(s)
    #         term2_label = self.get_topic_label(o)
    #
    #         if term1_label and term2_label:  # Ensure both labels exist
    #             direct_relationships.add((s, o))
    #             positive_pairs.append({
    #                 "term1": term1_label,
    #                 "term2": term2_label,
    #                 "relation": True,
    #                 "relationship_type": "direct"
    #             })
    #
    #     logger.info(f"Found {len(positive_pairs)} direct taxonomic relationships")
    #
    #     # Add transitive relationships (if A > B > C, then A > C)
    #     transitive_pairs = []
    #     processed_pairs = set()
    #
    #     def find_descendants(topic: URIRef, ancestor: URIRef, path_length: int = 0):
    #         """Recursively finds all descendants of a topic to build transitive relationships."""
    #         if path_length > 5:  # Limit depth to avoid too distant relationships
    #             return
    #
    #         descendants = list(self.g.objects(topic, self.CSO_SCHEMA.superTopicOf))
    #         for descendant in descendants:
    #             pair = (ancestor, descendant)
    #             if pair not in processed_pairs and pair not in direct_relationships:
    #                 processed_pairs.add(pair)
    #                 ancestor_label = self.get_topic_label(ancestor)
    #                 descendant_label = self.get_topic_label(descendant)
    #
    #                 if ancestor_label and descendant_label:
    #                     transitive_pairs.append({
    #                         "term1": ancestor_label,
    #                         "term2": descendant_label,
    #                         "relation": True,
    #                         "relationship_type": "transitive"
    #                     })
    #
    #                 # Recurse to find further descendants
    #                 find_descendants(descendant, ancestor, path_length + 1)
    #
    #     # Find all transitive relationships
    #     for s, _ in direct_relationships:
    #         find_descendants(s, s)
    #
    #     positive_pairs.extend(transitive_pairs)
    #     logger.info(f"Added {len(transitive_pairs)} transitive relationships")
    #
    #     # Apply sampling if needed
    #     if len(all_pairs) > sample_size:
    #         logger.info(f"Sampling {sample_size} pairs from total {len(all_pairs)}")
    #         # Ensure we maintain balance between positive and negative examples
    #         positive_sample = random.sample(positive_pairs, sample_size // 2)
    #
    #     logger.info(f"Final dataset: {len(all_pairs)} training samples")
    #
    #     # Additional statistics for validation
    #     train_positive = sum(1 for x in all_pairs if x["relation"])
    #
    #     logger.info(f"Training set: {train_positive} positive, {len(all_pairs) - train_positive} negative")
    #
    #     return all_pairs


    def generate_relation_dataset(self, sample_size: int = 100) -> List[Dict]:
        logger.info("Generating relation dataset")

        # Pre-compute topic labels and create an index of term relationships
        topic_label_cache = {}
        term_relations = defaultdict(set)

        for s, _, o in self.g.triples((None, self.RDF_SCHEMA.label, None)):
            if (s, RDF.type, self.CSO_SCHEMA.Topic) in self.g:
                topic_label_cache[s] = str(o)

        # Build relationship index
        for s, _, o in self.g.triples((None, self.CSO_SCHEMA.contributesTo, None)):
            term_relations[s].add(o)
            term_relations[o].add(s)

        relation_pairs = []
        processed_pairs = set()
        all_terms = list(topic_label_cache.keys())

        # Find contributes-to relationships
        for s, _, o in self.g.triples((None, self.CSO_SCHEMA.contributesTo, None)):
            term1_label = topic_label_cache.get(s)
            term2_label = topic_label_cache.get(o)

            if term1_label and term2_label:
                pair_key = (term1_label, term2_label)
                if pair_key not in processed_pairs:
                    relation_pairs.append({
                        "term1": term1_label,
                        "term2": term2_label,
                        "relation": "contributesTo"
                    })
                    processed_pairs.add(pair_key)

                    # Generate negative example efficiently
                    for _ in range(10):  # Try up to 10 times to find unrelated term
                        random_term = random.choice(all_terms)
                        if random_term not in term_relations[s] and random_term not in term_relations[o]:
                            random_label = topic_label_cache.get(random_term)
                            if random_label:
                                relation_pairs.append({
                                    "term1": term1_label,
                                    "term2": random_label,
                                    "relation": "none"
                                })
                                break

        # Apply sampling if needed
        if sample_size and len(relation_pairs) > sample_size:
            # Ensure balanced sampling
            contributesTo = [p for p in relation_pairs if p["relation"] == "contributesTo"]
            none_relations = [p for p in relation_pairs if p["relation"] == "none"]

            sample_per_type = sample_size // 2
            sampled_pairs = (random.sample(contributesTo, sample_per_type) +
                             random.sample(none_relations, sample_per_type))
            return sampled_pairs

        return relation_pairs


    def get_topic_label(self, topic_uri: URIRef) -> str:
        """Get human-readable label for a topic.

        Args:
            topic_uri (URIRef): The URI reference of the topic
        Returns:
            str: The human-readable label, or the last part of the URI if no label exists
        """
        labels = list(self.g.objects(subject=topic_uri, predicate=self.RDF_SCHEMA.label))

        return str(labels[0]) if labels else str(topic_uri).split('/')[-1].replace('_', ' ')


    def get_random_unrelated_term(self, term1: URIRef, term2: URIRef) -> URIRef:
        """Get a random term that's not related to either of two given terms.

        Args:
            term1 (URIRef): First term to avoid relations with
            term2 (URIRef): Second term to avoid relations with
        Returns:
            URIRef: A randomly selected unrelated term, or None if none exists
        """
        all_terms = set(self.g.subjects(predicate=self.RDF_SCHEMA.label, object=None))

        related_terms = set(self.g.objects(subject=term1, predicate=None)) | \
                        set(self.g.objects(subject=term2, predicate=None))

        unrelated_terms = all_terms - related_terms

        return random.choice(list(unrelated_terms)) if unrelated_terms else None


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
        print(f"\nHierarchy (📍 indicates top-level topics):")

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


# Example usage:
if __name__ == "__main__":
    # Initialize analyzer and generator
    generator = OntologyLearningDatasetGenerator("../../data/ontologies/CSO.3.4.owl")

    ## Explore term hierarchy
    generator.explore_term_hierarchy("time slots")

    ## Explore taxonomy relationship
    # generator.explore_taxonomy_relationship("computer science", "transceivers")
    # generator.explore_taxonomy_relationship("transceivers", "computer science")

    ## Task A: Term Typing
    # term_typing_dataset = generator.generate_term_typing_dataset()
    # save_dataset(term_typing_dataset, "../data/datasets/train_typing_dataset.json")

    # Task B: Taxonomy Discovery
    taxonomy_dataset = generator.generate_taxonomy_dataset()
    save_dataset(taxonomy_dataset, "../data/datasets/taxonomy_dataset.json")

    # Task C: Non-Taxonomic Relation Extraction
    relation_dataset = generator.generate_relation_dataset()
    save_dataset(relation_dataset, "../../data/datasets/relation_dataset.json")

