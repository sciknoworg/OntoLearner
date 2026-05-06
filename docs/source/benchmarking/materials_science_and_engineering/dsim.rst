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
         - 17.08.2023
       * - **Creator**
         - Ahmad Zainul Ihsan
       * - **License**
         - Creative Commons Attribution 3.0 Unported (CC BY 3.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Dislocation Simulation and Model Ontology (DSIM) <https://github.com/OCDO/DSIM>`_

Dislocation Simulation and Model Ontology (DSIM)
========================================================================================================

The Dislocation Simulation and Model Ontology (DSIM) is a domain ontology developed to model concepts and relationships in the field of discrete dislocation dynamics and microscopy techniques used in dislocation research [#dsim-github]_. DSIM provides a structured vocabulary for representing numerical descriptions of dislocations in simulations, as well as pictorial concepts such as pixels used in experimental images, including TEM, SEM, and FIM images [#dsim-github]_.

The ontology supports semantic annotation of dislocation simulation data, microscopy image data, and related modelling information, enabling data integration, semantic search, and reuse in materials science research [#dsim-github]_. By providing a standardized representation of simulation and image-based dislocation concepts, DSIM facilitates knowledge sharing and comparison across dislocation research workflows [#dsim-github]_.

**Example Usage**:
Annotate a dislocation dynamics simulation or microscopy dataset with DSIM terms to specify numerical dislocation representations, simulation-related concepts, microscopy image pixels, and image-based dislocation information, enabling semantic search and integration with dislocation research databases [#dsim-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 313
        * - **Total Edges**
          - 673
        * - **Root Nodes**
          - 19
        * - **Leaf Nodes**
          - 119
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 47
        * - **Individuals**
          - 0
        * - **Properties**
          - 78

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.05
        * - **Depth Variance**
          - 3.85
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 19
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 7.62
        * - **Breadth Variance**
          - 29.98
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
          - 6
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DSIM

    ontology = DSIM()
    ontology.load("path/to/DSIM-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#dsim-github] OCDO. n.d.
   "Dislocation Simulation and Model Ontology."
   GitHub repository.
   Available at:
   `https://github.com/OCDO/DSIM <https://github.com/OCDO/DSIM>`_
