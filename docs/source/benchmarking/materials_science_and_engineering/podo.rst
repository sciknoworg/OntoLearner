

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
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
         - `Download Point Defects Ontology (PODO) <https://github.com/OCDO/podo>`_

Point Defects Ontology (PODO)
========================================================================================================

PODO is a specialized ontology that formalizes the conceptualization and semantic representation of point defects in crystalline materials, enabling precise description and classification of atomic-scale defects. It provides structured vocabulary for describing different point defect types including vacancies, interstitials, substitutional defects, and antisite defects, along with their properties and formation mechanisms. PODO captures essential characteristics of point defects such as charge state, migration energy, binding interactions with other defects, and effects on material properties. The ontology enables systematic annotation of experimental observations (X-ray diffraction, electron microscopy) and computational predictions (first-principles calculations) of point defects in various crystal structures. PODO facilitates knowledge integration in materials informatics and computational materials databases by providing standardized semantic representations of point defect phenomena.

**Example Usage**: Annotate a first-principles DFT study of point defects in semiconductors with PODO terms describing defect type (e.g., oxygen vacancy in TiO2), charge state (+2, neutral, -2), formation energy, charge transition levels, and effects on band structure and electrical properties.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 153
        * - **Total Edges**
          - 192
        * - **Root Nodes**
          - 38
        * - **Leaf Nodes**
          - 84
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 12
        * - **Individuals**
          - 0
        * - **Properties**
          - 5

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.57
        * - **Depth Variance**
          - 0.40
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 38
        * - **Minimum Breadth**
          - 6
        * - **Average Breadth**
          - 25.00
        * - **Breadth Variance**
          - 188.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 12
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PODO

    ontology = PODO()
    ontology.load("path/to/PODO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
