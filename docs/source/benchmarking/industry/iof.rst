.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Industry
       * - **Category**
         - Manufacturing
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2020
       * - **Creator**
         - IOF Core Working Group
       * - **License**
         - MIT
       * - **Format**
         - rdf
       * - **Download**
         - `Download Industrial Ontology Foundry (IOF) <https://oagi.org/pages/Released-Ontologies>`_

Industrial Ontology Foundry (IOF)
========================================================================================================

The Industrial Ontology Foundry (IOF) Core Ontology is a foundational ontology for the manufacturing industry, capturing concepts and relationships common across multiple manufacturing domains [#iof-github]_ [#iof-core-paper]_. It is implemented in RDF/OWL and leverages the Basic Formal Ontology (BFO) as its upper-level framework, while also incorporating terms from other domain-independent and mid-level ontologies [#iof-github]_. IOF Core provides a standardized vocabulary for describing manufacturing-related concepts that support cross-system integration within factories, across enterprises, between suppliers and manufacturers, and throughout the product life cycle [#iof-github]_ [#iof-core-paper]_. The ontology is designed to ensure consistency and interoperability across domain-specific reference ontologies published by the IOF [#iof-github]_. IOF Core supports advanced applications such as smart manufacturing, industrial knowledge graphs, supply chain modeling, digital twins, industrial automation, data sharing, analytics, and knowledge management in the manufacturing sector [#iof-core-paper]_.

**Example Usage**:
Annotate a smart factory system with IOF Core terms to describe production lines, machines, materials, process steps, and organizational relationships, enabling integration with enterprise resource planning (ERP), manufacturing execution systems (MES), supply chain systems, and industrial knowledge graphs [#iof-github]_ [#iof-core-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1442
        * - **Total Edges**
          - 2686
        * - **Root Nodes**
          - 13
        * - **Leaf Nodes**
          - 716
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 212
        * - **Individuals**
          - 0
        * - **Properties**
          - 51

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 36
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 7.89
        * - **Depth Variance**
          - 35.71
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 117
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 24.32
        * - **Breadth Variance**
          - 922.11
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 87
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import IOF

    ontology = IOF()
    ontology.load("path/to/IOF-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#iof-github] Industrial Ontologies Foundry. n.d.
   "Industrial Ontologies Foundry."
   GitHub Repository.
   Available at:
   `https://github.com/iofoundry/ontology <https://github.com/iofoundry/ontology>`_

.. [#iof-core-paper] Kulvatunyou, Boonserm, Milos Drobnjakovic, Farhad Ameri, Chris Will, and Barry Smith. 2022.
   "The Industrial Ontologies Foundry (IOF) Core Ontology."
   *Formal Ontologies Meet Industry (FOMI) 2022*.
   Available at:
   `https://www.nist.gov/publications/industrial-ontologies-foundry-iof-core-ontology <https://www.nist.gov/publications/industrial-ontologies-foundry-iof-core-ontology>`_
