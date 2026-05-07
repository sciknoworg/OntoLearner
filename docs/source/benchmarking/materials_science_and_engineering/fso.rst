.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.1.0
       * - **Last Updated**
         - 2020-08-06
       * - **Creator**
         - Ali Kücükavci, Mads Holten Rasmussen, Ville Kukkonen
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Flow Systems Ontology (FSO) <https://github.com/alikucukavci/FSO/>`_

Flow Systems Ontology (FSO)
========================================================================================================

The Flow Systems Ontology (FSO) is a domain ontology developed to describe interconnected systems with material or energy flow connections and their components [#fso-doc]_ [#kukkonen2021]_. FSO provides a structured vocabulary for representing flow systems, components, distribution systems, supply systems, return systems, segments, terminals, storage devices, flow controllers, flow-moving devices, and treatment devices [#fso-doc]_.

The ontology supports the description of system composition and mass or energy flows between systems and components, enabling semantic annotation, interoperability, data integration, and querying across building and engineering workflows [#kukkonen2021]_. FSO was proposed to support flow-system descriptions from design to operation of buildings and was demonstrated using example models and SPARQL queries [#kukkonen2021]_. By providing a standardized semantic framework, FSO supports process modelling, simulation, and knowledge sharing across flow-system-related engineering domains [#fso-doc]_ [#kukkonen2021]_.

**Example Usage**:
Annotate a building or process-engineering model with FSO terms to specify flow-system structure, supply and return systems, components such as pumps, valves, ducts, pipes, terminals, and storage devices, and the material or energy flows between them. This enables semantic search, querying, and integration with building information modelling and engineering databases [#fso-doc]_ [#kukkonen2021]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 141
        * - **Total Edges**
          - 279
        * - **Root Nodes**
          - 10
        * - **Leaf Nodes**
          - 56
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 14
        * - **Individuals**
          - 1
        * - **Properties**
          - 22

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
          - 0.17
        * - **Depth Variance**
          - 0.14
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 10
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 6.00
        * - **Breadth Variance**
          - 16.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 11
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import FSO

    ontology = FSO()
    ontology.load("path/to/FSO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#fso-doc] Kücükavci, A. n.d.
   "Flow Systems Ontology."
   Ontology documentation.
   Available at:
   `https://alikucukavci.github.io/FSO/ <https://alikucukavci.github.io/FSO/>`_

.. [#kukkonen2021] Kukkonen, V., Kücükavci, A., Seidenschnur, M., Rasmussen, M. H., Smith, K. M., and Hviid, C. A. 2021.
   "An ontology to support flow system descriptions from design to operation of buildings."
   *Automation in Construction*, 134, Article 104067.
   DOI: 10.1016/j.autcon.2021.104067.
   Available at:
   `https://doi.org/10.1016/j.autcon.2021.104067 <https://doi.org/10.1016/j.autcon.2021.104067>`_
