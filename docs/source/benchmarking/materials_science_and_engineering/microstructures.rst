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

The EMMO-based ontology for microstructures (MicroStructures) is a domain ontology designed to represent metallic microstructures and related materials science concepts [#microstructures-emmc]_. It provides a structured framework for describing microstructure information, including microstructure features, materials, properties, processes, characterisation data, and modelling workflows [#microstructures-emmc]_.

MicroStructures supports semantic annotation and integration of microstructural data, helping connect experimental characterisation, data processing, and through-scale or through-process modelling in materials science [#microstructures-emmc]_. By providing an EMMO-based framework, it supports interoperability, knowledge sharing, and more consistent representation of microstructure-related information across research and engineering workflows [#microstructures-emmc]_.

**Example Usage**:
Annotate a microstructure characterisation dataset with MicroStructures terms to describe microstructure features, material properties, characterisation results, processing history, and modelling information, enabling semantic search and integration with materials databases and modelling tools [#microstructures-emmc]_.

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

References
---------

.. [#microstructures-emmc] European Materials Modelling Council. 2024.
   "TG Microstructure domain ontology."
   Available at:
   `https://emmc.eu/tg-microstructure-domain-ontology/ <https://emmc.eu/tg-microstructure-domain-ontology/>`_
