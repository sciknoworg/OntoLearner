.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2022-04-19
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Chemical Methods Ontology (ChMO) <https://github.com/rsc-ontologies/rsc-cmo>`_

Chemical Methods Ontology (ChMO)
========================================================================================================

The Chemical Methods Ontology (ChMO) is a comprehensive ontology that provides a structured vocabulary for describing chemical methods, experimental techniques, and analytical procedures used in chemistry and related sciences. ChMO contains over 3000 classes covering methods for data collection (e.g., mass spectrometry, electron microscopy), sample preparation and separation (e.g., ionisation, chromatography, electrophoresis), and material synthesis (e.g., epitaxy, vapor deposition). The ontology also describes the instruments and equipment used in these experiments, such as mass spectrometers and chromatography columns, as well as the outputs and results generated. ChMO enables semantic annotation of experimental workflows, facilitating data integration, reproducibility, and advanced analysis across chemical research and laboratory information systems. By providing a standardized framework, ChMO supports interoperability between chemical databases, electronic lab notebooks, and computational tools. The ontology is actively maintained and extended to incorporate new methods and technologies as the field evolves.

**Example Usage**:
Annotate a chemical experiment with ChMO terms to specify the analytical method (e.g., "liquid chromatography-mass spectrometry"), sample preparation steps, instrument configuration, and data outputs, enabling semantic search and integration with other chemical research datasets.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 24075
        * - **Total Edges**
          - 44651
        * - **Root Nodes**
          - 3100
        * - **Leaf Nodes**
          - 17250
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3202
        * - **Individuals**
          - 0
        * - **Properties**
          - 27

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.49
        * - **Depth Variance**
          - 0.63
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 13439
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 2993.88
        * - **Breadth Variance**
          - 20855464.86
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 3601
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ChMO

    ontology = ChMO()
    ontology.load("path/to/ChMO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
