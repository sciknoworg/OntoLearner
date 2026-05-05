

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2025-03-11
       * - **Creator**
         - University of Warsaw
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Physico-chemical process ontology (REX) <https://terminology.tib.eu/ts/ontologies/REX>`_

Physico-chemical process ontology (REX)
========================================================================================================

REX is an ontology for the formal representation of physico-chemical
processes, including both microscopic molecular transformations and
macroscopic chemical phenomena [#rex-obo]_ [#rex-bioportal]_. It
provides a structured vocabulary for describing processes at different
scales, such as molecular-level processes involving chemical bond
changes, molecular rearrangements, and electron transfer, as well as
macroscopic processes such as phase changes, dissolution, and
crystallization [#rex-obo]_ [#rex-bioportal]_. REX distinguishes
between different process types and supports formal representation of
chemical transformations in a standardized and machine-readable way
[#rex-obo]_ [#rex-bioportal]_. By providing explicit process
definitions, the ontology supports knowledge integration across
chemistry databases, computational chemistry platforms, and related
scientific data systems [#rex-obo]_ [#rex-bioportal]_.

**Example Usage**: Represent a multi-step chemical transformation using
REX terms to describe molecular-level processes such as oxidation or
substitution, together with their sequence and relationships, enabling
structured representation and semantic querying of complex
physico-chemical processes [#rex-obo]_ [#rex-bioportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2461
        * - **Total Edges**
          - 5630
        * - **Root Nodes**
          - 356
        * - **Leaf Nodes**
          - 1457
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 552
        * - **Individuals**
          - 0
        * - **Properties**
          - 6

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
          - 1.35
        * - **Depth Variance**
          - 0.97
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 978
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 304.57
        * - **Breadth Variance**
          - 116930.53
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 953
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import REX

    ontology = REX()
    ontology.load("path/to/REX-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#rex-obo] OBO Foundry. n.d. "Physico-chemical process."
   Available at: `https://obofoundry.org/ontology/rex.html <https://obofoundry.org/ontology/rex.html>`_

.. [#rex-bioportal] NCBO BioPortal. n.d. "Physico-Chemical Process (REX)."
   Available at: `https://bioportal.bioontology.org/ontologies/REX <https://bioportal.bioontology.org/ontologies/REX>`_
