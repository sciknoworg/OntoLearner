

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

LODE (Linking Open Descriptions of Events) is an ontology for publishing and interlinking structured event descriptions as Linked Data. It provides lightweight classes and properties for representing events, their time and place, and simple relationships to agents and sources. LODE is intentionally minimalistic to maximize interoperability and ease of adoption: it models events as occurrences with temporal extents and locations, and supports linking to richer event models when needed. Typical use cases include event directories, cultural heritage timelines, news event annotation, and discovery services that aggregate event records from multiple data providers. LODE emphasizes stable URIs and practical tools for populating event descriptions, enabling the creation of a searchable event directory of historical and contemporary events.

**Example usage**: describe a public lecture as an lode:Event with a start/end time, a dcterms:spatial property linking to a Place URI, and a dc:source pointing to a news article; link the event to authority URIs for the speaker. The ontology's simplicity makes it a useful pivot for integrating event data across heterogeneous datasets.

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
