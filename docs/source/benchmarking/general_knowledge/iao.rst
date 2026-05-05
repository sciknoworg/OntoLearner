

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Information, Data, Knowledge
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2022-11-07
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Information Artifact Ontology (IAO) <https://terminology.tib.eu/ts/ontologies/IAO>`_

Information Artifact Ontology (IAO)
========================================================================================================

The Information Artifact Ontology (IAO) is an ontology for representing
information entities, information artifacts, and related information
objects in a formal and semantically precise way [#iao-repo]_
[#iao-paper]_. It provides structured concepts for describing entities
such as documents, data items, information content entities, identifiers,
and other representational artifacts [#iao-repo]_.

IAO helps distinguish between information content and the concrete
artifacts or realizations through which that content is represented,
stored, transmitted, or used [#iao-paper]_. This makes it useful for
modeling relationships between data collections, documents, databases,
records, and the real-world entities or phenomena that they are about
[#iao-paper]_.

The ontology is widely used in biomedical informatics, scientific data
management, ontology annotation, and linked data applications where
information resources need formal semantic types [#iao-repo]_
[#iao-paper]_. It supports the annotation of publications, datasets,
measurement results, protocols, databases, licenses, and other
information-bearing resources in a consistent ontology-based framework
[#iao-repo]_.

**Example Usage**: Annotate a scientific publication with IAO terms such
as document, data item, information content entity, and is about
relations. This can represent the publication as an information artifact,
connect it to its authorship or metadata, and link its content to the
scientific claims, datasets, or real-world entities described in the
publication [#iao-repo]_ [#iao-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2303
        * - **Total Edges**
          - 4720
        * - **Root Nodes**
          - 151
        * - **Leaf Nodes**
          - 1523
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 292
        * - **Individuals**
          - 18
        * - **Properties**
          - 57

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
          - 2.05
        * - **Depth Variance**
          - 4.06
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 280
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 63.00
        * - **Breadth Variance**
          - 8210.29
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 18
        * - **Taxonomic Relations**
          - 347
        * - **Non-taxonomic Relations**
          - 19
        * - **Average Terms per Type**
          - 6.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import IAO

    ontology = IAO()
    ontology.load("path/to/IAO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#iao-repo] Information Artifact Ontology. n.d.
   "Information Artifact Ontology."
   GitHub Repository.
   Available at:
   `https://github.com/information-artifact-ontology/IAO <https://github.com/information-artifact-ontology/IAO>`_

.. [#iao-paper] Ceusters, W. 2012.
   "An Information Artifact Ontology Perspective on Data Collections
   and Associated Representational Artifacts."
   *Studies in Health Technology and Informatics* 180: 68--72.
   Available at:
   `https://pubmed.ncbi.nlm.nih.gov/22874154/ <https://pubmed.ncbi.nlm.nih.gov/22874154/>`_
