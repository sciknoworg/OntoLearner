

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Content Management Systems
       * - **Current Version**
         - 3.7
       * - **Last Updated**
         - 2012-12-01
       * - **Creator**
         - LinkedData@bbc.co.uk
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC CMS Ontology (BBCCMS) <https://www.bbc.co.uk/ontologies/cms-ontology>`_

BBC CMS Ontology (BBCCMS)
========================================================================================================

The BBC CMS Ontology is an ontology for representing content management systems and their interaction with the BBC Linked Data Platform [#bbccms-ontology]_. It defines how entities and creative works in the BBC triplestore are associated with external BBC content management systems that provide additional information about the same thing or content item [#bbccms-ontology]_.

The ontology provides terms for linking BBC concepts, web documents, creative works, and related CMS records, allowing the Linked Data Platform to point users and systems to information stored outside the triplestore [#bbccms-ontology]_. It supports content integration, semantic linking, retrieval, and management of relationships between BBC linked-data entities and the systems that produce or store content [#bbccms-ontology]_.

**Example Usage**:
Link a BBC entity such as **Manchester United** or a BBC creative work to an external content management system using BBC CMS Ontology terms, so that additional information such as sports statistics or the full body of a creative work can be retrieved from the relevant CMS [#bbccms-ontology]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 68
        * - **Total Edges**
          - 137
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 41
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 20
        * - **Individuals**
          - 4
        * - **Properties**
          - 2

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
          - 4
        * - **Taxonomic Relations**
          - 17
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 4.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCCMS

    ontology = BBCCMS()
    ontology.load("path/to/BBCCMS-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bbccms-ontology] BBC. 2012.
   "CMS Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/cms.html <https://iptc.org/thirdparty/bbc-ontologies/cms.html>`_
