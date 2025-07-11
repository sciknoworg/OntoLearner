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
