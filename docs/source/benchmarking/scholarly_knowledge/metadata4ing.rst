.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 1.3.1
       * - **Last Updated**
         - 2025-03-10
       * - **Creator**
         - Metadata4Ing Workgroup
       * - **License**
         - Creative Commons 4.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Metadata for Intelligent Engineering (Metadata4Ing) <https://git.rwth-aachen.de/nfdi4ing/metadata4ing/metadata4ing>`_

Metadata for Intelligent Engineering (Metadata4Ing)
========================================================================================================

The Metadata4Ing ontology provides a semantic framework for describing research data and the processes through which those data are generated, with a particular focus on engineering sciences and related disciplines [#m4i-nfdi]_ [#m4i-zenodo]_. It supports the representation of experiments, observations, simulations, objects of investigation, sample and data manipulation procedures, generated data files, and the personal or institutional roles involved in a research activity [#m4i-nfdi]_ [#m4i-zenodo]_.

Metadata4Ing follows a modular and extensible modeling approach in which research processes can be described through classes and relationships for methods, tools, variables, organizations, people, roles, and generated outputs [#m4i-nfdi]_. This allows the ontology to capture not only the resulting research data, but also the contextual and procedural information needed to understand how those data were produced [#m4i-nfdi]_ [#m4i-zenodo]_. The ontology therefore supports machine-readable documentation of research workflows and facilitates interpretation, integration, and reuse of engineering research data [#m4i-nfdi]_.

Metadata4Ing is intended for research data management and semantic description of scientific activities, including experimental, observational, simulation, and data-processing workflows [#m4i-nfdi]_ [#m4i-zenodo]_. Its structured representation of data-generation processes can support provenance documentation, interoperability between research infrastructures, FAIR-oriented data publication, and reuse of research information across engineering and neighbouring scientific domains [#m4i-nfdi]_ [#m4i-zenodo]_.

**Example Usage**:
Annotate an engineering experiment with Metadata4Ing terms to describe the object of investigation, the experimental or simulation method, tools and configurations used, variables and parameters, generated data files, and the persons or institutions responsible for different parts of the process. This provides a machine-readable description of how the research data were generated and supports provenance tracking, interpretation, and reuse [#m4i-nfdi]_ [#m4i-zenodo]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 1032
        * - **Total Edges**
          - 1517
        * - **Root Nodes**
          - 109
        * - **Leaf Nodes**
          - 731
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 48
        * - **Individuals**
          - 47
        * - **Properties**
          - 100

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 7
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.54
        * - **Depth Variance**
          - 1.36
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 413
        * - **Minimum Breadth**
          - 4
        * - **Average Breadth**
          - 109.75
        * - **Breadth Variance**
          - 18099.19
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 37
        * - **Taxonomic Relations**
          - 44
        * - **Non-taxonomic Relations**
          - 6
        * - **Average Terms per Type**
          - 9.25
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import Metadata4Ing

    ontology = Metadata4Ing()
    ontology.load("path/to/Metadata4Ing-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#m4i-nfdi] Metadata4Ing Workgroup. 2025.
   "Metadata4Ing: An Ontology for Describing the Generation
   of Research Data within a Scientific Activity."
   Ontology documentation.
   Available at:
   `https://nfdi4ing.pages.rwth-aachen.de/metadata4ing/metadata4ing/
   <https://nfdi4ing.pages.rwth-aachen.de/metadata4ing/metadata4ing/>`_

.. [#m4i-zenodo] Lanza, G., Iglezakis, D., Fuhrmans, M.,
   Jordan, M., Farnbacher, B., Sosa Rodriguez, A. A.,
   Leimer, S., Hachinger, S., Arndt, S., Terzijska, D.,
   et al. 2025.
   "Metadata4Ing: An Ontology for Describing the Generation
   of Research Data within a Scientific Activity."
   Version v7. Zenodo.
   Available at:
   `https://doi.org/10.5281/zenodo.17856129
   <https://doi.org/10.5281/zenodo.17856129>`_
