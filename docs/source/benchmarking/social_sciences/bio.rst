.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Social Sciences
       * - **Category**
         - Biographical Information
       * - **Current Version**
         - 0.1
       * - **Last Updated**
         - 2010-05-10
       * - **Creator**
         - Ian Davis and David Galbraith
       * - **License**
         - Public Domain
       * - **Format**
         - rdf
       * - **Download**
         - `Download BIO: A vocabulary for biographical information (BIO) <https://vocab.org/bio/>`_

BIO: A vocabulary for biographical information (BIO)
========================================================================================================

The BIO vocabulary is a domain vocabulary for describing biographical information about people, their backgrounds, and genealogical relationships [#bio-vocab]_ [#bio-github]_. It models a person's life as a series of interconnected key events, such as birth, marriage, employment, and death, around which additional biographical and genealogical information can be organized [#bio-vocab]_. BIO defines an event-centric approach, supplying a set of core event types and properties that are person-centric, making it suitable for representing life histories, family trees, career trajectories, and historical biographies [#bio-vocab]_ [#bio-github]_. The vocabulary is designed for extensibility, allowing other vocabularies to build upon its event framework for specialized use cases [#bio-vocab]_. BIO can be used in digital humanities, genealogy platforms, library metadata, and social history research to support semantic annotation, data integration, and structured queries over biographical datasets [#bio-vocab]_. By providing a standardized vocabulary for biographical events, BIO facilitates interoperability and knowledge sharing across biographical and genealogical information systems [#bio-github]_.

**Example Usage**:
Annotate a genealogy database with BIO terms to describe a person's birth, marriage, employment, and death events, linking them to dates, places, and related individuals for semantic search, family history visualization, and biographical data integration [#bio-vocab]_ [#bio-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 326
        * - **Total Edges**
          - 816
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 187
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 44
        * - **Individuals**
          - 1
        * - **Properties**
          - 30

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.24
        * - **Depth Variance**
          - 5.64
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 30
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 8.75
        * - **Breadth Variance**
          - 88.44
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1
        * - **Taxonomic Relations**
          - 58
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BIO

    ontology = BIO()
    ontology.load("path/to/BIO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bio-vocab] Davis, Ian, and David Galbraith. n.d.
   "BIO: A vocabulary for biographical information."
   Available at:
   `https://vocab.org/bio/ <https://vocab.org/bio/>`_

.. [#bio-github] Davis, Ian. n.d.
   "BIO Vocabulary."
   GitHub Repository.
   Available at:
   `https://github.com/iand/vocab-bio <https://github.com/iand/vocab-bio>`_
