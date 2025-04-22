import logging
from pathlib import Path

from ontolearner import ProcessorPipeline
from ontolearner.data_structure import OntologyMetrics
from ontolearner.ontology import *  # noqa


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    try:
        # Define paths
        DATA_DIR = Path("data")
        DOCS_DIR = Path("docs")
        ONTOLOGY_DIR = DATA_DIR / "ontologies"
        DATASET_DIR = DATA_DIR / "datasets"
        BENCHMARK_DIR = DOCS_DIR / "source/benchmarking"

        # Initialize processor
        processor = ProcessorPipeline(datasets_dir=DATASET_DIR, docs_dir=BENCHMARK_DIR)

        # Define ontologies to process
        ontologies = [
            # # Agricultural Ontologies
            # (FoodOn(), "agricultural/foodon.owl", "foodon ontology"),  # noqa: F405
            # (AGROVOC(), "agricultural/AGROVOC.rdf", "agrovoc ontology"),  # noqa: F405
            # (PO(), "agricultural/plant.owl", "plant ontology"),  # noqa: F405

            # # Arts and Humanities Ontologies
            # (ChordOntology(), "arts_&_humanities/chord.rdf", "chord ontology"),  # noqa: F405
            # (ICON(), "arts_&_humanities/icon.owl", "icon ontology"),  # noqa: F405
            # (MusicOntology(), "arts_&_humanities/music.rdf", "music ontology"),  # noqa: F405
            # (Nomisma(), "arts_&_humanities/nomisma.ttl", "nomisma ontology"),  # noqa: F405
            # (TimelineOntology(), "arts_&_humanities/timeline.rdf", "timeline ontology"),  # noqa: F405

            # # Biology & Life Sciences Ontologies
            # (BioPAX(), "biology_&_life_sciences/biopax.owl", "biopax ontology"),  # noqa: F405
            # (EFO(), "biology_&_life_sciences/efo.owl", "efo ontology"),  # noqa: F405
            # (GO(), "biology_&_life_sciences/gene.owl", "gene ontology"),  # noqa: F405
            # (LIFO(), "biology_&_life_sciences/life.owl", "life ontology"),  # noqa: F405
            # (MarineTLO(), "biology_&_life_sciences/marine_tlo.owl", "marinetlo ontology"),  # noqa: F405
            # (MGED(), "biology_&_life_sciences/mged.owl", "mged ontology"),  # noqa: F405
            # (Microscopy(), "biology_&_life_sciences/pmd_mo.ttl", "microscopy ontology"),  # noqa: F405
            # (NPO(), "biology_&_life_sciences/npo_asserted.owl", "npo ontology"),  # noqa: F405
            # (PATO(), "biology_&_life_sciences/pato.owl", "pato ontology"),  # noqa: F405

            # # Chemistry Ontologies
            # (AFO(), "chemistry/afo.ttl", "afo ontology"),  # noqa: F405
            # (ChEBI(), "chemistry/chebi.owl", "chebi ontology"),  # noqa: F405
            # (CHEMINF(), "chemistry/cheminf.owl", "cheminf ontology"),  # noqa: F405
            # (CHIRO(), "chemistry/chiro.owl", "chiro ontology"),  # noqa: F405
            # (ChMO(), "chemistry/ChMO.owl", "chmo ontology"),  # noqa: F405
            # (FIX(), "chemistry/fix.owl", "fix ontology"),  # noqa: F405
            # (MassSpectrometry(), "chemistry/mass_spectrometry.owl", "mass spectrometry ontology"),  # noqa: F405
            # (MOP(), "chemistry/mop.owl", "mop ontology"),  # noqa: F405
            # (NMRCV(), "chemistry/NMRCV.owl", "nmrcv ontology"),  # noqa: F405
            # (OntoKin(), "chemistry/ontokin.owl", "ontokin ontology"),  # noqa: F405
            # (PROCO(), "chemistry/proco.owl", "proco ontology"),  # noqa: F405
            # (PSIMOD(), "chemistry/psi-mod.owl", "psi-mod ontology"),  # noqa: F405
            # (REX(), "chemistry/rex.owl", "rex ontology"),  # noqa: F405
            # (RXNO(), "chemistry/rxno.owl", "rxno ontology"),  # noqa: F405
            # (VIBSO(), "chemistry/vibso.owl", "vibso ontology"),  # noqa: F405

            # # Ecology & Environment Ontologies
            # (ENVO(), "ecology_&_environment/envo.owl", "environment ontology"),  # noqa: F405
            # (OEO(), "ecology_&_environment/oeo.owl", "oeo ontology"),  # noqa: F405
            # (SWEET(), "ecology_&_environment/sweet.owl", "sweet ontology"),  # noqa: F405

            # # Education Ontologies
            # (BIBFRAME(), "education/bibframe.rdf", "bibframe ontology"),  # noqa: F405
            # (Common(), "education/common.rdf", "common ontology"),  # noqa: F405
            # (DoCO(), "education/doco.rdf", "doco ontology"),  # noqa: F405

            # # Event Ontologies
            # (ConferenceOntology(), "events/conference.owl", "conference ontology"),  # noqa: F405
            # (iCalendar(), "events/icalendar.rdf", "icalendar ontology"),  # noqa: F405
            # (LODE(), "events/lode.rdf", "lode ontology"),  # noqa: F405

            # # Finance Ontologies
            # (GoodRelations(), "finance/good_relations.owl", "good relations ontology"),  # noqa: F405

            # # Food & Beverage Ontologies
            # (Wine(), "food_&_beverage/wine.rdf", "wine ontology"),  # noqa: F405

            # # General Knowledge Ontologies
            # (CCO(), "general_knowledge/cco.ttl", "cco ontology"),  # noqa: F405
            # (DBpedia(), "general_knowledge/dbpedia.owl", "dbpedia ontology"),  # noqa: F405
            # (DublinCore(), "general_knowledge/dublin_core.rdf", "dublin core ontology"),  # noqa: F405
            # (EDAM(), "general_knowledge/edam.owl", "edam ontology"),  # noqa: F405
            # (GIST(), "general_knowledge/gist.rdf", "gist ontology"),  # noqa: F405
            # (IAO(), "general_knowledge/iao.owl", "iao ontology"),  # noqa: F405
            # (PROV(), "general_knowledge/prov.owl", "prov ontology"),  # noqa: F405
            # (RO(), "general_knowledge/ro.owl", "ro ontology"),  # noqa: F405
            # (SchemaOrg(), "general_knowledge/schema_org.owl", "schema org ontology"),  # noqa: F405
            # (UMBEL(), "general_knowledge/umbel.n3", "umbel ontology"),  # noqa: F405
            # (YAGO(), "general_knowledge/yago_facts.ttl", "yago ontology"),  # noqa: F405  # toto not working

            # # Geography Ontologies
            # (GEO(), "geography/geo.owl", "geo ontology"),  # noqa: F405
            # (GeoNames(), "geography/geonames.rdf", "geonames ontology"),  # noqa: F405
            # (GTS(), "geography/gts.ttl", "gts ontology"),  # noqa: F405
            # (Juso(), "geography/juso.ttl", "juso ontology"),  # noqa: F405

            # # Industry
            # (AUTO(), "industry/auto.rdf", "auto ontology"),  # noqa: F405
            # (DBO(), "industry/dbo.rdf", "dbo ontology"),  # noqa: F405
            # (DOAP(), "industry/doap.rdf", "doap ontology"),  # noqa: F405
            # (IOF(), "industry/iof.rdf", "iof ontology"),  # noqa: F405
            # (PTO(), "industry/pto.rdf", "pto ontology"),  # noqa: F405
            # (TUBES(), "industry/tubes.rdf", "tubes ontology"),  # noqa: F405

            # # Law Ontologies
            # (CopyrightOnto(), "law/copyright.ttl", "copyright ontology"),  # noqa: F405

            # # Library & Cultural Heritage
            # (GND(), "library_&_cultural_heritage/gnd.rdf", "gnd ontology"),  # noqa: F405

            # # Livestock Ontologies
            # (ATOL(), "livestock/atol.owl", "atol ontology"),  # noqa: F405

            # # Materials Science & Engineering
            # (AMOntology(), "materials_science_&_engineering/am_ontology.ttl", "AMO"),  # noqa: F405
            # (ASMO(), "materials_science_&_engineering/asmo.owl", "asmo"),   # noqa: F405
            # (Atomistic(), "materials_science_&_engineering/atomistic.ttl", "atomistic"),  # noqa: F405
            # # (BattINFO(), "materials_science_&_engineering/battinfo.ttl", "battinfo"),  # noqa: F405  # not done yet
            # (BMO(), "materials_science_&_engineering/bmo.ttl", "bmo"),  # noqa: F405
            # (BVCO(), "materials_science_&_engineering/bvco.ttl", "bvco"),  # noqa: F405
            # (CDCO(), "materials_science_&_engineering/cdco.owl", "cdco"),  # noqa: F405
            # (CHAMEO(), "materials_science_&_engineering/chameo.ttl", "chameo"),  # noqa: F405
            # (CIFCore(), "materials_science_&_engineering/cif_core.ttl", "cif"),  # noqa: F405
            # (CMSO(), "materials_science_&_engineering/cmso.owl", "cmso"),  # noqa: F405
            # (EMMOCrystallography(), "materials_science_&_engineering/crystallography.ttl", "emmo_crystallography"),  # noqa: F405
            # (DISO(), "materials_science_&_engineering/diso.owl", "diso"),  # noqa: F405
            # (DSIM(), "materials_science_&_engineering/dsim.owl", "dsim"),  # noqa: F405
            # (EMMO(), "materials_science_&_engineering/emmo.owl", "emmo"),  # noqa: F405
            # (FSO(), "materials_science_&_engineering/fso.ttl", "fso"),  # noqa: F405
            # (GPO(), "materials_science_&_engineering/gpo.ttl", "gpo"),  # noqa: F405
            # (HPOnt(), "materials_science_&_engineering/heat_pump.owl", "hp_ontology"),  # noqa: F405
            # (LDO(), "materials_science_&_engineering/ldo.owl", "ldo"),  # noqa: F405
            # (LPBFO(), "materials_science_&_engineering/lpbfo.owl", "lpbfo"),  # noqa: F405
            # (MAMBO(), "materials_science_&_engineering/mambo.owl", "mambo"),  # noqa: F405
            # (MAT(), "materials_science_&_engineering/mat.rdf", "mat"),  # noqa: F405
            # (MaterialInformation(), "materials_science_&_engineering/material_information.owl", "material_information"),  # noqa: F405
            # (MMO(), "materials_science_&_engineering/mmo.rdf", "mmo"),  # noqa: F405
            # (MatOnto(), "materials_science_&_engineering/materials_ontology.owl", "mat_ontology"),  # noqa: F405
            # (MatVoc(), "materials_science_&_engineering/matvoc.rdf", "matvoc"),  # noqa: F405
            # (MDO(), "materials_science_&_engineering/mdo.owl", "mdo"),  # noqa: F405
            # (MDS(), "materials_science_&_engineering/mds.ttl", "mds"),  # noqa: F405
            # (MechanicalTesting(), "materials_science_&_engineering/mechanical_testing.owl", "mechanical_testing"),  # noqa: F405
            # (MicroStructures(), "materials_science_&_engineering/microstructure.owl", "micro_structures"),  # noqa: F405
            # (MOLBRINELL(), "materials_science_&_engineering/molbrinell.ttl", "molbrinell"),  # noqa: F405
            # (MOLTENSILE(), "materials_science_&_engineering/moltensile.rdf", "moltensile"),  # noqa: F405
            # (MSEO(), "materials_science_&_engineering/mseo.ttl", "mseo"),  # noqa: F405
            # (MSLE(), "materials_science_&_engineering/msle.ttl", "msle"),  # noqa: F405
            # (NanoMine(), "materials_science_&_engineering/nanomine.ttl", "nanomine"),
            # (OIEManufacturing(), "materials_science_&_engineering/oie-manufacturing.ttl", "oie-manufacturing"),  # noqa: F405
            # (OIEMaterials(), "materials_science_&_engineering/oie-materials.ttl", "oie-materials"),  # noqa: F405
            # (OIESoftware(), "materials_science_&_engineering/oie-software.ttl", "oie-software"),  # noqa: F405
            # (OIEModels(), "materials_science_&_engineering/oie-models.ttl", "oie-models"),  # noqa: F405
            # (OntoCAPE(language='en', base_dir=str(ONTOLOGY_DIR / "materials_science_&_engineering")), "materials_science_&_engineering/OntoCAPE/OntoCAPE.owl", "cape"),  # noqa: F405
            # (ONTORULE(), "materials_science_&_engineering/ontorule.ttl", "ontorule"),  # noqa: F405
            # (PeriodicTable(), "materials_science_&_engineering/periodic-table.owl", "periodic-table"),  # noqa: F405
            # (Photovoltaics(), "materials_science_&_engineering/photovoltaics.ttl", "photovoltaics"),  # noqa: F405
            # (PLDO(), "materials_science_&_engineering/pldo.owl", "pldo"),  # noqa: F405
            # (PMDco(), "materials_science_&_engineering/pmdco.owl", "pmdco"),  # noqa: F405
            # (PODO(), "materials_science_&_engineering/podo.owl", "podo"),  # noqa: F405
            # # (PRIMA(), "materials_science_&_engineering/prima.ttl", "prima"),  # noqa: F405  # not done yet #
            # (SSN(), "materials_science_&_engineering/ssn.ttl", "ssn"),  # noqa: F405
            # (SystemCapabilities(), "materials_science_&_engineering/system_capabilities.owl", "system_capabilities"),  # noqa: F405
            # (VIMMP(), "materials_science_&_engineering/vimmp.owl", "vimmp"),  # noqa: F405

            # # Medicine Ontologies
            # (BTO(), "medicine/bto.owl", "bto ontology"),  # noqa: F405
            # (DEB(), "medicine/deb.owl", "deb ontology"),  # noqa: F405
            # (DOID(), "medicine/doid.owl", "doid ontology"),  # noqa: F405
            # (ENM(), "medicine/enm.owl", "enm ontology"),  # noqa: F405
            # (MFOEM(), "medicine/mfoem.owl", "MFOEM ontology"),  # noqa: F405
            # # (NCIt(), "medicine/ncit.owl", "ncit ontology"),  # noqa: F405  # not done yet #
            # (OBI(), "medicine/obi.owl", "obi ontology"),  # noqa: F405
            # # (PRotein(), "medicine/protein.rdf", "protein ontology"),  # noqa: F405  # not done yet #

            # # News & Media Ontologies
            # (BBC(), "news_&_media/bbc.ttl", "bbc"),  # noqa: F405
            # (BBCBusiness(), "news_&_media/business.ttl", "bbc business"),  # noqa: F405
            # (BBCCMS(), "news_&_media/cms.ttl", "bbc_cms"),  # noqa: F405
            # (BBCCoreConcepts(), "news_&_media/core_concepts.ttl", "bbc core concepts"),  # noqa: F405
            # (BBCCreativeWork(), "news_&_media/creative_work.ttl", "bbc creative work"),  # noqa: F405
            # (BBCFood(), "news_&_media/food.ttl", "bbc_food"),  # noqa: F405
            # (BBCPolitics(), "news_&_media/politics.ttl", "bbc journalism"),  # noqa: F405
            # (BBCProgrammes(), "news_&_media/programmes.ttl", "bbc programmes"),  # noqa: F405
            # (BBCProvenance(), "news_&_media/provenance.ttl", "bbc provenance"),  # noqa: F405
            # (BBCSport(), "news_&_media/sport.ttl", "bbc sport"),  # noqa: F405
            # (BBCStoryline(), "news_&_media/storyline.ttl", "bbc storyline"),  # noqa: F405
            # (BBCWildlife(), "news_&_media/wildlife.ttl", "bbc wildlife"),  # noqa: F405
            #
            # # Scholarly Knowledge Ontologies
            # (AIISO(), "scholarly_knowledge/aiiso.rdf", "aiiso"),  # noqa: F405
            # (CiTO(), "scholarly_knowledge/cito.owl", "cito"),  # noqa: F405
            # (CSO(), "scholarly_knowledge/cso.owl", "cso"),  # noqa: F405
            # (DataCite(), "scholarly_knowledge/datacite.rdf", "datacite"),  # noqa: F405
            # (DCAT(), "scholarly_knowledge/dcat.rdf", "dcat"),  # noqa: F405
            # (DUO(), "scholarly_knowledge/duo.owl", "duo"),  # noqa: F405
            # (EURIO(), "scholarly_knowledge/eurio.rdf", "eurio"),  # noqa: F405
            # (EXPO(), "scholarly_knowledge/expo.owl", "expo"),  # noqa: F405
            # (FRAPO(), "scholarly_knowledge/frapo.rdf", "frapo"),  # noqa: F405
            # (FRBRoo(), "scholarly_knowledge/frbroo.rdf", "frbroo"),  # noqa: F405
            # (LexInfo(), "scholarly_knowledge/lexinfo.rdf", "lexinfo"),  # noqa: F405
            # # (M4I(), "scholarly_knowledge/metadata4ing.ttl", "m4i"),  # noqa: F405
            # (Metadata4Ing(), "scholarly_knowledge/metadata4ing.ttl", "metadata4ing"),  # noqa: F405
            # (NFDIcore(), "scholarly_knowledge/nfdi.owl", "nfdi"),  # noqa: F405
            # (OBOE(), "scholarly_knowledge/oboe.owl", "oboe"),  # noqa: F405
            # (OPMW(), "scholarly_knowledge/opmw.owl", "opmw"),  # noqa: F405
            # (PPlan(), "scholarly_knowledge/pplan.owl", "pplan"),  # noqa: F405
            # (PreMOn(), "scholarly_knowledge/premon.owl", "premon"),  # noqa: F405
            # (SEPIO(), "scholarly_knowledge/sepio.owl", "sepio"),  # noqa: F405
            # (SPDocument(), "scholarly_knowledge/sp_document.owl", "sp document"),  # noqa: F405
            # (SPWorkflow(), "scholarly_knowledge/sp_workflow.owl", "sp workflow"),  # noqa: F405
            # (SWO(), "scholarly_knowledge/swo.owl", "swo"),  # noqa: F405
            # (TribAIn(), "scholarly_knowledge/tribain.ttl", "tribain"),  # noqa: F405
            # (VOAF(), "scholarly_knowledge/voaf.rdf", "voaf"),  # noqa: F405
            # (WiLD(), "scholarly_knowledge/wild.ttl", "wild"),   # noqa: F405

            # # Social Sciences
            # (AS2(), "social_sciences/as2.ttl", "as2"),  # noqa: F405
            # (BIO(), "social_sciences/bio.rdf", "bio"),  # noqa: F405
            # (Contact(), "social_sciences/contact.rdf", "contact"),  # noqa: F405
            # (FOAF(), "social_sciences/foaf.rdf", "foaf"),  # noqa: F405
            # (SIOC(), "social_sciences/sioc.rdf", "sioc"),  # noqa: F405

            # # Units and Measurements
            # (OM(), "units_and_measurements/om.rdf", "om"),  # noqa: F405
            # (OWLTime(), "units_and_measurements/owl_time.ttl", "time"),  # noqa: F405
            # (QUDT(), "units_and_measurements/qudt.ttl", "qudt"),  # noqa: F405
            # (QUDV(), "units_and_measurements/qudv.owl", "qudv"),  # noqa: F405
            # (UO(), "units_and_measurements/uo.owl", "uo"),  # noqa: F405

            # # Upper Ontologies
            # (BFO(), "upper_ontologies/bfo.owl", "bfo ontology"),  # noqa: F405
            # (DOLCE(), "upper_ontologies/dolce.owl", "dolce ontology"),  # noqa  # noqa: F405
            # (FAIR(), "upper_ontologies/fair.owl", "fair ontology"),  # noqa: F405
            # (GFO(), "upper_ontologies/gfo.owl", "gfo ontology"),  # noqa: F405
            # (SIO(), "upper_ontologies/sio.owl", "sio ontology"),  # noqa: F405
            # (SUMO(), "upper_ontologies/sumo.owl", "sumo ontology"),  # noqa: F405

            # # Web Ontologies
            # (Hydra(), "web_&_internet/hydra.jsonld", "hydra ontology"),  # noqa: F405
            # (SAREF(), "web_&_internet/saref.rdf", "saref ontology"),  # noqa: F405
        ]

        # Process each ontology
        for ontology, filename, identifier in ontologies:
            ontology_path = ONTOLOGY_DIR / filename

            metrics: OntologyMetrics = processor.process_ontology(
                ontology=ontology,
                ontology_path=ontology_path,
                ontology_identifier=identifier
            )

            if metrics:
                logger.info(f"\n{'=' * 20} {identifier.upper()} Metrics {'=' * 20}")

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

    except Exception as e:
        logger.error(f"Main execution failed: {e}")
        raise

if __name__ == "__main__":
    main()
