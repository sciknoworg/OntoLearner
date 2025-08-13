

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Agriculture
       * - **Category**
         - Animal Science
       * - **Current Version**
         - 6.0
       * - **Last Updated**
         - May 11, 2020
       * - **Creator**
         - INRAE, France
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Animal Trait Ontology for Livestock (ATOL) <https://bioportal.bioontology.org/ontologies/ATOL>`_

Animal Trait Ontology for Livestock (ATOL)
========================================================================================================

ATOL (Animal Trait Ontology for Livestock) is an ontology of characteristics defining phenotypes of livestock     in their environment (EOL). ATOL aims to:     - provide a reference ontology of phenotypic traits of farm animals for the international scientific and educational     - communities, farmers, etc.;     - deliver this reference ontology in a language which can be used by computers in order to support database management,     semantic analysis and modeling;     - represent traits as generic as possible for livestock vertebrates;     - make the ATOL ontology as operational as possible and closely related to measurement techniques;     - structure the ontology in relation to animal production.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 8220
        * - **Total Edges**
          - 52090
        * - **Root Nodes**
          - 12
        * - **Leaf Nodes**
          - 5868
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 2352
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

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
          - 2.30
        * - **Depth Variance**
          - 2.58
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 38
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 16.12
        * - **Breadth Variance**
          - 137.86
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 2628
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ATOL

    ontology = ATOL()
    ontology.load("path/to/ATOL-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
