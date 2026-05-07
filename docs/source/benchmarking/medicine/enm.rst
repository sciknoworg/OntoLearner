.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Material Science and Engineering
       * - **Current Version**
         - 10.0
       * - **Last Updated**
         - 2025-02-17
       * - **Creator**
         - eNanoMapper Consortium
       * - **License**
         - Creative Commons 3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Environmental Noise Measurement Ontology (ENM) <https://terminology.tib.eu/ts/ontologies/ENM>`_

Environmental Noise Measurement Ontology (ENM)
========================================================================================================

The Environmental Noise Measurement Ontology (ENM) is an application ontology developed to support toxicological data management and nanomaterial safety assessment for engineered nanomaterials [#enm-doc]_ [#enm-paper]_. It provides a structured vocabulary for describing nanomaterials, experimental procedures, measurement techniques, material properties, exposure scenarios, biological interactions, and safety-related information [#enm-doc]_ [#enm-paper]_.

ENM was developed in the context of the eNanoMapper project and reuses or extends existing ontologies relevant to nanosafety, including the Nanoparticle Ontology (NPO), Chemical Information Ontology (CHEMINF), Chemical Entities of Biological Interest (ChEBI), and Environment Ontology (ENVO) [#enm-paper]_. The ontology supports semantic annotation, data integration, interoperability, search, and reuse of nanomaterial safety data across research projects and databases [#enm-doc]_ [#enm-paper]_.

**Example Usage**:
Annotate a nanotoxicology study with ENM terms to specify the nanomaterial type, measurement method, exposure condition, experimental assay, material property, and observed biological effect, enabling cross-study comparison and integration with nanosafety databases [#enm-doc]_ [#enm-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 102719
        * - **Total Edges**
          - 226566
        * - **Root Nodes**
          - 11156
        * - **Leaf Nodes**
          - 64025
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 26142
        * - **Individuals**
          - 9
        * - **Properties**
          - 53

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 130
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.74
        * - **Depth Variance**
          - 56.70
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 11156
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 206.70
        * - **Breadth Variance**
          - 1767707.90
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 9
        * - **Taxonomic Relations**
          - 36933
        * - **Non-taxonomic Relations**
          - 84
        * - **Average Terms per Type**
          - 3.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ENM

    ontology = ENM()
    ontology.load("path/to/ENM-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#enm-doc] eNanoMapper. n.d.
   "Ontology."
   Available at:
   `https://www.enanomapper.net/ontology <https://www.enanomapper.net/ontology>`_

.. [#enm-paper] Hastings, J., Jeliazkova, N., Owen, G., Tsiliki, G., Munteanu, C. R., Steinbeck, C., and Willighagen, E. 2015.
   "eNanoMapper: harnessing ontologies to enable data integration for nanomaterial risk assessment."
   *Journal of Biomedical Semantics*, 6, Article 10.
   DOI: 10.1186/s13326-015-0005-5.
   Available at:
   `https://pmc.ncbi.nlm.nih.gov/articles/PMC4374589/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC4374589/>`_
