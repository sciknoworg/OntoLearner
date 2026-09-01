

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Computer Science
       * - **Current Version**
         - 3.4
       * - **Last Updated**
         - None
       * - **Creator**
         - Knowledge Media Institute, Open University
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Computer Science Ontology (CSO) <https://cso.kmi.open.ac.uk/home>`_

Computer Science Ontology (CSO)
========================================================================================================

The Computer Science Ontology (CSO) is a large-scale semantic resource that provides a comprehensive vocabulary of research areas, topics, and concepts in computer science, organized through semantic relationships and topic hierarchies [#cso-paper]_ [#cso-portal]_. It covers diverse computing domains, including artificial intelligence, software engineering, networking, databases, human-computer interaction, security, information retrieval, and emerging research areas, enabling precise semantic annotation of scholarly contributions [#cso-paper]_. CSO supports relationship modeling through properties such as ``superTopicOf`` for topic hierarchies, ``contributesTo`` for linking research topics to broader research areas, and other domain-relevant relationships that support knowledge discovery and research mapping [#cso-paper]_ [#cso-portal]_. The ontology enables automated research classification, literature organization, topic extraction, expertise matching, trend analysis, and scholarly knowledge graph construction by providing standardized semantic descriptions of computer science research areas [#cso-paper]_. CSO facilitates semantic interoperability in scholarly information systems, research management platforms, academic search engines, and recommendation systems [#cso-portal]_.

**Example Usage**: Annotate a research paper or researcher profile with CSO terms such as ``Machine Learning`` as a main topic, ``Deep Learning`` as a subtopic, and ``Natural Language Processing`` as a related topic. This enables semantic discovery of related research, topic-based search, expertise matching, and research landscape analysis [#cso-paper]_ [#cso-portal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 25897
        * - **Total Edges**
          - 152243
        * - **Root Nodes**
          - 94
        * - **Leaf Nodes**
          - 11199
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 0
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.67
        * - **Depth Variance**
          - 0.22
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 187
        * - **Minimum Breadth**
          - 94
        * - **Average Breadth**
          - 140.50
        * - **Breadth Variance**
          - 2162.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 44204
        * - **Non-taxonomic Relations**
          - 49080
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CSO

    ontology = CSO()
    ontology.load("path/to/CSO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#cso-paper] Salatino, Angelo A., Thiviyan Thanapalasingam,
   Andrea Mannocci, Francesco Osborne, and Enrico Motta. 2018.
   "The Computer Science Ontology: A Large-Scale Taxonomy of Research Areas."
   *The Semantic Web -- ISWC 2018*.
   DOI:
   `10.1007/978-3-030-00668-6_12 <https://doi.org/10.1007/978-3-030-00668-6_12>`_

.. [#cso-portal] Knowledge Media Institute, The Open University. n.d.
   "Computer Science Ontology."
   Available at:
   `https://cso.kmi.open.ac.uk/ <https://cso.kmi.open.ac.uk/>`_
