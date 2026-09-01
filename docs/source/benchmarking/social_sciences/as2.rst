.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Social Sciences
       * - **Category**
         - Social
       * - **Current Version**
         - 2.0
       * - **Last Updated**
         - 23 May 2017
       * - **Creator**
         - None
       * - **License**
         - W3C Document License
       * - **Format**
         - ttl
       * - **Download**
         - `Download Activity Streams 2.0 Ontology (AS2) <https://github.com/w3c/activitystreams?tab=License-1-ov-file#readme>`_

Activity Streams 2.0 Ontology (AS2)
========================================================================================================

The Activity Streams 2.0 Ontology (AS2) is a W3C standard vocabulary and syntax for describing social activities, actions, interactions, and content on the Web [#as2-core]_ [#as2-github]_. It provides a set of classes and properties for modeling activities such as posting, liking, sharing, following, creating, updating, and deleting, as well as the actors, objects, targets, collections, and links involved in those activities [#as2-core]_. AS2 enables interoperability between social networking platforms, federated social web applications, content syndication systems, and activity tracking systems by providing a common semantic framework for representing activity data [#as2-core]_ [#as2-github]_. The vocabulary supports extensibility, allowing developers to use additional vocabularies or define specialized activity types and properties for domain-specific use cases [#as2-core]_. AS2 is used in decentralized social web systems and social data exchange, enabling rich representation, publication, aggregation, and analysis of activity streams across platforms [#as2-core]_ [#as2-github]_. By standardizing the description of social actions and their related entities, AS2 facilitates data integration, interoperability, and machine-readable exchange of social activity information [#as2-core]_.

**Example Usage**:
Annotate a social networking application with AS2 terms to describe user activities such as posting a status update, liking a photo, following another user, or sharing content. This enables interoperability with other platforms, federated social web applications, and activity stream consumers [#as2-core]_ [#as2-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 426
        * - **Total Edges**
          - 945
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 120
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 107
        * - **Individuals**
          - 1
        * - **Properties**
          - 69

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 0
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.00
        * - **Depth Variance**
          - 0.00
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 0
        * - **Minimum Breadth**
          - 0
        * - **Average Breadth**
          - 0.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1
        * - **Taxonomic Relations**
          - 55
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AS2

    ontology = AS2()
    ontology.load("path/to/AS2-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#as2-core] W3C. 2017.
   "Activity Streams 2.0."
   W3C Recommendation.
   Available at:
   `https://www.w3.org/TR/activitystreams-core/ <https://www.w3.org/TR/activitystreams-core/>`_

.. [#as2-github] W3C. n.d.
   "Activity Streams 2.0."
   GitHub Repository.
   Available at:
   `https://github.com/w3c/activitystreams <https://github.com/w3c/activitystreams>`_
