

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Ecology and Environment
       * - **Category**
         - Environment, Ecosystems, Habitats
       * - **Current Version**
         - 2024-07-01
       * - **Last Updated**
         - 2024-07-01
       * - **Creator**
         - Pier Luigi Buttigieg (https://orcid.org/0000-0002-4366-3088)
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Environment Ontology (ENVO) <https://obofoundry.org/ontology/envo.html>`_

Environment Ontology (ENVO)
========================================================================================================

ENVO (Environment Ontology) is a comprehensive, community-driven
ontology for the concise, controlled description of environmental
systems, components, and processes [#envo-obo]_ [#envo-2016]_. It
provides a standardized vocabulary for describing environmental
features such as biomes, ecosystems, habitats, environmental materials,
and environmental conditions [#envo-2016]_ [#envo-obo]_. ENVO captures
semantic relationships between environmental entities and supports
precise annotation of environmental, ecological, biological, and
biomedical datasets [#envo-2016]_ [#envo-obo]_. As an open ontology
resource, ENVO promotes semantic interoperability by providing formal
definitions for environmental concepts that can be used by humans,
machines, and Semantic Web applications [#envo-obo]_ [#envo-2016]_.
The ontology supports diverse applications including environmental data
management, ecology, biodiversity and microbiome studies, and other
research that requires interoperable environmental descriptions
[#envo-2016]_ [#envo-obo]_.

**Example Usage**: Annotate an environmental dataset with ENVO terms for
a biome, habitat, environmental material, or environmental condition.
For example, use terms describing a tropical rainforest environment, a
biogeographic setting, or elevated soil moisture to enable semantic
search, cross-study integration, and automated discovery of related
environmental and ecological data [#envo-2016]_ [#envo-obo]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 43986
        * - **Total Edges**
          - 107616
        * - **Root Nodes**
          - 4449
        * - **Leaf Nodes**
          - 19297
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 9309
        * - **Individuals**
          - 44
        * - **Properties**
          - 208

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 28
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.69
        * - **Depth Variance**
          - 9.89
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 8473
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 1056.21
        * - **Breadth Variance**
          - 4840394.03
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 46
        * - **Taxonomic Relations**
          - 16175
        * - **Non-taxonomic Relations**
          - 147
        * - **Average Terms per Type**
          - 5.75
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import ENVO

    ontology = ENVO()
    ontology.load("path/to/ENVO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#envo-obo] OBO Foundry. n.d. "Environment Ontology (ENVO)."
   Available at: `https://obofoundry.org/ontology/envo.html <https://obofoundry.org/ontology/envo.html>`_

.. [#envo-2016] Buttigieg, P. L., Pafilis, E., Lewis, S. E.,
   Schildhauer, M. P., Walls, R. L., and Mungall, C. J. 2016.
   "The Environment Ontology in 2016: Bridging Domains with Increased
   Scope, Semantic Density, and Interoperation."
   *Journal of Biomedical Semantics* 7:57.
   doi:10.1186/s13326-016-0097-6
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC5035502/>`_
