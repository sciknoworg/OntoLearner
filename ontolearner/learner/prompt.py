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

from ..base import AutoPrompt

class StandardizedPrompting(AutoPrompt):
    def __init__(self, task: str = None):
        if task == "term-typing":
            prompt_template = """You are performing term typing.

Determine whether the given term is a clear and unambiguous instance of the specified high-level type.

Rules:
- Answer "yes" only if the term commonly and directly belongs to the type.
- Answer "no" if the term does not belong to the type, is ambiguous, or only weakly related.
- Use the most common meaning of the term.
- Do not explain your answer.

Term: {term}
Type: {type}
Answer (yes or no):"""
        elif task == "taxonomy-discovery":
            prompt_template =  """You are identifying taxonomic (is-a) relationships.

Question:
Is "{parent}" a superclass (direct or indirect) of "{child}" in a standard conceptual or ontological hierarchy?

Rules:
- A superclass means: "{child}" is a type or instance of "{parent}".
- Answer "yes" only if the relationship is a true is-a relationship.
- Answer "no" for part-of, related-to, or associative relationships.
- Use general world knowledge.
- Do not explain.

Parent: {parent}
Child: {child}
Answer (yes or no):"""
        elif task == "non-taxonomic-re":
            prompt_template = """You are identifying non-taxonomic conceptual relationships.

Given two conceptual types, determine whether the specified relation typically holds between them.

Rules:
- Answer "yes" only if the relation commonly and meaningfully applies.
- Answer "no" if the relation is rare, indirect, or context-dependent.
- Do not infer relations that require specific situations.
- Do not explain.

Head type: {head}
Tail type: {tail}
Relation: {relation}
Answer (yes or no):"""
        else:
            raise ValueError("Unknown task! Current tasks are: 'term-typing', 'taxonomy-discovery', 'non-taxonomic-re'")
        super().__init__(prompt_template)
