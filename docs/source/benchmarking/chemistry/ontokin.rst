

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Chemistry
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 08 February 2022
       * - **Creator**
         - IEEE
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Chemical Kinetics Ontology (OntoKin) <https://www.ontologyportal.org/>`_

Chemical Kinetics Ontology (OntoKin)
========================================================================================================

The Chemical Kinetics Ontology (OntoKin) is an ontology developed for
the formal and standardized representation of chemical kinetic reaction
mechanisms [#ontokin-paper]_ [#ontokin-context]_. It provides structured
definitions for reaction mechanisms, including chemical species,
reaction pathways, elementary reactions, phases, and kinetic rate
coefficients needed to model chemical processes [#ontokin-paper]_
[#ontokin-context]_. OntoKin captures important kinetics concepts such
as reaction types, activation energies, temperature dependence, and
other parameters used in combustion chemistry and related modeling
domains [#ontokin-paper]_. As a semantic framework for reaction
mechanism knowledge, it supports integration, querying, comparison, and
reuse of kinetic mechanisms across chemistry databases and computational
chemistry systems [#ontokin-paper]_ [#ontokin-context]_.

**Example Usage**: Represent a combustion reaction mechanism with
OntoKin terms for chemical species such as CH4, O2, and H2O, together
with elementary reaction steps, activation energies, and
temperature-dependent rate coefficients, enabling semantic comparison
and reuse of kinetic models across chemical and combustion datasets
[#ontokin-paper]_ [#ontokin-context]_.
Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 407
        * - **Total Edges**
          - 1011
        * - **Root Nodes**
          - 122
        * - **Leaf Nodes**
          - 103
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 83
        * - **Individuals**
          - 0
        * - **Properties**
          - 136

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
          - 1.64
        * - **Depth Variance**
          - 2.39
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 122
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 45.22
        * - **Breadth Variance**
          - 1858.40
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 51
        * - **Non-taxonomic Relations**
          - 1
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OntoKin

    ontology = OntoKin()
    ontology.load("path/to/OntoKin-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#ontokin-paper] Farazi, F., Akroyd, J., Mosbach, S., and Kraft, M. 2020.
   "An Ontology for Chemical Kinetic Reaction Mechanisms."
   *Journal of Chemical Information and Modeling* 60(1): 108-120.
   doi:10.1021/acs.jcim.9b00960

.. [#ontokin-context] NFDI4Chem Knowledge Base. n.d. "Ontology."
   Available at:
   `https://nfdi4chem.chemie.uni-mainz.de/knowledge_base/docs/topics/ontology/ <https://nfdi4chem.chemie.uni-mainz.de/knowledge_base/docs/topics/ontology/>`_
