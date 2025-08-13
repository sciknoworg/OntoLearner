

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Relations
       * - **Current Version**
         - 2024-04-24
       * - **Last Updated**
         - 2024-04-24
       * - **Creator**
         - None
       * - **License**
         - CC0
       * - **Format**
         - owl
       * - **Download**
         - `Download Relation Ontology (RO) <http://purl.obolibrary.org/obo/ro.owl>`_

Relation Ontology (RO)
========================================================================================================

The Relations Ontology (RO) is a collection of OWL relations (ObjectProperties) intended for use     across a wide variety of biological ontologies.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4635
        * - **Total Edges**
          - 10477
        * - **Root Nodes**
          - 381
        * - **Leaf Nodes**
          - 2650
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 88
        * - **Individuals**
          - 2
        * - **Properties**
          - 673

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.90
        * - **Depth Variance**
          - 2.53
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 870
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 181.93
        * - **Breadth Variance**
          - 70257.92
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 2
        * - **Taxonomic Relations**
          - 65
        * - **Non-taxonomic Relations**
          - 10
        * - **Average Terms per Type**
          - 2.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import RO

    ontology = RO()
    ontology.load("path/to/RO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
