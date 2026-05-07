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

The Units of Measurement Ontology (UO) is a domain ontology designed to provide a standardized vocabulary for metrical units, particularly for use with the Phenotype and Trait Ontology (PATO) and other biomedical ontologies [#uo-obofoundry]_ [#uo-paper]_. UO covers a wide range of measurement units, including SI units, derived units, and commonly used non-SI units, supporting the annotation of quantitative data in biological, medical, and scientific research [#uo-obofoundry]_ [#uo-paper]_. The ontology enables semantic interoperability and data integration by providing unique identifiers and structured relationships for units and measurement concepts [#uo-paper]_. UO is widely used in bioinformatics, clinical informatics, and scientific data repositories to ensure consistency and comparability of measurement data [#uo-paper]_. By providing a common framework for units of measurement, UO facilitates automated data analysis, semantic search, unit-aware annotation, and cross-study comparison [#uo-obofoundry]_ [#uo-paper]_. The ontology is maintained as part of the OBO Foundry ontology ecosystem [#uo-obofoundry]_.

**Example Usage**:
Annotate a biomedical dataset with UO terms to specify measurement units for phenotypic traits, such as ``UO:0000016`` for ``centimeter`` or ``UO:0000021`` for ``gram``. This enables semantic search, consistent quantitative annotation, and comparison of measurement data across biomedical datasets [#uo-obofoundry]_ [#uo-paper]_.

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

References
----------

.. [#uo-obofoundry] OBO Foundry. n.d.
   "Units of measurement ontology."
   Available at:
   `https://obofoundry.org/ontology/uo.html <https://obofoundry.org/ontology/uo.html>`_

.. [#uo-paper] Gkoutos, Georgios V., Paul N. Schofield, and Robert Hoehndorf. 2012.
   "The Units Ontology: a tool for integrating units of measurement in science."
   *Database* 2012: bas033.
   DOI:
   `10.1093/database/bas033 <https://doi.org/10.1093/database/bas033>`_
