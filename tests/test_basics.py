import unittest
import ontolearner

class TestOntoLearnerVersion(unittest.TestCase):
    def test_version_is_string(self):
        self.assertIsInstance(ontolearner.__version__, str)
        self.assertTrue(len(ontolearner.__version__) > 0, "Version string should not be empty")

if __name__ == '__main__':
    unittest.main()
