.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Units and Measurements
       * - **Category**
         - Physics
       * - **Current Version**
         - 2.1
       * - **Last Updated**
         - March 1, 2022
       * - **Creator**
         - NASA Ames Research Center
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Quantities, Units, Dimensions and Data Types (QUDT) <https://qudt.org/>`_

Quantities, Units, Dimensions and Data Types (QUDT)
========================================================================================================

The Quantities, Units, Dimensions and Data Types (QUDT) ontology is a comprehensive framework for representing quantities, units, dimensions, and data types in scientific, engineering, and technical domains [#qudt-official]_ [#qudt-github]_. QUDT provides a standardized vocabulary for describing measurement units, quantity kinds, dimensional vectors, physical constants, conversion factors, and measurement values [#qudt-official]_. The ontology supports data expressed in RDF and related semantic web formats, enabling machine-readable representation of scientific and engineering measurements [#qudt-github]_. QUDT is widely used for semantic annotation of scientific datasets, IoT data streams, engineering models, and knowledge graphs, supporting automated unit conversion, validation, interoperability, and dimensional analysis [#qudt-official]_ [#qudt-github]_. The QUDT models are made publicly available through the QUDT project and public repository, supporting reuse, extension, and integration in semantic web and engineering applications [#qudt-official]_ [#qudt-github]_. By providing a common semantic foundation, QUDT facilitates data integration, analytics, and knowledge sharing across multidisciplinary projects [#qudt-official]_.

**Example Usage**:
Annotate a scientific dataset with QUDT terms to specify the quantities measured, such as ``temperature`` or ``pressure``; their units, such as ``degree Celsius`` or ``pascal``; and conversion factors or dimensional information. This enables automated unit conversion, semantic search, validation, and integration across datasets [#qudt-official]_ [#qudt-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 772
        * - **Total Edges**
          - 2288
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 233
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 73
        * - **Individuals**
          - 24
        * - **Properties**
          - 165

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
          - 27
        * - **Taxonomic Relations**
          - 400
        * - **Non-taxonomic Relations**
          - 12
        * - **Average Terms per Type**
          - 2.45
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import QUDT

    ontology = QUDT()
    ontology.load("path/to/QUDT-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#qudt-official] QUDT. n.d.
   "Quantities, Units, Dimensions and Data Types Ontologies."
   Available at:
   `https://www.qudt.org/ <https://www.qudt.org/>`_

.. [#qudt-github] QUDT. n.d.
   "QUDT Public Repository."
   GitHub Repository.
   Available at:
   `https://github.com/qudt/qudt-public-repo <https://github.com/qudt/qudt-public-repo>`_
