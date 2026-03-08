

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Biomedical Investigations
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2025-01-09
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Ontology for Biomedical Investigations (OBI) <https://github.com/obi-ontology/obi/tree/master>`_

Ontology for Biomedical Investigations (OBI)
========================================================================================================

The Ontology for Biomedical Investigations (OBI) provides a comprehensive vocabulary for describing scientific investigations, experimental designs, and biomedical research methodology. It defines over 2500 terms covering assays, devices, protocols, objectives, materials, measurements, and outcomes used in biomedical and life sciences research. OBI enables standardized semantic annotation of experimental workflows, making research methodologies transparent, reproducible, and interoperable across databases and computational systems. The ontology captures hierarchical relationships between experimental concepts, allowing researchers to precisely describe complex experimental designs and data collection procedures. OBI integrates with other biological ontologies (BFO, ChEBI, CHEBI) to provide comprehensive semantic representation of biomedical investigations.

**Example Usage**: Annotate a microarray experiment with OBI terms such as "assay" for the type of investigation, "microarray device" for equipment, "RNA extraction" for material preparation steps, and measurement-related terms for results.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 40613
        * - **Total Edges**
          - 104537
        * - **Root Nodes**
          - 177
        * - **Leaf Nodes**
          - 10917
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 9703
        * - **Individuals**
          - 301
        * - **Properties**
          - 94

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 28
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.15
        * - **Depth Variance**
          - 23.70
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 386
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 81.62
        * - **Breadth Variance**
          - 11040.03
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 286
        * - **Taxonomic Relations**
          - 11843
        * - **Non-taxonomic Relations**
          - 38
        * - **Average Terms per Type**
          - 5.61
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OBI

    ontology = OBI()
    ontology.load("path/to/OBI-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
