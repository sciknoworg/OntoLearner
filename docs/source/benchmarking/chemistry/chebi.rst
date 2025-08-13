

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

Chemical Entities of Biological Interest (ChEBI) is a dictionary of molecular entities     focused on ‘small’ chemical compounds. The term ‘molecular entity’ refers to any constitutionally     or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer, etc.,     identifiable as a separately distinguishable entity. The molecular entities in question     are either products of nature or synthetic products used to intervene in the processes of living organisms.     ChEBI incorporates an ontological classification, whereby the relationships between molecular entities     or classes of entities and their parents and/or children are specified.

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
