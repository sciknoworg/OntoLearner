.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Sport
       * - **Current Version**
         - 3.2
       * - **Last Updated**
         - None
       * - **Creator**
         - https://uk.linkedin.com/pub/jem-rayfield/27/b19/757, https://uk.linkedin.com/in/paulwilton, https://www.blockslabpillar.com, https://www.linkedin.com/in/tfgrahame, https://uk.linkedin.com/pub/stuart-williams/8/684/351, https://uk.linkedin.com/in/brianwmcbride
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Sport Ontology (BBCSport) <https://www.bbc.co.uk/ontologies/sport-ontology>`_

BBC Sport Ontology (BBCSport)
========================================================================================================

The BBC Sport Ontology (BBCSport) is a lightweight ontology designed to represent competitive sports events, tournaments, participants, disciplines, and awards. It provides a structured vocabulary for describing the structure of sports tournaments as a series of events, the participation of agents (teams, athletes), the type of discipline involved, and the awards associated with competitions. BBCSport is designed for interoperability with general event ontologies and supports semantic annotation of sports data for publishing, search, and analytics. The ontology enables integration of sports data across platforms, facilitating advanced queries, personalized recommendations, and automated content generation for sports journalism. BBCSport is extensible and can be adapted to a wide range of sports and event types, supporting both professional and amateur competitions. The ontology is maintained as an open resource and is compatible with other BBC and external ontologies for broader data integration.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 232
        * - **Total Edges**
          - 490
        * - **Root Nodes**
          - 42
        * - **Leaf Nodes**
          - 115
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 28
        * - **Individuals**
          - 40
        * - **Properties**
          - 47

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
          - 1.07
        * - **Depth Variance**
          - 1.50
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 42
        * - **Minimum Breadth**
          - 10
        * - **Average Breadth**
          - 21.25
        * - **Breadth Variance**
          - 153.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 40
        * - **Taxonomic Relations**
          - 25
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 13.33
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCSport

    ontology = BBCSport()
    ontology.load("path/to/BBCSport-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

**Example Usage**:
Annotate a sports tournament database with BBCSport terms to specify the structure of the tournament, participating teams and athletes, event types (e.g., "final match"), and awards (e.g., "gold medal"), enabling semantic search and cross-platform sports analytics.
