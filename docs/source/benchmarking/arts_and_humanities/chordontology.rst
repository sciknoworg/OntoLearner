

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

The Chord Ontology is a formal representation for describing and classifying
chords and chord sequences in musical resources. It provides a structured
vocabulary for representing harmonic concepts and chord structures, enabling
semantic annotation and analysis of music data. The ontology captures core
chord properties including chord type (for example major, minor, diminished,
and augmented), root note, constituent intervals, and bass note. It supports
the annotation of audio files, musical scores, and symbolic music files by
linking chord events to temporal structures and music resources. The ontology
was developed within the OMRAS2 project and is designed to interoperate with
related Semantic Web resources such as the Music Ontology, Timeline Ontology,
and Event Ontology. By formalizing chord relationships and structures, the
Chord Ontology supports computational music analysis, harmonic annotation,
music information retrieval, and digital musicology applications. It provides
a common framework for music annotation across datasets and tools, supporting
harmonic analysis, corpus annotation, and music information systems
development [#chord-spec]_ [#omras2]_ [#music-ontology]_.

**Example Usage**: Annotate the harmonic timeline of an audio recording,
musical score, or symbolic music file with Chord Ontology terms for chord
events, root notes, intervals, and bass notes to enable semantic search,
computational harmonic analysis, and integration with music information
retrieval datasets and tools [#chord-spec]_ [#omras2]_.

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

References
----------

.. [#chord-spec] Sutton, C., Raimond, Y., and Mauch, M. 2007.
   "Chord Ontology Specification."
   OMRAS2 Project, Centre for Digital Music, Queen Mary University of London.
   Available at: http://purl.org/ontology/chord/
   Also available at: https://motools.sourceforge.net/chord_draft_1/chord.html

.. [#omras2] Fazekas, G., Raimond, Y., Jacobson, K., and Sandler, M. 2010.
   "An Overview of Semantic Web Activities in the OMRAS2 Project."
   *Journal of New Music Research* 39(4): 295-311.
   doi:10.1080/09298215.2010.536555

.. [#music-ontology] Raimond, Y., Abdallah, S. A., Sandler, M. B.,
   and Giasson, F. 2007.
   "The Music Ontology."
   In *Proceedings of the 8th International Conference on Music Information
   Retrieval (ISMIR 2007)*, Vienna, Austria, pp. 417-422.
   Available at: https://ismir2007.ismir.net/proceedings/ISMIR2007_p417_raimond.pdf
