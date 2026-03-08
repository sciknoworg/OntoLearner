.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scientific Observation
       * - **Current Version**
         - 1.2
       * - **Last Updated**
         - None
       * - **Creator**
         - The Regents of the University of California
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Extensible Observation Ontology (OBOE) <https://terminology.tib.eu/ts/ontologies/OBOE>`_

Extensible Observation Ontology (OBOE)
========================================================================================================

The Extensible Observation Ontology (OBOE) is a formal ontology for capturing the semantics of scientific observation and measurement. The ontology supports researchers to add detailed semantic annotations to scientific data, thereby clarifying the inherent meaning of scientific observations. It provides a structured vocabulary for representing scientific observations, measurements, and related data, supporting both theoretical and experimental research in scientific observation.

The ontology employs a class-based modeling approach, defining classes for different types of observations, measurements, and related data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. OBOE supports the integration of data from various sources, promoting interoperability and data-driven research in scientific observation.

Typical applications of OBOE include the development of new observation and measurement methods, the optimization of scientific observation practices, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, OBOE enhances collaboration and innovation in the field of scientific observation.

**Example Usage**:
Annotate a scientific observation dataset with OBOE terms to specify observation types, measurements, and related data, enabling semantic search and integration with scientific observation platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1868
        * - **Total Edges**
          - 5017
        * - **Root Nodes**
          - 169
        * - **Leaf Nodes**
          - 156
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 478
        * - **Individuals**
          - 0
        * - **Properties**
          - 30

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 11
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.96
        * - **Depth Variance**
          - 4.93
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 480
        * - **Minimum Breadth**
          - 6
        * - **Average Breadth**
          - 153.33
        * - **Breadth Variance**
          - 18183.39
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 819
        * - **Non-taxonomic Relations**
          - 60
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OBOE

    ontology = OBOE()
    ontology.load("path/to/OBOE-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
