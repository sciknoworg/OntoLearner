.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2010-05-31
       * - **Creator**
         - Diego Daz
       * - **License**
         - N/A
       * - **Format**
         - ttl
       * - **Download**
         - `Download Ontology for the Steel Domain (ONTORULE) <https://raw.githubusercontent.com/ISE-FIZKarlsruhe/mseo.github.io/master/Ontology_files/ONTORULEsteel.ttl>`_

Ontology for the Steel Domain (ONTORULE)
========================================================================================================

The Ontology for the Steel Domain (ONTORULE) is a domain ontology developed for the steel industry use case, providing a structured vocabulary for representing concepts, attributes, and relationships relevant to steel production and processing. ONTORULE supports the semantic annotation of steel industry data, including materials, processes, equipment, and quality attributes, enabling data integration and knowledge sharing across manufacturing systems. The ontology is designed for extensibility and can be adapted to represent new steel grades, production methods, and regulatory requirements. ONTORULE facilitates advanced analytics, process optimization, and compliance management in the steel industry by providing a standardized framework for knowledge representation. The ontology is documented with an HTML specification generated from the OWL file and is aligned with best practices in industrial ontology development.

**Example Usage**:
Annotate a steel manufacturing process with ONTORULE terms to specify the materials used, process steps, equipment, and quality control attributes, enabling semantic search and integration with production and quality management systems.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 131
        * - **Total Edges**
          - 348
        * - **Root Nodes**
          - 4
        * - **Leaf Nodes**
          - 53
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 24
        * - **Individuals**
          - 13
        * - **Properties**
          - 37

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
          - 4
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 2.50
        * - **Breadth Variance**
          - 2.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 11
        * - **Taxonomic Relations**
          - 16
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 2.20
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ONTORULE

    ontology = ONTORULE()
    ontology.load("path/to/ONTORULE-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
