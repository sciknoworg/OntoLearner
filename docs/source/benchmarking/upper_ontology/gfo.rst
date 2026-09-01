.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Upper Ontology
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2024-11-18
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download General Formal Ontology (GFO) <https://onto-med.github.io/GFO/release/2024-11-18/index-en.html>`_

General Formal Ontology (GFO)
========================================================================================================

The General Formal Ontology (GFO) is a top-level foundational ontology developed for conceptual modeling across scientific, technical, and philosophical domains [#gfo-github]_ [#gfo-paper]_. GFO provides a rigorous framework for representing fundamental categories such as objects, processes, time, space, properties, relations, roles, functions, facts, and situations [#gfo-github]_. It is designed to support the integration of material, mental, and social entities by incorporating the notion of levels of reality, enabling nuanced modeling of complex systems [#gfo-paper]_. GFO is modular and extensible, allowing domain ontologies to build upon its core categories for specialized applications [#gfo-github]_ [#gfo-paper]_. The ontology is used in knowledge engineering, biomedical informatics, cognitive science, and information systems to support semantic interoperability and logical consistency [#gfo-paper]_. GFO is maintained as an ontology resource through the Onto-Med GitHub repository and continues to support conceptual modeling and ontology integration work [#gfo-github]_.

**Example Usage**:
Use GFO as the upper ontology for a biomedical ontology, classifying entities such as ``disease`` as a situation, ``patient`` as an object, and ``treatment process`` as a process, enabling semantic integration and reasoning across clinical and research data [#gfo-github]_ [#gfo-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 296
        * - **Total Edges**
          - 708
        * - **Root Nodes**
          - 42
        * - **Leaf Nodes**
          - 71
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 94
        * - **Individuals**
          - 1
        * - **Properties**
          - 67

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 12
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.94
        * - **Depth Variance**
          - 3.22
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 88
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 21.23
        * - **Breadth Variance**
          - 874.02
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1
        * - **Taxonomic Relations**
          - 143
        * - **Non-taxonomic Relations**
          - 34
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GFO

    ontology = GFO()
    ontology.load("path/to/GFO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------
.. [#gfo-github] Onto-Med. n.d.
   "GFO: The General Formal Ontology."
   GitHub Repository.
   Available at:
   `https://github.com/Onto-Med/GFO <https://github.com/Onto-Med/GFO>`_

.. [#gfo-paper] Loebe, Frank, Patryk Burek, and Heinrich Herre. 2022.
   "GFO: The General Formal Ontology."
   *Applied Ontology*.
   DOI:
   `10.3233/AO-220264 <https://doi.org/10.3233/AO-220264>`_
