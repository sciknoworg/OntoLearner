

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Arts and Humanities
       * - **Category**
         - Numismatics
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2025-01-22
       * - **Creator**
         - American Numismatic Society, Institute for the Study of the Ancient World
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Nomisma Ontology (Nomisma) <https://www.dainst.org/forschung/projekte/noslug/2098>`_

Nomisma Ontology (Nomisma)
========================================================================================================

The Nomisma Ontology is a collaborative project that provides stable, standardized digital representations of numismatic concepts following the principles of Linked Open Data. It offers HTTP URIs that provide persistent access to information about numismatic entities in multiple formats, enabling seamless integration with other linked open data resources. Developed collaboratively by the American Numismatic Society and the Institute for the Study of the Ancient World at New York University, Nomisma represents a comprehensive framework for describing coins, denominations, mints, rulers, and monetary systems across different periods and cultures. The ontology facilitates semantic annotation of numismatic data, supporting interoperability across digital coin collections, archaeological databases, and historical research platforms. It enables advanced querying and analysis capabilities for numismatists, archaeologists, and historians seeking to understand monetary systems and economic aspects of historical societies. The ontology integrates with broader cultural heritage and historical linked data ecosystems, supporting cross-domain research on ancient economies, trade networks, and political history. By providing standardized semantic representations, Nomisma enhances discoverability and reusability of numismatic data in the global digital humanities and cultural heritage communities.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 245
        * - **Total Edges**
          - 431
        * - **Root Nodes**
          - 22
        * - **Leaf Nodes**
          - 113
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 36
        * - **Individuals**
          - 0
        * - **Properties**
          - 71

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
          - 0.97
        * - **Depth Variance**
          - 0.73
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 22
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 15.00
        * - **Breadth Variance**
          - 67.50
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 13
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Nomisma

    ontology = Nomisma()
    ontology.load("path/to/Nomisma-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
