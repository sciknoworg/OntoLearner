.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Testings
       * - **Current Version**
         - 0.4
       * - **Last Updated**
         - 04/16/2021
       * - **Creator**
         - Markus Schilling, markus.schilling@bam.de; Philipp von Hartrott, philipp.von.hartrott@iwm.fraunhofer.de
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - rdf
       * - **Download**
         - `Download Matolab Tensile Test Ontology (MOL_TENSILE) <https://matportal.org/ontologies/MOL_TENSILE>`_

Matolab Tensile Test Ontology (MOL_TENSILE)
========================================================================================================

The Matolab Tensile Test Ontology (MOL_TENSILE) is a domain ontology developed to describe the tensile test process [#moltensile-matportal]_. It provides a structured vocabulary for representing tensile testing methods, equipment, test-related entities, and results in materials testing workflows [#moltensile-matportal]_.

MOL_TENSILE supports semantic annotation and integration of tensile testing data, enabling interoperability, semantic search, and reuse in materials informatics platforms [#moltensile-matportal]_. By providing a standardized vocabulary for tensile testing, the ontology helps organize experimental testing information and supports knowledge sharing in materials testing applications [#moltensile-matportal]_.

**Example Usage**:
Annotate a tensile testing dataset with MOL_TENSILE terms to specify test types, equipment, testing conditions, and results, enabling semantic search and integration with materials informatics platforms [#moltensile-matportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1970
        * - **Total Edges**
          - 3602
        * - **Root Nodes**
          - 132
        * - **Leaf Nodes**
          - 1245
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 371
        * - **Individuals**
          - 20
        * - **Properties**
          - 95

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 90
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 16.30
        * - **Depth Variance**
          - 665.10
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 285
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 11.49
        * - **Breadth Variance**
          - 1763.74
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 20
        * - **Taxonomic Relations**
          - 370
        * - **Non-taxonomic Relations**
          - 20
        * - **Average Terms per Type**
          - 6.67
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MOLTENSILE

    ontology = MOLTENSILE()
    ontology.load("path/to/MOLTENSILE-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#moltensile-matportal] MatPortal. 2021.
   "Matolab Tensile Test Ontology (MOL_TENSILE)."
   Ontology registry entry.
   Available at:
   `https://matportal.org/ontologies/MOL_TENSILE <https://matportal.org/ontologies/MOL_TENSILE>`_
