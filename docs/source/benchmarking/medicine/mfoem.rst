.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Emotion
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Swiss Centre for Affective Sciences & University at Buffalo
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Mental Functioning Ontology of Emotions - Emotion Module (MFOEM) <http://purl.obolibrary.org/obo/MFOEM.owl>`_

Mental Functioning Ontology of Emotions - Emotion Module (MFOEM)
========================================================================================================

The Mental Functioning Ontology of Emotions - Emotion Module (MFOEM) is a domain ontology designed to comprehensively represent affective phenomena, including emotions, moods, and their various dimensions and expressions. MFOEM provides a structured vocabulary for describing the bearers of emotions, types of emotions, their parts, and the dimensions along which they vary (such as intensity, duration, and valence). The ontology also covers facial and vocal expressions of emotions and the influence of affective phenomena on human behavior. MFOEM supports semantic annotation of psychological and neuroscientific data, enabling interoperability, data integration, and advanced analysis in affective science research. By providing a standardized framework, MFOEM facilitates cross-study comparison, meta-analysis, and the development of emotion-aware applications in artificial intelligence and human-computer interaction. The ontology is actively maintained and extended to incorporate new findings and requirements from the affective science community.

**Example Usage**:
Annotate a psychological study with MFOEM terms to specify the types of emotions measured (e.g., "fear," "joy"), their intensity, and observed facial expressions, enabling semantic integration and comparison across emotion research datasets.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2542
        * - **Total Edges**
          - 5116
        * - **Root Nodes**
          - 163
        * - **Leaf Nodes**
          - 1513
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 637
        * - **Individuals**
          - 19
        * - **Properties**
          - 22

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.24
        * - **Depth Variance**
          - 5.65
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 274
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 65.07
        * - **Breadth Variance**
          - 8317.35
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 19
        * - **Taxonomic Relations**
          - 837
        * - **Non-taxonomic Relations**
          - 20
        * - **Average Terms per Type**
          - 4.75
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MFOEM

    ontology = MFOEM()
    ontology.load("path/to/MFOEM-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
