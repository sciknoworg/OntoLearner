.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - 1.3
       * - **Last Updated**
         - 2014-03-12
       * - **Creator**
         - http://www.isi.edu/~gil/
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Ontology for Provenance and Plans (P-Plan) <https://vocab.linkeddata.es/p-plan/index.html>`_

Ontology for Provenance and Plans (P-Plan)
========================================================================================================

The Ontology for Provenance and Plans (P-Plan) is an extension of the PROV-O ontology created to represent the plans that guide the execution of scientific processes [#pplan-ontology]_. P-Plan describes how plans are composed and how their elements correspond to provenance records that describe the execution itself [#pplan-ontology]_. It provides a structured vocabulary for representing plans, steps, variables, activities, entities, agents, and the relationships between abstract process descriptions and concrete executions [#pplan-ontology]_.

The ontology uses a class-based modeling approach, defining concepts such as ``p-plan:Plan``, ``p-plan:Step``, and ``p-plan:Variable``, together with links to execution-level provenance entities and activities [#pplan-ontology]_. This allows researchers to distinguish between the intended structure of a process and the actual provenance trace generated when that process is executed [#pplan-ontology]_. P-Plan supports interoperability between workflow descriptions, scientific process models, and provenance records by connecting planned process structures with their corresponding execution data [#pplan-ontology]_.

Typical applications of P-Plan include scientific workflow documentation, provenance tracking, process reproducibility, workflow comparison, experiment reporting, and integration of provenance data across computational research systems [#pplan-ontology]_. By connecting plans with execution provenance, P-Plan helps researchers understand how results were produced, which steps were followed, and how abstract methods correspond to concrete process executions [#pplan-ontology]_.

**Example Usage**:
Annotate a scientific process with P-Plan terms to describe the overall plan, individual steps, input and output variables, responsible agents, and the corresponding execution activities and entities generated during execution. This enables semantic search, provenance tracking, reproducibility analysis, and integration with workflow and provenance management platforms [#pplan-ontology]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 52
        * - **Total Edges**
          - 100
        * - **Root Nodes**
          - 10
        * - **Leaf Nodes**
          - 24
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 11
        * - **Individuals**
          - 0
        * - **Properties**
          - 14

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
          - 0.59
        * - **Depth Variance**
          - 0.60
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 10
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 5.67
        * - **Breadth Variance**
          - 9.56
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 16
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import PPlan

    ontology = PPlan()
    ontology.load("path/to/PPlan-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#pplan-ontology] OPMW. 2014.
   "The P-Plan Ontology."
   Available at:
   `https://www.opmw.org/model/p-plan/ <https://www.opmw.org/model/p-plan/>`_
