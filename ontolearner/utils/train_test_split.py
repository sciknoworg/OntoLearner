# Copyright (c) 2025 SciKnowOrg
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
from typing import Tuple, List, Set
import logging
from sklearn.model_selection import train_test_split as sklearn_split

from ontolearner.data_structure import OntologyData, TermTyping, TaxonomicRelation, NonTaxonomicRelation

logger = logging.getLogger(__name__)


def term_typing_split(term_typings: List[TermTyping],
                      test_size: float = 0.2,
                      random_state: int = 42,
                      verbose: bool=False) -> Tuple[List[TermTyping], List[TermTyping]]:
    """
    Split term typing data with stratified sampling to ensure balanced type distribution.

    This function performs intelligent splitting of term typing data by grouping terms
    by their primary (least common) type and ensuring proportional representation in
    both training and test sets. This prevents type distribution skew that could
    negatively impact model training and evaluation.

    Args:
        term_typings: List of term typing instances to split.
        test_size: Proportion of data to include in test set (0.0-1.0).
        random_state: Random seed for reproducible splits.

    Returns:
        Tuple of (train_typings, test_typings) with balanced type distributions.
    """
    # Get type frequencies
    type_counter = {}
    term_to_types = {}

    for tt in term_typings:
        term_to_types[tt.term] = tt.types
        for t in tt.types:
            type_counter[t] = type_counter.get(t, 0) + 1

    # Group terms by their most frequent type
    term_by_primary_type = {}
    for term, types in term_to_types.items():
        if not types:
            continue
        # Find the least common type for better stratification
        primary_type = min(types, key=lambda t: type_counter.get(t, 0))
        if primary_type not in term_by_primary_type:
            term_by_primary_type[primary_type] = []
        term_by_primary_type[primary_type].append(term)

    # Split terms within each type group
    train_terms = set()
    test_terms = set()

    for type_name, terms in term_by_primary_type.items():
        if len(terms) < 2:  # If only one term has this type, put in train
            train_terms.update(terms)
            continue

        n_test = max(1, int(len(terms) * test_size))
        type_test_terms = set(random.Random(random_state).sample(terms, n_test))
        type_train_terms = set(terms) - type_test_terms

        train_terms.update(type_train_terms)
        test_terms.update(type_test_terms)

    # Create the final train/test lists
    train_typings = [tt for tt in term_typings if tt.term in train_terms]
    test_typings = [tt for tt in term_typings if tt.term in test_terms]
    if verbose:
        logger.info(f"Term typing split: {len(train_typings)} train, {len(test_typings)} test")
    return train_typings, test_typings


def taxonomy_split(taxonomies: List[TaxonomicRelation],
                   train_terms: Set[str] = None,
                   test_size: float = 0.2,
                   random_state: int = 42,
                   verbose: bool=False) -> Tuple[List[TaxonomicRelation], List[TaxonomicRelation]]:
    """
    Split taxonomic relations while preventing data leakage between train and test sets.

    This function ensures that terms appearing in training data don't appear in test
    data, which is crucial for valid evaluation of ontology learning models. It
    prioritizes relations involving training terms for the training set and carefully
    splits remaining relations to maintain the desired test set size.

    Args:
        taxonomies: List of taxonomic relations to split.
        train_terms: Set of terms already assigned to training (from term typing).
                    If None, performs random split without leakage prevention.
        test_size: Target proportion of relations for test set (0.0-1.0).
        random_state: Random seed for reproducible splits.

    Returns:
        Tuple of (train_relations, test_relations) with no term overlap.
    """
    train_terms = train_terms or set()
    test_candidate_relations = []
    train_relations = []

    # First pass: separate relations involving training terms
    for rel in taxonomies:
        if rel.parent in train_terms or rel.child in train_terms:
            train_relations.append(rel)
        else:
            test_candidate_relations.append(rel)

    # Second pass: split remaining relations
    if test_candidate_relations:
        n_test = min(len(test_candidate_relations),
                     max(1, int(len(taxonomies) * test_size)))

        # Use sklearn's function for this step
        train_idx, test_idx = sklearn_split(
            range(len(test_candidate_relations)),
            test_size=n_test/len(test_candidate_relations),
            random_state=random_state
        )

        for idx in train_idx:
            train_relations.append(test_candidate_relations[idx])

        test_relations = [test_candidate_relations[idx] for idx in test_idx]
    else:
        # If all relations involve training terms, do a random split
        n_test = max(1, int(len(train_relations) * test_size))
        random.Random(random_state).shuffle(train_relations)
        test_relations = train_relations[-n_test:]
        train_relations = train_relations[:-n_test]
    if verbose:
        logger.info(f"Taxonomy split: {len(train_relations)} train, {len(test_relations)} test")
    return train_relations, test_relations


