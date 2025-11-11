LLMs4OL Challenge Learners
==========================

LLMs4OL is a community development initiative collocated with the 23rd International Semantic Web Conference (ISWC) to explore the potential of Large Language Models (LLMs) in Ontology Learning (OL), a vital process for enhancing the web with structured knowledge to improve interoperability. By leveraging LLMs, the challenge aims to advance understanding and innovation in OL, aligning with the goals of the Semantic Web to create a more intelligent and user-friendly web.

**Learning Tasks**

.. list-table:: 
   :widths: 20 80
   :header-rows: 1
  
   * - **Task**
     - **Description**
   * - **Term Typing**
     - Discover the generalized type for a lexical term.

       **ID**: ``term-typing``

       **Info**: The process of assigning a generalized type to each lexical term involves mapping lexical items to their most appropriate semantic categories or ontological classes. For example, in the biomedical domain, the term ``aspirin`` should be classified under ``Pharmaceutical Drug``. This task is crucial for organizing extracted terms into structured ontologies and improving knowledge reuse.

       **Example**: Assign the type ``"disease"`` to the term ``"myocardial infarction"``.
   * - **Taxonomy Discovery**
     - Discover the taxonomic hierarchy between type pairs.

       **ID**: ``taxonomy-discovery``

       **Info**: Taxonomy discovery focuses on identifying hierarchical relationships between types, enabling the construction of taxonomic structures (i.e., ``is-a`` relationships). Given a pair of terms or types, the task determines whether one is a subclass of the other. For example, discovering that ``Sedan is a subclass of Car`` contributes to structuring domain knowledge in a way that supports reasoning and inferencing in ontology-driven applications.

       **Example**: Recognize that ``"lung cancer"`` is a subclass of ``"cancer"``, which is a subclass of ``"disease"``.
   * - **Non-Taxonomic Relation Extraction**
     - Identify non-taxonomic, semantic relations between types.

       **ID**: ``non-taxonomic-re``

       **Info**: This task aims to extract non-hierarchical (non-taxonomic) semantic relations between concepts in an ontology. Unlike taxonomy discovery, which deals with is-a relationships, this task focuses on other meaningful associations such as part-whole (part-of), causal (causes), functional (used-for), and associative (related-to) relationships. For example, in a medical ontology, discovering that ``Aspirin treats Headache`` adds valuable relational knowledge that enhances the utility of an ontology.

       **Example**: Identify that *"virus"* ``causes`` *"infection"* or *"aspirin"* ``treats`` *"headache"*.



.. toctree::
   :maxdepth: 1
   :caption: LLMs4OL Learners
   :titlesonly:

   retrieval_model1
   retrieval_model2
   retrieval_model3
   retrieval_model4