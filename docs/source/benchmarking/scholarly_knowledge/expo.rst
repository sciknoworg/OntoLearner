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

The Ontology of Scientific Experiments (EXPO) formalizes generic knowledge about scientific experimental design, methodology, and results representation [#expo-sourceforge]_ [#expo-paper]_. It provides a structured OWL-based vocabulary for representing experiments, experimental goals, experimental design, methods, actions, objects, equipment, results, conclusions, and related scientific context [#expo-sourceforge]_ [#expo-paper]_. EXPO is intended to support the formal description of experiments for efficient analysis, annotation, sharing, comparison, and reuse of experimental results across scientific domains [#expo-paper]_. The ontology links the Suggested Upper Merged Ontology (SUMO) with subject-specific ontologies of experiments, allowing general experimental concepts to be specialized for particular domains [#expo-paper]_. EXPO has been demonstrated across different experimental domains, including high-energy physics and phylogenetics, showing its usefulness for making experimental goals, structures, and assumptions more explicit [#expo-paper]_.

The ontology uses a class-based modeling approach, defining concepts for experiment types, experimental goals, methodologies, experimental actions, experimental objects, equipment, results, and conclusions [#expo-sourceforge]_ [#expo-paper]_. These concepts are organized through hierarchical and relational structures, enabling semantic annotation, retrieval, comparison, and analysis of experimental knowledge [#expo-sourceforge]_. EXPO supports interoperability by providing a common ontology for describing experiments across disciplines, while still allowing extension through domain-specific experimental ontologies [#expo-paper]_.

Typical applications of EXPO include semantic annotation of scientific experiments, integration of experimental metadata from different sources, comparison of experimental designs, representation of methods and results, and support for reproducibility and knowledge discovery [#expo-sourceforge]_ [#expo-paper]_. By providing a standardized vocabulary and framework, EXPO enhances sharing, analysis, and reuse of experimental knowledge across scientific communities [#expo-paper]_.

**Example Usage**:
Annotate a scientific experiment with EXPO terms to specify its experimental goal, design, methodology, experimental object, equipment, actions, results, and conclusions. This enables semantic search, experiment comparison, reproducibility support, and integration with scientific experimentation platforms [#expo-sourceforge]_ [#expo-paper]_.

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

References
----------

.. [#expo-sourceforge] EXPO. n.d.
   "EXPO: Ontology of Scientific Experiments."
   Available at:
   `https://expo.sourceforge.net/ <https://expo.sourceforge.net/>`_

.. [#expo-paper] Soldatova, Larisa N., and Ross D. King. 2006.
   "An ontology of scientific experiments."
   *Journal of The Royal Society Interface* 3(11): 795--803.
   DOI:
   `10.1098/rsif.2006.0134 <https://doi.org/10.1098/rsif.2006.0134>`_
