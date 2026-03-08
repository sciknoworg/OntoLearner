.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Linguistics
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 19-04-2016
       * - **Creator**
         - Aldo Gangemi
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Framester Ontology (Framester) <http://150.146.207.114/lode/extract?url=http://ontologydesignpatterns.org/ont/framester/framester.owl>`_

Framester Ontology (Framester)
========================================================================================================

Framester is a frame-based ontological resource acting as a hub between linguistic resources such as FrameNet, WordNet, VerbNet, BabelNet, DBpedia, Yago, DOLCE-Zero, and leveraging this wealth of links to create an interoperable predicate space formalized according to frame semantics and semiotics. Framester uses WordNet and FrameNet at its core, expands it to other resources transitively, and represents them in a formal version of frame semantics. It provides a structured vocabulary for representing linguistic resources, supporting both theoretical and experimental research in linguistics.

The ontology employs a class-based modeling approach, defining classes for different types of linguistic resources, frames, and relationships, along with properties to describe their characteristics and interactions. Hierarchies are used to organize classes into categories, enabling efficient data retrieval and analysis. Framester supports the integration of data from various sources, promoting interoperability and data-driven research in linguistics.

Typical applications of Framester include the development of new linguistic resource integration methods, the optimization of linguistic data management practices, and the integration of diverse datasets to support advanced analytics and knowledge discovery. By providing a standardized vocabulary and framework, Framester enhances collaboration and innovation in the field of linguistics.

**Example Usage**:
Annotate a linguistic dataset with Framester terms to specify linguistic resources, frames, and relationships, enabling semantic search and integration with linguistic information management platforms.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 174
        * - **Total Edges**
          - 398
        * - **Root Nodes**
          - 85
        * - **Leaf Nodes**
          - 38
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 59
        * - **Individuals**
          - 0
        * - **Properties**
          - 77

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.69
        * - **Depth Variance**
          - 0.65
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 85
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 42.25
        * - **Breadth Variance**
          - 937.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 135
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Framester

    ontology = Framester()
    ontology.load("path/to/Framester-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
