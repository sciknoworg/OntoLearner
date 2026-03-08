

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Knowledge Graph
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2008-11-17
       * - **Creator**
         - DBpedia Maintainers and Contributors
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download DBpedia Ontology (DBpedia) <https://wiki.dbpedia.org/>`_

DBpedia Ontology (DBpedia)
========================================================================================================

The DBpedia ontology is generated from manually curated specifications in the DBpedia Mappings Wiki, providing a structured semantic model extracted from Wikipedia's rich content across multiple language editions. Each DBpedia release corresponds to a new Wikipedia data extraction, resulting in continuously evolving ontology versions that reflect growing knowledge representation in Wikipedia. The DBpedia ontology has become a shallow but comprehensive cross-domain ontology through crowd-sourced development involving thousands of contributors worldwide. It covers diverse knowledge domains including people, organizations, places, creative works, scientific concepts, and many others with relationships between them. DBpedia serves as a critical bridge between Wikipedia's unstructured information and the semantic web, enabling knowledge graph applications and linked data integration. The ontology is widely used in knowledge graph construction, information retrieval, entity linking, and semantic data integration projects leveraging Wikipedia's comprehensive and multilingual knowledge base.

**Example Usage**:
Query DBpedia to find relationships between entities (e.g., all people born in Berlin, all films directed by a specific director, companies in a particular industry) by using ontology classes (Person, Film, Company) and properties to enable advanced knowledge discovery and data analytics.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 18819
        * - **Total Edges**
          - 32745
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 14867
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 790
        * - **Individuals**
          - 0
        * - **Properties**
          - 3029

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
          - 2.61
        * - **Depth Variance**
          - 1.66
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 145
        * - **Minimum Breadth**
          - 12
        * - **Average Breadth**
          - 61.57
        * - **Breadth Variance**
          - 2369.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 799
        * - **Non-taxonomic Relations**
          - 1665
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DBpedia

    ontology = DBpedia()
    ontology.load("path/to/DBpedia-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
