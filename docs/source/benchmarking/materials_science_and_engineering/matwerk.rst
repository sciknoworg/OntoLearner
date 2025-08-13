

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Research Data, Interoperability
       * - **Current Version**
         - 3.0.0
       * - **Last Updated**
         - 2025-03-01
       * - **Creator**
         - Hossein Beygi Nasrabadi, Jörg Waitelonis, Ebrahim Norouzi, Kostiantyn Hubaiev, Harald Sack
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download NFDI MatWerk Ontology (MatWerk) <https://github.com/ISE-FIZKarlsruhe/mwo?tab=readme-ov-file>`_

NFDI MatWerk Ontology (MatWerk)
========================================================================================================

NFDI-MatWerk aims to establish a digital infrastructure for Materials Science and Engineering (MSE),     fostering improved data sharing and collaboration. This repository provides comprehensive documentation     for NFDI MatWerk Ontology (MWO) v3.0, a foundational framework designed to structure research data     and enhance interoperability within the MSE community. To ensure compliance with top-level ontology standards,     MWO v3.0 is aligned with the Basic Formal Ontology (BFO) and incorporates the modular approach     of the NFDIcore mid-level ontology, enriching metadata through standardized classes and properties.     The MWO addresses key aspects of MSE research data, including the NFDI-MatWerk community structure,     covering task areas, infrastructure use cases, projects, researchers, and organizations.     It also describes essential NFDI resources, such as software, workflows, ontologies, publications,     datasets, metadata schemas, instruments, facilities, and educational materials. Additionally,     MWO represents NFDI-MatWerk services, academic events, courses, and international collaborations.     As the foundation for the MSE Knowledge Graph, MWO facilitates efficient data integration and retrieval,     promoting collaboration and knowledge representation across MSE domains. This digital transformation     enhances data discoverability, reusability, and accelerates scientific exchange, innovation,     and discoveries by optimizing research data management and accessibility.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2554
        * - **Total Edges**
          - 4870
        * - **Root Nodes**
          - 86
        * - **Leaf Nodes**
          - 1384
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 449
        * - **Individuals**
          - 29
        * - **Properties**
          - 129

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.83
        * - **Depth Variance**
          - 5.95
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 148
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 40.00
        * - **Breadth Variance**
          - 1814.14
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 29
        * - **Taxonomic Relations**
          - 369
        * - **Non-taxonomic Relations**
          - 12
        * - **Average Terms per Type**
          - 4.14
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MatWerk

    ontology = MatWerk()
    ontology.load("path/to/MatWerk-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
