import unittest
from inquisitor import Inquisitor, ApiException
from tests.mock import *


class ApiCase(unittest.TestCase):
    def test_init(self):
        self.assertRaises(ValueError, Inquisitor, "")

    def setUp(self):
        self.authorized_api = Inquisitor("9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b")

    def test_datasets(self):
        with HTTMock(datasets_mock):
            self.assertEqual(list(self.authorized_api.datasets(page=1)), load_mock_json("datasets", True)["results"])
        with HTTMock(datasets_mock):
            self.assertEqual(
                list(self.authorized_api.datasets(page=1, dataset="ENPR_PSEDUC")),
                load_mock_json("dataset_filter", True)["results"]
            )

    def test_sources(self):
        with HTTMock(sources_mock):
            self.assertEqual(list(self.authorized_api.sources(page=1)), load_mock_json("sources", True)["results"])


if __name__ == '__main__':
    unittest.main()
