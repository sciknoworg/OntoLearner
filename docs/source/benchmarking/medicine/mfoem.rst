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

The Mental Functioning Ontology of Emotions - Emotion Module (MFOEM), also known as the **Emotion Ontology**, is a domain ontology for affective phenomena such as emotions, moods, appraisals, and subjective feelings [#mfoem-github]_ [#mfoem-obofoundry]_. It is a domain specialization of the broader Mental Functioning Ontology and is designed to support interdisciplinary emotion research through unified semantic annotations [#mfoem-obofoundry]_.

MFOEM provides a structured vocabulary for describing affective phenomena, including the bearers of emotions, types of emotions, parts of emotions, dimensions of variation, facial and vocal expressions, and the role of emotions in influencing human behavior [#mfoem-github]_. By providing standardized terminology, MFOEM supports semantic annotation, interoperability, data integration, and comparison of psychological, neuroscientific, and affective-science datasets [#mfoem-github]_ [#mfoem-obofoundry]_.

**Example Usage**:
Annotate a psychological or affective-science study with MFOEM terms to specify emotion types such as fear or joy, emotion dimensions such as intensity or duration, and observed facial or vocal expressions, enabling semantic integration and comparison across emotion research datasets [#mfoem-github]_ [#mfoem-obofoundry]_.

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
   `https://github.com/jannahastings/emotion-ontology <https://github.com/jannahastings/emotion-ontology>`_

.. [#mfoem-obofoundry] OBO Foundry. n.d.
   "Emotion Ontology."
   Ontology registry entry.
   Available at:
   `https://obofoundry.org/ontology/mfoem.html <https://obofoundry.org/ontology/mfoem.html>`_
