

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Library and Cultural Heritage
       * - **Category**
         - Authority Files
       * - **Current Version**
         - 1.2.0
       * - **Last Updated**
         - 2024-08-26
       * - **Creator**
         - Alexander Haffner
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Gemeinsame Normdatei (GND) <https://d-nb.info/standards/elementset/gnd>`_

Gemeinsame Normdatei (GND)
========================================================================================================

GND stands for Gemeinsame Normdatei (Integrated Authority File) and offers a broad range of elements     to describe authorities. The GND originates from the German library community and aims     to solve the name ambiguity problem in the library world.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2100
        * - **Total Edges**
          - 4128
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 1008
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 247
        * - **Individuals**
          - 0
        * - **Properties**
          - 236

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 0
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.00
        * - **Depth Variance**
          - 0.00
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 0
        * - **Minimum Breadth**
          - 0
        * - **Average Breadth**
          - 0.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 70
        * - **Non-taxonomic Relations**
          - 3
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GND

    ontology = GND()
    ontology.load("path/to/GND-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
