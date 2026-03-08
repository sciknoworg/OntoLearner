.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Mass Spectrometry, Proteomics
       * - **Current Version**
         - None
       * - **Last Updated**
         - 12:02:2025
       * - **Creator**
         - Andreas Bertsch
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Mass Spectrometry Ontology (MassSpectrometry) <https://terminology.tib.eu/ts/ontologies/MS>`_

Mass Spectrometry Ontology (MassSpectrometry)
========================================================================================================

A structured controlled vocabulary for the annotation of experiments concerned with proteomics mass spectrometry.

The Mass Spectrometry Ontology (MassSpectrometry) is a structured controlled vocabulary designed to annotate experiments in the field of proteomics mass spectrometry. It provides a standardized framework for describing experimental setups, instrumentation, data acquisition methods, and analysis workflows. The ontology captures essential concepts such as ionization techniques, mass analyzers, fragmentation methods, and data processing algorithms. By offering a common language for mass spectrometry, it facilitates data sharing, integration, and reproducibility across proteomics studies. The ontology is widely used in bioinformatics pipelines, proteomics databases, and experimental repositories to ensure semantic consistency and interoperability. Researchers can leverage the Mass Spectrometry Ontology to annotate datasets, describe experimental protocols, and enable advanced queries for comparative analyses.

**Example Usage**:
Annotate a proteomics experiment with MassSpectrometry terms to specify the ionization method (e.g., "electrospray ionization"), mass analyzer type (e.g., "time-of-flight"), and data processing software used for peak detection and quantification.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 17851
        * - **Total Edges**
          - 51814
        * - **Root Nodes**
          - 3786
        * - **Leaf Nodes**
          - 7959
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3636
        * - **Individuals**
          - 0
        * - **Properties**
          - 12

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.16
        * - **Depth Variance**
          - 0.58
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 7345
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 2534.57
        * - **Breadth Variance**
          - 9465403.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 7016
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MassSpectrometry

    ontology = MassSpectrometry()
    ontology.load("path/to/MassSpectrometry-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
