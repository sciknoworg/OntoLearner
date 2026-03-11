.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.1.0
       * - **Last Updated**
         - May 24, 2023
       * - **Creator**
         - None
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Crystallographic Information Framework Core Dictionary (CIFCore) <https://github.com/emmo-repo/CIF-ontology?tab=readme-ov-file>`_

Crystallographic Information Framework Core Dictionary (CIFCore)
========================================================================================================

The Crystallographic Information Framework Core Dictionary (CIFCore) is a domain ontology developed to provide a machine-actionable representation of data files covering various aspects of crystallography and related structural sciences. CIFCore explains the historical development of CIF dictionaries and demonstrates the handling of complex information types in crystallographic data. The ontology supports semantic annotation of crystallographic datasets, enabling interoperability, data integration, and advanced analysis in structural biology, materials science, and chemistry. CIFCore facilitates the standardized description of crystal structures, symmetry operations, atomic coordinates, and experimental conditions. By providing a comprehensive vocabulary, CIFCore supports data sharing, reproducibility, and computational modeling in crystallography research. The ontology is actively maintained and extended to incorporate new crystallographic concepts and data standards.

**Example Usage**:
Annotate a crystallographic dataset with CIFCore terms to specify crystal lattice parameters, atomic positions, symmetry groups, and experimental conditions, enabling semantic search and integration with structural databases.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4494
        * - **Total Edges**
          - 15377
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 3310
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1182
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

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
          - 0.75
        * - **Depth Variance**
          - 0.19
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 3
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 2.00
        * - **Breadth Variance**
          - 1.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 27150
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CIFCore

    ontology = CIFCore()
    ontology.load("path/to/CIFCore-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
