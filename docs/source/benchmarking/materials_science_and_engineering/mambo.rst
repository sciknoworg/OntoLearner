.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - General Public License v3.0 (GPL-3.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Molecules And Materials Basic Ontology (MAMBO) <https://github.com/daimoners/MAMBO>`_

Molecules And Materials Basic Ontology (MAMBO)
========================================================================================================

The Materials And Molecules Basic Ontology (MAMBO) is a domain ontology for molecular materials and related applications [#mambo-paper]_ [#mambo-github]_. It is designed to organize knowledge about computational and experimental workflows involving molecular materials, nanomaterials, supramolecular systems, molecular aggregates, organic materials, and polymeric materials [#mambo-paper]_.

MAMBO provides a structured vocabulary for representing molecular materials, structures, properties, devices, methods, workflows, and application-related concepts [#mambo-paper]_ [#mambo-github]_. The ontology supports the retrieval and integration of structured information about molecular materials and helps connect computational simulations with experimental studies [#mambo-github]_. By providing a lightweight and modular semantic framework, MAMBO supports interoperability, data integration, predictive modelling, materials design, and knowledge sharing in molecular materials research [#mambo-paper]_.

**Example Usage**:
Annotate a molecular materials dataset with MAMBO terms to specify molecular structures, material properties, devices, methods, workflows, and application contexts, enabling semantic search and integration with computational modelling tools and experimental databases [#mambo-paper]_ [#mambo-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 166
        * - **Total Edges**
          - 624
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 7
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 57
        * - **Individuals**
          - 0
        * - **Properties**
          - 104

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.50
        * - **Depth Variance**
          - 0.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 1
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 39
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MAMBO

    ontology = MAMBO()
    ontology.load("path/to/MAMBO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#mambo-paper] Le Piane, F., Baldoni, M., Gaspari, M., and Mercuri, F. 2024.
   "MAMBO: a lightweight ontology for multiscale materials and applications."
   arXiv:2412.17877.
   Available at:
   `https://arxiv.org/abs/2412.17877 <https://arxiv.org/abs/2412.17877>`_

.. [#mambo-github] DAIMONERS. n.d.
   "MAMBO: Ontology for molecular materials."
   GitHub repository.
   Available at:
   `https://github.com/daimoners/MAMBO <https://github.com/daimoners/MAMBO>`_
