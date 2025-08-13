

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scientific Evidence
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2015-02-23
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Scientific Evidence and Provenance Information Ontology (SEPIO) <https://terminology.tib.eu/ts/ontologies/SEPIO>`_

Scientific Evidence and Provenance Information Ontology (SEPIO)
========================================================================================================

The SEPIO ontology is in its early stages of development, undergoing iterative refinement     as new requirements emerge and alignment with existing standards is explored. The SEPIO core file imports two files     which can be resolved at the URLs below:     IAO ontology-metadata import: https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/imports/ontology-metadata.owl     bfo mireot: https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/mireots/bfo-mireot.owl

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1262
        * - **Total Edges**
          - 2385
        * - **Root Nodes**
          - 72
        * - **Leaf Nodes**
          - 781
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 129
        * - **Individuals**
          - 21
        * - **Properties**
          - 117

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 14
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.17
        * - **Depth Variance**
          - 8.36
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 170
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 40.60
        * - **Breadth Variance**
          - 2186.24
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 21
        * - **Taxonomic Relations**
          - 141
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 4.20
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SEPIO

    ontology = SEPIO()
    ontology.load("path/to/SEPIO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
