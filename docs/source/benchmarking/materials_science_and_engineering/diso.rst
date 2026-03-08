.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 21.03.202
       * - **Creator**
         - Ahmad Zainul Ihsan
       * - **License**
         - Creative Commons Attribution 3.0 International (CC BY 3.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Dislocation Ontology (DISO) <https://github.com/Materials-Data-Science-and-Informatics/dislocation-ontology>`_

Dislocation Ontology (DISO)
========================================================================================================

DISO is a specialized ontology that formalizes the conceptualization and semantic representation of linear defects in crystalline materials, with particular focus on dislocations and their complex relationships. It provides structured vocabulary for describing dislocation types (edge, screw, mixed), dislocation properties (Burgers vector, line direction), and dislocation interactions (annihilation, multiplication, cross-slip). The ontology captures the geometric and topological properties of dislocations essential for understanding plastic deformation, work hardening, and material strength in metals and alloys. DISO enables precise annotation of experimental observations and computational simulations of dislocations in crystalline microstructures, supporting materials science research and industrial applications. DISO facilitates knowledge integration in materials databases and computational materials science by providing standardized semantic representations of linear defects.

**Example Usage**:
Annotate a transmission electron microscopy (TEM) image or molecular dynamics simulation showing dislocations with DISO terms describing dislocation type (edge or screw), Burgers vector, crystal system context, and interactions with other dislocations or grain boundaries.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 324
        * - **Total Edges**
          - 739
        * - **Root Nodes**
          - 9
        * - **Leaf Nodes**
          - 91
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 62
        * - **Individuals**
          - 0
        * - **Properties**
          - 45

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.18
        * - **Depth Variance**
          - 0.15
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 9
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.50
        * - **Breadth Variance**
          - 12.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 38
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DISO

    ontology = DISO()
    ontology.load("path/to/DISO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
