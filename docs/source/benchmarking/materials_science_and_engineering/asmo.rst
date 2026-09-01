

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.0.0
       * - **Last Updated**
         - None
       * - **Creator**
         - https://orcid.org/0000-0001-7564-7990
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Atomistic Simulation Methods Ontology (ASMO) <https://github.com/OCDO/asmo?tab=readme-ov-file#atomistic-simulation-methods-ontology-asmo>`_

Atomistic Simulation Methods Ontology (ASMO)
========================================================================================================

The **Atomistic Simulation Methods Ontology (ASMO)** is a domain ontology that formalizes concepts and relationships used to describe and classify atomic-scale computational simulation methods in materials science and computational chemistry [#asmo-doc]_ [#asmo-github]_ [#asmo-paper]_. It provides a structured vocabulary for representing common simulation methodologies, including density functional theory (DFT), molecular dynamics (MD), kinetic Monte Carlo methods, molecular statics, and ab initio molecular dynamics [#asmo-doc]_ [#asmo-paper]_.

ASMO captures important simulation-related concepts such as computational methods, simulation algorithms, simulation parameters, interatomic potentials, statistical ensembles, structure manipulation, mathematical operations, and calculated physical properties [#asmo-doc]_ [#asmo-paper]_. The ontology also builds on the W3C Provenance Ontology (PROV-O) to describe simulation processes and provenance, enabling the representation of computational workflows, activities, inputs, generated results, agents, and software involved in simulations [#asmo-github]_ [#asmo-paper]_.

ASMO facilitates reproducibility and interoperability in computational materials science by providing standardized semantic representations of simulation methods, parameters, workflows, calculated properties, and provenance across heterogeneous computational environments [#asmo-doc]_ [#asmo-paper]_.

**Example Usage**: Annotate a materials database entry with ASMO terms for the simulation method, such as DFT or MD, together with computational details such as simulation parameters, interatomic potentials, statistical ensembles, and resulting properties such as bulk modulus, formation energy, total energy, pressure, or magnetic moment [#asmo-doc]_ [#asmo-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 588
        * - **Total Edges**
          - 1058
        * - **Root Nodes**
          - 23
        * - **Leaf Nodes**
          - 360
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 99
        * - **Individuals**
          - 30
        * - **Properties**
          - 41

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 5
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.71
        * - **Depth Variance**
          - 1.87
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 27
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 15.17
        * - **Breadth Variance**
          - 70.14
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 30
        * - **Taxonomic Relations**
          - 99
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 3.75
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ASMO

    ontology = ASMO()
    ontology.load("path/to/ASMO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#asmo-doc] Azocar Guzman, A. 2024.
   "Atomistic Simulation Methods Ontology (ASMO)."
   Ontology documentation.
   DOI: 10.5281/zenodo.10805591.
   Available at:
   `https://ocdo.github.io/asmo/ <https://ocdo.github.io/asmo/>`_

.. [#asmo-github] OCDO. n.d.
   "ASMO - Atomistic Simulation Methods Ontology."
   GitHub repository.
   Available at:
   `https://github.com/OCDO/asmo <https://github.com/OCDO/asmo>`_

.. [#asmo-paper] Azócar Guzmán, A., Menon, S., Hickel, T.,
   and Sandfeld, S. 2026.
   "Ontology-based Knowledge Graph Infrastructure for
   Interoperable Atomistic Simulation Data."
   arXiv:2604.06230.
   Available at:
   `https://arxiv.org/abs/2604.06230
   <https://arxiv.org/abs/2604.06230>`_
