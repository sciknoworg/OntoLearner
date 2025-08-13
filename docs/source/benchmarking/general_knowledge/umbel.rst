

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Web Development
       * - **Current Version**
         - 1.50
       * - **Last Updated**
         - May 10, 2016
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - n3
       * - **Download**
         - `Download Upper Mapping and Binding Exchange Layer Vocabulary (UMBEL) <https://github.com/structureddynamics/UMBEL/tree/master/Ontology>`_

Upper Mapping and Binding Exchange Layer Vocabulary (UMBEL)
========================================================================================================

UMBEL is the Upper Mapping and Binding Exchange Layer, designed to help content interoperate on the Web.     UMBEL provides two valuable functions: First, it is a broad, general reference structure of 34,000 concepts,     which provides a scaffolding to link and interoperate other datasets and domain vocabularies.     Second, it is a base vocabulary for the construction of other concept-based domain ontologies,     also designed for interoperation.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1185
        * - **Total Edges**
          - 2868
        * - **Root Nodes**
          - 64
        * - **Leaf Nodes**
          - 302
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 99
        * - **Individuals**
          - 10
        * - **Properties**
          - 42

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 42
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 10.19
        * - **Depth Variance**
          - 83.14
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 162
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 27.42
        * - **Breadth Variance**
          - 1013.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 10
        * - **Taxonomic Relations**
          - 64
        * - **Non-taxonomic Relations**
          - 33
        * - **Average Terms per Type**
          - 10.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import UMBEL

    ontology = UMBEL()
    ontology.load("path/to/UMBEL-ontology.n3")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
