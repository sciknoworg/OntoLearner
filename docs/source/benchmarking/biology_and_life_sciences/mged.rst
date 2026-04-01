.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Domain Ontology
       * - **Current Version**
         - 1.3.1.1
       * - **Last Updated**
         - Feb. 9, 2007
       * - **Creator**
         - Chris Stoeckert, Helen Parkinson, Trish Whetzel, Paul Spellman, Catherine A. Ball, Joseph White, John Matese, Liju Fan, Gilberto Fragoso, Mervi Heiskanen, Susanna Sansone, Helen Causton, Laurence Game, Chris Taylor
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download MGED Ontology (MGED) <https://mged.sourceforge.net/ontologies/MGEDontology.php/>`_

MGED Ontology (MGED)
========================================================================================================

The MGED Ontology (MGED) is a domain-specific ontology developed to
standardize the description of microarray experiments. It provides a
structured vocabulary and semantic framework for representing
experimental designs, protocols, biomaterials, array platforms, and
data-related aspects of microarray gene expression studies
[#mged-paper]_ [#mged-bioportal]_. MGED was developed by the microarray
community to support consistent annotation of experiments and to align
with broader microarray data standards such as MIAME and MAGE
[#mged-paper]_ [#mged-standards]_. The ontology has been described as
including a more stable core aligned with MAGE and an extended part that
adds further terms and associations for richer experimental description
[#mged-fairsharing]_ [#mged-scicrunch]_. MGED facilitates
interoperability between microarray data repositories and tools,
supporting the sharing, comparison, and analysis of experimental data
[#mged-paper]_ [#mged-standards]_. By providing a common framework for
experimental metadata, MGED supports reproducibility, data integration,
and meta-analysis in functional genomics and microarray informatics
[#mged-paper]_ [#mged-standards]_.

**Example Usage**: Annotate a microarray experiment with MGED terms to
describe the experimental design, sample and biomaterial
characteristics, hybridization and sample-preparation protocols, array
platform, and data-processing steps, so that the dataset can be shared,
interpreted, and compared consistently across repositories and analysis
tools [#mged-paper]_ [#mged-bioportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 3427
        * - **Total Edges**
          - 5101
        * - **Root Nodes**
          - 730
        * - **Leaf Nodes**
          - 2171
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 233
        * - **Individuals**
          - 681
        * - **Properties**
          - 121

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 11
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.38
        * - **Depth Variance**
          - 2.09
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 1771
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 282.92
        * - **Breadth Variance**
          - 244751.41
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 743
        * - **Taxonomic Relations**
          - 541
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 7.82
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MGED

    ontology = MGED()
    ontology.load("path/to/MGED-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#mged-paper] Whetzel, P. L., Parkinson, H., Causton, H. C.,
   Fan, L., Fostel, J., Fragoso, G., Game, L., Heiskanen, M.,
   Morrison, N., Rocca-Serra, P., Sansone, S.-A., and Stoeckert, C. J. Jr.
   2006. "The MGED Ontology: a resource for semantics-based description
   of microarray experiments."
   *Bioinformatics* 22(7): 866-873.
   doi:10.1093/bioinformatics/btl091

.. [#mged-standards] Ball, C. A., Brazma, A., Causton, H.,
   Chervitz, S., Edgar, R., Hingamp, P., Hermjakob, H., Ikeo, K.,
   Quackenbush, J., Sherlock, G., Spellman, P., Stoekert, C.,
   Tateno, Y., and Sarkans, U. 2006. "MGED standards: work in progress."
   *OMICS* 10(2): 138-144.
   Available at: `https://pubmed.ncbi.nlm.nih.gov/16901218/ <https://pubmed.ncbi.nlm.nih.gov/16901218/>`_

.. [#mged-bioportal] NCBO BioPortal. n.d.
   "Microarray and Gene Expression Data Ontology."
   Available at: `https://bioportal.bioontology.org/ontologies/MO <https://bioportal.bioontology.org/ontologies/MO>`_

.. [#mged-fairsharing] FAIRsharing. n.d.
   "Microarray and Gene Expression Data Ontology."
   Available at: `https://fairsharing.org/1193 <https://fairsharing.org/1193>`_

.. [#mged-scicrunch] SciCrunch. n.d.
   "MGED Ontology."
   Available at: `https://scicrunch.org/resolver/SCR_004484 <https://scicrunch.org/resolver/SCR_004484>`_
