

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Wildlife
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - 2013/12/18
       * - **Creator**
         - https://www.ldodds.com#me, http://tomscott.name/
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Wildlife Ontology (BBCWildlife) <https://www.bbc.co.uk/ontologies/wildlife-ontology>`_

BBC Wildlife Ontology (BBCWildlife)
========================================================================================================

A simple vocabulary for describing biological species and related taxa. The vocabulary defines terms     for describing the names and ranking of taxa, as well as providing support for describing their habitats,     conservation status, and behavioural characteristics, etc.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 157
        * - **Total Edges**
          - 414
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 93
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 31
        * - **Individuals**
          - 0
        * - **Properties**
          - 31

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
          - 0.67
        * - **Depth Variance**
          - 0.22
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 2
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.50
        * - **Breadth Variance**
          - 0.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 23
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCWildlife

    ontology = BBCWildlife()
    ontology.load("path/to/BBCWildlife-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
