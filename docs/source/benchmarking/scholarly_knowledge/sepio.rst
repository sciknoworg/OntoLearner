.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scientific Evidence
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2015-02-23
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Scientific Evidence and Provenance Information Ontology (SEPIO) <https://terminology.tib.eu/ts/ontologies/SEPIO>`_

Scientific Evidence and Provenance Information Ontology (SEPIO)
========================================================================================================

The Scientific Evidence and Provenance Information Ontology (SEPIO) is in its early stages of development, undergoing iterative refinement as new requirements emerge and alignment with existing standards is explored. SEPIO provides a structured vocabulary for representing scientific evidence, provenance, and related data, supporting both theoretical and experimental research in scientific evidence and provenance.

The ontology employs a class-based modeling approach, defining classes for different types of scientific evidence, provenance, and related data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. SEPIO supports the integration of data from various sources, promoting interoperability and data-driven research in scientific evidence and provenance.

Typical applications of SEPIO include the development of new scientific evidence and provenance representation methods, the optimization of scientific evidence management practices, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, SEPIO enhances collaboration and innovation in the field of scientific evidence and provenance.

**Example Usage**:
Annotate a scientific study with SEPIO terms to specify scientific evidence, provenance, and related data, enabling semantic search and integration with scientific evidence and provenance platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1262
        * - **Total Edges**
          - 2385
        * - **Root Nodes**
          - 72
        * - **Leaf Nodes**
          - 781
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 129
        * - **Individuals**
          - 21
        * - **Properties**
          - 117

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 14
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.17
        * - **Depth Variance**
          - 8.36
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 170
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 40.60
        * - **Breadth Variance**
          - 2186.24
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 21
        * - **Taxonomic Relations**
          - 141
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 4.20
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SEPIO

    ontology = SEPIO()
    ontology.load("path/to/SEPIO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
