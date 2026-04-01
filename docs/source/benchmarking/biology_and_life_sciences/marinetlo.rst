

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Marine Science, Oceanography
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2017-01-05
       * - **Creator**
         - Information System Laboratory (ISL), Institute of Computer Science (ICS), Foundation for Research and Technology - Hellas (FORTH)
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Marine Taxonomy and Life Ontology (MarineTLO) <https://projects.ics.forth.gr/isl/MarineTLO/>`_

Marine Taxonomy and Life Ontology (MarineTLO)
========================================================================================================

MarineTLO is a top-level ontology for the marine domain, designed to
provide consistent abstractions for concepts appearing across marine
data models and ontologies. It provides the properties needed to make a
distributed marine knowledge base a coherent source of facts, relating
observational data to spatiotemporal context and categorical
(systematic) domain knowledge [#marinetlo-site]_ [#marinetlo-paper]_.
It can be used as a core schema for publishing linked data and for
building integration systems for the marine domain [#marinetlo-site]_
[#marinetlo-paper]_. MarineTLO is generic enough to be extended to
different levels of detail while preserving monotonicity, and it has
been implemented in OWL 2 and evaluated through competency queries that
capture domain requirements provided by related communities
[#marinetlo-site]_ [#marinetlo-doc]_. By providing a shared top-level
semantic framework, MarineTLO supports semantic interoperability and the
integration of heterogeneous marine biodiversity and observation data
across distributed sources [#marinetlo-paper]_ [#marinetlo-site]_.

**Example Usage**: Use MarineTLO as a core schema to integrate marine
species, observations, habitats, and sampling-event data from multiple
sources, linking each observation to its taxonomic, spatial, and
temporal context to enable semantic querying and interoperable analysis
across marine biodiversity datasets [#marinetlo-paper]_
[#marinetlo-site]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 372
        * - **Total Edges**
          - 1205
        * - **Root Nodes**
          - 3
        * - **Leaf Nodes**
          - 171
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 104
        * - **Individuals**
          - 3
        * - **Properties**
          - 94

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 2
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.75
        * - **Depth Variance**
          - 0.44
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 4
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 2.67
        * - **Breadth Variance**
          - 1.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1
        * - **Taxonomic Relations**
          - 113
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MarineTLO

    ontology = MarineTLO()
    ontology.load("path/to/MarineTLO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#marinetlo-site] Institute of Computer Science, FORTH. 2020.
   "MarineTLO | A Top Level Ontology for the Marine/Biodiversity Domain."
   Available at: `https://projects.ics.forth.gr/isl/MarineTLO/ <https://projects.ics.forth.gr/isl/MarineTLO/>`_

.. [#marinetlo-doc] Tzitzikas, Y., and collaborators. n.d.
   "MarineTLO: A Top Level Ontology for the Marine Domain."
   Documentation.
   Available at: `https://projects.ics.forth.gr/isl/MarineTLO/files/MarineTLO.pdf <https://projects.ics.forth.gr/isl/MarineTLO/files/MarineTLO.pdf>`_

.. [#marinetlo-paper] Tzitzikas, Y., Allocca, C., Bekiari, C.,
   Marketakis, Y., Fafalios, P., Doerr, M., Minadakis, N., Patkos, T.,
   and Candela, L. 2016. "Unifying Heterogeneous and Distributed
   Information about Marine Species through the Top Level Ontology
   MarineTLO."
   *Program* 50(1): 16-40.
   doi:10.1108/PROG-10-2014-0072
   Available at: `https://www.vliz.be/imisdocs/publications/283055.pdf <https://www.vliz.be/imisdocs/publications/283055.pdf>`_
