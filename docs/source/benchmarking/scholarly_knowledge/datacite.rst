

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

The DataCite Ontology is an RDF/OWL-based representation of the DataCite Metadata Schema, providing a standardized semantic structure for describing research data and other digital research outputs with citation and identification metadata [#datacite-ontology]_ [#datacite-schema]_. It enables formal representation of metadata properties including identifiers, creators, titles, publishers, publication years, contributors, subjects, funding references, resource types, and relationships to other research outputs [#datacite-schema]_. The ontology allows DataCite-related metadata concepts to be represented in RDF, supporting machine-readable identification, citation, linking, and integration of research resources [#datacite-ontology]_. The DataCite Metadata Schema supports the description of diverse research outputs, including datasets, software, textual resources, and other scholarly objects [#datacite-schema]_. By combining persistent identifiers with structured descriptive and relational metadata, DataCite supports discovery, citation, linking, and reuse across research repositories and scholarly information systems [#datacite-schema]_. The DataCite Ontology extends this model into a Semantic Web representation that can be integrated with other scholarly communication vocabularies and linked-data infrastructures [#datacite-ontology]_.

**Example Usage**: Represent a published research dataset with DataCite terms for its persistent identifier, such as a DOI; creators and contributors, including ORCID identifiers where available; title, publisher, publication year, subject areas, funding information, resource type, and relationships to associated publications or other research outputs. This supports machine-readable citation, discovery, linking, and reuse across research repositories and scholarly information systems [#datacite-schema]_ [#datacite-ontology]_.

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
   `https://sparontologies.github.io/datacite/current/datacite.html
   <https://sparontologies.github.io/datacite/current/datacite.html>`_

.. [#datacite-schema] DataCite Metadata Working Group. 2026.
   "DataCite Metadata Schema Documentation for the Publication and Citation of
   Research Data and Other Research Outputs."
   Version 4.7. DataCite e.V.
   Available at:
   `https://doi.org/10.14454/qdd3-ps68
   <https://doi.org/10.14454/qdd3-ps68>`_
