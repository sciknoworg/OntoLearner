.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Open Innovation Environment Manufacturing (OIEManufacturing) <https://github.com/emmo-repo/OIE-Ontologies/>`_

Open Innovation Environment Manufacturing (OIEManufacturing)
========================================================================================================

The Open Innovation Environment Manufacturing (OIEManufacturing) ontology is a domain-level ontology developed to represent manufacturing processes in materials science. It provides a structured vocabulary for describing manufacturing methods, equipment, and data, supporting both experimental and computational research in materials science.

The ontology employs a class-based modeling approach, defining classes for different types of manufacturing methods, equipment, and data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. OIEManufacturing supports the integration of data from various sources, promoting interoperability and data-driven research in materials manufacturing.

Typical applications of OIEManufacturing include the development of new manufacturing methods, the optimization of manufacturing processes, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, OIEManufacturing enhances collaboration and innovation in the field of materials manufacturing.

**Example Usage**:
Annotate a manufacturing dataset with OIEManufacturing terms to specify manufacturing methods, equipment, and data, enabling semantic search and integration with materials informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 380
        * - **Total Edges**
          - 869
        * - **Root Nodes**
          - 13
        * - **Leaf Nodes**
          - 131
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 222
        * - **Individuals**
          - 0
        * - **Properties**
          - 3

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 5
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.39
        * - **Depth Variance**
          - 1.07
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 30
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 12.00
        * - **Breadth Variance**
          - 112.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 217
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OIEManufacturing

    ontology = OIEManufacturing()
    ontology.load("path/to/OIEManufacturing-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
