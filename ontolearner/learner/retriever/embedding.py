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
import torch
import torch.nn.functional as F
import numpy as np

from tqdm import tqdm
from typing import List, Optional
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import KeyedVectors
from gensim.utils import simple_preprocess

from ...base import AutoRetriever

logger = logging.getLogger(__name__)


class Word2VecRetriever(AutoRetriever):
    """
    Retriever that encodes each document by averaging its Word2Vec-style
    word embeddings. Retrieval is performed by cosine similarity between
    averaged document vectors and averaged query vectors.
    """

    def __init__(self) -> None:
        """
        Initialize an empty Word2VecRetriever. The model must be loaded using
        :meth:`load` before indexing or retrieval.
        """
        super().__init__()
        self.embedding_model: Optional[KeyedVectors] = None
        self.documents: List[str] = []
        self.embeddings: Optional[torch.Tensor] = None

    def load(self, model_id: str) -> None:
        """
        Load a pre-trained Word2Vec KeyedVectors model.

        Args:
            model_id (str):
                Path to a Word2Vec `.bin` or `.txt` vector file.
        """
        self.embedding_model = KeyedVectors.load_word2vec_format(model_id, binary=True)

    def _encode_text(self, text: str) -> np.ndarray:
        """
        Encode text by averaging embeddings for all in-vocabulary words.

        Args:
            text (str): Input text string.

        Returns:
            np.ndarray: Averaged embedding vector. If no word is in the vocabulary,
            a zero vector of appropriate dimensionality is returned.
        """
        if self.embedding_model is None:
            raise RuntimeError("Word2Vec model must be loaded before encoding.")

        words = simple_preprocess(text)
        valid_vectors = [self.embedding_model[word] for word in words if word in self.embedding_model]

        if not valid_vectors:
            return np.zeros(self.embedding_model.vector_size)

        return np.mean(valid_vectors, axis=0)

    def index(self, inputs: List[str]) -> None:
        """
        Encode and index a list of documents.

        Args:
            inputs (List[str]): Documents to index.

        Stores:
            - self.documents: The input documents.
            - self.embeddings: L2-normalized document embeddings.
        """
        self.documents = inputs
        embeddings = [self._encode_text(doc) for doc in tqdm(inputs)]
        self.embeddings = F.normalize(torch.tensor(np.stack(embeddings)), p=2, dim=1)

    def retrieve(self, query: List[str], top_k: int = 5, batch_size: int = -1) -> List[List[str]]:
        """
        Retrieve the top-k most similar documents for each query.

        Args:
            query (List[str]): Query texts.
            top_k (int): Number of results to return per query.
            batch_size (int): Batch size for processing queries. -1 means all at once.

        Returns:
            List[List[str]]: One list per query containing top-k matching documents.
        """
        if self.embeddings is None:
            raise RuntimeError("Documents must be indexed before retrieval.")

        query_vec = [self._encode_text(q) for q in query]
        query_vec = F.normalize(torch.tensor(np.stack(query_vec)), p=2, dim=1)

        if batch_size == -1:
            batch_size = len(query)

        results = []
        for i in tqdm(range(0, len(query), batch_size)):
            q_batch = query_vec[i:i + batch_size]
            sim = cosine_similarity(q_batch, self.embeddings)

            topk_idx = np.argsort(sim, axis=1)[:, ::-1][:, :top_k]

            for row in topk_idx:
                results.append([self.documents[j] for j in row])

        return results


class GloveRetriever(AutoRetriever):
    """
    Retriever that uses GloVe embedding vectors. Each document is encoded
    by averaging the embeddings of all words that exist in the GloVe vocabulary.
    """

    def __init__(self) -> None:
        """
        Initialize an empty GloveRetriever. Model must be loaded before use.
        """
        super().__init__()
        self.embedding_model: Optional[dict] = None
        self.documents: List[str] = []
        self.embeddings: Optional[torch.Tensor] = None

    def load(self, model_id: str) -> None:
        """
        Load GloVe embeddings from a text file.

        Args:
            model_id (str):
                Path to GloVe `.txt` file, e.g. `glove.6B.300d.txt`.
        """
        logger.info(f"Loading GloVe embeddings from {model_id} ...")
        self.embedding_model = {}

        with open(model_id, "r", encoding="utf8") as f:
            for line in f:
                values = line.split()
                word = values[0]
                vec = [float(v) for v in values[1:]]
                self.embedding_model[word] = vec

        logger.info(f"Loaded {len(self.embedding_model)} GloVe words.")

    def _encode_text(self, text: str) -> np.ndarray:
        """
        Encode text by averaging GloVe embeddings.

        Args:
            text (str): Input text.

        Returns:
            np.ndarray: Averaged embedding vector. Returns zero vector if no words match.
        """
        if self.embedding_model is None:
            raise RuntimeError("GloVe model must be loaded before encoding.")

        words = text.lower().split()
        vecs = [self.embedding_model[w] for w in words if w in self.embedding_model]

        if not vecs:
            dim = len(next(iter(self.embedding_model.values())))
            return np.zeros(dim)

        return np.mean(vecs, axis=0)

    def index(self, inputs: List[str]) -> None:
        """
        Index a list of documents by encoding and normalizing them.

        Args:
            inputs (List[str]): Documents to index.
        """
        if self.embedding_model is None:
            raise RuntimeError("You must load a GloVe model before indexing.")

        self.documents = inputs
        embeddings = [self._encode_text(doc) for doc in tqdm(inputs)]
        self.embeddings = F.normalize(torch.tensor(np.stack(embeddings)), p=2, dim=1)

    def retrieve(self, query: List[str], top_k: int = 5, batch_size: int = -1) -> List[List[str]]:
        """
        Retrieve top-k most similar documents.

        Args:
            query (List[str]): Query texts.
            top_k (int): Number of results per query.
            batch_size (int): Batch size for query computation.

        Returns:
            List[List[str]]: Each entry is a list of top-k matching documents.
        """
        if self.embeddings is None:
            raise RuntimeError("Documents must be indexed before retrieval.")

        query_vec = [self._encode_text(q) for q in query]
        query_vec = F.normalize(torch.tensor(np.stack(query_vec)), p=2, dim=1)

        if batch_size == -1:
            batch_size = len(query)

        results = []
        for i in tqdm(range(0, len(query), batch_size)):
            q_batch = query_vec[i:i + batch_size]
            sim = cosine_similarity(q_batch, self.embeddings)
            topk_idx = np.argsort(sim, axis=1)[:, ::-1][:, :top_k]

            for row in topk_idx:
                results.append([self.documents[j] for j in row])

        return results
