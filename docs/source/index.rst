

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/main/images/logo.png" alt="OntoLearner Logo" width="700"/>
   </div>

.. raw:: html

   <div align="center">
     <a href="https://badge.fury.io/py/OntoLearner"><img src="https://badge.fury.io/py/OntoLearner.svg" alt="PyPI version"></a>
     <a href="https://pepy.tech/projects/ontolearner"><img src="https://static.pepy.tech/badge/ontolearner" alt="PyPI Downloads"></a>
     <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
     <a href="https://github.com/pre-commit/pre-commit"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit" alt="pre-commit"></a>
     <a href="https://ontolearner.readthedocs.io/"><img src="https://app.readthedocs.org/projects/ontolearner/badge/" alt="Documentation Status"></a>
     <a href="MAINTANANCE.md"><img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintenance"></a>
     <a href="https://doi.org/10.5281/zenodo.15399773"><img src="https://zenodo.org/badge/913867999.svg" alt="DOI"></a>
   </div>

   <br>
   <br>

OntoLearner is a modular, open-source Python framework purpose-built for modern ontology learning (OL)—the semi-automatic construction and enrichment of ontologies from unstructured sources—powered by Large Language Models (LLMs). Rooted in decades of research in semantic web and NLP, OntoLearner integrates the breadth of existing ontology repositories with the reasoning and generative capabilities of state-of-the-art foundation models. Traditional OL systems often struggled with inconsistency, poor vocabulary alignment, and domain fragmentation. OntoLearner addresses these challenges by combining structured access to curated ontologies with LLM-driven enrichment workflows—enabling scalable, cross-domain ontology development grounded in best practices and FAIR principles.

Unlike general-purpose NLP or embedding libraries, OntoLearner is designed specifically for ontology engineering and OL research. It offers:

.. raw:: html

   <ul>
     <li>✅ Cross-domain coverage with leading repositories like BioPortal, OBO Foundry, OLS, LOV, and FAIRsharing.</li>
     <li>🤖 LLM-assisted modeling for tasks such as term suggestion, concept typing, taxonomy induction, relation extraction, and ontology enrichment.</li>
     <li>🧠 Benchmarking tools to evaluate, compare, and validate LLM-based methods for OL using standardized datasets and metrics.</li>
     <li>🔁 Machine-readable ontologies hosted on Hugging Face, optimized for integration into generative AI pipelines with full support for versioning, streaming, and metadata inspection.</li>
     <li>🔧 Modular APIs and extensible architecture that seamlessly integrate with existing ontology development environments.</li>
   </ul>

A wide selection of over `200 ontologies <https://huggingface.co/collections/SciKnowOrg/>`_ are available for immediate use on 🤗 Hugging Face. Additionally, it is easy to train your own `learner <docs/learners/learners.html>`_ using OntoLearner, enabling you to create custom models for your specific use cases.

OntoLearner was created by `Scientific Knowledge Organization (SciKnowOrg group) <https://github.com/sciknoworg/>`_ at `Technische Informationsbibliothek (TIB) <https://www.tib.eu/de/>`_. Don't hesitate to open an issue on the `OntoLearner repository <https://github.com/sciknoworg/OntoLearner>`_ if something is broken or if you have further questions.

Usage
=====
.. seealso::

   See the `Quickstart <quickstart.html>`_ for more quick information on how to use OntoLearner.

Working with OntoLearner s straightforward:

.. sidebar:: Installation

   You can install *ontolearner* using pip:

   .. code-block:: python

      pip install -U ontolearner

   We recommend **Python 3.10+** and **PyTorch 2.4.0+**. See `installation <installation.html>`_ for further installation options.



.. tab:: Ontologizer Module

   .. code-block:: python

      from ontolearner.ontology import Wine

      # 1. Initialize an ontologizer from OntoLearner
      ontology = Wine()

      # 2. Load the ontology automatically from Hugging Face
      ontology.load()

      # 3. Extract the learning task dataset
      data = ontology.extract()


.. tab:: Learner Module

   .. code-block:: python

      from ontolearner import ontology, utils, learner

      # 1. Load the ontology and extract training data
      onto = ontology.Wine()
      data = onto.extract()

      # 2. Split into train and test sets
      train_data, test_data = utils.train_test_split(
            data, test_size=0.2, random_state=42
      )

      # 3. Initialize a Retrieval-Augmented Generation (RAG) learner
      retriever = learner.BERTRetrieverLearner()
      llm = learner.AutoLearnerLLM()
      prompt = learner.StandardizedPrompting(task="term-typing")

      rag_learner = learner.AutoRAGLearner(
            learner_retriever=retriever,
            learner_llm=llm,
            prompting=prompt
      )

      # 4. Load pretrained components
      rag_learner.load(
            retriever_id="sentence-transformers/all-MiniLM-L6-v2",
            llm_id="mistralai/Mistral-7B-Instruct-v0.1"
      )

      # 5. Fit the model to training data
      rag_learner.fit(train_data=train_data, task="term-typing")

      # 6. Predict on test data
      predicted = rag_learner.predict(test_data, task="term-typing")



Citing
=======

If you find this repository helpful, feel free to cite our publication `LLMs4OL: Large language models for ontology learning <https://link.springer.com/chapter/10.1007/978-3-031-47240-4_22>`_:

 .. code-block:: bibtex

    @inproceedings{babaei2023llms4ol,
      title={LLMs4OL: Large language models for ontology learning},
      author={Babaei Giglou, Hamed and D’Souza, Jennifer and Auer, S{\"o}ren},
      booktitle={International Semantic Web Conference},
      pages={408--427},
      year={2023},
      organization={Springer}
    }

or GitHub repository:

 .. code-block:: bibtex

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



.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :hidden:

   installation
   quickstart
   huggingface

.. toctree::
   :maxdepth: 1
   :caption: Ontologizer
   :hidden:

   ontologizer/ontologizer
   ontologizer/adding_ontologies

.. toctree::
   :maxdepth: 1
   :caption: Learning Tasks
   :hidden:

   learning_tasks/learning_tasks
   learning_tasks/llms4ol
   learning_tasks/text2onto

.. toctree::
   :maxdepth: 1
   :caption: Learner Models
   :hidden:

   learners/learner
   learners/llm
   learners/retrieval
   learners/rag

.. toctree::
   :maxdepth: 4
   :caption: Benchmarking
   :hidden:

   benchmarking/benchmark


.. toctree::
   :maxdepth: 1
   :caption: Package Reference
   :glob:
   :hidden:

   package_reference/base
   package_reference/learner
   package_reference/ontology
