.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Linguistics
       * - **Current Version**
         - 2018a
       * - **Last Updated**
         - 2018-02-15
       * - **Creator**
         - Francesco Corcoglioniti, Marco Rospocher <https://dkm.fbk.eu/rospocher>
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Pre-Modern Ontology (PreMOn) <https://premon.fbk.eu/ontology/core#>`_

Pre-Modern Ontology (PreMOn)
========================================================================================================

The Pre-Modern Ontology (PreMOn) is an extension of lemon (W3C Ontology Lexicon Community Group, 2015) for representing predicate models and their mappings. The Core Module of the PreMOn Ontology defines the main abstractions for modelling semantic classes with their semantic roles, mappings between different predicate models, and annotations. It provides a structured vocabulary for representing predicate models, supporting both theoretical and experimental research in linguistics.

The ontology employs a class-based modeling approach, defining classes for different types of predicate models, semantic roles, and annotations, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. PreMOn supports the integration of data from various sources, promoting interoperability and data-driven research in linguistics.

Typical applications of PreMOn include the development of new predicate model representation methods, the optimization of linguistic data management practices, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, PreMOn enhances collaboration and innovation in the field of linguistics.

**Example Usage**:
Annotate a linguistic dataset with PreMOn terms to specify predicate models, semantic roles, and annotations, enabling semantic search and integration with linguistic information management platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 115
        * - **Total Edges**
          - 213
        * - **Root Nodes**
          - 13
        * - **Leaf Nodes**
          - 45
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 15
        * - **Individuals**
          - 0
        * - **Properties**
          - 16

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
          - 1.80
        * - **Depth Variance**
          - 3.33
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 20
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 7.29
        * - **Breadth Variance**
          - 38.49
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 17
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PreMOn

    ontology = PreMOn()
    ontology.load("path/to/PreMOn-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
