.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.0.2
       * - **Last Updated**
         - None
       * - **Creator**
         - Francesca L. Bleken, Jesper Friis
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Atomistic Ontology (Atomistic) <https://github.com/emmo-repo/domain-atomistic>`_

Atomistic Ontology (Atomistic)
========================================================================================================

The Atomistic Ontology is an EMMO-based domain ontology designed for atomistic and electronic modelling [#atomistic-github]_. It provides a structured vocabulary for representing concepts related to atomistic modelling, electronic modelling, and their connection to the wider EMMO materials ontology ecosystem [#atomistic-github]_. The ontology supports semantic annotation of atomistic and electronic modelling knowledge, enabling interoperability and data integration across materials modelling platforms [#atomistic-github]_.

Atomistic Ontology facilitates the description of computational modelling concepts used in atomistic and electronic simulations, supporting more consistent representation, sharing, and reuse of materials modelling knowledge [#atomistic-github]_. The ontology is described as work-in-progress and under development, rather than as a fully finalized or actively maintained standard [#atomistic-github]_. By providing a standardized semantic framework, Atomistic Ontology supports reproducibility, data sharing, and collaborative research in atomistic and electronic modelling [#atomistic-github]_.

**Example Usage**:
Annotate a computational materials science dataset with Atomistic Ontology terms to specify atomistic modelling concepts, electronic modelling concepts, simulation-related information, and their links to EMMO-based materials modelling vocabularies, enabling semantic search and integration with modelling tools [#atomistic-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 93
        * - **Total Edges**
          - 107
        * - **Root Nodes**
          - 11
        * - **Leaf Nodes**
          - 70
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 12
        * - **Individuals**
          - 0
        * - **Properties**
          - 2

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.80
        * - **Depth Variance**
          - 2.27
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 44
        * - **Minimum Breadth**
          - 3
        * - **Average Breadth**
          - 13.29
        * - **Breadth Variance**
          - 182.78
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Atomistic

    ontology = Atomistic()
    ontology.load("path/to/Atomistic-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#atomistic-github] EMMO-repo. n.d.
   "Domain ontology for atomistic and electronic modelling."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/domain-atomistic <https://github.com/emmo-repo/domain-atomistic>`_
