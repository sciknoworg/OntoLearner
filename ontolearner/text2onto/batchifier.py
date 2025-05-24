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

from collections import defaultdict, deque
from typing import Dict, List
from abc import ABC

from ..data_structure import PseudoSentence

class TaxonomyBatchifier(ABC):
    def __init__(self, parent_to_child: Dict[str, List], batch_size: int):
        self.parent_to_child = parent_to_child
        self.batch_size = batch_size
        self.child_to_parents = self._build_child_to_parents()
        self.visited_relation_ids = set()
        self.relation_queue = deque()
        self.raw_batches = []

    def _build_child_to_parents(self):
        child_to_parents = defaultdict(list)
        for parent, children in self.parent_to_child.items():
            for rel in children:
                child_to_parents[rel[1]].append((parent, rel[0]))  # (parent label, relation ID)
        return child_to_parents

    def _find_leaf_nodes(self):
        all_children = set()
        for children in self.parent_to_child.values():
            for child_info in children:
                all_children.add(child_info[1])
        return [child for child in all_children if child not in self.parent_to_child]

    def _enqueue_parents(self, node):
        for parent, rel_id in self.child_to_parents.get(node, []):
            if rel_id not in self.visited_relation_ids:
                self.relation_queue.append((parent, node, rel_id))

    def _structure_aware_batching(self, bootstrap_nodes=None):
        if bootstrap_nodes is None:
            bootstrap_nodes = self._find_leaf_nodes()
        elif len(bootstrap_nodes) == 0:
            return

        # Initialize queue from leaf nodes
        for leaf in bootstrap_nodes:
            for parent, rel_id in self.child_to_parents.get(leaf, []):
                self.relation_queue.append((parent, leaf, rel_id))

        while self.relation_queue:
            parent, child, rel_id = self.relation_queue.popleft()
            # if the relation is already included, skip it
            if rel_id in self.visited_relation_ids:
                continue

            current_batch = []

            # A: add children if any
            for child_rel in self.parent_to_child.get(child, []):
                child_id, grandchild, rel_label = child_rel
                if child_id not in self.visited_relation_ids:
                    current_batch.append((child, child_id, grandchild, rel_label))
                    self.visited_relation_ids.add(child_id)
                    self._enqueue_parents(child)

            # A: Add all siblings
            for sibling_rel in self.parent_to_child[parent]:
                sibling_id, sibling, rel_label = sibling_rel
                if sibling_id not in self.visited_relation_ids:
                    current_batch.append((parent, sibling_id, sibling, rel_label))
                    self.visited_relation_ids.add(sibling_id)

                    # B: Add children of each sibling
                    for child_rel in self.parent_to_child.get(sibling, []):
                        child_id, grandchild, rel_label = child_rel
                        if child_id not in self.visited_relation_ids:
                            current_batch.append((sibling, child_id, grandchild, rel_label))
                            self.visited_relation_ids.add(child_id)
                            self._enqueue_parents(sibling)

            if current_batch:
                self.raw_batches.append(current_batch)

        # C: Fallback for any missed relations
        fallback_bootstrap_nodes = []
        for parent, children in self.parent_to_child.items():
            for rel in children:
                if rel[0] not in self.visited_relation_ids:
                    fallback_bootstrap_nodes.append(parent)
                    fallback_bootstrap_nodes.append(rel[1])
        self._structure_aware_batching(bootstrap_nodes=fallback_bootstrap_nodes)


    def _split_batches_and_create_pseudo_sentences(self) -> List[PseudoSentence]:
        verbalized_batches = []
        id = 0
        for batch in self.raw_batches:
            verbalized_batch = []
            # keeping track of pseudo sentences to avoid adding duplicates
            pseudo_sentences = set()
            for rel in batch:
                pseudo_sentence = f"{rel[2]} {rel[3]} {rel[0]}"
                # keeping track of terms and types included in each pseudo sentence
                if rel[3] == "is a":
                    terms = [rel[2]]
                    types = [rel[0]]
                else:
                    terms = []
                    types = [rel[0], rel[2]]
                # skip duplicates
                if pseudo_sentence not in pseudo_sentences:
                    verbalized_batch.append([pseudo_sentence, terms, types])
                    pseudo_sentences.add(pseudo_sentence)
            verbalized_batches.append([id, verbalized_batch])
            id += 1

        final_batches = []
        for id, batch in verbalized_batches:
            sub_id = 0
            for i in range(0, len(batch), self.batch_size):
                final_batches.append([f"{id}_{sub_id}", batch[i:i + self.batch_size]])
                sub_id += 1

        final_batches_processed = []
        for id, batch in final_batches:
            doc_level_terms = set()
            doc_level_types = set()
            doc_level_pseudo_sentences = list()
            for pseudo_sentence, sent_terms, sent_types in batch:
                doc_level_pseudo_sentences.append(pseudo_sentence)
                doc_level_terms.update(sent_terms)
                doc_level_types.update(sent_types)
            final_batches_processed.append(PseudoSentence(id=id,
                                                          pseudo_sentences=doc_level_pseudo_sentences,
                                                          terms=list(doc_level_terms),
                                                          types=list(doc_level_types)))
        return final_batches_processed

    def batchify(self) -> List[PseudoSentence]:
        self._structure_aware_batching()
        return self._split_batches_and_create_pseudo_sentences()
