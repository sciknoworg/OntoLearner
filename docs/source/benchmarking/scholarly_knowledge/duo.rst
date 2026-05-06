

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2025-02-17
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Data Use Ontology (DUO) <https://terminology.tib.eu/ts/ontologies/DUO/>`_

Data Use Ontology (DUO)
========================================================================================================

The Data Use Ontology (DUO) is a controlled vocabulary and ontology for formally representing data use restrictions, permissions, and conditions that govern access to and use of biomedical, clinical, and life sciences research data [#duo-obofoundry]_ [#duo-paper]_. DUO provides standardized terms for describing data use conditions, including general research use, health or medical research use, disease-specific restrictions, population-origin restrictions, commercial use limitations, publication requirements, and ethics or policy-based conditions [#duo-obofoundry]_ [#duo-paper]_. It enables data stewards, repositories, and data access committees to precisely specify how datasets may be used, supporting responsible secondary reuse and helping match researcher requests with dataset permissions [#duo-paper]_. DUO bridges policy and technical implementation by expressing complex data use conditions in a human-readable and machine-readable form [#duo-paper]_. By providing structured data use terms, DUO supports discoverability, interoperability, compliant reuse, and FAIR-oriented management of sensitive research datasets [#duo-obofoundry]_ [#duo-paper]_.

**Example Usage**: Annotate a biomedical research dataset with DUO terms to specify permissions such as ``general research use`` or ``health/medical/biomedical research``, restrictions such as ``no commercial use`` or disease-specific use, and requirements such as publication acknowledgment. This enables data access review, automated compliance checking, and appropriate data sharing decisions [#duo-obofoundry]_ [#duo-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 476
        * - **Total Edges**
          - 583
        * - **Root Nodes**
          - 196
        * - **Leaf Nodes**
          - 168
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
          - 1

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.30
        * - **Depth Variance**
          - 0.32
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 196
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 65.50
        * - **Breadth Variance**
          - 6073.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 33
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DUO

    ontology = DUO()
    ontology.load("path/to/DUO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#duo-obofoundry] OBO Foundry. n.d.
   "Data Use Ontology."
   Available at:
   `https://obofoundry.org/ontology/duo.html <https://obofoundry.org/ontology/duo.html>`_

.. [#duo-paper] Lawson, James, et al. 2021.
   "The Data Use Ontology to streamline responsible access to human biomedical datasets."
   *Cell Genomics* 1(2): 100028.
   DOI:
   `10.1016/j.xgen.2021.100028 <https://doi.org/10.1016/j.xgen.2021.100028>`_
