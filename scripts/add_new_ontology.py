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
        ONTOLOGY_DIR = DATA_DIR / "ontologies"
        DATASET_DIR = DATA_DIR / "datasets"
        TEMPLATES_DIR = DOCS_DIR / "source/_templates"
        BENCHMARK_DIR = DOCS_DIR / "source/benchmarking"
        METRICS_DIR = DATA_DIR / "metrics"

        ONTOLOGY_DIR.mkdir(parents=True, exist_ok=True)
        DATASET_DIR.mkdir(parents=True, exist_ok=True)
        BENCHMARK_DIR.mkdir(parents=True, exist_ok=True)
        METRICS_DIR.mkdir(parents=True, exist_ok=True)

        processor = Processor(datasets_dir=DATASET_DIR, templates_dir=TEMPLATES_DIR, benchmark_dir=BENCHMARK_DIR, metrics_dir=METRICS_DIR)

        large_ontologies = [
            # (YAGO(), "general_knowledge/yago_facts.ttl"),
            # (BattINFO(), "materials_science_&_engineering/battinfo.ttl"),
            # (PRIMA(), "materials_science_&_engineering/prima.ttl"),  # large
            # (NCIt(), "medicine/ncit.owl"),
            # (PRotein(), "medicine/protein.rdf"),
        ]

        # ontologies = [
        #     # Agricultural Ontologies
        #     (FoodOn(), "agricultural/foodon.owl"),
        #     (AGROVOC(), "agricultural/AGROVOC.rdf"),
        #     (PO(), "agricultural/plant.owl"),
        #
        #     # Arts and Humanities Ontologies
        #     (ChordOntology(), "arts_&_humanities/chord.rdf"),
        #     (ICON(), "arts_&_humanities/icon.owl"),
        #     (MusicOntology(), "arts_&_humanities/music.rdf"),
        #     (Nomisma(), "arts_&_humanities/nomisma.ttl"),
        #     (TimelineOntology(), "arts_&_humanities/timeline.rdf"),
        #
        #     # # Biology & Life Sciences Ontologies
        #     (BioPAX(), "biology_&_life_sciences/biopax.owl"),
        #     (EFO(), "biology_&_life_sciences/efo.owl"),
        #     (GO(), "biology_&_life_sciences/gene.owl"),
        #     (LIFO(), "biology_&_life_sciences/life.owl"),
        #     (MarineTLO(), "biology_&_life_sciences/marine_tlo.owl"),
        #     (MGED(), "biology_&_life_sciences/mged.owl"),
        #     (Microscopy(), "biology_&_life_sciences/pmd_mo.ttl"),
        #     (NPO(), "biology_&_life_sciences/npo_asserted.owl"),
        #     (PATO(), "biology_&_life_sciences/pato.owl"),
        #
        #     # # Chemistry Ontologies
        #     (AFO(), "chemistry/afo.ttl"),
        #     (ChEBI(), "chemistry/chebi.owl"),
        #     (CHEMINF(), "chemistry/cheminf.owl"),
        #     (CHIRO(), "chemistry/chiro.owl"),
        #     (ChMO(), "chemistry/ChMO.owl"),
        #     (FIX(), "chemistry/fix.owl"),
        #     (MassSpectrometry(), "chemistry/mass_spectrometry.owl"),
        #     (MOP(), "chemistry/mop.owl"),
        #     (NMRCV(), "chemistry/NMRCV.owl"),
        #     (OntoKin(), "chemistry/ontokin.owl"),
        #     (PROCO(), "chemistry/proco.owl"),
        #     (PSIMOD(), "chemistry/psi-mod.owl"),
        #     (REX(), "chemistry/rex.owl"),
        #     (RXNO(), "chemistry/rxno.owl"),
        #     (VIBSO(), "chemistry/vibso.owl"),
        #
        #     # Ecology & Environment Ontologies
        #     (ENVO(), "ecology_&_environment/envo.owl"),
        #     (OEO(), "ecology_&_environment/oeo.owl"),
        #     (SWEET(), "ecology_&_environment/sweet.owl"),
        #
        #     # Education Ontologies
        #     (BIBFRAME(), "education/bibframe.rdf"),
        #     (Common(), "education/common.rdf"),
        #     (DoCO(), "education/doco.rdf"),
        #
        #     # # Event Ontologies
        #     (ConferenceOntology(), "events/conference.owl"),
        #     (iCalendar(), "events/icalendar.rdf"),
        #     (LODE(), "events/lode.rdf"),
        #
        #     # Finance Ontologies
        #     (GoodRelations(), "finance/good_relations.owl"),
        #
        #     # Food & Beverage Ontologies
        #     (Wine(), "food_&_beverage/wine.rdf"),
        #
        #     # # General Knowledge Ontologies
        #     (CCO(), "general_knowledge/cco.ttl"),
        #     (DBpedia(), "general_knowledge/dbpedia.owl"),
        #     (DublinCore(), "general_knowledge/dublin_core.rdf"),
        #     (EDAM(), "general_knowledge/edam.owl"),
        #     (GIST(), "general_knowledge/gist.rdf"),
        #     (IAO(), "general_knowledge/iao.owl"),
        #     (PROV(), "general_knowledge/prov.owl"),
        #     (RO(), "general_knowledge/ro.owl"),
        #     (SchemaOrg(), "general_knowledge/schema_org.owl"),
        #     (UMBEL(), "general_knowledge/umbel.n3"),
        #     # (YAGO(), "general_knowledge/yago_facts.ttl"),  # large
        #
        #     # Geography Ontologies
        #     (GEO(), "geography/geo.owl"),
        #     (GeoNames(), "geography/geonames.rdf"),
        #     (GTS(), "geography/gts.ttl"),
        #     (Juso(), "geography/juso.ttl"),
        #
        #     # Industry
        #     (AUTO(), "industry/auto.rdf"),
        #     (DBO(), "industry/dbo.rdf"),
        #     (DOAP(), "industry/doap.rdf"),
        #     (IOF(), "industry/iof.rdf"),
        #     (PTO(), "industry/pto.rdf"),
        #     (TUBES(), "industry/tubes.rdf"),
        #
        #     # Law Ontologies
        #     (CopyrightOnto(), "law/copyright.ttl"),
        #
        #     # Library & Cultural Heritage
        #     (GND(), "library_&_cultural_heritage/gnd.rdf"),
        #
        #     # Livestock Ontologies
        #     (ATOL(), "livestock/atol.owl"),
        #
        #     # Materials Science & Engineering
        #     (AMOntology(), "materials_science_&_engineering/am_ontology.ttl"),
        #     (ASMO(), "materials_science_&_engineering/asmo.owl"),
        #     (Atomistic(), "materials_science_&_engineering/atomistic.ttl"),
        #     # (BattINFO(), "materials_science_&_engineering/battinfo.ttl"),  # large
        #     (BMO(), "materials_science_&_engineering/bmo.ttl"),
        #     (BVCO(), "materials_science_&_engineering/bvco.ttl"),
        #     (CDCO(), "materials_science_&_engineering/cdco.owl"),
        #     (CHAMEO(), "materials_science_&_engineering/chameo.ttl"),
        #     (CIFCore(), "materials_science_&_engineering/cif_core.ttl"),
        #     (CMSO(), "materials_science_&_engineering/cmso.owl"),
        #     (EMMOCrystallography(), "materials_science_&_engineering/crystallography.ttl"),
        #     (DISO(), "materials_science_&_engineering/diso.owl"),
        #     (DSIM(), "materials_science_&_engineering/dsim.owl"),
        #     (EMMO(), "materials_science_&_engineering/emmo.owl"),
        #     (FSO(), "materials_science_&_engineering/fso.ttl"),
        #     (GPO(), "materials_science_&_engineering/gpo.ttl"),
        #     (HPOnt(), "materials_science_&_engineering/heat_pump.owl"),
        #     (LDO(), "materials_science_&_engineering/ldo.owl"),
        #     (LPBFO(), "materials_science_&_engineering/lpbfo.owl"),
        #     (MAMBO(), "materials_science_&_engineering/mambo.owl"),
        #     (MAT(), "materials_science_&_engineering/mat.rdf"),
        #     (MaterialInformation(), "materials_science_&_engineering/material_information.owl"),
        #     (MMO(), "materials_science_&_engineering/mmo.rdf"),
        #     (MatOnto(), "materials_science_&_engineering/materials_ontology.owl"),
        #     (MatVoc(), "materials_science_&_engineering/matvoc.rdf"),
        #     (MatWerk(), "materials_science_&_engineering/mwo.ttl"),
        #     (MDO(), "materials_science_&_engineering/mdo.owl"),
        #     (MDS(), "materials_science_&_engineering/mds.ttl"),
        #     (MechanicalTesting(), "materials_science_&_engineering/mechanical_testing.owl"),
        #     (MicroStructures(), "materials_science_&_engineering/microstructure.owl"),
        #     (MOLBRINELL(), "materials_science_&_engineering/molbrinell.ttl"),
        #     (MOLTENSILE(), "materials_science_&_engineering/moltensile.rdf"),
        #     (MSEO(), "materials_science_&_engineering/mseo.ttl"),
        #     (MSLE(), "materials_science_&_engineering/msle.ttl"),
        #     (NanoMine(), "materials_science_&_engineering/nanomine.ttl"),
        #     (OIEManufacturing(), "materials_science_&_engineering/oie-manufacturing.ttl"),
        #     (OIEMaterials(), "materials_science_&_engineering/oie-materials.ttl"),
        #     (OIESoftware(), "materials_science_&_engineering/oie-software.ttl"),
        #     (OIEModels(), "materials_science_&_engineering/oie-models.ttl"),
        #     (OntoCAPE(language='en', base_dir=str(ONTOLOGY_DIR / "materials_science_&_engineering")), "materials_science_&_engineering/OntoCAPE/OntoCAPE.owl"),
        #     (ONTORULE(), "materials_science_&_engineering/ontorule.ttl"),
        #     (PeriodicTable(), "materials_science_&_engineering/periodic-table.owl"),
        #     (Photovoltaics(), "materials_science_&_engineering/photovoltaics.ttl"),
        #     (PLDO(), "materials_science_&_engineering/pldo.owl"),
        #     (PMDco(), "materials_science_&_engineering/pmdco.owl"),
        #     (PODO(), "materials_science_&_engineering/podo.owl"),
        #     # (PRIMA(), "materials_science_&_engineering/prima.ttl"),  # large
        #     (SSN(), "materials_science_&_engineering/ssn.ttl"),
        #     (SystemCapabilities(), "materials_science_&_engineering/system_capabilities.owl"),
        #     (VIMMP(), "materials_science_&_engineering/vimmp.owl"),
        #
        #     # Medicine Ontologies
        #     (BTO(), "medicine/bto.owl"),
        #     (DEB(), "medicine/deb.owl"),
        #     (DOID(), "medicine/doid.owl"),
        #     (ENM(), "medicine/enm.owl"),
        #     (MFOEM(), "medicine/mfoem.owl"),
        #     # (NCIt(), "medicine/ncit.owl"),  # large
        #     (OBI(), "medicine/obi.owl"),
        #     # (PRotein(), "medicine/protein.rdf"),  # large
        #
        #     # News & Media Ontologies
        #     (BBC(), "news_&_media/bbc.ttl"),
        #     (BBCBusiness(), "news_&_media/business.ttl"),
        #     (BBCCMS(), "news_&_media/cms.ttl"),
        #     (BBCCoreConcepts(), "news_&_media/core_concepts.ttl"),
        #     (BBCCreativeWork(), "news_&_media/creative_work.ttl"),
        #     (BBCFood(), "news_&_media/food.ttl"),
        #     (BBCPolitics(), "news_&_media/politics.ttl"),
        #     (BBCProgrammes(), "news_&_media/programmes.ttl"),
        #     (BBCProvenance(), "news_&_media/provenance.ttl"),
        #     (BBCSport(), "news_&_media/sport.ttl"),
        #     (BBCStoryline(), "news_&_media/storyline.ttl"),
        #     (BBCWildlife(), "news_&_media/wildlife.ttl"),
        #
        #     # Scholarly Knowledge Ontologies
        #     (AIISO(), "scholarly_knowledge/aiiso.rdf"),
        #     (CiTO(), "scholarly_knowledge/cito.owl"),
        #     (CSO(), "scholarly_knowledge/cso.owl"),
        #     (DataCite(), "scholarly_knowledge/datacite.rdf"),
        #     (DCAT(), "scholarly_knowledge/dcat.rdf"),
        #     (DUO(), "scholarly_knowledge/duo.owl"),
        #     (EURIO(), "scholarly_knowledge/eurio.rdf"),
        #     (EXPO(), "scholarly_knowledge/expo.owl"),
        #     (FRAPO(), "scholarly_knowledge/frapo.rdf"),
        #     (FRBRoo(), "scholarly_knowledge/frbroo.rdf"),
        #     (LexInfo(), "scholarly_knowledge/lexinfo.rdf"),
        #     # (M4I(), "scholarly_knowledge/metadata4ing.ttl"),
        #     (Metadata4Ing(), "scholarly_knowledge/metadata4ing.ttl"),
        #     (NFDIcore(), "scholarly_knowledge/nfdi.owl"),
        #     (OBOE(), "scholarly_knowledge/oboe.owl"),
        #     (OPMW(), "scholarly_knowledge/opmw.owl"),
        #     (PPlan(), "scholarly_knowledge/pplan.owl"),
        #     (PreMOn(), "scholarly_knowledge/premon.owl"),
        #     (SEPIO(), "scholarly_knowledge/sepio.owl"),
        #     (SPDocument(), "scholarly_knowledge/sp_document.owl"),
        #     (SPWorkflow(), "scholarly_knowledge/sp_workflow.owl"),
        #     (SWO(), "scholarly_knowledge/swo.owl"),
        #     (TribAIn(), "scholarly_knowledge/tribain.ttl"),
        #     (VOAF(), "scholarly_knowledge/voaf.rdf"),
        #     (WiLD(), "scholarly_knowledge/wild.ttl"),
        #
        #     # Social Sciences
        #     (AS2(), "social_sciences/as2.ttl"),
        #     (BIO(), "social_sciences/bio.rdf",),
        #     (Contact(), "social_sciences/contact.rdf"),
        #     (FOAF(), "social_sciences/foaf.rdf"),
        #     (SIOC(), "social_sciences/sioc.rdf"),
        #
        #     # # Units and Measurements
        #     (OM(), "units_and_measurements/om.rdf"),
        #     (OWLTime(), "units_and_measurements/owl_time.ttl"),
        #     (QUDT(), "units_and_measurements/qudt.ttl"),
        #     (QUDV(), "units_and_measurements/qudv.owl"),
        #     (UO(), "units_and_measurements/uo.owl"),
        #
        #     # Upper Ontologies
        #     (BFO(), "upper_ontologies/bfo.owl"),
        #     (DOLCE(), "upper_ontologies/dolce.owl"),
        #     (FAIR(), "upper_ontologies/fair.owl"),
        #     (GFO(), "upper_ontologies/gfo.owl"),
        #     (SIO(), "upper_ontologies/sio.owl"),
        #     (SUMO(), "upper_ontologies/sumo.owl"),
        #
        #     # Web Ontologies
        #     (Hydra(), "web_&_internet/hydra.jsonld"),
        #     (SAREF(), "web_&_internet/saref.rdf"),
        # ]

        # Process each ontology
        for ontology, filename in large_ontologies:
            ontology_path = ONTOLOGY_DIR / filename

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
