.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Units and Measurements
       * - **Category**
         - Units and Measurements
       * - **Current Version**
         - 2009-10-30
       * - **Last Updated**
         - 2009-10-30
       * - **Creator**
         - SysML
       * - **License**
         - Apache License 2.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Quantities, Units, Dimensions and Values (QUDV) <https://www.omgwiki.org/OMGSysML/doku.php?id=sysml-qudv:qudv_owl>`_

Quantities, Units, Dimensions and Values (QUDV)
========================================================================================================

The Quantities, Units, Dimensions and Values (QUDV) ontology is a formal representation of the SysML QUDV modelLibrary, providing a standardized vocabulary for describing quantities, units, dimensions, and values in scientific and engineering domains. QUDV is specified in UML/SysML class/block diagrams and is designed to support interoperability and alignment with other standardization efforts concerning quantities and units. The ontology enables the semantic annotation of measurement data, supporting unit conversion, dimensional analysis, and data integration across diverse systems. QUDV is used in systems engineering, modeling and simulation, and scientific data management to ensure consistency and comparability of quantitative information. By providing a common framework, QUDV facilitates automated reasoning, validation, and knowledge sharing in multidisciplinary projects. The ontology is maintained by the SysML community and is aligned with other units and measurements ontologies for broader compatibility.

**Example Usage**:
Annotate a systems engineering model with QUDV terms to specify the quantities measured (e.g., "length", "mass"), their units (e.g., "meter", "kilogram"), and dimensions, enabling automated unit conversion and validation across engineering tools.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 186
        * - **Total Edges**
          - 491
        * - **Root Nodes**
          - 4
        * - **Leaf Nodes**
          - 20
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 33
        * - **Individuals**
          - 0
        * - **Properties**
          - 25

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 21
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 8.44
        * - **Depth Variance**
          - 24.45
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 17
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 8.00
        * - **Breadth Variance**
          - 22.18
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 9
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import QUDV

    ontology = QUDV()
    ontology.load("path/to/QUDV-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
