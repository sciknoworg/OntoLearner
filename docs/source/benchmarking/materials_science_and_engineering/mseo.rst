.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Thomas Hanke, Fraunhofer IWM
       * - **License**
         - MIT License
       * - **Format**
         - ttl
       * - **Download**
         - `Download Materials Science and Engineering Ontology (MSEO) <https://github.com/Mat-O-Lab/MSEO>`_

Materials Science and Engineering Ontology (MSEO)
========================================================================================================

The Materials Science and Engineering Ontology (MSEO) is a domain ontology developed to represent experiments and resulting data in materials science and engineering [#mseo-matportal]_ [#mseo-github]_. It provides a structured vocabulary for describing materials, processes, properties, software, identifiers, data transformations, and experiment-related information [#mseo-github]_.

MSEO supports the creation of machine-readable and human-readable semantic data, enabling interoperability, semantic annotation, data integration, retrieval, and reuse across materials science workflows [#mseo-matportal]_ [#mseo-github]_. By providing a standardized vocabulary, MSEO helps organize materials science experiments and supports knowledge sharing in materials informatics platforms [#mseo-github]_.

**Example Usage**:
Annotate a materials science experiment with MSEO terms to specify material types, experimental processes, measured properties, software, identifiers, data transformations, and resulting data, enabling semantic search and integration with materials informatics platforms [#mseo-matportal]_ [#mseo-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 543
        * - **Total Edges**
          - 782
        * - **Root Nodes**
          - 12
        * - **Leaf Nodes**
          - 396
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 138
        * - **Individuals**
          - 0
        * - **Properties**
          - 2

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 4
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.44
        * - **Depth Variance**
          - 1.58
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 18
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 9.60
        * - **Breadth Variance**
          - 24.24
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 102
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MSEO

    ontology = MSEO()
    ontology.load("path/to/MSEO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#mseo-matportal] MatPortal. 2023.
   "Material Science and Engineering Ontology."
   Ontology registry entry.
   Available at:
   `https://matportal.org/ontologies/MSEO <https://matportal.org/ontologies/MSEO>`_

.. [#mseo-github] Mat-O-Lab. n.d.
   "MSEO: Repository of Materials Science and Engineering Ontology."
   GitHub repository.
   Available at:
   `https://github.com/Mat-O-Lab/MSEO <https://github.com/Mat-O-Lab/MSEO>`_
