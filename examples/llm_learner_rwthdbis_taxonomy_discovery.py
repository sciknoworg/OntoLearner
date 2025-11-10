# Import core modules from the OntoLearner library
from ontolearner import LearnerPipeline, train_test_split, ChordOntology
from ontolearner.learner.taxonomy_discovery.rwthdbis import RWTHDBISSFTLearner

# Load the Chord ontology, which exposes hierarchical (parent, child) relations for taxonomy discovery
ontology = ChordOntology()
ontology.load()  # Read entities, type system, and taxonomic edges into memory

# Extract typed taxonomic edges and split into train/test while preserving the structured shape
train_data, test_data = train_test_split(
    ontology.extract(), test_size=0.2, random_state=42
)

# Initialize a supervised taxonomy classifier (encoder-based fine-tuning)
# Negative sampling controls the number of non-edge examples; bidirectional templates create both (p→c) and (c→p) views
# Context features are optional and can be enabled with with_context=True and a JSON path of type descriptions
learner = RWTHDBISSFTLearner(
    model_name="microsoft/deberta-v3-small",
    output_dir="./results/",
    device="cpu",
    num_train_epochs=1,
    per_device_train_batch_size=8,
    gradient_accumulation_steps=4,
    learning_rate=2e-5,
    max_length=256,
    seed=42,
    negative_ratio=5,
    bidirectional_templates=True,
    context_json_path=None,
    ontology_name=ontology.ontology_full_name,
)

# Build the pipeline
pipeline = LearnerPipeline(
    llm=learner,
    llm_id=learner.model_name,
    ontologizer_data=False,
)

# # Run the full learning pipeline on the taxonomy-discovery task
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    task="taxonomy-discovery",
    evaluate=True,
    ontologizer_data=False,
)

# Display the evaluation results
print(
    "Metrics:", outputs["metrics"]
)  # Shows {'precision': ..., 'recall': ..., 'f1_score': ...}

# Display total elapsed time for training + prediction + evaluation
print("Elapsed time:", outputs["elapsed_time"])

# Print all returned outputs (include predictions)
print(outputs)
