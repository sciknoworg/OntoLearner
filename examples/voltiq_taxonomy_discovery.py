import time

from ontolearner import GeoNames, train_test_split, evaluation_report
from ontolearner.learner.taxonomy_discovery import VoltIQTaxonomyLearner


# 1) Load & split
ontology = GeoNames()
ontology.load()
data = ontology.extract()

train_data, test_data = train_test_split(
    data, test_size=0.2, random_state=42
)

# 2) Configure the Volt-IQ taxonomy learner
voltiq_learner = VoltIQTaxonomyLearner(
    method="hybrid_cascade",
)

# 3) Train + predict
start_time = time.time()

voltiq_learner.fit(
    train_data,
    task="taxonomy-discovery",
    ontologizer=True,
)

predictions = voltiq_learner.predict(
    test_data,
    task="taxonomy-discovery",
    ontologizer=True,
)

elapsed_time = time.time() - start_time

# 4) Evaluate
ground_truth = voltiq_learner.tasks_ground_truth_former(
    data=test_data,
    task="taxonomy-discovery"
)

metrics = evaluation_report(
    y_true=ground_truth,
    y_pred=predictions,
    task="taxonomy-discovery"
)

print("Metrics:", metrics)
print("Elapsed time:", elapsed_time)
print("Predictions:", predictions)
