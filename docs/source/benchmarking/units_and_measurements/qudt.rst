.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Units and Measurements
       * - **Category**
         - Physics
       * - **Current Version**
         - 2.1
       * - **Last Updated**
         - March 1, 2022
       * - **Creator**
         - NASA Ames Research Center
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Quantities, Units, Dimensions and Data Types (QUDT) <https://qudt.org/>`_

Quantities, Units, Dimensions and Data Types (QUDT)
========================================================================================================

The Quantities, Units, Dimensions and Data Types (QUDT) ontology is a comprehensive framework for representing quantities, units, dimensions, and data types in scientific, engineering, and technical domains. QUDT provides a standardized vocabulary for describing measurement units, physical quantities, conversion factors, and dimensional analysis, supporting data expressed in RDF and JSON. The ontology is widely used for semantic annotation of scientific datasets, IoT data streams, and engineering models, enabling automated unit conversion, validation, and interoperability across diverse systems. QUDT is maintained by NASA Ames Research Center and is continuously updated to reflect new standards and measurement systems. By providing a common semantic foundation, QUDT facilitates data integration, analytics, and knowledge sharing in multidisciplinary projects. The ontology is extensible and can be aligned with other units and measurements ontologies for broader compatibility.

**Example Usage**:
Annotate a scientific dataset with QUDT terms to specify the quantities measured (e.g., "temperature", "pressure"), their units (e.g., "degree Celsius", "pascal"), and conversion factors, enabling automated unit conversion and semantic search across datasets.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 772
        * - **Total Edges**
          - 2288
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 233
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 73
        * - **Individuals**
          - 24
        * - **Properties**
          - 165

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
          - 27
        * - **Taxonomic Relations**
          - 400
        * - **Non-taxonomic Relations**
          - 12
        * - **Average Terms per Type**
          - 2.45
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import QUDT

    ontology = QUDT()
    ontology.load("path/to/QUDT-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
