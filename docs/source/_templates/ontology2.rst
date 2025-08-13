{{ ontology_name }}
==============================================================================

Overview
----------
{{ description }}

.. sidebar::

    .. list-table::
       :header-rows: 0

       * - **Domain**
         - {{ domain }}
       * - **Category**
         - {{ category }}
       * - **Current Version**
         - {{ version }}
       * - **Last Updated**
         - {{ last_updated }}
       * - **Creator**
         - {{ creator }}
       * - **License**
         - {{ license }}
       * - **Format**
         - {{ format }}
       * - **Download**
         - `Download {{ ontology_name }} <{{ download_url }}>`_

Metrics & Statistics

.. tab:: Graph Metrics

    .. list-table::
        :widths: 50 50
        :header-rows: 0

        * - **Total Nodes**
          - {{ total_nodes }}
        * - **Total Edges**
          - {{ total_edges }}
        * - **Root Nodes**
          - {{ root_nodes }}
        * - **Leaf Nodes**
          - {{ leaf_nodes }}
    ::


.. tab:: Knowledge Coverage

    .. list-table::
        :widths: 50 50
        :header-rows: 0

        * - **Classes**
          - {{ num_classes }}
        * - **Individuals**
		  - {{ num_individuals }}
		* - **Properties**
          - {{ num_properties }}

    ::

.. tab:: Hierarchical Metrics

	.. list-table::
		:widths: 50 50
		:header-rows: 0

        * - **Maximum Depth**
          - {{ max_depth }}
        * - **Minimum Depth**
          - {{ min_depth }}
        * - **Average Depth**
          - {{ avg_depth }}
        * - **Depth Variance**
          - {{ depth_variance }}
    ::


.. tab:: Breadth Metrics

	.. list-table::
	    :widths: 50 50
	    :header-rows: 0

	    * - **Maximum Breadth**
	      - {{ max_breadth }}
	    * - **Minimum Breadth**
	      - {{ min_breadth }}
	    * - **Average Breadth**
	      - {{ avg_breadth }}
	    * - **Breadth Variance**
	      - {{ breadth_variance }}
	::

.. tab:: Benchmark Dataset Statistics

	.. list-table::
		:widths: 50 50
		:header-rows: 0

		* - **Term Types**
		  - {{ num_term_types }}
	    * - **Taxonomic Relations**
	      - {{ num_taxonomic_relations }}
	    * - **Non-taxonomic Relations**
	      - {{ num_non_taxonomic_relations }}
	    * - **Average Terms per Type**
	      - {{ avg_terms_per_type }}
	::

Usage Example
-------------

.. code-block:: python

    from ontolearner.ontology import {{ class_name }}

    ontology = {{ class_name }}()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
