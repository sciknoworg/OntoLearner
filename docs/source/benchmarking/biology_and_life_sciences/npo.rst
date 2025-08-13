

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 2013-05-31
       * - **Last Updated**
         - 2013-05-31
       * - **Creator**
         - Dennis G. Thomas
       * - **License**
         - BSD-3-Clause license
       * - **Format**
         - owl
       * - **Download**
         - `Download NanoParticle Ontology (NPO) <https://github.com/sobolevnrm/npo?tab=readme-ov-file>`_

NanoParticle Ontology (NPO)
========================================================================================================

NanoParticle Ontology (NPO) is developed within the framework of the Basic Formal Ontology (BFO),     and implemented in the Ontology Web Language (OWL) using well-defined ontology design principles.     The NPO was developed to represent knowledge underlying the preparation, chemical composition,     and characterization of nanomaterials involved in cancer research. Public releases of the NPO     are available through BioPortal website, maintained by the National Center for Biomedical Ontology.     Mechanisms for editorial and governance processes are being developed for the maintenance,     review, and growth of the NPO.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 9976
        * - **Total Edges**
          - 36031
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 4344
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 2464
        * - **Individuals**
          - 0
        * - **Properties**
          - 87

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 10
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.26
        * - **Depth Variance**
          - 7.37
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 35
        * - **Minimum Breadth**
          - 7
        * - **Average Breadth**
          - 21.82
        * - **Breadth Variance**
          - 106.88
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 2724
        * - **Non-taxonomic Relations**
          - 12277
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import NPO

    ontology = NPO()
    ontology.load("path/to/NPO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
