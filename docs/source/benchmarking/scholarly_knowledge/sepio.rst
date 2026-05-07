.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scientific Evidence
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2015-02-23
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Scientific Evidence and Provenance Information Ontology (SEPIO) <https://terminology.tib.eu/ts/ontologies/SEPIO>`_

Scientific Evidence and Provenance Information Ontology (SEPIO)
========================================================================================================
The Scientific Evidence and Provenance Information Ontology (SEPIO) is an ontology for representing scientific evidence and provenance information, especially in relation to scientific claims [#sepio-github]_ [#sepio-bioportal]_. SEPIO provides a structured vocabulary for describing claims, evidence lines, information items, methods, tools, agents, and the provenance relationships involved in the creation and evaluation of scientific assertions [#sepio-bioportal]_.

The ontology employs a class-based modeling approach, defining classes for different types of scientific evidence, provenance, claims, evidence lines, and related information objects, along with properties to describe their relationships and interactions [#sepio-github]_ [#sepio-bioportal]_. Hierarchies and relations are used to organize evidence and provenance information, enabling structured retrieval, analysis, and comparison of scientific claims [#sepio-bioportal]_. SEPIO supports the integration of evidence and provenance metadata from various sources, promoting interoperability and data-driven research in scientific evidence representation [#sepio-github]_.

Typical applications of SEPIO include scientific claim annotation, evidence modeling, provenance tracking, data integration, curation, knowledge discovery, and manual or computational evaluation of scientific claims [#sepio-bioportal]_. By providing a standardized vocabulary and framework, SEPIO enhances interoperability and supports richer analysis of scientific evidence and provenance across research data platforms [#sepio-github]_ [#sepio-bioportal]_.

**Example Usage**:
Annotate a scientific study with SEPIO terms to specify a scientific claim, the evidence lines supporting or evaluating it, the information items used as evidence, and the methods, tools, and agents involved in producing that evidence. This enables semantic search, provenance tracking, claim evaluation, and integration with scientific evidence platforms [#sepio-github]_ [#sepio-bioportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1262
        * - **Total Edges**
          - 2385
        * - **Root Nodes**
          - 72
        * - **Leaf Nodes**
          - 781
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 129
        * - **Individuals**
          - 21
        * - **Properties**
          - 117

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 14
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.17
        * - **Depth Variance**
          - 8.36
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 170
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 40.60
        * - **Breadth Variance**
          - 2186.24
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 21
        * - **Taxonomic Relations**
          - 141
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 4.20
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SEPIO

    ontology = SEPIO()
    ontology.load("path/to/SEPIO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#sepio-github] Monarch Initiative. n.d.
   "Scientific Evidence and Provenance Information Ontology."
   GitHub Repository.
   Available at:
   `https://github.com/monarch-initiative/SEPIO-ontology <https://github.com/monarch-initiative/SEPIO-ontology>`_

.. [#sepio-bioportal] NCBO BioPortal. 2023.
   "Scientific Evidence and Provenance Information Ontology."
   Available at:
   `https://bioportal.bioontology.org/ontologies/SEPIO <https://bioportal.bioontology.org/ontologies/SEPIO>`_
