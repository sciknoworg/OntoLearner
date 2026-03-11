.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Periodic Table of Elements
       * - **Current Version**
         - 1.10
       * - **Last Updated**
         - 2004/02/05
       * - **Creator**
         - Michael Cook
       * - **License**
         - None
       * - **Format**
         - owl
       * - **Download**
         - `Download Periodic Table of the Elements Ontology (PeriodicTable) <https://www.daml.org/2003/01/periodictable/>`_

Periodic Table of the Elements Ontology (PeriodicTable)
========================================================================================================

The Periodic Table of the Elements Ontology (PeriodicTable) is a representation of the Periodic Table of the Elements in the OWL Web Ontology Language. It provides reference data to support Semantic Web applications in chemistry and related disciplines. The ontology offers a structured vocabulary for describing elements, their properties, and relationships, supporting both theoretical and experimental research in chemistry.

The ontology employs a class-based modeling approach, defining classes for different types of elements, properties, and relationships, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. PeriodicTable supports the integration of data from various sources, promoting interoperability and data-driven research in chemistry.

Typical applications of PeriodicTable include the development of new chemical compounds, the optimization of chemical processes, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, PeriodicTable enhances collaboration and innovation in the field of chemistry.

**Example Usage**:
Annotate a chemical research project with PeriodicTable terms to specify element types, properties, and relationships, enabling semantic search and integration with chemical informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 730
        * - **Total Edges**
          - 1845
        * - **Root Nodes**
          - 2
        * - **Leaf Nodes**
          - 521
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 6
        * - **Individuals**
          - 156
        * - **Properties**
          - 13

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
          - 0.75
        * - **Depth Variance**
          - 0.19
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 6
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 4.00
        * - **Breadth Variance**
          - 4.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 150
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 25.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PeriodicTable

    ontology = PeriodicTable()
    ontology.load("path/to/PeriodicTable-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
