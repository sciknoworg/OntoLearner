

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Arts and Humanities
       * - **Category**
         - Music Theory
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 25th October 2007
       * - **Creator**
         - Christopher Sutton, Yves Raimond, Matthias Mauch
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Timeline Ontology (TimelineOntology) <https://github.com/motools/timelineontology>`_

Timeline Ontology (TimelineOntology)
========================================================================================================

The Timeline Ontology provides a formal framework for representing and
managing temporal information in multimedia and music contexts. It is
centered around the notion of timelines as temporal backbones that can
support various types of media and temporal objects, including signals,
videos, performances, scores, and musical works [#timeline-spec]_. The
ontology enables precise temporal annotation by allowing instants and
intervals to be defined on a timeline, supporting structured
representation of time-based relationships between different media
components [#timeline-spec]_. It supports temporal modelling of
durations, intervals, and temporal positions within multimedia and music
resources [#timeline-spec]_ [#mo-paper]_. The Timeline Ontology
facilitates synchronization across different representations, such as
aligning audio signals with musical notation or linking performances and
recordings to temporal metadata [#timeline-spec]_ [#mo-paper]_. It is
particularly useful in music information retrieval, multimedia
annotation, and Semantic Web applications that require machine-readable
temporal descriptions [#timeline-spec]_ [#omras2]_. By providing a
common temporal framework, the Timeline Ontology supports interoperability
across music and media analysis systems and enables temporal querying and
integration of complex time-based data [#timeline-spec]_ [#omras2]_.

**Example Usage**: Annotate an audio recording, video, or symbolic music
file with Timeline Ontology terms for timelines, instants, and
intervals in order to align chord events, note events, subtitles, or
performance segments with precise temporal positions, enabling temporal
querying, cross-media synchronization, and interoperable multimedia
annotation [#timeline-spec]_ [#omras2]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 286
        * - **Total Edges**
          - 652
        * - **Root Nodes**
          - 20
        * - **Leaf Nodes**
          - 89
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 47
        * - **Individuals**
          - 2
        * - **Properties**
          - 46

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 5
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.28
        * - **Depth Variance**
          - 1.89
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 20
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 9.67
        * - **Breadth Variance**
          - 56.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 2
        * - **Taxonomic Relations**
          - 28
        * - **Non-taxonomic Relations**
          - 10
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import TimelineOntology

    ontology = TimelineOntology()
    ontology.load("path/to/TimelineOntology-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#timeline-spec] Raimond, Y., and Abdallah, S. A. 2006.
   "The Timeline Ontology."
   OWL ontology specification.
   Available at: `https://motools.sourceforge.net/timeline/timeline.html <https://motools.sourceforge.net/timeline/timeline.html>`_

.. [#mo-paper] Raimond, Y., Abdallah, S. A., Sandler, M. B.,
   and Giasson, F. 2007. "The Music Ontology."
   In *Proceedings of the 8th International Conference on Music
   Information Retrieval (ISMIR 2007)*, Vienna, Austria,
   pp. 417-422.
   Available at: `https://ismir2007.ismir.net/proceedings/ISMIR2007_p417_raimond.pdf <https://ismir2007.ismir.net/proceedings/ISMIR2007_p417_raimond.pdf>`_

.. [#omras2] Fazekas, G., Raimond, Y., Jacobson, K., and Sandler, M. 2010.
   "An Overview of Semantic Web Activities in the OMRAS2 Project."
   *Journal of New Music Research* 39(4): 295-311.
   doi:10.1080/09298215.2010.536555
