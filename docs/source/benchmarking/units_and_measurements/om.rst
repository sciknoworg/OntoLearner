

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Units and Measurements
       * - **Category**
         - Units and Measurements
       * - **Current Version**
         - 2.0.57
       * - **Last Updated**
         - June 28, 2024
       * - **Creator**
         - Hajo Rijgersberg, Don Willems, Jan Top
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Ontology of Units of Measure (OM) <https://bioportal.bioontology.org/ontologies/OM>`_

Ontology of Units of Measure (OM)
========================================================================================================

The Ontology of units of Measure (OM) models concepts and relations important to scientific research.     It has a strong focus on units, quantities, measurements, and dimensions.     It includes, for instance, common units such as the SI units metre and kilogram,     but also units from other systems of units such as the mile or nautical mile. For many application areas     it includes more specific units and quantities, such as the unit of the Hubble constant or the quantity vaselife.     The following application areas are supported by OM: Geometry; Mechanics; Thermodynamics; Electromagnetism;     Fluid mechanics; Chemical physics; Photometry; Radiometry and Radiobiology; Nuclear physics;     Astronomy and Astrophysics; Cosmology; Earth science; Meteorology; Material science; Microbiology;     Economics; Information technology and Typography.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 9352
        * - **Total Edges**
          - 27500
        * - **Root Nodes**
          - 27
        * - **Leaf Nodes**
          - 4836
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1100
        * - **Individuals**
          - 1688
        * - **Properties**
          - 34

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
          - 0.27
        * - **Depth Variance**
          - 0.20
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 27
        * - **Minimum Breadth**
          - 10
        * - **Average Breadth**
          - 18.50
        * - **Breadth Variance**
          - 72.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1953
        * - **Taxonomic Relations**
          - 1124
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 42.46
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OM

    ontology = OM()
    ontology.load("path/to/OM-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
