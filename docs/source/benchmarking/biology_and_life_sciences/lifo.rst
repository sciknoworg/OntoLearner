.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - General Purpose
       * - **Current Version**
         - 1.0.17
       * - **Last Updated**
         - March 11, 2018
       * - **Creator**
         - Yongqun "Oliver" He (YH)
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Life Ontology (LifO) <https://bioportal.bioontology.org/ontologies/LIFO>`_

Life Ontology (LifO)
========================================================================================================

The Life Ontology (LifO) is a general-purpose ontology designed to
represent the life processes of organisms and their associated entities
and relationships. It provides a structured framework for describing
common biological features across diverse organisms, including
unicellular prokaryotes such as *E. coli* and multicellular organisms
such as humans [#lifo-github]_ [#lifo-bioportal]_. LifO represents life
processes of organisms together with related entities and relations,
providing a common vocabulary for modelling biological phenomena in a
standardized way [#lifo-github]_ [#lifo-bioportal]_. The ontology is
intended as a broad life-science resource that can support interoperable
description of organism-level biological knowledge across different
systems and datasets [#lifo-github]_ [#lifo-bioportal]_. By providing a
shared framework for representing biological processes and related
entities, LifO can support comparative studies, knowledge organization,
and bioinformatics applications that benefit from a common semantic
structure [#lifo-github]_.

**Example Usage**: Use LifO to annotate a dataset describing organismal
life processes or related biological entities. For example, linking
metabolic or reproductive processes in *E. coli* or human-related
datasets to standardized ontology terms to support consistent
description, comparison, and integration across biological datasets
[#lifo-github]_ [#lifo-bioportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2140
        * - **Total Edges**
          - 4179
        * - **Root Nodes**
          - 43
        * - **Leaf Nodes**
          - 1522
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 239
        * - **Individuals**
          - 9
        * - **Properties**
          - 98

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.18
        * - **Depth Variance**
          - 0.83
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 65
        * - **Minimum Breadth**
          - 17
        * - **Average Breadth**
          - 41.67
        * - **Breadth Variance**
          - 384.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 9
        * - **Taxonomic Relations**
          - 321
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 9.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import LIFO

    ontology = LIFO()
    ontology.load("path/to/LIFO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#lifo-github] He, Y. 2018. "LifO: An Ontology of the Life of Organism."
   GitHub repository.
   Available at: `https://github.com/lifeontology/lifo <https://github.com/lifeontology/lifo>`_

.. [#lifo-bioportal] NCBO BioPortal. n.d. "Life Ontology (LIFO)."
   Available at: `https://bioportal.bioontology.org/ontologies/LIFO <https://bioportal.bioontology.org/ontologies/LIFO>`_
