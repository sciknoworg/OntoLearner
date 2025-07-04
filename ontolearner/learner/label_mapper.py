# Copyright 2025 Scientific Knowledge Organization (SciKnowOrg) Research Group.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This script provides an implementation of label mapping using different machine learning approaches.
It defines a base `LabelMapper` class and two specific subclasses:
- `TFIDFLabelMapper`: Uses a TfidfVectorizer and a classifier for label prediction.
- `SetFitShallowLabelMapper`: Uses a pretrained SetFit model for label prediction.
"""
from typing import Dict, List, Tuple, Any
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

class LabelMapper:
    """
    LabelMapper subclass using a TF-IDF vectorizer and a classifier for label prediction.
    """
    def __init__(self,
                 classifier: Any=LogisticRegression(),
                 ngram_range: Tuple=(1, 1),
                 label_dict: Dict[str, List[str]]=None,
                 analyzer: str = 'word',
                 iterator_no: int = 100):
        """
        Initializes the TFIDFLabelMapper with a specified classifier and TF-IDF configuration.

        Parameters:
            classifier (Any): Classifier object (e.g., LogisticRegression, SVC).
            ngram_range (Tuple): Range of n-grams for the TF-IDF vectorizer.
            label_dict (Dict[str, List[str]]): Dictionary mapping each label to a list of candidate phrases.
            analyzer (str): Specifies whether to analyze at the 'word' or 'char' level.
            iterator_no (int): Number of iterations to replicate training data.
        """
        if label_dict is None:
            label_dict = {
                "yes": ["yes", "true"],
                "no": ["no",  "false", " "]
            }
        self.labels = [label.lower() for label in list(label_dict.keys())]
        self.x_train, self.y_train = [], []
        for label, candidates in label_dict.items():
            self.x_train += [label] + candidates
            self.y_train += [label] * (len(candidates) + 1)
        self.x_train = iterator_no * self.x_train
        self.y_train = iterator_no * self.y_train
        assert len(self.x_train) == len(self.y_train)
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer(analyzer=analyzer, ngram_range=ngram_range)),
            ('classifier', classifier)
        ])

    def fit(self):
        """Fits the TF-IDF pipeline on the training data."""
        self.model.fit(self.x_train, self.y_train)

    def validate_predicts(self, preds: List[str]):
        """
        Validates if predictions are among valid labels.

        Parameters:
            preds (List[str]): List of predicted labels.
        """
        for pred in preds:
            if pred.lower() not in self.labels:
                raise AssertionError(f"{pred} in prediction is not a valid label!")

    def predict(self, X: List[str]) -> List[str]:
        """
        Predicts labels for the given input using the TF-IDF pipeline.

        Parameters:
            X (List[str]): List of input texts to classify.

        Returns:
            List[str]: Predicted labels.
        """
        predictions = list(self.model.predict(X))
        self.validate_predicts(predictions)
        return predictions
