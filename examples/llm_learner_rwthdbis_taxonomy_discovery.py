# Import core modules from the OntoLearner library
from ontolearner import LearnerPipeline, train_test_split, ChordOntology
from ontolearner.data_structure import OntologyData, TypeTaxonomies
from pathlib import Path
from ontolearner.learner.taxonomy_discovery import RWTHDBISSFTLearner

# Load the Chord ontology, which exposes hierarchical (parent, child) relations for taxonomy discovery
ontology = ChordOntology()
ontology.load()  # Read entities, type system, and taxonomic edges into memory

# Extract typed taxonomic edges and split into train/test while preserving the structured shape
train_data, test_data = train_test_split(
    ontology.extract(), test_size=0.2, random_state=42
)

# Limit inputs to 10 taxonomy relations for faster runs
small_train_taxonomies = train_data.type_taxonomies.taxonomies[:10]
small_test_taxonomies = test_data.type_taxonomies.taxonomies[:10]
train_types = sorted(
    {rel.parent for rel in small_train_taxonomies}
    | {rel.child for rel in small_train_taxonomies}
)
test_types = sorted(
    {rel.parent for rel in small_test_taxonomies}
    | {rel.child for rel in small_test_taxonomies}
)
small_train_data = OntologyData(
    term_typings=train_data.term_typings[:10],
    type_taxonomies=TypeTaxonomies(types=train_types, taxonomies=small_train_taxonomies),
    type_non_taxonomic_relations=train_data.type_non_taxonomic_relations,
)
small_test_data = OntologyData(
    term_typings=test_data.term_typings[:10],
    type_taxonomies=TypeTaxonomies(types=test_types, taxonomies=small_test_taxonomies),
    type_non_taxonomic_relations=test_data.type_non_taxonomic_relations,
)

# Initialize a supervised taxonomy classifier (encoder-based fine-tuning)
# Negative sampling controls the number of non-edge examples; bidirectional templates create both (p→c) and (c→p) views
# Context features are optional and can be enabled with with_context=True and a JSON path of type descriptions
train_method_dict = {
    1: "DS-CL + without_context FT-TC",
    2: "with_context FT-TC",
}
train_method = 2
print(f"Train method: {train_method_dict[train_method]}")

output_dir = Path("./results")
output_dir.mkdir(parents=True, exist_ok=True)
learner = RWTHDBISSFTLearner(
    model_name="microsoft/deberta-v3-small",
    output_dir=str(output_dir),
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
    train_method=train_method,
    save_strategy="no",
)

# Build the pipeline
pipeline = LearnerPipeline(
    llm=learner,
    llm_id=learner.model_name,
    ontologizer_data=False,
)

# # Run the full learning pipeline on the taxonomy-discovery task
outputs = pipeline(
    train_data=small_train_data,
    test_data=small_test_data,
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
