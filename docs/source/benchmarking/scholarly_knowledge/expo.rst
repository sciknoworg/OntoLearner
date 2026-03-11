.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scientific Experiments
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - Academic Free License (AFL)
       * - **Format**
         - owl
       * - **Download**
         - `Download Ontology of Scientific Experiments (EXPO) <https://expo.sourceforge.net/>`_

Ontology of Scientific Experiments (EXPO)
========================================================================================================

The Ontology of Scientific Experiments (EXPO) formalizes generic knowledge about scientific experimental design, methodology, and results representation. It provides a structured vocabulary for representing scientific experiments, methodologies, and results, supporting both theoretical and experimental research in scientific experimentation.

The ontology employs a class-based modeling approach, defining classes for different types of experiments, methodologies, and results, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. EXPO supports the integration of data from various sources, promoting interoperability and data-driven research in scientific experimentation.

Typical applications of EXPO include the development of new experimental design methods, the optimization of experimental methodologies, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, EXPO enhances collaboration and innovation in the field of scientific experimentation.

**Example Usage**:
Annotate a scientific experiment with EXPO terms to specify experiment types, methodologies, and results, enabling semantic search and integration with scientific experimentation platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 858
        * - **Total Edges**
          - 2921
        * - **Root Nodes**
          - 13
        * - **Leaf Nodes**
          - 265
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 347
        * - **Individuals**
          - 0
        * - **Properties**
          - 78

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 19
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 6.55
        * - **Depth Variance**
          - 13.84
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 71
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 24.15
        * - **Breadth Variance**
          - 438.53
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 432
        * - **Non-taxonomic Relations**
          - 726
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EXPO

    ontology = EXPO()
    ontology.load("path/to/EXPO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
