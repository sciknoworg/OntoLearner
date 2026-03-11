

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Ecology and Environment
       * - **Category**
         - Energy
       * - **Current Version**
         - 2.7.0
       * - **Last Updated**
         - 03/2025
       * - **Creator**
         - None
       * - **License**
         - Creative Commons Attribution 1.0 Generic (CC BY 1.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download The Open Energy Ontology (OEO) <https://github.com/OpenEnergyPlatform/ontology?tab=readme-ov-file>`_

The Open Energy Ontology (OEO)
========================================================================================================

The Open Energy Ontology (OEO) is a comprehensive domain ontology specifically designed for the energy system analysis context, covering concepts, relationships, and entities relevant to energy research and planning. Developed as part of the Open Energy Platform ecosystem, OEO provides standardized terminology for representing energy systems including generation, transmission, distribution, and consumption across diverse energy sources and technologies. The ontology is expressed in Manchester OWL Syntax to ensure user-friendliness for editing and version control, facilitating collaborative development and maintenance. OEO is actively maintained and continuously extended to incorporate emerging energy concepts, technologies, and regulatory frameworks relevant to energy system analysis and planning. The ontology is governed by a Steering Committee (OEO-SC) that ensures quality, alignment with community needs, and integration with ongoing energy research and policy projects. OEO enables standardized data representation, knowledge integration, and automated reasoning about energy systems for research, policy analysis, and strategic planning.

**Example Usage**:
Annotate an energy system dataset with OEO terms to describe energy sources (solar, wind, biomass), generation capacity, transmission networks, demand patterns, and storage systems to enable automated analysis of energy system configurations and transition scenarios.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 10
        * - **Total Edges**
          - 8
        * - **Root Nodes**
          - 8
        * - **Leaf Nodes**
          - 2
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 0
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
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.20
        * - **Depth Variance**
          - 0.16
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 8
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.00
        * - **Breadth Variance**
          - 9.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OEO

    ontology = OEO()
    ontology.load("path/to/OEO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
