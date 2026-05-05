

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - General
       * - **Current Version**
         - 1.25-20240924T0027Z-unstable(1.26)
       * - **Last Updated**
         - 24.09.2024
       * - **Creator**
         - Federico Bianchini, Hervé Ménager, Jon Ison, Matúš Kalaš
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download The ontology of data analysis and management (EDAM) <https://terminology.tib.eu/ts/ontologies/edam>`_

The ontology of data analysis and management (EDAM)
========================================================================================================

EDAM is a domain ontology that formalizes concepts, operations, data
types, identifiers, and formats used in computational data analysis and
data management across bioinformatics, biological sciences, and related
scientific domains [#edam-home]_ [#edam-paper]_. It provides a structured
vocabulary for describing bioinformatics analysis workflows, computational
operations, data types, data identifiers, data formats, and relationships
between analysis steps [#edam-paper]_.

EDAM is organized into four main sections: Topic, Operation, Data, and
Format [#edam-home]_ [#edam-paper]_. Topic represents research domains
and application areas; Operation represents analysis and processing
functions; Data represents data types and identifiers; and Format
represents computational data formats and standards [#edam-home]_. This
structure enables consistent semantic annotation of tools, workflows,
databases, datasets, publications, and software resources in
bioinformatics [#edam-paper]_.

EDAM is designed for usability by diverse stakeholders, including
bioinformaticians, tool developers, curators, and researchers
[#edam-home]_. Its relatively simple hierarchical organization supports
standardized descriptions of bioinformatics tools and services, automated
tool discovery, workflow composition, dataset annotation, and semantic
integration of computational biology resources [#edam-paper]_.

**Example Usage**: Annotate a bioinformatics tool or service with EDAM
terms for input data, operation, output format, and research topic, such
as sequence alignment data, pairwise sequence alignment, FASTA format,
and sequence analysis. These annotations make the tool easier to discover,
compare, integrate into workflows, and connect with related datasets or
services [#edam-home]_ [#edam-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 12367
        * - **Total Edges**
          - 36215
        * - **Root Nodes**
          - 176
        * - **Leaf Nodes**
          - 8223
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3513
        * - **Individuals**
          - 0
        * - **Properties**
          - 12

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
          - 2.75
        * - **Depth Variance**
          - 4.24
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 635
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 196.55
        * - **Breadth Variance**
          - 31795.52
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 7916
        * - **Non-taxonomic Relations**
          - 1314
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import EDAM

    ontology = EDAM()
    ontology.load("path/to/EDAM-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#edam-home] EDAM Ontology. n.d.
   "EDAM: The Ontology of Data Analysis and Management."
   Available at:
   `https://edamontology.org/ <https://edamontology.org/>`_

.. [#edam-paper] Ison, J., Kalaš, M., Jonassen, I., Bolser, D.,
   Uludag, M., McWilliam, H., Malone, J., Lopez, R., Pettifer, S.,
   and Rice, P. 2013.
   "EDAM: An Ontology of Bioinformatics Operations, Types of Data and
   Identifiers, Topics and Formats."
   *Bioinformatics* 29(10): 1325--1332.
   DOI:
   `10.1093/bioinformatics/btt113 <https://doi.org/10.1093/bioinformatics/btt113>`_
