.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Upper Ontology
       * - **Category**
         - Basic
       * - **Current Version**
         - 2.0
       * - **Last Updated**
         - 2020
       * - **Creator**
         - University at Buffalo
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Basic Formal Ontology (BFO) <https://github.com/BFO-ontology/BFO-2020/>`_

Basic Formal Ontology (BFO)
========================================================================================================

The Basic Formal Ontology (BFO) is a small, domain-neutral upper ontology designed to provide a common framework for organizing entities represented in scientific and technical domain ontologies [#bfo-bioinformatics]_ [#bfo-material]_. BFO distinguishes fundamentally between continuants, which persist through time while maintaining their identity, and occurrents, which unfold or occur through time, such as processes and events [#bfo-bioinformatics]_. Within the continuant branch, BFO further provides categories for material entities, including objects, object aggregates, and fiat object parts, supporting consistent classification of physical entities across different application domains [#bfo-material]_. By supplying a shared upper-level structure, BFO supports the development and integration of domain ontologies and promotes consistent representation of scientific knowledge [#bfo-bioinformatics]_ [#bfo-material]_.

**Example Usage**:
Use BFO as the upper ontology for a biomedical ontology by classifying a ``cell`` as a material entity and continuant, while representing ``cell division`` as a process and therefore an occurrent. Such upper-level distinctions provide a common ontological structure for integrating concepts defined in different biomedical domain ontologies [#bfo-bioinformatics]_ [#bfo-material]_.
Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 538
        * - **Total Edges**
          - 1002
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 276
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 84
        * - **Individuals**
          - 0
        * - **Properties**
          - 40

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 13
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.21
        * - **Depth Variance**
          - 6.56
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 54
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 19.79
        * - **Breadth Variance**
          - 293.74
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 66
        * - **Non-taxonomic Relations**
          - 5
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BFO

    ontology = BFO()
    ontology.load("path/to/BFO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bfo-bioinformatics] Smith, B., Kumar, A., and Bittner, T. 2005.
   "Basic Formal Ontology for Bioinformatics."
   IFOMIS Reports.
   Available at:
   `http://ontology.buffalo.edu/smith/articles/BFO_for_bioinformatics.pdf
   <http://ontology.buffalo.edu/smith/articles/BFO_for_bioinformatics.pdf>`_

.. [#bfo-material] Smith, B. 2012.
   "On Classifying Material Entities in Basic Formal Ontology."
   In *Interdisciplinary Ontology: Proceedings of the Third
   Interdisciplinary Ontology Meeting*, 1--13.
   Tokyo: Keio University Press.
   Available at:
   `https://philpapers.org/archive/SMIOCM.pdf
   <https://philpapers.org/archive/SMIOCM.pdf>`_
