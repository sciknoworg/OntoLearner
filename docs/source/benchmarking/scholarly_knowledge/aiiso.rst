

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

AIISO, the Academic Institution Internal Structure Ontology, is a specialized ontology for describing and formalizing the internal organizational structures, hierarchies, and administrative units of academic institutions, including universities, colleges, schools, departments, faculties, and research centers [#aiiso-vocab]_ [#aiiso-schema]_. It provides standardized classes and properties for representing academic organizational units, knowledge groupings, courses, modules, programmes, subjects, and their relationships within an institution's hierarchy [#aiiso-schema]_. AIISO is designed for integration with complementary vocabularies including Participation, FOAF, and AIISO Roles, enabling the description of people and the roles they play within academic institutions [#aiiso-vocab]_. The ontology supports semantic representation of academic organizational information, enabling institutional data integration, organizational mapping, academic resource description, and staff or student information systems [#aiiso-vocab]_ [#aiiso-schema]_. By providing standardized semantic definitions for academic structures, AIISO facilitates interoperability in academic information systems, institutional repositories, and linked open education data [#aiiso-vocab]_.

**Example Usage**: Represent an academic institution's structure with AIISO terms for faculties, departments, schools, research centers, programmes, courses, modules, and subjects, such as ``Faculty of Science``, ``Department of Computer Science``, and ``Artificial Intelligence Module``. This enables academic hierarchy modeling, semantic discovery, and integration across institutional information systems [#aiiso-schema]_.

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

References
----------

.. [#aiiso-vocab] Talis Information Ltd. 2008.
   "Academic Institution Internal Structure Ontology (AIISO)."
   Available at:
   `https://vocab.org/aiiso/ <https://vocab.org/aiiso/>`_

.. [#aiiso-schema] Talis Information Ltd. 2008.
   "Academic Institution Internal Structure Ontology Schema."
   Available at:
   `https://vocab.org/aiiso/schema-20080514.html <https://vocab.org/aiiso/schema-20080514.html>`_
