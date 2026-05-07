

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.0.1
       * - **Last Updated**
         - None
       * - **Creator**
         - Casper Welzel Andersen, Simon Clark
       * - **License**
         - Creative Commons license Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download EMMO Domain Ontology for Photovoltaics (Photovoltaics) <https://github.com/emmo-repo/domain-photovoltaics>`_

EMMO Domain Ontology for Photovoltaics (Photovoltaics)
========================================================================================================
The EMMO Domain Ontology for Photovoltaics is an EMMO-based domain ontology for representing knowledge in the photovoltaics domain [#photovoltaics-github]_. The repository describes the ontology as focused on perovskite solar cells, while the ontology metadata identifies it as a top-level photovoltaics domain ontology based on EMMO [#photovoltaics-github]_.

The ontology provides structured vocabulary for describing photovoltaic concepts such as photovoltaic devices, photovoltaic cells, photovoltaic modules, perovskite molecular entities, transport layers, substrate preparation, cell area, substrate area, storing before measurement, and photovoltaic quantities [#photovoltaics-github]_. By providing an EMMO-aligned semantic framework, the ontology supports semantic annotation, interoperability, data integration, and reuse of photovoltaic research information [#photovoltaics-github]_.

**Example Usage**:
Annotate a perovskite solar cell research dataset with Photovoltaics ontology terms to specify photovoltaic devices, photovoltaic cells, modules, perovskite molecular entities, hole transport layers, substrate cleaning, substrate area, cell area, and measurement-related information, enabling semantic search and integration with materials informatics platforms [#photovoltaics-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 131
        * - **Total Edges**
          - 281
        * - **Root Nodes**
          - 12
        * - **Leaf Nodes**
          - 48
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 47
        * - **Individuals**
          - 0
        * - **Properties**
          - 3

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
          - 0.40
        * - **Depth Variance**
          - 0.24
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 12
        * - **Minimum Breadth**
          - 8
        * - **Average Breadth**
          - 10.00
        * - **Breadth Variance**
          - 4.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 46
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Photovoltaics

    ontology = Photovoltaics()
    ontology.load("path/to/Photovoltaics-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#photovoltaics-github] EMMO-repo. n.d.
   "Photovoltaics - EMMO domain ontology."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/domain-photovoltaics <https://github.com/emmo-repo/domain-photovoltaics>`_
