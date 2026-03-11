.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Software
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2013-07-01
       * - **Creator**
         - Allyson Lister, Andy Brown, Duncan Hull, Helen Parkinson, James Malone, Jon Ison, Nandini Badarinarayan, Robert Stevens
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Software Ontology (SWO) <https://terminology.tib.eu/ts/ontologies/SWO>`_

Software Ontology (SWO)
========================================================================================================

The Software Ontology (SWO) is a resource for describing software tools, their types, tasks, versions, provenance, and associated data. It contains detailed information on licensing and formats as well as software applications themselves, mainly (but not limited) to the bioinformatics community. It provides a structured vocabulary for representing software tools, supporting both theoretical and experimental research in software management.

The ontology employs a class-based modeling approach, defining classes for different types of software tools, tasks, and associated data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. SWO supports the integration of data from various sources, promoting interoperability and data-driven research in software management.

Typical applications of SWO include the development of new software management methods, the optimization of software tool usage, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, SWO enhances collaboration and innovation in the field of software management.

**Example Usage**:
Annotate a software tool with SWO terms to specify tool types, tasks, and associated data, enabling semantic search and integration with software management platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 11581
        * - **Total Edges**
          - 33570
        * - **Root Nodes**
          - 177
        * - **Leaf Nodes**
          - 3150
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 2746
        * - **Individuals**
          - 443
        * - **Properties**
          - 165

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
          - 3.07
        * - **Depth Variance**
          - 5.30
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 392
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 132.93
        * - **Breadth Variance**
          - 17222.21
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 440
        * - **Taxonomic Relations**
          - 5852
        * - **Non-taxonomic Relations**
          - 612
        * - **Average Terms per Type**
          - 8.30
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import SWO

    ontology = SWO()
    ontology.load("path/to/SWO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
