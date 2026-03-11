

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
         - `Download Atomistic Simulation Methods Ontology (ASMO) <https://github.com/OCDO/asmo?tab=readme-ov-file#atomistic-simulation-methods-ontology-asmo>`_

Atomistic Simulation Methods Ontology (ASMO)
========================================================================================================

ASMO is a comprehensive ontology that formalizes concepts and relationships needed to describe and classify atomic-scale computational simulation methods used in materials science and computational chemistry. It provides structured vocabulary for representing commonly used simulation methodologies including density functional theory (DFT), molecular dynamics (MD), Monte Carlo (MC) methods, and other first-principles and statistical mechanics techniques. ASMO captures essential properties of simulation methods such as theoretical foundations, computational complexity, applicable material systems, and resulting properties that can be predicted. The ontology uses the Provenance Ontology (PROV-O) to formally describe simulation processes, enabling tracking of computational workflows, software tools, and input parameters used in materials modeling. ASMO facilitates reproducibility and interoperability in computational materials science by providing standardized semantic representations of simulation methods and their parameters.

**Example Usage**: Annotate a materials database entry with ASMO terms for the simulation method (e.g., DFT with specific functional), system size (number of atoms), computational details (basis sets, k-point meshes), and resulting properties (band gap, elastic constants).

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 588
        * - **Total Edges**
          - 1058
        * - **Root Nodes**
          - 23
        * - **Leaf Nodes**
          - 360
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 99
        * - **Individuals**
          - 30
        * - **Properties**
          - 41

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 5
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.71
        * - **Depth Variance**
          - 1.87
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 27
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 15.17
        * - **Breadth Variance**
          - 70.14
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 30
        * - **Taxonomic Relations**
          - 99
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 3.75
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ASMO

    ontology = ASMO()
    ontology.load("path/to/ASMO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
