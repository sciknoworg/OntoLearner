import logging
from pathlib import Path

from ontolearner import Processor
from ontolearner.data_structure import OntologyMetrics
from ontolearner.ontology import *  # noqa


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    try:
        DATA_DIR = Path("../data")
        DOCS_DIR = Path("../docs")
        ONTOLOGIES_DIR = DATA_DIR / "ontologies"
        DATASET_DIR = DATA_DIR / "datasets"
        TEMPLATES_DIR = DOCS_DIR / "source/_templates"
        BENCHMARK_DIR = DOCS_DIR / "source/benchmarking"
        METRICS_DIR = DATA_DIR / "metrics"

        ONTOLOGIES_DIR.mkdir(parents=True, exist_ok=True)
        DATASET_DIR.mkdir(parents=True, exist_ok=True)
        BENCHMARK_DIR.mkdir(parents=True, exist_ok=True)
        METRICS_DIR.mkdir(parents=True, exist_ok=True)

        processor = Processor(datasets_dir=DATASET_DIR, templates_dir=TEMPLATES_DIR, benchmark_dir=BENCHMARK_DIR, metrics_dir=METRICS_DIR)

        # todo_ontologies = [
        #     # YAGO(),
        #     # NCIt(),
        #     # PRotein(),
        # ]

        ontologies = [
            # # Agricultural Ontologies
            # AGROVOC(),
            # FoodOn(),
            # PO(),

            # # Arts and Humanities Ontologies
            # ChordOntology(),
            # ICON(),
            # MusicOntology(),
            # Nomisma(),
            # TimelineOntology(),

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

            # # Ecology & Environment Ontologies
            # ENVO(),
            # OEO(),
            # SWEET(),

            # # Education Ontologies
            # BIBFRAME(),
            # Common(),
            # DoCO(),

            # # Event Ontologies
            # ConferenceOntology(),
            # iCalendar(),
            # LODE(),

            # # Finance Ontologies
            # GoodRelations(),

            # # Food & Beverage Ontologies
            # Wine(),

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
            # # (YAGO(),  # large

            # # Geography Ontologies
            # GEO(),
            # GeoNames(),
            # GTS(),
            # Juso(),

            # # Industry
            # AUTO(),
            # DBO(),
            # DOAP(),
            # IOF(),
            # PTO(),
            # TUBES(),

            # # Law Ontologies
            # CopyrightOnto(),

            # # Library & Cultural Heritage
            # GND(),

            # # Livestock Ontologies
            # ATOL(),

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
            # MMO(),
            # MatOnto(),
            # MatVoc(),
            # MatWerk(),
            # MDO(),
            # MDS(),
            # MechanicalTesting(),
            # MicroStructures(),
            # MOLBRINELL(),
            # MOLTENSILE(),
            # MSEO(),
            # MSLE(),
            # NanoMine(),
            # OIECharacterisation(),
            # OIEManufacturing(),
            # OIEMaterials(),
            # OIEModels(),
            # OIESoftware(),
            # # OntoCAPE(language='en', base_dir=str(ONTOLOGIES_DIR / "materials_science_&_engineering")), "materials_science_and_engineering/OntoCAPE/OntoCAPE.owl"),
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

            # # Medicine Ontologies
            # BTO(),
            # DEB(),
            # DOID(),
            # ENM(),
            # MFOEM(),
            # # (NCIt(),  #large
            # OBI(),
            # # (PRotein(),  #large

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

            # # Social Sciences
            # AS2(),
            # BIO(),
            # Contact(),
            # FOAF(),
            # SIOC(),

            # # Units and Measurements
            # OM(),
            # OWLTime(),
            # QUDT(),
            # QUDV(),
            # UO(),

            # # Upper Ontologies
            # BFO(),
            # DOLCE(),
            # FAIR(),
            # GFO(),
            # SIO(),
            # SUMO(),

            # # Web Ontologies
            # Hydra(),
            # SAREF(),
        ]

        # Process each ontology
        for ontology in ontologies:
            ontology_path = ONTOLOGIES_DIR / ontology.domain.lower().replace(' ', '_') / f"{ontology.ontology_id.lower()}.{ontology.format.lower()}"

            metrics: OntologyMetrics = processor.process_ontology(
                ontology=ontology,
                ontology_path=ontology_path
            )

            if metrics:
                logger.info(f"\n{'=' * 20} {ontology.ontology_id} Metrics {'=' * 20}")
                logger.info("Basic graph metrics:")
                logger.info(f"Total nodes: {metrics.topology.total_nodes}")
                logger.info(f"Total edges: {metrics.topology.total_edges}")
                logger.info(f"Graph density: {metrics.topology.num_root_nodes}")
                logger.info(f"Number of leaf nodes: {metrics.topology.num_leaf_nodes}")

                logger.info("Knowledge coverage:")
                logger.info(f"Number of classes: {metrics.topology.num_classes}")
                logger.info(f"Number of properties: {metrics.topology.num_properties}")
                logger.info(f"Number of individuals: {metrics.topology.num_individuals}")

                logger.info("Hierarchical metrics:")
                logger.info(f"Maximum depth: {metrics.topology.max_depth}")
                logger.info(f"Minimum depth: {metrics.topology.min_depth}")
                logger.info(f"Average depth: {metrics.topology.avg_depth:.2f}")
                logger.info(f"Depth variance: {metrics.topology.depth_variance:.2f}")

                logger.info("Breadth metrics:")
                logger.info(f"Maximum breadth: {metrics.topology.max_breadth}")
                logger.info(f"Minimum breadth: {metrics.topology.min_breadth}")
                logger.info(f"Average breadth: {metrics.topology.avg_breadth:.2f}")
                logger.info(f"Breadth variance: {metrics.topology.breadth_variance:.2f}")

                logger.info("Dataset metrics:")
                logger.info(f"Number of term types: {metrics.dataset.num_term_types}")
                logger.info(f"Number of taxonomic relations: {metrics.dataset.num_taxonomic_relations}")
                logger.info(f"Number of non-taxonomic relations: {metrics.dataset.num_non_taxonomic_relations}")
                logger.info(f"Average terms per type: {metrics.dataset.avg_terms:.2f}")
                logger.info("=" * 60 + "\n")

        processor.export_metrics_to_excel()

    except Exception as e:
        logger.error(f"Main execution failed: {e}")
        raise

if __name__ == "__main__":
    main()
