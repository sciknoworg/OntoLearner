

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Law
       * - **Category**
         - Legal Knowledge
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2019-09
       * - **Creator**
         - Rhizomik
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Copyright Ontology (CopyrightOnto) <https://rhizomik.net/ontologies/copyrightonto/>`_

Copyright Ontology (CopyrightOnto)
========================================================================================================

The Copyright Ontology (CopyrightOnto) is an OWL/RDF ontology for
representing the copyright domain in a machine-processable way in order
to facilitate automated or computer-supported copyright management
through the whole content value chain, rather than focusing only on
end-user permissions [#copyright-repo]_ [#copyright-paper]_. The project
describes the ontology as a Web Ontology implemented using W3C standards
such as RDF and OWL, and organizes the domain into three main parts:
the **Creation Model**, **Rights Model**, and **Actions Model**
[#copyright-repo]_. These models are intended to capture how creations
appear across their lifecycle, which actions can be performed on them,
and which legal rights or constraints regulate those actions
[#copyright-repo]_ [#copyright-jis]_.

The ontology has been presented in the context of semantic digital
rights management and copyright-aware copyright management systems,
including support for interoperable licensing and contract-related
representations [#copyright-paper]_ [#copyright-contracts]_. This makes
it suitable for applications such as automated rights clearance, license
management, provenance-aware content workflows, and machine-readable
reuse analysis in publishing, repositories, and digital content
platforms [#copyright-joir]_ [#copyright-jis]_.

**Example Usage**: Describe a digital artwork as a CopyrightOnto
creation/work entity, associate it with a rightsholder, connect it to
the relevant rights or license statements, and attach temporal or legal
constraints so that downstream systems can perform automated permission
checks and copyright-aware reuse analysis [#copyright-repo]_
[#copyright-joir]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 218
        * - **Total Edges**
          - 470
        * - **Root Nodes**
          - 6
        * - **Leaf Nodes**
          - 75
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 38
        * - **Individuals**
          - 7
        * - **Properties**
          - 12

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 8
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.93
        * - **Depth Variance**
          - 6.62
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 6
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 3.22
        * - **Breadth Variance**
          - 2.40
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 7
        * - **Taxonomic Relations**
          - 118
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 7.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CopyrightOnto

    ontology = CopyrightOnto()
    ontology.load("path/to/CopyrightOnto-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#copyright-repo] Rhizomik. n.d. "CopyrightOnto - Copyright Ontology."
   GitHub repository.
   Available at:
   `https://github.com/rhizomik/copyrightonto <https://github.com/rhizomik/copyrightonto>`_

.. [#copyright-jis] García, R., Celma, Ò., and Gil, R. 2009.
   "Content Value Chains Modelling using a Copyright Ontology."
   Available at:
   `https://rhizomik.net/html/~roberto/papers/rg-jis09.pdf <https://rhizomik.net/html/~roberto/papers/rg-jis09.pdf>`_
