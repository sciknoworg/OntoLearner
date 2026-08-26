

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
OPMW, the Open Provenance Model for Workflows, is an ontology for the semantic description of computational workflow templates and their execution provenance [#opmw-ontology]_ [#opmw-fgcs]_. It provides a structured vocabulary for representing workflow templates, workflow steps, input and output artifacts, execution processes, agents, parameter values, software components, and provenance relationships that describe how data and computational activities are connected [#opmw-ontology]_.

The ontology supports representation of both the prospective structure of a workflow and the retrospective provenance of its execution [#opmw-ontology]_ [#opmw-fgcs]_. This makes it possible to describe how computational results were produced, which inputs and tools were used, what intermediate and final outputs were generated, and how individual workflow steps were related [#opmw-fgcs]_. OPMW supports the publication of workflow descriptions and execution information as Linked Data, facilitating workflow sharing, discovery, comparison, and reuse [#opmw-fgcs]_.

Typical applications of OPMW include scientific workflow documentation, workflow repository metadata, provenance tracking, reproducibility support, and semantic publication of computational workflows [#opmw-ontology]_ [#opmw-fgcs]_. By providing a common semantic representation for workflow structure and execution provenance, OPMW enables researchers to publish, discover, understand, and reuse workflows across scientific computing environments [#opmw-fgcs]_.

**Example Usage**:
Annotate a bioinformatics workflow with OPMW terms to describe workflow steps such as sequence alignment and variant calling, input datasets, generated outputs, software components, parameter values, execution processes, and provenance relationships. This provides a machine-readable description of both the workflow design and its execution history, supporting reproducibility, provenance analysis, discovery, and reuse [#opmw-ontology]_ [#opmw-fgcs]_.

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

.. [#opmw-fgcs] Garijo, D., Gil, Y., and Corcho, O. 2017.
   "Abstract, Link, Publish, Exploit:
   An End-to-End Framework for Workflow Sharing."
   *Future Generation Computer Systems*.
   Available at:
   `http://dgarijo.com/papers/fgcs2017.pdf
   <http://dgarijo.com/papers/fgcs2017.pdf>`_
