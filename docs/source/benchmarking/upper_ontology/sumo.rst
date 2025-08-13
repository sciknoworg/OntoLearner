

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Upper Ontology
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2025-02-17
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Suggested Upper Merged Ontology (SUMO) <https://www.ontologyportal.org/>`_

Suggested Upper Merged Ontology (SUMO)
========================================================================================================

The Suggested Upper Merged Ontology (SUMO) and its domain ontologies form the largest formal public ontology     in existence today. They are being used for research and applications in search, linguistics and reasoning.     SUMO is the only formal ontology that has been mapped to all of the WordNet lexicon.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 288016
        * - **Total Edges**
          - 496645
        * - **Root Nodes**
          - 77015
        * - **Leaf Nodes**
          - 197102
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 4525
        * - **Individuals**
          - 80034
        * - **Properties**
          - 587

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 9
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.04
        * - **Depth Variance**
          - 1.39
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 77015
        * - **Minimum Breadth**
          - 10
        * - **Average Breadth**
          - 19045.20
        * - **Breadth Variance**
          - 739917637.16
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 80280
        * - **Taxonomic Relations**
          - 7174
        * - **Non-taxonomic Relations**
          - 310
        * - **Average Terms per Type**
          - 165.53
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SUMO

    ontology = SUMO()
    ontology.load("path/to/SUMO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
