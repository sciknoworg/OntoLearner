

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

The DataCite Ontology is an RDF/OWL-based representation of the DataCite Metadata Schema, providing a standardized semantic structure for describing research data and other digital research objects with citation and identification metadata [#datacite-ontology]_ [#datacite-schema]_. It enables formal representation of essential metadata properties, including identifiers, creators, titles, publishers, publication dates, contributors, subjects, funding information, resource types, and relationships to other scholarly resources [#datacite-schema]_. The ontology allows DataCite metadata properties to be described in RDF, supporting machine-readable representation of resources for accurate identification, retrieval, citation, and linking [#datacite-ontology]_. DataCite metadata supports the description of diverse research outputs, including datasets, software, publications, and other digital objects [#datacite-schema]_. By providing standardized semantic metadata structures, the DataCite Ontology supports data discovery, citation tracking, scholarly linking, research impact assessment, and integration with linked data and FAIR-oriented research infrastructures [#datacite-ontology]_ [#datacite-schema]_.

**Example Usage**: Represent a published research dataset with DataCite ontology terms for its persistent identifier, such as a DOI; creators and contributors, including ORCID identifiers where available; title, publisher, publication date, subject areas, funding information, resource type, and related publications. This enables proper citation, discovery, linking, and reuse across research repositories and scholarly information systems [#datacite-ontology]_ [#datacite-schema]_.

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

References
----------

.. [#datacite-ontology] SPAR Ontologies. n.d.
   "The DataCite Ontology."
   Available at:
   `https://sparontologies.github.io/datacite/current/datacite.html <https://sparontologies.github.io/datacite/current/datacite.html>`_

.. [#datacite-schema] DataCite. n.d.
   "DataCite Metadata Schema."
   Available at:
   `https://schema.datacite.org/ <https://schema.datacite.org/>`_
