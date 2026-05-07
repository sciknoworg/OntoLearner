.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Linguistics
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 19-04-2016
       * - **Creator**
         - Aldo Gangemi
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Framester Ontology (Framester) <http://150.146.207.114/lode/extract?url=http://ontologydesignpatterns.org/ont/framester/framester.owl>`_

Framester Ontology (Framester)
========================================================================================================

Framester is a frame-based ontological resource that acts as a hub between linguistic and factual resources such as FrameNet, WordNet, VerbNet, BabelNet, DBpedia, YAGO, and DOLCE-Zero [#framester-home]_ [#framester-paper]_. It uses WordNet and FrameNet as core resources, expands connections to other resources transitively, and represents them in a formal version of frame semantics [#framester-paper]_. By leveraging links across lexical, ontological, and linked data resources, Framester creates an interoperable predicate space that supports linguistic linked data integration, frame-based knowledge representation, and semantic reasoning [#framester-home]_ [#framester-paper]_.

The ontology provides a structured framework for representing frames, frame elements, lexical units, semantic roles, synsets, and relationships between linguistic and factual resources [#framester-paper]_. Framester applies a formal treatment of Fillmore-style frame semantics, enabling OWL querying and reasoning over a large frame-based knowledge graph [#framester-paper]_. It also supports applications such as word frame disambiguation, semantic role labeling, knowledge graph construction from text, and integration of heterogeneous linguistic datasets [#framester-paper]_.

Typical applications of Framester include linguistic resource alignment, semantic annotation, natural language understanding, frame detection, semantic role analysis, and enrichment of knowledge graphs with frame-based meaning representations [#framester-home]_ [#framester-paper]_. By providing a shared frame-oriented semantic layer, Framester improves interoperability between lexical resources and supports advanced research in computational linguistics, semantic web technologies, and knowledge discovery [#framester-paper]_.

**Example Usage**:
Annotate a linguistic dataset with Framester terms to represent evoked frames, lexical units, semantic roles, frame elements, and mappings to resources such as FrameNet, WordNet, VerbNet, BabelNet, DBpedia, and YAGO. This enables semantic search, frame-based reasoning, word frame disambiguation, and integration with linguistic linked data platforms [#framester-home]_ [#framester-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 174
        * - **Total Edges**
          - 398
        * - **Root Nodes**
          - 85
        * - **Leaf Nodes**
          - 38
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 59
        * - **Individuals**
          - 0
        * - **Properties**
          - 77

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
          - 0.69
        * - **Depth Variance**
          - 0.65
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 85
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 42.25
        * - **Breadth Variance**
          - 937.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 135
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Framester

    ontology = Framester()
    ontology.load("path/to/Framester-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

eferences
----------

.. [#framester-home] Framester. n.d.
   "Framester."
   Available at:
   `https://etna.istc.cnr.it/framester_web/ <https://etna.istc.cnr.it/framester_web/>`_

.. [#framester-paper] Gangemi, Aldo, Mehwish Alam, Luigi Asprino,
   Valentina Presutti, and Diego Reforgiato Recupero. 2016.
   "Framester: A Wide Coverage Linguistic Linked Data Hub."
   *The Semantic Web: ESWC 2016 Satellite Events / EKAW 2016*, Lecture Notes in Computer Science.
   Available at:
   `https://www.fiz-karlsruhe.de/sites/default/files/FIZ/Dokumente/Forschung/ISE/Publications/EKAW-16.pdf <https://www.fiz-karlsruhe.de/sites/default/files/FIZ/Dokumente/Forschung/ISE/Publications/EKAW-16.pdf>`_
