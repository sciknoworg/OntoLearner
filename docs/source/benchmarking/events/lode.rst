

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

LODE (Linking Open Descriptions of Events) is an ontology for
publishing and interlinking structured event descriptions as Linked
Data [#lode-paper]_ [#lode-site]_. It provides lightweight classes and
properties for representing events, their time and place, and simple
relationships to agents and sources [#lode-paper]_ [#lode-site]_.
LODE is intentionally minimalistic in order to maximize
interoperability and ease of adoption, modeling events as occurrences
with temporal extents and locations while supporting links to richer
event models when needed [#lode-paper]_ [#lode-site]_. Typical use
cases include event directories, cultural heritage timelines, news
event annotation, and discovery services that aggregate event records
from multiple data providers [#lode-paper]_ [#lode-site]_. By
providing a lightweight and stable semantic framework for event
descriptions, LODE supports semantic integration, search, and reuse of
event data across heterogeneous datasets [#lode-paper]_ [#lode-site]_.

**Example Usage**: Describe a public lecture as a ``lode:Event`` with
a start and end time, a ``dcterms:spatial`` property linking to a place
URI, and a ``dc:source`` pointing to a news article, while linking the
event to authority URIs for the speaker. The ontology’s simplicity
makes it a useful pivot for integrating event data across heterogeneous
datasets [#lode-paper]_ [#lode-site]_.

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

References
----------

.. [#lode-paper] Shaw, R., Troncy, R., and Hardman, L. 2009.
   "LODE: Linking Open Descriptions of Events."
   In *The Semantic Web: Research and Applications*, pp. 153-167.
   doi:10.1007/978-3-642-02121-3_11
   Available at:
   `https://link.springer.com/chapter/10.1007/978-3-642-02121-3_11 <https://link.springer.com/chapter/10.1007/978-3-642-02121-3_11>`_

.. [#lode-site] Linked Events. n.d. "LODE Ontology Specification."
   Available at:
   `https://linkedevents.org/ontology/ <https://linkedevents.org/ontology/>`_
