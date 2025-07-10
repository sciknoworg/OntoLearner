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
            prompt_template = """Determine whether the given term can be categorized as an instance of the specified high-level type. Answer with `yes` if it is otherwise answer with `no`. Do not explain.
Term: {term}
Type: {type}
Answer: """
        elif task == "taxonomy-discovery":
            prompt_template = """Is {parent} a direct or indirect superclass (or parent concept) of {child} in a conceptual hierarchy? Answer with yes or no.
Answer: """
        elif task == "non-taxonomic-re":
            prompt_template = """Given the conceptual types `{head}` and `{tail}`, does a `{relation}` relation exist between them? Respond with "yes" if it does, otherwise respond with "no"."""
        else:
            raise ValueError("Unknown task! Current tasks are: 'term-typing', 'taxonomy-discovery', 'non-taxonomic-re'")
        super().__init__(prompt_template)
