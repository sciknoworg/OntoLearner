

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Knowledge Graph
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2008-11-17
       * - **Creator**
         - DBpedia Maintainers and Contributors
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download DBpedia Ontology (DBpedia) <https://wiki.dbpedia.org/>`_

DBpedia Ontology (DBpedia)
========================================================================================================

The DBpedia ontology is generated from the manually created specifications in the DBpedia Mappings Wiki.     Each release of this ontology corresponds to a new release of the DBpedia dataset, which contains     instance data extracted from various language versions of Wikipedia. The DBpedia ontology has evolved     into a crowd-sourced effort, resulting in a shallow cross-domain ontology.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 18819
        * - **Total Edges**
          - 32745
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 14867
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 790
        * - **Individuals**
          - 0
        * - **Properties**
          - 3029

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.61
        * - **Depth Variance**
          - 1.66
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 145
        * - **Minimum Breadth**
          - 12
        * - **Average Breadth**
          - 61.57
        * - **Breadth Variance**
          - 2369.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 799
        * - **Non-taxonomic Relations**
          - 1665
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DBpedia

    ontology = DBpedia()
    ontology.load("path/to/DBpedia-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
