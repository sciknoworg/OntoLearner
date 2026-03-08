.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Linguistics, Cognitive Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Laboratory for Applied Ontology, ISTC-CNR
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE) <https://www.loa.istc.cnr.it/index.php/dolce/>`_

Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE)
========================================================================================================

The Descriptive Ontology for Linguistic and Cognitive Engineering (DOLCE) is a foundational ontology that provides a conceptual framework for the formalization of domain ontologies. DOLCE is designed to capture the ontological categories underlying natural language and human common sense, supporting the modeling of linguistic, cognitive, and social phenomena. It distinguishes between endurants (entities persisting through time), perdurants (events and processes), qualities, and abstract entities, enabling nuanced representation of reality. DOLCE is widely used in linguistics, cognitive science, artificial intelligence, and knowledge engineering to support semantic interoperability and reasoning. Its modular structure allows for extensions and customization for specific domains, making it a popular choice for building interoperable ontologies. DOLCE has influenced the development of many domain ontologies and is recognized for its rigorous formal foundations and alignment with human conceptualization.

**Example Usage**:
Use DOLCE as the upper ontology for a linguistic ontology, classifying entities such as "utterance" (perdurant), "speaker" (endurant), and "meaning" (abstract), enabling semantic integration with other cognitive and linguistic resources.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 252
        * - **Total Edges**
          - 689
        * - **Root Nodes**
          - 10
        * - **Leaf Nodes**
          - 86
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 44
        * - **Individuals**
          - 0
        * - **Properties**
          - 70

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
          - 3.37
        * - **Depth Variance**
          - 4.11
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 28
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 14.20
        * - **Breadth Variance**
          - 75.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 73
        * - **Non-taxonomic Relations**
          - 18
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DOLCE

    ontology = DOLCE()
    ontology.load("path/to/DOLCE-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
