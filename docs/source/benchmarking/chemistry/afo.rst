.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Chemistry
       * - **Category**
         - Laboratory Analytical Processes
       * - **Current Version**
         - 2024-06
       * - **Last Updated**
         - 2024-06-28
       * - **Creator**
         - Allotrope Foundation
       * - **License**
         - CC BY 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Allotrope Foundation Ontology (AFO) <https://terminology.tib.eu/ts/ontologies/AFO>`_

Allotrope Foundation Ontology (AFO)
========================================================================================================

The Allotrope Foundation Ontology (AFO) is a comprehensive ontology
suite designed to standardize the representation of laboratory
analytical processes [#afo-bioportal]_ [#afo-paper]_. It provides a
semantic model and controlled vocabulary for describing key domains such
as equipment, material, process, and results [#afo-bioportal]_
[#afo-paper]_. The ontology is aligned with the Basic Formal Ontology
at its upper layer, supporting interoperable representation of
laboratory data across analytical systems [#afo-bioportal]_
[#afo-paper]_. Within the Allotrope framework, AFO serves as the
semantic layer for consistent description of experimental context,
analytical workflows, and resulting data [#afo-paper]_
[#afo-bioportal]_. By providing explicit definitions and relationships,
AFO supports laboratory data integration, reproducible analysis,
workflow automation, and traceable representation of analytical
processes [#afo-bioportal]_ [#afo-paper]_.

**Example Usage**: Annotate a laboratory experiment with AFO terms to
specify the equipment used, such as a mass spectrometer, the material
analyzed, such as a chemical sample, the analytical process performed,
such as chromatography, and the results obtained, enabling semantic
integration, standardized description, and interoperable analysis across
laboratory data systems [#afo-bioportal]_ [#afo-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 15547
        * - **Total Edges**
          - 36699
        * - **Root Nodes**
          - 142
        * - **Leaf Nodes**
          - 8003
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 3871
        * - **Individuals**
          - 38
        * - **Properties**
          - 318

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 24
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 5.14
        * - **Depth Variance**
          - 22.60
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 368
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 75.84
        * - **Breadth Variance**
          - 8251.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 37
        * - **Taxonomic Relations**
          - 6904
        * - **Non-taxonomic Relations**
          - 34
        * - **Average Terms per Type**
          - 3.36
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import AFO

    ontology = AFO()
    ontology.load("path/to/AFO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#afo-paper] Millecam, T., Jaeger, M., Oberkampf, H., and
   Hennebert, P. 2021. "Coming of Age of Allotrope: Proceedings from
   the Fall 2020 Allotrope Connect."
   *Drug Discovery Today* 26(11): 2675-2681.
   Available at:
   `https://www.sciencedirect.com/science/article/pii/S1359644621001653 <https://www.sciencedirect.com/science/article/pii/S1359644621001653>`_

.. [#afo-bioportal] NCBO BioPortal. n.d. "Allotrope Foundation Ontologies (AFO)."
   Available at:
   `https://bioportal.bioontology.org/ontologies/AFO <https://bioportal.bioontology.org/ontologies/AFO>`_
