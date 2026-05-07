.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.0.0
       * - **Last Updated**
         - 2024-04-12
       * - **Creator**
         - https://orcid.org/0000-0002-4181-2852, https://orcid.org/0000-0002-5174-8508, https://orcid.org/0000-0002-9668-6961
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Characterisation Methodology Domain Ontology (CHAMEO) <https://github.com/emmo-repo/domain-characterisation-methodology>`_

Characterisation Methodology Domain Ontology (CHAMEO)
========================================================================================================

The Characterisation Methodology Domain Ontology (CHAMEO) is a domain ontology for materials characterisation that represents the CHADA template in ontological form [#chameo-github]_ [#chameo-paper]_. CHAMEO supports the generation of FAIR documentation for characterisation experiments and provides a foundation for developing technique-specific and application-specific ontologies in the materials characterisation domain [#chameo-github]_. It provides a structured vocabulary for describing characterisation methodologies, experimental workflows, samples, measurement processes, instruments, data acquisition, and data processing activities [#chameo-paper]_.

The ontology supports semantic annotation of materials characterisation data, enabling interoperability, data integration, knowledge sharing, and more consistent documentation across laboratories and digital materials platforms [#chameo-github]_ [#chameo-paper]_. By providing a standardized framework, CHAMEO helps improve reproducibility and comparison of materials characterisation experiments [#chameo-paper]_.

**Example Usage**:
Annotate a materials characterisation experiment with CHAMEO terms to specify the measurement technique, sample preparation, instrument configuration, measurement process, acquired data, and data analysis workflow. For example, an X-ray diffraction experiment can be described using CHAMEO concepts for the sample, characterisation method, instrument setup, measurement activity, and data processing steps, enabling semantic search and integration with materials databases [#chameo-github]_ [#chameo-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 802
        * - **Total Edges**
          - 1526
        * - **Root Nodes**
          - 29
        * - **Leaf Nodes**
          - 459
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 203
        * - **Individuals**
          - 0
        * - **Properties**
          - 52

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 12
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 4.25
        * - **Depth Variance**
          - 8.29
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 45
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 19.92
        * - **Breadth Variance**
          - 154.69
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 195
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import CHAMEO

    ontology = CHAMEO()
    ontology.load("path/to/CHAMEO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#chameo-github] EMMO-repo. n.d.
   "Characterisation Methodology Domain Ontology."
   GitHub repository.
   Available at:
   `https://github.com/emmo-repo/domain-characterisation-methodology <https://github.com/emmo-repo/domain-characterisation-methodology>`_

.. [#chameo-paper] Del Nostro, P., Goldbeck, G., and Toti, D. 2022.
   "CHAMEO: An ontology for the harmonisation of materials characterisation methodologies."
   *Applied Ontology*, 17, 401--421.
   DOI: 10.3233/AO-220271.
   Available at:
   `https://journals.sagepub.com/doi/10.3233/AO-220271 <https://journals.sagepub.com/doi/10.3233/AO-220271>`_
