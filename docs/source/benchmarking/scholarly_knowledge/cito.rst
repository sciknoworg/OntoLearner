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

The Citation Typing Ontology (CiTO) is an ontology for characterizing the nature or type of citations between scholarly works, including both factual and rhetorical citation relationships [#cito-spec]_ [#cito-paper]_. It provides a structured vocabulary for describing how a citing work relates to a cited work, for example whether the citation provides evidence, extends previous work, uses a method, discusses, reviews, or disagrees with the cited resource [#cito-paper]_. CiTO therefore enables citation metadata to express not only that a citation exists, but also the scholarly function or intent associated with that citation [#cito-spec]_ [#cito-paper]_.

CiTO is part of the SPAR ontologies and is closely related to FaBiO, which provides terms for describing bibliographic entities and scholarly publications [#cito-paper]_. CiTO defines citation properties such as ``cito:cites`` together with more specific subproperties representing different citation functions [#cito-spec]_ [#cito-paper]_. These properties support structured representation, querying, and analysis of citation networks and enable richer semantic descriptions of relationships between scholarly resources [#cito-paper]_.

Typical applications of CiTO include semantic citation annotation, citation network analysis, scholarly knowledge graph construction, citation-intent analysis, and integration of bibliographic data from different scholarly sources [#cito-paper]_. By providing a standardized semantic vocabulary for citation relationships, CiTO supports interoperability and more expressive analysis of scholarly communication [#cito-spec]_ [#cito-paper]_.

**Example Usage**:
Annotate a research paper with CiTO properties such as ``cito:citesAsEvidence``, ``cito:extends``, ``cito:usesMethodIn``, or ``cito:disagreesWith`` to specify the function of individual citations. This enables machine-readable citation semantics, citation-intent analysis, and integration of citation information within scholarly knowledge graphs and bibliographic systems [#cito-spec]_ [#cito-paper]_.

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
   `https://sparontologies.github.io/cito/current/cito.html
   <https://sparontologies.github.io/cito/current/cito.html>`_

.. [#cito-paper] Peroni, S., and Shotton, D. 2012.
   "FaBiO and CiTO: Ontologies for Describing Bibliographic
   Resources and Citations."
   *Journal of Web Semantics*.
   Available at:
   `https://doi.org/10.1016/j.websem.2012.08.001
   <https://doi.org/10.1016/j.websem.2012.08.001>`_
