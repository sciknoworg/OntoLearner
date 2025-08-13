

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - 1.1.0
       * - **Last Updated**
         - 2017-10-19
       * - **Creator**
         - Daniel Schober
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Nuclear Magnetic Resonance Controlled Vocabulary (NMRCV) <https://terminology.tib.eu/ts/ontologies/NMRCV>`_

Nuclear Magnetic Resonance Controlled Vocabulary (NMRCV)
========================================================================================================

This artefact is an MSI-approved controlled vocabulary primarily developed under COSMOS EU and PhenoMeNal EU governance.     The nmrCV is supporting the nmrML XML format with standardized terms. nmrML is a vendor agnostic open access NMR raw data standard.     Its primaly role is analogous to the mzCV for the PSI-approved mzML XML format. It uses BFO2.0 as its Top level.     This CV was derived from two predecessors (The NMR CV from the David Wishart Group, developed by Joseph Cruz)     and the MSI nmr CV developed by Daniel Schober at the EBI. This simple taxonomy of terms (no DL semantics used)     serves the nuclear magnetic resonance markup language (nmrML) with meaningful descriptors to amend the nmrML xml file     with CV terms. Metabolomics scientists are encouraged to use this CV to annotrate their raw and experimental context data,     i.e. within nmrML. The approach to have an exchange syntax mixed of an xsd and CV stems from the PSI mzML effort.     The reason to branch out from an xsd into a CV is, that in areas where the terminology is likely to change faster     than the nmrML xsd could be updated and aligned, an externally and decentrallised maintained CV can accompensate     for such dynamics in a more flexible way. A second reason for this set-up is that semantic validity of CV terms     used in an nmrML XML instance (allowed CV terms, position/relation to each other, cardinality) can be validated     by rule-based proprietary validators: By means of cardinality specifications and XPath expressions defined     in an XML mapping file (an instances of the CvMappingRules.xsd ), one can define what ontology terms are allowed     in a specific location of the data model.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1596
        * - **Total Edges**
          - 3951
        * - **Root Nodes**
          - 184
        * - **Leaf Nodes**
          - 662
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 757
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
          - 5
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.01
        * - **Depth Variance**
          - 0.72
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 273
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 103.83
        * - **Breadth Variance**
          - 10836.47
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 792
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import NMRCV

    ontology = NMRCV()
    ontology.load("path/to/NMRCV-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
