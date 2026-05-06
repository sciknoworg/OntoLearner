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

The Quantities, Units, Dimensions and Values (QUDV) ontology is a formal representation of the SysML QUDV model library, providing a standardized framework for describing quantities, units, dimensions, and values in scientific and engineering domains [#qudv-owl]_. The QUDV OWL representation was created to support ontology-based use of the SysML QUDV model and to enable alignment with other standardization efforts concerning quantities and units [#qudv-owl]_. QUDV supports the description of quantity kinds, measurement units, dimensions, values, and related measurement concepts, enabling quantitative information to be represented in a machine-readable form [#qudv-w3c]_. The ontology enables semantic annotation of measurement data, supporting unit representation, dimensional analysis, validation, and data integration across engineering and scientific systems [#qudv-owl]_ [#qudv-w3c]_. It is useful in systems engineering, modeling and simulation, sensor data annotation, and scientific data management where consistent representation of units, dimensions, and quantities is required [#qudv-w3c]_. By providing a common conceptual framework, QUDV facilitates interoperability, automated reasoning, validation, and knowledge sharing across multidisciplinary engineering and semantic web applications [#qudv-owl]_ [#qudv-w3c]_.

**Example Usage**:
Annotate a systems engineering model with QUDV terms to specify measured quantities such as ``length`` and ``mass``, their units such as ``meter`` and ``kilogram``, dimensions, and associated values. This enables unit-aware data integration, dimensional validation, and interoperability across engineering and semantic web tools [#qudv-owl]_ [#qudv-w3c]_.

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

References
----------

.. [#qudv-owl] OMG SysML Portal. 2009.
   "QUDV OWL."
   Available at:
   `https://www.omgwiki.org/OMGSysML/doku.php?id=sysml-qudv:qudv_owl <https://www.omgwiki.org/OMGSysML/doku.php?id=sysml-qudv:qudv_owl>`_

.. [#qudv-w3c] W3C Semantic Sensor Network Incubator Group. n.d.
   "Library for Quantity Kinds and Units."
   Available at:
   `https://www.w3.org/2005/Incubator/ssn/ssnx/qu/qu <https://www.w3.org/2005/Incubator/ssn/ssnx/qu/qu>`_
