
.. sidebar:: Challenge Series Websites

	* `1st LLMs4OL @ ISWC 2024 <https://sites.google.com/view/llms4ol>`_
	* `2nd LLMs4OL @ ISWC 2025 <https://sites.google.com/view/llms4ol2025>`_


.. raw:: html

   <div align="center">
     <img src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/refs/heads/dev/docs/source/learners/images/challenge-logo.png" alt="challenge-logo" width="10%"/>
   </div>

LLMs4OL Challenge
==================================================================================================================




LLMs4OL is a community development initiative collocated with the International Semantic Web Conference (ISWC) to explore the potential of Large Language Models (LLMs) in Ontology Learning (OL), a vital process for enhancing the web with structured knowledge to improve interoperability. By leveraging LLMs, the challenge aims to advance understanding and innovation in OL, aligning with the goals of the Semantic Web to create a more intelligent and user-friendly web.


.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - **Edition**
     - **Task**
     - **Description**
   * - ``LLMs4OL'25``
     - **Text2Onto**
     - Extract ontological terms and types from unstructured text.

       **ID**: ``text2onto``

       **Info**: This task focuses on extracting foundational elements (Terms and Types) from unstructured text documents to build the initial structure of an ontology. It involves recognizing domain-relevant vocabulary (Term Extraction, SubTask 1) and categorizing it appropriately (Type Extraction, SubTask 2). It bridges the gap between natural language and structured knowledge representation.

       **Example**: **COVID-19** is a term of the type **Disease**.
   * - ``LLMs4OL'24``, ``LLMs4OL'25``
     - **Term Typing**
     - Discover the generalized type for a lexical term.

       **ID**: ``term-typing``

       **Info**: The process of assigning a generalized type to each lexical term involves mapping lexical items to their most appropriate semantic categories or ontological classes. For example, in the biomedical domain, the term ``aspirin`` should be classified under ``Pharmaceutical Drug``. This task is crucial for organizing extracted terms into structured ontologies and improving knowledge reuse.

       **Example**: Assign the type ``"disease"`` to the term ``"myocardial infarction"``.
   * - ``LLMs4OL'24``, ``LLMs4OL'25``
     - **Taxonomy Discovery**
     - Discover the taxonomic hierarchy between type pairs.

       **ID**: ``taxonomy-discovery``

       **Info**: Taxonomy discovery focuses on identifying hierarchical relationships between types, enabling the construction of taxonomic structures (i.e., ``is-a`` relationships). Given a pair of terms or types, the task determines whether one is a subclass of the other. For example, discovering that ``Sedan is a subclass of Car`` contributes to structuring domain knowledge in a way that supports reasoning and inferencing in ontology-driven applications.

       **Example**: Recognize that ``"lung cancer"`` is a subclass of ``"cancer"``, which is a subclass of ``"disease"``.
   * - ``LLMs4OL'24``, ``LLMs4OL'25``
     - **Non-Taxonomic Relation Extraction**
     - Identify non-taxonomic, semantic relations between types.

       **ID**: ``non-taxonomic-re``

       **Info**: This task aims to extract non-hierarchical (non-taxonomic) semantic relations between concepts in an ontology. Unlike taxonomy discovery, which deals with is-a relationships, this task focuses on other meaningful associations such as part-whole (part-of), causal (causes), functional (used-for), and associative (related-to) relationships. For example, in a medical ontology, discovering that ``Aspirin treats Headache`` adds valuable relational knowledge that enhances the utility of an ontology.

       **Example**: Identify that *"virus"* ``causes`` *"infection"* or *"aspirin"* ``treats`` *"headache"*.


.. note::

	* Proceedings of 1st LLMs4OL Challenge @ ISWC 2024 available at `https://www.tib-op.org/ojs/index.php/ocp/issue/view/169 <https://www.tib-op.org/ojs/index.php/ocp/issue/view/169>`_
	* Proceedings of 2nd LLMs4OL Challenge @ ISWC 2025 available at `https://www.tib-op.org/ojs/index.php/ocp/issue/view/185 <https://www.tib-op.org/ojs/index.php/ocp/issue/view/185>`_

.. toctree::
   :maxdepth: 1
   :caption: LLMs4OL Challenge Series Participants Learners
   :titlesonly:

   llms4ol_challenge/rwthdbis_learner
   llms4ol_challenge/skhnlp_learner
   llms4ol_challenge/alexbek_learner
   llms4ol_challenge/sbunlp_learner
