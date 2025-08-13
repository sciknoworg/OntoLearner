

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Metadata
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - February 17, 2017
       * - **Creator**
         - The Dublin Core Metadata Initiative
       * - **License**
         - Public Domain
       * - **Format**
         - rdf
       * - **Download**
         - `Download Dublin Core Vocabulary (DublinCore) <https://bioportal.bioontology.org/ontologies/DC>`_

Dublin Core Vocabulary (DublinCore)
========================================================================================================

The Dublin Core Schema is a small set of vocabulary terms that can be used to describe several kinds of resources.     Dublin Core Metadata may be used for multiple purposes, from simple resource description,     to combining metadata vocabularies of different metadata standards, to providing interoperability     for metadata vocabularies in the Linked Data cloud and Semantic Web implementations.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 296
        * - **Total Edges**
          - 632
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 210
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 11
        * - **Individuals**
          - 26
        * - **Properties**
          - 0

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.50
        * - **Depth Variance**
          - 0.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 1
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 30
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 3.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DublinCore

    ontology = DublinCore()
    ontology.load("path/to/DublinCore-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
