# Import the Wine example ontology class from OntoLearner's ontology module
from ontolearner.ontology import AgrO  # Example ontology

# Initialize an instance of the Wine ontology
ontology = AgrO()

# Load the ontology data from the Hugging Face Hub
# This is useful when the ontology is hosted remotely (e.g., in a pre-packaged dataset format)
ontology.from_huggingface()

# Alternatively, if the ontology is available locally, you can use:
# ontology.load()
# This will load the ontology from a local file path or huggingface

print(ontology)
# output will be look like:
# ontology_id: AgrO
# ontology_full_name: Agronomy Ontology (AgrO)
# domain: Agriculture
# category: Agronomy
# version: 1.0
# last_updated: 2022-11-02
# creator: The Crop Ontology Consortium
# license: Creative Commons 4.0
# format: RDF
# download_url: https://agroportal.lirmm.fr/ontologies/AGRO?p=summary
