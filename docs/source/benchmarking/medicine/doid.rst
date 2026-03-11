

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Human Diseases
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2024-12-18
       * - **Creator**
         - The Open Biological and Biomedical Ontology Foundry
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Human Disease Ontology (DOID) <http://purl.obolibrary.org/obo/doid/releases/2024-12-18/doid.owl>`_

Human Disease Ontology (DOID)
========================================================================================================

The Disease Ontology (DOID) is a standardized, machine-readable ontology that provides consistent, reusable and sustainable descriptions of human diseases, medical conditions, and disease-related phenotypic characteristics. Developed collaboratively by the biomedical research community, DOID comprehensively covers disease classifications across diverse medical domains including infectious diseases, genetic disorders, cancers, cardiovascular diseases, and mental health conditions. The ontology employs hierarchical relationships to organize diseases from general categories to specific disease subtypes, enabling both broad and fine-grained disease annotation. DOID integrates with other biomedical ontologies (e.g., phenotype ontologies, gene ontologies) to link disease concepts with associated genes, symptoms, and environmental factors. The ontology is widely used in biomedical databases, genomics research, and clinical informatics for disease annotation and knowledge integration.

**Example Usage**: Annotate a disease research paper or dataset with DOID terms such as "DOID:2841 (lymphoma)" or "DOID:1816 (diabetes mellitus)" to enable automated discovery of disease-related research and clinical data.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 136876
        * - **Total Edges**
          - 288142
        * - **Root Nodes**
          - 14035
        * - **Leaf Nodes**
          - 95185
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 15343
        * - **Individuals**
          - 0
        * - **Properties**
          - 2

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 26
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.59
        * - **Depth Variance**
          - 1.07
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 61852
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 4291.67
        * - **Breadth Variance**
          - 172233228.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 41569
        * - **Non-taxonomic Relations**
          - 25
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DOID

    ontology = DOID()
    ontology.load("path/to/DOID-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
