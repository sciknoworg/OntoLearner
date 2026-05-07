.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Crystallography
       * - **Current Version**
         - 0.0.1
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Crystallography Ontology (EMMOCrystallography) <https://github.com/emmo-repo/domain-crystallography>`_

Crystallography Ontology (EMMOCrystallography)
========================================================================================================

The Crystallography Domain Ontology (EMMOCrystallography) is an EMMO-based domain ontology for representing crystallographic knowledge [#emmocrystallography-github]_. It provides a formal vocabulary for describing crystallographic concepts such as crystal structures, crystallographic information, symmetry-related concepts, and structural data used in materials science [#emmocrystallography-github]_.

The ontology supports semantic annotation of crystallographic datasets, enabling interoperability, data integration, and reuse of crystallographic information across materials science and modelling workflows [#emmocrystallography-github]_. By connecting crystallographic concepts with the wider EMMO ontology ecosystem, EMMOCrystallography provides a standardized semantic framework for describing crystallographic structures and related data [#emmocrystallography-github]_.

**Example Usage**:
Annotate a crystallographic dataset with EMMOCrystallography terms to specify crystal structures, symmetry information, lattice-related data, atomic positions, and crystallographic metadata, enabling semantic search and integration with materials databases and modelling tools [#emmocrystallography-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 337
        * - **Total Edges**
          - 586
        * - **Root Nodes**
          - 29
        * - **Leaf Nodes**
          - 166
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 61
        * - **Individuals**
          - 0
        * - **Properties**
          - 5

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 14
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.20
        * - **Depth Variance**
          - 9.99
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 74
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 22.07
        * - **Breadth Variance**
          - 290.60
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EMMOCrystallography

    ontology = EMMOCrystallography()
    ontology.load("path/to/EMMOCrystallography-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#emmocrystallography-github] EMMO-repo. n.d.
   "Crystallography Domain Ontology."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/domain-crystallography <https://github.com/emmo-repo/domain-crystallography>`_
