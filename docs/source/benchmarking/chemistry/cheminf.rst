

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - 2.1.0
       * - **Last Updated**
         - None
       * - **Creator**
         - Egon Willighagen, Nina Jeliazkova, Ola Spjuth, Valery Tkachenko
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Chemical Information Ontology (CHEMINF) <https://terminology.tib.eu/ts/ontologies/CHEMINF>`_

Chemical Information Ontology (CHEMINF)
========================================================================================================

The Chemical Information Ontology (CHEMINF) provides a comprehensive vocabulary for representing and describing information entities and computational descriptors about chemical compounds and substances. It formalizes chemical descriptors, properties, and computational methods used in cheminformatics, enabling standardized representation of molecular attributes derived from chemical informatics tools and algorithms. CHEMINF captures qualitative and quantitative descriptors including molecular weight, logP, HOMO/LUMO energies, and topological indices used for chemical structure analysis and prediction. The ontology is designed to support semantic interoperability in chemistry databases, computational chemistry platforms, and drug discovery systems by providing unambiguous definitions of chemical information concepts. CHEMINF integrates with other chemistry ontologies (ChEBI, MOP, RXNO) to link chemical structures with their calculated properties and computational methods.

**Example Usage**: Represent a computed molecular descriptor as a CHEMINF information entity linked to a ChEBI chemical structure, specifying the calculation method (e.g., "Wildman-Crippen LogP") and the resulting numeric value.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1467
        * - **Total Edges**
          - 2837
        * - **Root Nodes**
          - 213
        * - **Leaf Nodes**
          - 435
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 358
        * - **Individuals**
          - 0
        * - **Properties**
          - 52

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
          - 1.73
        * - **Depth Variance**
          - 9.21
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 213
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 29.24
        * - **Breadth Variance**
          - 3411.59
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 93
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CHEMINF

    ontology = CHEMINF()
    ontology.load("path/to/CHEMINF-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
