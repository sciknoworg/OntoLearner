

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

The Data Use Ontology (DUO) is a comprehensive vocabulary for formally representing and managing data use restrictions, permissions, and conditions that govern access to and usage of biomedical and life sciences research data. It provides standardized definitions of data use constraints including disease-specific research restrictions, commercial use prohibitions, publication acknowledgment requirements, and ethical/policy-based limitations. DUO enables data stewards and repositories to precisely specify how datasets can be used, facilitating automated enforcement of data use agreements and supporting secondary data reuse in compliant ways. The ontology bridges the gap between legal/ethical restrictions and technical implementations by providing machine-readable representations of complex data use policies. DUO supports FAIR data principles by enabling discoverable, interoperable, and reusable data through clear expression of usage conditions.

**Example Usage**: Annotate a biomedical research dataset with DUO terms to specify permissions (medical research only), restrictions (no commercial use), and requirements (publication acknowledgment, return of results to participants) enabling automated compliance checking and appropriate data sharing decisions.

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
