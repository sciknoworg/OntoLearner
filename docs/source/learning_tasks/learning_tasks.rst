Ontology Learning Tasks
==========================

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/refs/heads/main/docs/source/images/learning_tasks.jpg" alt="OntoLearner Logo" width="90%"/>
   </div>
   <br>

.. sidebar:: Tasks

    * `LLMs4OL Paradigm Tasks <https://ontolearner.readthedocs.io/learning_tasks/llms4ol.html>`_
    * `Text2Onto <https://ontolearner.readthedocs.io/learning_tasks/text2onto.html>`_.

Within the OntoLearner framework, the modularized ontologies are extended with OL capabilities to effectively support ontology engineering tasks. This extension is guided by the **LLMs4OL paradigm** tasks, which leverages LLMs to automate the key ontology learning process. The LLMs4OL paradigm is structured around three primary tasks essential for developing a primitive ontology: 1) Term Typing, 2) Taxonomy Discovery, and 3) Non-Taxonomic Relationship Extraction.  By incorporating these tasks, OntoLearner ensures that its modularized ontologies through Ontologizer are not only structured and reusable but also capable of continuous learning and enhancement through automated ontology learning techniques.

Additionally, OntoLearner incorporates a **Text2Onto**, which focuses on extracting ontological terms and types directly from raw text. Notably, Text2Onto is designed to function independently of the LLMs4OL pipeline, and Ontologizer. Users can import or load LLMs4OL tasks as inputs to Text2Onto, enabling flexible and extensible data extraction workflows for OL.

LLMs4OL Paradigm
-------------------

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/refs/heads/dev/docs/source/images/LLMs4OL.png" alt="OntoLearner Logo" width="100%"/>
   </div>
   <br>

The LLMs4OL (Large Language Models for Ontology Learning) paradigm represents
a transformative approach to automated ontology construction and enrichment. OntoLearner implements state-of-the-art LLM-based methodologies that leverage the vast knowledge encoded in pre-trained language models to perform sophisticated ontological reasoning and knowledge extraction.

.. hint::

    The LLMs4OL paper is available online and can be accessed via `this link <https://doi.org/10.1007/978-3-031-47240-4_22>`_.

Text2Onto
----------------

The Text2Onto task aims for **extracting ontological terminologies and types from a raw text**. So, for given an unstructured text corpus/documents, the goal is to identify foundational elements for ontology construction by recognizing domain-relevant vocabulary and categorizing it appropriately.

We aim to extract:

* **Terms (or Entities)**: These are specific terms that form the basis of an ontology. They populate the ontology by instantiating the defined classes. For instance, COVID-19 is a term of the type Disease, and Paris is a term of the type City.
* **Types (or Classes)**: These are abstract categories or groupings that represent general concepts within a domain. They form the backbone of an ontology's structure. Examples include Disease, Vehicle, or City.

By identifying and extracting these elements, the task helps bridge the gap between unstructured natural language and structured ontological knowledge. This process is critical for building knowledge representations that support reasoning, semantic integration, and advanced information retrieval.

To construct datasets for this task, OntoLearner leverages a **Synthetic Data Generator** module. This module is implemented with respect to the following algorithm.

.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/refs/heads/main/docs/source/images/text2onto.png" width="90%"/>
   </div>
   <br>
