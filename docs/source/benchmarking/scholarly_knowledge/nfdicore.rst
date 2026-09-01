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

The NFDIcore ontology is a mid-level ontology developed to support semantic interoperability across the consortia of the German National Research Data Infrastructure (NFDI) [#nfdicore-docs]_ [#nfdicore-paper]_. It provides a shared semantic model for describing research infrastructure entities such as persons, organizations, projects, datasets, data portals, services, repositories, and related resources [#nfdicore-docs]_ [#nfdicore-paper]_.

NFDIcore is designed to bridge general concepts with more domain-specific models, allowing heterogeneous metadata from different NFDI consortia to be represented in a consistent and machine-readable form [#nfdicore-paper]_. Its classes and relations support the description of organizational structures, research activities, digital resources, services, and the relationships between them [#nfdicore-docs]_. This shared modeling layer enables metadata from different research data infrastructures to be linked, integrated, and queried across consortium boundaries [#nfdicore-paper]_.

Typical applications of NFDIcore include metadata integration, documentation of research infrastructures, semantic annotation of NFDI resources, modeling of projects and organizations, knowledge graph construction, and cross-consortium interoperability [#nfdicore-docs]_ [#nfdicore-paper]_. By providing a common semantic framework, NFDIcore supports more consistent representation, discovery, and integration of research infrastructure metadata within the NFDI ecosystem [#nfdicore-paper]_.

**Example Usage**:
Annotate an NFDI research infrastructure with NFDIcore terms to describe participating organizations, researchers, projects, datasets, repositories, data portals, services, and their relationships. This enables metadata from different NFDI consortia to be represented in a shared semantic structure and supports cross-consortium discovery and integration [#nfdicore-docs]_ [#nfdicore-paper]_.

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
   `https://ise-fizkarlsruhe.github.io/nfdicore/
   <https://ise-fizkarlsruhe.github.io/nfdicore/>`_

.. [#nfdicore-paper] Bruns, O., Tietz, T., Waitelonis, J.,
   Posthumus, E., and Sack, H. 2024.
   "NFDIcore 2.0: A BFO-Compliant Ontology for
   Multi-Domain Research Infrastructures."
   arXiv:2410.01821.
   `doi:10.48550/arXiv.2410.01821 <https://doi.org/10.48550/arXiv.2410.01821>`_
