

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Agriculture
       * - **Category**
         - Plant Anatomy, Morphology, Growth and Development
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Plant Ontology (PO) <https://github.com/Planteome/plant-ontology>`_

Plant Ontology (PO)
========================================================================================================

The Plant Ontology (PO) is a structured vocabulary and database resource that links plant anatomy, morphology and growth and development to plant genomics data. Developed collaboratively by plant biologists and ontology experts, PO provides a comprehensive framework for describing plant structures and developmental stages. The ontology integrates anatomical terms that can be associated with plant genes, enabling researchers to annotate phenotypic data and support comparative genomics across plant species. PO is designed to facilitate seamless data integration and interoperability in plant science research, allowing scientists to discover relationships between genes and plant structures. With its hierarchical organization of plant parts from whole organism level down to cellular structures, PO supports diverse applications including literature curation, genome annotation, and systems biology studies. The ontology is actively maintained by the Planteome project and integrated with other biological ontologies to ensure compatibility and comprehensive semantic representation in the plant science community.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 20790
        * - **Total Edges**
          - 60638
        * - **Root Nodes**
          - 5936
        * - **Leaf Nodes**
          - 11639
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1874
        * - **Individuals**
          - 0
        * - **Properties**
          - 13

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
          - 1.07
        * - **Depth Variance**
          - 0.72
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 8034
        * - **Minimum Breadth**
          - 82
        * - **Average Breadth**
          - 3462.50
        * - **Breadth Variance**
          - 11752362.58
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 2863
        * - **Non-taxonomic Relations**
          - 36
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PO

    ontology = PO()
    ontology.load("path/to/PO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
