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
         - `Download Open Innovation Environment Manufacturing (OIEManufacturing) <https://github.com/emmo-repo/OIE-Ontologies/>`_

Open Innovation Environment Manufacturing (OIEManufacturing)
========================================================================================================

The Open Innovation Environment Manufacturing (OIEManufacturing) ontology is a domain-level ontology developed to represent manufacturing processes in materials science [#oiemanufacturing-github]_. It provides a structured vocabulary for describing manufacturing-related concepts and supports their alignment with the wider Open Innovation Environment ontology set [#oiemanufacturing-github]_.

OIEManufacturing is part of the Open Innovation Environment ontology collection, which includes domain-level ontologies for characterisation methods, manufacturing processes, materials, models, and software products [#oiemanufacturing-github]_. The ontology supports semantic annotation, interoperability, data integration, and reuse of manufacturing-related materials science information [#oiemanufacturing-github]_. By providing a standardized semantic framework, OIEManufacturing helps organize manufacturing knowledge for semantic search and integration with materials informatics platforms [#oiemanufacturing-github]_.

**Example Usage**:
Annotate a manufacturing dataset with OIEManufacturing terms to specify manufacturing processes, manufacturing methods, and related materials science information, enabling semantic search and integration with materials informatics platforms [#oiemanufacturing-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 380
        * - **Total Edges**
          - 869
        * - **Root Nodes**
          - 13
        * - **Leaf Nodes**
          - 131
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 222
        * - **Individuals**
          - 0
        * - **Properties**
          - 3

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 5
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.39
        * - **Depth Variance**
          - 1.07
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 30
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 12.00
        * - **Breadth Variance**
          - 112.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 217
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OIEManufacturing

    ontology = OIEManufacturing()
    ontology.load("path/to/OIEManufacturing-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#oiemanufacturing-github] EMMO-repo. n.d.
   "Open Innovation Environment (OIE) domain ontologies."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/OIE-Ontologies <https://github.com/emmo-repo/OIE-Ontologies>`_
