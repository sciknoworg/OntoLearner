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

The Open Innovation Environment Characterisation (OIECharacterisation) ontology is an EMMO-compliant, domain-level ontology developed to represent characterisation methods in materials science [#oiecharacterisation-github]_. It provides a structured vocabulary for describing characterisation-method concepts and supports their alignment with the wider EMMO ontology ecosystem [#oiecharacterisation-github]_.

OIECharacterisation is part of the Open Innovation Environment (OIE) ontology set, which covers characterisation methods, manufacturing processes, materials, models, and software products [#oiecharacterisation-github]_. The OIE ontologies are aligned with EMMO and were developed in the context of the OYSTER project [#oiecharacterisation-github]_. By providing a standardized semantic framework, OIECharacterisation supports semantic annotation, interoperability, data integration, and reuse of characterisation-related materials science information [#oiecharacterisation-github]_.

**Example Usage**:
Annotate a materials characterisation dataset with OIECharacterisation terms to specify characterisation methods, related measurement information, and links to EMMO-aligned materials science concepts, enabling semantic search and integration with materials informatics platforms [#oiecharacterisation-github]_.

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

References
----------

.. [#oiecharacterisation-github] EMMO-repo. n.d.
   "Open Innovation Environment (OIE) domain ontologies."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/OIE-Ontologies <https://github.com/emmo-repo/OIE-Ontologies>`_
