.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.0.0
       * - **Last Updated**
         - 2022-12-12
       * - **Creator**
         - Tatyana Sheveleva, Javad Chamanara
       * - **License**
         - MIT License
       * - **Format**
         - rdf
       * - **Download**
         - `Download Materials Vocabulary (MatVoc) <https://stream-project.github.io/#overv>`_

Materials Vocabulary (MatVoc)
========================================================================================================

The Materials Vocabulary (MatVoc) is a vocabulary developed in the context of the STREAM project to provide structured terminology for representing materials-related knowledge [#matvoc-github]_. It supports the description of materials concepts in RDF/Turtle form and provides documentation and RDF files through the STREAM project resources [#matvoc-github]_.

MatVoc supports semantic annotation, retrieval, and integration of materials data, enabling interoperability and reuse across materials science workflows and related ontology-based applications [#matvoc-github]_. It is also used together with other vocabularies in materials-science ontology work, such as the Materials Science Laboratory Equipment ontology, where MatVoc contributes materials-related terminology [#msle2023]_.

**Example Usage**:
Annotate a materials database with MatVoc terms to specify materials-related concepts and properties, enabling semantic search, RDF-based integration, and reuse of materials information across materials informatics platforms [#matvoc-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 94
        * - **Total Edges**
          - 161
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 44
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 28
        * - **Individuals**
          - 0
        * - **Properties**
          - 15

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
          - 0.62
        * - **Depth Variance**
          - 0.48
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 16
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 10.67
        * - **Breadth Variance**
          - 24.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 6
        * - **Non-taxonomic Relations**
          - 7
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MatVoc

    ontology = MatVoc()
    ontology.load("path/to/MatVoc-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------
.. [#matvoc-github] STREAM Project. n.d.
   "Ontology."
   GitHub repository.
   Available at:
   `https://github.com/stream-project/ontology <https://github.com/stream-project/ontology>`_

.. [#msle2023] Jalali, M., et al. 2023.
   "An ontology for Materials Science Laboratory Equipment."
   arXiv:2308.07325.
   Available at:
   `https://arxiv.org/pdf/2308.07325 <https://arxiv.org/pdf/2308.07325>`_
