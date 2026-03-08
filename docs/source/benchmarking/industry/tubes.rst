.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Industry
       * - **Category**
         - Building Services
       * - **Current Version**
         - 0.3.0
       * - **Last Updated**
         - 2022-02-01
       * - **Creator**
         - Nicolas Pauen
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download TUBES System Ontology (TUBES) <https://rwth-e3d.github.io/tso/>`_

TUBES System Ontology (TUBES)
========================================================================================================

The TUBES System Ontology (TSO) is a domain ontology for the Architecture, Engineering, Construction, and Operations (AECO) industry, explicitly defining interconnected building service systems, their hierarchical subdivisions, structural and functional aspects, and links to spatial entities. TSO supports the semantic representation of building services such as HVAC, plumbing, and electrical systems, enabling detailed modeling of their components, relationships, and operational characteristics. The ontology is designed to facilitate the integration of building information across design, construction, and facility management processes, supporting digital twins and smart building applications. TSO aligns with other W3C community ontologies to ensure interoperability and data exchange in the semantic web of building data. By providing a standardized vocabulary, TSO enables automated reasoning, compliance checking, and lifecycle management of building services. The ontology is actively developed and adopted by industry stakeholders for advanced building information modeling (BIM) and digital transformation initiatives.

**Example Usage**:
Annotate a BIM model with TUBES terms to describe the HVAC system, its components (air handling units, ducts, sensors), their spatial locations, and operational relationships, enabling automated analysis and integration with facility management systems.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 610
        * - **Total Edges**
          - 1122
        * - **Root Nodes**
          - 9
        * - **Leaf Nodes**
          - 412
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 52
        * - **Individuals**
          - 0
        * - **Properties**
          - 101

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
          - 0.10
        * - **Depth Variance**
          - 0.09
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 9
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 5.00
        * - **Breadth Variance**
          - 16.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 31
        * - **Non-taxonomic Relations**
          - 3
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import TUBES

    ontology = TUBES()
    ontology.load("path/to/TUBES-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
