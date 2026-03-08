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

The Environmental Noise Measurement Ontology (ENM) is an application ontology developed as part of the eNanoMapper  (https://www.enanomapper.net/), NanoCommons (https://www.nanocommons.eu/), and ACEnano (http://acenano-project.eu/)  projects to support toxicological data management for engineered nanomaterials (ENMs). ENM provides a comprehensive vocabulary for describing nanomaterial safety assessment, including experimental procedures, measurement techniques, material properties, and exposure scenarios. The ontology reuses and integrates terms from several established ontologies, such as the Nanoparticle Ontology (NPO), Chemical Information Ontology (CHEMINF), Chemical Entities of Biological Interest (ChEBI), and Environment Ontology (ENVO), to ensure semantic interoperability and data integration. ENM enables standardized annotation of nanomaterial safety data, facilitating data sharing, regulatory compliance, and advanced analysis across research projects and databases. By providing a common framework, ENM supports the development of computational infrastructure for toxicology, risk assessment, and environmental health studies. The ontology is actively maintained and extended to incorporate new concepts and requirements from the nanomaterial safety community.

**Example Usage**:
Annotate a nanotoxicology study with ENM terms to specify the nanomaterial type, measurement methods, exposure conditions, and observed biological effects, enabling cross-study comparison and regulatory reporting.

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
