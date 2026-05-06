.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scholarly Communication
       * - **Current Version**
         - 2.8.1
       * - **Last Updated**
         - 2018-02-16
       * - **Creator**
         - Silvio Peroni, David Shotton
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Citation Typing Ontology (CiTO) <https://github.com/SPAROntologies/cito/tree/master/docs/current>`_

Citation Typing Ontology (CiTO)
========================================================================================================

The Citation Typing Ontology (CiTO) is an ontology that enables characterization of the nature or type of citations, both factually and rhetorically [#cito-spec]_ [#cito-paper]_. It provides a structured vocabulary for describing citation relationships between citing and cited scholarly works, including whether a citation supports, extends, disputes, uses methods from, reviews, or obtains background from another work [#cito-spec]_. CiTO enables citation metadata to describe not only the existence of a citation link, but also the author's citation intent and the scholarly context of that relationship [#cito-spec]_ [#cito-paper]_.

The ontology employs an OWL-based modeling approach, defining citation properties such as ``cito:cites`` and more specific subproperties for different citation functions [#cito-spec]_. These properties are organized into hierarchies, enabling structured retrieval, reasoning, and analysis of citation networks [#cito-spec]_. CiTO supports integration of citation data from different scholarly sources and publishing platforms, promoting interoperability and data-driven research in scholarly communication [#cito-paper]_.

Typical applications of CiTO include semantic citation annotation, citation network analysis, scholarly knowledge graph construction, citation intent analysis, and integration of bibliographic datasets for advanced analytics and knowledge discovery [#cito-paper]_. By providing a standardized vocabulary and framework, CiTO enhances semantic interoperability and supports richer analysis of how scholarly works relate to one another [#cito-spec]_ [#cito-paper]_.

**Example Usage**:
Annotate a research paper with CiTO terms to specify citation relationships and contexts, such as ``cito:citesAsEvidence``, ``cito:extends``, ``cito:usesMethodIn``, or ``cito:disagreesWith``. This enables semantic search, citation intent analysis, and integration with scholarly communication platforms [#cito-spec]_ [#cito-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 312
        * - **Total Edges**
          - 574
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 182
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 10
        * - **Individuals**
          - 0
        * - **Properties**
          - 101

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.56
        * - **Depth Variance**
          - 0.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 11
        * - **Average Breadth**
          - 12.50
        * - **Breadth Variance**
          - 2.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 9
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CiTO

    ontology = CiTO()
    ontology.load("path/to/CiTO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#cito-spec] SPAR Ontologies. 2018.
   "CiTO, the Citation Typing Ontology."
   Available at:
   `https://sparontologies.github.io/cito/current/cito.html <https://sparontologies.github.io/cito/current/cito.html>`_

.. [#cito-paper] Shotton, David. 2010.
   "CiTO, the Citation Typing Ontology."
   *Journal of Biomedical Semantics* 1(Suppl 1): S6.
   DOI:
   `10.1186/2041-1480-1-S1-S6 <https://doi.org/10.1186/2041-1480-1-S1-S6>`_
