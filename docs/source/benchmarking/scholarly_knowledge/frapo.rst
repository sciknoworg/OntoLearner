

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Administration
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - David Shotton
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Funding, Research Administration and Projects Ontology (FRAPO) <http://www.sparontologies.net/ontologies/frapo>`_

Funding, Research Administration and Projects Ontology (FRAPO)
========================================================================================================

The Funding, Research Administration and Projects Ontology (FRAPO) is an ontology     for describing the administrative information of research projects, e.g., grant applications,     funding bodies, project partners, etc.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 539
        * - **Total Edges**
          - 1076
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 274
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 97
        * - **Individuals**
          - 25
        * - **Properties**
          - 125

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.68
        * - **Depth Variance**
          - 1.08
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 18
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 7.00
        * - **Breadth Variance**
          - 40.50
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 25
        * - **Taxonomic Relations**
          - 82
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 8.33
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import FRAPO

    ontology = FRAPO()
    ontology.load("path/to/FRAPO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
