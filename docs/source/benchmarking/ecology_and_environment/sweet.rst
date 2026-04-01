

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
SWEET (Semantic Web for Earth and Environmental Terminology) is a
comprehensive collection of interconnected ontologies designed to
improve discovery and use of Earth science data through semantic
understanding of web resources and Earth system science concepts
[#sweet-paper]_ [#sweet-repo]_. It conceptualizes a knowledge space for
Earth system science that includes cross-cutting concepts such as
space, time, Earth realms, phenomena, physical quantities, and units,
alongside more domain-specific scientific concepts [#sweet-paper]_
[#sweet-repo]_. SWEET is represented in OWL and organized as a highly
modular ontology suite, enabling semantic interoperability and automated
reasoning in Earth and environmental science applications
[#sweet-paper]_ [#sweet-repo]_. The ontology supports integration of
heterogeneous Earth science datasets and models by providing shared
semantic definitions across domains such as atmospheric science,
oceanography, geology, and climate science [#sweet-paper]_
[#sweet-search]_. By providing a shared semantic framework, SWEET
supports Earth science data discovery, semantic search, and knowledge
management across distributed datasets and services [#sweet-paper]_
[#sweet-search]_.

**Example Usage**: Annotate a climate or Earth observation dataset with
SWEET terms to describe observed phenomena, Earth realm or layer,
spatial and temporal context, and relevant physical quantities and
units, enabling semantic search, automated linking of related datasets,
and interoperable Earth science analysis [#sweet-paper]_ [#sweet-repo]_.

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

References
----------

.. [#sweet-paper] Raskin, R. G., and Pan, M. J. 2005.
   "Knowledge Representation in the Semantic Web for Earth and
   Environmental Terminology (SWEET)."
   *Computers & Geosciences* 31(9): 1119-1125.
   Available at: `https://www.sciencedirect.com/science/article/pii/S0098300405001020 <https://www.sciencedirect.com/science/article/pii/S0098300405001020>`_

.. [#sweet-repo] ESIP Federation. n.d.
   "SWEET: Official repository for Semantic Web for Earth and
   Environmental Terminology Ontologies."
   Available at: `https://github.com/ESIPFed/sweet <https://github.com/ESIPFed/sweet>`_

.. [#sweet-search] Pouchard, L. C., Huhns, M. N., and McGuinness, D. L.
   2013. "Linking Earth and Climate Science to Support Semantic Search."
   *Semantic Web*.
   Available at: `https://semantic-web-journal.net/content/linking-earth-and-climate-science-semantic-search-supporting-investigation-climate-change <https://semantic-web-journal.net/content/linking-earth-and-climate-science-semantic-search-supporting-investigation-climate-change>`_
