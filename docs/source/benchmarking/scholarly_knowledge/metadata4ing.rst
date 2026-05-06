.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.3.1
       * - **Last Updated**
         - 2025-03-10
       * - **Creator**
         - Metadata4Ing Workgroup
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Metadata for Intelligent Engineering (Metadata4Ing) <https://git.rwth-aachen.de/nfdi4ing/metadata4ing/metadata4ing>`_

Metadata for Intelligent Engineering (Metadata4Ing)
========================================================================================================

The Metadata4Ing ontology provides a framework for the semantic description of research data and the complete data generation process, with a particular focus on engineering sciences and related disciplines [#m4i-nfdi]_. It covers the object of investigation, sample and data manipulation methods, tools, generated data files, and the roles of persons and institutions involved in the research process [#m4i-nfdi]_. Metadata4Ing supports the structured description of experiments, simulations, observations, workflows, and data-processing activities, enabling research data and its provenance context to be represented in a machine-readable form [#m4i-nfdi]_.

The ontology uses a class-based modeling approach to describe research data, methods, tools, projects, organizations, people, roles, variables, and generated outputs [#m4i-nfdi]_. These semantic descriptions support data retrieval, interpretation, comparison, reuse, and integration across engineering research datasets and infrastructures [#m4i-nfdi]_. Metadata4Ing is especially useful for research data management because it helps document not only the final dataset, but also how the data was created, processed, and contextualized [#m4i-nfdi]_.

Typical applications of Metadata4Ing include research data management, documentation of data generation workflows, semantic annotation of engineering datasets, FAIR data publication, provenance tracking, and knowledge graph construction for research processes [#m4i-nfdi]_. By providing a standardized vocabulary and framework, Metadata4Ing enhances interoperability, reproducibility, collaboration, and data-driven research in engineering and related scientific domains [#m4i-nfdi]_.

**Example Usage**:
Annotate an engineering research dataset with Metadata4Ing terms to specify the object of investigation, experimental or simulation method, tools used, generated data files, variables, responsible persons, institutional roles, and related project context. This enables semantic search, reproducibility, provenance tracking, and integration with research data management platforms [#m4i-nfdi]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1032
        * - **Total Edges**
          - 1517
        * - **Root Nodes**
          - 109
        * - **Leaf Nodes**
          - 731
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 48
        * - **Individuals**
          - 47
        * - **Properties**
          - 100

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.54
        * - **Depth Variance**
          - 1.36
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 413
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 109.75
        * - **Breadth Variance**
          - 18099.19
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 37
        * - **Taxonomic Relations**
          - 44
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 9.25
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Metadata4Ing

    ontology = Metadata4Ing()
    ontology.load("path/to/Metadata4Ing-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#m4i-nfdi] NFDI4Ing. n.d.
   "Metadata4Ing."
   Available at:
   `https://nfdi4ing.de/m4i/ <https://nfdi4ing.de/m4i/>`_
