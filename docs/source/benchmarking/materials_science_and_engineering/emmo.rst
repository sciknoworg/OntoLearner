.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Modelling
       * - **Current Version**
         - 1.0.0-rc3
       * - **Last Updated**
         - 2024-03
       * - **Creator**
         - European Materials Modelling Council (EMMC)
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download The Elementary Multiperspective Material Ontology (EMMO) <https://emmo-repo.github.io/>`_

The Elementary Multiperspective Material Ontology (EMMO)
========================================================================================================

The Elementary Multiperspective Material Ontology (EMMO) is a foundational ontology developed by the European Materials Modelling Council (EMMC) to provide a standard representational framework for materials science, materials modelling, characterisation, and manufacturing [#emmo-emmc]_ [#emmo-github]_. EMMO is distinctive because it starts from the physical world as described by applied sciences, especially physics and materials science, rather than only from abstract upper-level concepts [#emmo-emmc]_.

The ontology provides a framework for representing materials, processes, properties, models, measurements, and data, supporting semantic interoperability across materials modelling, characterisation, and experimental workflows [#emmo-emmc]_ [#emmo-github]_. EMMO is modular and extensible, allowing domain-specific ontologies to be developed for specialised applications in materials research, digital platforms, and manufacturing [#emmo-github]_. By providing a rigorous semantic foundation, EMMO supports data interoperability, knowledge sharing, FAIR documentation, and reuse across the materials science community [#emmo-emmc]_ [#emmo-github]_.

**Example Usage**:
Annotate a materials database with EMMO terms to describe the composition, structure, and properties of a material sample, the characterisation techniques used, and the modelling workflows applied, enabling semantic search and data integration across materials science research projects [#emmo-emmc]_ [#emmo-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 13613
        * - **Total Edges**
          - 30349
        * - **Root Nodes**
          - 281
        * - **Leaf Nodes**
          - 7742
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 2448
        * - **Individuals**
          - 2
        * - **Properties**
          - 181

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 41
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 8.16
        * - **Depth Variance**
          - 107.87
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 552
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 67.24
        * - **Breadth Variance**
          - 14619.32
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 2
        * - **Taxonomic Relations**
          - 16281
        * - **Non-taxonomic Relations**
          - 52
        * - **Average Terms per Type**
          - 2.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EMMO

    ontology = EMMO()
    ontology.load("path/to/EMMO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#emmo-emmc] European Materials Modelling Council. n.d.
   "EMMO – Ontology for Materials Science."
   Available at:
   `https://emmc.eu/emmo/ <https://emmc.eu/emmo/>`_

.. [#emmo-github] EMMO-repo. n.d.
   "Elementary Multiperspective Material Ontology (EMMO)."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/EMMO <https://github.com/emmo-repo/EMMO>`_
