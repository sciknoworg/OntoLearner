# pip install langchain
import time
from pathlib import Path
import pandas as pd
from dotenv import find_dotenv, load_dotenv
import logging
import shutil
import json
import os
from huggingface_hub import HfApi, Repository, login
from huggingface_hub.errors import RepositoryNotFoundError

from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

from ontolearner.data_structure import OntologyMetrics, TopologyMetrics, DatasetMetrics
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
    "arts_&_humanities": "Ontologies that describe music, iconography, cultural artifacts, and humanistic content.",
    "biology_&_life_sciences": "Ontologies about biological entities, systems, organisms, and molecular biology.",
    "chemistry": "Ontologies describing chemical entities, reactions, methods, and computational chemistry models.",
    "ecology_&_environment": "Ontologies about ecological systems, environments, biomes, and sustainability science.",
    "education": "Ontologies describing learning content, educational programs, competencies, and teaching resources.",
    "events": "Ontologies for representing events, time, schedules, and calendar-based occurrences.",
    "finance": "Ontologies describing economic indicators, e-commerce, trade, and financial instruments.",
    "food_&_beverage": "Ontologies related to food, beverages, ingredients, and culinary products.",
    "general_knowledge": "Broad-scope ontologies and upper vocabularies used across disciplines for general-purpose semantic modeling.",
    "geography": "Ontologies for modeling spatial and geopolitical entities, locations, and place names.",
    "industry": "Ontologies describing industrial processes, smart buildings, manufacturing systems, and equipment.",
    "law": "Ontologies dealing with legal processes, regulations, and rights (e.g., copyright).",
    "library_&_cultural_heritage": "Ontologies used in cataloging, archiving, and authority control of cultural and scholarly resources.",
    "materials_science_&_engineering": "Ontologies related to materials, their structure, properties, processing, and engineering applications.",
    "medicine": "Ontologies covering clinical knowledge, diseases, drugs, treatments, and biomedical data.",
    "news_&_media": "Ontologies that model journalism, broadcasting, creative works, and media metadata.",
    "scholarly_knowledge": "Ontologies modeling the structure, process, and administration of scholarly research, publications, and infrastructure.",
    "social_sciences": "Ontologies for modeling societal structures, behavior, identity, and social interaction.",
    "units_and_measurements": "Ontologies defining scientific units, quantities, dimensions, and observational models.",
    "upper_ontology": "Foundational ontologies that provide abstract concepts like objects, processes, and relations.",
    "web_&_internet": "Ontologies that model web semantics, linked data, APIs, and online communication standards.",
}

SYSTEM_PROMPT = """
As an ontology domain expert, enhance this domain definition with precision and academic clarity.

Domain: {domain}
Current definition: {domain_definition}

The OntoLearner library includes these ontologies in this domain (for context only):
{ontologies}

Create a concise, enhanced domain definition (2-3 sentences) that:
- Accurately describes the domain's scope and technical focus
- Highlights its significance in knowledge representation
- Avoids any reference to specific ontologies in the definition

Enhanced definition:
"""
gpt_4o_llm = ChatOpenAI(
    api_key = os.environ['OPENAI_API_KEY'],
    model = "gpt-4o",
    temperature = 0,
)
prompt = PromptTemplate(input_variables=["domain", "domain_definition", "ontologies"], template=SYSTEM_PROMPT)
chain = prompt | gpt_4o_llm | StrOutputParser()


def improve_domain_definition(domain: str, domain_definition: str, ontologies: List[BaseOntology]) -> str:
    """Improve the domain definition using GPT-4o"""
    try:
        result = chain.invoke(
            {
                "domain": domain,
                "domain_definition": domain_definition,
                "ontologies": "\n".join([f"- {ontology.ontology_full_name}" for ontology in ontologies])
            }
        )
        return result
    except Exception as e:
        logger.error(f"Failed to improve domain definition: {str(e)}", exc_info=True)
        return domain_definition


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
        logger.info(f"Copied ontology file: {source_file}")
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


def create_domain_readme(domain: str,
                         domain_definition: str,
                         ontologies: List[BaseOntology],
                         metrics: Dict[str, OntologyMetrics]) -> str:
    """Generate a README file for a domain with a table of ontologies and their metrics."""
    domain_title = domain.replace('_', ' ').title()
    readme = f"""
---
license: mit
language:
- en
tags:
- OntoLearner
- ontology-learning
- {domain}
pretty_name: Agricultural
---
<div>
  <img  src="https://raw.githubusercontent.com/sciknoworg/OntoLearner/main/images/logo.png"  alt="OntoLearner"
    style="display: block; margin: 0 auto; width: 500px; height: auto;">
  <h1 style="text-align: center; margin-top: 1em;">{domain_title} Domain Ontologies</h1>
</div>

## Overview
{domain_definition}

## Ontologies
| Ontology ID | Full Name | Classes | Properties | Last Updated |
|-------------|-----------|---------|------------|--------------|
"""

    # Add a row for each ontology
    for ontology in ontologies:
        metrics_data = metrics.get(ontology.ontology_id)
        if metrics_data:
            num_classes = metrics_data.topology.num_classes
            num_properties = metrics_data.topology.num_properties
        else:
            num_classes = "N/A"
            num_properties = "N/A"

        readme += f"| {ontology.ontology_id} | {ontology.ontology_full_name} | {num_classes} | {num_properties} | {ontology.last_updated}|\n"

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


def push_domain_to_huggingface(domain: str, domain_definition: str,
                               ontologies: List[BaseOntology],
                               metrics: Dict[str, OntologyMetrics]) -> Tuple[bool, str]:
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
        readme_content = create_domain_readme(domain, domain_definition, ontologies, metrics)
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
        ontologies: list[BaseOntology] = [
            # # Agricultural Ontologies
            # FoodOn(),
            # AGROVOC(),
            # PO(),
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
            # # Livestock Ontologies
            # ATOL(),
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
        metrics = load_metrics_from_excel(METRICS_FILE)

        # Push each domain as a separate repository
        successes = 0
        failures = 0

        for domain, domain_ontologies in domain_groups.items():
            logger.info(f"Processing {domain} domain with {len(domain_ontologies)} ontologies")

            extended_definition = improve_domain_definition(domain, DOMAINS_DEFINITIONS[domain], domain_ontologies)

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
