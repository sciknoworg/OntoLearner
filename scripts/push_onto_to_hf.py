from ontolearner.ontology import AgrO

ontology = AgrO()

# Push to Hugging Face
result = ontology.push_to_hub()
print(result)
