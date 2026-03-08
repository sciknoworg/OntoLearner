.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Mechanical Testing
       * - **Current Version**
         - 1.0.0
       * - **Last Updated**
         - None
       * - **Creator**
         - Fraunhofer IWM
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Mechanical Testing Ontology (MechanicalTesting) <https://github.com/emmo-repo/domain-mechanical-testing>`_

Mechanical Testing Ontology (MechanicalTesting)
========================================================================================================

The Mechanical Testing Ontology (MechanicalTesting) is a domain ontology developed to represent knowledge in the field of mechanical testing, based on the Elementary Multiperspective Material Ontology (EMMO). It provides a structured vocabulary for describing mechanical testing methods, equipment, and results, supporting both experimental and computational research in materials science.

The ontology employs a class-based modeling approach, defining classes for different types of mechanical tests, equipment, and results, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. MechanicalTesting supports the integration of data from experimental studies and simulations, promoting interoperability and data-driven research in mechanical testing.

Typical applications of MechanicalTesting include the development of new testing methods, the optimization of testing procedures, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, MechanicalTesting enhances collaboration and innovation in the field of mechanical testing.

**Example Usage**:
Annotate a mechanical testing dataset with MechanicalTesting terms to specify test types, equipment, and results, enabling semantic search and integration with materials informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1365
        * - **Total Edges**
          - 2569
        * - **Root Nodes**
          - 174
        * - **Leaf Nodes**
          - 713
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 369
        * - **Individuals**
          - 0
        * - **Properties**
          - 5

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 18
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.14
        * - **Depth Variance**
          - 4.98
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 466
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 66.89
        * - **Breadth Variance**
          - 14051.46
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 36
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MechanicalTesting

    ontology = MechanicalTesting()
    ontology.load("path/to/MechanicalTesting-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
