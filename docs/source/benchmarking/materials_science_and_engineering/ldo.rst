.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Defects
       * - **Current Version**
         - 1.0.0
       * - **Last Updated**
         - None
       * - **Creator**
         - https://orcid.org/0000-0001-7564-7990
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Line Defect Ontology (LDO) <https://github.com/OCDO/ldo>`_

Line Defect Ontology (LDO)
========================================================================================================

The Line Defect Ontology (LDO) is a domain ontology developed to provide a comprehensive and standardized vocabulary for describing line defects in crystalline materials, such as dislocations and disclinations. LDO enables the semantic annotation of experimental and computational data related to line defects, supporting interoperability and data integration across materials science databases and research platforms. The ontology covers key concepts including defect types, geometric and topological properties, formation mechanisms, and interactions with other defects or microstructural features. LDO is designed for extensibility, allowing researchers to describe new line defect types, characterization methods, and material systems as the field evolves. By providing a rigorous semantic framework, LDO facilitates advanced analytics, defect modeling, and knowledge sharing in materials science and engineering. The ontology is actively maintained and extended to incorporate new concepts and requirements from the materials science community.

**Example Usage**:
Annotate a transmission electron microscopy (TEM) dataset with LDO terms to specify the types of line defects observed, their Burgers vectors, line directions, and interactions with grain boundaries, enabling semantic search and integration with defect modeling tools.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 111
        * - **Total Edges**
          - 207
        * - **Root Nodes**
          - 6
        * - **Leaf Nodes**
          - 49
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 30
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
          - 4
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.25
        * - **Depth Variance**
          - 1.56
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 6
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 3.20
        * - **Breadth Variance**
          - 2.96
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 21
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import LDO

    ontology = LDO()
    ontology.load("path/to/LDO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
