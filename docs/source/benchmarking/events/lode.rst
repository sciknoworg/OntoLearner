

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Events
       * - **Category**
         - Events
       * - **Current Version**
         - 2020-10-31
       * - **Last Updated**
         - 2020-10-31
       * - **Creator**
         - Ryan Shaw
       * - **License**
         - Creative Commons Attribution 3.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Linking Open Descriptions of Events (LODE) <https://linkedevents.org/ontology/>`_

Linking Open Descriptions of Events (LODE)
========================================================================================================

People conventionally refer to an action or occurrence taking place at a certain time     at a specific location as an event. This notion is potentially useful for connecting individual facts     recorded in the rapidly growing collection of linked data sets and for discovering more complex relationships     between data. The LODE provide an overview and comparison of existing event models,     looking at the different choices they make of how to represent events. It is a model for publishing records     of events as Linked Data. A tools for populating this model and a prototype “event directory” web service,     which can be used to locate stable URIs for events that have occurred,     provide RDFS+OWL descriptions and link to related resources.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 81
        * - **Total Edges**
          - 115
        * - **Root Nodes**
          - 7
        * - **Leaf Nodes**
          - 59
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1
        * - **Individuals**
          - 0
        * - **Properties**
          - 7

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 4
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.12
        * - **Depth Variance**
          - 1.37
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 19
        * - **Minimum Breadth**
          - 7
        * - **Average Breadth**
          - 12.00
        * - **Breadth Variance**
          - 25.60
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 4
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import LODE

    ontology = LODE()
    ontology.load("path/to/LODE-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
