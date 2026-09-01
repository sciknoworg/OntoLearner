.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 3.0.0-alpha1
       * - **Last Updated**
         - 2025-03-20
       * - **Creator**
         - Jannis Grundmann
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download The Platform MaterialDigital core ontology (PMDco) <https://github.com/materialdigital/core-ontology?tab=readme-ov-file>`_

The Platform MaterialDigital core ontology (PMDco)
========================================================================================================

The Platform MaterialDigital Core Ontology (PMDco) is a mid-level ontology developed for Materials Science and Engineering (MSE) [#pmdco-doc]_ [#pmdco-paper]_. It provides a structured semantic framework for representing materials, processes, experiments, workflows, simulations, data, metadata, and material properties across MSE domains [#pmdco-doc]_.

PMDco is based on the Basic Formal Ontology (BFO) and reuses BFO-aligned ontologies such as RO, IAO, and OBI to support interoperability with established ontology ecosystems [#pmdco-doc]_. The ontology helps bridge semantic gaps between top-level ontologies, domain-specific MSE application ontologies, and real-world research or industrial data sources [#pmdco-paper]_. By providing a standardized vocabulary, PMDco supports semantic annotation, data integration, traceability, reproducibility, FAIR data practices, and knowledge sharing in materials science [#pmdco-doc]_ [#pmdco-paper]_.

**Example Usage**:
Annotate a materials science project with PMDco terms to specify material types, processes, experiments, workflows, simulation data, measurement results, and metadata, enabling semantic search and integration with materials informatics platforms [#pmdco-doc]_ [#pmdco-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4207
        * - **Total Edges**
          - 8103
        * - **Root Nodes**
          - 85
        * - **Leaf Nodes**
          - 2365
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1002
        * - **Individuals**
          - 0
        * - **Properties**
          - 66

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
          - 3.90
        * - **Depth Variance**
          - 11.78
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 161
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 40.45
        * - **Breadth Variance**
          - 2084.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 903
        * - **Non-taxonomic Relations**
          - 19
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PMDco

    ontology = PMDco()
    ontology.load("path/to/PMDco-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#pmdco-doc] Platform MaterialDigital. n.d.
   "PMD Core Ontology (PMDco)."
   Ontology documentation.
   Available at:
   `https://materialdigital.github.io/core-ontology/docs/ <https://materialdigital.github.io/core-ontology/docs/>`_

.. [#pmdco-paper] Bayerlein, B., Schilling, M., Birkholz, H., Jung, M., Waitelonis, J., Mädler, L., and Sack, H. 2024.
   "PMD Core Ontology: Achieving semantic interoperability in materials science."
   *Materials & Design*, 237, 112603.
   DOI: 10.1016/j.matdes.2023.112603.
   Available at:
   `https://www.sciencedirect.com/science/article/pii/S0264127523010195 <https://www.sciencedirect.com/science/article/pii/S0264127523010195>`_
