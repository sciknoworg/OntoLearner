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
         - Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Open Innovation Environment Materials (OIEMaterials) <https://github.com/emmo-repo/OIE-Ontologies/>`_

Open Innovation Environment Materials (OIEMaterials)
========================================================================================================

The Open Innovation Environment Materials (OIEMaterials) ontology is a domain-level ontology developed to represent materials-related concepts in materials science [#oiematerials-github]_. It provides a structured vocabulary for describing materials and supports their alignment with the wider Open Innovation Environment ontology set [#oiematerials-github]_.

OIEMaterials is part of the Open Innovation Environment ontology collection, which includes EMMO-compliant, domain-level ontologies for characterisation methods, manufacturing processes, materials, models, and software products [#oiematerials-github]_. The ontology supports semantic annotation, interoperability, data integration, and reuse of materials-related information across materials science and informatics workflows [#oiematerials-github]_.

**Example Usage**:
Annotate a materials dataset with OIEMaterials terms to specify materials and related materials science information, enabling semantic search and integration with materials informatics platforms [#oiematerials-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 278
        * - **Total Edges**
          - 561
        * - **Root Nodes**
          - 13
        * - **Leaf Nodes**
          - 115
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 119
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
          - 4
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.64
        * - **Depth Variance**
          - 1.87
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 14
        * - **Minimum Breadth**
          - 6
        * - **Average Breadth**
          - 10.00
        * - **Breadth Variance**
          - 10.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 156
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OIEMaterials

    ontology = OIEMaterials()
    ontology.load("path/to/OIEMaterials-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#oiematerials-github] EMMO-repo. n.d.
   "Open Innovation Environment (OIE) domain ontologies."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/OIE-Ontologies <https://github.com/emmo-repo/OIE-Ontologies>`_
