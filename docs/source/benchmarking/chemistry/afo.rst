.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Laboratory Analytical Processes
       * - **Current Version**
         - 2024-06
       * - **Last Updated**
         - 2024-06-28
       * - **Creator**
         - Allotrope Foundation
       * - **License**
         - CC BY 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Allotrope Foundation Ontology (AFO) <https://terminology.tib.eu/ts/ontologies/AFO>`_

Allotrope Foundation Ontology (AFO)
========================================================================================================

The Allotrope Foundation Ontology (AFO) is a comprehensive ontology suite designed to standardize the representation of laboratory analytical processes. It provides a semantic model and controlled vocabulary for describing key domains such as Equipment, Material, Process, and Results. The AFO is aligned with the Basic Formal Ontology (BFO) at its upper layer, ensuring compatibility with other ontological frameworks. This ontology suite is particularly valuable for integrating data from diverse laboratory systems, enabling semantic interoperability and facilitating advanced data analysis. By providing explicit definitions and relationships, the AFO supports the automation of laboratory workflows, enhances data reproducibility, and improves the traceability of analytical processes. Researchers and organizations can use the AFO to annotate experimental data, describe laboratory protocols, and ensure compliance with data standards.

**Example Usage**:
Annotate a laboratory experiment with AFO terms to specify the equipment used (e.g., "mass spectrometer"), the materials analyzed (e.g., "chemical sample"), and the processes performed (e.g., "chromatography"), along with the results obtained.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 15547
        * - **Total Edges**
          - 36699
        * - **Root Nodes**
          - 142
        * - **Leaf Nodes**
          - 8003
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3871
        * - **Individuals**
          - 38
        * - **Properties**
          - 318

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 24
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.14
        * - **Depth Variance**
          - 22.60
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 368
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 75.84
        * - **Breadth Variance**
          - 8251.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 37
        * - **Taxonomic Relations**
          - 6904
        * - **Non-taxonomic Relations**
          - 34
        * - **Average Terms per Type**
          - 3.36
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AFO

    ontology = AFO()
    ontology.load("path/to/AFO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
