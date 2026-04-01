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

ATOL (Animal Trait Ontology for Livestock) is an ontology of
characteristics defining phenotypes of livestock in their environment
[#inra]_ [#atol-paper]_. ATOL aims to provide a reference ontology of
phenotypic traits for farm animals for the international scientific and
educational communities and other stakeholders, and to deliver this
reference ontology in a form that can be used by computers to support
database management, semantic analysis, and modeling [#inra]_. It is
designed to represent traits as generically as possible for livestock
vertebrates, to remain closely related to measurement techniques, and to
structure the ontology in relation to animal production [#inra]_. The
multi-species ATOL model was developed as a reference source for
indexing phenotype databases and scientific papers, and it covers major
livestock production topics including growth and meat quality, animal
nutrition, milk production, reproduction, and welfare [#atol-paper]_.
By providing a standardized vocabulary and semantic framework, ATOL
supports consistent annotation, interoperability, and integration of
livestock phenotype data across animal science resources [#inra]_
[#agroportal]_.

**Example Usage**: Annotate a livestock dataset with ATOL terms to specify phenotypic
traits, measurement techniques, and related data, enabling semantic
search and integration with animal science research platforms
[#inra]_ [#atol-paper]_.

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

References
----------

.. [#inra] INRAE Open Data. n.d. "Animal Trait Ontology for Livestock."
   Available at: https://opendata.inra.fr/ATOL/page/

.. [#agroportal] AgroPortal. n.d. "ATOL | Summary."
   Available at: https://agroportal.lirmm.fr/ontologies/ATOL

.. [#atol-paper] Golik, W., Dameron, O., Bugeon, J., Fatet, A., Hue, I.,
   Hurtaud, C., Reichstadt, M., Salaün, M.-C., Vernet, J., Joret, L.,
   Papazian, F., Nédellec, C., and Le Bail, P.-Y. 2012.
   "ATOL: The Multi-species Livestock Trait Ontology."
   In *Metadata and Semantics Research*, CCIS 343, 289-300.
   doi:10.1007/978-3-642-35233-1_28
