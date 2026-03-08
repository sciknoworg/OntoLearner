

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Arts and Humanities
       * - **Category**
         - Music Theory
       * - **Current Version**
         - 2.1.5
       * - **Last Updated**
         - 2013/07/22
       * - **Creator**
         - Knowledge Media Institute, Open University
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Music Ontology (MusicOntology) <https://github.com/motools/musicontology>`_

Music Ontology (MusicOntology)
========================================================================================================

The Music Ontology Specification provides a comprehensive framework for describing music and related entities on the Semantic Web. It defines core concepts and properties for representing artists, albums, tracks, performances, and musical relationships. The ontology enables standardized music metadata annotation, facilitating interoperability across music information systems, streaming platforms, and digital libraries. It supports rich description of musical works including production details, distribution information, and artistic collaborations. The Music Ontology integrates with other semantic web vocabularies and allows linking of music resources with external datasets and knowledge bases. It enables music recommendation systems, search engines, and music discovery applications to leverage structured semantic data. The ontology supports various music-related use cases including discography management, performance tracking, playlist creation, and music history documentation. By providing a common framework for music representation, the Music Ontology facilitates semantic data integration across the music industry and enables advanced music information retrieval and analysis capabilities.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 662
        * - **Total Edges**
          - 1844
        * - **Root Nodes**
          - 39
        * - **Leaf Nodes**
          - 268
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 92
        * - **Individuals**
          - 13
        * - **Properties**
          - 165

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
          - 1.70
        * - **Depth Variance**
          - 1.89
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 66
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 26.25
        * - **Breadth Variance**
          - 621.44
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 13
        * - **Taxonomic Relations**
          - 67
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 6.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MusicOntology

    ontology = MusicOntology()
    ontology.load("path/to/MusicOntology-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
