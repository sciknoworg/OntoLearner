

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
      <li>✅ <strong>Cross-domain coverage</strong> with leading repositories like BioPortal, OBO Foundry, OLS, LOV, and FAIRsharing.</li>
      <li>🤖 <strong>LLM-assisted modeling</strong> for tasks such as term suggestion, concept typing, taxonomy induction, relation extraction, and ontology enrichment.</li>
      <li>🧠 <strong>Benchmarking tools</strong> to evaluate, compare, and validate LLM-based methods for OL using standardized datasets and metrics.</li>
      <li>🔁 <strong>Machine-readable ontologies</strong> hosted on Hugging Face, optimized for integration into generative AI pipelines with full support for versioning, streaming, and metadata inspection.</li>
      <li>🔧 <strong>Modular and extensible architecture</strong> that seamlessly integrate with existing ontology development environments.</li>
    </ul>

A wide selection of over `200 ontologies <https://huggingface.co/collections/SciKnowOrg/>`_
are available for immediate use on 🤗 Hugging Face.

OntoLearner was created by `Scientific Knowledge Organization (SciKnowOrg group) <https://github.com/sciknoworg/>`_
at `Technische Informationsbibliothek (TIB) <https://www.tib.eu/de/>`_. Don't hesitate to open an issue
on the `OntoLearner repository <https://github.com/sciknoworg/OntoLearner>`_ if something is broken or if you have further questions.

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

        from ontolearner import AgrO

        # 1. Initialize an ontologizer from OntoLearner
        ontology = AgrO()

        # 2. Load the ontology automatically from Hugging Face
        ontology.load()

        # 3. Extract the learning task dataset
        data = ontology.extract()

        print(ontology)
        # outputs:
        # ontology_id: AgrO
        # ontology_full_name: Agronomy Ontology (AgrO)
        # domain: Agriculture
        # category: Agronomy
        # version: 1.0
        # last_updated: 2022-11-02
        # creator: The Crop Ontology Consortium
        # license: Creative Commons 4.0
        # format: RDF
        # download_url: https://agroportal.lirmm.fr/ontologies/AGRO?p=summary



.. tab:: Learner Module

   .. code-block:: python

        from ontolearner import LearnerPipeline, AgrO, train_test_split

        # Load the AgrO ontology
        ontology = AgrO()
        ontology.load()

        # Extract term-typing instances and split into train and test sets
        train_data, test_data = train_test_split(
            ontology.extract(),
            test_size=0.2,
            random_state=42
        )

        # Initialize a multi-component learning pipeline (retriever + LLM)
        # This configuration enables a Retrieval-Augmented Generation (RAG) setup
        pipeline = LearnerPipeline(
            retriever_id='sentence-transformers/all-MiniLM-L6-v2',
            llm_id='Qwen/Qwen2.5-0.5B-Instruct',
            hf_token='...',
            batch_size=32,
            top_k=5
        )

        # Run the pipeline: training, prediction, and evaluation in one call
        outputs = pipeline(
            train_data=train_data,
            test_data=test_data,
            evaluate=True,              # Compute metrics like precision, recall, and F1
            task='term-typing'          # Specifies the task
        )

        # Print final evaluation metrics
        print("Metrics:", outputs['metrics'])

        # Print the total time taken for the full pipeline execution
        print("Elapsed time:", outputs['elapsed_time'])

        # Print all outputs
        print(outputs)


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

.. toctree::
   :maxdepth: 1
   :caption: Ontologizer
   :hidden:

   ontologizer/ontology_modularization
   ontologizer/ontology_hosting
   ontologizer/new_ontologies
   ontologizer/metadata

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

   package_reference/ontologizer
   package_reference/text2onto
   package_reference/learner
   package_reference/data_structure
   package_reference/evaluation
   package_reference/tools
   package_reference/utils
   package_reference/pipeline
