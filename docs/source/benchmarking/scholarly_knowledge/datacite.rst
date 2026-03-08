

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Metadata
       * - **Current Version**
         - 3.1
       * - **Last Updated**
         - 15/09/2022
       * - **Creator**
         - David Shotton, Silvio Peroni
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download DataCite Ontology (DataCite) <https://schema.datacite.org/>`_

DataCite Ontology (DataCite)
========================================================================================================

The DataCite Ontology is an RDF-based representation of the DataCite Metadata Schema, providing standardized vocabulary and semantic structure for describing research data and digital objects with comprehensive citation and identification metadata. It enables formal representation of essential dataset properties including creators, titles, publication dates, contributors, funding information, and relationships to other scholarly resources. DataCite provides machine-readable definitions of metadata properties for accurate and consistent identification, retrieval, and citation of diverse digital resources including datasets, software, and research outputs. The ontology supports FAIR data principles by enabling standardized, interoperable representation of dataset metadata in linked data formats (RDF, JSON-LD). DataCite facilitates data discovery, citation tracking, and research impact assessment by providing standardized semantic metadata structures.

**Example Usage**: Represent a published research dataset with DataCite ontology terms including persistent identifier (DOI), creators and contributors (with ORCID), publication date, subject areas, funding information, and related publications to enable proper citation and discovery across research repositories.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 260
        * - **Total Edges**
          - 519
        * - **Root Nodes**
          - 14
        * - **Leaf Nodes**
          - 120
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 19
        * - **Individuals**
          - 70
        * - **Properties**
          - 10

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 8
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.21
        * - **Depth Variance**
          - 5.93
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 7.56
        * - **Breadth Variance**
          - 9.80
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 71
        * - **Taxonomic Relations**
          - 27
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 8.88
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DataCite

    ontology = DataCite()
    ontology.load("path/to/DataCite-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
