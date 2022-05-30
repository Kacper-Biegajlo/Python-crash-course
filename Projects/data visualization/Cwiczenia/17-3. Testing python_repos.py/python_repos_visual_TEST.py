import unittest
import python_repos_visual as prv

class Test_prv(unittest.TestCase):

    def setUp(self):
        """Call all the functions here, and test elements separately."""
        self.r = prv.get_api_response()
        self.repo_dicts = prv.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.repo_links, self.stars, self.labels = prv.get_data(
                self.repo_dicts)

    def test_status_code(self):
        """Test to see if we get status code 200."""
        self.assertEqual(self.r.status_code, 200)

    def test_repo_dicts(self):
        """Test to see if we get dictionaries for 30 repositories."""
        self.assertEqual(len(self.repo_dicts), 30)

    def test_items_returned(self):
        """Test to if each respositiory has a key."""
        for self.repo_dict in self.repo_dicts:
            self.assertTrue('name' in self.repo_dict.keys())
            self.assertTrue('html_url' in self.repo_dict.keys())
            self.assertTrue('owner' in self.repo_dict.keys())
            self.assertTrue('stargazers_count' in self.repo_dict.keys())

if __name__ == '__main__':
    unittest.main()