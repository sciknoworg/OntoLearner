

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Arts and Humanities
       * - **Category**
         - Numismatics
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2025-01-22
       * - **Creator**
         - American Numismatic Society, Institute for the Study of the Ancient World
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Nomisma Ontology (Nomisma) <https://www.dainst.org/forschung/projekte/noslug/2098>`_

Nomisma Ontology (Nomisma)
========================================================================================================

Nomisma Ontology is a collaborative project to provide stable digital representations of numismatic concepts according     to the principles of Linked Open Data. These take the form of http URIs that provide access to the information     about a concept in various formats. The project is a collaborative effort of the American Numismatic Society     and the Institute for the Study of the Ancient World at New York University.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 245
        * - **Total Edges**
          - 431
        * - **Root Nodes**
          - 22
        * - **Leaf Nodes**
          - 113
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 36
        * - **Individuals**
          - 0
        * - **Properties**
          - 71

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
          - 0.97
        * - **Depth Variance**
          - 0.73
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 22
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 15.00
        * - **Breadth Variance**
          - 67.50
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 13
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Nomisma

    ontology = Nomisma()
    ontology.load("path/to/Nomisma-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
