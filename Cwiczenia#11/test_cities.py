import unittest
from city_function import get_formatted_city_country

class CityTestCase(unittest.TestCase):
    """Test city_function.py"""

    def test_city_country(self):
        """Does function correctly forms a string of city and country?"""
        formatted_city = get_formatted_city_country('warsaw', 'poland')
        self.assertEqual(formatted_city, 'Warsaw, Poland.')

    def test_city_country_population(self):
        """Does function correctly forms a string of city, country and pop?"""
        formatted_city = get_formatted_city_country('london',\
 'england', '500000')
        self.assertEqual(formatted_city, 'London, England - population 500000.')

if __name__ == '__main__':
    unittest.main()