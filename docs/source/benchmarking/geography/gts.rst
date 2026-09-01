.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Geography
       * - **Category**
         - geospatial Information, Geology
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 2020-05-31
       * - **Creator**
         - Simon J D Cox (simon.cox@csiro.au) of CSIRO
       * - **License**
         - Creative Commons 1.0
       * - **Format**
         - ttl
       * - **Download**
         - `Download Geologic Timescale model (GTS) <https://raw.githack.com/CGI-IUGS/timescale-ont/master/html/gts.html>`_

Geologic Timescale model (GTS)
========================================================================================================

The Geologic Timescale (GTS) is an RDF/OWL ontology representation of the standard geologic timescale model, adapted from the GeoSciML framework and compatible with geospatial information transfer standards [#gts-ontology]_ [#gts-cox-richard-2015]_. It provides a formal semantic model for representing geological time periods, epochs, eons, stages, and their boundaries [#gts-cox-richard-2015]_. GTS enables precise temporal annotation of geological data, allowing scientists to associate geological observations, samples, fossil records, stratigraphic units, and events with specific intervals in Earth's history [#gts-ontology]_. The ontology supports hierarchical relationships between geological time divisions, enabling both broad geological age classification and detailed temporal analysis [#gts-ontology]_ [#gts-cox-richard-2015]_. GTS facilitates integration of paleontological, stratigraphic, and geological survey data across diverse research institutions, databases, and linked data systems [#gts-cox-richard-2015]_.

**Example Usage**:
Annotate a rock sample or fossil record with GTS terms such as ``Cretaceous``, ``Campanian``, or specific geologic time boundary information to enable temporal querying, stratigraphic correlation, and integration with geological survey datasets [#gts-ontology]_ [#gts-cox-richard-2015]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 311
        * - **Total Edges**
          - 743
        * - **Root Nodes**
          - 0
        * - **Leaf Nodes**
          - 92
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 40
        * - **Individuals**
          - 7
        * - **Properties**
          - 12

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 0
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 0.00
        * - **Depth Variance**
          - 0.00
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 0
        * - **Minimum Breadth**
          - 0
        * - **Average Breadth**
          - 0.00
        * - **Breadth Variance**
          - 0.00
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 7
        * - **Taxonomic Relations**
          - 77
        * - **Non-taxonomic Relations**
          - 2
        * - **Average Terms per Type**
          - 7.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import GTS

    ontology = GTS()
    ontology.load("path/to/GTS-ontology.ttl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#gts-ontology] CGI-IUGS. n.d.
   "Geologic Timescale Ontology."
   GitHub Repository.
   Available at:
   `https://github.com/CGI-IUGS/timescale-ont <https://github.com/CGI-IUGS/timescale-ont>`_

.. [#gts-cox-richard-2015] Cox, Simon J. D., and Stephen M. Richard. 2015.
   "A Geologic Timescale Ontology and Service."
   Available at:
   `https://publications.csiro.au/publications/publication/PIcsiro:EP14855 <https://publications.csiro.au/publications/publication/PIcsiro:EP14855>`_
