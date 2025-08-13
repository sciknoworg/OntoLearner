

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemicals, Roles
       * - **Current Version**
         - 2015-11-23
       * - **Last Updated**
         - 2015-11-23
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download CHEBI Integrated Role Ontology (CHIRO) <https://terminology.tib.eu/ts/ontologies/chiro>`_

CHEBI Integrated Role Ontology (CHIRO)
========================================================================================================

CHEBI provides a distinct role hierarchy. Chemicals in the structural hierarchy are connected via a 'has role' relation.     CHIRO provides links from these roles to useful other classes in other ontologies.     This will allow direct connection between chemical structures (small molecules, drugs) and what they do.     This could be formalized using 'capable of', in the same way Uberon and the Cell Ontology link structures to processes.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 81778
        * - **Total Edges**
          - 197071
        * - **Root Nodes**
          - 14636
        * - **Leaf Nodes**
          - 50439
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 13930
        * - **Individuals**
          - 0
        * - **Properties**
          - 15

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 16
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.36
        * - **Depth Variance**
          - 1.13
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 34719
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 4620.24
        * - **Breadth Variance**
          - 105924794.30
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 25262
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CHIRO

    ontology = CHIRO()
    ontology.load("path/to/CHIRO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
