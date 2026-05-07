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

The BBC Sport Ontology (BBCSport) is a simple, lightweight ontology for publishing data about competitive sports events [#bbcsport-ontology]_. It provides a structured vocabulary for representing the structure of sports tournaments as a series of events, the competing of agents in a competition, the type of discipline involved in an event, and awards associated with competitions [#bbcsport-ontology]_.

BBCSport is designed for interoperability with more general event ontologies and draws heavily on the Events Ontology [#bbcsport-ontology]_. Although it originates from a BBC use case, it is intended to be applicable to a wide range of competitive sports event data publishing use cases [#bbcsport-ontology]_. By providing standardized terms for competitions, events, participants, disciplines, and awards, BBCSport supports semantic annotation, linked-data publishing, content discovery, and integration of sports information [#bbcsport-ontology]_.

**Example Usage**:
Annotate a sports tournament database with BBCSport terms to specify competitions, tournament events, participating teams or athletes, disciplines, and awards, enabling semantic search and integration across sports data publishing platforms [#bbcsport-ontology]_.

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

References
----------

.. [#bbcsport-ontology] BBC. n.d.
   "Sport Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/sport.html <https://iptc.org/thirdparty/bbc-ontologies/sport.html>`_
