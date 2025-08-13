

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Industry
       * - **Category**
         - Provenance
       * - **Current Version**
         - 1.0.0
       * - **Last Updated**
         - 2025-03-01
       * - **Creator**
         - Mario Scrocca (Cefriel), Valentina Carriero (Cefriel)
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Provenance Knowledge Ontology (PKO) <https://github.com/perks-project/pk-ontology/tree/master>`_

Provenance Knowledge Ontology (PKO)
========================================================================================================

Procedural Knowledge (PK) is knowing how to perform some tasks,     as opposed to descriptive/declarative knowledge, which is knowing     what in terms of facts and notions. In industry, PK refers in general     to structured processes to be followed, and can be related     to both production (e.g., procedure on the production line in a plant)     and services (e.g., procedure for troubleshooting during customer support);     to specific technical expertise (e.g., procedure to set up a specific machine)     and general regulations and best practices (e.g., safety procedures,     activities to minimise environmental impact).

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 302
        * - **Total Edges**
          - 623
        * - **Root Nodes**
          - 24
        * - **Leaf Nodes**
          - 141
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 38
        * - **Individuals**
          - 8
        * - **Properties**
          - 93

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
          - 0.50
        * - **Depth Variance**
          - 0.51
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 24
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 12.67
        * - **Breadth Variance**
          - 66.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 8
        * - **Taxonomic Relations**
          - 11
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 4.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PKO

    ontology = PKO()
    ontology.load("path/to/PKO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
