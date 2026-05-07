

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

The DBpedia ontology is generated from manually curated specifications
in the DBpedia Mappings Wiki, providing a structured semantic model
extracted from Wikipedia's rich content across multiple language
editions [#dbpedia-ontology]_ [#dbpedia-paper]_. Each DBpedia release
corresponds to a new Wikipedia data extraction, resulting in evolving
ontology versions that reflect changes and growth in Wikipedia-based
knowledge representation [#dbpedia-ontology]_.

The DBpedia ontology is a shallow but comprehensive cross-domain
ontology developed through community-based mapping and curation
activities [#dbpedia-ontology]_ [#dbpedia-paper]_. It covers diverse
knowledge domains including people, organizations, places, creative
works, scientific concepts, events, and many other entity types, together
with properties that describe relationships between them
[#dbpedia-ontology]_.

DBpedia serves as a bridge between Wikipedia's semi-structured
information and the Semantic Web, enabling linked data publication,
knowledge graph construction, information retrieval, entity linking, and
semantic data integration [#dbpedia-paper]_. Its ontology and mappings
allow Wikipedia-derived information to be represented in RDF and queried
using semantic technologies such as SPARQL [#dbpedia-paper]_.

**Example Usage**: Query DBpedia to find relationships between entities,
such as all people born in Berlin, all films directed by a specific
director, or companies in a particular industry, by using ontology
classes such as Person, Film, and Company together with ontology
properties that support structured knowledge discovery and data
analytics [#dbpedia-ontology]_ [#dbpedia-paper]_.

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

References
---------------

.. [#dbpedia-ontology] DBpedia Association. n.d.
   "DBpedia Ontology."
   Available at:
   `https://www.dbpedia.org/resources/ontology/ <https://www.dbpedia.org/resources/ontology/>`_

.. [#dbpedia-paper] Lehmann, J., Isele, R., Jakob, M., Jentzsch, A.,
   Kontokostas, D., Mendes, P. N., Hellmann, S., Morsey, M.,
   van Kleef, P., Auer, S., and Bizer, C. 2015.
   "DBpedia: A Large-scale, Multilingual Knowledge Base Extracted
   from Wikipedia."
   Semantic Web 6(2): 167-195.
   Available at:
   `https://jens-lehmann.org/files/2015/swj_dbpedia.pdf <https://jens-lehmann.org/files/2015/swj_dbpedia.pdf>`_
