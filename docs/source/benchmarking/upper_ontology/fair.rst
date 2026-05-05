

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Data, Metadata
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download FAIR Vocabulary (FAIR) <https://terminology.tib.eu/ts/ontologies/FAIR>`_

FAIR Vocabulary (FAIR)
========================================================================================================
The FAIR Vocabulary is a formal vocabulary that provides machine-readable definitions and semantic representation of the FAIR Data Principles: Findability, Accessibility, Interoperability, and Reusability [#fair-vocabulary]_. It formalizes key concepts underlying FAIR data management, including persistent identifiers, metadata, access protocols, interoperability standards, qualified references, provenance, licensing, and reusability conditions [#fair-vocabulary]_. The vocabulary represents FAIR principles and sub-principles as semantic entities, allowing them to be referenced, linked, and interpreted in machine-readable environments [#fair-vocabulary]_. FAIR vocabulary terms can be applied to dataset descriptions, data repositories, metadata records, and digital object properties to formally express FAIR characteristics and support FAIR assessment workflows [#fair-vocabulary]_. By providing standardized semantic definitions, the vocabulary facilitates communication of FAIR principles within research organizations, funding agencies, repositories, and data management communities [#fair-vocabulary]_.

**Example Usage**: Annotate a dataset in a repository with FAIR terms to indicate its Findability through persistent identifiers, Accessibility through standard access protocols, Interoperability through shared formats and ontologies, and Reusability through clear licensing, provenance, and rich metadata [#fair-vocabulary]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 92
        * - **Total Edges**
          - 180
        * - **Root Nodes**
          - 9
        * - **Leaf Nodes**
          - 37
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 7
        * - **Individuals**
          - 19
        * - **Properties**
          - 1

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
          - 0.18
        * - **Depth Variance**
          - 0.15
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 9
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.50
        * - **Breadth Variance**
          - 12.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 19
        * - **Taxonomic Relations**
          - 3
        * - **Non-taxonomic Relations**
          - 3
        * - **Average Terms per Type**
          - 9.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import FAIR

    ontology = FAIR()
    ontology.load("path/to/FAIR-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#fair-vocabulary] FAIR Principles Vocabulary. n.d.
   "FAIR Vocabulary."
   Available at:
   `https://peta-pico.github.io/FAIR-nanopubs/principles/index-en.html <https://peta-pico.github.io/FAIR-nanopubs/principles/index-en.html>`_
