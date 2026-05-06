.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 21.03.202
       * - **Creator**
         - Ahmad Zainul Ihsan
       * - **License**
         - Creative Commons Attribution 3.0 International (CC BY 3.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Dislocation Ontology (DISO) <https://github.com/Materials-Data-Science-and-Informatics/dislocation-ontology>`_

Dislocation Ontology (DISO)
========================================================================================================

The Dislocation Ontology (DISO) is a domain ontology that defines concepts and relationships related to linear defects in crystalline materials, especially dislocations [#diso-doc]_ [#ihsan2023]_. It provides a structured vocabulary for describing dislocation-related concepts, including dislocation structures, dislocation lines, Burgers vectors, crystal structures, and relationships between dislocation-domain entities [#ihsan2023]_.

DISO was developed using a top-down approach, starting from general concepts in the dislocation domain and then specializing them into more specific concepts [#diso-doc]_ [#ihsan2023]_. Version 1.1 adapts and extends DISO for the discrete dislocation dynamics domain by adding missing concepts, improving class definitions, exploring additional relationships, and aligning it with related ontologies such as EMMO and the Materials Design Ontology (MDO) [#diso-doc]_. By providing a standardized semantic representation, DISO supports annotation, interoperability, data integration, and reuse of dislocation-related experimental and simulation data [#ihsan2023]_.

**Example Usage**:
Annotate a transmission electron microscopy (TEM) dataset or dislocation dynamics simulation with DISO terms to specify dislocation structures, Burgers vectors, line directions, crystal-structure context, and relationships between dislocation-domain entities, enabling semantic search and integration with materials science databases and simulation workflows [#diso-doc]_ [#ihsan2023]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 324
        * - **Total Edges**
          - 739
        * - **Root Nodes**
          - 9
        * - **Leaf Nodes**
          - 91
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 62
        * - **Individuals**
          - 0
        * - **Properties**
          - 45

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
          - 0.18
        * - **Depth Variance**
          - 0.15
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 9
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.50
        * - **Breadth Variance**
          - 12.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 38
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DISO

    ontology = DISO()
    ontology.load("path/to/DISO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#diso-doc] Materials Data Science and Informatics. n.d.
   "Dislocation Ontology (DISO)."
   *Dislocation Ontology Suite*.
   Available at:
   `https://materials-data-science-and-informatics.github.io/Dislocation-Ontology-Suite/DISO/ <https://materials-data-science-and-informatics.github.io/Dislocation-Ontology-Suite/DISO/>`_

.. [#ihsan2023] Ihsan, A. Z., Fathalla, S., and Sandfeld, S. 2023.
   "DISO: A Domain Ontology for Modeling Dislocations in Crystalline Materials."
   In *The 38th ACM/SIGAPP Symposium on Applied Computing (SAC '23)*, Article 4, 8 pages.
   DOI: 10.1145/3555776.3578739.
   Available at:
   `https://arxiv.org/html/2401.02540v1 <https://arxiv.org/html/2401.02540v1>`_
