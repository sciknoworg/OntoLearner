.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.2
       * - **Last Updated**
         - None
       * - **Creator**
         - REACT project team
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - owl
       * - **Download**
         - `Download The Heat Pump Ontology (HPOnt) <https://react2020.github.io/REACT-ONTOLOGY/HPOnt/index-en.html/>`_

The Heat Pump Ontology (HPOnt)
========================================================================================================

The Heat Pump Ontology (HPOnt) is a domain ontology developed to formalize and represent information about heat pump systems [#hpont-doc]_. HPOnt provides a structured vocabulary for describing heat pump-related concepts such as operating mode, cooling capacity, power supply, storage volume, power consumption, and other technical information relevant to heat pump operation [#hpont-doc]_.

The ontology supports semantic annotation of heat pump data, enabling interoperability, data integration, querying, and reuse across smart-building and energy-management systems [#hpont-doc]_ [#hpont-bioregistry]_. HPOnt was developed in the context of the REACT project and is registered as the Heat Pump Ontology in Bioregistry [#hpont-bioregistry]_.

**Example Usage**:
Annotate a smart building energy management system with HPOnt terms to specify heat pump operating mode, cooling capacity, power supply, storage volume, power consumption, and related system information, enabling semantic search and integration with building energy management platforms [#hpont-doc]_ [#hpont-bioregistry]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 84
        * - **Total Edges**
          - 143
        * - **Root Nodes**
          - 16
        * - **Leaf Nodes**
          - 43
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 4
        * - **Individuals**
          - 6
        * - **Properties**
          - 12

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 4
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.13
        * - **Depth Variance**
          - 1.98
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 16
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 6.00
        * - **Breadth Variance**
          - 27.20
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 5
        * - **Taxonomic Relations**
          - 0
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 2.50
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import HPOnt

    ontology = HPOnt()
    ontology.load("path/to/HPOnt-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#hpont-doc] REACT Project. 2021.
   "The Heat Pump Ontology (HPOnt)."
   Ontology documentation.
   Available at:
   `https://react2020.github.io/REACT-ONTOLOGY/HPOnt/index-en.html <https://react2020.github.io/REACT-ONTOLOGY/HPOnt/index-en.html>`_

.. [#hpont-bioregistry] Bioregistry. n.d.
   "Heat Pump Ontology."
   Registry entry.
   Available at:
   `https://bioregistry.io/tib.hpont <https://bioregistry.io/tib.hpont>`_
