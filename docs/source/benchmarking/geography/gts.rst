

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Geography
       * - **Category**
         - geospatial Information, Geology
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2020-05-31
       * - **Creator**
         - Simon J D Cox (simon.cox@csiro.au) of CSIRO
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Geologic Timescale model (GTS) <https://raw.githack.com/CGI-IUGS/timescale-ont/master/html/gts.html>`_

Geologic Timescale model (GTS)
========================================================================================================

This is an RDF/OWL representation of the GeoSciML Geologic Timescale model, which has been adapted     from the model described in Cox, S.J.D, & Richard, S.M. (2005) A formal model for the geologic timescale and GSSP,     compatible with geospatial information transfer standards, Geosphere, Geological Society of America.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 311
        * - **Total Edges**
          - 743
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 92
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 40
        * - **Individuals**
          - 7
        * - **Properties**
          - 12

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
          - 7
        * - **Taxonomic Relations**
          - 77
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 7.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GTS

    ontology = GTS()
    ontology.load("path/to/GTS-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
