

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Scholarly Knowledge
       * - **Category**
         - Workflows
       * - **Current Version**
         - 3.1
       * - **Last Updated**
         - 2014-12-22
       * - **Creator**
         - http://delicias.dia.fi.upm.es/members/DGarijo/#me, http://www.isi.edu/~gil/
       * - **License**
         - Creative Commons Attribution 2.0 Generic (CC BY 2.0)
       * - **Format**
         - owl
       * - **Download**
         - `Download Open Provenance Model for Workflows (OPMW) <https://www.opmw.org/model/OPMW_20141222/>`_

Open Provenance Model for Workflows (OPMW)
========================================================================================================
OPMW, the Open Provenance Model for Workflows, is an ontology for the semantic description of computational workflow templates and workflow execution traces [#opmw-ontology]_ [#opmw-publications]_. It is based on the Open Provenance Model and was designed as an OPM profile, extending and reusing OPM's core ontologies, including OPMV and OPMO, while later aligning with W3C PROV for provenance representation [#opmw-ontology]_. OPMW provides vocabulary for describing workflow templates, workflow steps, input and output artifacts, execution accounts, execution processes, agents, parameter values, software components, and provenance links that track data flow and transformations [#opmw-ontology]_.

The ontology supports systematic documentation and sharing of scientific workflows by representing both the prospective structure of a workflow and the retrospective provenance of its execution [#opmw-ontology]_ [#opmw-publications]_. This makes it useful for describing how computational results were produced, which input datasets and tools were used, what intermediate outputs were generated, and how workflow steps were connected [#opmw-ontology]_. OPMW therefore supports reproducibility, reuse, workflow comparison, provenance querying, and publication of workflow metadata as Linked Data [#opmw-publications]_.

Typical applications of OPMW include scientific workflow documentation, workflow repository metadata, provenance tracking, reproducibility support, data-intensive research, and integration between workflow management systems and semantic web platforms [#opmw-ontology]_ [#opmw-publications]_. By providing a standardized provenance model for workflows, OPMW helps researchers publish, discover, compare, and reuse computational workflows and their execution traces [#opmw-publications]_.

**Example Usage**:
Annotate a bioinformatics workflow with OPMW terms to describe workflow steps such as sequence alignment and variant calling, inputs such as raw sequencing data, outputs such as VCF files, execution agents, software tools, parameter settings, intermediate artifacts, and provenance relationships. This enables workflow reproducibility, semantic search, provenance tracking, and reuse across scientific computing platforms [#opmw-ontology]_ [#opmw-publications]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 539
        * - **Total Edges**
          - 1387
        * - **Root Nodes**
          - 33
        * - **Leaf Nodes**
          - 306
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 59
        * - **Individuals**
          - 2
        * - **Properties**
          - 87

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 6
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.14
        * - **Depth Variance**
          - 2.07
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 59
        * - **Minimum Breadth**
          - 5
        * - **Average Breadth**
          - 31.57
        * - **Breadth Variance**
          - 405.67
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 77
        * - **Non-taxonomic Relations**
          - 4
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OPMW

    ontology = OPMW()
    ontology.load("path/to/OPMW-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#opmw-ontology] OPMW. 2014.
   "The OPMW-PROV Ontology."
   Available at:
   `https://www.opmw.org/ontology/ <https://www.opmw.org/ontology/>`_

.. [#opmw-publications] OPMW. n.d.
   "OPMW-PROV: The Open Provenance Model for Workflows - Publications."
   Available at:
   `https://www.opmw.org/publications.html <https://www.opmw.org/publications.html>`_
