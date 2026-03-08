.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Education
       * - **Category**
         - Library, Museums, Archives
       * - **Current Version**
         - 2.5.0
       * - **Last Updated**
         - 2022-10-03
       * - **Creator**
         - United States, Library of Congress
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Bibliographic Framework Ontology (BIBFRAME) <https://id.loc.gov/ontologies/bflc.html>`_

Bibliographic Framework Ontology (BIBFRAME)
========================================================================================================

The Bibliographic Framework Ontology (BIBFRAME) is a comprehensive RDF-based vocabulary developed by the Library of Congress to modernize bibliographic description for libraries, museums, and archives. It provides a structured model for representing bibliographic resources, focusing on three core classes: Work (the abstract creative content), Instance (the physical or digital embodiment), and Item (the specific copy). BIBFRAME supports detailed description of relationships among resources, such as translations, adaptations, and editions, as well as attributes like subject, extent, and publication information. The ontology is designed to facilitate linked data publishing, interoperability, and integration with other metadata standards, enabling richer discovery and reuse of bibliographic information. BIBFRAME is widely adopted by libraries and cultural heritage institutions transitioning from MARC records to semantic web technologies. Its extensible structure allows for domain-specific adaptations and integration with authority files, vocabularies, and digital repositories.

**Example Usage**:
Describe a library book using BIBFRAME by linking the Work (e.g., "Pride and Prejudice"), its Instance (the 2003 Penguin Classics edition), and the Item (the specific copy held by a library), including relationships to subjects, authors, and related works.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 967
        * - **Total Edges**
          - 2460
        * - **Root Nodes**
          - 6
        * - **Leaf Nodes**
          - 578
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 212
        * - **Individuals**
          - 0
        * - **Properties**
          - 215

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
          - 1.11
        * - **Depth Variance**
          - 0.54
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 22
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 9.00
        * - **Breadth Variance**
          - 59.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 134
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BIBFRAME

    ontology = BIBFRAME()
    ontology.load("path/to/BIBFRAME-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
