

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Medicine
       * - **Category**
         - Human Diseases
       * - **Current Version**
         - None
       * - **Last Updated**
         - 2024-12-18
       * - **Creator**
         - The Open Biological and Biomedical Ontology Foundry
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - owl
       * - **Download**
         - `Download Human Disease Ontology (DOID) <http://purl.obolibrary.org/obo/doid/releases/2024-12-18/doid.owl>`_

Human Disease Ontology (DOID)
========================================================================================================

The Disease Ontology (DOID) is a standardized, machine-readable ontology for describing and classifying human diseases [#doid-paper-2012]_ [#doid-paper-2022]_. It provides stable disease identifiers and a structured classification that supports the integration of disease-related knowledge across biomedical resources [#doid-paper-2012]_. The ontology was developed to provide a common semantic framework for human disease concepts and to improve interoperability between biological and clinical data sources [#doid-paper-2012]_ [#doid-paper-2022]_.

DOID supports disease annotation, data integration, search, and reuse across biomedical databases, genomics resources, and related research applications [#doid-paper-2012]_ [#doid-paper-2022]_. Its continued development has expanded disease classification, cross-references, definitions, and interoperability with other biomedical resources, supporting consistent disease representation and cross-resource comparison [#doid-paper-2022]_.

**Example Usage**:
Annotate a disease-related dataset or research resource with DOID identifiers, such as ``DOID:2841`` for lymphoma or ``DOID:9352`` for diabetes mellitus, to provide standardized disease annotations that can be linked and compared across biomedical databases and knowledge resources [#doid-paper-2012]_ [#doid-paper-2022]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 136876
        * - **Total Edges**
          - 288142
        * - **Root Nodes**
          - 14035
        * - **Leaf Nodes**
          - 95185
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 15343
        * - **Individuals**
          - 0
        * - **Properties**
          - 2

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 26
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 1.59
        * - **Depth Variance**
          - 1.07
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 61852
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 4291.67
        * - **Breadth Variance**
          - 172233228.89
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 41569
        * - **Non-taxonomic Relations**
          - 25
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import DOID

    ontology = DOID()
    ontology.load("path/to/DOID-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#doid-paper-2012] Schriml, L. M., Arze, C., Nadendla, S.,
   Chang, Y.-W. W., Mazaitis, M., Felix, V., Feng, G.,
   and Kibbe, W. A. 2012.
   "Disease Ontology: A Backbone for Disease Semantic Integration."
   *Nucleic Acids Research*, 40(Database issue), D940--D946.
   Available at:
   `https://doi.org/10.1093/nar/gkr972
   <https://doi.org/10.1093/nar/gkr972>`_

.. [#doid-paper-2022] Schriml, L. M., Munro, J. B., Schor, M.,
   et al. 2022.
   "The Human Disease Ontology 2022 Update."
   *Nucleic Acids Research*, 50(D1), D1255--D1261.
   Available at:
   `https://doi.org/10.1093/nar/gkab1063
   <https://doi.org/10.1093/nar/gkab1063>`_
