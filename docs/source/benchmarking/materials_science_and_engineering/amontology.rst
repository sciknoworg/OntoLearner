

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Manufacturing
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2023-05-10
       * - **Creator**
         - Iassou Souroko, Ali Riza Durmaz
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Additive Manufacturing Ontology (AMOntology) <https://github.com/iassouroko/AMontology>`_

Additive Manufacturing Ontology (AMOntology)
========================================================================================================

The AM ontology has been developed following two major milestones. The ontology developed within the first milestone     includes AMProcessOntology, ModelOntology and AMOntology files. AMProcessOntology contains the set of entities     used to capture knowledge about additive manufacturing processes. ModelOntology contains the set of entities     used to capture knowledge about modeling concepts that represent (possibly) multi-physics multi-scale processes.     AMOntology uses AMProcessOntology and ModelOntology files to describe entities that capture knowledge     about characteristics of computational models for AM processes.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 900
        * - **Total Edges**
          - 2299
        * - **Root Nodes**
          - 71
        * - **Leaf Nodes**
          - 99
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 328
        * - **Individuals**
          - 56
        * - **Properties**
          - 21

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 15
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.66
        * - **Depth Variance**
          - 11.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 116
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 55.50
        * - **Breadth Variance**
          - 1339.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 59
        * - **Taxonomic Relations**
          - 657
        * - **Non-taxonomic Relations**
          - 5
        * - **Average Terms per Type**
          - 1.26
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AMOntology

    ontology = AMOntology()
    ontology.load("path/to/AMOntology-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
