.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Manufacturing
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2023-05-10
       * - **Creator**
         - Iassou Souroko, Ali Riza Durmaz
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Additive Manufacturing Ontology (AMOntology) <https://github.com/iassouroko/AMontology>`_

Additive Manufacturing Ontology (AMOntology)
========================================================================================================

The Additive Manufacturing Ontology (AMOntology) is a domain ontology developed to represent knowledge about additive manufacturing (AM) processes, computational models, and their characteristics. It is structured around two main components: AMProcessOntology, which captures entities and relationships relevant to AM processes, and ModelOntology, which describes modeling concepts for multi-physics, multi-scale simulations. AMOntology integrates these components to provide a comprehensive framework for describing process parameters, material properties, equipment, and computational models in AM. The ontology supports semantic annotation of digital manufacturing workflows, enabling data integration, process optimization, and knowledge sharing across research and industry. By providing a standardized vocabulary, AMOntology facilitates interoperability between digital manufacturing systems, simulation tools, and research databases. The ontology is actively maintained and extended to support new developments in additive manufacturing and computational modeling.

**Example Usage**:
Annotate an additive manufacturing workflow with AMOntology terms to specify process parameters (e.g., laser power, layer thickness), computational model characteristics, and material properties, enabling semantic search and integration with digital manufacturing platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 900
        * - **Total Edges**
          - 2299
        * - **Root Nodes**
          - 71
        * - **Leaf Nodes**
          - 99
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 328
        * - **Individuals**
          - 56
        * - **Properties**
          - 21

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 15
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.66
        * - **Depth Variance**
          - 11.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 116
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 55.50
        * - **Breadth Variance**
          - 1339.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 59
        * - **Taxonomic Relations**
          - 657
        * - **Non-taxonomic Relations**
          - 5
        * - **Average Terms per Type**
          - 1.26
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AMOntology

    ontology = AMOntology()
    ontology.load("path/to/AMOntology-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
