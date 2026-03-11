.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Crystallography
       * - **Current Version**
         - 0.0.1
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Crystallography Ontology (EMMOCrystallography) <https://github.com/emmo-repo/domain-crystallography>`_

Crystallography Ontology (EMMOCrystallography)
========================================================================================================

The Crystallography Ontology (EMMOCrystallography) is a domain ontology based on the Elementary Multiperspective Material Ontology (EMMO) and the Crystallographic Information Framework (CIF) core dictionary. It provides a formal language for representing crystallographic concepts, including crystal structures, symmetry operations, atomic positions, and experimental conditions. EMMOCrystallography supports semantic annotation of crystallographic datasets, enabling interoperability, data integration, and advanced analysis in materials science and structural biology. The ontology facilitates the standardized description of crystallographic experiments, data processing workflows, and structural models. By providing a rigorous semantic framework, EMMOCrystallography enhances reproducibility, data sharing, and computational modeling in crystallography research. The ontology is actively maintained and extended to incorporate new crystallographic concepts and community requirements.

**Example Usage**:
Annotate a crystallographic dataset with EMMOCrystallography terms to specify crystal lattice parameters, symmetry groups, atomic coordinates, and experimental metadata, enabling semantic search and integration with structural databases.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 337
        * - **Total Edges**
          - 586
        * - **Root Nodes**
          - 29
        * - **Leaf Nodes**
          - 166
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 61
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
          - 14
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.20
        * - **Depth Variance**
          - 9.99
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 74
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 22.07
        * - **Breadth Variance**
          - 290.60
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EMMOCrystallography

    ontology = EMMOCrystallography()
    ontology.load("path/to/EMMOCrystallography-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
