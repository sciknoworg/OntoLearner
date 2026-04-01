

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Arts and Humanities
       * - **Category**
         - Numismatics
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2025-01-22
       * - **Creator**
         - American Numismatic Society, Institute for the Study of the Ancient World
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Nomisma Ontology (Nomisma) <https://www.dainst.org/forschung/projekte/noslug/2098>`_

Nomisma Ontology (Nomisma)
========================================================================================================

The Nomisma Ontology is a collaborative framework that provides stable,
standardized digital representations of numismatic concepts according to
the principles of Linked Open Data. It offers HTTP URIs that provide
persistent access to reusable information about numismatic entities and
related concepts, enabling integration with other linked data resources
[#nomisma-project]_ [#numismatics-lod]_. The Nomisma community maintains
a formalized RDF ontology and a data model for encoding concepts, coins,
typologies, hoards, and other kinds of numismatic objects as linked open
data [#nomisma-project]_. The ontology and controlled vocabulary support
the description of entities such as coins, denominations, mints, rulers,
regions, and related numismatic concepts across different periods and
cultures [#nomisma-project]_ [#diginuma]_. It facilitates semantic
annotation of numismatic data and supports interoperability across
digital coin collections, archaeological datasets, and historical
research resources [#numismatics-lod]_ [#diginuma]_. By providing
standardized semantic representations, Nomisma enables querying,
integration, and comparative analysis of monetary and material culture
data within broader cultural heritage and digital humanities ecosystems
[#numismatics-lod]_ [#semantic-solutions]_.

**Example Usage**: Annotate a digital coin collection, hoard dataset, or
archaeological numismatic catalog with Nomisma terms for coin types,
denominations, mints, rulers, regions, and materials to enable semantic
search, linked data integration, and comparative analysis across
numismatic and historical datasets [#nomisma-project]_ [#numismatics-lod]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 245
        * - **Total Edges**
          - 431
        * - **Root Nodes**
          - 22
        * - **Leaf Nodes**
          - 113
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 36
        * - **Individuals**
          - 0
        * - **Properties**
          - 71

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.97
        * - **Depth Variance**
          - 0.73
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 22
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 15.00
        * - **Breadth Variance**
          - 67.50
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 13
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Nomisma

    ontology = Nomisma()
    ontology.load("path/to/Nomisma-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#nomisma-project] Deutsches Archäologisches Institut. n.d.
   "Nomisma.org - a linked open data approach to numismatics."
   Available at: `https://www.dainst.org/en/research/projects/nomismaorg-a-linked-data-approach-to-numismatics/2098 <https://www.dainst.org/en/research/projects/nomismaorg-a-linked-data-approach-to-numismatics/2098>`_

.. [#numismatics-lod] Gruber, E. 2021. "Numismatics and Linked Open Data."
   *ISAW Papers* 20(6).
   Available at: `https://dlib.nyu.edu/awdl/isaw/isaw-papers/20-6/ <https://dlib.nyu.edu/awdl/isaw/isaw-papers/20-6/>`_

.. [#diginuma] Rantala, H., Oksanen, E., Ehrnsten, F., and Hyvönen, E. 2022.
   "Harmonizing and Using Numismatic Linked Data in Digital Humanities
   Research and Application Development: Case DigiNUMA."
   In *The Semantic Web: ESWC 2022 Satellite Events*, pp. 141-146.
   Available at: `https://2022.eswc-conferences.org/wp-content/uploads/2022/05/pd_Rantala_et_al_paper_238.pdf <https://2022.eswc-conferences.org/wp-content/uploads/2022/05/pd_Rantala_et_al_paper_238.pdf>`_

.. [#semantic-solutions] Hyvönen, E., Rantala, H., Oksanen, E., and
   Ehrnsten, F. 2023. "Semantic Solutions for Democratizing
   Archaeological and Numismatic Data."
   *Journal on Computing and Cultural Heritage* 16(4).
   doi:10.1145/3625302
