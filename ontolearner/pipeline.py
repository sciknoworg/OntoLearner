
from pathlib import Path
from typing import Union

from . import logger

from .base import BaseOntology
from .data_structure import OntologyMetrics, OntologyData
from .tools import Analyzer
from .utils import io


class ProcessorPipeline:
    """
    Handles the complete ontology processing pipeline including:
    loading, extraction, analysis, and saving of results.
    """

    def __init__(self, datasets_dir: Path, analyzer_class: type[Analyzer] = Analyzer):
        self.datasets_dir = datasets_dir
        self.analyzer_class = analyzer_class

    def process_ontology(self, ontology: BaseOntology, ontology_path: Union[str, Path], ontology_identifier: str) -> OntologyMetrics:
        """
        Process a single ontology through the complete pipeline.

        :arg:
            ontology: The ontology instance to process
            ontology_path: Path to the ontology file
            ontology_identifier: Ontology identifier name for the ontology

        :return: OntologyMetrics: Computed metrics for the ontology
        """
        try:
            logger.info(f"Processing {ontology_identifier} ontology...")

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
            self.save_datasets(data, ontology_identifier)

            logger.info(f"Successfully processed {ontology_identifier} ontology")
            return metrics

        except Exception as e:
            logger.error(f"Error processing {ontology_identifier} ontology: {e}")
            raise

    def save_datasets(self, data: OntologyData, ontology_identifier: str) -> None:
        """Save extracted datasets to files"""
        for dataset_type in ['term_typings', 'type_taxonomies', 'type_non_taxonomic_relations']:
            save_path = self.datasets_dir / f"{ontology_identifier}_{dataset_type}_dataset.json"

            io.save_json(data.model_dump()[dataset_type], save_path)
