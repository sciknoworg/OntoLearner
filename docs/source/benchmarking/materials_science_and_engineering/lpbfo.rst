.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.1.9
       * - **Last Updated**
         - 2022-09-20
       * - **Creator**
         - Fraunhofer IWM
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Laser Powder Bed Fusion Ontology (LPBFO) <https://matportal.org/ontologies/LPBFO>`_

Laser Powder Bed Fusion Ontology (LPBFO)
========================================================================================================

The Laser Powder Bed Fusion Ontology (LPBFO) is a domain ontology developed to describe knowledge related to Laser Powder Bed Fusion (LPBF) additive manufacturing [#lpbfo-gitlab]_. LPBFO provides a structured vocabulary for representing LPBF manufacturing knowledge, including process information, materials, equipment, component-related data, and quality-relevant concepts [#lpbfo-gitlab]_.

The ontology supports semantic annotation of LPBF manufacturing workflows, enabling data integration, knowledge sharing, semantic search, and interoperability across additive manufacturing research and industrial platforms [#lpbfo-gitlab]_. By providing a standardized semantic framework, LPBFO supports the reuse and comparison of LPBF manufacturing knowledge [#lpbfo-gitlab]_.

**Example Usage**:
Annotate an LPBF manufacturing workflow with LPBFO terms to specify process parameters such as laser power, scan speed, layer thickness, material type, equipment information, component geometry, and quality-related attributes, enabling semantic search and integration with digital manufacturing platforms [#lpbfo-gitlab]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1835
        * - **Total Edges**
          - 3548
        * - **Root Nodes**
          - 129
        * - **Leaf Nodes**
          - 1056
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 508
        * - **Individuals**
          - 0
        * - **Properties**
          - 38

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 90
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 13.97
        * - **Depth Variance**
          - 590.11
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 276
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 10.16
        * - **Breadth Variance**
          - 1618.27
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 507
        * - **Non-taxonomic Relations**
          - 22
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import LPBFO

    ontology = LPBFO()
    ontology.load("path/to/LPBFO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#lpbfo-gitlab] Fraunhofer EMI_datamanagement. n.d.
   "LPBFO: Laser Powder Bed Fusion Ontology."
   GitLab repository.
   Available at:
   `https://gitlab.cc-asp.fraunhofer.de/EMI_datamanagement/LPBFO <https://gitlab.cc-asp.fraunhofer.de/EMI_datamanagement/LPBFO>`_
