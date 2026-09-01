

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Biomedical Investigations
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2025-01-09
       * - **Creator**
         - None
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Ontology for Biomedical Investigations (OBI) <https://github.com/obi-ontology/obi/tree/master>`_

Ontology for Biomedical Investigations (OBI)
========================================================================================================

The Ontology for Biomedical Investigations (OBI) is an ontology for representing scientific investigations, experimental designs, and biomedical research processes [#obi-brinkman]_ [#obi-paper]_. It provides a structured vocabulary for describing assays, protocols, devices, materials, objectives, measurements, data, and analysis processes used in biomedical and life-science research [#obi-brinkman]_ [#obi-paper]_.

OBI was developed to provide a common semantic framework for modeling how biomedical experiments are planned and performed, including the relationships between experimental inputs, procedures, instruments, outputs, and generated data [#obi-brinkman]_. It supports standardized semantic annotation of experimental workflows and promotes interoperability, integration, comparison, and reuse of investigation data across biomedical databases and computational systems [#obi-brinkman]_ [#obi-paper]_. By formally representing the processes through which scientific data are generated, OBI supports more consistent description and interpretation of biomedical experiments [#obi-paper]_.

**Example Usage**:
Annotate a biomedical experiment with OBI terms to describe the assay type, experimental objective, input material, device or instrument, protocol steps, generated data, and measurement results. This enables structured representation, semantic search, and integration of experimental information across biomedical resources [#obi-brinkman]_ [#obi-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 40613
        * - **Total Edges**
          - 104537
        * - **Root Nodes**
          - 177
        * - **Leaf Nodes**
          - 10917
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 9703
        * - **Individuals**
          - 301
        * - **Properties**
          - 94

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 28
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.15
        * - **Depth Variance**
          - 23.70
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 386
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 81.62
        * - **Breadth Variance**
          - 11040.03
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 286
        * - **Taxonomic Relations**
          - 11843
        * - **Non-taxonomic Relations**
          - 38
        * - **Average Terms per Type**
          - 5.61
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OBI

    ontology = OBI()
    ontology.load("path/to/OBI-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#obi-brinkman] Brinkman, R. R., Courtot, M., Derom, D.,
   et al. 2010.
   "Modeling Biomedical Experimental Processes with OBI."
   *Journal of Biomedical Semantics*, 1(Suppl 1), S7.
   Available at:
   `https://doi.org/10.1186/2041-1480-1-S1-S7
   <https://doi.org/10.1186/2041-1480-1-S1-S7>`_

.. [#obi-paper] Bandrowski, A., Brinkman, R.,
   Brochhausen, M., et al. 2016.
   "The Ontology for Biomedical Investigations."
   *PLOS ONE*, 11(4), e0154556.
   Available at:
   `https://doi.org/10.1371/journal.pone.0154556
   <https://doi.org/10.1371/journal.pone.0154556>`_
