

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - News and Media
       * - **Category**
         - Wildlife
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - 2013/12/18
       * - **Creator**
         - https://www.ldodds.com#me, http://tomscott.name/
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download BBC Wildlife Ontology (BBCWildlife) <https://www.bbc.co.uk/ontologies/wildlife-ontology>`_

BBC Wildlife Ontology (BBCWildlife)
========================================================================================================

The BBC Wildlife Ontology is a specialized vocabulary for describing and classifying biological species, taxa, and their ecological characteristics in a machine-readable format. It provides standardized terminology for representing biological classification hierarchies including species names, taxonomic ranks (kingdom, phylum, class, order, family, genus, species), and relationships between taxa. The ontology enables semantic annotation of wildlife information including habitat descriptions, conservation status, behavioral characteristics, geographic distribution, and ecological roles. BBCWildlife supports wildlife content discovery and semantic linking across BBC media platforms and broader biodiversity databases. The ontology facilitates knowledge integration in natural history and biodiversity research by providing standardized semantic representations of organisms and their ecological contexts. **Example Usage**: Annotate a wildlife documentary or encyclopedia entry about a species (e.g., tiger, African elephant) with BBCWildlife terms for taxonomic classification, habitat (forest, savanna, wetland), conservation status (endangered, vulnerable), behavior (predatory, migratory), and geographic distribution.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 157
        * - **Total Edges**
          - 414
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 93
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 31
        * - **Individuals**
          - 0
        * - **Properties**
          - 31

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
          - 0.67
        * - **Depth Variance**
          - 0.22
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 2
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.50
        * - **Breadth Variance**
          - 0.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 23
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BBCWildlife

    ontology = BBCWildlife()
    ontology.load("path/to/BBCWildlife-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
