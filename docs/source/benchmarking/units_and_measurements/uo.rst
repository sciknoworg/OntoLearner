.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Units and Measurements
       * - **Category**
         - Units and Measurements
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2023-05-25
       * - **Creator**
         - KAUST
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Units of Measurement Ontology (UO) <https://bioportal.bioontology.org/ontologies/UO>`_

Units of Measurement Ontology (UO)
========================================================================================================

The Units of Measurement Ontology (UO) is a domain ontology designed to provide a standardized vocabulary for metrical units, particularly for use in conjunction with the Phenotype and Trait Ontology (PATO) and other biomedical ontologies. UO covers a wide range of units, including SI units, derived units, and commonly used non-SI units, supporting the annotation of quantitative data in biological, medical, and scientific research. The ontology enables semantic interoperability and data integration by providing unique identifiers and relationships for units, quantities, and measurement systems. UO is widely used in bioinformatics, clinical informatics, and data repositories to ensure consistency and comparability of measurement data. By providing a common framework, UO facilitates automated data analysis, unit conversion, and cross-study comparison. The ontology is actively maintained and extended to incorporate new units and measurement concepts as research needs evolve.

**Example Usage**:
Annotate a biomedical dataset with UO terms to specify measurement units for phenotypic traits (e.g., "UO:0000016 (centimeter)", "UO:0000021 (gram)") and enable automated unit conversion and semantic search across datasets.

.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 11
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 4.40
        * - **Breadth Variance**
          - 13.84
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 708
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import UO

    ontology = UO()
    ontology.load("path/to/UO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
