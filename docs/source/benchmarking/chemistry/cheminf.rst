

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - 2.1.0
       * - **Last Updated**
         - None
       * - **Creator**
         - Egon Willighagen, Nina Jeliazkova, Ola Spjuth, Valery Tkachenko
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Chemical Information Ontology (CHEMINF) <https://terminology.tib.eu/ts/ontologies/CHEMINF>`_

Chemical Information Ontology (CHEMINF)
========================================================================================================

The Chemical Information Ontology (CHEMINF) provides a comprehensive
vocabulary for representing chemical information entities, including
chemical descriptors, properties, algorithms, and computational methods
used in cheminformatics [#cheminf-paper]_ [#cheminf-obo]_. It supports
standardized representation of molecular attributes and calculated or
reported chemical information, enabling unambiguous description of
qualitative and quantitative descriptors derived from chemical
informatics tools and workflows [#cheminf-paper]_ [#cheminf-obo]_.
CHEMINF is designed to improve semantic interoperability across chemistry
databases, computational chemistry platforms, and drug discovery
systems by providing explicit definitions for chemical information
concepts and their provenance [#cheminf-paper]_ [#cheminf-obo]_. It can
be used alongside related chemistry ontologies to link chemical
structures with their calculated properties, descriptors, and generating
methods [#cheminf-paper]_ [#cheminf-obo]_.

**Example Usage**: Represent a computed molecular descriptor as a
CHEMINF information entity linked to a chemical structure, specifying
the descriptor type, the calculation method, and the resulting numeric
value, so that descriptor data can be queried, compared, and integrated
across cheminformatics datasets and software environments
[#cheminf-paper]_ [#cheminf-obo]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1467
        * - **Total Edges**
          - 2837
        * - **Root Nodes**
          - 213
        * - **Leaf Nodes**
          - 435
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 358
        * - **Individuals**
          - 0
        * - **Properties**
          - 52

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 16
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.73
        * - **Depth Variance**
          - 9.21
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 213
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 29.24
        * - **Breadth Variance**
          - 3411.59
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 93
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CHEMINF

    ontology = CHEMINF()
    ontology.load("path/to/CHEMINF-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#cheminf-paper] Hastings, J., Chepelev, L., Willighagen, E.,
   Adams, N., Steinbeck, C., and Dumontier, M. 2011.
   "The Chemical Information Ontology: Provenance and Disambiguation
   for Chemical Data on the Biological Semantic Web."
   *PLoS ONE* 6(10): e25513.
   doi:10.1371/journal.pone.0025513
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC3184996/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC3184996/>`_

.. [#cheminf-obo] OBO Foundry. n.d. "Chemical Information Ontology."
   Available at: `https://obofoundry.org/ontology/cheminf.html <https://obofoundry.org/ontology/cheminf.html>`_
