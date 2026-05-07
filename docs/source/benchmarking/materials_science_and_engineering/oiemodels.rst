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
         - `Download Open Innovation Environment Models (OIEModels) <https://github.com/emmo-repo/OIE-Ontologies/>`_

Open Innovation Environment Models (OIEModels)
========================================================================================================

The Open Innovation Environment Models (OIEModels) ontology is a domain-level ontology developed to represent model-related concepts in materials science [#oiemodels-github]_. It provides a structured vocabulary for describing models and supports their alignment with the wider Open Innovation Environment ontology set [#oiemodels-github]_.

OIEModels is part of the Open Innovation Environment ontology collection, which includes EMMO-compliant, domain-level ontologies for characterisation methods, manufacturing processes, materials, models, and software products [#oiemodels-github]_. The ontology supports semantic annotation, interoperability, data integration, and reuse of model-related information across materials modelling and materials informatics workflows [#oiemodels-github]_.

**Example Usage**:
Annotate a materials modelling dataset with OIEModels terms to specify model types, model-related information, and links to materials science concepts, enabling semantic search and integration with materials informatics platforms [#oiemodels-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 186
        * - **Total Edges**
          - 413
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 64
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 108
        * - **Individuals**
          - 0
        * - **Properties**
          - 1

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 0
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.00
        * - **Depth Variance**
          - 0.00
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 0
        * - **Minimum Breadth**
          - 0
        * - **Average Breadth**
          - 0.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 101
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OIEModels

    ontology = OIEModels()
    ontology.load("path/to/OIEModels-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#oiemodels-github] EMMO-repo. n.d.
   "Open Innovation Environment (OIE) domain ontologies."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/OIE-Ontologies <https://github.com/emmo-repo/OIE-Ontologies>`_
