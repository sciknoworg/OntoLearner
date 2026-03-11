.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Microstructure
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - owl
       * - **Download**
         - `Download EMMO-based ontology for microstructures (MicroStructures) <https://github.com/jesper-friis/emmo-microstructure>`_

EMMO-based ontology for microstructures (MicroStructures)
========================================================================================================

The EMMO-based ontology for microstructures (MicroStructures) is a domain ontology designed to represent metallic microstructures, including their composition, particles (both stable and metastable), grains, subgrains, grain boundaries, particle free zones (PFZs), texture, and dislocations. The ontology provides a structured vocabulary for describing microstructure features, supporting both microstructure modeling and experimental characterization. MicroStructures enables semantic annotation of microstructural data, facilitating interoperability, data integration, and advanced analysis in materials science and engineering. The ontology is designed for extensibility, allowing researchers to describe new microstructure types, characterization techniques, and material systems. By providing a standardized framework, MicroStructures supports cross-study comparison, microstructure-property correlation, and knowledge sharing in materials research. The ontology is actively maintained and extended to incorporate new concepts and requirements from the materials science community.

**Example Usage**:
Annotate a microstructure characterization dataset with MicroStructures terms to specify grain size distribution, particle types, texture, and dislocation density, enabling semantic search and integration with materials databases and modeling tools.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 115
        * - **Total Edges**
          - 287
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 37
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 43
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
          - 0.67
        * - **Depth Variance**
          - 0.22
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 2
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.50
        * - **Breadth Variance**
          - 0.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 17
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MicroStructures

    ontology = MicroStructures()
    ontology.load("path/to/MicroStructures-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
