

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - General Knowledge
       * - **Category**
         - Metadata
       * - **Current Version**
         - 1.1
       * - **Last Updated**
         - February 17, 2017
       * - **Creator**
         - The Dublin Core Metadata Initiative
       * - **License**
         - Public Domain
       * - **Format**
         - rdf
       * - **Download**
         - `Download Dublin Core Vocabulary (DublinCore) <https://bioportal.bioontology.org/ontologies/DC>`_

Dublin Core Vocabulary (DublinCore)
========================================================================================================

The Dublin Core Schema is a compact but powerful metadata vocabulary for
describing resources across diverse domains [#dublin-core]_
[#dublin-core-paper]_. It provides a set of fifteen core metadata
elements, including title, creator, subject, description, publisher,
contributor, date, type, format, identifier, source, language, relation,
coverage, and rights, which are broadly applicable to many types of
resources [#dublin-core]_.

Dublin Core metadata can be used for simple resource description,
cross-standard metadata interoperability, and resource discovery on the
Internet [#dublin-core-paper]_. The vocabulary supports basic resource
description using the Dublin Core Metadata Element Set and can be used
in digital libraries, repositories, archives, government systems,
scientific institutions, and business information systems
[#dublin-core]_ [#dublin-core-paper]_.

Dublin Core is language-independent and widely used for resource
description and discovery across heterogeneous information systems
[#dublin-core-paper]_. By providing standardized metadata terms, it
supports semantic interoperability and enables automated resource
discovery, citation, description, and management [#dublin-core]_
[#dublin-core-paper]_.

**Example Usage**: Annotate a research dataset or publication with
Dublin Core terms such as title, creator, date, subject, description,
format, identifier, and rights. This allows the resource to be discovered,
cited, exchanged, and integrated across digital repositories and metadata
systems using a common semantic description model [#dublin-core]_
[#dublin-core-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 296
        * - **Total Edges**
          - 632
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 210
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 11
        * - **Individuals**
          - 26
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
          - 0.50
        * - **Depth Variance**
          - 0.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 1
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 1.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 30
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 3.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DublinCore

    ontology = DublinCore()
    ontology.load("path/to/DublinCore-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------------
.. [#dublin-core] Dublin Core Metadata Initiative. 2020.
   "Dublin Core Metadata Element Set, Version 1.1."
   Available at:
   `https://www.dublincore.org/documents/dces/ <https://www.dublincore.org/documents/dces/>`_

.. [#dublin-core-paper] Sugimoto, S., Baker, T., and Weibel, S. L. 2002.
   "Dublin Core: Process and Principles."
   In *Digital Libraries: People, Knowledge, and Technology*,
   ICADL 2002, Lecture Notes in Computer Science, vol. 2555,
   pp. 25--35. Springer, Berlin, Heidelberg.
   DOI:
   `10.1007/3-540-36227-4_3 <https://doi.org/10.1007/3-540-36227-4_3>`_
