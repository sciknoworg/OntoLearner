from pathlib import Path
from dotenv import load_dotenv
from ontolearner.ontology import AgrO

load_dotenv(Path('.env'))

ontology = AgrO()

print("Starting push to Hugging Face...")

result = ontology.push_to_hub()

print("Push completed!")

print(result)
