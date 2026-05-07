.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2021-12-16
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Reaction Ontology (RXNO) <https://github.com/rsc-ontologies/rxno>`_

Reaction Ontology (RXNO)
========================================================================================================

The Reaction Ontology (RXNO) is a specialized ontology that provides a
comprehensive vocabulary for representing organic chemical reactions
[#rxno-obo]_ [#rxno-repo]_. It includes classes that describe named
reactions, such as the Diels–Alder cyclization, and their associated
roles in organic synthesis [#rxno-obo]_ [#rxno-repo]_. RXNO enables the
semantic annotation of chemical reaction data, facilitating data
sharing, integration, and advanced querying in cheminformatics and
organic chemistry research [#rxno-obo]_ [#rxno-repo]_. By standardizing
the representation of chemical reactions, RXNO supports the development
of reaction databases, computational chemistry tools, and automated
synthesis planning systems [#rxno-obo]_ [#rxno-repo]_. The ontology
also captures relationships between reactions and related molecular
processes, enabling more detailed modeling of reaction knowledge
[#rxno-obo]_ [#rxno-repo]_.

**Example Usage**: Annotate a reaction database with RXNO terms to
specify reaction types, such as a Diels–Alder reaction, and link these
reactions to related reaction information to support semantic search,
integration, and comparison across chemical reaction datasets
[#rxno-obo]_ [#rxno-repo]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 5676
        * - **Total Edges**
          - 14841
        * - **Root Nodes**
          - 845
        * - **Leaf Nodes**
          - 2924
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1109
        * - **Individuals**
          - 0
        * - **Properties**
          - 14

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
          - 1.71
        * - **Depth Variance**
          - 1.67
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 2230
        * - **Minimum Breadth**
          - 12
        * - **Average Breadth**
          - 623.00
        * - **Breadth Variance**
          - 588146.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 1990
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import RXNO

    ontology = RXNO()
    ontology.load("path/to/RXNO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#rxno-obo] OBO Foundry. n.d. "Name Reaction Ontology."
   Available at: `https://obofoundry.org/ontology/rxno.html <https://obofoundry.org/ontology/rxno.html>`_

.. [#rxno-repo] Royal Society of Chemistry. n.d. "RXNO: reaction ontologies."
   Available at: `https://github.com/rsc-ontology/rxno <https://github.com/rsc-ontology/rxno>`_
