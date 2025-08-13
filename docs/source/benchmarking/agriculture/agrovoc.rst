

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

AGROVOC is a relevant Linked Open Data set about agriculture available for public use and facilitates     access and visibility of data across domains and languages. It offers a structured collection of agricultural concepts,     terms, definitions and relationships which are used to unambiguously identify resources, allowing standardized     indexing processes and making searches more efficient.

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
