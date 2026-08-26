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

The Mental Functioning Ontology of Emotions - Emotion Module (MFOEM), also known as the **Emotion Ontology**, is a domain ontology for representing affective phenomena and concepts related to emotions [#mfoem-github]_ [#mfoem-paper]_. It was developed to support the semantic annotation and integration of data in affective science and neuroscience by providing a shared formal representation of emotion-related concepts [#mfoem-paper]_.

MFOEM provides structured terms for describing emotions and related affective phenomena, including emotion types, their components, and associated features relevant to affective and neuroscientific research [#mfoem-github]_ [#mfoem-paper]_. The ontology supports annotation and comparison of heterogeneous datasets by enabling emotion-related information to be represented in a consistent, machine-readable form [#mfoem-paper]_. By providing standardized semantic descriptions, MFOEM facilitates data integration and interoperability across psychological, neuroscientific, and affective-science research [#mfoem-paper]_.

**Example Usage**:
Annotate an affective-neuroscience dataset with MFOEM terms to represent the emotions investigated in an experiment and associate those emotion concepts with experimental observations or neuroscientific data. This supports consistent semantic annotation and comparison of emotion-related data across studies [#mfoem-paper]_.

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

References
----------

.. [#mfoem-github] Hastings, J. n.d.
   "emotion-ontology."
   GitHub repository.
   Available at:
   `https://github.com/jannahastings/emotion-ontology
   <https://github.com/jannahastings/emotion-ontology>`_

.. [#mfoem-paper] Hastings, J., Ceusters, W.,
   Mulligan, K., and Smith, B. 2012.
   "Annotating Affective Neuroscience Data with the Emotion Ontology."
   Conference paper.
   Available at:
   `https://api.semanticscholar.org/CorpusID:12260742
   <https://api.semanticscholar.org/CorpusID:12260742>`_
