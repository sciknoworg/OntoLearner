.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Social Network
       * - **Current Version**
         - 2.3
       * - **Last Updated**
         - 2013-05-24
       * - **Creator**
         - Bernard Vatant
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Vocabulary of a Friend (VOAF) <https://lov.linkeddata.es/vocommons/voaf/v2.3/>`_

Vocabulary of a Friend (VOAF)
========================================================================================================

The Vocabulary of a Friend (VOAF) is a vocabulary specification providing elements allowing the description of vocabularies (RDFS vocabularies or OWL ontologies). It is based on Dublin Core and VOID. VOAF provides a structured vocabulary for representing vocabularies, supporting both theoretical and experimental research in vocabulary management.

The ontology employs a class-based modeling approach, defining classes for different types of vocabularies, elements, and relationships, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. VOAF supports the integration of data from various sources, promoting interoperability and data-driven research in vocabulary management.

Typical applications of VOAF include the development of new vocabulary management methods, the optimization of vocabulary usage, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, VOAF enhances collaboration and innovation in the field of vocabulary management.

**Example Usage**:
Annotate a vocabulary with VOAF terms to specify vocabulary types, elements, and relationships, enabling semantic search and integration with vocabulary management platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 175
        * - **Total Edges**
          - 304
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 129
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3
        * - **Individuals**
          - 1
        * - **Properties**
          - 21

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 0
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.00
        * - **Depth Variance**
          - 0.00
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 0
        * - **Minimum Breadth**
          - 0
        * - **Average Breadth**
          - 0.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1
        * - **Taxonomic Relations**
          - 4
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import VOAF

    ontology = VOAF()
    ontology.load("path/to/VOAF-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
