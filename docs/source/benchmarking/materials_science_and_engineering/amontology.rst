.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Manufacturing
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2023-05-10
       * - **Creator**
         - Iassou Souroko, Ali Riza Durmaz
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Additive Manufacturing Ontology (AMOntology) <https://github.com/iassouroko/AMontology>`_

Additive Manufacturing Ontology (AMOntology)
========================================================================================================
The **Additive Manufacturing Ontology (AMOntology)** is a domain ontology developed to represent knowledge about additive manufacturing (AM) processes, computational models, and their characteristics [#amontology-github]_. It is structured around two main components: **AMProcessOntology**, which captures entities and relationships relevant to AM processes, and **ModelOntology**, which describes modeling concepts for potentially multi-physics and multi-scale processes [#amontology-github]_. AMOntology integrates these components to provide a framework for describing AM process knowledge, model characteristics, assumptions, approximations, and qualitative indicators of model fidelity [#amontology-github]_. It supports semantic annotation and knowledge integration across additive manufacturing workflows, helping improve interoperability, reuse, and sharing of AM information across research and digital manufacturing environments [#ali2019]_ [#amontology-github]_.

**Example Usage**:
Annotate an additive manufacturing workflow with AMOntology terms to specify process parameters, material properties, equipment information, and computational model characteristics, enabling semantic search, data integration, and comparison of AM knowledge across digital manufacturing platforms [#ali2019]_ [#amontology-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 900
        * - **Total Edges**
          - 2299
        * - **Root Nodes**
          - 71
        * - **Leaf Nodes**
          - 99
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 328
        * - **Individuals**
          - 56
        * - **Properties**
          - 21

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 15
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.66
        * - **Depth Variance**
          - 11.25
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 116
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 55.50
        * - **Breadth Variance**
          - 1339.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 59
        * - **Taxonomic Relations**
          - 657
        * - **Non-taxonomic Relations**
          - 5
        * - **Average Terms per Type**
          - 1.26
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AMOntology

    ontology = AMOntology()
    ontology.load("path/to/AMOntology-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#ali2019] Mohd Ali, M., Rai, R., Otte, J. N., and Smith, B. 2019.
   "A product life cycle ontology for additive manufacturing."
   *Computers in Industry*, 105, 191--203.
   DOI: 10.1016/j.compind.2018.12.007.
   Available at:
   `https://www.sciencedirect.com/science/article/pii/S0166361518301647 <https://www.sciencedirect.com/science/article/pii/S0166361518301647>`_

.. [#amontology-github] Assouroko, I., Witherell, P., Lopez, F., and contributors. n.d.
   "AMontology: NIST's OWL ontology of additive manufacturing."
   GitHub repository.
   Available at:
   `https://github.com/iassouroko/AMontology <https://github.com/iassouroko/AMontology>`_
