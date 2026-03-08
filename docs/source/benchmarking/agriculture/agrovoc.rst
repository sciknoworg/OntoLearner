.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Agriculture
       * - **Category**
         - Agricultural Knowledge
       * - **Current Version**
         - 2024-04
       * - **Last Updated**
         - August 12, 2024
       * - **Creator**
         - Food and Agriculture Organization of the United Nations
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download AGROVOC Multilingual Thesaurus (AGROVOC) <https://agroportal.lirmm.fr/ontologies/AGROVOC>`_

AGROVOC Multilingual Thesaurus (AGROVOC)
========================================================================================================

AGROVOC is a comprehensive Linked Open Data resource developed and maintained by the Food and Agriculture Organization (FAO) of the United Nations. It provides a structured collection of agricultural concepts, terms, definitions, and relationships that enable unambiguous identification of resources and standardized indexing. As a multilingual thesaurus, AGROVOC supports multiple languages, facilitating access and visibility of agricultural data across domains and languages. The ontology covers diverse agricultural domains including crops, livestock, farm management practices, soil science, and food production. AGROVOC's hierarchical structure enables both broader and narrower term relationships, supporting semantic interoperability and making searches more efficient. The resource is widely used by research institutions, government agencies, and international organizations for data annotation, knowledge organization, and information retrieval. With millions of concept nodes and sophisticated relationship mappings, AGROVOC serves as a critical backbone for agricultural knowledge representation and data integration in the global agricultural community.

**Example Usage**: Annotate a multilingual agricultural dataset with AGROVOC terms for crops, soil types, and farming practices to enable standardized indexing and cross-language search in international agricultural databases.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2279766
        * - **Total Edges**
          - 10140352
        * - **Root Nodes**
          - 59
        * - **Leaf Nodes**
          - 981249
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 35
        * - **Individuals**
          - 1234769
        * - **Properties**
          - 209

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 11
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.24
        * - **Depth Variance**
          - 2.31
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 617543
        * - **Minimum Breadth**
          - 9
        * - **Average Breadth**
          - 189858.08
        * - **Breadth Variance**
          - 44142143480.08
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 12
        * - **Taxonomic Relations**
          - 11
        * - **Non-taxonomic Relations**
          - 7
        * - **Average Terms per Type**
          - 3.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AGROVOC

    ontology = AGROVOC()
    ontology.load("path/to/AGROVOC-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
