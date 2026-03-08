

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 08 February 2022
       * - **Creator**
         - IEEE
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Chemical Kinetics Ontology (OntoKin) <https://www.ontologyportal.org/>`_

Chemical Kinetics Ontology (OntoKin)
========================================================================================================

OntoKin is a comprehensive ontology developed for formal and standardized representation of chemical kinetics data, reaction mechanisms, and kinetic rate parameters used in chemistry and combustion science. It provides structured definitions of reaction mechanisms, including species involved, reaction pathways, elementary steps, and kinetic rate coefficients essential for modeling chemical processes. OntoKin captures important chemical kinetics concepts such as reaction types (forward, reverse, three-body), activation energies, temperature dependencies, and pressure effects on reaction rates. The ontology facilitates data integration and knowledge sharing in computational chemistry, combustion research, and chemical process modeling by providing unambiguous semantic representations. OntoKin supports automated reasoning and knowledge discovery in chemical databases, enabling researchers to search, compare, and reuse kinetic mechanisms across different applications.

**Example Usage**: Represent a chemical reaction mechanism with OntoKin terms for species (CH4, O2, H2O), elementary reaction steps with activation energies, and temperature-dependent rate coefficients using Arrhenius or modified Arrhenius equations.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 407
        * - **Total Edges**
          - 1011
        * - **Root Nodes**
          - 122
        * - **Leaf Nodes**
          - 103
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 83
        * - **Individuals**
          - 0
        * - **Properties**
          - 136

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
          - 1.64
        * - **Depth Variance**
          - 2.39
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 122
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 45.22
        * - **Breadth Variance**
          - 1858.40
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 51
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OntoKin

    ontology = OntoKin()
    ontology.load("path/to/OntoKin-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
