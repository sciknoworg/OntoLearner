

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Linguistics
       * - **Current Version**
         - 3.0
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - Apache 2.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download LexInfo (LexInfo) <https://lexinfo.net/index.html>`_

LexInfo (LexInfo)
========================================================================================================

LexInfo allows us to associate linguistic information to elements in an ontology with respect     to any level of linguistic description and expressivity. LexInfo has been implemented as an OWL ontology     and is available together with an API.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 3351
        * - **Total Edges**
          - 5435
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 2308
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 334
        * - **Individuals**
          - 276
        * - **Properties**
          - 189

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
          - 0.50
        * - **Depth Variance**
          - 0.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 1
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 288
        * - **Taxonomic Relations**
          - 276
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 11.08
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import LexInfo

    ontology = LexInfo()
    ontology.load("path/to/LexInfo-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
