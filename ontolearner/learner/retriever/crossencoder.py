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
from typing import List
from sentence_transformers import CrossEncoder, SentenceTransformer, util
from tqdm import tqdm
import numpy as np

from ...base import AutoRetriever

logger = logging.getLogger(__name__)


class CrossEncoderRetriever(AutoRetriever):
    """
    A hybrid dense retriever that combines a BiEncoder for fast candidate
    retrieval and a CrossEncoder for accurate reranking.

    This retriever follows a two-stage retrieval process:

    1. **BiEncoder retrieval**:
       Encodes all documents and queries into embeddings.
       Computes approximate nearest neighbors to obtain a set of top-k candidates.

    2. **CrossEncoder reranking**:
       Evaluates each (query, document) pair for semantic relevance.
       Reranks the initial candidates and outputs the final top results.

    This provides an efficient and accurate alternative to pure CrossEncoder
    or pure BiEncoder approaches.
    """

    def __init__(self, bi_encoder_model_id: str = None) -> None:
        """
        Initialize the retriever.

        Args:
            bi_encoder_model_id (str, optional):
                Model ID for the BiEncoder used in the first-stage retrieval.
                If not provided, the CrossEncoder model_id passed to `load()`
                will also be used as the BiEncoder.
        """
        super().__init__()
        self.bi_encoder_model_id = bi_encoder_model_id

    def load(self, model_id: str):
        """
        Load both the BiEncoder and CrossEncoder models.

        Args:
            model_id (str):
                Model ID for the CrossEncoder (reranking model). If no explicit
                BiEncoder ID was given at initialization, this ID is also used
                for the BiEncoder.

        Notes:
            - BiEncoder is used for fast vector similarity search.
            - CrossEncoder is used for slow but accurate reranking.
        """
        if not self.bi_encoder_model_id:
            self.bi_encoder_model_id = model_id
        self.bi_encoder = SentenceTransformer(self.bi_encoder_model_id)
        self.cross_encoder = CrossEncoder(model_id)

    def index(self, inputs: List[str]):
        """
        Pre-encode all documents using the BiEncoder to support efficient
        semantic search.

        Args:
            inputs (List[str]):
                List of documents to index.

        Stores:
            - `self.documents`: Raw input documents.
            - `self.document_embeddings`: Tensor of BiEncoder embeddings.
        """
        self.documents = inputs
        self.document_embeddings = self.bi_encoder.encode(inputs, convert_to_tensor=True, show_progress_bar=True)

    def retrieve(self, query: List[str], top_k: int = 5, rerank_k: int = 100, batch_size: int = 32) -> List[List[str]]:
        """
        Retrieve top-k most relevant documents per query using a two-stage process.

        Stage 1: Retrieve top `rerank_k` documents using BiEncoder embeddings.
        Stage 2: Rerank those candidates using the CrossEncoder, returning `top_k`.

        Args:
            query (List[str]):
                List of user query strings.
            top_k (int):
                Number of final documents to return after reranking.
            rerank_k (int):
                Number of candidates to retrieve before reranking.
            batch_size (int):
                Batch size for CrossEncoder inference.

        Returns:
            List[List[str]]:
                For each query, a list of top-k reranked documents.
        """
        results = []
        # Step 1: Encode queries with the BiEncoder
        query_embeddings = self.bi_encoder.encode(
            query, convert_to_tensor=True, show_progress_bar=True
        )
        # Step 2: Retrieve candidate documents
        hits_batch = util.semantic_search(query_embeddings, self.document_embeddings, top_k=rerank_k)
        # Step 3: Rerank using CrossEncoder
        for i, hits in enumerate(tqdm(hits_batch, desc="Reranking")):
            candidates = [self.documents[hit["corpus_id"]] for hit in hits]
            pairs = [(query[i], doc) for doc in candidates]
            scores = self.cross_encoder.predict(pairs, batch_size=batch_size, show_progress_bar=False)
            reranked_idx = np.argsort(scores)[::-1][:top_k]
            top_docs = [candidates[j] for j in reranked_idx]
            results.append(top_docs)

        return results
