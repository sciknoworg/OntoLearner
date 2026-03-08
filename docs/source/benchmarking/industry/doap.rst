

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Industry
       * - **Category**
         - Software
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2020-04-03
       * - **Creator**
         - Edd Wilder-James
       * - **License**
         - Apache License 2.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download The Description of a Project vocabulary (DOAP) <https://github.com/ewilderj/doap/blob/master/schema/doap.rdf>`_

The Description of a Project vocabulary (DOAP)
========================================================================================================

The Description of a Project (DOAP) vocabulary is an RDF/OWL-based ontology for machine-readable description of software projects, particularly open source initiatives. It models core project entities such as Project, Person, Revision, Repository, and License, capturing essential metadata about software development and distribution. DOAP enables representation of project attributes including name, description, homepage, version control systems (Git, SVN), issue tracking systems, programming languages, release history, and developer/maintainer information. The vocabulary facilitates integration of project data across diverse repositories, forges, and development platforms, supporting automated project discovery, dependency analysis, and ecosystem mapping. DOAP enables research on software development practices, project evolution, and open source community dynamics through structured, interoperable metadata.

**Example Usage**: Describe an open source project with DOAP properties like foaf:name (project name), doap:repository (code repository URL), doap:programming-language (Python), doap:maintainer (developer agent), and doap:license (CC0 or Apache 2.0).

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 496
        * - **Total Edges**
          - 634
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 435
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 14
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

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
          - 0.75
        * - **Depth Variance**
          - 0.19
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 3
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 2.00
        * - **Breadth Variance**
          - 1.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 14
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DOAP

    ontology = DOAP()
    ontology.load("path/to/DOAP-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
