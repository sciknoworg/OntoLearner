.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Research Information
       * - **Current Version**
         - 2.4
       * - **Last Updated**
         - 2023-10-19
       * - **Creator**
         - Publications Office of the European Commission
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download EUropean Research Information Ontology (EURIO) <https://op.europa.eu/de/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurio>`_

EUropean Research Information Ontology (EURIO)
========================================================================================================

The EUropean Research Information Ontology (EURIO) conceptualizes, formally encodes, and makes available data about research projects funded by the European Union's framework programmes for research and innovation in an open, structured, and machine-readable format [#eurio-euvoc]_ [#eurio-paper]_. EURIO was developed for CORDIS and the Publications Office of the European Union to represent research project information as semantic data, improving its visibility, accessibility, interoperability, and reuse [#eurio-paper]_. It provides a structured vocabulary for describing research projects, funding schemes, grants, organizations, persons, project results, publications, and related research information [#eurio-euvoc]_ [#eurio-paper]_.

The ontology uses a class-based semantic modeling approach, defining classes and properties for research projects, participants, funding information, outputs, and administrative metadata [#eurio-paper]_. These concepts allow EU-funded research information to be organized, linked, queried, and integrated with other semantic resources and reference data assets [#eurio-euvoc]_ [#eurio-paper]_. EURIO supports interoperability in research information management by enabling project data from CORDIS and related sources to be represented consistently in linked data formats [#eurio-euvoc]_.

Typical applications of EURIO include semantic publication of EU research project data, research information management, project discovery, funding analysis, institutional reporting, knowledge graph construction, and integration of research outputs across platforms [#eurio-paper]_. By providing a standardized ontology for EU-funded research information, EURIO supports data discovery, analytics, interoperability, and knowledge sharing across research information systems [#eurio-euvoc]_ [#eurio-paper]_.

**Example Usage**:
Annotate an EU-funded research project with EURIO terms to specify the project title, acronym, grant information, funding programme, participating organizations, researchers, project duration, deliverables, publications, and related results. This enables semantic search, project discovery, funding analysis, and integration with research information management platforms [#eurio-euvoc]_ [#eurio-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 502
        * - **Total Edges**
          - 1193
        * - **Root Nodes**
          - 18
        * - **Leaf Nodes**
          - 204
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 44
        * - **Individuals**
          - 0
        * - **Properties**
          - 111

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 14
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 6.54
        * - **Depth Variance**
          - 11.75
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 56
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 24.73
        * - **Breadth Variance**
          - 192.33
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 43
        * - **Non-taxonomic Relations**
          - 4
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EURIO

    ontology = EURIO()
    ontology.load("path/to/EURIO-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#eurio-euvoc] Publications Office of the European Union. n.d.
   "EUropean Research Information Ontology (EURIO)."
   Available at:
   `https://op.europa.eu/en/web/eu-vocabularies/eurio <https://op.europa.eu/en/web/eu-vocabularies/eurio>`_

.. [#eurio-paper] Publications Office of the European Union. 2020.
   "EURIO: an ontology for publishing research projects' data."
   Available at:
   `https://publications.europa.eu/resource/cellar/369859bb-3611-11eb-b27b-01aa75ed71a1.0001.01/DOC_1 <https://publications.europa.eu/resource/cellar/369859bb-3611-11eb-b27b-01aa75ed71a1.0001.01/DOC_1>`_
