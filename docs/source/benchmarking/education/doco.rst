

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Education
       * - **Category**
         - document components
       * - **Current Version**
         - 1.3
       * - **Last Updated**
         - 2015-07-03
       * - **Creator**
         - David Shotton and Silvio Peroni
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Document Components Ontology (DoCO) <http://www.sparontologies.net/ontologies/doco>`_

Document Components Ontology (DoCO)
========================================================================================================

DoCO, the Document Components Ontology, is an OWL 2 DL ontology that provides a general-purpose structured vocabulary     of document elements. DoCO has been designed as a general unifying ontological framework for describing different aspects     related to the content of scientific and other scholarly texts. Its primary goal has been to improve the interoperability     and shareability of academic documents (and related services) when multiple formats are actually used for their storage.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 442
        * - **Total Edges**
          - 922
        * - **Root Nodes**
          - 12
        * - **Leaf Nodes**
          - 73
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 137
        * - **Individuals**
          - 0
        * - **Properties**
          - 7

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 25
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 8.29
        * - **Depth Variance**
          - 25.91
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 35
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 14.54
        * - **Breadth Variance**
          - 110.71
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 59
        * - **Non-taxonomic Relations**
          - 7
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DoCO

    ontology = DoCO()
    ontology.load("path/to/DoCO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
