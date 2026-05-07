

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

The Ontology for Biomedical Investigations (OBI) is an ontology for describing scientific investigations, experimental designs, and biomedical research methodology [#obi-obofoundry]_ [#obi-paper]_. It provides a structured vocabulary for representing assays, devices, protocols, objectives, materials, measurements, data, and analysis processes used in biomedical and life sciences research [#obi-paper]_.

OBI supports standardized semantic annotation of experimental workflows, enabling interoperability, data integration, comparison, and reuse of biomedical investigation data across databases and computational systems [#obi-obofoundry]_ [#obi-paper]_. By providing a common framework for describing how scientific data are generated, OBI helps make research methods more transparent and reproducible [#obi-paper]_.

**Example Usage**:
Annotate a microarray experiment with OBI terms to specify the assay type, microarray device, RNA extraction step, protocol, input material, generated data, and measurement results, enabling semantic search and integration with biomedical databases [#obi-obofoundry]_ [#obi-paper]_.

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

.. [#obi-obofoundry] OBO Foundry. n.d.
   "OBI: Ontology for Biomedical Investigations."
   Ontology registry entry.
   Available at:
   `https://obofoundry.org/ontology/obi.html <https://obofoundry.org/ontology/obi.html>`_

.. [#obi-paper] Bandrowski, A., Brinkman, R., Brochhausen, M., et al. 2016.
   "The Ontology for Biomedical Investigations."
   *PLOS ONE*, 11(4), e0154556.
   DOI: 10.1371/journal.pone.0154556.
   Available at:
   `https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0154556 <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0154556>`_
