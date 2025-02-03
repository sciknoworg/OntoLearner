
import logging
from pathlib import Path

from ontolearner import ProcessorPipeline
from ontolearner.data_structure import OntologyMetrics
from ontolearner.ontology import * # NOQA

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    try:
        # Define paths
        DATA_DIR = Path("data")
        ONTOLOGY_DIR = DATA_DIR / "ontologies"
        DATASET_DIR = DATA_DIR / "datasets"

        # Initialize processor
        processor = ProcessorPipeline(datasets_dir=DATASET_DIR)

        # Define ontologies to process
        ontologies = [
            # # ---> 1. 1000 +- lines done
            # (ConferenceOntology(), "conference-ontology.owl", "conference"),
            # # ---> 2. 2000 +- lines
            # (IconOntology(), "icon-ontology.owl", "icon"),
            # # ---> 3. 7000 +- lines
            # (LifeOntology(), "life-ontology.owl", "life"),
            # # ---> 4. 9000 +- lines
            # (DBPediaOntology(), "dbpedia-ontology.owl", "dbpedia"),
            # # ---> 5. 10000 +- lines
            # (EmotionOntology(), "mfoem-ontology.owl", "emotion"),
            # # ---> 6. 80000 +- lines
            # (PlantOntology(), "plant-ontology.owl", "plant"),
            # # ---> 7. 150000 +- lines
            # (SWEETOntology(), "sweet-ontology.owl", "sweet"),
            # # -> 8. 210000 +- lines
            # (HumanDiseaseOntology(), "human-disease-ontology.owl", "disease"),
            # # -> 10. 500000 +- lines
            (CSO(), "cs-ontology.owl", "cso"), # NOQA
            # # -> 9. big +- lines
            # (FoodOn(), "foodon.owl", "food"),
        ]

        # Process each ontology
        for ontology, filename, identifier in ontologies:
            ontology_path = ONTOLOGY_DIR / filename

            metrics: OntologyMetrics = processor.process_ontology(
                ontology=ontology,
                ontology_path=ontology_path,
                ontology_identifier=identifier
            )

            # Log metrics
            if metrics:
                logger.info(f"\n{'=' * 20} {identifier.upper()} Metrics {'=' * 20}")
                logger.info("Dataset Metrics:")
                logger.info(f"Number of term types: {metrics.dataset.num_term_types}")
                logger.info(f"Number of taxonomic relations: {metrics.dataset.num_taxonomic_relations}")
                logger.info(f"Number of non-taxonomic relations: {metrics.dataset.num_non_taxonomic_relations}")
                logger.info(f"Average terms per type: {metrics.dataset.avg_terms:.2f}")

                logger.info("\nTopology Metrics:")
                logger.info(f"Total nodes: {metrics.topology.total_nodes}")
                logger.info(f"Total edges: {metrics.topology.total_edges}")
                logger.info(f"Graph density: {metrics.topology.density:.4f}")
                # logger.info(f"Average degree: {metrics.topology.avg_degree:.2f}")
                # logger.info(f"Maximum depth: {metrics.topology.max_depth}")
                logger.info(f"Number of root nodes: {metrics.topology.num_root_nodes}")
                logger.info(f"Number of leaf nodes: {metrics.topology.num_leaf_nodes}")
                logger.info("=" * 60 + "\n")

    except Exception as e:
        logger.error(f"Main execution failed: {e}")
        raise


if __name__ == "__main__":
    main()
