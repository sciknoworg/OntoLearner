

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Material Science and Engineering
       * - **Current Version**
         - 10.0
       * - **Last Updated**
         - 2025-02-17
       * - **Creator**
         - eNanoMapper Consortium
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Environmental Noise Measurement Ontology (ENM) <https://terminology.tib.eu/ts/ontologies/ENM>`_

Environmental Noise Measurement Ontology (ENM)
========================================================================================================

The eNanoMapper project (https://www.enanomapper.net/), NanoCommons project (https://www.nanocommons.eu/)     and ACEnano project (http://acenano-project.eu/) are creating a pan-European computational infrastructure     for toxicological data management for ENMs, based on semantic web standards and ontologies.     This ontology is an application ontology targeting the full domain of nanomaterial safety assessment.     It re-uses several other ontologies including the NPO, CHEMINF, ChEBI, and ENVO.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 102719
        * - **Total Edges**
          - 226566
        * - **Root Nodes**
          - 11156
        * - **Leaf Nodes**
          - 64025
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 26142
        * - **Individuals**
          - 9
        * - **Properties**
          - 53

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 130
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.74
        * - **Depth Variance**
          - 56.70
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 11156
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 206.70
        * - **Breadth Variance**
          - 1767707.90
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 9
        * - **Taxonomic Relations**
          - 36933
        * - **Non-taxonomic Relations**
          - 84
        * - **Average Terms per Type**
          - 3.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ENM

    ontology = ENM()
    ontology.load("path/to/ENM-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
