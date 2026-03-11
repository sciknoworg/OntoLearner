.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemicals, Roles
       * - **Current Version**
         - 2015-11-23
       * - **Last Updated**
         - 2015-11-23
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download CHEBI Integrated Role Ontology (CHIRO) <https://terminology.tib.eu/ts/ontologies/chiro>`_

CHEBI Integrated Role Ontology (CHIRO)
========================================================================================================

The CHEBI Integrated Role Ontology (CHIRO) is a specialized ontology designed to provide a structured role hierarchy for chemicals. It connects chemicals in the structural hierarchy via a 'has role' relation, linking them to relevant classes in other ontologies. This enables the formalization of relationships between chemical structures (e.g., small molecules, drugs) and their functional roles, such as their biological or chemical activities. CHIRO facilitates the integration of chemical data with biological and biomedical ontologies, supporting applications in drug discovery, chemical informatics, and systems biology. By providing a standardized framework for describing chemical roles, CHIRO enhances data interoperability and enables advanced semantic queries across chemical and biological datasets. The ontology is particularly useful for linking chemical entities to their roles in biological processes, such as enzyme inhibitors, signaling molecules, or structural components.

**Example Usage**:
Annotate a dataset of small molecules with CHIRO terms to specify their roles, such as "enzyme inhibitor" or "neurotransmitter," and link these roles to relevant biological processes or pathways.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 81778
        * - **Total Edges**
          - 197071
        * - **Root Nodes**
          - 14636
        * - **Leaf Nodes**
          - 50439
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 13930
        * - **Individuals**
          - 0
        * - **Properties**
          - 15

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 16
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.36
        * - **Depth Variance**
          - 1.13
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 34719
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 4620.24
        * - **Breadth Variance**
          - 105924794.30
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 25262
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CHIRO

    ontology = CHIRO()
    ontology.load("path/to/CHIRO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
