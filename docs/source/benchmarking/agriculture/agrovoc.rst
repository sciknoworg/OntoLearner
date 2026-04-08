.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Agriculture
       * - **Category**
         - Agricultural Knowledge
       * - **Current Version**
         - 2024-04
       * - **Last Updated**
         - August 12, 2024
       * - **Creator**
         - Food and Agriculture Organization of the United Nations
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download AGROVOC Multilingual Thesaurus (AGROVOC) <https://agroportal.lirmm.fr/ontologies/AGROVOC>`_

AGROVOC Multilingual Thesaurus (AGROVOC)
========================================================================================================

AGROVOC is a multilingual thesaurus and Linked Open Data resource
developed and maintained by the Food and Agriculture Organization (FAO)
of the United Nations [#fao-home]_ [#linked-dataset]_. It provides a
structured collection of agricultural concepts, terms, definitions, and
relationships that support unambiguous resource identification,
standardized indexing, and more efficient search [#fao-home]_.
As a multilingual knowledge organization system, AGROVOC facilitates
access to agricultural information across domains and languages
[#fao-home]_ [#linked-dataset]_. It covers concepts relevant to food,
agriculture, fisheries, forestry, environment, and related domains, and
supports semantic interoperability through hierarchical and associative
relationships as well as links to other vocabularies and datasets
[#fao-home]_ [#linked-dataset]_. AGROVOC is widely used for data
annotation, knowledge organization, and information retrieval in
agricultural and food-related information systems [#fao-home]_
[#linked-dataset]_.

**Example Usage**: Annotate a multilingual agricultural dataset with
AGROVOC concepts for crops, soil types, pests, livestock, and farming
practices to enable standardized indexing, semantic interoperability,
and cross-language search across agricultural databases and repositories
[#fao-home]_ [#linked-dataset]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2279766
        * - **Total Edges**
          - 10140352
        * - **Root Nodes**
          - 59
        * - **Leaf Nodes**
          - 981249
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 35
        * - **Individuals**
          - 1234769
        * - **Properties**
          - 209

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 11
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.24
        * - **Depth Variance**
          - 2.31
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 617543
        * - **Minimum Breadth**
          - 9
        * - **Average Breadth**
          - 189858.08
        * - **Breadth Variance**
          - 44142143480.08
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 12
        * - **Taxonomic Relations**
          - 11
        * - **Non-taxonomic Relations**
          - 7
        * - **Average Terms per Type**
          - 3.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AGROVOC

    ontology = AGROVOC()
    ontology.load("path/to/AGROVOC-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#fao-home] Food and Agriculture Organization of the United Nations
   (FAO). n.d. "AGROVOC."
   Available at:
   https://www.fao.org/agrovoc/

.. [#linked-dataset] Caracciolo, C., Stellato, A., Morshed, A.,
   Johannsen, G., Rajbhandari, S., Jaques, Y., and Keizer, J. 2013.
   "The AGROVOC Linked Dataset." *Semantic Web* 4(3):341-348.
   Available at:
   https://www.fao.org/agrovoc/publications/agrovoc-linked-dataset
