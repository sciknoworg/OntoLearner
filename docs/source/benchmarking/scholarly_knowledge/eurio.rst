

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Research Information
       * - **Current Version**
         - 2.4
       * - **Last Updated**
         - 2023-10-19
       * - **Creator**
         - Publications Office of the European Commission
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download EUropean Research Information Ontology (EURIO) <https://op.europa.eu/de/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurio>`_

EUropean Research Information Ontology (EURIO)
========================================================================================================

EURIO (EUropean Research Information Ontology) conceptualises, formally encodes and makes available in an open,     structured and machine-readable format data about resarch projects funded by the EU's     framework programmes for research and innovation.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 502
        * - **Total Edges**
          - 1193
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 204
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 44
        * - **Individuals**
          - 0
        * - **Properties**
          - 111

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
          - 6.54
        * - **Depth Variance**
          - 11.75
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 56
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 24.73
        * - **Breadth Variance**
          - 192.33
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 43
        * - **Non-taxonomic Relations**
          - 4
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EURIO

    ontology = EURIO()
    ontology.load("path/to/EURIO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
