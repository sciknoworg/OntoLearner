

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Properties
       * - **Current Version**
         - 0.0.8
       * - **Last Updated**
         - None
       * - **Creator**
         - María Poveda-Villalón, Serge Chávez-Feria
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Material Properties Ontology (MAT) <https://bimerr.iot.linkeddata.es/def/material-properties/>`_

Material Properties Ontology (MAT)
========================================================================================================

The Material Properties Ontology aims to provide the vocabulary to describe the building components,     materials, and their corresponding properties, relevant within the construction industry. More specifically,     the building elements and properties covered in this ontology support applications     focused on the design of building renovation projects.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 263
        * - **Total Edges**
          - 691
        * - **Root Nodes**
          - 7
        * - **Leaf Nodes**
          - 52
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 140
        * - **Individuals**
          - 0
        * - **Properties**
          - 21

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
          - 5.21
        * - **Depth Variance**
          - 11.10
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 12
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.67
        * - **Breadth Variance**
          - 7.22
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 128
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MAT

    ontology = MAT()
    ontology.load("path/to/MAT-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
