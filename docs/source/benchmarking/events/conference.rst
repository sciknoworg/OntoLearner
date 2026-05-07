

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

The Conference Ontology is a self-contained ontology for modeling
conferences, workshops, and related scholarly events
[#conference-onto]_ [#conference-paper]_. It captures core entities
such as events, organizers, venues, sessions, papers, posters, and
participants, together with their relationships, enabling structured
representation of program schedules, affiliations, and scholarly
communications around conferences [#conference-onto]_
[#conference-paper]_. Designed following ontology design patterns and
reuse principles, it reuses established vocabularies where appropriate
and interlinks with the Semantic Web Conference ontology to support
interoperability [#conference-paper]_ [#conference-onto]_. The ontology
models temporal and spatial aspects, roles and responsibilities, and
provenance-related information relevant to conference organization and
scholarly communication [#conference-onto]_ [#conference-paper]_. It
supports applications such as conference management systems, semantic
search of proceedings, program generation, and linking publications to
presentation metadata [#conference-onto]_ [#conference-paper]_.

**Example Usage**: Represent a conference session as an event with
start and end times, linked to a room or venue, and containing multiple
talk instances that are connected to speaker agents and associated
paper resources, enabling RDF/OWL-based integration with digital
libraries, repositories, and research discovery services
[#conference-onto]_ [#conference-paper]_.

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

References
----------

.. [#conference-onto] scholarlydata.org. n.d. "The Conference Ontology."
   Available at:
   `https://www.scholarlydata.org/ontology/doc/ <https://www.scholarlydata.org/ontology/doc/>`_

.. [#conference-paper] Nuzzolese, A. G., Gentile, A. L.,
   Presutti, V., and Gangemi, A. 2016.
   "Semantic Web Conference Ontology - A Refactoring Solution."
   In *The Semantic Web: ESWC 2016 Satellite Events*,
   Lecture Notes in Computer Science 9989, pp. 84-87.
   doi:10.1007/978-3-319-47602-5_18
