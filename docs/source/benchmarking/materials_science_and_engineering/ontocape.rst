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

The Ontology of Computer-Aided Process Engineering (OntoCAPE) is a large-scale ontology for the domain of Computer-Aided Process Engineering (CAPE) [#ontocape-homepage]_. It is represented in a formal, machine-interpretable ontology language and captures consensual knowledge of the process engineering domain in a generic way so that it can be reused and shared across groups of people and software systems [#ontocape-homepage]_.

OntoCAPE supports the development of software tools for engineering activities such as the systematic management and retrieval of simulation models and design documents, electronic procurement of plant equipment, mathematical modelling, and integration of design data from distributed sources [#ontocape-homepage]_. By providing a standardized semantic framework, OntoCAPE facilitates interoperability, knowledge sharing, and data integration in process engineering and manufacturing-related workflows [#ontocape-homepage]_.

**Example Usage**:
Annotate a process engineering project with OntoCAPE terms to specify process types, plant equipment, simulation models, mathematical models, and design data, enabling semantic search and integration with process informatics platforms [#ontocape-homepage]_.

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

.. [#ontocape-homepage] RWTH Aachen University. n.d.
   "Ontology of Computer-Aided Process Engineering (OntoCAPE)."
   Available at:
   `https://www.avt.rwth-aachen.de/cms/avt/forschung/sonstiges/software/~ipts/ontocape/?lidx=1 <https://www.avt.rwth-aachen.de/cms/avt/forschung/sonstiges/software/~ipts/ontocape/?lidx=1>`_
