import unittest
from src.dopplersdk.models.AddTrustedIpResponse import AddTrustedIpResponse


class TestAddTrustedIpResponseModel(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_add_trusted_ip_response(self):
        # Create AddTrustedIpResponse class instance
        test_model = AddTrustedIpResponse(ip="laboriosam")
        self.assertEqual(test_model.ip, "laboriosam")


if __name__ == "__main__":
    unittest.main()
