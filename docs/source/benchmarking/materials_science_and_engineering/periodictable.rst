.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Periodic Table of Elements
       * - **Current Version**
         - 1.10
       * - **Last Updated**
         - 2004/02/05
       * - **Creator**
         - Michael Cook
       * - **License**
         - None
       * - **Format**
         - owl
       * - **Download**
         - `Download Periodic Table of the Elements Ontology (PeriodicTable) <https://www.daml.org/2003/01/periodictable/>`_

Periodic Table of the Elements Ontology (PeriodicTable)
========================================================================================================

The Periodic Table of the Elements Ontology (PeriodicTable) is an OWL
representation of the Periodic Table of the Elements designed to provide
reference data for Semantic Web applications in chemistry and related
disciplines [#periodictable]_. Michael Cook developed the initial
representation in DAML+OIL, which was subsequently converted to OWL and
maintained by Mike Dean [#periodictable]_.

PeriodicTable provides machine-readable descriptions of chemical elements
and their associated information, allowing element data to be represented
and queried using Semantic Web technologies. Properties represented in the
ontology include information such as element names, symbols, atomic numbers,
atomic weights, and periodic-table groups [#periodictable]_.

Ontology-based representations of the periodic table have also been explored
in subsequent work. Liu and He developed the Ontology of Chemical Elements
(OCE), in which chemical-element attributes and logical axioms were used to
support automated classification and reasoning. Their study demonstrated that
ontology-based reasoning could reconstruct major structural features of
Mendeleev's Periodic Table and support prediction of element characteristics
[#oce]_. OCE is a separate ontology from PeriodicTable, but illustrates the
broader use of ontological representations for organizing and reasoning over
knowledge about chemical elements.

**Example Usage**:

Use PeriodicTable to represent or query chemical elements according to
properties such as their name, symbol, atomic number, atomic weight, or
periodic-table group, enabling structured access to element information in
Semantic Web applications.
Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 730
        * - **Total Edges**
          - 1845
        * - **Root Nodes**
          - 2
        * - **Leaf Nodes**
          - 521
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 6
        * - **Individuals**
          - 156
        * - **Properties**
          - 13

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 1
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.75
        * - **Depth Variance**
          - 0.19
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 6
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 4.00
        * - **Breadth Variance**
          - 4.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 150
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 25.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PeriodicTable

    ontology = PeriodicTable()
    ontology.load("path/to/PeriodicTable-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#periodictable] M. Cook,
   "Periodic Table in OWL,"
   DAML.org.
   Available: https://www.daml.org/2003/01/periodictable/

.. [#oce] K. Liu and Y. He,
   "Ontological Derivation of Mendeleev's Periodic Table of Chemical Elements,"
   in *Proceedings of the 10th International Conference on Biomedical Ontology
   (ICBO 2019)*, Buffalo, NY, USA, 2019.
   Available: https://ceur-ws.org/Vol-2931/ICBO_2019_paper_39.pdf
