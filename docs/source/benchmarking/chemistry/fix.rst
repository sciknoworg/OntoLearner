

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

The FIX (Physico-Chemical Methods and Properties) Ontology provides a
systematic vocabulary for describing and classifying physico-chemical
methods and their associated properties [#fix-context]_. It represents
analytical and experimental techniques used in chemistry and materials
science, including measurement methods, analytical procedures, and the
physical and chemical properties they determine [#fix-context]_. In the
broader chemistry ontology landscape, FIX is related to ontologies such
as ChEBI, which provides a comprehensive classification of chemical
entities and their roles [#fix-context]_ [#chebi-paper]_. The ontology
captures relationships between methods and properties, enabling precise
description of experimental workflows and results in laboratory and
industrial settings [#fix-context]_. It supports semantic
interoperability in chemistry databases, laboratory information systems,
and scientific data repositories [#fix-context]_.

**Example Usage**: Represent a mass spectrometry measurement as an
instance of a FIX analytical method linked to chemical property terms
such as molecular weight or compound identification, and connect the
measured substance to a ChEBI chemical entity to support semantic
integration and structured querying of experimental results
[#fix-context]_ [#chebi-paper]_.

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

.. [#chebi-paper] Degtyarenko, K., de Matos, P., Ennis, M., Hastings, J.,
   Zbinden, M., McNaught, A., Alcántara, R., Darsow, M., Guedj, M.,
   and Ashburner, M. 2008. "ChEBI: A Database and Ontology for Chemical
   Entities of Biological Interest."
   *Nucleic Acids Research* 36(Database issue): D344-D350.
   doi:10.1093/nar/gkm791
   Available at:
   `https://pubmed.ncbi.nlm.nih.gov/17932057/ <https://pubmed.ncbi.nlm.nih.gov/17932057/>`_
