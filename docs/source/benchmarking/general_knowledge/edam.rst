

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - General
       * - **Current Version**
         - 1.25-20240924T0027Z-unstable(1.26)
       * - **Last Updated**
         - 24.09.2024
       * - **Creator**
         - Federico Bianchini, Hervé Ménager, Jon Ison, Matúš Kalaš
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download The ontology of data analysis and management (EDAM) <https://terminology.tib.eu/ts/ontologies/edam>`_

The ontology of data analysis and management (EDAM)
========================================================================================================

EDAM is a domain ontology of data analysis and data management in bio- and other sciences, and science-based applications.     It comprises concepts related to analysis, modelling, optimisation, and data life cycle. Targetting usability by diverse users,     the structure of EDAM is relatively simple, divided into 4 main sections: Topic, Operation, Data (incl. Identifier), and Format.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 12367
        * - **Total Edges**
          - 36215
        * - **Root Nodes**
          - 176
        * - **Leaf Nodes**
          - 8223
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3513
        * - **Individuals**
          - 0
        * - **Properties**
          - 12

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 10
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.75
        * - **Depth Variance**
          - 4.24
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 635
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 196.55
        * - **Breadth Variance**
          - 31795.52
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 7916
        * - **Non-taxonomic Relations**
          - 1314
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EDAM

    ontology = EDAM()
    ontology.load("path/to/EDAM-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
