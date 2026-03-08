.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Education
       * - **Category**
         - Computer Science
       * - **Current Version**
         - 0.1.0
       * - **Last Updated**
         - None
       * - **Creator**
         - Jhon Toledo, Miguel Angel García, Oscar Corcho
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - rdf
       * - **Download**
         - `Download Common Ontology (Common) <https://w3id.org/mobility/trias/common/0.1.0>`_

Common Ontology (Common)
========================================================================================================

The Common Ontology provides a foundational vocabulary for representing shared and reusable elements used across the Trias (Transport and Mobility) ontology framework. It defines core concepts such as entities, attributes, relationships, and constraints that are applicable to multiple mobility and transportation domains. The ontology captures common modeling patterns for representing agents, organizations, times, locations, and relationships in a standardized way across diverse transportation contexts. Common Ontology enables semantic interoperability across Trias domain modules (mobility, traffic, vehicles) by providing consistent foundational concepts and relationships. It serves as the shared semantic backbone for specialized domain ontologies in transportation, facilitating knowledge integration and reasoning.

**Example Usage**:
Use Common Ontology entity types to represent agents (persons, organizations), locations (stops, streets, zones), time concepts, and relationships across transportation domain ontologies that extend or reference Common.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 67
        * - **Total Edges**
          - 131
        * - **Root Nodes**
          - 8
        * - **Leaf Nodes**
          - 30
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 6
        * - **Individuals**
          - 0
        * - **Properties**
          - 15

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
          - 0.27
        * - **Depth Variance**
          - 0.20
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 8
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 5.50
        * - **Breadth Variance**
          - 6.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Common

    ontology = Common()
    ontology.load("path/to/Common-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
