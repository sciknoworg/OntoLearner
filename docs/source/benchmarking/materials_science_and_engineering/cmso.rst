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

The Computational Material Sample Ontology (CMSO) is a domain ontology developed to describe computational materials science samples (or structures), with an initial focus on atomic-scale representations and crystalline defects. CMSO provides a structured vocabulary for representing atomic configurations, simulation cells, boundary conditions, and various types of defects such as vacancies, interstitials, and dislocations. The ontology supports semantic annotation of computational models, simulation workflows, and results, enabling interoperability and data integration across materials modeling platforms. CMSO is designed for extensibility, allowing researchers to describe new sample types, simulation methods, and material systems. By providing a standardized framework, CMSO facilitates cross-study comparison, advanced analytics, and knowledge sharing in computational materials science. The ontology is actively maintained and extended to incorporate new concepts and requirements from the materials science community.

**Example Usage**:
Annotate a computational materials science dataset with CMSO terms to specify the atomic structure, simulation cell parameters, defect types, and boundary conditions, enabling semantic search and integration with materials modeling databases.

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
