from pathlib import Path
from typing import Dict, List, Tuple
import os
import pandas as pd
from dotenv import find_dotenv, load_dotenv
import logging
import shutil
import json
from huggingface_hub import HfApi, Repository, login
from huggingface_hub.errors import RepositoryNotFoundError

from ontolearner.data_structure import OntologyMetrics, TopologyMetrics, DatasetMetrics
from ontolearner.ontology import *  # noqa
from ontolearner.base import BaseOntology


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

_ = load_dotenv(find_dotenv())

huggingface_key = os.environ['HUGGINGFACE_ACCESS_TOKEN']

# Local directories
# Handle both cases: running from project root or from scripts directory
script_dir = Path(__file__).parent.absolute()
project_root = script_dir.parent

# Check if data directory exists at project root or one level up
if (project_root / "data").exists():
    DATA_DIR = project_root / "data"
    DOCS_DIR = project_root / "docs"
else:
    # Fallback to original paths (for running from scripts directory)
    DATA_DIR = Path("../data")
    DOCS_DIR = Path("../docs")

ONTOLOGIES_DIR = DATA_DIR / "ontologies"
DATASETS_DIR = DATA_DIR / "datasets"
BENCHMARK_DIR = DOCS_DIR / "source/benchmarking"
METRICS_FILE = DATA_DIR / "metrics" / "metrics.xlsx"

# Hugging Face
TMP_DIR = Path("./tmp")
ORGANIZATION = "SciKnowOrg/OntoLearner"


def copy_ontology_files(ontology: BaseOntology, domain_dir: Path, format: str):
    """
    Copy ontology file and documentation to the domain directory.
    """
    # Create ontology-specific directory within the domain directory
    ontology_dir = domain_dir / ontology.ontology_id.lower()
    ontology_dir.mkdir(parents=True, exist_ok=True)

    # Copy ontology file from source to domain directory
    source_file = ONTOLOGIES_DIR / ontology.domain.lower() / f"{ontology.ontology_id.lower()}.{format}"
    if source_file.exists():
        shutil.copy2(source_file, ontology_dir / f"{ontology.ontology_id.lower()}.{format}")
        logger.info(f"Copied ontology file: {source_file}")
    else:
        logger.warning(f"Ontology file not found at {source_file}. Skipping.")

    # Copy documentation file
    doc_file = BENCHMARK_DIR / ontology.domain.lower() / f"{ontology.ontology_id.lower()}.rst"
    if doc_file.exists():
        shutil.copy2(doc_file, ontology_dir / f"{ontology.ontology_id.lower()}.rst")
        logger.info(f"Copied documentation file: {doc_file}")
    else:
        logger.warning(f"Documentation file not found at {doc_file}. Skipping.")

    # Copy dataset files
    dataset_paths = [
        DATASETS_DIR / ontology.domain.lower() / ontology.ontology_id.lower() / "term_typings.json",
        DATASETS_DIR / ontology.domain.lower() / ontology.ontology_id.lower() / "type_taxonomies.json",
        DATASETS_DIR / ontology.domain.lower() / ontology.ontology_id.lower() / "type_non_taxonomic_relations.json"
    ]
    for path in dataset_paths:
        if path.exists():
            shutil.copy2(path, ontology_dir / path.name)
            logger.info(f"Copied dataset file: {path}")
        else:
            logger.warning(f"Dataset file not found at {path}. Skipping.")

    # dataset_path = DATASETS_DIR / ontology.domain.lower() / ontology.ontology_id.lower()
    # if dataset_path.is_dir():
    #     for file in dataset_path.glob("*.json"):
    #         shutil.copy2(file, ontology_dir)
    #         logger.info(f"Copied dataset file: {file}")
    # else:
    #     logger.warning(f"Dataset path not found at {dataset_path}. Skipping.")


