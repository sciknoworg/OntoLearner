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
    def __init__(self, prompt_template: str = None, task: str = None):
        if prompt_template is None:
            if task == "term-typing":
                prompt_template = """
Given a list of types as candidates to be assigned to the term, identify the most probable types.
Return the types only in the form of a list. Do not provide any explanation outside the list.

Term:
{term}

Candidates Types:
{context}

Response:
"""
            elif task == "taxonomy-discovery":
                prompt_template = """
Is {parent} a parent of {child}?
Answer yes/no. Do not explain.
"""
            elif task == "non-taxonomic-re":
                prompt_template = """
What is the relation between {head} and {tail}? Return only the relation type.
"""

        super().__init__(prompt_template)

    def format(self, **kwargs):
        return self.prompt_template.format(**kwargs)
