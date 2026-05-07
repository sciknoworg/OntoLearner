.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemicals, Roles
       * - **Current Version**
         - 2015-11-23
       * - **Last Updated**
         - 2015-11-23
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download CHEBI Integrated Role Ontology (CHIRO) <https://terminology.tib.eu/ts/ontologies/chiro>`_

CHEBI Integrated Role Ontology (CHIRO)
========================================================================================================

The CHEBI Integrated Role Ontology (CHIRO) is a specialized ontology
designed to provide a structured role hierarchy for chemicals
[#chiro-obo]_ [#chiro-paper]_. It extends the role branch associated
with ChEBI by connecting chemicals in the structural hierarchy through
a `has role` relation and by linking chemical roles to relevant classes
in other ontologies [#chiro-obo]_ [#chiro-paper]_. This enables formal
representation of relationships between chemical structures, such as
small molecules and drugs, and the biological or chemical roles they
play [#chiro-obo]_ [#chiro-paper]_. By providing a standardized
framework for describing chemical roles, CHIRO supports semantic
interoperability, ontology-based integration, and advanced querying
across chemical and biomedical datasets [#chiro-paper]_ [#chiro-obo]_.

**Example Usage**: Annotate a dataset of small molecules with CHIRO
terms to specify roles such as enzyme inhibitor or neurotransmitter,
and link those roles to related biological processes or target classes,
enabling semantic search, cross-dataset integration, and role-based
analysis of chemical entities [#chiro-obo]_ [#chiro-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 81778
        * - **Total Edges**
          - 197071
        * - **Root Nodes**
          - 14636
        * - **Leaf Nodes**
          - 50439
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 13930
        * - **Individuals**
          - 0
        * - **Properties**
          - 15

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
          - 1.36
        * - **Depth Variance**
          - 1.13
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 34719
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 4620.24
        * - **Breadth Variance**
          - 105924794.30
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 25262
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CHIRO

    ontology = CHIRO()
    ontology.load("path/to/CHIRO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#chiro-obo] OBO Foundry. n.d. "CHEBI Integrated Role Ontology."
   Available at: `https://obofoundry.org/ontology/chiro.html <https://obofoundry.org/ontology/chiro.html>`_

.. [#chiro-paper] Hoyt, C. T., Mungall, C., Vasilevsky, N.,
   Domingo-Fernández, D., Healy, M., and Colluru, V. 2020.
   "Extension of Roles in the ChEBI Ontology."
   ChemRxiv.
   doi:10.26434/chemrxiv.12591221
   Available at: `https://chemrxiv.org/doi/10.26434/chemrxiv.12591221 <https://chemrxiv.org/doi/10.26434/chemrxiv.12591221>`_
