.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Protein Modifications
       * - **Current Version**
         - 1.031.6
       * - **Last Updated**
         - 2022-06-13
       * - **Creator**
         - None
       * - **License**
         - Creative Commons Attribution 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Protein Modifications Ontology (PSIMOD) <https://github.com/HUPO-PSI/psi-mod-CV>`_

Protein Modifications Ontology (PSIMOD)
========================================================================================================

The Protein Modifications Ontology (PSIMOD) is a comprehensive ontology
developed by the Proteomics Standards Initiative (PSI) to describe
chemical modifications of proteins [#psimod-paper]_ [#psimod-obo]_.
It organizes protein modifications into a directed acyclic graph (DAG)
structure, enabling hierarchical classification based on molecular
structure or the modified amino acid residue [#psimod-paper]_
[#psimod-obo]_. PSIMOD captures a wide range of protein modifications,
including phosphorylation, acetylation, ubiquitination, and
glycosylation, providing detailed descriptions of their chemical nature
and biological significance [#psimod-paper]_ [#psimod-obo]_. The
ontology supports semantic annotation of proteomics datasets,
facilitating data integration, analysis, and sharing across proteomics
studies [#psimod-paper]_ [#psimod-obo]_. By providing a standardized
vocabulary, PSIMOD enhances the reproducibility and interoperability of
proteomics research, enabling advanced queries and comparative analyses
[#psimod-paper]_ [#psimod-obo]_.

**Example Usage**: Annotate a proteomics dataset with PSIMOD terms to
specify protein modifications, such as phosphorylation or acetylation,
and link these modifications to their relevant biological context,
enabling standardized annotation, semantic querying, and cross-study
comparison [#psimod-paper]_ [#psimod-obo]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 28523
        * - **Total Edges**
          - 86380
        * - **Root Nodes**
          - 9338
        * - **Leaf Nodes**
          - 16902
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 2098
        * - **Individuals**
          - 0
        * - **Properties**
          - 4

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 4
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.95
        * - **Depth Variance**
          - 0.60
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 11284
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 5684.00
        * - **Breadth Variance**
          - 22690827.20
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 7913
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PSIMOD

    ontology = PSIMOD()
    ontology.load("path/to/PSIMOD-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------
.. [#psimod-obo] OBO Foundry. n.d. "Protein Modification Ontology (MOD)."
   Available at: `https://obofoundry.org/ontology/mod.html <https://obofoundry.org/ontology/mod.html>`_

.. [#psimod-paper] Montecchi-Palazzi, L., Beavis, R., Binz, P.-A.,
   Chalkley, R. J., Cottrell, J., Creasy, D., Shofstahl, J.,
   Seymour, S. L., Garavelli, J. S., and Orchard, S. 2008.
   "The PSI-MOD Community Standard for Representation of Protein
   Modification Data."
   *Nature Biotechnology* 26(8): 864-866.
