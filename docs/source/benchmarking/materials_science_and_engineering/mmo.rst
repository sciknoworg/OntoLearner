.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - 1.0.1
       * - **Last Updated**
         - 2024-01-30
       * - **Creator**
         - Akhil Thomas, Ali Riza Durmaz
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Materials Mechanics Ontology (MMO) <https://iwm-micro-mechanics-public.pages.fraunhofer.de/ontologies/materials-mechanics-ontology/index-en.html>`_

Materials Mechanics Ontology (MMO)
========================================================================================================

The Materials Mechanics Ontology (MMO) is an application-level ontology developed to support ontology-based named entity recognition in the materials mechanics and materials fatigue domain [#mmo-paper]_ [#mmo-gitlab]_. It provides a structured vocabulary for representing mechanics-of-materials concepts, including crystallographic defects, microstructural entities, material properties, damage mechanisms, fatigue concepts, specimens, tests, and processing-related entities [#mmo-paper]_.

MMO links ontology concepts with textual entities from scientific literature, enabling fine-grained and coarse-grained NER datasets for materials mechanics text mining [#mmo-paper]_. The ontology is mapped to PMDco and includes concepts relevant to composition-process-microstructure-property relationships, supporting semantic annotation, data standardization, information extraction, and knowledge graph generation from materials science literature [#mmo-paper]_.

**Example Usage**:
Annotate a materials fatigue paper or dataset with MMO terms to specify defects, microstructural features, fatigue properties, mechanical tests, damage mechanisms, and processing conditions, enabling ontology-based named entity recognition, semantic search, and integration with materials informatics workflows [#mmo-paper]_ [#mmo-gitlab]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1043
        * - **Total Edges**
          - 2402
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 509
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 428
        * - **Individuals**
          - 0
        * - **Properties**
          - 17

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 8
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.92
        * - **Depth Variance**
          - 5.32
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 17
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 8.89
        * - **Breadth Variance**
          - 21.65
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 566
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MMO

    ontology = MMO()
    ontology.load("path/to/MMO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#mmo-paper] Durmaz, A. R., Thomas, A., Mishra, L., Murthy, R. N., and Straub, T. 2024.
   "An ontology-based text mining dataset for extraction of process-structure-property entities."
   *Scientific Data*, 11, Article 1112.
   DOI: 10.1038/s41597-024-03926-5.
   Available at:
   `https://www.nature.com/articles/s41597-024-03926-5 <https://www.nature.com/articles/s41597-024-03926-5>`_

.. [#mmo-gitlab] Fraunhofer IWM Micro Mechanics Public. n.d.
   "Materials Mechanics Ontology."
   GitLab repository.
   Available at:
   `https://gitlab.cc-asp.fraunhofer.de/iwm-micro-mechanics-public/ontologies/materials-mechanics-ontology <https://gitlab.cc-asp.fraunhofer.de/iwm-micro-mechanics-public/ontologies/materials-mechanics-ontology>`_
