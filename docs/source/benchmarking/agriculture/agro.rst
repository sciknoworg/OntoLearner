

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Agriculture
       * - **Category**
         - Agronomy
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2022-11-02
       * - **Creator**
         - The Crop Ontology Consortium
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Agronomy Ontology (AgrO) <https://agroportal.lirmm.fr/ontologies/AGRO?p=summary>`_

Agronomy Ontology (AgrO)
========================================================================================================

The Agronomy Ontology (AgrO) provides terms from the agronomy domain
that are semantically organized and facilitate the collection, storage,
and use of agronomic data, enabling easier interpretation and reuse by
both humans and machines [#cgiar]_ [#obo]_. To analyze the effects of
varying practices within cropping systems, it is often necessary to
integrate data from multiple disciplinary domains. For example, data on
field management, soil, weather, and crop phenotypes may need to be
combined to assess crop performance under different management
interventions. However, agronomic data are often collected, described,
and stored in inconsistent ways, which impedes data comparison, mining,
interpretation, and reuse [#cgiar]_. The use of standards for metadata
and data annotation plays a key role in addressing these challenges.
While the CG Core Metadata Schema provides a metadata standard to
describe agricultural datasets, the Agronomy Ontology enables the
description of agronomic variables using standardized and semantically
defined terms [#cgiar]_ [#agrofims]_. AgrO specifically covers agronomic
practices, techniques, and variables used in agronomic experiments and
reuses terms from other ontologies to support interoperability [#obo]_.

**Example Usage**: Annotate agronomic field experiment data with AgrO terms for management
practices, treatments, and measured variables to enable standardized
description, interoperable storage, and cross-study comparison of
agricultural data [#obo]_ [#agrofims]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 31951
        * - **Total Edges**
          - 80144
        * - **Root Nodes**
          - 5369
        * - **Leaf Nodes**
          - 14046
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 5778
        * - **Individuals**
          - 326
        * - **Properties**
          - 209

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 22
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.92
        * - **Depth Variance**
          - 6.01
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 7562
        * - **Minimum Breadth**
          - 6
        * - **Average Breadth**
          - 1033.17
        * - **Breadth Variance**
          - 4403827.97
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 71
        * - **Taxonomic Relations**
          - 10931
        * - **Non-taxonomic Relations**
          - 1699
        * - **Average Terms per Type**
          - 4.18
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AgrO

    ontology = AgrO()
    ontology.load("path/to/AgrO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#cgiar] CGIAR. n.d. "Agronomy Ontology."
   Available at: https://bigdata.cgiar.org/resources/agronomy-ontology/

.. [#obo] OBO Foundry. n.d. "Agronomy Ontology (AGRO)."
   Available at: https://obofoundry.org/ontology/agro.html

.. [#agrofims] Devare, M., Aubert, C., Benites Alfaro, O. E.,
   Perez Masias, I. O., and Laporte, M.-A. 2021.
   "AgroFIMS: A Tool to Enable Digital Collection of
   Standards-Compliant FAIR Data."
   *Frontiers in Sustainable Food Systems* 5:726646.
   Available at:
   https://www.frontiersin.org/journals/sustainable-food-systems/articles/10.3389/fsufs.2021.726646/full
