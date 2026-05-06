.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials
       * - **Current Version**
         - 0.1
       * - **Last Updated**
         - None
       * - **Creator**
         - Adham Hashibon, Daniele Toti, Emanuele Ghedini, Georg J. Schmitz, Gerhard Goldbeck, Jesper Friis, Pierluigi Del Nostro
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Open Innovation Environment Software (OIESoftware) <https://github.com/emmo-repo/OIE-Ontologies/>`_

Open Innovation Environment Software (OIESoftware)
========================================================================================================

The Open Innovation Environment Software Ontology (OIESoftware) is an EMMO-compliant, domain-level ontology developed to represent software products in materials science and engineering [#oiesoftware-github]_. It provides a structured vocabulary for describing software-related concepts and supports their alignment with the wider Open Innovation Environment ontology set [#oiesoftware-github]_.

OIESoftware is part of the Open Innovation Environment ontology collection, which includes domain-level ontologies for characterisation methods, manufacturing processes, materials, models, and software products [#oiesoftware-github]_. The ontology supports semantic annotation, interoperability, data integration, and reuse of software-related information across materials science workflows and digital research infrastructures [#oiesoftware-github]_.

**Example Usage**:
Annotate a computational materials science workflow with OIESoftware terms to specify the software products used, their roles in the workflow, and their links to related models, materials, or characterisation/manufacturing processes, enabling semantic search and integration with research data management systems [#oiesoftware-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 205
        * - **Total Edges**
          - 489
        * - **Root Nodes**
          - 17
        * - **Leaf Nodes**
          - 49
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 155
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
          - 3
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.01
        * - **Depth Variance**
          - 0.59
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 37
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 17.25
        * - **Breadth Variance**
          - 155.19
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 179
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OIESoftware

    ontology = OIESoftware()
    ontology.load("path/to/OIESoftware-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#oiesoftware-github] EMMO-repo. n.d.
   "Open Innovation Environment (OIE) domain ontologies."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/OIE-Ontologies <https://github.com/emmo-repo/OIE-Ontologies>`_
