
import time
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import logging
import shutil
import json
import os
from huggingface_hub import HfApi, Repository, login
from huggingface_hub.errors import RepositoryNotFoundError



from ontolearner import Processor
from ontolearner.ontology import *  # noqa
from ontolearner.base import BaseOntology

from typing import Dict, List, Tuple

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

DOMAINS_DEFINITIONS = {
    "agriculture": "Ontologies about farming systems, crops, food production, and agricultural vocabularies.",
    "arts_and_humanities": "Ontologies that describe music, iconography, cultural artifacts, and humanistic content.",
    "biology_and_life_sciences": "Ontologies about biological entities, systems, organisms, and molecular biology.",
    "chemistry": "Ontologies describing chemical entities, reactions, methods, and computational chemistry models.",
    "ecology_and_environment": "Ontologies about ecological systems, environments, biomes, and sustainability science.",
    "education": "Ontologies describing learning content, educational programs, competencies, and teaching resources.",
    "events": "Ontologies for representing events, time, schedules, and calendar-based occurrences.",
    "finance": "Ontologies describing economic indicators, e-commerce, trade, and financial instruments.",
    "food_and_beverage": "Ontologies related to food, beverages, ingredients, and culinary products.",
    "general_knowledge": "Broad-scope ontologies and upper vocabularies used across disciplines for general-purpose semantic modeling.",
    "geography": "Ontologies for modeling spatial and geopolitical entities, locations, and place names.",
    "industry": "Ontologies describing industrial processes, smart buildings, manufacturing systems, and equipment.",
    "law": "Ontologies dealing with legal processes, regulations, and rights (e.g., copyright).",
    "library_and_cultural_heritage": "Ontologies used in cataloging, archiving, and authority control of cultural and scholarly resources.",
    "materials_science_and_engineering": "Ontologies related to materials, their structure, properties, processing, and engineering applications.",
    "medicine": "Ontologies covering clinical knowledge, diseases, drugs, treatments, and biomedical data.",
    "news_and_media": "Ontologies that model journalism, broadcasting, creative works, and media metadata.",
    "scholarly_knowledge": "Ontologies modeling the structure, process, and administration of scholarly research, publications, and infrastructure.",
    "social_sciences": "Ontologies for modeling societal structures, behavior, identity, and social interaction.",
    "units_and_measurements": "Ontologies defining scientific units, quantities, dimensions, and observational models.",
    "upper_ontology": "Foundational ontologies that provide abstract concepts like objects, processes, and relations.",
    "web_and_internet": "Ontologies that model web semantics, linked data, APIs, and online communication standards.",
}


def copy_ontology_files(ontology: BaseOntology, domain_dir: Path, format: str):
    """
    Copy ontology file and documentation to the domain directory.
    """
    # Create ontology-specific directory within the domain directory
    ontology_dir = domain_dir / ontology.ontology_id.lower()
    ontology_dir.mkdir(parents=True, exist_ok=True)

    # Copy ontology file from source to domain directory
    source_file = ONTOLOGIES_DIR / ontology.domain.lower().replace(' ', '_') / f"{ontology.ontology_id.lower()}.{format}"
    if source_file.exists():
        shutil.copy2(source_file, ontology_dir / f"{ontology.ontology_id.lower()}.{format}")
    else:
        logger.warning(f"Ontology file not found at {source_file}. Skipping.")

    # Copy documentation file
    doc_file = BENCHMARK_DIR / ontology.domain.lower().replace(' ', '_') / f"{ontology.ontology_id.lower()}.rst"
    if doc_file.exists():
        shutil.copy2(doc_file, ontology_dir / f"{ontology.ontology_id.lower()}.rst")
        logger.info(f"Copied documentation file: {doc_file}")
    else:
        logger.warning(f"Documentation file not found at {doc_file}. Skipping.")

    # Copy dataset files
    dataset_path = DATASETS_DIR / ontology.domain.lower().replace(' ', '_') / ontology.ontology_id.lower()
    if dataset_path.is_dir():
        for file in dataset_path.glob("*.json"):
            shutil.copy2(file, ontology_dir)
            logger.info(f"Copied dataset file: {file}")
    else:
        logger.warning(f"Dataset path not found at {dataset_path}. Skipping.")


