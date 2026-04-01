

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Agriculture
       * - **Category**
         - Plant Anatomy, Morphology, Growth and Development
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Plant Ontology (PO) <https://github.com/Planteome/plant-ontology>`_

Plant Ontology (PO)
========================================================================================================

The Plant Ontology (PO) is a structured vocabulary and ontology
resource that links plant anatomy, morphology, growth, and development
to plant genomics and phenomics data [#obo]_ [#po-paper]_. Developed as
a community resource, PO provides a framework for describing plant
structures and developmental stages across plant species [#obo]_
[#po-dev-paper]_. The ontology integrates anatomical and developmental
terms that can be associated with plant genes and phenotypes, enabling
researchers to annotate data and support comparative genomics and
comparative plant biology [#po-paper]_ [#po-dev-paper]_. PO is designed
to facilitate data integration and interoperability in plant science
research [#obo]_ [#po-paper]_. With its hierarchical organization of
plant structures and developmental stages, including whole plants,
organs, tissues, and cell types, PO supports applications such as
literature curation, genome annotation, and phenotypic data annotation
[#po-paper]_. The ontology is under active development and is integrated
with the Planteome project and other biological ontologies to support
semantic compatibility in the plant science community [#obo]_
[#planteome]_.

**Example Usage**: Annotate a plant genomics or phenomics dataset with PO terms for plant
structures and developmental stages, such as leaf, root, flower, seed,
or senescent stage, to enable standardized annotation, cross-species
comparison, and integration with plant science databases and analysis
platforms [#obo]_ [#po-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 20790
        * - **Total Edges**
          - 60638
        * - **Root Nodes**
          - 5936
        * - **Leaf Nodes**
          - 11639
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1874
        * - **Individuals**
          - 0
        * - **Properties**
          - 13

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
          - 1.07
        * - **Depth Variance**
          - 0.72
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 8034
        * - **Minimum Breadth**
          - 82
        * - **Average Breadth**
          - 3462.50
        * - **Breadth Variance**
          - 11752362.58
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 2863
        * - **Non-taxonomic Relations**
          - 36
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PO

    ontology = PO()
    ontology.load("path/to/PO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#obo] OBO Foundry. n.d. "Plant Ontology (PO)."
   Available at: `https://obofoundry.org/ontology/po.html <https://obofoundry.org/ontology/po.html>`_

.. [#po-paper] Cooper, L., Walls, R. L., Elser, J., Gandolfo, M. A.,
   Stevenson, D. W., Smith, B., Preece, J., Athreya, B., Mungall, C. J.,
   and Rensing, S. A. 2013. "The Plant Ontology as a Tool for Comparative
   Plant Anatomy and Genomic Analyses."
   *Plant and Cell Physiology* 54(2): e1.
   doi:10.1093/pcp/pcs163
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC3583023/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC3583023/>`_

.. [#po-dev-paper] Walls, R. L., Cooper, L., Elser, J., Gandolfo, M. A.,
   Mungall, C. J., Smith, B., Stevenson, D. W., and Jaiswal, P. 2019.
   "The Plant Ontology Facilitates Comparisons of Plant Development
   Stages Across Species."
   *Frontiers in Plant Science* 10:631.
   doi:10.3389/fpls.2019.00631
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC6558174/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC6558174/>`_

.. [#planteome] Cooper, L., Elser, J., Laporte, M.-A., Arnaud, E.,
   and Jaiswal, P. 2024. "Planteome 2024 Update: Reference Ontologies
   and Knowledgebase for Plant Biology."
   *Nucleic Acids Research* 52(D1): D1548-D1555.
   doi:10.1093/nar/gkad1028
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC10767901/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC10767901/>`_
