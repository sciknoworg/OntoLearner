from pathlib import Path
from typing import Union
from jinja2 import Template

from . import logger

from .base import BaseOntology
from .data_structure import OntologyMetrics, OntologyData
from .tools import Analyzer
from .utils import io


DOC_TEMPLATE = Template('''\
{{ ontology_name }}
==========================

Overview
--------
{{ description }}

:Domain: {{ domain }}
:Category: {{ category }}
:Current Version: {{ version }}
:Last Updated: {{ last_updated }}
:Creator: {{ creator }}
:License: {{ license }}
:Format: {{ format }}
:Download: `{{ ontology_name }} Homepage <{{ download_url }}>`_

Graph Metrics
-------------
    - **Total Nodes**: {{ total_nodes }}
    - **Total Edges**: {{ total_edges }}
    - **Root Nodes**: {{ root_nodes }}
    - **Leaf Nodes**: {{ leaf_nodes }}

Knowledge coverage
------------------
    - Classes: {{ num_classes }}
    - Individuals: {{ num_individuals }}
    - Properties: {{ num_properties }}

Hierarchical metrics
--------------------
    - **Maximum Depth**: {{ max_depth }}
    - **Minimum Depth**: {{ min_depth }}
    - **Average Depth**: {{ avg_depth }}
    - **Depth Variance**: {{ depth_variance }}

Breadth metrics
------------------
    - **Maximum Breadth**: {{ max_breadth }}
    - **Minimum Breadth**: {{ min_breadth }}
    - **Average Breadth**: {{ avg_breadth }}
    - **Breadth Variance**: {{ breadth_variance }}

Dataset Statistics
------------------
Generated Benchmarks:
    - **Term Types**: {{ num_term_types }}
    - **Taxonomic Relations**: {{ num_taxonomic_relations }}
    - **Non-taxonomic Relations**: {{ num_non_taxonomic_relations }}
    - **Average Terms per Type**: {{ avg_terms_per_type }}

Usage Example
-------------
.. code-block:: python

    from ontolearner.ontology import {{ class_name }}

    # Initialize and load ontology
    ontology = {{ class_name }}()
    ontology.load("path/to/ontology.owl")

    # Extract datasets
    data = ontology.extract()

    # Access specific relations
    term_types = data.term_typings
    taxonomic_relations = data.type_taxonomies
    non_taxonomic_relations = data.type_non_taxonomic_relations
''')


class ProcessorPipeline:
    """
    Handles the complete ontology processing pipeline including:
    loading, extraction, analysis, and saving of results.
    """
    def __init__(self, datasets_dir: Path, docs_dir: Path, analyzer_class: type[Analyzer] = Analyzer):
        self.datasets_dir = datasets_dir
        self.docs_dir = docs_dir
        self.analyzer_class = analyzer_class

    def process_ontology(self, ontology: BaseOntology, ontology_path: Union[str, Path], ontology_identifier: str) \
            -> OntologyMetrics:
        """Process a single ontology through the complete pipeline."""
        try:
            logger.info(f"Processing {ontology_identifier} ontology...")

            if not Path(ontology_path).exists():
                raise ValueError(f"Ontology file not found: {ontology_path}")

            ontology.load(str(ontology_path))

            data: OntologyData = ontology.extract()

            ontology.build_graph()

            analyzer = self.analyzer_class()

            metrics: OntologyMetrics = analyzer(ontology)

            self._save_datasets(data, ontology_identifier)

            self._generate_documentation(ontology, metrics)

            logger.info(f"Successfully processed {ontology_identifier} ontology")
            return metrics
        except Exception as e:
            logger.error(f"Error processing {ontology_identifier} ontology: {e}")
            raise

    def _save_datasets(self, data: OntologyData, ontology_identifier: str) -> None:
        """Save extracted datasets to files"""
        for dataset_type in ['term_typings', 'type_taxonomies', 'type_non_taxonomic_relations']:
            save_path = self.datasets_dir / f"{ontology_identifier}_{dataset_type}_dataset.json"
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

        # Render
        content = DOC_TEMPLATE.render(context)
        # Save
        domain_dir = self.docs_dir / f"{ontology.domain.lower().replace(' ', '_')}"
        domain_dir.mkdir(parents=True, exist_ok=True)
        doc_path = domain_dir / f"{ontology.ontology_id.lower()}.rst"
        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"Generated documentation at {doc_path}")
