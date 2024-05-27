import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @parameterized.expand([
        ("google", {"login": "google", "id": 1}),
        ("abc", {"login": "abc", "id": 2}),
    ])
    @patch('client.GithubOrgClient._get')
    def test_org(self, org_name, expected_response, mock_get):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get.return_value = expected_response

        client = GithubOrgClient(org_name)
        org = client.get_org()

        self.assertEqual(org, expected_response)
        mock_get.assert_called_once_with("")

if __name__ == "__main__":
    unittest.main()

