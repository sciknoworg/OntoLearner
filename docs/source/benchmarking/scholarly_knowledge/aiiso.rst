

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Academic Institution
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2008-05-14
       * - **Creator**
         - Open University
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Academic Institution Internal Structure Ontology (AIISO) <https://vocab.org/aiiso/>`_

Academic Institution Internal Structure Ontology (AIISO)
========================================================================================================

AIISO is a specialized ontology for describing and formalizing the internal organizational structures, hierarchies, and administrative units of academic institutions including universities, colleges, and research centers. It provides standardized vocabulary for representing academic departments, faculties, schools, research groups, and their relationships within an institution's organizational hierarchy. AIISO is designed for integration with complementary ontologies including Participation (for describing role participation), FOAF (for person information), and aiiso-roles (for person roles within institutions). The ontology enables semantic representation of academic organizational information, supporting institutional data integration, organizational mapping, and staff/student management systems. AIISO facilitates interoperability in academic information systems and institutional repositories by providing standardized semantic definitions of academic structures.

**Example Usage**: Represent an academic institution's structure with AIISO terms for faculties (Faculty of Science, Faculty of Engineering), departments (Computer Science Department, Physics Department), research groups, and their organizational relationships and hierarchies.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 119
        * - **Total Edges**
          - 247
        * - **Root Nodes**
          - 8
        * - **Leaf Nodes**
          - 54
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 22
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.89
        * - **Depth Variance**
          - 0.47
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 9.00
        * - **Breadth Variance**
          - 14.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 13
        * - **Non-taxonomic Relations**
          - 3
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AIISO

    ontology = AIISO()
    ontology.load("path/to/AIISO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
