.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Testing
       * - **Current Version**
         - 0.1
       * - **Last Updated**
         - 05/05/2022
       * - **Creator**
         - Birgit Skrotzki, Hossein Beygi Nasrabadi, Philipp von Hartrott, Vinicius Carrillo Beber, Yue Chen
       * - **License**
         - None
       * - **Format**
         - ttl
       * - **Download**
         - `Download MatoLab Brinell Test Ontology (MOL_BRINELL) <https://matportal.org/ontologies/MOL_BRINELL>`_

MatoLab Brinell Test Ontology (MOL_BRINELL)
========================================================================================================

The MatoLab Brinell Test Ontology (MOL_BRINELL) is a domain ontology developed to describe the Brinell hardness testing process. It provides a structured vocabulary for representing the testing methods, equipment, and results, supporting both experimental and computational research in materials testing.

The ontology employs a class-based modeling approach, defining classes for different types of tests, equipment, and results, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. MOL_BRINELL supports the integration of data from experimental studies and simulations, promoting interoperability and data-driven research in materials testing.

Typical applications of MOL_BRINELL include the development of new testing methods, the optimization of testing procedures, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, MOL_BRINELL enhances collaboration and innovation in the field of materials testing.

**Example Usage**:
Annotate a Brinell hardness testing dataset with MOL_BRINELL terms to specify test types, equipment, and results, enabling semantic search and integration with materials informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 3648
        * - **Total Edges**
          - 16347
        * - **Root Nodes**
          - 29
        * - **Leaf Nodes**
          - 308
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 37
        * - **Individuals**
          - 3053
        * - **Properties**
          - 21

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.26
        * - **Depth Variance**
          - 0.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 29
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 12.67
        * - **Breadth Variance**
          - 141.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 3053
        * - **Taxonomic Relations**
          - 14
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 105.28
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MOLBRINELL

    ontology = MOLBRINELL()
    ontology.load("path/to/MOLBRINELL-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
