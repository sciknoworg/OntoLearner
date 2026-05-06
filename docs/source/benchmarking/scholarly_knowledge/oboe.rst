.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scientific Observation
       * - **Current Version**
         - 1.2
       * - **Last Updated**
         - None
       * - **Creator**
         - The Regents of the University of California
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Extensible Observation Ontology (OBOE) <https://terminology.tib.eu/ts/ontologies/OBOE>`_

Extensible Observation Ontology (OBOE)
========================================================================================================
The Extensible Observation Ontology (OBOE) is a formal ontology for capturing the semantics of scientific observations and measurements [#oboe-github]_ [#oboe-bioportal]_. It supports researchers in adding detailed semantic annotations to scientific data, thereby clarifying the meaning of observations, measured values, entities, characteristics, standards, and protocols [#oboe-bioportal]_. OBOE provides a generic conceptual framework for describing observational datasets, especially datasets consisting of observations and measurements [#oboe-github]_.

The ontology uses a class-based modeling approach, defining core concepts such as ``Observation``, ``Measurement``, ``Entity``, ``Characteristic``, ``Standard``, and ``Protocol`` [#oboe-bioportal]_. In OBOE, an observation is an event in which one or more measurements are taken; a measurement records the measured value of a characteristic of an entity; and standards provide units or controlled vocabularies for interpreting those values [#oboe-bioportal]_. OBOE can also represent contextual information such as space and time, as well as dependencies between observations, including nested experimental observations [#oboe-bioportal]_.

Typical applications of OBOE include semantic annotation of observational datasets, measurement metadata modeling, dataset discovery, interoperability across scientific data repositories, and support for data interpretation and reuse [#oboe-github]_ [#oboe-bioportal]_. By providing a standardized and extensible framework for describing observations and measurements, OBOE helps make scientific data more interpretable, comparable, searchable, and reusable across research domains [#oboe-bioportal]_.

**Example Usage**:
Annotate a scientific observation dataset with OBOE terms to specify the observed entity, measured characteristic, measurement value, unit or standard, protocol, and contextual information such as location and time. This enables semantic search, dataset integration, measurement interpretation, and reuse across scientific observation platforms [#oboe-github]_ [#oboe-bioportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1868
        * - **Total Edges**
          - 5017
        * - **Root Nodes**
          - 169
        * - **Leaf Nodes**
          - 156
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 478
        * - **Individuals**
          - 0
        * - **Properties**
          - 30

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 11
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.96
        * - **Depth Variance**
          - 4.93
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 480
        * - **Minimum Breadth**
          - 6
        * - **Average Breadth**
          - 153.33
        * - **Breadth Variance**
          - 18183.39
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 819
        * - **Non-taxonomic Relations**
          - 60
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OBOE

    ontology = OBOE()
    ontology.load("path/to/OBOE-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#oboe-github] NCEAS. n.d.
   "OBOE: The Extensible Observation Ontology."
   GitHub Repository.
   Available at:
   `https://github.com/NCEAS/oboe <https://github.com/NCEAS/oboe>`_

.. [#oboe-bioportal] NCBO BioPortal. 2019.
   "The Extensible Observation Ontology."
   Available at:
   `https://bioportal.bioontology.org/ontologies/OBOE <https://bioportal.bioontology.org/ontologies/OBOE>`_
