

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Units and Measurements
       * - **Category**
         - Units and Measurements
       * - **Current Version**
         - 2009-10-30
       * - **Last Updated**
         - 2009-10-30
       * - **Creator**
         - SysML
       * - **License**
         - Apache License 2.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Quantities, Units, Dimensions and Values (QUDV) <https://www.omgwiki.org/OMGSysML/doku.php?id=sysml-qudv:qudv_owl>`_

Quantities, Units, Dimensions and Values (QUDV)
========================================================================================================

The SysML QUDV (Quantities, Units, Dimensions and Values) modelLibrary is specified in a UML/SysML     class/block diagram. In order to generalize its potential usage and alignment with other standardization efforts     concerning quantities and units, it is of interest to verify that the QUDV model can also be represented     in the form of an ontology using a formal ontology definition language.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 186
        * - **Total Edges**
          - 491
        * - **Root Nodes**
          - 4
        * - **Leaf Nodes**
          - 20
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 33
        * - **Individuals**
          - 0
        * - **Properties**
          - 25

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 21
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 8.44
        * - **Depth Variance**
          - 24.45
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 17
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 8.00
        * - **Breadth Variance**
          - 22.18
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 9
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import QUDV

    ontology = QUDV()
    ontology.load("path/to/QUDV-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
