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

from ..data_structure import SyntheticText2OntoData, PseudoSentence
from .batchifier import TaxonomyBatchifier
import dspy
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
from typing import Any, List, Dict
from abc import ABC

class SyntheticVerbalizer(dspy.Signature):
    """
    You are given a set of pseudo sentences in the form of a triple, i.e., (subject, relation, object). In addition, you are given
    the name of the ontology to provide more context. Your task is to convert into a fluent natural language. In addition to the text,
    please provide a descriptive and concise title for the passage of text.
    IMPORTANT:
    - Subject and object must appear in the sentnece.
    - Add some additional context to make the text more natural and informative.
    """
    topic: str = dspy.InputField(
        desc="The topic providing a bit of context about the topic or the domain of thepseudo sentences."
    )

    pseudo_sentences: list[str] = dspy.InputField(
        desc="A list of pseudo sentences in the form of triples."
    )

    fluent_passage_text: str = dspy.OutputField(
        desc="A passage of text describing the same pseudo sentences in a fluent natural language."
    )

    title: str = dspy.OutputField(
        desc="A descriptive and concise title for the passage of text."
    )


class SyntheticGenerator(ABC):

    def __init__(self, batch_size: int=50, worker_count: int=3, verbalizer: dspy.Signature=SyntheticVerbalizer):
        self.batch_size = batch_size
        self.worker_count = worker_count
        self.verbalizer_cot = dspy.ChainOfThought(verbalizer)

    def generate_pseudo_sentences(self, parent_to_child: Dict[str, List]) -> List[PseudoSentence]:
        taxonomy_batcher = TaxonomyBatchifier(parent_to_child=parent_to_child,
                                              batch_size=self.batch_size)
        return taxonomy_batcher.batchify()

    def worker(self, row, topic):
        doc_id = row['id']
        try:
            response = self.verbalizer_cot(topic=topic, pseudo_sentences=row['pseudo_sentences'])
            doc = {
                "id": doc_id,
                "title": response.title,
                "text": response.fluent_passage_text
            }
            return True, doc
        except Exception as e:
            print(f"[ERROR] Processing failed for {doc_id}: {e}")
            return False, None

    def generate_documents(self, pseudo_sentences, topic):
        generated_docs = []
        with ThreadPoolExecutor(max_workers=self.worker_count) as executor:
            futures = {
                executor.submit(self.worker, row, topic): row['id']
                for _, row in pd.DataFrame([ps.dict() for ps in pseudo_sentences]).iterrows()
            }
            for future in tqdm(as_completed(futures), total=len(futures), desc="Processing batches"):
                doc_id = futures[future]
                try:
                    sucess, doc = future.result(timeout=120)  # 2-minute timeout per worker
                    if sucess:
                        generated_docs.append(doc)
                    else:
                        print(f"[ERROR] Document generation failed for {doc_id}")
                except TimeoutError:
                    print(f"[TIMEOUT] Processing timed out for {doc_id}")
                except Exception as e:
                    print(f"[ERROR] Unexpected error for {doc_id}: {e}")
        return generated_docs

    def generate(self, ontological_data: Any, topic: str) -> SyntheticText2OntoData:
        term_types = ontological_data.term_typings
        taxonomic_relations = ontological_data.type_taxonomies

        parent_to_child = defaultdict(list)
        child_to_parent = defaultdict(set)
        for tt in term_types:
            for a_type in tt.types:
                # TODO this has to be handled properly in ontology learning
                if a_type.startswith("N") or tt.term.startswith("N"):
                    continue
                parent_to_child[a_type].append([tt.ID, tt.term, "is a"])
                child_to_parent[tt.term].add(a_type)

        for tr in taxonomic_relations.taxonomies:
            if tr.parent.startswith("N") or tr.child.startswith("N"):
                continue
            parent_to_child[tr.parent].append([tr.ID, tr.child, "is a type of"])
            child_to_parent[tr.child].add(tr.parent)

        child_to_parent = {k: list(v) for k, v in child_to_parent.items()}
        pseudo_sentences = self.generate_pseudo_sentences(parent_to_child=parent_to_child)
        generated_docs = self.generate_documents(pseudo_sentences=pseudo_sentences, topic=topic)

        return SyntheticText2OntoData(
            child_to_parent=child_to_parent,
            pseudo_sentences=pseudo_sentences,
            generated_docs=generated_docs
        )
