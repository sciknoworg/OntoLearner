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
