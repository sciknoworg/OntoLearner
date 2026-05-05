


.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Library and Cultural Heritage
       * - **Category**
         - Authority Files
       * - **Current Version**
         - 1.2.0
       * - **Last Updated**
         - 2024-08-26
       * - **Creator**
         - Alexander Haffner
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Gemeinsame Normdatei (GND) <https://d-nb.info/standards/elementset/gnd>`_

Gemeinsame Normdatei (GND)
========================================================================================================

The Gemeinsame Normdatei (GND, Integrated Authority File) is a comprehensive semantic vocabulary and linked data resource developed by the German library and information community for describing and disambiguating authority data [#gnd-dnb]_ [#gnd-ontology]_. GND provides standardized, machine-readable descriptions of entities such as persons, corporate bodies, conferences and events, geographic entities, topics, and works relating to cultural and academic collections [#gnd-dnb]_. The GND Ontology defines RDF classes and relations used to describe Integrated Authority File data in RDF format, enabling authority data to be represented in semantic web and linked data environments [#gnd-ontology]_. GND offers rich properties and relationships for describing names, biographical information, organizational relationships, geographic entities, subject authorities, and links to related resources [#gnd-ontology]_. It is widely used by libraries and is increasingly relevant for archives, museums, and cultural heritage institutions for authority control, entity identification, and semantic data linking [#gnd-dnb]_. The vocabulary supports integration with broader linked data ecosystems by enabling GND entities to be linked with other authority files and external knowledge resources [#gnd-ontology]_.

**Example Usage**: Link a library catalog record to GND authority entries for the author as a person, the publisher as a corporate body, and subject headings as topic authorities. This enables semantic discovery, entity disambiguation, and cross-institutional linking across German and international library systems [#gnd-dnb]_ [#gnd-ontology]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2100
        * - **Total Edges**
          - 4128
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 1008
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 247
        * - **Individuals**
          - 0
        * - **Properties**
          - 236

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
          - 0
        * - **Taxonomic Relations**
          - 70
        * - **Non-taxonomic Relations**
          - 3
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GND

    ontology = GND()
    ontology.load("path/to/GND-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#gnd-dnb] German National Library. n.d.
   "The Integrated Authority File (GND)."
   Available at:
   `https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html <https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html>`_

.. [#gnd-ontology] German National Library. n.d.
   "RDF Vocabularies: GND Ontology."
   Available at:
   `https://www.dnb.de/EN/Professionell/Metadatendienste/Exportformate/RDF-Vokabulare/rdf_node.html <https://www.dnb.de/EN/Professionell/Metadatendienste/Exportformate/RDF-Vokabulare/rdf_node.html>`_
