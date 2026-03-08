.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 3.0.0-alpha1
       * - **Last Updated**
         - 2025-03-20
       * - **Creator**
         - Jannis Grundmann
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download The Platform MaterialDigital core ontology (PMDco) <https://github.com/materialdigital/core-ontology?tab=readme-ov-file>`_

The Platform MaterialDigital core ontology (PMDco)
========================================================================================================


The ontology employs a class-based modeling approach, defining classes for different types of materials, processes, and data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. PMDco supports the integration of data from various sources, promoting interoperability and data-driven research in materials science.

Typical applications of PMDco include the development of new materials with specific properties, the optimization of materials for industrial applications, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, PMDco enhances collaboration and innovation in the field of materials science.

**Example Usage**:
Annotate a materials science project with PMDco terms to specify material types, processes, and data, enabling semantic search and integration with materials informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4207
        * - **Total Edges**
          - 8103
        * - **Root Nodes**
          - 85
        * - **Leaf Nodes**
          - 2365
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1002
        * - **Individuals**
          - 0
        * - **Properties**
          - 66

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 19
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.90
        * - **Depth Variance**
          - 11.78
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 161
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 40.45
        * - **Breadth Variance**
          - 2084.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 903
        * - **Non-taxonomic Relations**
          - 19
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PMDco

    ontology = PMDco()
    ontology.load("path/to/PMDco-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
