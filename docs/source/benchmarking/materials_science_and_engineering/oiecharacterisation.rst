.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - Daniele Toti, Gerhard Goldbeck, Pierluigi Del Nostro
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Open Innovation Environment Characterisation (OIECharacterisation) <https://github.com/emmo-repo/OIE-Ontologies/>`_

Open Innovation Environment Characterisation (OIECharacterisation)
========================================================================================================

The Open Innovation Environment Characterisation (OIECharacterisation) ontology is an EMMO-compliant, domain-level ontology developed to represent characterization methods in materials science. It provides a structured vocabulary for describing characterization techniques, equipment, and data, supporting both experimental and computational research in materials science.

The ontology employs a class-based modeling approach, defining classes for different types of characterization methods, equipment, and data, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. OIECharacterisation supports the integration of data from various sources, promoting interoperability and data-driven research in materials characterization.

Typical applications of OIECharacterisation include the development of new characterization methods, the optimization of characterization procedures, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, OIECharacterisation enhances collaboration and innovation in the field of materials characterization.

**Example Usage**:
Annotate a characterization dataset with OIECharacterisation terms to specify characterization methods, equipment, and data, enabling semantic search and integration with materials informatics platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 54
        * - **Total Edges**
          - 135
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 11
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 42
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
          - 0.88
        * - **Depth Variance**
          - 0.11
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 7
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 4.00
        * - **Breadth Variance**
          - 9.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 41
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OIECharacterisation

    ontology = OIECharacterisation()
    ontology.load("path/to/OIECharacterisation-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
