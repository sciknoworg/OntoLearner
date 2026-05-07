.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Biomaterials
       * - **Current Version**
         - 06/2021
       * - **Last Updated**
         - Jun 2, 2021
       * - **Creator**
         - Osnat Hakimi
       * - **License**
         - GPL-3.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Devices, Experimental scaffolds and Biomaterials Ontology (DEB) <https://github.com/ProjectDebbie/Ontology_DEB>`_

Devices, Experimental scaffolds and Biomaterials Ontology (DEB)
========================================================================================================

The Devices, Experimental Scaffolds and Biomaterials Ontology (DEB) is an ontology for organizing information about biomaterials, devices, experimental scaffolds, and related biological testing [#deb-github]_ [#deb-bioportal]_. It provides a structured vocabulary for describing biomaterial types, scaffold-related concepts, device information, fabrication or processing details, and biological evaluation data [#deb-github]_ [#deb-bioportal]_.

DEB supports semantic annotation, data integration, search, and reuse of biomaterials research information across experimental studies and databases [#deb-github]_ [#deb-bioportal]_. By providing standardized terminology, DEB helps organize biomaterials knowledge and supports cross-study comparison in biomaterials science and tissue engineering [#deb-bioportal]_.

**Example Usage**:
Annotate a biomaterials experiment with DEB terms to specify the scaffold material, device type, fabrication or processing method, and biological assay information, enabling semantic search, cross-study comparison, and data integration [#deb-github]_ [#deb-bioportal]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1081
        * - **Total Edges**
          - 2354
        * - **Root Nodes**
          - 533
        * - **Leaf Nodes**
          - 278
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 601
        * - **Individuals**
          - 0
        * - **Properties**
          - 120

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
          - 0.67
        * - **Depth Variance**
          - 0.59
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 533
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 213.80
        * - **Breadth Variance**
          - 43756.96
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 672
        * - **Non-taxonomic Relations**
          - 8
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DEB

    ontology = DEB()
    ontology.load("path/to/DEB-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#deb-github] ProjectDebbie. n.d.
   "Ontology_DEB: The Device, Experimental Scaffolds and Biomaterials Ontology."
   GitHub repository.
   Available at:
   `https://github.com/ProjectDebbie/Ontology_DEB <https://github.com/ProjectDebbie/Ontology_DEB>`_

.. [#deb-bioportal] BioPortal. 2021.
   "Devices, Experimental scaffolds and Biomaterials Ontology."
   Ontology registry entry.
   Available at:
   `https://bioportal.bioontology.org/ontologies/DEB <https://bioportal.bioontology.org/ontologies/DEB>`_
