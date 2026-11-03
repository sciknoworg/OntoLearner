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

import logging
import random
from typing import Any, Dict, List, Optional, Sequence, Tuple

from sklearn.model_selection import train_test_split as sklearn_split

logger = logging.getLogger(__name__)

TRIPLES_KEY = "primitive-ontology-triples"
INITIAL_KEY = "initial-primitive-ontology-triples"
EXTENDED_KEY = "extended-primitive-ontology-triples"


class PrimitiveOntologyDataset:
    """
    Builds the dataset of one primitive-ontology task from the records of ``SyntheticDataPreprocessor``.

    * ``"construction"``: a context and its complete ontology (the LLMs4OL 2026 Flagship task).
    * ``"expansion"``: a context, an initial ontology and the triples that extend it (the Reuse task).

    The task names are the ones ``evaluation_report`` uses; ``"ontology_construction"`` and
    ``"ontology_expansion"`` are accepted too. ``prepare`` never modifies the records, so the same preprocessed
    records can be prepared for both tasks.

    Example:
        >>> dataset = PrimitiveOntologyDataset(task="expansion", random_state=42)
        >>> train_data = dataset.prepare(records)
        >>> test_input, test_gold = dataset.prepare(test_records, test=True), dataset.prepare(test_records)
    """

    TASKS = {"construction": "construction", "ontology_construction": "construction",
             "expansion": "expansion", "ontology_expansion": "expansion"}

    def __init__(self, task: str, random_state: int = 42, existing_ratio: float = 0.5,
                 drop_empty: bool = True) -> None:
        """
        Args:
            task: ``"construction"`` or ``"expansion"``.
            random_state: Seed for the expansion split; the same seed gives the same split.
            existing_ratio: Share of each tail group kept in the initial ontology (expansion).
            drop_empty: Drop expansion samples with nothing to extend.
        """
        if task not in self.TASKS:
            raise ValueError(f"Unsupported task: {task}. Choose 'construction' or 'expansion'.")
        self.task = self.TASKS[task]
        self.random_state = random_state
        self.existing_ratio = existing_ratio
        self.drop_empty = drop_empty

    def prepare(self, records: List[Dict[str, Any]], test: bool = False) -> List[Dict[str, Any]]:
        """
        Format records for the task.

        Args:
            records: ``{"id", "context", "primitive-ontology-triples"}`` records, with ``"terms"`` and
                ``"types"`` unless the alignment filter removed them.
            test: Leave the answers out (the input file of a test set); the gold file is the same call with
                ``test=False``.

        Returns:
            construction: ``{"id", "context", "terms", "types", "primitive-ontology-triples"}``, without
            ``terms`` and ``types`` when the records have none, as in the released train set
            (``{"id", "context"}`` with ``test=True``).
            expansion: ``{"id", "context", "terms", "types", "initial-primitive-ontology-triples",
            "extended-primitive-ontology-triples"}`` (without the extended triples with ``test=True``).
        """
        if self.task == "construction":
            return self._construction(records, test)
        return self._expansion(records, test)

    def split_triples(self, triples: Sequence[Sequence[str]],
                      rng: Optional[random.Random] = None) -> Tuple[List[List[str]], List[List[str]]]:
        """
        Split one record's triples into an initial ontology and the triples that extend it.

        The triples are shuffled and grouped by tail. In each group ``existing_ratio`` of them (at least one) stay
        in the initial ontology, so every extension target attaches to a type that is already there.

        Returns:
            ``(initial, extended)``, both new lists.
        """
        shuffled = [list(t) for t in triples]
        (rng or random.Random(self.random_state)).shuffle(shuffled)
        by_tail: Dict[str, List[List[str]]] = {}
        for triple in shuffled:
            by_tail.setdefault(triple[2], []).append(triple)
        initial, extended = [], []
        for group in by_tail.values():
            cut = max(1, int(len(group) * self.existing_ratio))
            initial.extend(group[:cut])
            extended.extend(group[cut:])
        return initial, extended

    @staticmethod
    def split_by_task(records: List[Dict[str, Any]], expansion_size: float = 0.4,
                      random_state: int = 42) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """
        Split records into a construction part and an expansion part, as in the LLMs4OL 2026 release
        (``expansion_size`` 0.4 for train, 0.5 for test).

        Returns:
            ``(construction_records, expansion_records)``.
        """
        ids = [r["id"] for r in records]
        construction_ids, expansion_ids = sklearn_split(ids, test_size=expansion_size, random_state=random_state)
        by_id = {r["id"]: r for r in records}
        return [by_id[i] for i in construction_ids], [by_id[i] for i in expansion_ids]

    def _construction(self, records: List[Dict[str, Any]], test: bool) -> List[Dict[str, Any]]:
        samples = []
        for record in records:
            sample = {"id": record["id"], "context": record["context"]}
            if not test:
                for key in ("terms", "types"):
                    if key in record:
                        sample[key] = list(record[key])
                sample[TRIPLES_KEY] = [list(t) for t in record[TRIPLES_KEY]]
            samples.append(sample)
        return samples

    def _expansion(self, records: List[Dict[str, Any]], test: bool) -> List[Dict[str, Any]]:
        rng = random.Random(self.random_state)
        samples = []
        for record in records:
            initial, extended = self.split_triples(record[TRIPLES_KEY], rng)
            if self.drop_empty and not extended:
                continue
            terms, types = set(), set()
            for head, relation, tail in extended:
                (terms if relation == "instance-of" else types).add(head)
                types.add(tail)
            sample = {"id": record["id"], "context": record["context"], "terms": sorted(terms),
                      "types": sorted(types), INITIAL_KEY: initial}
            if not test:
                sample[EXTENDED_KEY] = extended
            samples.append(sample)
        logger.info("Expansion: %d samples from %d records.", len(samples), len(records))
        return samples