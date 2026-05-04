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
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](MAINTENANCE.md)
[![DOI](https://zenodo.org/badge/913867999.svg)](https://doi.org/10.5281/zenodo.15399773)

</div>

---

**OntoLearner** is a modular and extensible Python library for **ontology learning** powered by Large Language Models (LLMs). It provides a unified framework covering the full workflow — from loading and modularizing ontologies to training, predicting, and evaluating learner models across multiple ontology learning tasks.

The framework is built around three core components:

- 🧩 **Ontologizers** — load, parse, and modularize ontologies from 150+ ready-to-use sources across 20+ domains.
- 📋 **Learning Tasks** — support for Term Typing, Taxonomy Discovery, Non-Taxonomic Relation Extraction, and Text2Onto.
- 🤖 **Learner Models** — plug-and-play LLM, Retriever, and RAG-based learners with a consistent `fit → predict → evaluate` interface.

---

## 🧪 Installation

OntoLearner is available on [PyPI](https://pypi.org/project/OntoLearner/) and can be installed with `pip`:

```bash
pip install ontolearner
```

Verify the installation:

```python
import ontolearner

print(ontolearner.__version__)
```

> For additional installation options (e.g., from source, with optional dependencies), see the [Installation Guide](https://ontolearner.readthedocs.io/installation.html).

---

## 🔗 Essential Resources

| Resource | Description |
|:---------|:------------|
| **[📚 Documentation](https://ontolearner.readthedocs.io/)** | Full documentation website. |
| **[🤗 Datasets on Hugging Face](https://huggingface.co/collections/SciKnowOrg/ontolearner-benchmarking-6823bcd051300c210b7ef68a)** | Curated, machine-readable ontology datasets. |
| **[🚀 Quickstart](https://ontolearner.readthedocs.io/quickstart.html)** | Get started in minutes. |
| **[🕸️ Learning Tasks](https://ontolearner.readthedocs.io/learning_tasks/learning_tasks.html)** | Term Typing, Taxonomy Discovery, Relation Extraction, and Text2Onto. |
| **[🧠 Learner Models](https://ontolearner.readthedocs.io/learners/llm.html)** | LLM, Retriever, and RAG-based learner models. |
| **[📖 Ontologies Documentation](https://ontolearner.readthedocs.io/benchmarking/benchmark.html)** | Browse 150+ benchmark ontologies across 20+ domains. |
| **[🧩 Ontologizer Guide](https://ontolearner.readthedocs.io/ontologizer/ontology_modularization.html)** | How to modularize and preprocess ontologies. |
| **[📊 Metrics Dashboard](https://huggingface.co/spaces/SciKnowOrg/OntoLearner-Benchmark-Metrics)** | Explore benchmark ontology metrics and complexity scores. |

---

## ✨ Key Features

- **150+ Ontologizers** across 20+ domains (biology, medicine, agriculture, chemistry, law, finance, and more).
- **Multiple learning tasks**: Term Typing, Taxonomy Discovery, Non-Taxonomic Relation Extraction, and Text2Onto.
- **Three learner paradigms**: LLM-based, Retriever-based, and Retrieval-Augmented Generation (RAG).
- **Hugging Face integration**: auto-download ontologies and models directly from the Hub.
- **Unified API**: consistent `fit → predict → evaluate` interface across all learners.
- **LearnerPipeline**: end-to-end pipeline in a single call.
- **Extensible**: easily plug in custom ontologies, learners, or retrievers.
- **Text2Onto generation**: synthetic document generation now uses a direct `transformers` backend with ontology-aware context enrichment.

---

## 🚀 Quick Tour

### Loading an Ontology

Load any of the 150+ built-in ontologies and extract task datasets in just a few lines:

```python
from ontolearner import Wine

# Initialize an ontologizer
ontology = Wine()

# Auto-download from Hugging Face and load
ontology.load()

# Extract learning task datasets
data = ontology.extract()

# Inspect ontology metadata
print(ontology)
```

> Explore [150+ ready-to-use ontologies](https://ontolearner.readthedocs.io/benchmarking/benchmark.html) or learn [how to work with ontologizers](https://ontolearner.readthedocs.io/ontologizer/ontology_modularization.html).

---

### Retriever-Based Learner

Use a dense retriever model to perform non-taxonomic relation extraction:

```python
from ontolearner import AutoRetrieverLearner, AgrO, train_test_split, evaluation_report

# Load and extract ontology data
ontology = AgrO()
ontology.load()
ontological_data = ontology.extract()

# Split into train and test sets
train_data, test_data = train_test_split(ontological_data, test_size=0.2, random_state=42)

# Initialize and load a retriever-based learner
task = 'non-taxonomic-re'
ret_learner = AutoRetrieverLearner(top_k=5)
ret_learner.load(model_id='sentence-transformers/all-MiniLM-L6-v2')

# Fit on training data and predict on test data
ret_learner.fit(train_data, task=task)
predicts = ret_learner.predict(test_data, task=task)

# Evaluate predictions
truth = ret_learner.tasks_ground_truth_former(data=test_data, task=task)
metrics = evaluation_report(y_true=truth, y_pred=predicts, task=task)
print(metrics)
```

Other available learners:
- [LLM-Based Learner](https://ontolearner.readthedocs.io/learners/llm.html)
- [Retriever-Based Learner](https://ontolearner.readthedocs.io/learners/retrieval.html)
- [RAG-Based Learner](https://ontolearner.readthedocs.io/learners/rag.html)
- [LLMs4OL Challenge Learners](https://ontolearner.readthedocs.io/learners/llms4ol.html)

---

### LearnerPipeline

`LearnerPipeline` consolidates the entire workflow — initialization, training, prediction, and evaluation — into a single call:

```python
from ontolearner import LearnerPipeline, AgrO, train_test_split

# Load ontology and extract data
ontology = AgrO()
ontology.load()

train_data, test_data = train_test_split(
    ontology.extract(),
    test_size=0.2,
    random_state=42
)

# Initialize the pipeline with a dense retriever
pipeline = LearnerPipeline(
    retriever_id='sentence-transformers/all-MiniLM-L6-v2',
    batch_size=10,
    top_k=5
)

# Run: fit → predict → evaluate
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    evaluate=True,
    task='non-taxonomic-re'
)

print("Metrics:", outputs['metrics'])
print("Elapsed time:", outputs['elapsed_time'])
```

---

## ⭐ Contribution

We welcome contributions of all kinds — bug reports, new features, documentation improvements, or new ontologies!

Please review our guidelines before getting started:
- [CONTRIBUTING.md](CONTRIBUTING.md) — contribution guidelines
- [MAINTENANCE.md](MAINTENANCE.md) — ongoing maintenance notes

For bugs or questions, please open an issue in the [GitHub Issue Tracker](https://github.com/sciknoworg/OntoLearner/issues).

---

## 💡 Acknowledgements

If OntoLearner is useful in your research or work, please consider citing one of our publications:

```bibtex
@inproceedings{babaei2023llms4ol,
  title     = {LLMs4OL: Large Language Models for Ontology Learning},
  author    = {Babaei Giglou, Hamed and D'Souza, Jennifer and Auer, S{\"o}ren},
  booktitle = {International Semantic Web Conference},
  pages     = {408--427},
  year      = {2023},
  organization = {Springer}
}
```

```bibtex
@software{babaei_giglou_2025_15399783,
  author    = {Babaei Giglou, Hamed and D'Souza, Jennifer and Aioanei, Andrei
               and Mihindukulasooriya, Nandana and Auer, Sören},
  title     = {OntoLearner: A Modular Python Library for Ontology Learning with LLMs},
  month     = may,
  year      = 2025,
  publisher = {Zenodo},
  version   = {v1.3.0},
  doi       = {10.5281/zenodo.15399783},
  url       = {https://doi.org/10.5281/zenodo.15399783}
}
```

---

This software is archived on Zenodo under [![DOI](https://zenodo.org/badge/913867999.svg)](https://doi.org/10.5281/zenodo.15399773) and is licensed under [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT).
