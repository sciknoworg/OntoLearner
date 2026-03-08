.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Microscopy
       * - **Current Version**
         - 2.0
       * - **Last Updated**
         - None
       * - **Creator**
         - https://orcid.org/0000-0002-3717-7104,https://orcid.org/0000-0002-7094-5371
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Microscopy Ontology (MO) <https://github.com/materialdigital/microscopy-ontology?tab=readme-ov-file>`_

Microscopy Ontology (MO)
========================================================================================================

The Microscopy Ontology (MO) is a domain ontology designed to provide a structured framework for describing microscopy and microanalysis experiments, data, and equipment. MO extends the PMDco ontological framework and enables semantic integration and interoperability of diverse data sources in microscopy research. The ontology covers key concepts such as imaging modalities, sample preparation methods, instrument components, acquisition parameters, and data analysis techniques. MO supports the annotation of experimental workflows, facilitating data sharing, reproducibility, and advanced analysis across various microscopy studies. By providing a standardized vocabulary, MO enables the development of adaptable data applications and cross-experiment comparisons in materials science, biology, and medical research. The ontology is actively maintained and extended to incorporate new microscopy techniques and research requirements.

**Example Usage**:
Annotate a microscopy dataset with MO terms to specify the imaging modality (e.g., "scanning electron microscopy"), sample preparation method, instrument configuration, and analysis workflow, enabling semantic search and integration with other microscopy data sources.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 931
        * - **Total Edges**
          - 1776
        * - **Root Nodes**
          - 10
        * - **Leaf Nodes**
          - 693
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 217
        * - **Individuals**
          - 0
        * - **Properties**
          - 3

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
          - 0.09
        * - **Depth Variance**
          - 0.08
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 10
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 5.50
        * - **Breadth Variance**
          - 20.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 130
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MO

    ontology = MO()
    ontology.load("path/to/MO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
