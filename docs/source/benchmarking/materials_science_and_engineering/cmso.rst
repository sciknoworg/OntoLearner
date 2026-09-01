.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.0.1
       * - **Last Updated**
         - None
       * - **Creator**
         - https://orcid.org/0000-0001-7564-7990
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Computational Material Sample Ontology (CMSO) <https://github.com/OCDO/cmso/tree/main>`_

Computational Material Sample Ontology (CMSO)
========================================================================================================

The Computational Material Sample Ontology (CMSO) is a domain ontology developed to describe computational materials science samples or structures, with a focus on machine-actionable representation of atomistic simulation data [#cmso-doc]_ [#azocar2026]_. It provides a structured vocabulary for representing computational samples, atomic-scale samples, crystal structures, chemical composition, simulation cells, geometry, and crystallographic defects [#cmso-doc]_ [#azocar2026]_.

CMSO supports semantic annotation of computational materials data, enabling interoperability, data integration, and reuse across atomistic simulation workflows and materials databases [#azocar2026]_. The ontology is designed in a modular way and can be connected with related ontologies for crystallographic defects and atomistic simulation methods [#azocar2026]_. By providing a standardized framework, CMSO facilitates semantic search, cross-study comparison, and knowledge sharing in computational materials science [#cmso-doc]_ [#azocar2026]_.

**Example Usage**:
Annotate a computational materials science dataset with CMSO terms to specify the computational sample, atomic-scale structure, chemical composition, crystal structure, simulation cell, geometry, and crystallographic defects, enabling semantic search and integration with materials modelling databases [#cmso-doc]_ [#azocar2026]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 347
        * - **Total Edges**
          - 556
        * - **Root Nodes**
          - 40
        * - **Leaf Nodes**
          - 192
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 45
        * - **Individuals**
          - 0
        * - **Properties**
          - 51

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.56
        * - **Depth Variance**
          - 0.40
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 40
        * - **Minimum Breadth**
          - 6
        * - **Average Breadth**
          - 26.00
        * - **Breadth Variance**
          - 210.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 22
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CMSO

    ontology = CMSO()
    ontology.load("path/to/CMSO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#cmso-doc] OCDO. n.d.
   "Computational Material Sample Ontology (CMSO)."
   Ontology documentation.
   Available at:
   `https://ocdo.github.io/cmso/ <https://ocdo.github.io/cmso/>`_

.. [#azocar2026] Azócar Guzmán, A., Menon, S., Hickel, T., and Sandfeld, S. 2026.
   "Ontology-based knowledge graph infrastructure for interoperable atomistic simulation data."
   arXiv:2604.06230v1.
   Available at:
   `https://arxiv.org/html/2604.06230v1 <https://arxiv.org/html/2604.06230v1>`_
