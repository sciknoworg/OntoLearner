.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Workflows
       * - **Current Version**
         - 4.0
       * - **Last Updated**
         - 2013-07-01
       * - **Creator**
         - http://oxgiraldo.wordpress.com
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download SMART Protocols Ontology: Workflow Module (SP-Workflow) <https://github.com/SMARTProtocols/SMART-Protocols>`_

SMART Protocols Ontology: Workflow Module (SP-Workflow)
========================================================================================================

SP-Workflow module represents: i) the executable elements of a protocol; ii) the experimental actions and material entities that participate in instructions (sample/specimen, organisms, reagents, instruments); and iii) the order of execution of the instructions. It provides a structured vocabulary for representing workflows, experimental actions, and related data, supporting both theoretical and experimental research in workflow management.

The ontology employs a class-based modeling approach, defining classes for different types of workflows, experimental actions, and related data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. SP-Workflow supports the integration of data from various sources, promoting interoperability and data-driven research in workflow management.

Typical applications of SP-Workflow include the development of new workflow management methods, the optimization of experimental workflows, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, SP-Workflow enhances collaboration and innovation in the field of workflow management.

**Example Usage**:
Annotate an experimental workflow with SP-Workflow terms to specify workflow steps, experimental actions, and related data, enabling semantic search and integration with workflow management platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1446
        * - **Total Edges**
          - 3017
        * - **Root Nodes**
          - 4
        * - **Leaf Nodes**
          - 834
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 419
        * - **Individuals**
          - 5
        * - **Properties**
          - 17

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
          - 7.23
        * - **Depth Variance**
          - 8.19
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 36
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 14.07
        * - **Breadth Variance**
          - 120.78
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 5
        * - **Taxonomic Relations**
          - 577
        * - **Non-taxonomic Relations**
          - 22
        * - **Average Terms per Type**
          - 1.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SPWorkflow

    ontology = SPWorkflow()
    ontology.load("path/to/SPWorkflow-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
