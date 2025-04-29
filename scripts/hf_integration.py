import logging
from pathlib import Path
from typing import Union
import shutil
import json
from huggingface_hub import HfApi, Repository, login
from huggingface_hub.errors import RepositoryNotFoundError

from ontolearner.ontology import *  # noqa
from ontolearner.base import BaseOntology

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Local directories
DATA_DIR = Path("../data")
DOCS_DIR = Path("../docs")
ONTOLOGY_DIR = DATA_DIR / "ontologies"
DATASET_DIR = DATA_DIR / "datasets"

# Hugging Face
TMP_DIR = Path("./tmp")
HF_TOKEN = "hf_token"


def create_readme(ontology: BaseOntology) -> str:
    """
    Generate a README file with ontology information and metrics.
    """
    doc_string = ontology.__doc__.strip() if ontology.__doc__ else "No description available"

    readme = f"""# {ontology.ontology_full_name} Ontology Dataset

## Description
{doc_string}

## Metadata
- **Ontology ID:** {ontology.ontology_id}
- **Domain:** {ontology.domain}
- **Category:** {ontology.category}
- **Version:** {ontology.version}
- **Last Updated:** {ontology.last_updated}
- **Creator:** {ontology.creator}
- **License:** {ontology.license}
- **Format:** {ontology.format}
- **Download URL:** {ontology.download_url}

## Dataset Files
This repository contains the following files:
1. `{ontology.ontology_id.lower()}.{ontology.format.lower()}` - The original ontology file
2. `term_typings.json` - Dataset of term to type mappings
3. `taxonomies.json` - Dataset of taxonomic relations
4. `non_taxonomic_relations.json` - Dataset of non-taxonomic relations

## Usage
These datasets will be used for ontology learning.
"""
    return readme


def push_to_huggingface(ontology: BaseOntology, ontology_path: Union[str, Path], dataset_dir: Path) \
        -> tuple[bool, str]:
    """Returns (success_status, repo_name)"""
    api = HfApi()
    login(token=HF_TOKEN)

    repo_name = f"ontology-{ontology.ontology_id.lower().replace(' ', '-')}"
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

        # --- File Validation ---
        required_files = [
            ontology_path,
            dataset_dir / f"{ontology.domain.lower().replace(' ', '_')}" /
                f"{ontology.ontology_id.lower().replace(' ', '_')}" / "term_typings.json",
        ]
        if not all(f.exists() for f in required_files):
            logger.error(f"Missing files for {ontology.ontology_id}")
            return False, repo_name

        # --- Copy Files ---
        # README
        readme_content = create_readme(ontology)  # Your existing function
        (local_dir / "README.md").write_text(readme_content)

        # Ontology file
        ontology_filename = f"{ontology.ontology_id}.{ontology.format}"
        shutil.copy2(ontology_path, local_dir / ontology_filename)

        # Datasets
        domain_dir = dataset_dir / f"{ontology.domain.lower().replace(' ', '_')}"
        ontology_dataset_dir = domain_dir / f"{ontology.ontology_id.lower().replace(' ', '_')}"
        for f in ontology_dataset_dir.glob("*.json"):
            shutil.copy2(f, local_dir)

        # Create dataset card (metadata.json)
        metadata = {
            "name": f"Ontology: {ontology.ontology_full_name}",
            "description": ontology.__doc__.strip() if ontology.__doc__ else f"Dataset for {ontology.ontology_full_name} ontology",
            "license": ontology.license if ontology.license else "unknown",
            "tags": [
                "ontology",
                ontology.domain.lower().replace("&", "and").replace(" ", "-"),
                "knowledge-graph"
            ]
        }
        with open(local_dir / "dataset_infos.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)

        # --- Push ---
        repo.git_add(auto_lfs_track=True)
        repo.git_commit("Update datasets and ontology")
        repo.git_push()
        logger.info(f"Pushed to https://huggingface.co/datasets/{repo_name}")
        return True, repo_name

    except Exception as e:
        logger.error(f"Failed to process {ontology.ontology_id}: {str(e)}", exc_info=True)
        return False, repo_name
    finally:
        if local_dir.exists():
            shutil.rmtree(local_dir)


def main():
    try:
        ontologies = [
            # Agricultural Ontologies
            # (FoodOn(), "agricultural/foodon.owl"),
            # (AGROVOC(), "agricultural/AGROVOC.rdf"),
            # (PO(), "agricultural/plant.owl"),
            #
            # # Arts and Humanities Ontologies
            # (ChordOntology(), "arts_&_humanities/chord.rdf"),
            # (ICON(), "arts_&_humanities/icon.owl"),
            # (MusicOntology(), "arts_&_humanities/music.rdf"),
            # # Add all other ontologies here...
            #
            # # Large ontologies
            # (BattINFO(), "materials_science_&_engineering/battinfo.ttl"),
            # (PRIMA(), "materials_science_&_engineering/prima.ttl"),
            # (NCIt(), "medicine/ncit.owl"),
            # (PRotein(), "medicine/protein.rdf"),
        ]

        successes = 0
        failures = 0

        for ontology, filename in ontologies:
            ontology_path = ONTOLOGY_DIR / filename

            if not ontology_path.exists():
                logger.warning(f"Ontology file not found: {ontology_path}. Skipping.")
                continue

            success, _ = push_to_huggingface(
                ontology=ontology,
                ontology_path=ontology_path,
                dataset_dir=DATASET_DIR
            )

            if success:
                successes += 1
            else:
                failures += 1

        logger.info(f"Completed processing all ontologies. Successes: {successes}, Failures: {failures}")
    except Exception as e:
        logger.error(f"Main execution failed: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
