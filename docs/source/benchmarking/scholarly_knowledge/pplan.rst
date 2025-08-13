

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - 1.3
       * - **Last Updated**
         - 2014-03-12
       * - **Creator**
         - http://www.isi.edu/~gil/
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Ontology for Provenance and Plans (P-Plan) <https://vocab.linkeddata.es/p-plan/index.html>`_

Ontology for Provenance and Plans (P-Plan)
========================================================================================================

The Ontology for Provenance and Plans (P-Plan) is an extension of the PROV-O ontology [PROV-O]     created to represent the plans that guided the execution of scientific processes. P-Plan describes     how the plans are composed and their correspondence to provenance records that describe the execution itself.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 52
        * - **Total Edges**
          - 100
        * - **Root Nodes**
          - 10
        * - **Leaf Nodes**
          - 24
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 11
        * - **Individuals**
          - 0
        * - **Properties**
          - 14

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.59
        * - **Depth Variance**
          - 0.60
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 10
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 5.67
        * - **Breadth Variance**
          - 9.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 16
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PPlan

    ontology = PPlan()
    ontology.load("path/to/PPlan-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
