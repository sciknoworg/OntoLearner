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
import numpy as np
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm

from ...base import AutoRetriever

logger = logging.getLogger(__name__)


class NgramRetriever(AutoRetriever):
    """
    A retriever based on traditional n-gram vectorization methods such as TF-IDF
    and CountVectorizer.

    This retriever converts documents and queries into sparse bag-of-ngrams
    vectors and ranks documents using cosine similarity. It is simple,
    interpretable, and suitable for small-scale baselines or non-semantic
    text matching.
    """

    def __init__(self, **vectorizer_kwargs) -> None:
        """
        Initialize the n-gram retriever.

        Args:
            **vectorizer_kwargs: Additional keyword arguments passed directly
                to the scikit-learn vectorizer (e.g., ngram_range, stop_words).
        """
        super().__init__()
        self.vectorizer_kwargs = vectorizer_kwargs
        self.vectorizer = None
        self.embeddings = None

    def load(self, model_id) -> None:
        """
        Load and initialize the vectorizer based on `model_id`.

        Args:
            model_id (str): Either `"tfidf"` for TF-IDF or `"count"` for
                CountVectorizer.

        Raises:
            ValueError: If the model_id is not one of the supported options.
        """
        if model_id == "tfidf":
            self.vectorizer = TfidfVectorizer(**self.vectorizer_kwargs)
        elif model_id == "count":
            self.vectorizer = CountVectorizer(**self.vectorizer_kwargs)
        else:
            raise ValueError(f"Invalid mode '{model_id}'. Choose from ['tfidf', 'count'].")

    def index(self, inputs: List[str]) -> None:
        """
        Fit the vectorizer and index (vectorize) the input documents.

        Args:
            inputs (List[str]): List of text documents to index.

        Notes:
            This method must be run before calling `retrieve()`. It creates the
            document embedding matrix used for similarity search.
        """
        if self.vectorizer is None:
            # Default to TF-IDF if the user never called `load()`
            self.load(model_id="tfidf")

        self.documents = inputs
        logger.info("Fitting vectorizer and transforming documents...")
        self.embeddings = self.vectorizer.fit_transform(inputs)
        logger.info(f"Document embeddings created with shape: {self.embeddings.shape}")

    def retrieve(self, query: List[str], top_k: int = 5, batch_size: int = -1) -> List[List[str]]:
        """
        Retrieve the most similar documents for each query string.

        Args:
            query (List[str]): A list of query strings.
            top_k (int): Number of most similar documents to return per query.
            batch_size (int): Number of queries to process at once.
                Use `-1` to process all queries in a single batch.

        Returns:
            List[List[str]]: For each query, a list containing the top-k
            matching documents.

        Raises:
            RuntimeError: If retrieval is attempted before indexing.
        """
        if self.embeddings is None:
            raise RuntimeError("Retriever must index documents before calling `retrieve()`.")

        logger.info("Vectorizing query text...")
        query_vec = self.vectorizer.transform(query)
        logger.info(f"Query vectors created with shape: {query_vec.shape}")

        results = []
        if batch_size == -1:
            batch_size = len(query)

        for i in tqdm(range(0, len(query), batch_size)):
            q_batch = query_vec[i : i + batch_size]
            sim = cosine_similarity(q_batch, self.embeddings)
            topk_idx = np.argsort(sim, axis=1)[:, ::-1][:, :top_k]
            for row_indices in topk_idx:
                results.append([self.documents[j] for j in row_indices])

        return results
