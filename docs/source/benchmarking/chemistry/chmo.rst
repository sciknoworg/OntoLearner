.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2022-04-19
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Chemical Methods Ontology (ChMO) <https://github.com/rsc-ontologies/rsc-cmo>`_

Chemical Methods Ontology (ChMO)
========================================================================================================

The Chemical Methods Ontology (ChMO) is a structured ontology that
provides a controlled vocabulary for describing chemical methods,
experimental techniques, and analytical procedures used in chemistry and
related sciences [#chmo-repo]_ [#chmo-bioportal]_. ChMO contains terms
covering methods for data collection, sample preparation and separation,
and material synthesis, together with associated instruments and
experimental outputs [#chmo-repo]_ [#chmo-bioportal]_. The ontology is
intended to support semantic annotation of chemical workflows and to
improve interoperability across chemical databases, laboratory
information systems, and computational tools [#chmo-repo]_
[#chmo-bioportal]_. By providing a standardized framework for chemical
methods and related experimental information, ChMO supports data
integration, reproducibility, and structured querying across chemical
research datasets [#chmo-repo]_ [#chmo-bioportal]_.

**Example Usage**: Annotate a chemical experiment with ChMO terms to
specify the analytical method, such as liquid
chromatography-mass spectrometry, the sample preparation steps, the
instrument configuration, and the data outputs, enabling semantic
search and integration with other chemical research datasets
[#chmo-repo]_ [#chmo-bioportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 24075
        * - **Total Edges**
          - 44651
        * - **Root Nodes**
          - 3100
        * - **Leaf Nodes**
          - 17250
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3202
        * - **Individuals**
          - 0
        * - **Properties**
          - 27

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.49
        * - **Depth Variance**
          - 0.63
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 13439
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 2993.88
        * - **Breadth Variance**
          - 20855464.86
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 3601
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ChMO

    ontology = ChMO()
    ontology.load("path/to/ChMO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#chmo-repo] Royal Society of Chemistry. n.d.
   "Chemical Methods Ontology (ChMO)."
   GitHub repository.
   Available at:
   `https://github.com/rsc-ontology/rsc-cmo <https://github.com/rsc-ontology/rsc-cmo>`_

.. [#chmo-bioportal] NCBO BioPortal. n.d. "Chemical Methods Ontology."
   Available at: `https://bioportal.bioontology.org/ontologies/CHMO <https://bioportal.bioontology.org/ontologies/CHMO>`_
