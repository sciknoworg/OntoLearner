.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Social Sciences
       * - **Category**
         - Social
       * - **Current Version**
         - 0.1
       * - **Last Updated**
         - 14 January 2014
       * - **Creator**
         - Dan Brickley, Libby Miller
       * - **License**
         - Creative Commons
       * - **Format**
         - rdf
       * - **Download**
         - `Download Friend of a Friend (FOAF) <http://xmlns.com/foaf/0.1/>`_

Friend of a Friend (FOAF)
========================================================================================================

FOAF (Friend of a Friend) is a widely adopted RDF vocabulary for describing people, their relationships, and the information that links them on the Web [#foaf-spec]_ [#foaf-bioportal]_. It provides a standardized vocabulary for representing personal profiles, social connections, organizations, projects, documents, online accounts, and other related entities [#foaf-spec]_. FOAF enables the creation of machine-readable social networks, supporting interoperability between personal websites, social platforms, linked data applications, and knowledge graphs [#foaf-spec]_. The vocabulary is designed for extensibility and can be used together with other RDF vocabularies and domain-specific ontologies to describe richer social and identity-related data [#foaf-spec]_. FOAF is used in digital identity management, social data publishing, semantic search, and knowledge graph construction to support data integration and discovery of social connections [#foaf-spec]_ [#foaf-bioportal]_. By providing a common framework for describing people, agents, and their relationships, FOAF facilitates linking people and information across the decentralized Web [#foaf-spec]_.

**Example Usage**:
Annotate a personal website or social network profile with FOAF terms to describe a person's name, email, homepage, friends, online accounts, and memberships in organizations, enabling semantic search and cross-platform social data integration [#foaf-spec]_ [#foaf-bioportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 168
        * - **Total Edges**
          - 504
        * - **Root Nodes**
          - 5
        * - **Leaf Nodes**
          - 87
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 15
        * - **Individuals**
          - 13
        * - **Properties**
          - 60

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.17
        * - **Depth Variance**
          - 0.14
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 5
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 3.00
        * - **Breadth Variance**
          - 4.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 13
        * - **Taxonomic Relations**
          - 11
        * - **Non-taxonomic Relations**
          - 21
        * - **Average Terms per Type**
          - 13.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import FOAF

    ontology = FOAF()
    ontology.load("path/to/FOAF-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#foaf-spec] Brickley, Dan, and Libby Miller. 2014.
   "FOAF Vocabulary Specification 0.99."
   Available at:
   `https://xmlns.com/foaf/spec/ <https://xmlns.com/foaf/spec/>`_

.. [#foaf-bioportal] NCBO BioPortal. 2019.
   "Friend of a Friend Vocabulary."
   Available at:
   `https://bioportal.bioontology.org/ontologies/FOAF <https://bioportal.bioontology.org/ontologies/FOAF>`_
