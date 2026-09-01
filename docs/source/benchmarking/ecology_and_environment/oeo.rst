

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Ecology and Environment
       * - **Category**
         - Energy
       * - **Current Version**
         - 2.7.0
       * - **Last Updated**
         - 03/2025
       * - **Creator**
         - None
       * - **License**
         - Creative Commons Attribution 1.0 Generic (CC BY 1.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download The Open Energy Ontology (OEO) <https://github.com/OpenEnergyPlatform/ontology?tab=readme-ov-file>`_

The Open Energy Ontology (OEO)
========================================================================================================

The Open Energy Ontology (OEO) is a domain ontology designed for the
energy system analysis context, covering concepts, relationships, and
entities relevant to energy research and planning [#oeo-paper]_
[#oeo-site]_. Developed as part of the Open Energy Family and used
within the Open Energy Platform ecosystem, OEO provides standardized
terminology for representing energy systems, including generation,
conversion, transmission, distribution, storage, and consumption
concepts across different technologies and sectors [#oeo-paper]_
[#oeo-site]_. The ontology is intended to support collaborative and
interoperable modeling of energy knowledge, enabling clearer data
interpretation and more consistent interfacing between models, datasets,
and analytical workflows [#oeo-paper]_ [#oeo-site]_. OEO is updated
through an ongoing development and release process in order to
incorporate concepts relevant to energy system modelling and analysis
[#oeo-site]_ [#oeo-paper]_. By providing a shared semantic framework,
OEO supports standardized data annotation, knowledge integration,
semantic search, model interfacing, and automated reasoning for energy
system research and related applications [#oeo-paper]_ [#oeo-site]_.

**Example Usage**: Annotate an energy system dataset with OEO terms to
describe energy carriers and sources, generation technologies,
transmission or distribution infrastructure, storage systems, demand
concepts, or scenario-study entities, enabling semantic search,
interoperable data integration, and analysis of energy system
configurations and transition scenarios [#oeo-paper]_ [#oeo-site]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 10
        * - **Total Edges**
          - 8
        * - **Root Nodes**
          - 8
        * - **Leaf Nodes**
          - 2
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 0
        * - **Individuals**
          - 0
        * - **Properties**
          - 0

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
          - 0.20
        * - **Depth Variance**
          - 0.16
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 8
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 5.00
        * - **Breadth Variance**
          - 9.00
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

    from ontolearner.ontology import OEO

    ontology = OEO()
    ontology.load("path/to/OEO-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#oeo-paper] Booshehri, M., Emele, L., Flügel, S., Förster, H.,
   Frey, J., Frey, U., Glauer, M., Hastings, J., Hofmann, C.,
   Hoyer-Klick, C., Hülk, L., Kleinau, A., Knosala, K., Kotzur, L.,
   Kuckertz, P., Mossakowski, T., Muschner, C., Neuhaus, F., Pehl, M.,
   Robinius, M., Sehn, V., and Stappel, M. 2021.
   "Introducing the Open Energy Ontology: Enhancing Data Interpretation
   and Interfacing in Energy Systems Analysis."
   *Energy and AI* 5:100074.
   doi:10.1016/j.egyai.2021.100074
   Available at: `https://publications.pik-potsdam.de/pubman/item/item_25641_2/component/file_25642/25641oa.pdf <https://publications.pik-potsdam.de/pubman/item/item_25641_2/component/file_25642/25641oa.pdf>`_

.. [#oeo-site] Open Energy Platform. n.d. "OEO Ontology."
   Available at: `https://openenergyplatform.org/ontology/ <https://openenergyplatform.org/ontology/>`_
