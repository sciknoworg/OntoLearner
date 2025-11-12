# Import core modules from the OntoLearner library
from ontolearner import GO, train_test_split, LearnerPipeline
from ontolearner.learner.taxonomy_discovery.skhnlp import SKHNLPSequentialFTLearner

# Load ontology and split
# Load the GeoNames ontology for taxonomy discovery.
# GeoNames provides geographic parent-child relationships (is-a hierarchy).
ontology = GO()
ontology.load()
data = ontology.extract()

# Split the taxonomic relationships into train and test sets
train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)

# Configure the learner with user-defined training args + device
# Configure the supervised BERT SFT Learner for taxonomy discovery.
# This fine-tunes BERT-Large using Sequential Prompts on (Parent, Child) pairs.
bert_learner = SKHNLPSequentialFTLearner(
    model_name="bert-large-uncased",
    n_prompts=2,
    random_state=1403,
    device="cuda",  # Note: CPU training for BERT-Large is very slow.
    output_dir="./results/",
    num_train_epochs=1,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir="./logs/",
    logging_steps=50,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

# Build pipeline and run
# Build the pipeline, passing the BERT Learner.
pipeline = LearnerPipeline(
    llm=bert_learner,
    llm_id="bert-large-uncased",
    ontologizer_data=False,
)

# Run the full learning pipeline on the taxonomy-discovery task
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
    task="taxonomy-discovery",
    evaluate=True,
    ontologizer_data=False,
)

# Display the evaluation results
print("Metrics:", outputs.get("metrics"))

# Display total elapsed time for training + prediction + evaluation
print("Elapsed time:", outputs["elapsed_time"])

# Print all returned outputs (include predictions)
print(outputs)
