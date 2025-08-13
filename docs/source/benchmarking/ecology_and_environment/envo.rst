

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Ecology and Environment
       * - **Category**
         - Environment, Ecosystems, Habitats
       * - **Current Version**
         - 2024-07-01
       * - **Last Updated**
         - 2024-07-01
       * - **Creator**
         - Pier Luigi Buttigieg (https://orcid.org/0000-0002-4366-3088)
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Environment Ontology (ENVO) <https://obofoundry.org/ontology/envo.html>`_

Environment Ontology (ENVO)
========================================================================================================

ENVO is an expressive, community ontology which helps humans, machines,     and semantic web applications understand environmental entities of all kinds,     from microscopic to intergalactic scales. As a FAIR-compliant resource, it promotes interoperability     through the concise, controlled description of all things environmental.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 43986
        * - **Total Edges**
          - 107616
        * - **Root Nodes**
          - 4449
        * - **Leaf Nodes**
          - 19297
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 9309
        * - **Individuals**
          - 44
        * - **Properties**
          - 208

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 28
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.69
        * - **Depth Variance**
          - 9.89
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 8473
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 1056.21
        * - **Breadth Variance**
          - 4840394.03
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 46
        * - **Taxonomic Relations**
          - 16175
        * - **Non-taxonomic Relations**
          - 147
        * - **Average Terms per Type**
          - 5.75
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ENVO

    ontology = ENVO()
    ontology.load("path/to/ENVO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
