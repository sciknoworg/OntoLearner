.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Industry
       * - **Category**
         - Automotive
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2021-03-01
       * - **Creator**
         - EDM Council
       * - **License**
         - MIT
       * - **Format**
         - rdf
       * - **Download**
         - `Download Automotive Ontology (AUTO) <https://github.com/edmcouncil/auto/tree/master>`_

Automotive Ontology (AUTO)
========================================================================================================

The Automotive Ontology (AUTO) is a comprehensive OWL ontology that defines shared conceptual structures and relationships in the automotive industry [#auto-edmc]_ [#auto-github]_. It provides a standardized semantic framework for representing automotive concepts and supporting interoperability across automotive data sources [#auto-edmc]_. AUTO is built upon the ``auto`` Schema.org extension created by the W3C Automotive Ontology Community Group [#auto-github]_. Its development process follows best practices established by the EDMC FIBO Community, supporting consistent ontology modeling and reusable conceptual design [#auto-github]_. The ontology supports integration of information from automotive manufacturers, suppliers, dealers, service providers, and other automotive data publishers [#auto-edmc]_ [#auto-github]_. By providing a common semantic framework, AUTO enables automotive data integration, knowledge sharing, semantic reasoning, and interoperability across the automotive ecosystem [#auto-edmc]_.

**Example Usage**:
Annotate a vehicle information system with AUTO terms to describe vehicle models, vehicle types, automotive characteristics, and related industry concepts, enabling integration with manufacturer databases, dealer websites, automotive knowledge graphs, and downstream analytics systems [#auto-edmc]_ [#auto-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 6344
        * - **Total Edges**
          - 17693
        * - **Root Nodes**
          - 417
        * - **Leaf Nodes**
          - 2589
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1372
        * - **Individuals**
          - 58
        * - **Properties**
          - 336

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 25
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.72
        * - **Depth Variance**
          - 17.16
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 574
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 116.38
        * - **Breadth Variance**
          - 20295.70
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 58
        * - **Taxonomic Relations**
          - 2731
        * - **Non-taxonomic Relations**
          - 42
        * - **Average Terms per Type**
          - 3.62
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AUTO

    ontology = AUTO()
    ontology.load("path/to/AUTO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#auto-edmc] EDM Council. n.d.
   "AUTO - Automotive."
   Available at:
   `https://edmcouncil.org/frameworks/industry-models/auto/ <https://edmcouncil.org/frameworks/industry-models/auto/>`_

.. [#auto-github] EDM Council. n.d.
   "Automotive Ontology (AUTO)."
   GitHub Repository.
   Available at:
   `https://github.com/edmcouncil/auto <https://github.com/edmcouncil/auto>`_
