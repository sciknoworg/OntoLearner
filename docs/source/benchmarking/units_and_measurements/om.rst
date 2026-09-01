.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Units and Measurements
       * - **Category**
         - Units and Measurements
       * - **Current Version**
         - 2.0.57
       * - **Last Updated**
         - June 28, 2024
       * - **Creator**
         - Hajo Rijgersberg, Don Willems, Jan Top
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - rdf
       * - **Download**
         - `Download Ontology of Units of Measure (OM) <https://bioportal.bioontology.org/ontologies/OM>`_

Ontology of Units of Measure (OM)
========================================================================================================

The Ontology of units of Measure (OM) models concepts and relations important to scientific research, with a strong focus on units, quantities, measurements, measures, and dimensions [#om-github]_ [#om-paper]_. It includes common units such as the SI units ``metre`` and ``kilogram``, as well as units from other systems of units, including examples such as ``mile`` and ``nautical mile`` [#om-github]_. OM also includes more specialized units and quantities for many scientific and technical application areas, supporting fields such as geometry, mechanics, thermodynamics, electromagnetism, fluid mechanics, chemical physics, astronomy, Earth science, meteorology, material science, microbiology, economics, information technology, and typography [#om-github]_. The ontology provides classes, instances, and properties for defining and using measures and units, enabling quantitative research data to be represented more explicitly, integrated across sources, verified, and reproduced [#om-paper]_. OM supports interoperability by providing a standardized semantic framework for describing quantities, units, dimensions, scales, prefixes, systems of units, and measurement values [#om-github]_ [#om-paper]_.

The ontology employs a class-based modeling approach, defining classes for different types of units, quantities, and measurements, along with properties to describe their characteristics and relationships [#om-paper]_. Hierarchies are used to organize units, quantities, dimensions, and systems of units into structured categories, enabling efficient retrieval, comparison, conversion, and analysis [#om-github]_. OM supports the integration of quantitative data from diverse sources, promoting interoperability and data-driven research in units and measurements [#om-paper]_.

Typical applications of OM include semantic annotation of scientific datasets, explicit representation of measurement values, support for unit conversion, development of measurement-related tools and services, and integration of heterogeneous datasets for analytics and knowledge discovery [#om-github]_ [#om-paper]_. By providing a standardized vocabulary and framework, OM enhances collaboration, reproducibility, and innovation in domains that depend on precise units and measurements [#om-paper]_.

**Example Usage**:
Annotate a scientific dataset with OM terms to specify quantities, units, dimensions, and measurement values, enabling semantic search, unit conversion, data integration, and interoperability with measurement management platforms [#om-github]_ [#om-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 9352
        * - **Total Edges**
          - 27500
        * - **Root Nodes**
          - 27
        * - **Leaf Nodes**
          - 4836
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1100
        * - **Individuals**
          - 1688
        * - **Properties**
          - 34

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
          - 0.27
        * - **Depth Variance**
          - 0.20
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 27
        * - **Minimum Breadth**
          - 10
        * - **Average Breadth**
          - 18.50
        * - **Breadth Variance**
          - 72.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 1953
        * - **Taxonomic Relations**
          - 1124
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 42.46
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OM

    ontology = OM()
    ontology.load("path/to/OM-ontology.rdf")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#om-github] Rijgersberg, Hajo. n.d.
   "Ontology of units of Measure (OM)."
   GitHub Repository.
   Available at:
   `https://github.com/HajoRijgersberg/OM <https://github.com/HajoRijgersberg/OM>`_

.. [#om-paper] Rijgersberg, Hajo, Mark van Assem, and Jan L. Top. 2013.
   "Ontology of Units of Measure and Related Concepts."
   *Semantic Web* 4(1): 3--13.
   DOI:
   `10.3233/SW-2012-0069 <https://doi.org/10.3233/SW-2012-0069>`_
