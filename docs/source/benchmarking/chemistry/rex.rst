

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2025-03-11
       * - **Creator**
         - University of Warsaw
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Physico-chemical process ontology (REX) <https://terminology.tib.eu/ts/ontologies/REX>`_

Physico-chemical process ontology (REX)
========================================================================================================

REX is a comprehensive ontology for formal representation of physico-chemical processes, including both microscopic molecular transformations and macroscopic chemical phenomena occurring over time. It provides structured vocabulary for describing processes at different scales: molecular-level processes (involving chemical bonds, molecular rearrangement, electron transfer) and macroscopic processes (phase changes, dissolution, crystallization). REX distinguishes between different process types and captures temporal and causal relationships between processes, enabling precise semantic representation of chemical transformations. The ontology integrates with biological process vocabularies (e.g., Gene Ontology's biological process namespace) to bridge molecular biochemistry and cellular processes. REX facilitates knowledge integration in chemistry databases, computational chemistry platforms, and systems biology models by providing standardized process definitions.

**Example Usage**: Represent a multi-step chemical transformation process using REX terms to describe molecular-level processes (e.g., nucleophilic substitution, oxidation) linked together in sequence, with temporal ordering and causal dependencies between elementary steps.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2461
        * - **Total Edges**
          - 5630
        * - **Root Nodes**
          - 356
        * - **Leaf Nodes**
          - 1457
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 552
        * - **Individuals**
          - 0
        * - **Properties**
          - 6

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.35
        * - **Depth Variance**
          - 0.97
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 978
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 304.57
        * - **Breadth Variance**
          - 116930.53
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 953
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import REX

    ontology = REX()
    ontology.load("path/to/REX-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
