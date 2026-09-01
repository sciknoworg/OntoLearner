.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Microscopy
       * - **Current Version**
         - 2.0
       * - **Last Updated**
         - None
       * - **Creator**
         - https://orcid.org/0000-0002-3717-7104,https://orcid.org/0000-0002-7094-5371
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Microscopy Ontology (MO) <https://github.com/materialdigital/microscopy-ontology?tab=readme-ov-file>`_

Microscopy Ontology (MO)
========================================================================================================

The Microscopy Ontology (MO) is a domain ontology developed to provide a
structured framework for describing microscopy and microanalysis
experiments, data, and equipment [#mo-paper]_ [#mo-repo]_. It was
developed within the Platform MaterialDigital ecosystem to support
semantic integration and interoperability of microscopy data
[#mo-paper]_ [#mo-repo]_. The ontology covers microscopy-specific
concepts and relationships needed to describe processes, equipment, and
parameters in microscopy and microanalysis workflows [#mo-paper]_
[#mo-repo]_. MO is intended to improve the semantic representation of
microscopy knowledge and support better query results and logical
linking among related terms and data objects [#mo-paper]_ [#mo-repo]_.
By providing a standardized vocabulary for microscopy data, the
ontology supports interoperable data description and integration across
materials-science microscopy datasets and related digital research
infrastructures [#mo-paper]_ [#mo-repo]_.

**Example Usage**: Annotate a microscopy dataset with MO terms to
specify the imaging modality, for example scanning electron microscopy
or transmission electron microscopy, relevant equipment and parameters,
sample-related descriptors, and analysis-related concepts, enabling
semantic search, interoperable data integration, and improved querying
across microscopy data sources [#mo-paper]_ [#mo-repo]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 931
        * - **Total Edges**
          - 1776
        * - **Root Nodes**
          - 10
        * - **Leaf Nodes**
          - 693
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 217
        * - **Individuals**
          - 0
        * - **Properties**
          - 3

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
          - 0.09
        * - **Depth Variance**
          - 0.08
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 10
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 5.50
        * - **Breadth Variance**
          - 20.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 130
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MO

    ontology = MO()
    ontology.load("path/to/MO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#mo-paper] Bayerlein, B., Schilling, M., Curran, M., and Lau, J. W.
   2024. "Natural Language Processing-Driven Microscopy Ontology
   Development."
   *Integrating Materials and Manufacturing Innovation*.
   doi:10.1007/s40192-024-00378-y

.. [#mo-repo] materialdigital. n.d. "Microscopy Ontology (MO)."
   GitHub repository.
   Available at: `https://github.com/materialdigital/microscopy-ontology <https://github.com/materialdigital/microscopy-ontology>`_
