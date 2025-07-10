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
from typing import Dict
from .metrics import text2onto_metrics, term_typing_metrics, taxonomy_discovery_metrics, non_taxonomic_re_metrics

def evaluation_report(y_true, y_pred, task: str) -> Dict:
    if task == "text2onto":
        return text2onto_metrics(y_true, y_pred)
    elif task == "term-typing":
        return term_typing_metrics(y_true, y_pred)
    elif task == "taxonomy-discovery":
        return taxonomy_discovery_metrics(y_true, y_pred)
    elif task == "non-taxonomic-re":
        return non_taxonomic_re_metrics(y_true, y_pred)
    else:
        raise ValueError(f"unknown task: {task}")
