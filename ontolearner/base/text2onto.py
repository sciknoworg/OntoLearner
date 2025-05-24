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

import json
from abc import ABC
from pathlib import Path
from typing import Any, List, Dict, Union, Set

from ontolearner.data_structure import TextualData, Term, Document, DocumentReference


class BaseText2OntoDataset(ABC):
    """Base class for textual datasets."""
    data_full_name: str = None

    def __init__(self):
        """Initialize the BaseTextualDataset class."""
        self.splits = ["train", "test", "validation"]
        self.data: Dict[str, TextualData] = {}

    def load(self, path: Path) -> dict[str, TextualData]:
        """Load the dataset from the given path."""
        for split in self.splits:
            try:
                self.data[split] = self._load_split(path, split)
            except FileNotFoundError as e:
                print(f"Warning: Could not load {split} split: {e}")
                continue
        return self.data


    def _load_split(self, base_path: Path, split: str) -> TextualData:
        """Load data for a specific split"""
        structure_path = base_path / split

        if not structure_path.exists():
            raise FileNotFoundError(f"Path {structure_path} does not exist")

        return self._load_from_structure(structure_path)


    def _load_from_structure(self, path: Path) -> TextualData:
        """Load data from the new directory structure"""
        # Load raw data from files
        terms_data = self._load_json(path / "terms.json")
        documents_data = self._load_jsonl(path / "documents.jsonl")
        term2documents_data = self._load_json(path / "terms2documents.json")

        terms = [Term(**t) for t in terms_data]
        documents = [Document(**d) for d in documents_data]

        term2documents = {}
        for term_name, doc_entries in term2documents_data.items():
            term2documents[term_name] = [
                DocumentReference(
                    doc_id=entry["doc_id"],
                    extraction_method=entry["extraction_method"]
                )
                for entry in doc_entries
            ]

        return TextualData(
            terms=terms,
            documents=documents,
            term2documents=term2documents
        )

    @staticmethod
    def _load_json(path: Union[str, Path]) -> Any:
        """Load data from JSON file"""
        with open(path, "r") as f:
            return json.load(f)

    @staticmethod
    def _load_jsonl(path: Union[str, Path]) -> List[Dict[str, Any]]:
        """Load data from JSONL file"""
        documents = []
        with open(path, "r") as f:
            for line in f:
                if line.strip():
                    documents.append(json.loads(line))
        return documents

    def get_terms_by_document(self, doc_id: Union[int, str], split: str) -> List[Term]:
        """
        Get terms associated with a specific document
        """
        if split not in self.data:
            raise ValueError(f"Split {split} not loaded. Call load() first.")

        term_list = []
        doc_id_str = str(doc_id)

        for term_name, doc_refs in self.data[split].term2documents.items():
            for doc_ref in doc_refs:
                if str(doc_ref.doc_id) == doc_id_str:
                    # Find the full term data
                    for term in self.data[split].terms:
                        if term.term == term_name:
                            term_list.append(term)
                            break

        return term_list

    def get_statistics(self, split: str) -> Dict[str, Any]:
        """
        Get statistics about the dataset split
        """
        if split not in self.data:
            raise ValueError(f"Split {split} not loaded. Call load() first.")

        data = self.data[split]

        # Count terms by extraction method
        extraction_methods: Dict[str, int] = {}
        for term in data.terms:
            method = term.extraction_method
            extraction_methods[method] = extraction_methods.get(method, 0) + 1

        # Count documents per term
        docs_per_term = {
            term.term: len(data.term2documents.get(term.term, []))
            for term in data.terms
        }

        # Get all unique document IDs that have terms
        docs_with_terms: Set[Union[int, str]] = set()
        for refs in data.term2documents.values():
            for ref in refs:
                docs_with_terms.add(ref.doc_id)

        return {
            "total_terms": len(data.terms),
            "total_documents": len(data.documents),
            "terms_by_extraction_method": extraction_methods,
            "avg_docs_per_term": sum(docs_per_term.values()) / len(docs_per_term) if docs_per_term else 0,
            "docs_with_terms": len(docs_with_terms),
            "docs_coverage_pct": (len(docs_with_terms) / len(data.documents) * 100) if data.documents else 0
        }