def push_domain_to_huggingface(domain: str, domain_definition: str,
                               ontologies: List[BaseOntology],
                               metrics: dict[str, dict]) -> Tuple[bool, str]:
    """
    Push a domain with all its ontologies to Hugging Face as a single repository
    """
    api = HfApi()
    login(token=huggingface_key)

    # Create repository name from domain
    repo_name = f"SciKnowOrg/ontolearner-{domain.lower()}"
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
        readme_content = Processor.create_domain_readme(domain, domain_definition, metrics)

        (local_dir / "README.md").write_text(readme_content)

        # Create dataset card (metadata.json)
        metadata = {
            "name": f"Ontology Domain: {domain.replace('_', ' ').title()}",
            "description": f"Dataset containing ontologies and processed data for the {domain.replace('_', ' ').title()} domain",
            "license": "mixed",
            "tags": [
                "ontology",
                domain.lower().replace(" ", "-"),
                "knowledge-graph"
            ],
            "ontologies": [ontology.ontology_id for ontology in ontologies]
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


def group_ontologies_by_domain(ontologies: List[BaseOntology]) -> Dict[str, List[BaseOntology]]:
    """Group ontologies by their domain."""
    domain_groups = {}

    for ontology in ontologies:
        domain = ontology.domain.lower().replace(' ', '_')
        if domain not in domain_groups:
            domain_groups[domain] = []
        domain_groups[domain].append(ontology)

    return domain_groups


def main():
    try:
        ontologies: list[BaseOntology] = [
            # # Agricultural Ontologies
            # AGROVOC(),
            # ATOL(),
            # PO(),
            # FoodOn(),
            #
            # # Arts and Humanities Ontologies
            # ChordOntology(),
            # ICON(),
            # MusicOntology(),
            # Nomisma(),
            # TimelineOntology(),
            #
            # # Biology & Life Sciences Ontologies
            # BioPAX(),
            # EFO(),
            # GO(),
            # LIFO(),
            # MarineTLO(),
            # MGED(),
            # MO(),
            # NPO(),
            # PATO(),
            #
            # # Chemistry Ontologies
            # AFO(),
            # ChEBI(),
            # CHEMINF(),
            # CHIRO(),
            # ChMO(),
            # FIX(),
            # MassSpectrometry(),
            # MOP(),
            # NMRCV(),
            # OntoKin(),
            # PROCO(),
            # PSIMOD(),
            # REX(),
            # RXNO(),
            # VIBSO(),
            #
            # # Ecology & Environment Ontologies
            # ENVO(),
            # OEO(),
            # SWEET(),
            #
            # # Education Ontologies
            # BIBFRAME(),
            # Common(),
            # DoCO(),
            #
            # # # Event Ontologies
            # ConferenceOntology(),
            # iCalendar(),
            # LODE(),
            #
            # # Finance Ontologies
            # GoodRelations(),
            #
            # # Food & Beverage Ontologies
            # Wine(),
            #
            # # General Knowledge Ontologies
            # CCO(),
            # DBpedia(),
            # DublinCore(),
            # EDAM(),
            # GIST(),
            # IAO(),
            # PROV(),
            # RO(),
            # SchemaOrg(),
            # UMBEL(),
            # YAGO(),
            #
            # # Geography Ontologies
            # GEO(),
            # GeoNames(),
            # GTS(),
            # Juso(),
            #
            # # Industry
            # AUTO(),
            # DBO(),
            # DOAP(),
            # IOF(),
            # PTO(),
            # TUBES(),
            #
            # # Law Ontologies
            # CopyrightOnto(),
            #
            # # Library & Cultural Heritage
            # GND(),
            #
            # # Materials Science & Engineering
            # AMOntology(),
            # ASMO(),
            # Atomistic(),
            # BattINFO(),
            # BMO(),
            # BVCO(),
            # CDCO(),
            # CHAMEO(),
            # CIFCore(),
            # CMSO(),
            # DISO(),
            # DSIM(),
            # EMMO(),
            # EMMOCrystallography(),
            # FSO(),
            # GPO(),
            # HPOnt(),
            # LDO(),
            # LPBFO(),
            # MAMBO(),
            # MAT(),
            # MaterialInformation(),
            # MatOnto(),
            # MatVoc(),
            # MatWerk(),
            # MDO(),
            # MDS(),
            # MechanicalTesting(),
            # MicroStructures(),
            # MMO(),
            # MOLBRINELL(),
            # MOLTENSILE(),
            # MSEO(),
            # MSLE(),
            # NanoMine(),
            # OIEManufacturing(),
            # OIEMaterials(),
            # OIEModels(),
            # OIESoftware(),
            # #(OntoCAPE(language='en', base_dir=str(ONTOLOGIES_DIR / "materials_science_&_engineering")), "materials_science_&_engineering/OntoCAPE/OntoCAPE.owl"),
            # ONTORULE(),
            # PeriodicTable(),
            # Photovoltaics(),
            # PLDO(),
            # PMDco(),
            # PODO(),
            # PRIMA(),
            # SSN(),
            # SystemCapabilities(),
            # VIMMP(),
            #
            # # Medicine Ontologies
            # BTO(),
            # DEB(),
            # DOID(),
            # ENM(),
            # MFOEM(),
            # NCIt(),
            # OBI(),
            # PRotein(),  # large
            #
            # # News & Media Ontologies
            # BBC(),
            # BBCBusiness(),
            # BBCCMS(),
            # BBCCoreConcepts(),
            # BBCCreativeWork(),
            # BBCFood(),
            # BBCPolitics(),
            # BBCProgrammes(),
            # BBCProvenance(),
            # BBCSport(),
            # BBCStoryline(),
            # BBCWildlife(),
            #
            # # Scholarly Knowledge Ontologies
            # AIISO(),
            # CiTO(),
            # CSO(),
            # DataCite(),
            # DCAT(),
            # DUO(),
            # EURIO(),
            # EXPO(),
            # FRAPO(),
            # FRBRoo(),
            # LexInfo(),
            # Metadata4Ing(),
            # NFDIcore(),
            # OBOE(),
            # OPMW(),
            # PPlan(),
            # PreMOn(),
            # SEPIO(),
            # SPDocument(),
            # SPWorkflow(),
            # SWO(),
            # TribAIn(),
            # VOAF(),
            # WiLD(),
            #
            # # Social Sciences
            # AS2(),
            # BIO(),
            # Contact(),
            # FOAF(),
            # SIOC(),
            #
            # # Units and Measurements
            # OM(),
            # OWLTime(),
            # QUDT(),
            # QUDV(),
            # UO(),
            #
            # # Upper Ontologies
            # BFO(),
            # DOLCE(),
            # FAIR(),
            # GFO(),
            # SIO(),
            # SUMO(),
            #
            # # Web Ontologies
            # Hydra(),
            # SAREF(),
        ]

        # Group ontologies by domain
        domain_groups = group_ontologies_by_domain(ontologies)

        # Load metrics for all ontologies
        metrics = Processor.load_metrics_from_excel(METRICS_FILE)

        # Push each domain as a separate repository
        successes = 0
        failures = 0

        for domain, domain_ontologies in domain_groups.items():
            logger.info(f"Processing {domain} domain with {len(domain_ontologies)} ontologies")

            extended_definition = Processor.improve_domain_definition(
                domain,
                DOMAINS_DEFINITIONS[domain],
                domain_ontologies
            )

            logger.info(f"Extended domain definition: {extended_definition}")

            success, _ = push_domain_to_huggingface(
                domain=domain,
                domain_definition=extended_definition,
                ontologies=domain_ontologies,
                metrics=metrics
            )

            if success:
                successes += 1
            else:
                failures += 1

            logger.info("Waiting 30 seconds before processing next domain...")
            time.sleep(30)

        logger.info(f"Completed processing all domains. Successes: {successes}, Failures: {failures}")
    except Exception as e:
        logger.error(f"Main execution failed: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    main()