def non_taxonomic_re_split(non_taxonomies: List[NonTaxonomicRelation],
                           train_terms: Set[str] = None,
                           test_size: float = 0.2,
                           random_state: int = 42,
                           verbose: bool=False) -> Tuple[List[NonTaxonomicRelation], List[NonTaxonomicRelation]]:
    """
    Split non-taxonomy relations ensuring no term leakage from train to test
    """
    train_terms = train_terms or set()
    test_candidate_relations = []
    train_relations = []

    # First pass: separate relations involving training terms
    for rel in non_taxonomies:
        if rel.head in train_terms or rel.tail in train_terms:
            train_relations.append(rel)
        else:
            test_candidate_relations.append(rel)

    # Second pass: ensure relation type distribution
    relation_types = {}
    for rel in test_candidate_relations:
        if rel.relation not in relation_types:
            relation_types[rel.relation] = []
        relation_types[rel.relation].append(rel)

    test_relations = []

    # For each relation type, take a proportional number for test
    for rel_type, rels in relation_types.items():
        n_test = max(1, int(len(rels) * test_size))
        sampled_test = random.Random(random_state).sample(rels, min(n_test, len(rels)))
        test_relations.extend(sampled_test)

        # Remove the test relations from candidates
        for rel in sampled_test:
            test_candidate_relations.remove(rel)

    # Add remaining candidates to train
    train_relations.extend(test_candidate_relations)
    if verbose:
        logger.info(f"Non-taxonomy split: {len(train_relations)} train, {len(test_relations)} test")
    return train_relations, test_relations


def train_test_split(data: OntologyData,
                     test_size: float = 0.2,
                     random_state: int = 42,
                     verbose: bool = False) -> Tuple[OntologyData, OntologyData]:
    """
    Create comprehensive train/test split of ontology data with data leakage prevention.
    This is the main function for splitting ontology learning datasets. It performs
    coordinated splitting across all three ontology learning tasks while ensuring
    no data leakage between training and test sets. The function maintains consistency
    in term assignments and preserves the integrity of the ontological structure.

    Args:
        data: Complete ontology data containing all three learning task datasets.
        test_size: Proportion of data for test set (0.0-1.0). Applied consistently
                  across all tasks with intelligent adjustments for small datasets.
        random_state: Random seed for reproducible splits across all tasks.

    Returns:
        Tuple of (train_data, test_data) as complete OntologyData objects ready
        for use in machine learning pipelines.

    Raises:
        ValueError: If test_size is not in valid range [0.0, 1.0].
    """
    # First split term typing to establish term assignment
    train_typings, test_typings = term_typing_split(
        data.term_typings, test_size, random_state
    )

    # Get sets of training and test terms
    train_terms = {tt.term for tt in train_typings}
    test_terms = {tt.term for tt in test_typings}

    # Split taxonomic relations considering term assignment
    train_taxonomies, test_taxonomies = taxonomy_split(
        data.type_taxonomies.taxonomies,
        train_terms,
        test_size,
        random_state
    )

    # Update term sets based on taxonomy split
    train_terms.update({rel.parent for rel in train_taxonomies})
    train_terms.update({rel.child for rel in train_taxonomies})
    test_terms.update({rel.parent for rel in test_taxonomies})
    test_terms.update({rel.child for rel in test_taxonomies})

    # Split non-taxonomic relations considering term assignment
    train_non_taxonomies, test_non_taxonomies = non_taxonomic_re_split(
        data.type_non_taxonomic_relations.non_taxonomies,
        train_terms,
        test_size,
        random_state
    )

    # Create train and test ontology data objects
    train_data = OntologyData(
        term_typings=train_typings,
        type_taxonomies=data.type_taxonomies.__class__(
            types=data.type_taxonomies.types,
            taxonomies=train_taxonomies
        ),
        type_non_taxonomic_relations=data.type_non_taxonomic_relations.__class__(
            types=data.type_non_taxonomic_relations.types,
            relations=data.type_non_taxonomic_relations.relations,
            non_taxonomies=train_non_taxonomies
        )
    )

    test_data = OntologyData(
        term_typings=test_typings,
        type_taxonomies=data.type_taxonomies.__class__(
            types=data.type_taxonomies.types,
            taxonomies=test_taxonomies
        ),
        type_non_taxonomic_relations=data.type_non_taxonomic_relations.__class__(
            types=data.type_non_taxonomic_relations.types,
            relations=data.type_non_taxonomic_relations.relations,
            non_taxonomies=test_non_taxonomies
        )
    )

    # Log the split summary
    if verbose:
        logger.info("Ontology data split complete:")
        logger.info(f"  Term typing: {len(train_typings)} train, {len(test_typings)} test")
        logger.info(f"  Taxonomy: {len(train_taxonomies)} train, {len(test_taxonomies)} test")
        logger.info(f"  Non-taxonomy: {len(train_non_taxonomies)} train, {len(test_non_taxonomies)} test")

    return train_data, test_data
