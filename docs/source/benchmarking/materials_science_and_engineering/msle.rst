.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - Sep 15, 2022
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - ttl
       * - **Download**
         - `Download Material Science Lab Equipment Ontology (MSLE) <https://github.com/MehrdadJalali-AI/MSLE-Ontology>`_

Material Science Lab Equipment Ontology (MSLE)
========================================================================================================

The Material Science Lab Equipment Ontology (MSLE) is a domain ontology developed to describe laboratory equipment used in materials science, with a focus on large-scale devices for materials characterization [#msle-paper]_. It provides a structured vocabulary for representing laboratory equipment, equipment types, device specifications, acronyms, alternative labels, and characterization-related information [#msle-paper]_.

MSLE supports semantic annotation, interoperability, data integration, querying, and reuse of laboratory-equipment information in materials science workflows [#msle-paper]_. The ontology integrates relevant semantic web resources such as the Semantic Sensor Network ontology, Material Vocabulary, SKOS, and SHACL to represent and validate equipment-related knowledge [#msle-paper]_. By providing a standardized vocabulary, MSLE supports better organization, discovery, and integration of materials science laboratory equipment data [#msle-paper]_.

**Example Usage**:
Annotate a laboratory equipment dataset with MSLE terms to specify equipment types, device specifications, acronyms, alternative names, and characterization-device information, enabling semantic search and integration with materials informatics platforms [#msle-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 146
        * - **Total Edges**
          - 479
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 52
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 45
        * - **Individuals**
          - 3
        * - **Properties**
          - 10

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.77
        * - **Depth Variance**
          - 1.70
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 53
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 17.75
        * - **Breadth Variance**
          - 353.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 3
        * - **Taxonomic Relations**
          - 47
        * - **Non-taxonomic Relations**
          - 228
        * - **Average Terms per Type**
          - 1.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MSLE

    ontology = MSLE()
    ontology.load("path/to/MSLE-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#msle-paper] Jalali, M., Mail, M., Aversa, R., and Kübel, C. 2023.
   "MSLE: An ontology for Materials Science Laboratory Equipment. Large-Scale Devices for Materials Characterization."
   *Materials Today Communications*, 35, 105532.
   DOI: 10.1016/j.mtcomm.2023.105532.
   Available at:
   `https://arxiv.org/abs/2308.07325 <https://arxiv.org/abs/2308.07325>`_
