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
from typing import Any, Dict, List, Sequence, Tuple

class PrimitiveOntologyDataset:
    """
    Prepare primitive ontology datasets for two tasks.

    ontology_construction:
        Context -> Complete primitive ontology

    ontology_expansion:
        Context + Initial ontology -> Extended ontology

    All supplied records are processed for the selected task.
    Train, validation, and test records have the same schema.
    """

    TRIPLES_KEY = "primitive-ontology-triples"
    INITIAL_KEY = "initial-primitive-ontology-triples"
    EXTENDED_KEY = "extended-primitive-ontology-triples"

    def __init__(
        self,
        task: str,
        random_state: int = 42,
    ) -> None:

        if task not in ("ontology_construction", "ontology_expansion"):
            raise ValueError(
                "task must be 'ontology_construction' or 'ontology_expansion'."
            )

        self.task = task
        self.random_state = random_state

    def prepare(
        self,
        records: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """
        Prepare all records for the selected ontology task.
        """

        if self.task == "ontology_construction":
            return self._construction(records)

        return self._expansion(records)

    def split_triples(
        self,
        triples: Sequence[Sequence[str]],
        rng: random.Random,
    ) -> Tuple[List[List[str]], List[List[str]]]:
        """
        Split complete ontology triples into initial and extended.

        Triples are grouped by tail.
        Approximately half of each group is retained as initial,
        with at least one triple per group.
        """

        shuffled = [list(triple) for triple in triples]
        rng.shuffle(shuffled)

        groups: Dict[str, List[List[str]]] = {}

        for triple in shuffled:
            groups.setdefault(triple[2], []).append(triple)

        initial = []
        extended = []

        for group in groups.values():
            cut = max(1, len(group) // 2)

            initial.extend(group[:cut])
            extended.extend(group[cut:])

        return initial, extended

    def _construction(
        self,
        records: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """
        Prepare records for ontology construction.
        """

        samples = []

        for record in records:

            sample = {
                "id": record["id"],
                "context": record["context"],
            }

            for key in ("terms", "types"):
                if key in record:
                    sample[key] = list(record[key])

            sample[self.TRIPLES_KEY] = [
                list(triple)
                for triple in record[self.TRIPLES_KEY]
            ]

            samples.append(sample)

        return samples

    def _expansion(
        self,
        records: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """
        Prepare records for ontology expansion.

        Each record's triples are divided into:
        - Initial ontology
        - Extended ontology
        """

        rng = random.Random(self.random_state)
        samples = []

        for record in records:

            initial, extended = self.split_triples(
                record[self.TRIPLES_KEY],
                rng,
            )

            # Skip records without any extension triples.
            if not extended:
                continue

            terms = set()
            types = set()

            for head, relation, tail in extended:

                if relation == "instance-of":
                    terms.add(head)
                else:
                    types.add(head)

                types.add(tail)

            sample = {
                "id": record["id"],
                "context": record["context"],
                "terms": sorted(terms),
                "types": sorted(types),
                self.INITIAL_KEY: initial,
                self.EXTENDED_KEY: extended,
            }

            samples.append(sample)

        return samples
