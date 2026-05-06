.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Properties
       * - **Current Version**
         - 0.0.8
       * - **Last Updated**
         - None
       * - **Creator**
         - María Poveda-Villalón, Serge Chávez-Feria
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Material Properties Ontology (MAT) <https://bimerr.iot.linkeddata.es/def/material-properties/>`_

Material Properties Ontology (MAT)
========================================================================================================

The Material Properties Ontology (MAT) is designed to provide a structured vocabulary for describing building components, materials, and their properties within the construction industry [#mat-doc]_ [#mat-bioregistry]_. It supports building renovation projects by representing material characteristics, property values, and relationships between materials, components, and building elements [#mat-doc]_.

MAT enables semantic annotation and integration of data from design, construction, and renovation workflows, supporting interoperability, data retrieval, and reuse in construction informatics platforms [#mat-doc]_. By providing a standardized vocabulary for material-property representation, MAT supports semantic search, material assessment, and knowledge sharing in building renovation and construction projects [#mat-doc]_ [#mat-bioregistry]_.

**Example Usage**:
Annotate a building renovation project with MAT terms to specify material types, building components, material properties, and performance-related values, enabling semantic search and integration with construction informatics and BIM-based renovation platforms [#mat-doc]_ [#mat-bioregistry]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 263
        * - **Total Edges**
          - 691
        * - **Root Nodes**
          - 7
        * - **Leaf Nodes**
          - 52
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 140
        * - **Individuals**
          - 0
        * - **Properties**
          - 21

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 11
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.21
        * - **Depth Variance**
          - 11.10
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 12
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.67
        * - **Breadth Variance**
          - 7.22
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 128
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MAT

    ontology = MAT()
    ontology.load("path/to/MAT-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations


References
----------

.. [#mat-doc] Poveda-Villalón, M., and Chávez-Feria, S. n.d.
   "Material Properties Ontology."
   Ontology documentation.
   Available at:
   `https://bimerr.iot.linkeddata.es/def/material-properties/ <https://bimerr.iot.linkeddata.es/def/material-properties/>`_

.. [#mat-bioregistry] Bioregistry. n.d.
   "Material properties ontology."
   Registry entry.
   Available at:
   `https://bioregistry.io/tib.mat <https://bioregistry.io/tib.mat>`_
