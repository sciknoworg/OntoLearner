.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 2013-05-31
       * - **Last Updated**
         - 2013-05-31
       * - **Creator**
         - Dennis G. Thomas
       * - **License**
         - BSD-3-Clause license
       * - **Format**
         - owl
       * - **Download**
         - `Download NanoParticle Ontology (NPO) <https://github.com/sobolevnrm/npo?tab=readme-ov-file>`_

NanoParticle Ontology (NPO)
========================================================================================================

The NanoParticle Ontology (NPO) is a domain ontology developed within
the Basic Formal Ontology framework to represent knowledge about the
preparation, chemical composition, and characterization of
nanomaterials, especially in cancer research and nanomedicine
[#npo-paper]_ [#npo-bioportal]_. NPO provides a structured vocabulary
for describing nanoparticle composition, preparation methods,
physicochemical characteristics, and related entities relevant to
nanotechnology research [#npo-paper]_ [#npo-bioportal]_. The ontology
supports semantic annotation of nanomaterial data, enabling data
integration, interoperability, and ontology-based querying across
biomedical and nanoinformatics resources [#npo-paper]_
[#npo-bioportal]_. NPO is publicly available through NCBO BioPortal and
serves as a reference resource for standardized nanomaterial
representation [#npo-bioportal]_ [#npo-paper]_. By providing a
standardized semantic framework for nanomaterial representation, NPO
supports knowledge sharing, data reuse, and computational analysis in
nanotechnology and nanomedicine research [#npo-paper]_.

**Example Usage**: Annotate a nanomedicine study with NPO terms to
specify nanoparticle composition, for example a gold nanoparticle,
preparation or formulation characteristics, surface functionalization,
and measured physicochemical or biological assay properties, enabling
cross-study comparison, semantic search, and integration across
nanomaterial datasets [#npo-paper]_ [#npo-bioportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 9976
        * - **Total Edges**
          - 36031
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 4344
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 2464
        * - **Individuals**
          - 0
        * - **Properties**
          - 87

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 10
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.26
        * - **Depth Variance**
          - 7.37
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 35
        * - **Minimum Breadth**
          - 7
        * - **Average Breadth**
          - 21.82
        * - **Breadth Variance**
          - 106.88
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 2724
        * - **Non-taxonomic Relations**
          - 12277
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import NPO

    ontology = NPO()
    ontology.load("path/to/NPO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#npo-paper] Thomas, D. G., Pappu, R. V., and Baker, N. A. 2011.
   "NanoParticle Ontology for Cancer Nanotechnology Research."
   *Journal of Biomedical Informatics* 44(1): 59-74.
   doi:10.1016/j.jbi.2010.03.001
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC3042056/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC3042056/>`_

.. [#npo-bioportal] NCBO BioPortal. n.d. "NanoParticle Ontology (NPO)."
   Available at: `https://bioportal.bioontology.org/ontologies/NPO <https://bioportal.bioontology.org/ontologies/NPO>`_
