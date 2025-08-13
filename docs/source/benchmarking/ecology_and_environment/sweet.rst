

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Ecology and Environment
       * - **Category**
         - Earth Science, Geoscience
       * - **Current Version**
         - 3.6.0
       * - **Last Updated**
         - July 14, 2022
       * - **Creator**
         - NASA, JPL, Caltech
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Semantic Web for Earth and Environment Technology Ontology (SWEET) <https://bioportal.bioontology.org/ontologies/SWEET>`_

Semantic Web for Earth and Environment Technology Ontology (SWEET)
========================================================================================================

The Semantic Web for Earth and Environment Technology Ontology (SWEET) is an investigation in improving discovery     and use of Earth science data, through software understanding of the semantics of web resources.     SWEET is a collection of ontologies conceptualizing a knowledge space for Earth system science,     represented using the web ontology language (OWL). It includes both orthogonal concepts (space, time,     Earth realms, physical quantities, etc.) and integrative science knowledge concepts (phenomena, events, etc.).

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 26249
        * - **Total Edges**
          - 64544
        * - **Root Nodes**
          - 244
        * - **Leaf Nodes**
          - 11866
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 10240
        * - **Individuals**
          - 2351
        * - **Properties**
          - 358

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 15
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 3.62
        * - **Depth Variance**
          - 9.36
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 303
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 102.81
        * - **Breadth Variance**
          - 8823.90
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 2219
        * - **Taxonomic Relations**
          - 16111
        * - **Non-taxonomic Relations**
          - 515
        * - **Average Terms per Type**
          - 11.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SWEET

    ontology = SWEET()
    ontology.load("path/to/SWEET-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
