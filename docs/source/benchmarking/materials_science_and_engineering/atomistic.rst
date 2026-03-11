.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.0.2
       * - **Last Updated**
         - None
       * - **Creator**
         - Francesca L. Bleken, Jesper Friis
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Atomistic Ontology (Atomistic) <https://github.com/emmo-repo/domain-atomistic>`_

Atomistic Ontology (Atomistic)
========================================================================================================

The Atomistic Ontology is an EMMO-based domain ontology designed for atomistic and electronic modeling in materials science. It provides a structured vocabulary for representing atomic-scale structures, electronic properties, and simulation methods. The ontology supports semantic annotation of computational models, enabling interoperability and data integration across materials modeling platforms. Atomistic Ontology facilitates detailed description of atomic configurations, electronic states, and interactions, supporting advanced materials design and analysis. The ontology is actively maintained and extended to incorporate new modeling techniques and scientific findings. By providing a standardized framework, Atomistic Ontology enhances reproducibility, data sharing, and collaborative research in atomistic simulations.

**Example Usage**:
Annotate a computational materials science dataset with Atomistic Ontology terms to specify atomic structures, electronic properties, and simulation parameters, enabling semantic search and integration with modeling tools.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 93
        * - **Total Edges**
          - 107
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 70
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 12
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
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.80
        * - **Depth Variance**
          - 2.27
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 44
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 13.29
        * - **Breadth Variance**
          - 182.78
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Atomistic

    ontology = Atomistic()
    ontology.load("path/to/Atomistic-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
