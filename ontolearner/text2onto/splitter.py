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
import pandas as pd
from tqdm import tqdm
import random
from ..data_structure import SyntheticText2OntoData

class SyntheticDataSplitter:

    def __init__(self, synthetic_data: SyntheticText2OntoData, onto_name:str):
        self.pseudo_sentence_batches = pd.DataFrame([ps.dict() for ps in synthetic_data.pseudo_sentences])
        self.child_to_parent = synthetic_data.child_to_parent

        self.documents = list()
        self.term_to_doc_id = defaultdict(set)
        self.type_to_doc_id = defaultdict(set)
        self.doc_id_to_terms = defaultdict(set)
        self.doc_id_to_types = defaultdict(set)
        for row in tqdm(self.pseudo_sentence_batches.itertuples(index=False), total=len(self.pseudo_sentence_batches)):
            doc_id = str(row.id)
            self.doc_id_to_types[doc_id] = set(row.types)
            self.doc_id_to_terms[doc_id] = set(row.terms)
            for a_type in row.types:
                self.type_to_doc_id[a_type].add(doc_id)
            for a_term in row.terms:
                self.term_to_doc_id[a_term].add(doc_id)

        self.doc_id_to_doc = {doc.id: doc for doc in synthetic_data.generated_docs}
        print(f"loaded {len(self.doc_id_to_doc)} documents!")

        total_type_count = len(set().union(*self.doc_id_to_types.values()))
        total_term_count = len(set().union(*self.doc_id_to_terms.values()))
        print(f" total type count: {total_type_count}")
        print(f" total term count: {total_term_count}")

        self.onto_name = onto_name

    def set_train_val_test_sizes(self, train_percentage: float = 0.8,
                                 val_percentage: float = 0.1,
                                 test_percentage: float = 0.1):
        if train_percentage + val_percentage + test_percentage != 1:
            raise Exception("The sum of train/val/test percentages should be 1.")
        total_types = len(self.type_to_doc_id.keys())
        total_docs = len(self.doc_id_to_doc.keys())
        train_quota = int(train_percentage * total_types)
        val_quota = int(val_percentage * total_types)
        test_quota = total_types - train_quota - val_quota
        print(f"train_quota: {train_quota}\nval_quota: {val_quota}\ntest_quota: {test_quota}")
        split_targets = {
            'train': train_quota,
            'val': val_quota,
            'test': test_quota
        }
        train_docs_quota = int(train_percentage * total_docs)
        val_docs_quota = int(val_percentage * total_docs)
        test_docs_quota = total_docs - train_docs_quota - val_docs_quota
        print(
            f"train docs quota: {train_docs_quota}\nval docs quota: {val_docs_quota}\ntest docs quota: {test_docs_quota}")
        split_docs_targets = {
            'train': train_docs_quota,
            'val': val_docs_quota,
            'test': test_docs_quota
        }
        return split_targets, split_docs_targets

    def assign_types_with_propagation(self, split_name, split_targets, split_docs_targets,
                                      split_types, split_docs, unassigned_types, unassigned_docs, assigned_docs):
        target_size = split_targets[split_name]
        docs_target_size = split_docs_targets[split_name]
        while len(split_types[split_name]) < target_size and len(
                split_docs[split_name]) < docs_target_size and unassigned_types:
            type_seed = unassigned_types.pop()
            queue = deque([type_seed])
            while (queue and len(split_types[split_name]) < target_size and
                   len(split_docs[split_name]) < docs_target_size):
                current_type = queue.popleft()
                if current_type in split_types['train'] | split_types['val'] | split_types['test']:
                    continue
                split_types[split_name].add(current_type)
                # Get all documents for this type
                for doc_id in self.type_to_doc_id.get(current_type, []):
                    if doc_id in assigned_docs:
                        continue
                    split_docs[split_name].add(doc_id)
                    assigned_docs.add(doc_id)
                    unassigned_docs.discard(doc_id)
                    for t in self.doc_id_to_types[doc_id]:
                        if t not in split_types['train'] | split_types['val'] | split_types['test']:
                            queue.append(t)
                            unassigned_types.discard(t)
        return split_types, split_docs, unassigned_docs, assigned_docs

    def create_train_val_test_splits(self, split_targets, split_docs_targets):
        split_types = {'train': set(), 'val': set(), 'test': set()}
        split_docs = {'train': set(), 'val': set(), 'test': set()}
        all_types = list(self.type_to_doc_id.keys())
        random.seed(25)
        random.shuffle(all_types)
        unassigned_types = set(all_types)
        unassigned_docs = set(self.doc_id_to_doc.keys())
        assigned_docs = set()

        for split_name in ['train', 'test', 'val']:
            split_types, split_docs, unassigned_docs, assigned_docs = self.assign_types_with_propagation(split_name,
                                                                                         split_targets,
                                                                                         split_docs_targets,
                                                                                         split_types,
                                                                                         split_docs,
                                                                                         unassigned_types,
                                                                                         unassigned_docs,
                                                                                         assigned_docs)

        # assign the unassigned documents based on their overlap with types in the already assigned types to splits
        for doc_id in unassigned_docs.copy():
            doc_types = self.doc_id_to_types[doc_id]
            doc_type_split_counts = {"train": 0, "test": 0, "val": 0}
            for a_type in doc_types:
                for split_name in ['train', 'test', 'val']:
                    if a_type in split_types[split_name]:
                        doc_type_split_counts[split_name] += 1

            total = sum(doc_type_split_counts.values())
            if total == 0:
                split_docs["train"].add(doc_id)
            else:
                max_key = max(doc_type_split_counts, key=doc_type_split_counts.get)
                split_docs[max_key].add(doc_id)
            unassigned_docs.discard(doc_id)

        assert len(unassigned_docs) == 0, "There are no unassigned documents."

        print(f"Train: {len(split_docs['train'])} docs, {len(split_types['train'])} types")
        print(f"Val: {len(split_docs['val'])} docs, {len(split_types['val'])} types")
        print(f"Test: {len(split_docs['test'])} docs, {len(split_types['test'])} types")
        return split_docs

    def generate_split_artefacts(self, split_docs):
        split_terms = {'train': set(), 'val': set(), 'test': set()}
        terms_splits = {}
        for split_name in ['train', 'val', 'test']:
            for doc_id in split_docs[split_name]:
                split_terms[split_name].update(self.doc_id_to_terms[doc_id])
            split_terms[split_name] = list(split_terms[split_name])
            terms_with_types = []
            for term in split_terms[split_name]:
                if term in self.child_to_parent:
                    terms_with_types.append({"term": term, "types": self.child_to_parent[term]})
                else:
                    terms_with_types.append({"term": term, "types": []})
            terms_splits[split_name] = terms_with_types

        types_splits = {}
        for split_name in ['train', 'val', 'test']:
            split_types_from_docs = set()
            for doc_id in split_docs[split_name]:
                split_types_from_docs.update(self.doc_id_to_types[doc_id])
            types_with_parents = []
            for a_type in split_types_from_docs:
                if a_type in self.child_to_parent:
                    types_with_parents.append({"type": a_type, "parents": self.child_to_parent[a_type]})
                else:
                    types_with_parents.append({"type": a_type, "parents": []})
            types_splits[split_name] = types_with_parents

        docs_split = {'train': [], 'val': [], 'test': []}
        split_to_text = {'train': "", 'val': "", 'test': ""}
        for split_name in ['train', 'val', 'test']:
            for doc_id in split_docs[split_name]:
                doc = self.doc_id_to_doc[doc_id]
                docs_split[split_name].append(doc)
                split_to_text[split_name] += " " + doc.title + " " + doc.text

        types2docs_splits = {}
        for split_name in ['train', 'val', 'test']:
            type2doc = defaultdict(list)
            split_types_from_docs = set()
            for doc_id in split_docs[split_name]:
                split_types_from_docs.update(self.doc_id_to_types[doc_id])
            for a_type in split_types_from_docs:
                for doc_id in self.type_to_doc_id[a_type]:
                    if doc_id in split_docs[split_name]:
                        extraction_type = "abstractive"
                        if a_type in split_to_text[split_name]:
                            extraction_type = "extractive"
                        type2doc[a_type].append({"doc_id": doc_id, "extraction_type": extraction_type})
            types2docs_splits[split_name] = type2doc

        return terms_splits, types_splits, docs_split, types2docs_splits

    def split(self, train: float = 0.8, val: float = 0.1, test: float = 0.1):
        split_targets, split_docs_targets = self.set_train_val_test_sizes(train_percentage=train,
                                                                          val_percentage=val,
                                                                          test_percentage=test)
        split_docs = self.create_train_val_test_splits(split_targets, split_docs_targets)
        terms, types, docs, types2docs = self.generate_split_artefacts(split_docs)
        return terms, types, docs, types2docs
