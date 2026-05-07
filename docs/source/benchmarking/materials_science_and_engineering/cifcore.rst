.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.1.0
       * - **Last Updated**
         - May 24, 2023
       * - **Creator**
         - None
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Crystallographic Information Framework Core Dictionary (CIFCore) <https://github.com/emmo-repo/CIF-ontology?tab=readme-ov-file>`_

Crystallographic Information Framework Core Dictionary (CIFCore)
========================================================================================================

The Crystallographic Information Framework Core Dictionary (CIFCore) is a machine-readable dictionary developed to represent core crystallographic data within the Crystallographic Information Framework (CIF) [#cifcore-iucr]_. It provides structured data names for archiving and exchanging raw data, processed data, and derived structural results in crystallography and related structural sciences [#cifcore-iucr]_.

The CIF Ontology provides an ontological representation of the CIF Dictionary Definition Language (DDLm) and the IUCr CIF core dictionary, supporting semantic annotation and machine-actionable use of CIF data [#cif-ontology-github]_. CIFCore supports the standardized description of crystallographic information such as crystal structures, symmetry information, atomic coordinates, diffraction data, and experimental details [#cifcore-iucr]_ [#cif-ontology-github]_. By providing a structured vocabulary, CIFCore supports data exchange, validation, interoperability, reproducibility, and integration with crystallographic and structural databases [#cifcore-iucr]_ [#cif-ontology-github]_.

**Example Usage**:
Annotate a crystallographic dataset with CIFCore terms to specify crystal lattice parameters, atomic positions, symmetry information, diffraction experiment details, and derived structural results, enabling semantic search, validation, and integration with structural databases [#cifcore-iucr]_ [#cif-ontology-github]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 4494
        * - **Total Edges**
          - 15377
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 3310
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 1182
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
          - 0.75
        * - **Depth Variance**
          - 0.19
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 3
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 2.00
        * - **Breadth Variance**
          - 1.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 27150
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CIFCore

    ontology = CIFCore()
    ontology.load("path/to/CIFCore-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#cifcore-iucr] International Union of Crystallography. n.d.
   "Core CIF dictionary."
   Available at:
   `https://www.iucr.org/resources/cif/dictionaries/cif_core <https://www.iucr.org/resources/cif/dictionaries/cif_core>`_

.. [#cif-ontology-github] EMMO-repo. n.d.
   "CIF Ontology."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/CIF-ontology <https://github.com/emmo-repo/CIF-ontology>`_
