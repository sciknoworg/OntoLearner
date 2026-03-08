

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Events
       * - **Category**
         - Conferences
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2016/04/30
       * - **Creator**
         - Aldo Gangemi et al.
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Conference Ontology (Conference) <http://www.scholarlydata.org/ontology/conference-ontology.owl>`_

Conference Ontology (Conference)
========================================================================================================

The Conference Ontology is a self-contained ontology for modeling conferences, workshops, and related scholarly events. It captures core entities (events, organizers, venues, sessions, papers, posters, and participants) and their relationships, allowing structured representation of program schedules, affiliations, and scholarly communications around conferences. Designed following ontology design patterns and reuse principles, it reuses established vocabularies (e.g., FOAF, BIBO, schema.org) where appropriate and interlinks with the SWC (Semantic Web Conference) ontology to ensure interoperability. The ontology models temporal and spatial aspects (start/end times, room assignments), roles and responsibilities (chairs, speakers, reviewers), and provenance metadata (submission dates, acceptance decisions). Typical applications include conference management systems, semantic search of proceedings, program generation, and linking publications to presentation metadata.

**Example usage**: represent a conference session as an Event with start/end times, linked to a Room (Venue), containing multiple Talk instances each linked to Speaker agents and associated Paper resources. The ontology supports export to RDF/OWL and integration with digital libraries, repositories, and research discovery services.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 243
        * - **Total Edges**
          - 652
        * - **Root Nodes**
          - 8
        * - **Leaf Nodes**
          - 61
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 42
        * - **Individuals**
          - 32
        * - **Properties**
          - 52

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
          - 4.60
        * - **Depth Variance**
          - 6.67
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 25
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 12.42
        * - **Breadth Variance**
          - 49.74
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 32
        * - **Taxonomic Relations**
          - 49
        * - **Non-taxonomic Relations**
          - 3
        * - **Average Terms per Type**
          - 10.67
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Conference

    ontology = Conference()
    ontology.load("path/to/Conference-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
