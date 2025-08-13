

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Social Sciences
       * - **Category**
         - Social
       * - **Current Version**
         - 0.1
       * - **Last Updated**
         - 14 January 2014
       * - **Creator**
         - Dan Brickley, Libby Miller
       * - **License**
         - Creative Commons
       * - **Format**
         - rdf
       * - **Download**
         - `Download Friend of a Friend (FOAF) <http://xmlns.com/foaf/0.1/>`_

Friend of a Friend (FOAF)
========================================================================================================

FOAF is a project devoted to linking people and information using the Web.     Regardless of whether information is in people's heads, in physical or digital documents,     or in the form of factual data, it can be linked.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 168
        * - **Total Edges**
          - 504
        * - **Root Nodes**
          - 5
        * - **Leaf Nodes**
          - 87
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 15
        * - **Individuals**
          - 13
        * - **Properties**
          - 60

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
          - 0.17
        * - **Depth Variance**
          - 0.14
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 5
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 3.00
        * - **Breadth Variance**
          - 4.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 13
        * - **Taxonomic Relations**
          - 11
        * - **Non-taxonomic Relations**
          - 21
        * - **Average Terms per Type**
          - 13.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import FOAF

    ontology = FOAF()
    ontology.load("path/to/FOAF-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
