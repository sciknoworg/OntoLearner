.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Administration
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - David Shotton
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Funding, Research Administration and Projects Ontology (FRAPO) <http://www.sparontologies.net/ontologies/frapo>`_

Funding, Research Administration and Projects Ontology (FRAPO)
========================================================================================================

The Funding, Research Administration and Projects Ontology (FRAPO) is an ontology for describing administrative information relating to grant funding and research projects [#frapo-spar]_ [#frapo-github]_. It provides a structured vocabulary for representing grant applications, funding bodies, research projects, project partners, project-related roles, and other administrative information commonly managed in Current Research Information Systems (CRIS) [#frapo-spar]_. FRAPO is CERIF-compliant and written in OWL 2 DL, making it suitable for representing research administration information in semantic web and linked data environments [#frapo-github]_.

The ontology defines classes and properties for modeling funding, project administration, organizations, agents, and project-related relationships [#frapo-spar]_. It imports FOAF and is designed to work with related SPAR ontologies such as SCoRO for scholarly roles and FaBiO for documents such as grant applications, project plans, project reports, datasets, and journal articles [#frapo-spar]_. This allows FRAPO to represent research administration metadata while linking it to people, organizations, roles, outputs, and related documents [#frapo-spar]_.

Typical applications of FRAPO include research information management, grant administration, project reporting, Current Research Information Systems, funding analysis, institutional reporting, and integration of research project metadata across repositories and administrative systems [#frapo-spar]_ [#frapo-github]_. By providing a standardized semantic framework, FRAPO enhances interoperability, data integration, and knowledge discovery in research administration and project management contexts [#frapo-github]_.

**Example Usage**:
Annotate a research project with FRAPO terms to specify the funding body, grant application, project partners, administrative roles, project status, and related project documents. This enables semantic search, grant tracking, institutional reporting, and integration with research administration platforms and CRIS systems [#frapo-spar]_ [#frapo-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 539
        * - **Total Edges**
          - 1076
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 274
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 97
        * - **Individuals**
          - 25
        * - **Properties**
          - 125

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.68
        * - **Depth Variance**
          - 1.08
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 18
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 7.00
        * - **Breadth Variance**
          - 40.50
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 25
        * - **Taxonomic Relations**
          - 82
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 8.33
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import FRAPO

    ontology = FRAPO()
    ontology.load("path/to/FRAPO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#frapo-spar] SPAR Ontologies. n.d.
   "FRAPO, the Funding, Research Administration and Projects Ontology."
   Available at:
   `https://sparontologies.github.io/frapo/current/frapo.html <https://sparontologies.github.io/frapo/current/frapo.html>`_

.. [#frapo-github] SPAR Ontologies. n.d.
   "Funding, Research Administration and Projects Ontology (FRAPO)."
   GitHub Repository.
   Available at:
   `https://github.com/sparontologies/frapo <https://github.com/sparontologies/frapo>`_
