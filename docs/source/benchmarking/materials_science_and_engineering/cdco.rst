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
         - `Download Crystallographic Defect Core Ontology (CDCO) <https://github.com/OCDO/cdco>`_

Crystallographic Defect Core Ontology (CDCO)
========================================================================================================

The Crystallographic Defect Core Ontology (CDCO) is a domain ontology designed to provide a unified framework for representing and integrating data about crystallographic defects in materials science. CDCO defines common terminology for various types of defects, including vacancies, interstitials, dislocations, grain boundaries, and stacking faults, as well as their properties and relationships. The ontology supports semantic annotation of experimental and computational data, enabling interoperability, data integration, and advanced analysis across materials databases and research platforms. CDCO is designed for extensibility, allowing researchers to describe new defect types, characterization methods, and material systems. By providing a standardized vocabulary, CDCO facilitates cross-study comparison, defect modeling, and knowledge sharing in materials science. The ontology is actively maintained and extended to incorporate new concepts and requirements from the materials science community.

**Example Usage**:
Annotate a materials database with CDCO terms to specify the types of crystallographic defects present in a sample, their properties (e.g., density, energy), and relationships to material processing conditions, enabling semantic search and integration with defect modeling tools.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 85
        * - **Total Edges**
          - 123
        * - **Root Nodes**
          - 8
        * - **Leaf Nodes**
          - 53
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 7
        * - **Individuals**
          - 0
        * - **Properties**
          - 2

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
          - 0.11
        * - **Depth Variance**
          - 0.10
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 8
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 4.50
        * - **Breadth Variance**
          - 12.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 4
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CDCO

    ontology = CDCO()
    ontology.load("path/to/CDCO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
