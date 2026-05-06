.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Patricia Kügler
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Tribology and Artificial Intelligence Ontology (TribAIn) <https://github.com/snow0815/tribAIn>`_

Tribology and Artificial Intelligence Ontology (TribAIn)
========================================================================================================
TribAIn is an ontology for the description of tribological experiments and their results [#tribain-github]_ [#tribain-paper]_. It is designed to be used in the context of the TribAIn project, which aims to develop a knowledge-based system for the design and analysis of tribological systems [#tribain-paper]_. It provides a structured vocabulary for representing tribological experiments, experimental setups, methodological background knowledge, measurements, analyses, interpretations, and related data, supporting research in tribology [#tribain-github]_ [#tribain-paper]_.

The ontology employs a class-based modeling approach, defining classes for different types of tribological experiments, experimental setups, results, measurements, analyses, and related data, along with properties to describe their characteristics and interactions [#tribain-paper]_. Hierarchies are used to organize classes into categories, enabling efficient data retrieval, comparison, and analysis [#tribain-github]_. TribAIn supports the integration of data from various sources, including natural-language texts and tabular data, promoting interoperability and data-driven research in tribology [#tribain-paper]_.

Typical applications of TribAIn include the documentation of tribological experiments, semantic annotation of experimental setups and results, reuse and comparison of tribological knowledge, optimization of tribological system design, and integration of diverse datasets to support advanced analytics and knowledge discovery [#tribain-github]_ [#tribain-paper]_. By providing a standardized vocabulary and framework, TribAIn enhances collaboration, interoperability, and knowledge reuse in the field of tribology [#tribain-paper]_.

**Example Usage**:
Annotate a tribological experiment with TribAIn terms to specify the experimental setup, contact bodies, lubricant, testing conditions, measurements, analysis results, and interpretations. This enables semantic search, comparison of experimental results, and integration with tribology research platforms [#tribain-github]_ [#tribain-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 771
        * - **Total Edges**
          - 1723
        * - **Root Nodes**
          - 163
        * - **Leaf Nodes**
          - 279
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 241
        * - **Individuals**
          - 21
        * - **Properties**
          - 64

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 9
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.56
        * - **Depth Variance**
          - 2.52
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 320
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 72.90
        * - **Breadth Variance**
          - 9158.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 21
        * - **Taxonomic Relations**
          - 324
        * - **Non-taxonomic Relations**
          - 24
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import TribAIn

    ontology = TribAIn()
    ontology.load("path/to/TribAIn-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#tribain-github] Kügler, Patricia. n.d.
   "tribAIn: Ontology for scientific experiments in the domain of tribology."
   GitHub Repository.
   Available at:
   `https://github.com/snow0815/tribAIn <https://github.com/snow0815/tribAIn>`_

.. [#tribain-paper] Kügler, Patricia, and Marian Wartzack. 2020.
   "tribAIn—Towards an Explicit Specification of Shared Tribological Understanding."
   *Applied Sciences* 10(13): 4421.
   DOI:
   `10.3390/app10134421 <https://doi.org/10.3390/app10134421>`_
