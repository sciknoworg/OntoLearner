.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemical Entities
       * - **Current Version**
         - 239
       * - **Last Updated**
         - 01/01/2025
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Chemical Entities of Biological Interest (ChEBI) <https://www.ebi.ac.uk/chebi/>`_

Chemical Entities of Biological Interest (ChEBI)
========================================================================================================

Chemical Entities of Biological Interest (ChEBI) is a comprehensive
database and ontology of molecular entities, with a particular focus on
small chemical compounds [#chebi-site]_ [#chebi-paper]_. It provides a
structured vocabulary for describing constitutionally or isotopically
distinct atoms, molecules, ions, radicals, complexes, and related
chemical entities, including both naturally occurring substances and
synthetic compounds relevant to biological systems [#chebi-site]_
[#chebi-paper]_. ChEBI incorporates an ontological classification system
that organizes entities into parent-child relationships and supports the
representation of chemical roles, structural classes, and molecular
relationships [#chebi-paper]_ [#chebi-site]_. Widely used in
bioinformatics, cheminformatics, and systems biology, ChEBI enables
consistent chemical annotation, interoperability between databases, and
integration of chemical knowledge across diverse scientific resources
[#chebi-paper]_ [#chebi-site]_. By providing a standardized semantic
framework for chemical entities, ChEBI supports data sharing, advanced
querying, and computational analysis across the life sciences
[#chebi-site]_ [#chebi-paper]_.

**Example Usage**: Annotate a metabolomics dataset with ChEBI terms to
identify compounds such as glucose or ATP, specify their chemical
classification and biological roles, and support standardized
annotation, pathway analysis, and cross-database integration
[#chebi-site]_ [#chebi-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2433610
        * - **Total Edges**
          - 6913389
        * - **Root Nodes**
          - 609907
        * - **Leaf Nodes**
          - 1528418
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 220816
        * - **Individuals**
          - 0
        * - **Properties**
          - 10

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.14
        * - **Depth Variance**
          - 0.69
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 908127
        * - **Minimum Breadth**
          - 26
        * - **Average Breadth**
          - 310545.00
        * - **Breadth Variance**
          - 135103408992.57
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 739967
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ChEBI

    ontology = ChEBI()
    ontology.load("path/to/ChEBI-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#chebi-site] EMBL-EBI. n.d. "ChEBI - Chemical Entities of Biological Interest."
   Available at: `https://www.ebi.ac.uk/chebi/ <https://www.ebi.ac.uk/chebi/>`_

.. [#chebi-paper] Degtyarenko, K., de Matos, P., Ennis, M., Hastings, J.,
   Zbinden, M., McNaught, A., Alcántara, R., Darsow, M., Guedj, M.,
   and Ashburner, M. 2008. "ChEBI: A Database and Ontology for Chemical
   Entities of Biological Interest."
   *Nucleic Acids Research* 36(Database issue): D344-D350.
   doi:10.1093/nar/gkm791
   Available at: `https://pubmed.ncbi.nlm.nih.gov/17932057/ <https://pubmed.ncbi.nlm.nih.gov/17932057/>`_