def create_domain_readme(domain: str, ontologies: List[BaseOntology], metrics: Dict[str, OntologyMetrics]) -> str:
    """Generate a README file for a domain with a table of ontologies and their metrics."""
    # Convert domain name to proper title format
    domain_title = domain.replace('_', ' ').title()

    readme = f"""
# {domain_title} Ontologies Dataset

## Overview
This repository contains ontologies and their processed datasets for the {domain_title} domain.

## Ontologies
| Ontology ID | Full Name | Classes | Properties | Terms | Last Updated | License |
|-------------|-----------|---------|------------|-------|--------------|---------|
"""

    # Add a row for each ontology
    for ontology in ontologies:
        metrics_data = metrics.get(ontology.ontology_id)
        if metrics_data:
            num_classes = metrics_data.topology.num_classes
            num_properties = metrics_data.topology.num_properties
            num_terms = metrics_data.dataset.num_term_types
        else:
            num_classes = "N/A"
            num_properties = "N/A"
            num_terms = "N/A"

        readme += f"| {ontology.ontology_id} | {ontology.ontology_full_name} | {num_classes} | {num_properties} | {num_terms} | {ontology.last_updated} | {ontology.license} |\n"

    readme += """
## Dataset Files
Each ontology directory contains the following files:
1. `<ontology_id>.<format>` - The original ontology file
2. `term_typings.json` - Dataset of term to type mappings
3. `taxonomies.json` - Dataset of taxonomic relations
4. `non_taxonomic_relations.json` - Dataset of non-taxonomic relations
5. `<ontology_id>.rst` - Documentation describing the ontology

## Usage
These datasets are intended for ontology learning research and applications.
    """

    return readme


