.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Mechanical Testing
       * - **Current Version**
         - 1.0.0
       * - **Last Updated**
         - None
       * - **Creator**
         - Fraunhofer IWM
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Mechanical Testing Ontology (MechanicalTesting) <https://github.com/emmo-repo/domain-mechanical-testing>`_

Mechanical Testing Ontology (MechanicalTesting)
========================================================================================================

The Mechanical Testing Ontology (MechanicalTesting) is a domain ontology developed to represent knowledge in the field of mechanical testing and is built on top of the Elementary Multiperspective Material Ontology (EMMO) [#mechanicaltesting-github]_ [#morgado2020]_. It provides a structured vocabulary for describing mechanical testing concepts, supporting semantic representation of experiments, models, software, and data in materials science [#morgado2020]_.

The ontology supports semantic annotation, data integration, interoperability, and sharing of mechanical-testing information across materials science workflows [#mechanicaltesting-github]_ [#morgado2020]_. It is described as an EMMO-based domain ontology and was developed as part of efforts to create EMMO-compliant domain ontologies for materials science [#mechanicaltesting-github]_ [#morgado2020]_. By providing a standardized semantic framework, MechanicalTesting supports knowledge representation, data retrieval, and reuse in mechanical testing and digital-twin-related applications [#morgado2020]_.

**Example Usage**:
Annotate a mechanical testing dataset with MechanicalTesting terms to specify mechanical testing methods, experiment-related information, test data, models, software, and results, enabling semantic search and integration with materials informatics platforms [#mechanicaltesting-github]_ [#morgado2020]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1365
        * - **Total Edges**
          - 2569
        * - **Root Nodes**
          - 174
        * - **Leaf Nodes**
          - 713
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 369
        * - **Individuals**
          - 0
        * - **Properties**
          - 5

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 18
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.14
        * - **Depth Variance**
          - 4.98
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 466
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 66.89
        * - **Breadth Variance**
          - 14051.46
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 36
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import MechanicalTesting

    ontology = MechanicalTesting()
    ontology.load("path/to/MechanicalTesting-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#mechanicaltesting-github] EMMO-repo. n.d.
   "Domain: mechanical-testing."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/domain-mechanical-testing <https://github.com/emmo-repo/domain-mechanical-testing>`_

.. [#morgado2020] Morgado, J. F., Ghedini, E., Goldbeck, G., Hashibon, A., Schmitz, G. J., Friis, J., and de Baas, A. F. 2020.
   "Mechanical testing ontology for digital-twins: A roadmap based on EMMO."
   *International Workshop on Semantic Digital Twins (SeDiT 2020)*.
   Available at:
   `https://publica.fraunhofer.de/entities/publication/cda015f5-a194-4e82-8b5f-cba29b43cf5b <https://publica.fraunhofer.de/entities/publication/cda015f5-a194-4e82-8b5f-cba29b43cf5b>`_
