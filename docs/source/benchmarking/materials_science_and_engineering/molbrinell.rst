.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Testing
       * - **Current Version**
         - 0.1
       * - **Last Updated**
         - 05/05/2022
       * - **Creator**
         - Birgit Skrotzki, Hossein Beygi Nasrabadi, Philipp von Hartrott, Vinicius Carrillo Beber, Yue Chen
       * - **License**
         - None
       * - **Format**
         - ttl
       * - **Download**
         - `Download MatoLab Brinell Test Ontology (MOL_BRINELL) <https://matportal.org/ontologies/MOL_BRINELL>`_

MatoLab Brinell Test Ontology (MOL_BRINELL)
========================================================================================================

The MatoLab Brinell Test Ontology (MOL_BRINELL) is an application-level ontology developed to represent the Brinell hardness testing process [#molbrinell-matportal]_ [#bto-github]_. It provides a structured vocabulary for describing Brinell testing processes, testing equipment requirements, test-piece characteristics, related testing parameters, and measurement procedures according to the DIN EN ISO 6506-1 standard [#bto-github]_.

MOL_BRINELL supports semantic annotation of Brinell hardness testing data, enabling interoperability, data integration, semantic search, and reuse in materials testing and materials informatics workflows [#molbrinell-matportal]_ [#bto-github]_. The Brinell Test Ontology repository also documents multiple ontology versions developed with different top-level ontology alignments, including BFO+CCO, EMMO+CHAMEO, PROV-O+PMDco, and BFO+IOF [#bto-github]_.

**Example Usage**:
Annotate a Brinell hardness testing dataset with MOL_BRINELL terms to specify the Brinell testing process, testing equipment, test-piece characteristics, testing parameters, measurement procedure, and hardness-test results, enabling semantic search and integration with materials informatics platforms [#molbrinell-matportal]_ [#bto-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 3648
        * - **Total Edges**
          - 16347
        * - **Root Nodes**
          - 29
        * - **Leaf Nodes**
          - 308
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 37
        * - **Individuals**
          - 3053
        * - **Properties**
          - 21

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
          - 0.26
        * - **Depth Variance**
          - 0.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 29
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 12.67
        * - **Breadth Variance**
          - 141.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 3053
        * - **Taxonomic Relations**
          - 14
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 105.28
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MOLBRINELL

    ontology = MOLBRINELL()
    ontology.load("path/to/MOLBRINELL-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bto-github] Nasrabadi, H. B. n.d.
   "Brinell-Test-Ontology-BTO."
   GitHub repository.
   Available at:
   `https://github.com/HosseinBeygiNasrabadi/Brinell-Test-Ontology-BTO- <https://github.com/HosseinBeygiNasrabadi/Brinell-Test-Ontology-BTO->`_

.. [#molbrinell-matportal] MatPortal. 2022.
   "MatoLab Brinell Test Ontology (MOL_BRINELL)."
   Ontology registry entry.
   Available at:
   `https://matportal.org/ontologies/MOL_BRINELL <https://matportal.org/ontologies/MOL_BRINELL>`_