def push_domain_to_huggingface(domain: str, ontologies: List[BaseOntology],
                               metrics: Dict[str, OntologyMetrics]) -> Tuple[bool, str]:
    """
    Push a domain with all its ontologies to Hugging Face as a single repository
    """
    api = HfApi()
    login(token=huggingface_key)

    # Create repository name from domain
    repo_name = f"SciKnowOrg/ontology-domain-{domain.lower().replace(' ', '-').replace('&', 'and')}"
    local_dir = TMP_DIR / repo_name

    try:
        # Cleanup and prepare
        if local_dir.exists():
            shutil.rmtree(local_dir)
        local_dir.mkdir(parents=True)

        # Check/Create repo
        try:
            api.repo_info(repo_id=repo_name, repo_type="dataset")
            logger.info(f"Repository {repo_name} exists. Cloning...")
            repo = Repository(local_dir=local_dir, clone_from=repo_name, repo_type="dataset")
            repo.git_pull()
        except RepositoryNotFoundError:
            logger.info(f"Creating new repository {repo_name}")
            api.create_repo(repo_id=repo_name, repo_type="dataset", private=False)
            repo = Repository(local_dir=local_dir, clone_from=repo_name, repo_type="dataset")

        # Copy files for each ontology
        for ontology in ontologies:
            copy_ontology_files(
                ontology=ontology,
                domain_dir=local_dir,
                format=ontology.format.lower()
            )

        # Create domain README
        readme_content = create_domain_readme(domain, ontologies, metrics)
        (local_dir / "README.md").write_text(readme_content)

        # Create dataset card (metadata.json)
        metadata = {
            "name": f"Ontology Domain: {domain.replace('_', ' ').title()}",
            "description": f"Dataset containing ontologies and processed data for the {domain.replace('_', ' ').title()} domain",
            "license": "mixed",
            "tags": [
                "ontology",
                domain.lower().replace("&", "and").replace(" ", "-"),
                "knowledge-graph"
            ]
        }
        with open(local_dir / "dataset_infos.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        # Push
        repo.git_add(auto_lfs_track=True)
        repo.git_commit(f"Update {domain} domain with {len(ontologies)} ontologies")
        repo.git_push()
        logger.info(f"Pushed to https://huggingface.co/datasets/{repo_name}")
        return True, repo_name

    except Exception as e:
        logger.error(f"Failed to process {domain} domain: {str(e)}", exc_info=True)
        return False, repo_name
    finally:
        if local_dir.exists():
            shutil.rmtree(local_dir)


def get_ontology_class_by_id(ontology_id: str) -> type[BaseOntology]:
    """Returns the ontology class based on the ontology ID"""
    for cls in BaseOntology.__subclasses__():
        if cls.ontology_id == ontology_id:
            return cls
    raise ValueError(f"No ontology class found for ID: {ontology_id}")


def group_ontologies_by_domain(ontologies: List[Tuple[BaseOntology, str]]) -> Dict[str, List[BaseOntology]]:
    """Group ontologies by their domain."""
    domain_groups = {}

    for ontology, _ in ontologies:
        domain = ontology.domain.lower().replace(' ', '_')
        if domain not in domain_groups:
            domain_groups[domain] = []
        domain_groups[domain].append(ontology)

    return domain_groups


def load_metrics_from_excel(metrics_file: Path) -> Dict[str, OntologyMetrics]:
    """Load metrics for all ontologies from the Excel file generated by processor."""
    if not metrics_file.exists():
        logger.warning(f"Metrics file not found: {metrics_file}")
        return {}

    metrics = {}
    try:
        df = pd.read_excel(metrics_file)
        for _, row in df.iterrows():
            # Create topology metrics
            topology_metrics = TopologyMetrics(
                total_nodes=row.get("total_nodes", 0),
                total_edges=row.get("total_edges", 0),
                num_classes=row.get("num_classes", 0),
                num_properties=row.get("num_properties", 0),
                num_individuals=row.get("num_individuals", 0),
                max_depth=row.get("max_depth", 0),
                min_depth=row.get("min_depth", 0),
                avg_depth=row.get("avg_depth", 0),
                depth_variance=row.get("depth_variance", 0),
                max_breadth=row.get("max_breadth", 0),
                min_breadth=row.get("min_breadth", 0),
                avg_breadth=row.get("avg_breadth", 0),
                breadth_variance=row.get("breadth_variance", 0),
                num_root_nodes=row.get("num_root_nodes", 0),
                num_leaf_nodes=row.get("num_leaf_nodes", 0)
            )

            # Create dataset metrics
            dataset_metrics = DatasetMetrics(
                num_term_types=row.get("num_term_types", 0),
                num_taxonomic_relations=row.get("num_taxonomic_relations", 0),
                num_non_taxonomic_relations=row.get("num_non_taxonomic_relations", 0),
                avg_terms=row.get("avg_terms", 0)
            )

            # Create ontology metrics
            ontology_metrics = OntologyMetrics(
                name=row.get("Ontology Name", ""),
                topology=topology_metrics,
                dataset=dataset_metrics
            )

            # Add to metrics dictionary
            metrics[row.get("Ontology ID")] = ontology_metrics

        logger.info(f"Loaded metrics for {len(metrics)} ontologies from Excel file")
        return metrics
    except Exception as e:
        logger.error(f"Error loading metrics from Excel file: {e}")
        return {}


def main():
    try:
        ontologies: list[tuple[BaseOntology, str]] = [
            # Agricultural Ontologies
            # (FoodOn(), "owl"),
            # (AGROVOC(), "rdf"),
            # (PO(), "owl"),

            # # Arts and Humanities Ontologies
            # (ChordOntology(), "rdf"),
            # (ICON(), "icon.owl"),
            # (MusicOntology(), "music.rdf"),
            # (Nomisma(), "nomisma.ttl"),
            # (TimelineOntology(), "timeline.rdf"),
        ]

        # Group ontologies by domain
        domain_groups = group_ontologies_by_domain(ontologies)

        # Load metrics for all ontologies
        metrics = load_metrics_from_excel(METRICS_FILE)

        # Push each domain as a separate repository
        successes = 0
        failures = 0

        for domain, domain_ontologies in domain_groups.items():
            success, _ = push_domain_to_huggingface(
                domain=domain,
                ontologies=domain_ontologies,
                metrics=metrics
            )

            if success:
                successes += 1
            else:
                failures += 1

        logger.info(f"Completed processing all domains. Successes: {successes}, Failures: {failures}")
    except Exception as e:
        logger.error(f"Main execution failed: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
