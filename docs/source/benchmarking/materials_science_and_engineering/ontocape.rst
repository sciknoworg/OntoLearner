.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Materials Science and Engineering
       * - **Category**
         - Manufacturing
       * - **Current Version**
         - 2.0
       * - **Last Updated**
         - None
       * - **Creator**
         - RWTH Aachen University
       * - **License**
         - GNU General Public License
       * - **Format**
         - OWL
       * - **Download**
         - `Download Ontology of Computer-Aided Process Engineering (OntoCAPE) <https://www.avt.rwth-aachen.de/cms/avt/forschung/sonstiges/software/~ipts/ontocape/?lidx=1>`_

Ontology of Computer-Aided Process Engineering (OntoCAPE)
========================================================================================================

The Ontology of Computer-Aided Process Engineering (OntoCAPE) is a
large-scale, formal ontology for the domain of Computer-Aided Process
Engineering (CAPE) [#ontocape-homepage]_ [#ontocape-v2]_.
It captures domain knowledge in a machine-interpretable form so that
process-engineering knowledge can be reused and shared across people
and software systems [#ontocape-paper]_ [#ontocape-v2]_.

OntoCAPE is organized as a modular ontology framework and was developed
to balance usability for specific engineering applications with
reusability across different CAPE tasks [#ontocape-paper]_
[#ontocape-v2]_. It supports applications including knowledge
management, mathematical modelling, plant design, management and
retrieval of simulation models and engineering documents, equipment
procurement, and integration of information from distributed sources
[#ontocape-homepage]_ [#ontocape-paper]_.

By providing a formal semantic representation of process-engineering
knowledge, OntoCAPE supports interoperability, knowledge sharing, and
integration of heterogeneous engineering information
[#ontocape-paper]_ [#ontocape-v2]_.

**Example Usage**:
Annotate a process-engineering project with OntoCAPE concepts to
represent process systems, plant equipment, mathematical models,
simulation models, and related engineering information, enabling
knowledge retrieval, integration, and reuse across CAPE software
applications [#ontocape-homepage]_ [#ontocape-v2]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 11
        * - **Total Edges**
          - 10
        * - **Root Nodes**
          - 1
        * - **Leaf Nodes**
          - 10
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
          - 0.91
        * - **Depth Variance**
          - 0.08
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 10
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 5.50
        * - **Breadth Variance**
          - 20.25
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 179
        * - **Non-taxonomic Relations**
          - 0
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import OntoCAPE

    ontology = OntoCAPE()
    ontology.load("path/to/OntoCAPE-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#ontocape-homepage] RWTH Aachen University.
   "Ontology of Computer-Aided Process Engineering (OntoCAPE)."
   Aachener Verfahrenstechnik, RWTH Aachen University.
   Available at:
   `OntoCAPE <https://www.avt.rwth-aachen.de/cms/avt/forschung/sonstiges/software/~ipts/ontocape/?lidx=1>`_

.. [#ontocape-v2] Morbach, J., Wiesner, A., and Marquardt, W. 2008.
   "OntoCAPE 2.0 -- A (Re-)usable Ontology for
   Computer-Aided Process Engineering."
   In *Computer Aided Chemical Engineering*, vol. 25,
   pp. 991--996.
   `doi:10.1016/S1570-7946(08)80171-X <https://doi.org/10.1016/S1570-7946(08)80171-X>`_

.. [#ontocape-paper] Morbach, J., Yang, A., and Marquardt, W. 2007.
   "OntoCAPE -- A Large-Scale Ontology for
   Chemical Process Engineering."
   *Engineering Applications of Artificial Intelligence*
   20(2):147--161.
   `doi:10.1016/j.engappai.2006.06.010 <https://doi.org/10.1016/j.engappai.2006.06.010>`_
