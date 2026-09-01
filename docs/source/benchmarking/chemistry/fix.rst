

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemicals, Properties
       * - **Current Version**
         - 2020-04-13
       * - **Last Updated**
         - 2020-04-13
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - owl
       * - **Download**
         - `Download FIX Ontology (FIX) <https://terminology.tib.eu/ts/ontologies/FIX>`_

FIX Ontology (FIX)
========================================================================================================
The FIX (Physico-Chemical Methods and Properties) Ontology is an
ontology for representing physico-chemical methods and properties in
chemistry and biochemistry [#fix-paper]_ [#fix-context]_. FIX was
developed with two principal components: an ontology of
physico-chemical methods and an ontology of physico-chemical
properties, with methods applied to the study of properties
[#fix-paper]_.

FIX provides hierarchical representations of experimental methods and
properties and defines relationships between them. In its original
design, the ``inferred_by`` relation was introduced to associate a
physico-chemical property with the method from which it can be inferred
[#fix-paper]_. The ontology also supports more detailed representations
linking a method to the underlying phenomenon, the object being studied,
the resulting data and data features, and the corresponding
physico-chemical property [#fix-paper]_.

FIX property terms can be used to annotate chemical entities at both
the molecular and compound levels [#fix-paper]_. The ontology is
currently no longer maintained and is classified as orphaned; many of
its concepts are also represented in newer chemistry ontologies such as
CHMO, MOP, and RXNO [#fix-context]_.

**Example Usage**: Represent a circular dichroism spectroscopy
experiment using a FIX method term and relate the resulting spectral
features to a physico-chemical property of the studied molecule or
compound [#fix-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 3402
        * - **Total Edges**
          - 7621
        * - **Root Nodes**
          - 22
        * - **Leaf Nodes**
          - 2147
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1163
        * - **Individuals**
          - 0
        * - **Properties**
          - 5

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
          - 2.46
        * - **Depth Variance**
          - 2.32
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 75
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 36.25
        * - **Breadth Variance**
          - 666.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 2751
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import FIX

    ontology = FIX()
    ontology.load("path/to/FIX-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#fix-context] NFDI4Chem Knowledge Base. n.d. "Ontology."
   Available at:
   `https://knowledgebase.nfdi4chem.de/knowledge_base/docs/ontology/ <https://knowledgebase.nfdi4chem.de/knowledge_base/docs/ontology/>`_

.. [#fix-paper] Degtyarenko, K. 2003.
   "Chemical Vocabularies and Ontologies for Bioinformatics."
   In *Proceedings of the 2003 International Chemical Information
   Conference*, Nîmes, France, 19--22 October 2003,
   pp. 144--162.
   Infonortics, Tetbury.
   Available at:
   `https://www.researchgate.net/publication/200179492_Chemical_vocabularies_and_ontologies_for_bioinformatics
   <https://www.researchgate.net/publication/200179492_Chemical_vocabularies_and_ontologies_for_bioinformatics>`_
