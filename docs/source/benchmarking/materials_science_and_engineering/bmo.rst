.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials
       * - **Current Version**
         - 0.1
       * - **Last Updated**
         - 2019-12-10
       * - **Creator**
         - Janakiram Karlapudi, Prathap Valluru
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Building Material Ontology (BMO) <https://matportal.org/ontologies/BUILDMAT>`_

Building Material Ontology (BMO)
========================================================================================================

The Building Material Ontology (BMO) is a domain ontology designed to represent the main concepts, types, layers, and properties of building materials used in construction and civil engineering [#bmo-doc]_ [#bmo-paper]_. BMO provides a structured vocabulary for describing material composition, material properties, functional layers, values, units, and relationships between materials in building assemblies [#bmo-doc]_ [#bmo-paper]_. The ontology was developed to improve the representation and management of building-material information in BIM workflows and to support interoperability and information exchange between stakeholders [#bmo-paper]_. By using Semantic Web and Linked Data principles, BMO facilitates material information management, data integration, querying, and reuse across construction and BIM applications [#bmo-paper]_.

**Example Usage**: Annotate a BIM model with BMO terms to describe the material composition of a building element, including individual materials or material layers and their associated properties. This allows building-material information to be represented and exchanged more consistently across BIM-based workflows and related construction applications [#bmo-doc]_ [#bmo-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 203
        * - **Total Edges**
          - 420
        * - **Root Nodes**
          - 83
        * - **Leaf Nodes**
          - 68
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 24
        * - **Individuals**
          - 12
        * - **Properties**
          - 62

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
          - 0.91
        * - **Depth Variance**
          - 1.30
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 83
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 27.29
        * - **Breadth Variance**
          - 1092.20
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 12
        * - **Taxonomic Relations**
          - 20
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 3.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BMO

    ontology = BMO()
    ontology.load("path/to/BMO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bmo-doc] Digital Construction Ontologies. 2021.
   "Digital Construction Materials."
   Ontology documentation.
   Available at:
   `https://digitalconstruction.github.io/Materials/v/0.5/ <https://digitalconstruction.github.io/Materials/v/0.5/>`_

.. [#bmo-paper] Valluru, P., and Karlapudi, J. 2020.
   "Building Material Ontology: A Semantic Data Model
   to Represent Building Material Data."
   Preprint.
   Available at:
   `https://www.researchgate.net/publication/341120638_Building_Material_Ontology_A_Semantic_data_model_to_represent_building_material_data
   <https://www.researchgate.net/publication/341120638_Building_Material_Ontology_A_Semantic_data_model_to_represent_building_material_data>`_
