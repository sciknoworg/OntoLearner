.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - APACHE 2.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download NanoMine Ontology (NanoMine) <https://github.com/tetherless-world/nanomine-ontology>`_

NanoMine Ontology (NanoMine)
========================================================================================================

The NanoMine Ontology is a domain ontology developed to support research in polymer nanocomposites. It provides a structured vocabulary for representing the inter-relationships between different materials processing methods, compositions, and resulting material properties. NanoMine enables researchers to develop and test hypotheses about how these inter-relationships affect material performance, supporting both experimental and computational research in materials science.

The ontology employs a class-based modeling approach, defining classes for different types of materials, processes, and properties, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. NanoMine supports the integration of data from various sources, promoting interoperability and data-driven research in polymer nanocomposites.

Typical applications of NanoMine include the development of new polymer nanocomposites with specific properties, the optimization of processing methods, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, NanoMine enhances collaboration and innovation in the field of polymer nanocomposites.

**Example Usage**:
Annotate a polymer nanocomposite dataset with NanoMine terms to specify material types, processing methods, and properties, enabling semantic search and integration with materials informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 496
        * - **Total Edges**
          - 971
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 263
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 157
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

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
          - 212
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import NanoMine

    ontology = NanoMine()
    ontology.load("path/to/NanoMine-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
