.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - ttl
       * - **Download**
         - `Download Battery Interface Ontology (BattINFO) <https://github.com/BIG-MAP/BattINFO>`_

Battery Interface Ontology (BattINFO)
========================================================================================================

The Battery Interface Ontology (BattINFO) is a domain ontology developed to standardize and harmonize the representation of battery-related knowledge, data, and interfaces. BattINFO provides a structured vocabulary for describing battery materials, components, interfaces, processes, and performance metrics, supporting the annotation and integration of experimental and computational battery data. The ontology is designed to enable FAIR battery data practices, facilitating data sharing, interoperability, and reuse across research, industry, and digital platforms. BattINFO supports semantic annotation of battery experiments, manufacturing workflows, and simulation results, enabling advanced analytics, lifecycle assessment, and knowledge discovery. The ontology is extensible and can be aligned with other materials science and energy ontologies for broader compatibility. BattINFO is actively maintained and extended to incorporate new battery technologies, standards, and research requirements.

**Example Usage**:
Annotate a battery research dataset with BattINFO terms to specify electrode materials, electrolyte composition, interface properties, and performance metrics (e.g., capacity, cycle life), enabling semantic search and integration with battery databases and digital twins.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 27319
        * - **Total Edges**
          - 50787
        * - **Root Nodes**
          - 2855
        * - **Leaf Nodes**
          - 16852
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 4431
        * - **Individuals**
          - 7
        * - **Properties**
          - 304

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 27
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.09
        * - **Depth Variance**
          - 7.40
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 10695
        * - **Minimum Breadth**
          - 7
        * - **Average Breadth**
          - 827.86
        * - **Breadth Variance**
          - 4644992.84
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 10
        * - **Taxonomic Relations**
          - 195
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 10.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BattINFO

    ontology = BattINFO()
    ontology.load("path/to/BattINFO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
