# Import core modules from the OntoLearner library
from ontolearner import LearnerPipeline, train_test_split, GO
from ontolearner.learner.term_typing.rwthdbis import RWTHDBISSFTLearner
import os
from datetime import datetime

# load the GO ontology.
# GO provides term-typing supervision where each term can be annotated with one or more types.
ontology = GO()
ontology.load()


# Split the labeled term-typing data into train and test sets
train_data, test_data = train_test_split(
    ontology.extract(), test_size=0.3, random_state=42
)

# # Create timestamp
# timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# # Create a directory for this run
# output_dir = f"data_splits_{timestamp}"
# os.makedirs(output_dir, exist_ok=True)

# # Define file paths with timestamp in filenames
# train_path = os.path.join(output_dir, f"train_data_{timestamp}.csv")
# test_path = os.path.join(output_dir, f"test_data_{timestamp}.csv")

# # Save to CSV (change to sep="\t" if you prefer TSV)
# # Convert OntologyData -> DataFrame
# train_df = pd.DataFrame(train_data.term_typings)
# test_df = pd.DataFrame(test_data.term_typings)

# # Save to CSV (or TSV)
# train_df.to_csv(train_path, index=False)
# test_df.to_csv(test_path, index=False)

# print(f"✅ Train/test splits saved with timestamp:")
# print(f"   📁 Directory: {output_dir}")
# print(f"   🧩 Train file: {train_path}")
# print(f"   🧩 Test file:  {test_path}")

# Configure a supervised encoder-based classifier for term typing.
# This fine-tunes DeBERTa v3 on (term → type) signals; increase epochs for stronger results.
learner = RWTHDBISSFTLearner(
    model_name="microsoft/deberta-v3-small",
    output_dir="./results/deberta-v3",
    device="cuda",
    num_train_epochs=30,
    per_device_train_batch_size=16,
    gradient_accumulation_steps=2,
    learning_rate=2e-5,
    max_length=64,
    seed=42,
)

# Build the pipeline and pass raw structured objects end-to-end.
pipeline = LearnerPipeline(
    llm=learner,
    llm_id=learner.model_name,
    ontologizer_data=False,
)

# Run the full learning pipeline on the term-typing task
outputs = pipeline(
    train_data=train_data,
    test_data=test_data,
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
