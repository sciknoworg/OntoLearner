

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Software
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2013-07-01
       * - **Creator**
         - Allyson Lister, Andy Brown, Duncan Hull, Helen Parkinson, James Malone, Jon Ison, Nandini Badarinarayan, Robert Stevens
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Software Ontology (SWO) <https://terminology.tib.eu/ts/ontologies/SWO>`_

Software Ontology (SWO)
========================================================================================================

The Software Ontology (SWO) is a resource for describing software tools, their types, tasks, versions,     provenance and associated data. It contains detailed information on licensing and formats     as well as software applications themselves, mainly (but not limited) to the bioinformatics community.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 11581
        * - **Total Edges**
          - 33570
        * - **Root Nodes**
          - 177
        * - **Leaf Nodes**
          - 3150
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 2746
        * - **Individuals**
          - 443
        * - **Properties**
          - 165

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.07
        * - **Depth Variance**
          - 5.30
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 392
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 132.93
        * - **Breadth Variance**
          - 17222.21
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 440
        * - **Taxonomic Relations**
          - 5852
        * - **Non-taxonomic Relations**
          - 612
        * - **Average Terms per Type**
          - 8.30
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SWO

    ontology = SWO()
    ontology.load("path/to/SWO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
