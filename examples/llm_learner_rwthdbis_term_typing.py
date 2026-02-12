# Import core modules from the OntoLearner library
from ontolearner import LearnerPipeline, train_test_split, AgrO
from ontolearner.data_structure import OntologyData
from pathlib import Path
from ontolearner.learner.term_typing import RWTHDBISSFTLearner

# load the AgrO ontology.
# AgrO provides term-typing supervision where each term can be annotated with one or more types.
ontology = AgrO()
ontology.load()
data = ontology.extract()

# Split the labeled term-typing data into train and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Limit inputs to 10 term-typing entries for faster runs
small_train_data = OntologyData(
    term_typings=train_data.term_typings[:10],
    type_taxonomies=train_data.type_taxonomies,
    type_non_taxonomic_relations=train_data.type_non_taxonomic_relations,
)
small_test_data = OntologyData(
    term_typings=test_data.term_typings[:10],
    type_taxonomies=test_data.type_taxonomies,
    type_non_taxonomic_relations=test_data.type_non_taxonomic_relations,
)

# Configure a supervised encoder-based classifier for term typing.
# This fine-tunes DeBERTa v3 on (term → type) signals; increase epochs for stronger results.
train_method_dict = {
    1: "DS-CL: Domain-specific Continual Learning",
    2: "FT-TC: Fine-tuning for Text Classification",
    3: "SKPT: Structured Knowledge Prompt Tuning",
}
train_method = 2
print(f"Train method: {train_method_dict[train_method]}")

output_dir = Path("./results/deberta-v3")
output_dir.mkdir(parents=True, exist_ok=True)
learner = RWTHDBISSFTLearner(
    model_name="microsoft/deberta-v3-small",
    output_dir=str(output_dir),
    device="cpu",
    num_train_epochs=1,
    per_device_train_batch_size=16,
    gradient_accumulation_steps=2,
    learning_rate=2e-5,
    max_length=64,
    seed=42,
    train_method=train_method,
    save_strategy="no",
)

# Build the pipeline and pass raw structured objects end-to-end.
pipeline = LearnerPipeline(
    llm=learner,
    llm_id=learner.model_name,
    ontologizer_data=False,
)

# Run the full learning pipeline on the term-typing task
outputs = pipeline(
    train_data=small_train_data,
    test_data=small_test_data,
    task="term-typing",
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
