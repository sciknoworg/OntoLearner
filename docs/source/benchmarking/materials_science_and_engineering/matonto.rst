.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Scholarly Knowledge
       * - **Current Version**
         - None
       * - **Last Updated**
         - None
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - owl
       * - **Download**
         - `Download Material Ontology (MatOnto) <https://github.com/EngyNasr/MSE-Benchmark/blob/main/testCases/secondTestCase/MatOnto.owl>`_

Material Ontology (MatOnto)
========================================================================================================

The Material Ontology (MatOnto) is a domain ontology for representing materials science knowledge, including materials, material categories, properties, units, symbols, crystal-related concepts, and thermodynamic or thermomechanical properties [#matonto-matportal]_ [#matonto-github]_. It provides a structured vocabulary for describing material types such as metals, ceramics, composites, polymers, plastics, glasses, nanomaterials, and related material qualities [#matonto-github]_.

MatOnto supports semantic annotation of materials data, enabling interoperability, data integration, retrieval, and reuse across materials science databases and informatics workflows [#matonto-matportal]_. The ontology includes concepts for measured properties such as band gap, heat capacity, specific heat, bulk modulus, shear modulus, Gibbs free energy, and other material-related quantities [#matonto-github]_. By providing a standardized vocabulary, MatOnto facilitates semantic search, materials information sharing, and knowledge integration in materials science and engineering [#matonto-matportal]_ [#matonto-github]_.

**Example Usage**:
Annotate a materials database with MatOnto terms to specify material types such as metal, ceramic, polymer, or nanomaterial, together with properties such as band gap, heat capacity, bulk modulus, shear modulus, crystal system, and space group information, enabling semantic search and integration with materials informatics platforms [#matonto-matportal]_ [#matonto-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4753
        * - **Total Edges**
          - 11287
        * - **Root Nodes**
          - 33
        * - **Leaf Nodes**
          - 1063
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1307
        * - **Individuals**
          - 122
        * - **Properties**
          - 95

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 129
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 38.24
        * - **Depth Variance**
          - 1437.88
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 155
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 18.92
        * - **Breadth Variance**
          - 522.53
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 122
        * - **Taxonomic Relations**
          - 1215
        * - **Non-taxonomic Relations**
          - 167
        * - **Average Terms per Type**
          - 1.94
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MatOnto

    ontology = MatOnto()
    ontology.load("path/to/MatOnto-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#matonto-matportal] Materials Open Laboratory. 2021.
   "MatOnto Ontology."
   MatPortal ontology entry.
   Available at:
   `https://matportal.org/ontologies/MATONTO <https://matportal.org/ontologies/MATONTO>`_

.. [#matonto-github] iNovexIrad. n.d.
   "MatOnto-Ontologies."
   GitHub repository.
   Available at:
   `https://github.com/inovexcorp/MatOnto-Ontologies <https://github.com/inovexcorp/MatOnto-Ontologies>`_
