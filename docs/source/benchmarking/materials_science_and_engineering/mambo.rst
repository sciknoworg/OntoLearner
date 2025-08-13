

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - General Public License v3.0 (GPL-3.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Molecules And Materials Basic Ontology (MAMBO) <https://github.com/daimoners/MAMBO>`_

Molecules And Materials Basic Ontology (MAMBO)
========================================================================================================

MAMBO (Molecules And Materials Basic Ontology) is a domain ontology for molecular materials.     Its main targets are: Allowing the retrieval of structured information regarding molecular materials     and related applications (i.e. devices based on molecular materials) Supporting the development of new,     complex workflows for modelling systems based on molecular materials (computational modelling     and data-driven techniques) Integrating data generated via computational simulations and empirical experiments.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 166
        * - **Total Edges**
          - 624
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 7
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 57
        * - **Individuals**
          - 0
        * - **Properties**
          - 104

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
          - 0.50
        * - **Depth Variance**
          - 0.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 1
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 39
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MAMBO

    ontology = MAMBO()
    ontology.load("path/to/MAMBO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
