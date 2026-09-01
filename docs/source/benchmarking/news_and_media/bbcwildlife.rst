

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

The BBC Wildlife Ontology is a lightweight ontology for describing biological species and related taxa [#bbcwildlife-ontology]_. It provides a structured vocabulary for describing taxon names and ranks, relationships between taxa, habitats, conservation status, modes of life, behavioural characteristics, and topic relations to web documents or multimedia objects featuring a taxon [#bbcwildlife-ontology]_.

The ontology was originally designed to support data publishing for the BBC Wildlife Finder application, but it is intended to be applicable to a wider range of biological data publishing use cases [#bbcwildlife-ontology]_. It is designed to interoperate with more specialized ontologies used in taxonomy, ecology, environmental science, and bioinformatics [#bbcwildlife-ontology]_. By providing standardized terms for taxa and wildlife-related information, the BBC Wildlife Ontology supports semantic annotation, linked-data publishing, content discovery, and integration of biodiversity-related information [#bbcwildlife-ontology]_.

**Example Usage**:
Annotate a wildlife documentary or species entry with BBC Wildlife Ontology terms to specify a taxon, its rank, habitat, conservation status, mode of life, behavioural characteristics, and related multimedia content, enabling semantic search and integration across wildlife and biodiversity data platforms [#bbcwildlife-ontology]_.

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

References
----------

.. [#bbcwildlife-ontology] BBC. 2013.
   "Wildlife Ontology."
   Available at:
   `https://iptc.org/thirdparty/bbc-ontologies/wo.html <https://iptc.org/thirdparty/bbc-ontologies/wo.html>`_
