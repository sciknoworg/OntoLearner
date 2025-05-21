{{ ontology_name }}
========================================================================================================================

Overview
--------
{{ description }}

:Domain: {{ domain }}
:Category: {{ category }}
:Current Version: {{ version }}
:Last Updated: {{ last_updated }}
:Creator: {{ creator }}
:License: {{ license }}
:Format: {{ format }}
:Download: `{{ ontology_name }} Homepage <{{ download_url }}>`_

Graph Metrics
-------------
    - **Total Nodes**: {{ total_nodes }}
    - **Total Edges**: {{ total_edges }}
    - **Root Nodes**: {{ root_nodes }}
    - **Leaf Nodes**: {{ leaf_nodes }}

Knowledge coverage
------------------
    - Classes: {{ num_classes }}
    - Individuals: {{ num_individuals }}
    - Properties: {{ num_properties }}

Hierarchical metrics
--------------------
    - **Maximum Depth**: {{ max_depth }}
    - **Minimum Depth**: {{ min_depth }}
    - **Average Depth**: {{ avg_depth }}
    - **Depth Variance**: {{ depth_variance }}

Breadth metrics
------------------
    - **Maximum Breadth**: {{ max_breadth }}
    - **Minimum Breadth**: {{ min_breadth }}
    - **Average Breadth**: {{ avg_breadth }}
    - **Breadth Variance**: {{ breadth_variance }}

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: {{ num_term_types }}
    - **Taxonomic Relations**: {{ num_taxonomic_relations }}
    - **Non-taxonomic Relations**: {{ num_non_taxonomic_relations }}
    - **Average Terms per Type**: {{ avg_terms_per_type }}

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import {{ class_name }}

    # Initialize and load ontology from local file
    ontology = {{ class_name }}()
    ontology.load("path/to/ontology.{{ format }}")

    # Or load from a Hugging Face repository
    ontology = {{ class_name }}()
    ontology.load()

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
