.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Biology
       * - **Current Version**
         - 1.2
       * - **Last Updated**
         - 2025-02-01
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Phenotype and Trait Ontology (PATO) <https://terminology.tib.eu/ts/ontologies/PATO>`_

Phenotype and Trait Ontology (PATO)
========================================================================================================

The Phenotype and Trait Ontology (PATO) is a structured vocabulary for
describing phenotypic qualities, attributes, and traits in a
species-neutral way [#pato-obo]_ [#pato-framework]_. It provides a
standardized framework for annotating and analyzing phenotypic data by
defining qualities such as size, shape, color, morphology, and other
characteristics that can be combined with biological entity ontologies
to describe phenotypes [#pato-framework]_ [#pato-anatomy]_. PATO is
widely used in phenotype annotation and in the logical definition of
phenotype terms across species, supporting data integration and
comparative analysis in genetics, developmental biology, and related
life science domains [#pato-obo]_ [#pato-integration]_. By providing a
common language for phenotypic qualities, PATO facilitates cross-species
interoperability, computational reasoning, and semantic analysis of
phenotype data [#pato-anatomy]_ [#oba-paper]_.

**Example Usage**: Annotate a genetic or phenotype study with PATO terms
to describe qualities such as red coloration, increased size, abnormal
shape, or altered morphology in association with a specific biological
entity, enabling cross-study comparison, semantic integration, and
computational phenotype analysis [#pato-framework]_ [#pato-integration]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 98691
        * - **Total Edges**
          - 259386
        * - **Root Nodes**
          - 16564
        * - **Leaf Nodes**
          - 45644
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 13544
        * - **Individuals**
          - 0
        * - **Properties**
          - 252

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 20
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.73
        * - **Depth Variance**
          - 2.02
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 35876
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 4564.14
        * - **Breadth Variance**
          - 92888669.36
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 30496
        * - **Non-taxonomic Relations**
          - 752
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PATO

    ontology = PATO()
    ontology.load("path/to/PATO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#pato-obo] OBO Foundry. n.d. "Phenotype And Trait Ontology (PATO)."
   Available at: `https://obofoundry.org/ontology/pato.html <https://obofoundry.org/ontology/pato.html>`_

.. [#pato-framework] Gkoutos, G. V., Green, E. C. J., Mallon, A.-M.,
   Hancock, J. M., and Davidson, D. 2005.
   "Using Ontologies to Describe Mouse Phenotypes."
   *Genome Biology* 6:R8.
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC545487/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC545487/>`_

.. [#pato-integration] Mungall, C. J., Gkoutos, G. V., Smith, C. L.,
   Haendel, M. A., Lewis, S. E., and Ashburner, M. 2010.
   "Integrating Phenotype Ontologies Across Multiple Species."
   *Genome Biology* 11:R2.
   doi:10.1186/gb-2010-11-1-r2
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC2847714/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC2847714/>`_

.. [#pato-anatomy] Gkoutos, G. V., Schofield, P. N., and Hoehndorf, R.
   2018. "The Anatomy of Phenotype Ontologies: Principles, Properties
   and Applications."
   *Briefings in Bioinformatics* 19(5): 1008-1021.
   doi:10.1093/bib/bbx035
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC6169674/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC6169674/>`_

.. [#oba-paper] Stefancsik, R., Mungall, C. J., Robinson, P. N.,
   Smith, C. L., Haendel, M. A., and Gkoutos, G. V. 2023.
   "The Ontology of Biological Attributes (OBA)—Computational Traits for
   the Life Sciences."
   *Database* 2023: baad038.
   doi:10.1093/database/baad038
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC9900877/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC9900877/>`_
