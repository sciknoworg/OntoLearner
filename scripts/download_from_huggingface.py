import logging
from ontolearner.ontology import Wine  # Example ontology

logging.basicConfig(level=logging.INFO)


def main():
    print("OntoLearner - Downloading Ontologies from Hugging Face")
    ontology = Wine()
    file_path = ontology.download_from_huggingface()
    ontology.load(file_path)
    print(f"Downloaded to: {file_path}")


if __name__ == "__main__":
    main()
