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

from ..base.text2onto import BaseText2OntoDataset


class OLLMWikipedia(BaseText2OntoDataset):
    """
    OLLM Wikipedia is a synthetic ontology generated from Wikipedia articles.
    It is used to evaluate the performance of ontology learning algorithms.
    The ontology is generated from the Wikipedia dump and contains concepts and their relationships.

    This class processes OLLM Wikipedia using default textual processing methods.
    """
    dataset_id: str = "OLLMWikipedia"
    dataset_full_name: str = "OLLM Wikipedia Ontology"
