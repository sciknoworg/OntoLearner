

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry, Molecular Biology
       * - **Current Version**
         - 2022-05-11
       * - **Last Updated**
         - 2022-05-11
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Molecular Process Ontology (MOP) <https://terminology.tib.eu/ts/ontologies/MOP>`_

Molecular Process Ontology (MOP)
========================================================================================================

MOP is the molecular process ontology. It contains the molecular processes that underlie     the name reaction ontology RXNO, for example cyclization, methylation and demethylation.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 15794
        * - **Total Edges**
          - 41157
        * - **Root Nodes**
          - 3693
        * - **Leaf Nodes**
          - 8182
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3717
        * - **Individuals**
          - 0
        * - **Properties**
          - 11

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
          - 1.09
        * - **Depth Variance**
          - 0.63
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 7300
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 2253.14
        * - **Breadth Variance**
          - 7474153.55
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 3840
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MOP

    ontology = MOP()
    ontology.load("path/to/MOP-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
