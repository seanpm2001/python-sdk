import unittest
from src.dopplersdk.models.UnlockRequest import UnlockRequest


class TestUnlockRequestModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_unlock_request(self):
        # Create UnlockRequest class instance
        test_model = UnlockRequest(config="delectus", project="aperiam")
        self.assertEqual(test_model.config, "delectus")
        self.assertEqual(test_model.project, "aperiam")

    def test_unlock_request_required_fields_missing(self):
        # Assert UnlockRequest class generation fails without required fields
        with self.assertRaises(TypeError):
            test_model = UnlockRequest()


if __name__ == "__main__":
    unittest.main()
