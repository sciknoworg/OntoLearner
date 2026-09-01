

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Upper Ontology
       * - **Current Version**
         - 12.1.0
       * - **Last Updated**
         - 2024-Feb-27
       * - **Creator**
         - Semantic Arts
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download GIST Upper Ontology (GIST) <https://semanticarts.com/gist>`_

GIST Upper Ontology (GIST)
========================================================================================================

GIST is Semantic Arts' minimalist upper ontology designed for enterprise
information systems, providing broad coverage of common business concepts
with a small set of primitives and reduced ambiguity [#gist-home]_
[#gist-repo]_. It is intended to serve as a practical starting point for
organizations building enterprise ontologies or semantic models for
business data integration [#gist-repo]_.

GIST emphasizes practical expressiveness, semantic clarity, and usability
in enterprise settings [#gist-home]_ [#gist-repo]_. It covers essential
business concepts such as agents, organizations, people, physical and
conceptual objects, events, measurements, units, places, agreements, and
other abstract entities, together with relationships that support
structured representation of enterprise knowledge [#gist-repo]_.

The ontology is deliberately lightweight so that it can be adopted and
extended more easily than larger or more complex upper ontologies
[#gist-home]_. GIST can support semantic querying, reasoning, knowledge
graph construction, enterprise data integration, data governance, and
business intelligence applications by providing a shared semantic
foundation for business information [#gist-home]_ [#gist-repo]_.

**Example Usage**: Design a healthcare enterprise ontology by extending
GIST's Agent concepts to represent physicians and patients, Event
concepts to represent treatments and procedures, and Object concepts to
represent medications and medical devices. This can support the creation
of a healthcare knowledge graph for clinical decision support, data
integration, and semantic querying across healthcare information systems
[#gist-home]_ [#gist-repo]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1352
        * - **Total Edges**
          - 2543
        * - **Root Nodes**
          - 77
        * - **Leaf Nodes**
          - 633
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 199
        * - **Individuals**
          - 8
        * - **Properties**
          - 113

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 27
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.14
        * - **Depth Variance**
          - 21.06
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 298
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 34.86
        * - **Breadth Variance**
          - 3571.91
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 8
        * - **Taxonomic Relations**
          - 39
        * - **Non-taxonomic Relations**
          - 56
        * - **Average Terms per Type**
          - 8.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GIST

    ontology = GIST()
    ontology.load("path/to/GIST-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#gist-home] Semantic Arts. n.d.
   "gist Upper Ontology."
   Available at:
   `https://www.semanticarts.com/gist/ <https://www.semanticarts.com/gist/>`_

.. [#gist-repo] Semantic Arts. n.d.
   "gist."
   GitHub Repository.
   Available at:
   `https://github.com/semanticarts/gist <https://github.com/semanticarts/gist>`_
