.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Upper Ontology
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2025-02-17
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Suggested Upper Merged Ontology (SUMO) <https://www.ontologyportal.org/>`_

Suggested Upper Merged Ontology (SUMO)
========================================================================================================

The Suggested Upper Merged Ontology (SUMO) is one of the largest and most widely used formal upper ontologies, providing a comprehensive framework for representing general concepts and relationships across many domains of knowledge [#sumo-github]_ [#sumo-paper]_. SUMO and its domain ontologies are used for research and applications in search, linguistics, automated reasoning, semantic interoperability, and artificial intelligence [#sumo-paper]_. The ontology covers abstract and concrete entities, processes, attributes, relations, and events, supporting logical inference and knowledge discovery [#sumo-github]_ [#sumo-paper]_. SUMO is open source and maintained through the Ontology Portal project, with ongoing extensions and domain-specific modules for specialized applications [#sumo-github]_. By providing a rigorous semantic foundation, SUMO facilitates interoperability, data integration, and advanced reasoning in knowledge-based systems [#sumo-paper]_.

**Example Usage**:
Use SUMO as an upper ontology for a domain knowledge graph, mapping domain entities such as ``Vehicle``, ``Process``, ``Agent``, or ``Communication`` to SUMO classes and relations. This enables logical reasoning, semantic search, knowledge discovery, and integration across heterogeneous knowledge-based systems [#sumo-github]_ [#sumo-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 288016
        * - **Total Edges**
          - 496645
        * - **Root Nodes**
          - 77015
        * - **Leaf Nodes**
          - 197102
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 4525
        * - **Individuals**
          - 80034
        * - **Properties**
          - 587

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 9
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.04
        * - **Depth Variance**
          - 1.39
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 77015
        * - **Minimum Breadth**
          - 10
        * - **Average Breadth**
          - 19045.20
        * - **Breadth Variance**
          - 739917637.16
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 80280
        * - **Taxonomic Relations**
          - 7174
        * - **Non-taxonomic Relations**
          - 310
        * - **Average Terms per Type**
          - 165.53
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SUMO

    ontology = SUMO()
    ontology.load("path/to/SUMO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#sumo-github] Ontology Portal. n.d.
   "SUMO: Suggested Upper Merged Ontology."
   GitHub Repository.
   Available at:
   `https://github.com/ontologyportal/sumo <https://github.com/ontologyportal/sumo>`_

.. [#sumo-paper] Pease, Adam, Ian Niles, and John Li. 2002.
   "The Suggested Upper Merged Ontology: A Large Ontology for the Semantic Web and its Applications."
   *AAAI Workshop on Ontologies and the Semantic Web*.
   Available at:
   `https://cdn.aaai.org/Workshops/2002/WS-02-11/WS02-11-011.pdf <https://cdn.aaai.org/Workshops/2002/WS-02-11/WS02-11-011.pdf>`_
