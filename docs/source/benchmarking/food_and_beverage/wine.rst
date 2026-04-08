

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Food and Beverage
       * - **Category**
         - Wine
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - rdf
       * - **Download**
         - `Download Wine Ontology (Wine) <https://github.com/UCDavisLibrary/wine-ontology>`_

Wine Ontology (Wine)
========================================================================================================

The Wine Ontology is an RDF-based vocabulary for describing wines and
related wine domain concepts in a structured and machine-readable way
[#wine-w3c]_ [#wine-repo]_. It provides a classification framework for
different types of wines, grape varieties, wine regions, wineries, and
wine characteristics, supporting semantic representation of wine
products and their attributes [#wine-w3c]_ [#wine-repo]_. As a well-known
example ontology in the Semantic Web community, it has been used to
illustrate ontology modeling patterns and reasoning over class-based
descriptions [#wine-w3c]_. The ontology can support applications such
as semantic data integration, structured search, recommendation, and
knowledge representation in domains involving wine, food, and related
commercial or cultural information [#wine-repo]_ [#wine-w3c]_.

**Example Usage**: Describe a specific wine by linking it to its grape
variety, wine region, producer, vintage year, and taste-related
characteristics through ontology properties, enabling structured search,
comparison, and semantic integration of wine-related information
[#wine-repo]_ [#wine-w3c]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 729
        * - **Total Edges**
          - 1816
        * - **Root Nodes**
          - 84
        * - **Leaf Nodes**
          - 22
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 101
        * - **Individuals**
          - 161
        * - **Properties**
          - 13

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 41
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.51
        * - **Depth Variance**
          - 29.20
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 164
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 17.19
        * - **Breadth Variance**
          - 1612.73
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 161
        * - **Taxonomic Relations**
          - 47
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 4.13
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Wine

    ontology = Wine()
    ontology.load("path/to/Wine-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#wine-w3c] McGuinness, D. L., and van Harmelen, F. 2004.
   "OWL Web Ontology Language Guide."
   W3C Recommendation, 10 February 2004.
   Available at:
   `https://www.w3.org/TR/owl-guide/ <https://www.w3.org/TR/owl-guide/>`_

.. [#wine-repo] UC Davis Library. n.d. "Wine Linked Data / Wine Ontology."
   Available at:
   `https://github.com/UCDavisLibrary/wine-ontology <https://github.com/UCDavisLibrary/wine-ontology>`_
