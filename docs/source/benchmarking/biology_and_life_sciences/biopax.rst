

.. sidebar::

    .. list-table:: **Ontology Card**
       :header-rows: 0

       * - **Domain**
         - Biology and Life Sciences
       * - **Category**
         - Bioinformatics
       * - **Current Version**
         - 1.0
       * - **Last Updated**
         - 16 April 2015
       * - **Creator**
         - None
       * - **License**
         - None
       * - **Format**
         - owl
       * - **Download**
         - `Download Biological Pathways Exchange (BioPAX) <http://www.biopax.org/>`_

Biological Pathways Exchange (BioPAX)
========================================================================================================

BioPAX (Biological Pathway Exchange) is a standard RDF/OWL-based
language and ontology for exchanging, integrating, and analyzing
biological pathway data [#biopax-paper]_ [#biopax-spec]_. It enables the
representation of molecular interaction networks, including metabolic and
signaling pathways, molecular and genetic interactions, and gene
regulation processes [#biopax-paper]_ [#biopax-spec]_. BioPAX models
core pathway concepts such as interactions, physical entities
(for example proteins, DNA, RNA, complexes, and small molecules),
pathways, and their associated biological and cellular properties
[#biopax-paper]_ [#biopax-spec]_. The ontology is designed to reduce
complexity in data interchange by providing a unified format that
supports integration across pathway databases, visualization tools, and
computational analysis platforms [#biopax-paper]_. BioPAX is widely used
in pathway informatics and has been adopted by major resources and tools
for pathway data sharing and integration [#biopax-paper]_ [#pathway-commons]_.
By providing a common semantic framework for pathway representation,
BioPAX supports systems biology analysis, pathway visualization, and
interoperable exchange of biological knowledge across diverse resources
[#biopax-paper]_.

**Example Usage**: Represent a phosphorylation event as a BioPAX
BiochemicalReaction in which a protein substrate is converted into its
phosphorylated form, linked to the relevant catalyst or controller,
cellular location, and pathway context to enable pathway exchange,
visualization, and computational analysis [#biopax-spec]_ [#biopax-paper]_.

Metrics & Statistics
--------------------------

.. tab:: Graph


    .. list-table:: Graph Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - 555
        * - **Total Edges**
          - 1611
        * - **Root Nodes**
          - 68
        * - **Leaf Nodes**
          - 200
    ::


.. tab:: Coverage


    .. list-table:: Knowledge Coverage Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - 92
        * - **Individuals**
          - 0
        * - **Properties**
          - 96

    ::

.. tab:: Hierarchy


    .. list-table:: Hierarchical Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Depth**
          - 15
        * - **Minimum Depth**
          - 0
        * - **Average Depth**
          - 2.70
        * - **Depth Variance**
          - 6.33
    ::


.. tab:: Breadth


    .. list-table:: Breadth Metrics
        :widths: 50 50
        :header-rows: 0

        * - **Maximum Breadth**
          - 138
        * - **Minimum Breadth**
          - 1
        * - **Average Breadth**
          - 34.50
        * - **Breadth Variance**
          - 1919.38
    ::

.. tab:: LLMs4OL


    .. list-table:: LLMs4OL Dataset Statistics
        :widths: 50 50
        :header-rows: 0

        * - **Term Types**
          - 0
        * - **Taxonomic Relations**
          - 126
        * - **Non-taxonomic Relations**
          - 446
        * - **Average Terms per Type**
          - 0.00
    ::

Usage Example
----------------
Use the following code to import this ontology programmatically:

.. code-block:: python

    from ontolearner.ontology import BioPAX

    ontology = BioPAX()
    ontology.load("path/to/BioPAX-ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations

References
----------

.. [#biopax-paper] Demir, E., Cary, M. P., Paley, S., Fukuda, K.,
   Lemer, C., Vastrik, I., Wu, G., D'Eustachio, P., Schaefer, C.,
   Luciano, J., Schacherer, F., Martinez-Flores, I., Hu, Z.,
   Jimenez-Jacinto, V., Joshi-Tope, G., Kandasamy, K., Lopez-Fuentes,
   A. C., Mi, H., Pichler, E., Rodchenkov, I., Splendiani, A.,
   Tkachev, S., Zucker, J., Gopinath, G., Rajasimha, H., Ramakrishnan,
   R., Shah, I., Syed, M., Anwar, N., Babur, O., Blinov, M., Brauner,
   E., Corwin, D., Donaldson, S., Gibbons, F., Goldberg, R.,
   Hornbeck, P., Luna, A., Murray-Rust, P., Neumann, E., Reubenacker,
   O., Samwald, M., van Iersel, M., Wimalaratne, S., Allen, K.,
   Braun, B., Whirl-Carrillo, M., Cheung, K.-H., Dahlquist, K.,
   Finney, A., Gillespie, M., Glass, E., Gong, L., Haw, R.,
   Honig, M., Hubaut, O., Kane, D., Krupa, S., Kutmon, M.,
   Leonard, J., Marks, D., Merberg, D., Petri, V., Pico, A.,
   Ravenscroft, D., Ren, L., Shah, N., Sunshine, M., Tang, R.,
   Whaley, R., Letovksy, S., Buetow, K. H., Rzhetsky, A.,
   Schriml, L. M., Shah, N. H., Wilkinson, M. D., Kelder, T.,
   Collado-Vides, J., Goto, S., Hofestädt, R., Hermjakob, H.,
   and Bader, G. D. 2010. "The BioPAX Community Standard for Pathway
   Data Sharing."
   *Nature Biotechnology* 28(9): 935-942.
   doi:10.1038/nbt.1666
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC3001121/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC3001121/>`_

.. [#biopax-spec] BioPAX Editorial Board. n.d.
   "BioPAX Level 3 Documentation."
   Available at: `https://biopax.github.io/Paxtools/ <https://biopax.github.io/Paxtools/>`_

.. [#pathway-commons] Cerami, E. G., Gross, B. E., Demir, E.,
   Rodchenkov, I., Babur, O., Anwar, N., Schultz, N., Bader, G. D.,
   and Sander, C. 2011. "Pathway Commons, a Web Resource for Biological
   Pathway Data."
   *Nucleic Acids Research* 39(Database issue): D685-D690.
   doi:10.1093/nar/gkq1039
   Available at: `https://pmc.ncbi.nlm.nih.gov/articles/PMC3013641/ <https://pmc.ncbi.nlm.nih.gov/articles/PMC3013641/>`_
