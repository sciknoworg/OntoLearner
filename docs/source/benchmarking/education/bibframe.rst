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

The Bibliographic Framework Ontology (BIBFRAME) is an RDF-based
vocabulary developed by the Library of Congress to modernize
bibliographic description for libraries, museums, and archives
[#bibframe-report]_ [#bibframe-loc]_. It provides a structured model
for representing bibliographic resources, centered on core classes such
as Work, Instance, and Item, together with properties for describing
relationships, subjects, contributions, publication details, and other
bibliographic characteristics [#bibframe-loc]_ [#bibframe-report]_.
BIBFRAME is designed to support linked data publishing, semantic
interoperability, and integration with other metadata standards,
enabling richer discovery and reuse of bibliographic information
[#bibframe-report]_ [#bibframe-loc]_. By providing an extensible
semantic framework for bibliographic description, BIBFRAME supports the
transition from legacy cataloging models to linked data environments in
libraries and cultural heritage institutions [#bibframe-report]_
[#bibframe-loc]_.

**Example Usage**: Describe a library book using BIBFRAME by linking the
Work, such as *Pride and Prejudice*, to an Instance representing a
specific edition and to an Item representing a particular copy held by a
library, while also connecting the resource to authors, subjects, and
related works for improved discovery and interoperability
[#bibframe-loc]_ [#bibframe-report]_.

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

References
----------

.. [#bibframe-report] Library of Congress. 2012.
   "Bibliographic Framework as a Web of Data: Linked Data Model and
   Supporting Services."
   Available at:
   `https://www.loc.gov/bibframe/news/pdf/marcld-report-11-21-2012.pdf <https://www.loc.gov/bibframe/news/pdf/marcld-report-11-21-2012.pdf>`_

   .. [#bibframe-loc] Library of Congress. n.d. "BIBFRAME Model, Vocabulary,
   Guidelines, Examples, and Vocabulary Mapping."
   Available at:
   `https://www.loc.gov/bibframe/docs/index.html <https://www.loc.gov/bibframe/docs/index.html>`_
