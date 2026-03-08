.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - Sep 15, 2022
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - ttl
       * - **Download**
         - `Download Material Science Lab Equipment Ontology (MSLE) <https://github.com/MehrdadJalali-AI/MSLE-Ontology>`_

Material Science Lab Equipment Ontology (MSLE)
========================================================================================================

The Material Science Lab Equipment Ontology (MSLE) is a domain ontology developed to describe laboratory equipment used in materials science. It provides a structured vocabulary for representing equipment, processes, and data, supporting both experimental and computational research in materials science.

The ontology employs a class-based modeling approach, defining classes for different types of equipment, processes, and data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. MSLE supports the integration of data from various sources, promoting interoperability and data-driven research in materials science.

Typical applications of MSLE include the integration of laboratory data from various sources, the development of new materials with specific properties, and the optimization of laboratory processes. By providing a standardized vocabulary and framework, MSLE enhances collaboration and innovation in the field of materials science.

**Example Usage**:
Annotate a laboratory equipment dataset with MSLE terms to specify equipment types, processes, and data, enabling semantic search and integration with materials informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 146
        * - **Total Edges**
          - 479
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 52
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 45
        * - **Individuals**
          - 3
        * - **Properties**
          - 10

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.77
        * - **Depth Variance**
          - 1.70
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 53
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 17.75
        * - **Breadth Variance**
          - 353.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 3
        * - **Taxonomic Relations**
          - 47
        * - **Non-taxonomic Relations**
          - 228
        * - **Average Terms per Type**
          - 1.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MSLE

    ontology = MSLE()
    ontology.load("path/to/MSLE-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
