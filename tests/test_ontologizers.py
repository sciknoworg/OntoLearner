import unittest
from ontolearner.ontology import (ChordOntology, AGROVOC, PO, ICON, LIFO, MOP, SWEET, PROV, DBO, CopyrightOnto,
                                  BIBFRAME, Conference, GoodRelations, Wine, GeoNames, Atomistic, DOID,
                                  BBC, CSO, FOAF, OWLTime, BFO, SAREF)
import inspect
import ontolearner.ontology as ontology_module
from ontolearner import AutoOntology

class TestOntologizers(unittest.TestCase):

    def setUp(self):
        self.ontologies = [
            [ChordOntology(), "ChordOntology"],
            [AGROVOC(), "AGROVOC"],
            [PO(), "PO"],
            [ICON(), "ICON"],
            [LIFO(), "LIFO"],
            [MOP(), "MOP"],
            [SWEET(), "SWEET"],
            [BIBFRAME(), "BIBFRAME"],
            [Conference(), "Conference"],
            [GoodRelations(), "GoodRelations"],
            [Wine(), "Wine"],
            [PROV(), "PROV"],
            [GeoNames(), "GeoNames"],
            [DBO(), "DBO"],
            [CopyrightOnto(), "CopyrightOnto"],
            [Atomistic(), "Atomistic"],
            [DOID(), "DOID"],
            [BBC(), "BBC"],
            [CSO(), "CSO"],
            [FOAF(), "FOAF"],
            [OWLTime(), "OWLTime"],
            [BFO(), "BFO"],
            [SAREF(), "SAREF"]
        ]

    def test_metadata(self):
        for ontology in self.ontologies:
            self.assertEqual(ontology[0].ontology_id, ontology[1])

    def test_ontologizers(self):
        for name, obj in inspect.getmembers(ontology_module):
            # Filter: only classes that are subclasses of some OntologyBase
            if inspect.isclass(obj):
                # Optionally filter only ontology classes by name or base class
                if hasattr(obj, 'load') and callable(getattr(obj, 'load')) and hasattr(obj, 'ontology_id'):
                    instance = obj()
                    if "BaseOntology" not in str(obj):
                        self.assertEqual(str(obj).split("'")[-2].split(".")[-1], instance.ontology_id)

    def test_autoontologizer(self):
        self.assertEqual(AutoOntology(ontology_id="bfo").ontology_id, "BFO")


if __name__ == "__main__":
    unittest.main()
