.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Materials Science
       * - **Current Version**
         - 0.4.3
       * - **Last Updated**
         - None
       * - **Creator**
         - Lukas Gold, Simon Stier
       * - **License**
         - Creative Commons Attribution 4.0 International (CC BY 4.0)
       * - **Format**
         - ttl
       * - **Download**
         - `Download Battery Value Chain Ontology (BVCO) <https://github.com/Battery-Value-Chain-Ontology/ontology>`_

Battery Value Chain Ontology (BVCO)
========================================================================================================

The Battery Value Chain Ontology (BVCO) is a domain ontology developed to model processes along the battery value chain [#bvco-github]_ [#bvco-zenodo]_. BVCO provides a structured vocabulary for describing holistic processes that transform inputs or educts, such as matter, energy, and information, into outputs or products using tools such as devices and algorithms [#bvco-github]_. The ontology supports decomposition of processes into sub-processes and captures predecessor and successor relationships, enabling detailed representation of battery value chain activities [#bvco-github]_.

BVCO facilitates semantic annotation of battery value chain data and supports interoperability, data integration, and knowledge sharing across battery research and industrial workflows [#bvco-github]_. It is described as a work-in-progress ontology and is based on the General Process Ontology (GPO) and EMMO [#bvco-github]_.

**Example Usage**:
Annotate a battery manufacturing workflow with BVCO terms to specify raw material processing, cell production, quality-control steps, logistics, and recycling processes, enabling semantic search and integration with battery value chain data platforms [#bvco-github]_.


Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 804
        * - **Total Edges**
          - 1719
        * - **Root Nodes**
          - 85
        * - **Leaf Nodes**
          - 283
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 262
        * - **Individuals**
          - 0
        * - **Properties**
          - 6

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 14
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.47
        * - **Depth Variance**
          - 5.27
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 230
        * - **Minimum Breadth**
          - 2
        * - **Average Breadth**
          - 52.20
        * - **Breadth Variance**
          - 4920.43
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

    from ontolearner.ontology import BVCO

    ontology = BVCO()
    ontology.load("path/to/BVCO-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#bvco-github] Battery-Value-Chain-Ontology. n.d.
   "Battery Value Chain Ontology."
   GitHub repository.
   Available at:
   `https://github.com/Battery-Value-Chain-Ontology/ontology <https://github.com/Battery-Value-Chain-Ontology/ontology>`_

.. [#bvco-zenodo] Stier, S., and Gold, L. 2023.
   "Battery Value Chain Ontology (BVCO)."
   Zenodo.
   DOI: 10.5281/zenodo.8114726.
   Available at:
   `https://zenodo.org/records/8114726 <https://zenodo.org/records/8114726>`_
