<div align="center">
  <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/main/images/logo.png" alt="OntoLearner Logo"/>
</div>

<h3 align="center">OntoLearner: A Modular Python Library for Ontology Learning with LLMs</h3>

<div align="center">

[![PyPI version](https://badge.fury.io/py/OntoLearner.svg)](https://badge.fury.io/py/OntoLearner)
[![PyPI Downloads](https://static.pepy.tech/badge/ontolearner)](https://pepy.tech/projects/ontolearner)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Hugging Face Collection](https://img.shields.io/badge/🤗HuggingFace-Collection-blue)](https://huggingface.co/collections/SciKnowOrg/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Documentation Status](https://app.readthedocs.org/projects/ontolearner/badge/)](https://ontolearner.readthedocs.io/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](MAINTANANCE.md)
[![DOI](https://zenodo.org/badge/913867999.svg)](https://doi.org/10.5281/zenodo.15399773)


</div>

**OntoLearner**  is a modular and extensible architecture designed to support ontology learning and reuse. The conceptual and functional architecture of OntoLearner is shown as following. The framework comprises three core components—**Ontologizers**, **Learning Tasks**, and **Learner Models**—structured to enable reusable and customizable ontology engineering workflows.

## 🧪 Installation

OntoLearner is available on [PyPI](https://pypi.org/project/OntoLearner/) and you can install using `pip`:

```bash
pip install ontolearner
```

Next, verify the installation:
```python
import ontolearner

print(ontolearner.__version__)
```

Please refer to [Installation](https://ontolearner.readthedocs.io/installation.html) page for further options.

## 🔗 Essential Resources

| Resource                                                                                                                                                                                                            | Info                                                                                                                                                                                                                                                                                                                     |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **[📚 OntoLearner Documentation](https://ontolearner.readthedocs.io/)**                                                                                                                                             | OntoLearner's extensive documentation website.                                                                                                                                                                                                                                                                           |
| **[🤗 Datasets on Hugging Face](https://huggingface.co/collections/SciKnowOrg/ontolearner-benchmarking-6823bcd051300c210b7ef68a)**                                                                                  | Access curated, machine-readable ontologies.                                                                                                                                                                                                                                                                             |
| **Quick Tour on OntoLearner** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DuElAyEFzd1vtqTjDEXWcc0zCbiV2Yee?usp=sharing) ``version=1.2.1`` | OntoLearner hands-on Colab tutorials. |
| **[🚀 Quickstart](https://ontolearner.readthedocs.io/quickstart.html)**                                                                                                                                             | Get started quickly with OntoLearner’s main features and workflow.                                                                                                                                                                                                                                                       |
| **[🕸️ Learning Tasks](https://ontolearner.readthedocs.io/learning_tasks/learning_tasks.html)**                                                                                                                     | Explore supported ontology learning tasks like LLMs4OL Paradigm tasks and Text2Onto.                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                    |
| **[🧠 Learner Models](https://ontolearner.readthedocs.io/learners/llm.html)**                                                                                                                                       | Browse and configure various learner models, including LLMs, Retrieval, or RAG approaches.                                                                                                                                                                                                                               |
| **[📚 Ontologies Documentations](https://ontolearner.readthedocs.io/benchmarking/benchmark.html)**                                                                                                                  | Review benchmark ontologies and datasets used for evaluation and training.                                                                                                                                                                                                                                               |
| **[🧩 How to work with Ontologizer?](https://ontolearner.readthedocs.io/ontologizer/ontology_modularization.html)**                                                                                                 | Learn how to modularize and preprocess ontologies using the Ontologizer module.                                                                                                                                                                                                                                          |

## 🚀 Quick Tour
Get started with OntoLearner in just a few lines of code. This guide demonstrates how to initialize ontologies, load datasets, and train an LLM-assisted learner for ontology engineering tasks.

**Basic Usage - Automatic Download from Hugging Face**:
```python
from ontolearner import Wine

# 1. Initialize an ontologizer from OntoLearner
ontology = Wine()

# 2. Load the ontology automatically from HuggingFace
ontology.load()

# 3. Extract the learning task dataset
data = ontology.extract()
```

To see the ontology metadata you can print the ontology:
```python
print(ontology)
```

Now, explore [150+ ready-to-use ontologies](https://ontolearner.readthedocs.io/benchmarking/benchmark.html) or read on [how to work with ontologizers](https://ontolearner.readthedocs.io/ontologizer/ontology_modularization.html).

**Learner Models**:

```python
from ontolearner import AutoRetrieverLearner, AgrO, train_test_split, evaluation_report

# 1. Programmatic import of an ontology
ontology = AgrO()
ontology.load()

# 2. Load tasks datasets
ontological_data = ontology.extract()

# 3. Split into train and test sets
train_data, test_data = train_test_split(ontological_data, test_size=0.2, random_state=42)

# 4. Initialize Learner
task = 'non-taxonomic-re'
ret_learner = AutoRetrieverLearner(top_k=5)
ret_learner.load(model_id='sentence-transformers/all-MiniLM-L6-v2')

# 5. Fit the model to training data and do the predict
ret_learner.fit(train_data, task=task)
predicts = ret_learner.predict(test_data, task=task)

# 6. Evaluation
truth = ret_learner.tasks_ground_truth_former(data=test_data, task=task)
metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
print(metrics)
```
Other learners:
* [LLM-Based Learner](https://ontolearner.readthedocs.io/learners/llm.html)
* [RAG-Based Learner](https://ontolearner.readthedocs.io/learners/rag.html)

**LearnerPipeline**: The OntoLearner also offers a streamlined `LearnerPipeline` class that simplifies the entire process of initializing, training, predicting, and evaluating a RAG setup into a single call.



```python
# Import core components from the OntoLearner library
from ontolearner import LearnerPipeline, AgrO, train_test_split

# Load the AgrO ontology, which includes structured agricultural knowledge
ontology = AgrO()
ontology.load()  # Load ontology data (e.g., entities, relations, metadata)

# Extract relation instances from the ontology and split them into training and test sets
train_data, test_data = train_test_split(
    ontology.extract(),      # Extract annotated (head, tail, relation) triples
    test_size=0.2,           # 20% for evaluation
    random_state=42          # Ensures reproducible splits
)

# Initialize the learning pipeline using a dense retriever
pipeline = LearnerPipeline(
    retriever_id='sentence-transformers/all-MiniLM-L6-v2',  # Hugging Face model ID for retrieval
    batch_size=10,       # Number of samples to process per batch (if batching is enabled internally)
    top_k=5              # Retrieve top-5 most relevant support instance per query
)

# Run the pipeline on the training and test data
# The pipeline performs: fit() → predict() → evaluate() in sequence
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    evaluate=True,           # If True, computes precision, recall, and F1-score
    task='non-taxonomic-re'  # Specifies that we are doing non-taxonomic relation prediction
)

# Print the evaluation metrics (precision, recall, F1)
print("Metrics:", outputs['metrics'])

# Print the total elapsed time for training and evaluation
print("Elapsed time:", outputs['elapsed_time'])

# Print the full output dictionary (includes predictions)
print(outputs)
```

## ⭐ Contribution

We welcome contributions to enhance OntoLearner and make it even better! Please review our contribution guidelines in [CONTRIBUTING.md](CONTRIBUTING.md) before getting started. You are also welcome to assist with the ongoing maintenance by referring to [MAINTENANCE.md](MAINTENANCE.md). Your support is greatly appreciated.


If you encounter any issues or have questions, please submit them in the [GitHub issues tracker](https://github.com/sciknoworg/OntoLearner/issues).


## 💡 Acknowledgements

If you find this repository helpful or use OntoLearner in your work or research, feel free to cite our publication:

```bibtex
@inproceedings{babaei2023llms4ol,
  title={LLMs4OL: Large language models for ontology learning},
  author={Babaei Giglou, Hamed and D’Souza, Jennifer and Auer, S{\"o}ren},
  booktitle={International Semantic Web Conference},
  pages={408--427},
  year={2023},
  organization={Springer}
}
```
or:
```bibtex
@software{babaei_giglou_2025_15399783,
  author       = {Babaei Giglou, Hamed and D'Souza, Jennifer and Aioanei, Andrei and Mihindukulasooriya, Nandana and Auer, Sören},
  title        = {OntoLearner: A Modular Python Library for Ontology Learning with LLMs},
  month        = may,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {v1.3.0},
  doi          = {10.5281/zenodo.15399783},
  url          = {https://doi.org/10.5281/zenodo.15399783},
}
```

***

This software is archived in Zenodo under the DOI [![DOI](https://zenodo.org/badge/913867999.svg)](https://doi.org/10.5281/zenodo.15399773) and is licensed under [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT).
