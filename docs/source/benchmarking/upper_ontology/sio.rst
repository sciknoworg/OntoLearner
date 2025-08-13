

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Basic
       * - **Current Version**
         - 1.59
       * - **Last Updated**
         - 03/25/2024
       * - **Creator**
         - M. Dumontier
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Semanticscience Integrated Ontology (SIO) <https://bioportal.bioontology.org/ontologies/SIO>`_

Semanticscience Integrated Ontology (SIO)
========================================================================================================

The semanticscience integrated ontology (SIO) provides a simple, integrated upper level ontology (types, relations)     for consistent knowledge representation across physical, processual and informational entities.     This project provides foundational support for the Bio2RDF (http://bio2rdf.org) and SADI (http://sadiframework.org) projects.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 7811
        * - **Total Edges**
          - 15701
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 4921
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1726
        * - **Individuals**
          - 0
        * - **Properties**
          - 212

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 20
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 6.67
        * - **Depth Variance**
          - 12.94
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 186
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 63.71
        * - **Breadth Variance**
          - 3373.16
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 2019
        * - **Non-taxonomic Relations**
          - 65
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SIO

    ontology = SIO()
    ontology.load("path/to/SIO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
