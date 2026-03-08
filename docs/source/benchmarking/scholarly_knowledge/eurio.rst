.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Research Information
       * - **Current Version**
         - 2.4
       * - **Last Updated**
         - 2023-10-19
       * - **Creator**
         - Publications Office of the European Commission
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download EUropean Research Information Ontology (EURIO) <https://op.europa.eu/de/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurio>`_

EUropean Research Information Ontology (EURIO)
========================================================================================================

The EUropean Research Information Ontology (EURIO) conceptualizes, formally encodes, and makes available in an open, structured, and machine-readable format data about research projects funded by the EU's framework programmes for research and innovation. It provides a structured vocabulary for representing research projects, funding information, and related data, supporting both theoretical and experimental research in research information management.

The ontology employs a class-based modeling approach, defining classes for different types of research projects, funding information, and related data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. EURIO supports the integration of data from various sources, promoting interoperability and data-driven research in research information management.

Typical applications of EURIO include the development of new research information management methods, the optimization of research project management practices, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, EURIO enhances collaboration and innovation in the field of research information management.

**Example Usage**:
Annotate a research project with EURIO terms to specify project types, funding information, and related data, enabling semantic search and integration with research information management platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 502
        * - **Total Edges**
          - 1193
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 204
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 44
        * - **Individuals**
          - 0
        * - **Properties**
          - 111

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
          - 6.54
        * - **Depth Variance**
          - 11.75
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 56
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 24.73
        * - **Breadth Variance**
          - 192.33
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 43
        * - **Non-taxonomic Relations**
          - 4
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EURIO

    ontology = EURIO()
    ontology.load("path/to/EURIO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
