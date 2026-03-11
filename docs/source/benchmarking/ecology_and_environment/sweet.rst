

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

SWEET is a comprehensive collection of interconnected ontologies designed to enhance discovery and utilization of Earth science data through semantic understanding of web resources and Earth system science concepts. It conceptualizes a knowledge space for Earth system science including orthogonal (cross-cutting) concepts such as space, time, Earth realms (atmosphere, hydrosphere, lithosphere), physical quantities, and units, alongside integrative science knowledge concepts such as phenomena, events, and processes. SWEET is represented in OWL (Web Ontology Language) to enable automated reasoning and semantic interoperability in Earth science research. The ontology supports integration of heterogeneous Earth science datasets and models by providing shared semantic definitions across atmospheric science, oceanography, geology, and climate science domains. SWEET facilitates Earth science data discovery and knowledge management by enabling semantic search and automated linking of related datasets and research findings.

**Example Usage**: Annotate a climate dataset with SWEET terms to describe measured phenomena (e.g., "temperature increase"), spatial context (e.g., "atmosphere" realm, "troposphere" layer), temporal extent (e.g., "1980-2020"), and physical quantities (e.g., "degrees Celsius").

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
