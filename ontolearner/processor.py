from pathlib import Path
from typing import Union, Dict
import pandas as pd
from jinja2 import Template
import time

from .base import BaseOntology
from .data_structure import OntologyMetrics, OntologyData
from .tools import Analyzer
from .utils import io
from . import logger

class Processor:
    """
    Handles the complete ontology processing pipeline including:
    loading, extraction, analysis, and saving of results.
    """
    def __init__(self, datasets_dir: Path, templates_dir: Path, benchmark_dir: Path,  metrics_dir: Path, analyzer_class: type[Analyzer] = Analyzer):
        self.datasets_dir = datasets_dir
        self.templates_dir = templates_dir
        self.benchmark_dir = benchmark_dir
        self.metrics_dir = metrics_dir
        self.analyzer_class = analyzer_class
        self.all_metrics: Dict[str, dict] = {}
        self.doc_template_path = templates_dir / "ontology.rst"
        self.doc_template = Template(self.doc_template_path.read_text())

    def process_ontology(self, ontology: BaseOntology, ontology_path: Union[str, Path]) \
            -> OntologyMetrics:
        """Process a single ontology through the complete pipeline."""
        start_time = time.time()

        try:
            logger.info(f"Processing {ontology.ontology_id} ontology...")

            if not Path(ontology_path).exists():
                raise ValueError(f"Ontology file not found: {ontology_path}")

            ontology.load(str(ontology_path))
            # ontology.load()

            data: OntologyData = ontology.extract()
            ontology.build_graph()
            analyzer = self.analyzer_class()
            metrics: OntologyMetrics = analyzer(ontology)

            end_time = time.time()
            processing_time = end_time - start_time

            self.all_metrics[ontology.ontology_id] = {
                "metrics": metrics,
                "ontology_id": ontology.ontology_id,
                "ontology_full_name": ontology.ontology_full_name,
                "domain": ontology.domain,
                "processing_time": processing_time
            }

            self._save_datasets(data, ontology)

            self._generate_documentation(ontology, metrics)

            logger.info(f"Successfully processed {ontology.ontology_id} ontology")
            return metrics
        except Exception as e:
            logger.error(f"Error processing {ontology.ontology_id} ontology: {e}")
            raise

    def _save_datasets(self, data: OntologyData, ontology: BaseOntology) -> None:
        """Save extracted datasets to files"""
        for dataset_type in ['term_typings', 'type_taxonomies', 'type_non_taxonomic_relations']:
            domain_dir = self.datasets_dir / f"{ontology.domain.lower().replace(' ', '_')}"
            domain_dir.mkdir(parents=True, exist_ok=True)

            save_path = domain_dir / f"{ontology.ontology_id.lower().replace(' ', '_')}/{dataset_type}.json"
            io.save_json(data.model_dump()[dataset_type], save_path)

    def _generate_documentation(self, ontology: BaseOntology, metrics: OntologyMetrics):
        """Generate RST documentation from template"""
        context = {
            # Class metadata
            'ontology_name': ontology.ontology_full_name,
            'description': ontology.__doc__.strip() if ontology.__doc__ else "No description available",
            'domain': ontology.domain,
            'category': ontology.category,
            'version': ontology.version,
            'last_updated': ontology.last_updated,
            'creator': ontology.creator,
            'license': ontology.license,
            'format': ontology.format,
            'download_url': ontology.download_url,
            'class_name': ontology.__class__.__name__,

            # Graph metrics
            'total_nodes': metrics.topology.total_nodes,
            'total_edges': metrics.topology.total_edges,
            'root_nodes': metrics.topology.num_root_nodes,
            'leaf_nodes': metrics.topology.num_leaf_nodes,

            # Knowledge coverage
            'num_classes': metrics.topology.num_classes,
            'num_individuals': metrics.topology.num_individuals,
            'num_properties': metrics.topology.num_properties,

            # Hierarchical metrics
            'max_depth': metrics.topology.max_depth,
            'min_depth': metrics.topology.min_depth,
            'avg_depth': f"{metrics.topology.avg_depth:.2f}",
            'depth_variance': f"{metrics.topology.depth_variance:.2f}",

            # Breadth metrics
            'max_breadth': metrics.topology.max_breadth,
            'min_breadth': metrics.topology.min_breadth,
            'avg_breadth': f"{metrics.topology.avg_breadth:.2f}",
            'breadth_variance': f"{metrics.topology.breadth_variance:.2f}",

            # Dataset statistics
            'num_term_types': metrics.dataset.num_term_types,
            'num_taxonomic_relations': metrics.dataset.num_taxonomic_relations,
            'num_non_taxonomic_relations': metrics.dataset.num_non_taxonomic_relations,
            'avg_terms_per_type': f"{metrics.dataset.avg_terms:.2f}"
        }

        content = self.doc_template.render(context)
        domain_dir = self.benchmark_dir / f"{ontology.domain.lower().replace(' ', '_')}"
        domain_dir.mkdir(parents=True, exist_ok=True)
        doc_path = domain_dir / f"{ontology.ontology_id.lower()}.rst"
        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"Generated documentation at {doc_path}")

    def export_metrics_to_excel(self):
        """
        Export all collected metrics to an Excel file.
        If the Excel file already exists, read it, update with new metrics, and write it back.
        This preserves metrics for ontologies not processed in the current run.
        """
        if not self.all_metrics:
            logger.warning("No metrics to export. Process at least one ontology first.")
            return

        excel_path = self.metrics_dir / "metrics.xlsx"

        # Try to read existing Excel file if it exists
        existing_df = None
        if excel_path.exists():
            try:
                existing_df = pd.read_excel(excel_path)
                logger.info(f"Read existing metrics from {excel_path}")
            except Exception as e:
                logger.warning(f"Could not read existing metrics file: {e}. Creating a new file.")

        # Create DataFrame from current metrics
        current_rows = []
        for ontology_id, data in self.all_metrics.items():
            metrics = data["metrics"]
            row = {
                "Ontology ID": data["ontology_id"],
                "Ontology Full Name": data["ontology_full_name"],
                "Domain": data["domain"],
                "Ontology Name": metrics.name,
                "Processing Time (s)": data["processing_time"],
                **metrics.topology.dict(),
                **metrics.dataset.dict()
            }
            current_rows.append(row)

        current_df = pd.DataFrame(current_rows)

        # Merge existing and current metrics
        if existing_df is not None and not existing_df.empty:
            # Remove rows for ontologies that are in the current metrics (to be updated)
            current_ontology_ids = current_df["Ontology ID"].tolist()
            existing_df = existing_df[~existing_df["Ontology ID"].isin(current_ontology_ids)]

            # Concatenate existing (minus updated ones) with current
            final_df = pd.concat([existing_df, current_df], ignore_index=True)

            # Sort by Ontology ID for consistency
            final_df = final_df.sort_values("Ontology ID").reset_index(drop=True)

            logger.info(f"Updated metrics for {len(current_ontology_ids)} ontologies, preserved metrics for {len(existing_df)} ontologies")
        else:
            final_df = current_df
            logger.info(f"Created new metrics file with {len(current_rows)} ontologies")

        # Calculate total processing time
        total_processing_time = sum(data.get("processing_time", 0) for data in self.all_metrics.values())
        logger.info(f"Total processing time for all ontologies: {total_processing_time:.2f} seconds")

        if not final_df.empty:
            # Sort the DataFrame by processing time (descending) to see which ontologies took longest
            final_df = final_df.sort_values("Processing Time (s)", ascending=False).reset_index(drop=True)

        # Write to Excel
        final_df.to_excel(excel_path, index=False)
        logger.info(f"Exported metrics to Excel file: {excel_path}")
