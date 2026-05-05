

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - General
       * - **Current Version**
         - 2.0
       * - **Last Updated**
         - 2024-11-06
       * - **Creator**
         - None
       * - **License**
         - BSD-3-Clause license
       * - **Format**
         - ttl
       * - **Download**
         - `Download Common Core Ontologies (CCO) <https://github.com/CommonCoreOntology/CommonCoreOntologies>`_

Common Core Ontologies (CCO)
========================================================================================================

The Common Core Ontologies (CCO) are a suite of eleven interconnected
mid-level ontologies that provide logically well-defined generic terms
and relations applicable across many domains of interest [#cco-repo]_
[#cco-paper]_. CCO extends the Basic Formal Ontology (BFO), an upper-level
ontology, and is designed to support semantic interoperability, data
integration, and reusable domain ontology development [#cco-repo]_.

CCO is built on formal semantic principles, ensuring that its concepts
are unambiguous, semantically consistent, and suitable for computational
reasoning [#cco-paper]_. The ontology suite covers foundational concepts
including objects, processes, qualities, information entities, locations,
units of measure, agents, artifacts, facilities, and relations between
entities [#cco-repo]_ [#cco-paper]_. Its terms are intended to be reused
and extended by domain-specific ontologies while preserving compatibility
with other CCO- and BFO-based systems [#cco-repo]_.

The ontologies are documented with formal definitions, examples, and
design patterns that support both human understanding and automated
reasoning [#cco-paper]_. CCO can be used in enterprise information
systems, knowledge graph construction, semantic data integration, and
ontology engineering projects that require rigorous semantic foundations
[#cco-repo]_ [#cco-paper]_.

**Example Usage**: Represent a business domain ontology by extending
CCO's generic Object, Agent, Organization, and Event/Process concepts to
define company-specific entities such as employees, contracts,
transactions, departments, and business activities. This helps ensure
that the business ontology remains compatible with other systems using
CCO or BFO-based semantic foundations [#cco-repo]_ [#cco-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 6002
        * - **Total Edges**
          - 13554
        * - **Root Nodes**
          - 19
        * - **Leaf Nodes**
          - 3389
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1539
        * - **Individuals**
          - 350
        * - **Properties**
          - 277

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 10
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.35
        * - **Depth Variance**
          - 5.00
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 56
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 23.18
        * - **Breadth Variance**
          - 276.88
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 362
        * - **Taxonomic Relations**
          - 1532
        * - **Non-taxonomic Relations**
          - 21
        * - **Average Terms per Type**
          - 10.06
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CCO

    ontology = CCO()
    ontology.load("path/to/CCO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------------
.. [#cco-repo] Common Core Ontology Repository. n.d.
   "The Common Core Ontologies."
   GitHub Repository.
   Available at:
   `https://github.com/CommonCoreOntology/CommonCoreOntologies <https://github.com/CommonCoreOntology/CommonCoreOntologies>`_

.. [#cco-paper] Jensen, M., De Colle, G., Kindya, S., More, C.,
   Cox, A. P., and Beverley, J. 2024.
   "The Common Core Ontologies."
   arXiv.
   Available at:
   `https://arxiv.org/abs/2404.17758 <https://arxiv.org/abs/2404.17758>`_
