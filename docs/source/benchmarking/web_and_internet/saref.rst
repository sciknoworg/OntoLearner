

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Web and Internet
       * - **Category**
         - interoperability
       * - **Current Version**
         - 3.2.1
       * - **Last Updated**
         - 2020-12-31
       * - **Creator**
         - ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M)
       * - **License**
         - None
       * - **Format**
         - rdf
       * - **Download**
         - `Download Smart Applications REFerence ontology (SAREF) <https://saref.etsi.org/core/v3.2.1/>`_

Smart Applications REFerence ontology (SAREF)
========================================================================================================

The Smart Applications REFerence (SAREF) suite of ontologies forms a shared model of consensus     intended to enable semantic interoperability between solutions from different providers     and among various activity sectors in the Internet of Things (IoT),     thus contributing to the development of data spaces. SAREF is published as a set of open standards     produced by ETSI Technical Committee Smart Machine-to-Machine communications (SmartM2M).

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 804
        * - **Total Edges**
          - 1720
        * - **Root Nodes**
          - 14
        * - **Leaf Nodes**
          - 376
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 129
        * - **Individuals**
          - 10
        * - **Properties**
          - 89

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.07
        * - **Depth Variance**
          - 0.06
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 7.50
        * - **Breadth Variance**
          - 42.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 10
        * - **Taxonomic Relations**
          - 88
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 10.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SAREF

    ontology = SAREF()
    ontology.load("path/to/SAREF-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
