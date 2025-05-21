from ontolearner.ontology import Wine  # Example ontology
ontology = Wine()
file_path = ontology.from_huggingface()
# Or
# ontology.load()
