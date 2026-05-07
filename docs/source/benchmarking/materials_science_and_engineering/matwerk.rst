.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Research Data, Interoperability
       * - **Current Version**
         - 3.0.0
       * - **Last Updated**
         - 2025-03-01
       * - **Creator**
         - Hossein Beygi Nasrabadi, Jörg Waitelonis, Ebrahim Norouzi, Kostiantyn Hubaiev, Harald Sack
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download NFDI MatWerk Ontology (MatWerk) <https://github.com/ISE-FIZKarlsruhe/mwo?tab=readme-ov-file>`_

NFDI MatWerk Ontology (MatWerk)
========================================================================================================

The NFDI MatWerk Ontology (MWO) is a BFO-compliant ontology developed for research data management in Materials Science and Engineering (MSE) [#mwo-doc]_ [#mwo-paper]_. It provides a semantic framework for structuring MSE research data and improving interoperability, data sharing, and knowledge representation within the NFDI-MatWerk community [#mwo-doc]_ [#mwo-paper]_.

MWO incorporates the modular approach of the NFDIcore mid-level ontology and represents key MSE research-data entities such as task areas, infrastructure use cases, projects, researchers, organizations, datasets, software, workflows, ontologies, publications, metadata schemas, instruments, facilities, services, and educational resources [#mwo-doc]_. As a foundation for the MSE Knowledge Graph, MWO supports semantic annotation, data integration, retrieval, discoverability, and reuse of materials science research data [#mwo-doc]_ [#mwo-paper]_.

**Example Usage**:
Annotate a materials science research project with MWO terms to specify task areas, infrastructure use cases, participating researchers, organizations, datasets, software, workflows, instruments, and related resources, enabling semantic search and integration with the MSE Knowledge Graph [#mwo-doc]_ [#mwo-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 2554
        * - **Total Edges**
          - 4870
        * - **Root Nodes**
          - 86
        * - **Leaf Nodes**
          - 1384
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 449
        * - **Individuals**
          - 29
        * - **Properties**
          - 129

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.83
        * - **Depth Variance**
          - 5.95
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 148
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 40.00
        * - **Breadth Variance**
          - 1814.14
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 29
        * - **Taxonomic Relations**
          - 369
        * - **Non-taxonomic Relations**
          - 12
        * - **Average Terms per Type**
          - 4.14
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MatWerk

    ontology = MatWerk()
    ontology.load("path/to/MatWerk-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#mwo-doc] ISE-FIZKarlsruhe. n.d.
   "NFDI MatWerk Ontology (MWO)."
   Ontology documentation.
   Available at:
   `https://ise-fizkarlsruhe.github.io/mwo/docs/ <https://ise-fizkarlsruhe.github.io/mwo/docs/>`_

.. [#mwo-paper] Beygi Nasrabadi, H., et al. 2025.
   "NFDI MatWerk Ontology (MWO): A BFO-Compliant Ontology for Research Data Management in Materials Science and Engineering."
   *Advanced Engineering Materials*.
   DOI: 10.1002/adem.202502331.
   Available at:
   `https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202502331 <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adem.202502331>`_
