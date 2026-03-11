

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Arts and Humanities
       * - **Category**
         - Musical Works
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2007-10-25
       * - **Creator**
         - Yves Raimond, Samer Abdallah, Centre for Digital Music, Queen Mary, University of London
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Chord Ontology (ChordOntology) <https://github.com/motools/chordontology>`_

Chord Ontology (ChordOntology)
========================================================================================================

The Chord Ontology is a formal representation for describing and classifying chords in musical compositions. It provides a structured vocabulary for representing harmonic concepts and chord structures, enabling precise annotation and analysis of music at the semantic level. The ontology captures essential chord properties including chord type (major, minor, diminished, augmented), root note, and constituent pitch classes. It facilitates semantic annotation of audio files, musical scores, and music information retrieval systems, allowing researchers and musicians to query and discover musical pieces based on harmonic content. The ontology integrates with broader music theory frameworks and supports interoperability with other music-related ontologies. By formalizing chord relationships and structures, the Chord Ontology enables computational music analysis, music recommendation systems, and digital musicology applications. It provides a common framework for music annotation across diverse platforms and datasets, supporting music education, composition analysis, and music information systems development.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 196
        * - **Total Edges**
          - 456
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 66
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 9
        * - **Individuals**
          - 108
        * - **Properties**
          - 0

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
          - 1.19
        * - **Depth Variance**
          - 0.77
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 31
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 11.60
        * - **Breadth Variance**
          - 109.44
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 42
        * - **Taxonomic Relations**
          - 4
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 10.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ChordOntology

    ontology = ChordOntology()
    ontology.load("path/to/ChordOntology-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
