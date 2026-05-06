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

SP-Workflow module represents: i) the executable elements of a protocol; ii) the experimental actions and material entities that participate in instructions, such as samples/specimens, organisms, reagents, and instruments; and iii) the order of execution of the instructions [#sp-workflow]_ [#sp-github]_. It provides a structured vocabulary for representing workflows, experimental actions, protocol instructions, material entities, and related data, supporting semantic representation of experimental protocol execution [#sp-workflow]_.

The ontology employs a class-based modeling approach, defining classes for different types of protocol instructions, experimental actions, workflow elements, samples/specimens, organisms, reagents, instruments, and related data, along with properties to describe their characteristics and interactions [#sp-workflow]_. Hierarchies and relations are used to organize workflow concepts into structured categories, enabling retrieval, comparison, and analysis of experimental protocol workflows [#sp-workflow]_. SP-Workflow supports the integration of protocol workflow information from various sources, promoting interoperability and data-driven research in experimental workflow management [#sp-github]_.

Typical applications of SP-Workflow include the semantic representation of experimental protocol execution, documentation of protocol instructions, optimization of experimental workflows, workflow comparison, protocol retrieval, and integration of workflow descriptions with laboratory information systems and workflow management platforms [#sp-workflow]_ [#sp-github]_. By providing a standardized vocabulary and framework, SP-Workflow enhances interoperability, reuse, and semantic search in the field of experimental workflow documentation [#sp-workflow]_.

**Example Usage**:
Annotate an experimental workflow with SP-Workflow terms to specify protocol instructions, workflow steps, experimental actions, samples/specimens, organisms, reagents, instruments, and the order in which instructions should be executed. This enables semantic search, workflow comparison, protocol reuse, and integration with workflow management platforms [#sp-workflow]_ [#sp-github]_.

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

References
----------

.. [#sp-workflow] SMART Protocols. 2013.
   "SMART Protocols Ontology: Workflow Module."
   Available at:
   `https://vocab.linkeddata.es/SMARTProtocols/myDocumentation_SPwf_19Abril2017/index_SPwf_V4.0.html <https://vocab.linkeddata.es/SMARTProtocols/myDocumentation_SPwf_19Abril2017/index_SPwf_V4.0.html>`_

.. [#sp-github] Ontology Engineering Group, Universidad Politécnica de Madrid. n.d.
   "SMART-Protocols."
   GitHub Repository.
   Available at:
   `https://github.com/oeg-upm/SMART-Protocols <https://github.com/oeg-upm/SMART-Protocols>`_
