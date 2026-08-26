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
The Extensible Observation Ontology (OBOE) is a formal ontology for representing the semantics of scientific observations and measurements [#oboe-github]_ [#oboe-paper]_. It was developed to provide a structured framework for describing observational data in terms of the entities being observed, their characteristics, measurements, standards, and contextual relationships [#oboe-paper]_. This semantic representation helps make the meaning of scientific data explicit and supports integration and synthesis across heterogeneous observational datasets [#oboe-paper]_.

OBOE defines core concepts for representing observations and measurements, including observed entities, characteristics, measurement values, standards, protocols, and relationships between observations [#oboe-github]_ [#oboe-paper]_. The ontology can also represent contextual dependencies among observations, allowing complex observational structures and nested relationships to be modeled in a machine-readable form [#oboe-paper]_. By formally describing how measurements relate to entities and characteristics, OBOE supports interpretation and comparison of observational data across different studies [#oboe-paper]_.

Typical applications of OBOE include semantic annotation of ecological and other scientific observation datasets, integration of heterogeneous measurement data, dataset discovery, and synthesis of observational information across research studies [#oboe-paper]_. Its extensible structure allows domain-specific concepts to be incorporated while preserving a shared model for observations and measurements [#oboe-github]_ [#oboe-paper]_.

**Example Usage**:
Annotate an ecological observation dataset with OBOE terms to describe the observed entity, such as a plant or habitat; the characteristic being measured, such as biomass or temperature; the recorded measurement value; the standard or unit used; and contextual relationships to other observations. This enables consistent interpretation, integration, and synthesis of ecological observation data across studies [#oboe-paper]_.

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
   GitHub repository.
   Available at:
   `https://github.com/NCEAS/oboe
   <https://github.com/NCEAS/oboe>`_

.. [#oboe-paper] Madin, J., Bowers, S.,
   Schildhauer, M., Krivov, S., Pennington, D.,
   and Villa, F. 2007.
   "An Ontology for Describing and Synthesizing
   Ecological Observation Data."
   *Ecological Informatics*, 2, 279--296.
   Available at:
   `https://doi.org/10.1016/j.ecoinf.2007.05.004
   <https://doi.org/10.1016/j.ecoinf.2007.05.004>`_
