import unittest
from src.dopplersdk.models.ListPermissionsResponse import ListPermissionsResponse


class TestListPermissionsResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_list_permissions_response(self):
        # Create ListPermissionsResponse class instance
        test_model = ListPermissionsResponse(permissions=["libero", "officiis"])
        self.assertEqual(test_model.permissions, ["libero", "officiis"])


if __name__ == "__main__":
    unittest.main()
