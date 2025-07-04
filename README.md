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


## 🔗 Essential Resources

| Resource                                                                                                                                                                                          | Info |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----|
| **[📚 OntoLearner Documentation](https://ontolearner.readthedocs.io/)**                                                                                                                           | Dive into OntoLearner's extensive documentation to explore its modular architecture, including Ontologizers, Learning Tasks, and Learner Models. The documentation provides detailed guides, references, and tutorials to help you get started and make the most of OntoLearner's capabilities.  |
| **[🤗 Datasets on Hugging Face](https://huggingface.co/collections/SciKnowOrg/ontolearner-benchmarking-6823bcd051300c210b7ef68a)**                                                                | You can access the curated colloctions of machine-readable ontologies across diverse domains such as agriculture, medicine, social sciences, and more. OntoLearner Benchmarking datasets are optimized for integration into generative AI pipelines, supporting versioning, streaming, and metadata inspection.|
| **Quick Tour on OntoLearner** [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1DuElAyEFzd1vtqTjDEXWcc0zCbiV2Yee?usp=sharing) | Follow this hands-on Colab tutorial to explore the complete OntoLearner workflow—from loading ontologies and extracting structured data, to training RAG models and evaluating performance on benchmark tasks. Ideal for researchers, developers, and educators getting started with ontology-centric machine learning. |


## 🚀 Quick Tour
Get started with OntoLearner in just a few lines of code. This guide demonstrates how to initialize ontologies, load datasets, and train an LLM-assisted learner for ontology engineering tasks.

**Basic Usage - Automatic Download from Hugging Face**:
```python
from ontolearner.ontology import Wine

# 1. Initialize an ontologizer from OntoLearner
ontology = Wine()

# 2. Load the ontology automatically from Hugging Face
ontology.load()

# 3. Extract the learning task dataset
data = ontology.extract()
```

To see the ontology metadata you can print the ontology:
```python
print(ontology)
```

**Basic Usage - Manual Download from Hugging Face**:
```python
from ontolearner.ontology import Wine

# 1. Initialize an ontologizer from OntoLearner
ontology = Wine()

# 2. Download the ontology from Hugging Face
ontology.from_huggingface()
```

**LLM-Based Learning Pipeline**:
```python
from ontolearner import ontology, utils, learner
from ontolearner.evaluation import calculate_term_typing_metrics

# 1. Load the ontology and extract training data
onto = ontology.Wine()
data = onto.extract()

# 2. Split into train and test sets
train_data, test_data = utils.train_test_split(
    data, test_size=0.2, random_state=42
)

# 3. Initialize a Retrieval-Augmented Generation (RAG) learner
retriever = learner.BERTRetrieverLearner()
llm = learner.AutoLearnerLLM(token="...") # a token required for LLMs with an access
prompt = learner.StandardizedPrompting(task="term-typing")

rag_learner = learner.AutoRAGLearner(
    learner_retriever=retriever,
    learner_llm=llm,
    prompting=prompt
)

# 4. Load pretrained components
rag_learner.load(
    retriever_id="sentence-transformers/all-MiniLM-L6-v2",
    llm_id="Qwen/Qwen2.5-0.5B-Instruct"
)

# 5. Fit the model to training data
rag_learner.fit(train_data=train_data, task="term-typing")

# 6. Predict on test data
results = []
for typing in test_data.term_typings:
    term = typing.term
    ground_truth = typing.types
    predicted = rag_learner.predict(term, task="term-typing")
    metrics = calculate_term_typing_metrics(predicted, ground_truth)
    results.append({
        'term': term,
        'ground_truth': ground_truth,
        'predicted': predicted,
        **metrics
    })
```

**LearnerPipeline**:
```python
from ontolearner import LearnerPipeline
from ontolearner import ontology, utils

# 1. Load the ontology and extract training data
onto = ontology.Wine()
data = onto.extract()

# 2. Split into train and test sets
train_data, test_data = utils.train_test_split(
    data, test_size=0.2, random_state=42
)

# 3. Specify learner pipeline and models
pipeline = LearnerPipeline(
    task="term-typing",
    retriever_id="sentence-transformers/all-MiniLM-L6-v2",
    llm_id="Qwen/Qwen2.5-0.5B-Instruct",
    hf_token="your_huggingface_token"
)

# 4. fit, predict, and evaluate
results, metrics = pipeline.fit_predict_evaluate(
    train_data=train_data,
    test_data=test_data,
    top_k=3,  # Retrieve top-3 similar examples
    test_limit=-1 # on all samples
)

# 5. printing the results
print(f"RAG F1-Score: {metrics['avg_f1_score']:.3f}")
print(f"RAG Exact Match: {metrics['avg_exact_match']:.3f}")
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
  version      = {v1.0.1},
  doi          = {10.5281/zenodo.15399783},
  url          = {https://doi.org/10.5281/zenodo.15399783},
}
```

***

This software is archived in Zenodo under the DOI [![DOI](https://zenodo.org/badge/913867999.svg)](https://doi.org/10.5281/zenodo.15399773) and is licensed under [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT).
