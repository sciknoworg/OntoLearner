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

import numpy as np
from typing import List, Dict, Any


def aggregate_metrics(results: List[Dict[str, Any]], task: str) -> Dict[str, float]:
    """
    Aggregate metrics across multiple examples
    """
    metrics = {}

    if not results:
        return metrics

    if task == "term-typing":
        metrics['avg_precision_score'] = np.mean([r['precision_score'] for r in results])
        metrics['avg_recall_score'] = np.mean([r['recall_score'] for r in results])
        metrics['avg_f1_score'] = np.mean([r['f1_score'] for r in results])
        metrics['avg_exact_match'] = np.mean([r['exact_match'] for r in results])

    elif task == "taxonomy-discovery":
        metrics['avg_accuracy'] = np.mean([r['accuracy'] for r in results])
        metrics['avg_f1_score'] = np.mean([r['f1_score'] for r in results])

    elif task == "non-taxonomy-discovery":
        metrics['avg_exact_match'] = np.mean([r['exact_match'] for r in results])
        metrics['avg_similarity'] = np.mean([r['similarity_score'] for r in results])

    metrics['num_samples'] = len(results)

    return metrics
