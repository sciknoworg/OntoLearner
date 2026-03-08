.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - owl
       * - **Download**
         - `Download Material Ontology (MatOnto) <https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MatOnto.owl>`_

Material Ontology (MatOnto)
========================================================================================================

The Material Ontology (MatOnto) is a domain ontology based on the Basic Formal Ontology (BFO) designed to provide a structured vocabulary for representing materials, their properties, and relationships in materials science and engineering. MatOnto supports semantic annotation of materials data, enabling interoperability, data integration, and advanced analysis across research databases, digital twins, and manufacturing systems. The ontology covers key concepts such as material types, compositions, processing methods, properties, and applications. MatOnto is designed for extensibility, allowing researchers and engineers to describe new materials, characterization techniques, and performance metrics. By providing a standardized framework, MatOnto facilitates cross-study comparison, materials selection, and knowledge sharing in materials research and industry. The ontology is actively maintained and extended to incorporate new materials, technologies, and research requirements.

**Example Usage**:
Annotate a materials database with MatOnto terms to specify material types (e.g., polymer, alloy), composition, processing methods, and properties (e.g., tensile strength, thermal conductivity), enabling semantic search and integration with materials informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4753
        * - **Total Edges**
          - 11287
        * - **Root Nodes**
          - 33
        * - **Leaf Nodes**
          - 1063
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1307
        * - **Individuals**
          - 122
        * - **Properties**
          - 95

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 129
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 38.24
        * - **Depth Variance**
          - 1437.88
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 155
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 18.92
        * - **Breadth Variance**
          - 522.53
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 122
        * - **Taxonomic Relations**
          - 1215
        * - **Non-taxonomic Relations**
          - 167
        * - **Average Terms per Type**
          - 1.94
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MatOnto

    ontology = MatOnto()
    ontology.load("path/to/MatOnto-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
