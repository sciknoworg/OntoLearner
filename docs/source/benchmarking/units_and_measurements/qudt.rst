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

The Quantities, Units, Dimensions and Data Types (QUDT) ontology is a comprehensive framework for representing quantities, units, dimensions, and data types in scientific, engineering, and technical domains [#qudt-fairsharing]_. QUDT provides a standardized vocabulary for describing measurement units, quantity kinds, dimensional vectors, physical constants, conversion factors, and measurement values [#qudt-fairsharing]_. The ontology supports machine-readable representation of scientific and engineering measurements and is used to promote interoperability across data and knowledge representation systems [#qudt-fairsharing]_. QUDT supports semantic annotation of scientific and technical data by providing reusable identifiers and structured descriptions for quantities, units, dimensions, and related concepts [#qudt-fairsharing]_. By providing a common semantic foundation for measurement information, QUDT facilitates consistent data representation, integration, and reuse across scientific and engineering applications [#qudt-fairsharing]_.

**Example Usage**:
Annotate a scientific dataset with QUDT terms to specify the quantities measured, such as ``temperature`` or ``pressure``; their associated units, such as ``degree Celsius`` or ``pascal``; and relevant dimensional information. This enables consistent machine-readable representation and integration of measurement data across datasets and applications [#qudt-fairsharing]_.
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

References
----------

.. [#qudt-fairsharing] FAIRsharing.org. 2026.
   "QUDT: Quantities, Units, Dimensions and Types."
   DOI: 10.25504/FAIRsharing.d3pqw7.
   Last edited March 26, 2026.
   Available at:
   `https://doi.org/10.25504/FAIRsharing.d3pqw7
   <https://doi.org/10.25504/FAIRsharing.d3pqw7>`_
