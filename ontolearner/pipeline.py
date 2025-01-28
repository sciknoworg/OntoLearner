
from pathlib import Path
from typing import Union

from . import logger

from ontolearner.base.ontology import BaseOntology
from ontolearner.data_structure.metric import OntologyMetrics
from ontolearner.data_structure.data import OntologyData
from ontolearner.analyzer.analyzer import OntologyAnalyzer
from ontolearner.utils.io import save_json


class ProcessorPipeline:
    """
    Handles the complete ontology processing pipeline including:
    loading, extraction, analysis, and saving of results.
    """

    def __init__(self, datasets_dir: Path, analyzer_class: type[OntologyAnalyzer] = OntologyAnalyzer):
        self.datasets_dir = datasets_dir
        self.analyzer_class = analyzer_class

    def process_ontology(self, ontology: BaseOntology, ontology_path: Union[str, Path], name: str) -> OntologyMetrics:
        """
        Process a single ontology through the complete pipeline.

        :arg:
            ontology: The ontology instance to process
            ontology_path: Path to the ontology file
            name: Name identifier for the ontology

        :return: OntologyMetrics: Computed metrics for the ontology
        """
        try:
            logger.info(f"Processing {name} ontology...")

            # Ensure paths exist
            if not Path(ontology_path).exists():
                raise ValueError(f"Ontology file not found: {ontology_path}")

            # Step 1: Load the ontology
            ontology.load(str(ontology_path))

            # Step 2: Extract and validate data
            data: OntologyData = ontology.extract()

            # Step 3: Build graph structure
            ontology.build_graph()

            # Step 4: Analyze ontology structure
            analyzer = self.analyzer_class()

            metrics: OntologyMetrics = analyzer(ontology)

            # Step 5: Save datasets
            self.save_datasets(data, name)

            logger.info(f"Successfully processed {name} ontology")
            return metrics

        except Exception as e:
            logger.error(f"Error processing {name} ontology: {e}")
            raise

    def save_datasets(self, data: OntologyData, name: str) -> None:
        """Save extracted datasets to files"""
        for dataset_type in ['term_typings', 'type_taxonomies', 'type_non_taxonomic_relations']:
            save_path = self.datasets_dir / f"{name}_{dataset_type}_dataset.json"

            save_json(data.model_dump()[dataset_type], save_path)
