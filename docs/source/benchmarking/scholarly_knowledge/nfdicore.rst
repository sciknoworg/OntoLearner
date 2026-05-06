.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Research Data Infrastructure
       * - **Current Version**
         - 3.0.0
       * - **Last Updated**
         - 2025-02-07
       * - **Creator**
         - Jörg Waitelonis, Oleksandra Bruns, Tabea Tietz, Etienne Posthumus, Hossein Beygi Nasrabadi, Harald Sack
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download National Research Data Infrastructure Ontology (NFDIcore) <https://ise-fizkarlsruhe.github.io/nfdicore/>`_

National Research Data Infrastructure Ontology (NFDIcore)
========================================================================================================

The NFDIcore ontology is a mid-level ontology developed to support interoperability across the consortia of the National Research Data Infrastructure (NFDI) [#nfdicore-docs]_ [#nfdicore-github]_. It represents metadata related to NFDI resources, including individuals, organizations, projects, data portals, datasets, services, and other research infrastructure entities [#nfdicore-github]_. NFDIcore helps provide a shared semantic structure for describing the organization of NFDI and the research data resources made available by its project partners [#nfdicore-docs]_.

The ontology uses a class-based modeling approach to define reusable concepts and relations for research data infrastructure, metadata, organizations, projects, persons, services, repositories, and related resources [#nfdicore-docs]_. As a mid-level ontology, it bridges general upper-level concepts with more specific domain ontologies, supporting both flexibility and consistency across different NFDI consortia [#nfdicore-docs]_. This enables heterogeneous research data infrastructure metadata to be described, linked, queried, and integrated in a machine-readable form [#nfdicore-github]_.

Typical applications of NFDIcore include research data infrastructure documentation, metadata integration, semantic annotation of NFDI resources, data portal description, project and organization modeling, knowledge graph construction, and cross-consortium interoperability [#nfdicore-docs]_ [#nfdicore-github]_. By providing a standardized semantic framework, NFDIcore supports data discovery, integration, collaboration, and knowledge sharing across research data management platforms [#nfdicore-docs]_.

**Example Usage**:
Annotate an NFDI research data infrastructure project with NFDIcore terms to describe participating organizations, researchers, projects, datasets, data portals, services, software repositories, and related metadata. This enables semantic search, cross-consortium integration, and interoperability with research data management platforms [#nfdicore-docs]_ [#nfdicore-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1849
        * - **Total Edges**
          - 3525
        * - **Root Nodes**
          - 84
        * - **Leaf Nodes**
          - 1029
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 302
        * - **Individuals**
          - 0
        * - **Properties**
          - 102

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.85
        * - **Depth Variance**
          - 5.97
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 145
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 39.29
        * - **Breadth Variance**
          - 1732.49
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 237
        * - **Non-taxonomic Relations**
          - 10
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import NFDIcore

    ontology = NFDIcore()
    ontology.load("path/to/NFDIcore-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#nfdicore-docs] FIZ Karlsruhe. n.d.
   "NFDIcore Ontology."
   Available at:
   `https://ise-fizkarlsruhe.github.io/nfdicore/ <https://ise-fizkarlsruhe.github.io/nfdicore/>`_

.. [#nfdicore-github] ISE-FIZKarlsruhe. n.d.
   "NFDI Core Ontology."
   GitHub Repository.
   Available at:
   `https://github.com/ISE-FIZKarlsruhe/nfdicore <https://github.com/ISE-FIZKarlsruhe/nfdicore>`_
