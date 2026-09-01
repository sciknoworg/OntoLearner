.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.3.0.0
       * - **Last Updated**
         - 03/24/2024
       * - **Creator**
         - SDLE Research Center
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Materials Data Science Ontology (MDS) <https://matportal.org/ontologies/MDS>`_

Materials Data Science Ontology (MDS)
========================================================================================================

The Materials Data Science Ontology (MDS) is a low-level ontology designed to unify domain knowledge in materials science and applied data science [#mds-paper]_ [#mds-matportal]_. It encompasses multiple domains relevant to materials science, chemical synthesis and characterisation, photovoltaics, and geospatial datasets [#mds-matportal]_.

MDS provides a structured vocabulary for representing materials-related data, processes, and domain-specific concepts, with terms mapped to PMDCo and BFO ontologies [#mds-matportal]_ [#mds-paper]_. It follows a modular approach to support interoperability, data integration, semantic reasoning, and reuse across heterogeneous materials and data science datasets [#mds-paper]_. By providing a standardized framework, MDS supports semantic annotation, knowledge graph construction, and data-driven research in materials science [#mds-paper]_.

**Example Usage**:
Annotate a materials database with MDS terms to specify materials science concepts, chemical synthesis information, characterisation data, photovoltaic datasets, and geospatial information, enabling semantic search, data integration, and knowledge graph construction across materials informatics platforms [#mds-paper]_ [#mds-matportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 657
        * - **Total Edges**
          - 1457
        * - **Root Nodes**
          - 63
        * - **Leaf Nodes**
          - 303
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 363
        * - **Individuals**
          - 0
        * - **Properties**
          - 10

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.86
        * - **Depth Variance**
          - 0.57
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 87
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 46.00
        * - **Breadth Variance**
          - 997.50
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 351
        * - **Non-taxonomic Relations**
          - 128
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MDS

    ontology = MDS()
    ontology.load("path/to/MDS-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#mds-paper] Rajamohan, B. P., Bradley, A. C. H., Tran, V. D., et al. 2025.
   "Materials Data Science Ontology(MDS-Onto): Unifying Domain Knowledge in Materials and Applied Data Science."
   *Scientific Data*, 12, 628.
   DOI: 10.1038/s41597-025-04938-5.
   Available at:
   `https://www.nature.com/articles/s41597-025-04938-5 <https://www.nature.com/articles/s41597-025-04938-5>`_

.. [#mds-matportal] MatPortal. n.d.
   "Materials Data Science Ontology."
   Ontology registry entry.
   Available at:
   `https://matportal.org/ontologies/MDS <https://matportal.org/ontologies/MDS>`_
