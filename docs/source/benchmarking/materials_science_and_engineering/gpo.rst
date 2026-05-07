.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Simon Stier
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download General Process Ontology (GPO) <https://github.com/General-Process-Ontology/ontology>`_

General Process Ontology (GPO)
========================================================================================================

The General Process Ontology (GPO) is a domain ontology developed to model processes across scientific and industrial domains [#gpo-github]_ [#gpo-ontocommons]_. GPO provides a structured vocabulary for representing holistic processes that transform inputs or educts, such as matter, energy, and information, into outputs or products using tools such as devices and algorithms [#gpo-github]_ [#gpo-ontocommons]_.

The ontology supports decomposition of processes into sub-processes and represents predecessor and successor relationships between processes [#gpo-github]_. GPO is based on EMMO and is described as a cross-project development coordinated by Fraunhofer ISC, with application areas including manufacturing, logistics, mining, and information and data processing [#gpo-github]_ [#gpo-ontocommons]_. By providing a standardized process vocabulary, GPO supports semantic annotation, data integration, interoperability, and knowledge sharing across process-related workflows [#gpo-github]_.

**Example Usage**:
Annotate a manufacturing workflow with GPO terms to specify process steps, input materials or information, output products, tools such as devices or algorithms, and predecessor or successor relationships between process steps, enabling semantic search and integration with process management systems [#gpo-github]_ [#gpo-ontocommons]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 548
        * - **Total Edges**
          - 923
        * - **Root Nodes**
          - 99
        * - **Leaf Nodes**
          - 270
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 187
        * - **Individuals**
          - 0
        * - **Properties**
          - 17

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.41
        * - **Depth Variance**
          - 1.20
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 223
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 76.14
        * - **Breadth Variance**
          - 5799.55
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GPO

    ontology = GPO()
    ontology.load("path/to/GPO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#gpo-github] General-Process-Ontology. n.d.
   "General Process Ontology (GPO)."
   GitHub repository.
   Available at:
   `https://github.com/General-Process-Ontology/ontology <https://github.com/General-Process-Ontology/ontology>`_

.. [#gpo-ontocommons] OntoCommons. n.d.
   "General Process Ontology (GPO)."
   Ontology catalogue entry.
   Available at:
   `https://data.ontocommons.linkeddata.es/vocabulary/GeneralProcessOntology%28gpo%29 <https://data.ontocommons.linkeddata.es/vocabulary/GeneralProcessOntology%28gpo%29>`_
