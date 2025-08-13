

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Human Diseases
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2024-12-18
       * - **Creator**
         - The Open Biological and Biomedical Ontology Foundry
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Human Disease Ontology (DOID) <http://purl.obolibrary.org/obo/doid/releases/2024-12-18/doid.owl>`_

Human Disease Ontology (DOID)
========================================================================================================

The Disease Ontology has been developed as a standardized ontology for human disease     with the purpose of providing the biomedical community with consistent,     reusable and sustainable descriptions of human disease terms,     phenotype characteristics and related medical vocabulary disease concepts.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 136876
        * - **Total Edges**
          - 288142
        * - **Root Nodes**
          - 14035
        * - **Leaf Nodes**
          - 95185
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 15343
        * - **Individuals**
          - 0
        * - **Properties**
          - 2

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 26
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.59
        * - **Depth Variance**
          - 1.07
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 61852
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 4291.67
        * - **Breadth Variance**
          - 172233228.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 41569
        * - **Non-taxonomic Relations**
          - 25
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DOID

    ontology = DOID()
    ontology.load("path/to/DOID-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
