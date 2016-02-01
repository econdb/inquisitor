import unittest
from inquisitor import Inquisitor, ApiException
from tests.mock import *

class ApiCase(unittest.TestCase):
    def test_init(self):
        self.assertRaises(ValueError, Inquisitor, "")
        self.assertRaises(ValueError, Inquisitor, "wrongkey")

    def setUp(self):
        self.authorized_api = Inquisitor("9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b")

    def test_authorization(self):
        inquisitor = Inquisitor("9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b")
        with HTTMock(series_mock):
            self.assertEqual(list(inquisitor.series(1)), load_mock_json("series", True)["results"])
        inquisitor = Inquisitor("9000b09199c62bcf9418ad846dd0e4bbdfc6ee4b")
        with HTTMock(series_mock):
            with self.assertRaises(ApiException):
                list(inquisitor.series(1))

    def test_datasets(self):
        with HTTMock(datasets_mock):
            self.assertEqual(list(self.authorized_api.datasets(page=1)), load_mock_json("datasets", True)["results"])
        with HTTMock(datasets_mock):
            self.assertEqual(
                list(self.authorized_api.datasets(page=1, dataset="ENPR_PSEDUC")),
                load_mock_json("dateset_single", True)["results"]
            )

if __name__ == '__main__':
    unittest.main()
