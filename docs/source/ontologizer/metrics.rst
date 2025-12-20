Metrics
=================

.. sidebar:: Metric Space:

	There are a dedicated Hugging Face space for `OntoLearner Benchmark Metrics  <https://huggingface.co/spaces/SciKnowOrg/OntoLearner-Benchmark-Metrics>`_ with analysis and live plots.

The ``Analyzer`` class in OntoLearner provides a unified interface for computing **ontology metrics**, which can be divided into two main categories: **Topology Metrics** (capture the structural characteristics of the ontology graph) and **Dataset Metrics** (assess the quality and distribution of the extracted learning datasets). Additionally, a **complexity score** can be derived from these metrics to summarize the overall ontology richness and complexity.

Topology Metrics
----------------
Topology metrics describe the structure and organization of an ontology. The ``Analyzer`` computes the following key metrics:

- **Total nodes** (``total_nodes``): Total number of nodes in the ontology graph.
- **Total edges** (``total_edges``): Total number of edges representing relations between nodes.
- **Root nodes** (``num_root_nodes``): Nodes with no incoming edges, representing top-level concepts.
- **Leaf nodes** (``num_leaf_nodes``): Nodes with no outgoing edges, representing bottom-level concepts.
- **Classes** (``num_classes``): Number of distinct ontology classes.
- **Properties** (``num_properties``): Number of distinct properties (object or datatype properties).
- **Individuals** (``num_individuals``): Number of instances associated with classes.
- **Depth metrics**:

  - ``max_depth``: Maximum hierarchical depth in the ontology.
  - ``min_depth``: Minimum hierarchical depth.
  - ``avg_depth``: Average hierarchical depth across all nodes.
  - ``depth_variance``: Variance of depth distribution.

- **Breadth metrics**:

  - ``max_breadth``: Maximum number of nodes at any single hierarchy level.
  - ``min_breadth``: Minimum number of nodes at any hierarchy level.
  - ``avg_breadth``: Average number of nodes per hierarchy level.
  - ``breadth_variance``: Variance of breadth distribution.

Dataset Metrics
---------------

Dataset metrics evaluate the characteristics of machine-learning datasets extracted from the ontology. These metrics include:

- **Number of term-type mappings** (``num_term_types``): Number of terms associated with types.
- **Number of taxonomic (is-a) relations** (``num_taxonomic_relations``): Count of hierarchical relations.
- **Number of non-taxonomic relations** (``num_non_taxonomic_relations``): Count of semantic associations not in the hierarchy.
- **Average terms per type** (``avg_terms``): Measures dataset balance across classes.


Complexity Score
----------------

The **complexity score** combines topology and dataset metrics into a single normalized score in ``[0, 1]``. First, metrics are **log-normalized** and weighted by category:

.. list-table::
   :header-rows: 1
   :widths: 25 50 25

   * - Metric Category
     - Example Metrics
     - Weight
   * - Graph structure
     - ``total_nodes``, ``total_edges``, ``num_root_nodes``, ``num_leaf_nodes``
     - 0.3
   * - Knowledge coverage
     - ``num_classes``, ``num_properties``, ``num_individuals``
     - 0.25
   * - Hierarchy
     - ``max_depth``, ``min_depth``, ``avg_depth``, ``depth_variance``
     - 0.10
   * - Breadth
     - ``max_breadth``, ``min_breadth``, ``avg_breadth``, ``breadth_variance``
     - 0.20
   * - Dataset (LLMs4OL)
     - ``num_term_types``, ``num_taxonomic_relations``, ``num_non_taxonomic_relations``, ``avg_terms``
     - 0.15


Next, the weighted sum of metrics is passed through a **logistic function** to normalize the final complexity score.


Example Usage
-------------

Here is a simple example demonstrating how to compute metrics and complexity for an ontology:

.. code-block:: python

    from ontolearner.tools import Analyzer
    from ontolearner.ontology import Wine

    # Step 1 — Load ontology
    ontology = Wine()
    ontology.build_graph()

    # Step 2 — Create the analyzer
    analyzer = Analyzer()

    # Step 3 — Compute topology and dataset metrics
    topology_metrics = analyzer.compute_topology_metrics(ontology)
    dataset_metrics = analyzer.compute_dataset_metrics(ontology)

    # Step 4 — Compute overall complexity score
    complexity_score = analyzer.compute_complexity_score(
	    topology_metrics=topology_metrics,
	    dataset_metrics=dataset_metrics
	    )
    # Step 5 — Display results
    print("Topology Metrics:", topology_metrics)
    print("Dataset Metrics:", dataset_metrics)
    print("Ontology Complexity Score:", complexity_score)


This workflow allows ontology engineers and researchers to **quantify structural quality, dataset richness, and overall complexity**, providing actionable insights for ontology evaluation, benchmarking, and improvement.
