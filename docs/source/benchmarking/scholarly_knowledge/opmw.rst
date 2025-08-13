

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Workflows
       * - **Current Version**
         - 3.1
       * - **Last Updated**
         - 2014-12-22
       * - **Creator**
         - http://delicias.dia.fi.upm.es/members/DGarijo/#me, http://www.isi.edu/~gil/
       * - **License**
         - Creative Commons Attribution 2.0 Generic (CC BY 2.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Open Provenance Model for Workflows (OPMW) <https://www.opmw.org/model/OPMW_20141222/>`_

Open Provenance Model for Workflows (OPMW)
========================================================================================================

The Open Provenance Model for Workflows (OPMW) is an ontology for describing workflow traces     and their templates based on the Open Provenance Model. It has been designed as a profile for OPM,     extending and reusing OPM's core ontologies OPMV (OPM-Vocabulary) and OPMO (OPM-Ontology).

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 539
        * - **Total Edges**
          - 1387
        * - **Root Nodes**
          - 33
        * - **Leaf Nodes**
          - 306
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 59
        * - **Individuals**
          - 2
        * - **Properties**
          - 87

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
          - 2.14
        * - **Depth Variance**
          - 2.07
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 59
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 31.57
        * - **Breadth Variance**
          - 405.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 77
        * - **Non-taxonomic Relations**
          - 4
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OPMW

    ontology = OPMW()
    ontology.load("path/to/OPMW-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
