

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

The Sport Ontology is a simple lightweight ontology for publishing data about competitive sports events.     The terms in this ontology allow data to be published about:     The structure of sports tournaments as a series of eventsThe competing of agents in a competitionThe type     of discipline a event involvesThe award associated with the competition and how received it...etc     Whilst it originates in a specific BBC use case, the Sport Ontology should be applicable     to a wide range of competitive sporting events data publishing use cases.     Care has been taken to try and ensure interoperability with more general ontologies in use.     In particular, it draws heavily upon the events ontology.

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
