

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Bioinformatics
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 16 April 2015
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - owl
       * - **Download**
         - `Download Biological Pathways Exchange (BioPAX) <http://www.biopax.org/>`_

Biological Pathways Exchange (BioPAX)
========================================================================================================

BioPAX is a standard language that aims to enable integration, exchange, visualization and analysis     of biological pathway data. Specifically, BioPAX supports data exchange between pathway data     groups and thus reduces the complexity of interchange between data formats by providing an     accepted standard format for pathway data.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 555
        * - **Total Edges**
          - 1611
        * - **Root Nodes**
          - 68
        * - **Leaf Nodes**
          - 200
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 92
        * - **Individuals**
          - 0
        * - **Properties**
          - 96

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 15
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.70
        * - **Depth Variance**
          - 6.33
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 138
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 34.50
        * - **Breadth Variance**
          - 1919.38
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 126
        * - **Non-taxonomic Relations**
          - 446
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BioPAX

    ontology = BioPAX()
    ontology.load("path/to/BioPAX-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
