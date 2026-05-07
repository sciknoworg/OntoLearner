

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Provenance
       * - **Current Version**
         - 1.9
       * - **Last Updated**
         - 2012-12-01
       * - **Creator**
         - LinkedData@bbc.co.uk
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Provenance News Ontology (BBCProvenance) <https://www.bbc.co.uk/ontologies/provenance-ontology>`_

BBC Provenance News Ontology (BBCProvenance)
========================================================================================================

The BBC Provenance News Ontology is a vocabulary for capturing provenance metadata about data in the BBC RDF triple store [#bbcprovenance-ontology]_. It supports data management and auditing tasks by defining types of named graphs used in the BBC quad store and associating them with metadata for managing, validating, and exposing data to BBC services [#bbcprovenance-ontology]_.

The ontology focuses on recording the immediate provider of data rather than the ultimate source; for example, it can record that geodata was provided by the BBC Locator team rather than by the original external source [#bbcprovenance-ontology]_. In the BBC Linked Data Platform, this provenance information is applied to contexts or named graphs, where the named graph acts as a fourth part of an RDF triple, forming a quad store [#bbcprovenance-ontology]_.

**Example Usage**:
Annotate geodata in a named graph with BBC Provenance terms to indicate that the data was provided by the BBC Locator team, enabling attribution, validation, auditing, and management of provenance metadata in BBC linked-data systems [#bbcprovenance-ontology]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 74
        * - **Total Edges**
          - 151
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 48
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 7
        * - **Individuals**
          - 1
        * - **Properties**
          - 18

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
          - 6
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCProvenance

    ontology = BBCProvenance()
    ontology.load("path/to/BBCProvenance-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bbcprovenance-ontology] BBC. 2012.
   "Provenance Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/provenance.html <https://iptc.org/thirdparty/bbc-ontologies/provenance.html>`_
